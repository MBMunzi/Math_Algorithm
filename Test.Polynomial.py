import unittest
from Polynomio import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_evaluate_roots_about_polynomial(self):
        roots = [1, 2, -3]
        self.assertEqual(roots, Polynomial([1, 0, -7, 6]))

    def test_Evaluate_Polynomial(self):
        self.assertEqual(0, Polynomial.evaluate_polynomial(2))


if __name__== "__main__":
    unittest.main()