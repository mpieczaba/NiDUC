from gf import GF


class Polynomial:
    """
    Represents a polynomial in the given Galois field.

    Parameters
    ----------
    coef : array_like
        Polynomial coefficients in order of increasing degree.

    Attributes
    ----------
    coef : array_like
        Polynomial coefficients in order of increasing degree.
    """

    def __init__(self, coef):
        self.coef = coef

    def __call__(self, x):
        res = self.coef[0]

        for i in range(1, len(self)):
            res ^= GF.mul(self.coef[i], GF.pow(x, i))

        return res

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

        return Polynomial.__normalize(res)

    def __mul__(self, poly):
        res = Polynomial([0] * (len(self) + len(poly) - 1))

        for i in range(0, len(poly)):
            for j in range(0, len(self)):
                res.coef[i + j] ^= GF.mul(self.coef[j], poly.coef[i])

        return Polynomial.__normalize(res)

    def __truediv__(self, poly):
        return Polynomial.__normalize(self.__div(poly)[0])

    def __mod__(self, poly):
        return Polynomial.__normalize(self.__div(poly)[1])

    def __div(self, poly):
        """
        Calculates P(x) / Q(x) + R(x) using the long division algorithm.

        Parameters
        ----------
        poly : Polynomial
            The divisor polynomial.

        Returns
        -------
        res : Polynomial
            The quotient polynomial.
        rmd : Polynomial
            The remainder polynomial.
        """
        
        res_len = len(self) - len(poly) + 1

        rmd = Polynomial(self.coef)
        res = Polynomial([0] * res_len)

        i = 0
        while len(rmd) >= len(poly) and rmd.coef != [0] and i < res_len:
            coef = GF.div(rmd.coef[-1], poly.coef[-1])
            res.coef[-1 - i] = coef

            rmd += poly * Polynomial([0] * (len(rmd) - len(poly)) + [coef])

            i += 1

        return (res, rmd)

    def __normalize(poly):
        """
        Trims trailing zero coefficients of the polynomial.

        Parameters
        ----------
        poly : Polynomial
            The polynomial to be trimmed.

        Returns
        -------
        res : Polynomial
            The trimmed polynomial.
        """

        while len(poly) > 1 and poly.coef[-1] == 0:
            poly.coef.pop(-1)

        return poly

    def degree(self):
        """
        The degree of the polynomial.

        Returns
        -------
        degree : int
            Degree of the polynomial.
        """

        return len(self) - 1
    
    def to_list(self):
        return self.coef
    
    def to_bytes(self):
        return bytes(self.coef)

    @staticmethod
    def from_bytes(data):
        coefficients = list(data)
        return Polynomial(coefficients)