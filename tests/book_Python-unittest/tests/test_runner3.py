# Using TestLoader class, method loadTestsFromModule

import unittest
from tests import calc_tests

test_load = unittest.TestLoader()
suites = test_load.loadTestsFromModule(calc_tests)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suites)
