import os
import sys

# add root directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest


# Discover and run all test files
def run_tests():
    # unittest set up
    loader = unittest.TestLoader()
    testcase_dir = os.path.join("tests", "controller", "api_resources")

    # Load all tests into a TestSuite
    test_suite = loader.discover(
        start_dir=testcase_dir,
        # pattern="*_testcase.py",
        pattern="user_friends_testcase.py",
    )

    # Run the test suite
    test_runner = unittest.TextTestRunner(verbosity=3)
    test_runner.run(test_suite)


if __name__ == "__main__":
    run_tests()
