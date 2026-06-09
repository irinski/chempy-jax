#!/usr/bin/env python3

import sys
import os

# Load Chempy library from path in environment variable CHEMPY_PATH
chempy_path = os.environ.get('CHEMPY_PATH')
if chempy_path and chempy_path not in sys.path:
    sys.path.insert(0, chempy_path)

from Chempy.parameter import ModelParameters

def test_solar_abundance_name_list():
  a = ModelParameters()
  assert a.solar_abundance_name_list == ['Lodders09', 'Asplund09', 'Asplund05_pure_solar', 'Asplund05_apogee_correction', 'AG89']
