import unittest
from .Polynomio import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_evaluate_roots_about_polynomial(self):
        roots = [-3.0, -2.0, 1.0]
        self.assertEqual(roots, Polynomial([1, 4, 1, -6]))

    def test_Evaluate_Polynomial(self):
        self.assertEqual(0, Polynomial.evaluate_polynomial(1))


if __name__ == "__main__":
    unittest.main()


