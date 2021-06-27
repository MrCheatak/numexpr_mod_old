###################################################################
#  Numexpr - Fast numerical array expression evaluator for NumPy.
#
#      License: MIT
#      Author:  See AUTHORS.txt
#
#  See LICENSE.txt and LICENSES/*.txt for details about copyright and
#  rights to use.
####################################################################

"""
Numexpr is a fast numerical expression evaluator for NumPy.  With it,
expressions that operate on arrays (like "3*a+4*b") are accelerated
and use less memory than doing the same calculation in Python.

See:

https://github.com/pydata/numexpr

for more info about it.

"""

from .__config__ import show as show_config, get_info

from numexpr_mod.interpreter import MAX_THREADS, use_vml, __BLOCK_SIZE1__

is_cpu_amd_intel = False # DEPRECATION WARNING: WILL BE REMOVED IN FUTURE RELEASE

# cpuinfo imports were moved into the test submodule function that calls them 
# to improve import times.

import os, os.path
import platform
from numexpr_mod.expressions import E
from numexpr_mod.necompiler import NumExpr, disassemble, evaluate, re_evaluate, evaluate_cached, cache_expression

from numexpr_mod.utils import (_init_num_threads,
                           get_vml_version, set_vml_accuracy_mode, set_vml_num_threads,
                           set_num_threads, get_num_threads,
                           detect_number_of_cores, detect_number_of_threads)

# Detect the number of cores
ncores = detect_number_of_cores()
# Initialize the number of threads to be used
nthreads = _init_num_threads()
# The default for VML is 1 thread (see #39)
# set_vml_num_threads(1)

from . import version
__version__ = version.version

def print_versions():
    """Print the versions of software that numexpr_mod relies on."""
    try:
        import numexpr_mod.tests
        return numexpr_mod.tests.print_versions()
    except ImportError:
        # To maintain Python 2.6 compatibility we have simple error handling
        raise ImportError('`numexpr_mod.tests` could not be imported, likely it was excluded from the distribution.')

def test(verbosity=1):
    """Run all the tests in the test suite."""
    try:
        import numexpr_mod.tests
        return numexpr_mod.tests.test(verbosity=verbosity)
    except ImportError:
        # To maintain Python 2.6 compatibility we have simple error handling
        raise ImportError('`numexpr_mod.tests` could not be imported, likely it was excluded from the distribution.')