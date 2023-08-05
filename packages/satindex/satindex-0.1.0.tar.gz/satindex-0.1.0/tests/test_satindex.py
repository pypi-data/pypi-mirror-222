"""Tests for the satindex module."""

import pytest
import rasterio

from satindex import SatelliteImage


class TestSatelliteImage:
    def test_init(self, temp_rgbi):
        img = SatelliteImage(temp_rgbi)
        assert img

    def test_init_img_without_nir(self, caplog, temp_rgb):
        img_rgb = SatelliteImage(temp_rgb)
        assert (
            caplog.records[0].message
            == "Source file consists of 3 channels, expected 4."
        )

    def test_get_red(self, img):
        assert (img.red == [[10, 10], [20, 20]]).all()
        assert (img.red == [[10, 10], [20, 20]]).all()

    def test_get_green(self, img):
        assert (img.green == [[20, 20], [10, 10]]).all()
        assert (img.green == [[20, 20], [10, 10]]).all()

    def test_get_blue(self, img):
        assert (img.blue == [[10, 20], [10, 20]]).all()
        assert (img.blue == [[10, 20], [10, 20]]).all()

    def test_get_nir(self, img):
        assert (img.nir == [[1, 40], [1, 40]]).all()
        assert (img.nir == [[1, 40], [1, 40]]).all()

    def test_get_non_existing_band(self, img):
        with pytest.raises(IndexError):
            img._get_band(5)

    def test_get_non_existing_color(self, caplog, img_rgb):
        with pytest.raises(IndexError):
            img_rgb.nir

    def test_ndwi(self, img):
        ndwi = img.ndwi
        assert ndwi[0, 0] == (20 - 1) / (20 + 1)
        assert ndwi[1, 0] == (10 - 1) / (10 + 1)
        assert ndwi[0, 1] == (20 - 40) / (20 + 40)
        assert ndwi[1, 1] == (10 - 40) / (10 + 40)

    def test_ndvi(self, img):
        ndvi = img.ndvi
        assert ndvi[0, 0] == (1 - 10) / (1 + 10)
        assert ndvi[1, 0] == (1 - 20) / (1 + 20)
        assert ndvi[0, 1] == (40 - 10) / (40 + 10)
        assert ndvi[1, 1] == (40 - 20) / (40 + 20)

    def test_save_ndwi(self, img, tmp_path):
        index_path = tmp_path / "ndwi.tif"
        img.save_ndwi(index_path)
        with rasterio.open(index_path) as src:
            ndwi = src.read()
        assert ndwi[0, 0, 0] == pytest.approx((20 - 1) / (20 + 1))
        assert ndwi[0, 1, 0] == pytest.approx((10 - 1) / (10 + 1))
        assert ndwi[0, 0, 1] == pytest.approx((20 - 40) / (20 + 40))
        assert ndwi[0, 1, 1] == pytest.approx((10 - 40) / (10 + 40))

    def test_save_ndvi(self, img, tmp_path):
        index_path = tmp_path / "ndvi.tif"
        img.save_ndvi(index_path)
        with rasterio.open(index_path) as src:
            ndvi = src.read()
        assert ndvi[0, 0, 0] == pytest.approx((1 - 10) / (1 + 10))
        assert ndvi[0, 1, 0] == pytest.approx((1 - 20) / (1 + 20))
        assert ndvi[0, 0, 1] == pytest.approx((40 - 10) / (40 + 10))
        assert ndvi[0, 1, 1] == pytest.approx((40 - 20) / (40 + 20))
