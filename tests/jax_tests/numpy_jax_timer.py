import numpy as np
import jax
import jax.numpy as jnp
import time

jax.config.update("jax_enable_x64", True)

N = 116
I = 100
print(f"N = {N}, I = {I}")

x_np = np.arange(N)
x_jax = jnp.arange(N)

def f_numpy(x):
    x =  x * x + 17
    x = x**(1/2)
    return(x)

x_np = f_numpy(x_np)

@jax.jit
def f_jax(x):
    x =  x * x + 17
    x = x**(1/2)
    return(x)

# compile once
x_jax = f_jax(x_jax)
tmp = x_jax[100]

# NumPy
print("NUMPY:")
start = time.time()

for _ in range(I):
    x_np = f_numpy(x_np)
print(x_np[100])

numpy_time = time.time() - start
print(numpy_time)

# JAX
print("\nJAX:")
start = time.time()

for _ in range(I):
    x_jax = f_jax(x_jax)

print(x_jax[100])

jax_time = time.time() - start
print(jax_time)

