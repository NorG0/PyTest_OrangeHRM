import unittest

from tests.login_test import TestLogin



def main():
    # Add tests cases
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestLogin))

    # Run tests
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    main()