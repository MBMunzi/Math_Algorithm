class Polynomial:
    """ Instance a Polynomial.

        Args:
            coefficients(list): Polynomial coefficients.

        Attributes:
            coefficients(list): Polynomial coefficients.
            a0(int): Lower coefficient, like form x^1.
            an(int): Greatest coefficient, like form x^an
            roots test(method): Test Roots which founded.
            roots(list): Initiate a list of roots
    """
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.a0 = abs(self.coefficients[len(self.coefficients)-1])
        self.an = abs(self.coefficients[0])
        self.roots = []
        self.roots_test()

    def evaluate_a0(self):
        """ Calculate divisors of an.

            Returns:
                divisors_a0: Divisors about lower coefficient.
        """
        divisors_a0 = []
        if self.a0 != 1:
            for i in range(1, self.a0):
                if self.a0 % i == 0:
                    divisors_a0.extend((-1, 1, i, -i, self.a0, -self.a0))
            divisors_a0.sort()
        else:
            divisors_a0.extend((-1, 1))
        return divisors_a0

    def evaluate_an(self):
        """ Calculate divisors of an.

            Returns:
                divisors_an: Divisors about lower coefficient.
        """
        divisors_an = []
        if self.an != 1:
            for i in range(1, self.an):
                if self.an % i == 0:
                    divisors_an.extend((-1, 1, i, -i, self.an, -self.an))
            divisors_an.sort()
        else:
            divisors_an.extend((-1, 1))
        return divisors_an

    def possibles_roots(self):
        """ Calculate possibles roots, like form divisors about a0/an.

            Returns:

                possibles_roots: possibles roots about polynomial.
        """
        possibles_roots = []
        for p in self.evaluate_a0():
            for q in self.evaluate_an():
                possibles_roots.append(p/q)
        possibles_roots.sort()
        possibles_roots = list(set(possibles_roots))
        return possibles_roots

    def evaluate_polynomial(self, x):
        """ Evaluate Polynomial for any value.

            Args:
                x(int): Value to evaluate polynomial.

            Returns:
                Summation about Polynomial.
        """
        y = []
        self.coefficients.reverse()
        for power in range(len(self.coefficients)):
            partial_result = self.coefficients[power]*(x**(power+1))
            y.append(partial_result)
        return sum(y)

    def roots_test(self):
        """ Execute a test for verify the possible roots.

            Raises:

                Exception: The Polynomial don't has a rational root.

            Returns:

                roots: Roots about Polynomial.
        """
        for root in self.possibles_roots():
            if self.evaluate_polynomial(root) == 0:
                self.roots.append(root)
        return self.roots

    def __str__(self):
        return str(self.roots)

    def __repr__(self):
        return str(self)


test = Polynomial([1, 0, -7, 6])
print(test)
