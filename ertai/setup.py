from distutils.core import setup
"""from distutils.extension import Extension"""
from Cython.Build import cythonize

"""setup(
    ext_modules = cythonize("helloworld.pyx")
)

setup(
    ext_modules=cythonize("fib.pyx")
)"""

setup(
    ext_modules=cythonize("primes.pyx")
)

