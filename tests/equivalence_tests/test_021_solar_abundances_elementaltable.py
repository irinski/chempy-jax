#!/usr/bin/env python3

import sys
import os
import numpy as np

# Load Chempy library from path in environment variable CHEMPY_PATH
chempy_path = os.environ.get('CHEMPY_PATH')
if chempy_path and chempy_path not in sys.path:
    sys.path.insert(0, chempy_path)

from Chempy.parameter import ModelParameters
from Chempy.solar_abundance import solar_abundances

def test_elemental_table():
    elemental_table = np.load(chempy_path + '/Chempy/input/elemental_table.npy')
    print("Fields:", elemental_table.dtype.names)
    print("Shape :", elemental_table.shape)
    print("Dtype :", elemental_table.dtype)
    print(elemental_table['Symbol'])
    assert elemental_table.shape == (116, )

test_elemental_table()   