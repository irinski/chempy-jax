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
from Chempy.making_abundances import abundance_to_mass_fraction
import numpy as np

def test_030_making_abundances__abundance_to_mass_fraction():
    a = ModelParameters()
    basic_solar = solar_abundances()
    #print(basic_solar.all_elements)
    solar_scaled_material = PRIMORDIAL_INFALL(list(basic_solar.all_elements),np.copy(basic_solar.table))

    all_fractions = abundance_to_mass_fraction(
        solar_scaled_material.all_elements,
        solar_scaled_material.masses,
        solar_scaled_material.all_abundances,
        solar_scaled_material.all_abundances,
        solar_scaled_material.all_elements
    )

    #print(repr(all_fractions))

    expected_array = np.array([6.05637749e-05, 2.40503092e-04, 4.17061692e-04, 5.41512155e-04,
       6.49597169e-04, 7.21683167e-04, 8.41616193e-04, 9.61350933e-04,
       1.14161099e-03, 1.21253131e-03, 1.38137906e-03, 1.46040692e-03,
       1.62123125e-03, 1.68756464e-03, 1.86111073e-03, 1.92667961e-03,
       2.13025330e-03, 2.40034296e-03, 2.34928730e-03, 2.40815423e-03,
       2.70125179e-03, 2.87616943e-03, 3.06090594e-03, 3.12427336e-03,
       3.30104509e-03, 3.35554101e-03, 3.54110042e-03, 3.52669193e-03,
       3.81826859e-03, 3.92846757e-03, 4.18942405e-03, 4.36469691e-03,
       4.50179070e-03, 4.74444477e-03, 4.80116661e-03, 5.03514416e-03,
       5.13547691e-03, 5.26479548e-03, 5.34205794e-03, 5.48134790e-03,
       5.58243654e-03, 5.76591845e-03, 5.88849529e-03, 6.07296141e-03,
       6.18325053e-03, 6.39442519e-03, 6.48144273e-03, 6.75440453e-03,
       6.89903318e-03, 7.13289057e-03, 7.31615496e-03, 7.66706121e-03,
       7.62526912e-03, 7.88896134e-03, 7.98584823e-03, 8.25152441e-03,
       8.34636944e-03, 8.41910618e-03, 8.46667380e-03, 8.66702385e-03,
       8.71256956e-03, 9.03463420e-03, 9.13101324e-03, 9.44863147e-03,
       9.54929770e-03, 9.76409258e-03, 9.91011645e-03, 1.00500391e-02,
       1.01506969e-02, 1.03982415e-02, 1.05131753e-02, 1.07248727e-02,
       1.08725586e-02, 1.10463365e-02, 1.11885616e-02, 1.14302904e-02,
       1.15496826e-02, 1.15416911e-02, 1.18350685e-02, 1.20527885e-02,
       1.22807153e-02, 1.24499615e-02, 1.25569399e-02, 1.26182042e-02,
       1.26182042e-02, 1.32190710e-02, 1.33993311e-02, 1.35795912e-02,
       1.36396779e-02, 1.39423982e-02, 1.38821805e-02, 1.43023685e-02,
       1.42405447e-02, 1.46611515e-02, 1.46010648e-02, 1.48414116e-02,
       1.48414116e-02, 1.50817583e-02, 1.51418450e-02, 1.54422785e-02,
       1.55023651e-02, 1.55624518e-02, 1.57427119e-02, 1.56826252e-02,
       1.57427119e-02, 1.59830586e-02, 1.58628853e-02, 1.66440122e-02,
       1.61032320e-02, 1.62834921e-02, 1.63435788e-02, 1.71247057e-02,
       1.70646190e-02, 1.73650524e-02, 1.73049657e-02, 1.75453125e-02])
    
    assert np.allclose(all_fractions, expected_array)


    