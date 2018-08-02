# Using TestLoader class, method loadTestsFromTestCase

import unittest
from tests import calc_tests

test_cases = []
test_cases.append(calc_tests.CalcTests)
test_cases.append(calc_tests.CalcExTests)

test_load = unittest.TestLoader()

suites = []

for tl in test_cases:
    suites.append(test_load.loadTestsFromTestCase(tl))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
