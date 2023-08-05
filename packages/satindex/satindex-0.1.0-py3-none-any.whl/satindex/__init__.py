# -*- coding: utf-8 -*-
"""Documentation about satindex"""
import logging
import sys
from pathlib import Path

from satindex.satellite_image import SatelliteImage

logging.getLogger(__name__).addHandler(logging.NullHandler())
logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    format="%(asctime)s %(levelname)s: %(message)s",
)

__author__ = "RWS Datalab"
__email__ = "datalab.codebase@rws.nl"
__version__ = "0.1.0"

example_data_path = Path(__file__).parents[1] / "example_data/rgbi.tif"
