from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        'app.py', 'evaluate.pyx', 'model/bimpm.pyx', 'model/layers.pyx',
        'model/utils.pyx'
    ],
                          annotate=True))
