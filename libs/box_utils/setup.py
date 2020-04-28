# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

import os
from os.path import join as pjoin
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import subprocess
import numpy as np

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

ext_modules = [
    Extension('iou_cpu',
              ['iou_cpu.pyx'],
              library_dirs=[],
              libraries=[],
              language='c++',
              runtime_library_dirs=[],
              # this syntax is specific to this build system
              # we're only going to use certain compiler args with nvcc and not with
              # gcc the implementation of this trick is in customize_compiler() below
              extra_compile_args={'gcc': ["-Wno-unused-function"]},
              include_dirs=[numpy_include])
]

setup(
    name='fast_rcnn',
    ext_modules=ext_modules
)
