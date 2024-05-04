class Polynomial:
    """
    Represents a polynomial in the given Galois field.

    Parameters
    ----------
    coef : array_like
        Polynomial coefficients in order of increasing degree.
    gf : GF, optional
        The instance of the GF class.
    """

    def __init__(self, coef, gf=None):
        self.coef = coef
        self.gf = gf

    def __call__(self, x):
        return sum(map(lambda e: e[1] * x ** e[0], enumerate(self.coef)))

    def __str__(self):
        return " + ".join(
            reversed(
                list(map(lambda e: str(e[1]) + "*x^" + str(e[0]), enumerate(self.coef)))
            )
        )

    def __len__(self):
        return len(self.coef)

    def __add__(self, poly):
        res = Polynomial(self.coef + [0] * (len(poly) - len(self)))

        for i in range(0, min(len(res), len(poly))):
            res.coef[i] ^= poly.coef[i]

        return res

    def __mul__(self, poly):
        if self.gf is None:
            raise ValueError("Galois field is not set!")

        res = Polynomial([0] * (len(self) + len(poly) - 1))

        for i in range(0, len(poly)):
            for j in range(0, len(self)):
                res.coef[i + j] ^= self.gf.alpha[
                    (self.gf.index[self.coef[j]] + self.gf.index[poly.coef[i]]) % 16
                ]

        return res

    def degree(self):
        """
        The degree of the polynomial.

        Returns
        -------
        degree : int
            Degree of the polynomial.
        """

        return len(self) - 1
