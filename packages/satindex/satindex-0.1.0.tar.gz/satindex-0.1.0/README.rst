########
satindex
########

.. begin-inclusion-intro-marker-do-not-remove

This package calculates several indexes based on multiband satellite images.

.. end-inclusion-intro-marker-do-not-remove


.. begin-inclusion-usage-marker-do-not-remove

How to use
----------

.. code-block:: python

   from satindex import SatelliteImage
   from satindex import example_data_path

   # load a rgbi geotif
   img = SatelliteImage(example_data_path)

   # save ndwi image to example_data/ndwi.tif
   img.save_ndwi(example_data_path.with_name("ndwi.tif"))

   # save ndvi image to example_data/ndvi.tif
   img.save_ndvi(example_data_path.with_name("ndvi.tif"))

   # get ndwi as numpy array
   ndwi = img.ndwi

.. end-inclusion-usage-marker-do-not-remove


.. begin-inclusion-installation-marker-do-not-remove

Installation
------------

To install satindex, do:

.. code-block:: console

  git clone https://gitlab.com/rwsdatalab/public/codebase/image/satindex.git
  cd satindex
  pip install .

Run tests (including coverage) with:

.. code-block:: console

  pip install -r requirements-dev.txt
  python setup.py test

.. end-inclusion-installation-marker-do-not-remove


Documentation
-------------

.. begin-inclusion-readme-marker-do-not-remove

Find the full documentation at https://rwsdatalab.gitlab.io/public/codebase/image/satindex


.. begin-inclusion-license-marker-do-not-remove

License
-------

Copyright (c) 2022, Rijkswaterstaat


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



.. end-inclusion-license-marker-do-not-remove
