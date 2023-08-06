__bibtex__ = """
@ARTICLE{pysyd,
       author = {{Chontos}, Ashley and {Huber}, Daniel and {Sayeed}, Maryum and {Yamsiri}, Pavadol},
        title = "{pySYD: Automated measurements of global asteroseismic parameters}",
      journal = {The Journal of Open Source Software},
     keywords = {Python, fundamental stellar properties, solar-like oscillations, stellar oscillations, stellar astrophysics, asteroseismology, astronomy, global asteroseismology, Astrophysics - Solar and Stellar Astrophysics, Astrophysics - Instrumentation and Methods for Astrophysics},
         year = 2022,
        month = nov,
       volume = {7},
       number = {79},
          eid = {3331},
        pages = {3331},
          doi = {10.21105/joss.03331},
archivePrefix = {arXiv},
       eprint = {2108.00582},
 primaryClass = {astro-ph.SR},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022JOSS....7.3331C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
__url__ = "https://pysyd.readthedocs.io"
__author__ = "Ashley Chontos<ashleychontos@astro.princeton.edu>"
__license__ = "MIT"
__description__ = "Automated measurements of global asteroseismic parameters"
__version__ = '0.10b1'

__all__ = ['cli','models','pipeline','plots','target','utils']

import os
import sys 

# Directory with personal pysyd data & info
_ROOT = os.path.abspath(os.getcwd())

# Package directory & data
PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))

# enforce python version
# (same as check at beginning of setup.py)

__minimum_python_version__ = "3.8"

class PythonNotSupportedError(Exception):
    pass

if sys.version_info < tuple((int(val) for val in __minimum_python_version__.split('.'))):
    raise PythonNotSupportedError(
        f"{__package__} does not support Python < {__minimum_python_version__}")