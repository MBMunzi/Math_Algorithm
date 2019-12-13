import unittest
from Polynomio import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_evaluate_roots_about_polynomial(self):
        roots = [(3 / 2), 3, -1]
        self.assertEqual(roots, Polynomial([2, -7, 9]))

    def test_Evaluate_Polynomial(self):
        self.assertEqual(0, Polynomial.evaluate_polynomial(1))


if __name__== "__main__":
    unittest.main()