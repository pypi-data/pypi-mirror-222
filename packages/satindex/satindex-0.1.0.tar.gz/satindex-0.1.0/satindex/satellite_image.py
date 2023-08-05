"""Calculate NDWI or NDVI indices based on 4-band satellite image."""

import logging
from pathlib import Path
from typing import Dict, Optional, Union

import numpy as np
import rasterio

logger = logging.getLogger(__name__)


class SatelliteImage:
    """Satellite image containing RGBI channels."""

    def __init__(
        self,
        source: Union[Path, str],
        channel_mapping: Optional[Dict[str, int]] = None,
        verbosity: int = logging.WARNING,
    ):
        """Satellite image for RGBI images.

        The satellite image class contains the channels of the satellite images as
        raster data. It allows calculating NDWI and NDVI indexes. Additionally, new
        rasters can be written to a geotif in the same projection and dimensions as the
        source image. It expects RGBI images from satellietdataportaal.nl.

        Parameters
        ----------
        source : str or Path
            Path to RGBI geotif sourcefile.
        channel_mapping : Dict[str, int]
            Dictionary mapping the colors to their corresponding geotif band. Default
            for satellietdataportaal RGBI data is:
            {"blue": 1, "green": 2, "red": 3, "nir": 4}
        verbosity : int
            Verbosity level as defined in logging. Can be logging.DEBUG,
            logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
        """
        self.source = Path(source)
        self._check_source(self.source)
        self._red: Optional[np.ndarray] = None
        self._green: Optional[np.ndarray] = None
        self._blue: Optional[np.ndarray] = None
        self._nir: Optional[np.ndarray] = None
        self.background_value = -1
        self._channel_mapping = channel_mapping or {
            "blue": 1,
            "green": 2,
            "red": 3,
            "nir": 4,
        }

        self.logging_verbosity = verbosity
        logger.setLevel(verbosity)

    def _check_source(self, source):
        """Check suitability of source for index calculation."""
        with rasterio.open(source) as src:
            channels = src.meta["count"]
            if channels != 4:
                logger.warning(
                    "Source file consists of %d channels, expected 4.", channels
                )

    @property
    def blue(self) -> np.ndarray:
        """Get the blue band.

        Returns
        -------
        np.ndarray
            2d array with blue band intensity values
        """
        if self._blue is None:
            self._blue = self._get_band(self._channel_mapping["blue"])
        return self._blue

    @property
    def green(self) -> np.ndarray:
        """Get the green band.

        Returns
        -------
        np.ndarray
            2d array with green band intensity values
        """
        if self._green is None:
            self._green = self._get_band(self._channel_mapping["green"])
        return self._green

    @property
    def red(self) -> np.ndarray:
        """Get the red band.

        Returns
        -------
        np.ndarray
            2d array with red band intensity values
        """
        if self._red is None:
            self._red = self._get_band(self._channel_mapping["red"])
        return self._red

    @property
    def nir(self) -> np.ndarray:
        """Get the near-infrared band.

        Returns
        -------
        np.ndarray[np.uint64]
            2d array with near-infrared band intensity values
        """
        if self._nir is None:
            try:
                self._nir = self._get_band(self._channel_mapping["nir"])
            except KeyError:
                raise IndexError(
                    "No mapping for nir was found in channel_mapping dictionary"
                )
        return self._nir

    @property
    def ndwi(self) -> np.ndarray:
        """Get normalized difference water index.

        The normalized difference water index is related to the water content
        of water bodies. It uses the green and nir bands according to the definition
        of McFeeters (1996):

            NDWI = (Xgreen - Xnir) / (Xgreen + Xnir)

        Returns
        -------
        np.ndarray[np.float]
            2d array with NDWI values

        """
        green = self.green.astype("float")
        nir = self.nir.astype("float")
        with np.errstate(invalid="ignore"):
            ndwi = (green - nir) / (green + nir)
        ndwi[np.isnan(ndwi)] = self.background_value
        return ndwi

    @property
    def ndvi(self) -> np.ndarray:
        """Get normalized difference vegetation index.

        The normalized difference vegetation index is used to assess the amount of
        vegetation on a per-pixel bases. It's defined as:

            NDVI = (Xnir - Xred) / (Xnir + Xred)

        Returns
        -------
        np.ndarray[np.float]
            2d array with NDVI values

        """
        red = self.red.astype("float")
        nir = self.nir.astype("float")
        with np.errstate(invalid="ignore"):
            ndvi = (nir - red) / (nir + red)
        ndvi[np.isnan(ndvi)] = self.background_value
        return ndvi

    def ndwi_mask(self, lower_thr: float = 0, upper_thr: float = 1) -> np.ndarray:
        """Get mask based on a threshold set for the normalized difference water index.

        Parameters
        ----------
        lower_thr: lower threshold
        upper_thr: upper threshold
        By default, values greater than 0 and smaller than or equal to 1
        are set to 1 to define areas within the mask.

        Returns
        -------
        np.ndarray[np.float]
            2d array with binary values

        """
        ndwi = self.ndwi
        mask = np.where((ndwi > lower_thr) & (ndwi <= upper_thr), 1, 0)
        return mask

    def ndvi_mask(self, lower_thr: float = 0, upper_thr: float = 1) -> np.ndarray:
        """Get mask based on a threshold set for the normalized difference vegetation index.

        Parameters
        ----------
        lower_thr: lower threshold
        upper_thr: upper threshold
        By default, values greater than 0 and smaller than or equal to 1
        are set to 1 to define areas within the mask.

        Returns
        -------
        np.ndarray[np.float]
            2d array with binary values

        """
        ndvi = self.ndvi
        mask = np.where((ndvi > lower_thr) & (ndvi <= upper_thr), 1, 0)
        return mask

    def save_ndwi(self, dest_path: Union[Path, str]):
        """Save NDWI values to a geotif.

        The resulting geotif has the same resolution and projection as the source
        rgbi geotif that the NDWI is based upon.

        Parameters
        ----------
        dest_path : Path
            Path to destination tif file. A different extension will be changed to .tif.
        """
        self._save_index(dest_path, self.ndwi)

    def save_ndvi(self, dest_path: Union[Path, str]):
        """Save NDVI values to a geotif.

        The resulting geotif has the same resolution and projection as the source
        rgbi geotif that the NDVI is based upon.

        Parameters
        ----------
        dest_path : Path
            Path to destination tif file. A different extension will be changed to .tif.
        """
        self._save_index(dest_path, self.ndvi)

    def _save_index(
        self,
        dest_path: Union[Path, str],
        index: np.ndarray,
    ):
        with rasterio.open(self.source) as src:
            meta = src.meta
        meta["dtype"] = rasterio.dtypes.float32
        meta["count"] = 1
        meta["nodata"] = self.background_value
        dest_path = Path(dest_path).with_suffix(".tif")
        with rasterio.open(
            dest_path, "w", **meta, BIGTIFF="YES", compress="lzw"
        ) as dst:
            dst.write(index, 1)

    def _get_band(self, band: int) -> np.ndarray:
        logger.info("reading band %d", band)
        with rasterio.open(self.source) as src:
            array = src.read(band)
        return array
