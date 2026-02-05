#!/usr/bin/env python3

import sys
import os

# Load Chempy library from path in environment variable CHEMPY_PATH
chempy_path = os.environ.get('CHEMPY_PATH')
if chempy_path and chempy_path not in sys.path:
    sys.path.insert(0, chempy_path)

from Chempy.parameter import ModelParameters
from Chempy.solar_abundance import solar_abundances
from Chempy.infall import PRIMORDIAL_INFALL
import numpy as np

def test_PRIMORDIAL_INFALL():
  a = ModelParameters()
  basic_solar = solar_abundances()
  solar_scaled_material = PRIMORDIAL_INFALL(list(basic_solar.all_elements),np.copy(basic_solar.table))
  solar_scaled_material.solar(-0.3)
  # print(repr(solar_scaled_material.fractions))
  # Or use: print(solar_scaled_material.fractions.tolist())
  expected_array = np.array([2.13963657e-01, 2.85000000e-01, 2.09025995e-04, 2.71398979e-04,
       3.25569808e-04, 3.61698390e-04, 4.21807292e-04, 4.81816815e-04,
       5.72160856e-04, 6.07705213e-04, 6.92329550e-04, 7.31937303e-04,
       8.12540407e-04, 8.45785852e-04, 9.32764938e-04, 9.65627222e-04,
       1.06765576e-03, 1.20302125e-03, 1.17743280e-03, 1.20693615e-03,
       1.35383291e-03, 1.44149940e-03, 1.53408698e-03, 1.56584592e-03,
       1.65444166e-03, 1.68175432e-03, 1.77475432e-03, 1.76753297e-03,
       1.91366747e-03, 1.96889779e-03, 2.09968585e-03, 2.18753037e-03,
       2.25624003e-03, 2.37785515e-03, 2.40628341e-03, 2.52354997e-03,
       2.57383547e-03, 2.63864828e-03, 2.67737124e-03, 2.74718159e-03,
       2.79784593e-03, 2.88980471e-03, 2.95123866e-03, 3.04369073e-03,
       3.09896623e-03, 3.20480427e-03, 3.24841635e-03, 3.38522132e-03,
       3.45770735e-03, 3.57491369e-03, 3.66676346e-03, 3.84263320e-03,
       3.82168753e-03, 3.95384671e-03, 4.00240518e-03, 4.13555869e-03,
       4.18309381e-03, 4.21954854e-03, 4.24338882e-03, 4.34380171e-03,
       4.36662863e-03, 4.52804332e-03, 4.57634727e-03, 4.73553347e-03,
       4.78598610e-03, 4.89363855e-03, 4.96682385e-03, 5.03695130e-03,
       5.08739971e-03, 5.21146587e-03, 5.26906923e-03, 5.37516927e-03,
       5.44918754e-03, 5.53628281e-03, 5.60756426e-03, 5.72871562e-03,
       5.78855349e-03, 5.78454824e-03, 5.93158524e-03, 6.04070371e-03,
       6.15493772e-03, 6.23976174e-03, 6.29337795e-03, 6.32408285e-03,
       6.32408285e-03, 6.62522965e-03, 6.71557369e-03, 6.80591773e-03,
       6.83603241e-03, 6.98775198e-03, 6.95757165e-03, 7.16816451e-03,
       7.13717921e-03, 7.34798198e-03, 7.31786730e-03, 7.43832602e-03,
       7.43832602e-03, 7.55878474e-03, 7.58889942e-03, 7.73947282e-03,
       7.76958750e-03, 7.79970218e-03, 7.89004622e-03, 7.85993154e-03,
       7.89004622e-03, 8.01050494e-03, 7.95027558e-03, 8.34176642e-03,
       8.07073430e-03, 8.16107834e-03, 8.19119302e-03, 8.58268387e-03,
       8.55256919e-03, 8.70314259e-03, 8.67302791e-03, 8.79348663e-03])

  assert np.allclose(solar_scaled_material.fractions, expected_array)


#test_x()
