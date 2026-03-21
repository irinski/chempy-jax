#!/usr/bin/env python3
 
import sys
import os
import numpy as np
import jax
import jax.numpy as jnp
# jax.config.update("jax_enable_x64", True)
 
# Load Chempy library from path in environment variable CHEMPY_PATH
chempy_path = os.environ.get('CHEMPY_PATH')
if chempy_path and chempy_path not in sys.path:
    sys.path.insert(0, chempy_path)
 
from Chempy.parameter import ModelParameters
from Chempy.solar_abundance import solar_abundances


def test_solar_abundances_jax():  
    a = ModelParameters()
    print(a.solar_abundance_name_list)
    
    basic_solar = solar_abundances()
    
    solar_table = np.copy(basic_solar.table)
    
    print(f"Original NumPy array type: {type(solar_table)}")
    
    print("Fields:", solar_table.dtype.names)
    print("Shape :", solar_table.shape)
    print("Dtype :", solar_table.dtype)

    numeric_fields = ("Number", "Mass", "photospheric", "error")
 
    solar_table_jax = {
        field: jnp.asarray(solar_table[field])
        for field in numeric_fields
    }
    solar_symbols = np.asarray(solar_table["Symbol"])
    
    print("JAX-compatible numeric fields:")
    for field, values in solar_table_jax.items():
        print(f"  {field}: {type(values)}, shape={values.shape}, dtype={values.dtype}")
    
    print(f"Symbol field stays outside JAX: {type(solar_symbols)}, dtype={solar_symbols.dtype}")
    
    matrix_dtype = jnp.float64 if jax.config.jax_enable_x64 else jnp.float32
    print(f"Using matrix dtype: {matrix_dtype}")
    
    solar_table_matrix_jax = jnp.column_stack([
        solar_table_jax[field].astype(jnp.float64)
        for field in numeric_fields
    ])
    print(
        "Combined numeric matrix:",
        type(solar_table_matrix_jax),
        solar_table_matrix_jax.shape,
        solar_table_matrix_jax.dtype,
    )

test_solar_abundances_jax()   