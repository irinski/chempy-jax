#!/usr/bin/env python3

import sys
import os

# Load Chempy library from path in environment variable CHEMPY_PATH
chempy_path = os.environ.get('CHEMPY_PATH')
if chempy_path and chempy_path not in sys.path:
    sys.path.insert(0, chempy_path)

from Chempy.parameter import ModelParameters
from Chempy.solar_abundance import solar_abundances

def test_x():
  a = ModelParameters()
  basic_solar = solar_abundances()
  getattr(basic_solar, a.solar_abundance_name)()
  assert basic_solar.x == 0.7373977678803461
  assert basic_solar.y == 0.24923529618045798
