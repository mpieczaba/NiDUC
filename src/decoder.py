import gf
from gf import GF
from polynomial import Polynomial


class Decoder:
    """
    Represents a Reed-Solomon decoder.

    Parameters
    ----------
    t : int
        The number of symbols.

    Attributes
    ----------
    t : int
        The number of symbols.
    r : Polynomial
            The received message polynomial.
    s : Polynomial
        The instance of the syndrome polynomial.
    e : Polynomial
        The instance of the error polynomial.
    omega : Polynomial
        The instance of the error magnitude polynomial.
    lmbd : Polynomial
        The instance of the error locator polynomial.
    lmbd_derivative : Polynomial
        The instance of the derivative of the error locator polynomial.
    """

    def __init__(self, t):
        self.t = t
        self.n = 15
        self.s = Polynomial([0] * 2 * self.t)
        self.omega = Polynomial(self.s.coef)

    def decode(self, r):
        """
        Decodes given message polynomial.

        Parameters
        ----------
        r : Polynomial
            The received message polynomial.

        Returns
        -------
        res : Polynomial
            The decoded code word polynomial.
        """

        self.r = r

        self.__calculate_syndrome_polynomial()
        self.__calculate_error_locator_polynomial()
        self.__calculate_error_magnitude_polynomial()
        self.__calculate_error_locations()
        self.__calculate_error_locator_polynomial_derivative()
        self.__calculate_error_polynomial()

        res = self.r + self.e

        while len(res) < self.n:
            res.coef.append(0)

        return res

    def __calculate_syndrome_polynomial(self):
        """Calculates the syndrome polynomial."""

        for i in range(len(self.s)):
            self.s.coef[i] = self.r(GF.pow(2, i + 1))

    def __calculate_error_locator_polynomial(self):
        """Calculates the error locator polynomial."""

        k = 1
        l = 0

        self.lmbd = Polynomial([1])
        c = Polynomial([0, 1])
        e = self.s.coef[0]

        while k < 2 * self.t:

            j = 1
            while j <= l:
                e ^= GF.mul(self.lmbd.coef[j], self.s.coef[k - 1 - j])
                j += 1

            tmp = self.lmbd + Polynomial([e]) * c

            if 2 * l < k and e != 0:
                l = k - l
                c = self.lmbd / Polynomial([e])

            c *= Polynomial([0, 1])
            e = self.s.coef[k]
            self.lmbd = tmp
            k += 1

    def __calculate_error_magnitude_polynomial(self):
        """Calculates the error magnitude polynomial."""

        self.omega = (self.s * self.lmbd) % Polynomial([0] * 2 * self.t + [1])

    def __calculate_error_locations(self):
        """Calculates error locations."""

        self.e = Polynomial([0] * len(self.r))

        for i in range(0, len(gf.alpha)):
            if self.lmbd(gf.alpha[i]) == 0:
                self.e.coef[(self.n - i) % self.n] = 1

    def __calculate_error_locator_polynomial_derivative(self):
        """Calculates the derivative of the error locator polynomial."""

        self.lmbd_derivative = Polynomial([0] * len(self.lmbd))

        for i in range(0, len(self.lmbd)):
            self.lmbd_derivative.coef[i] = ((i) % 2) * self.lmbd.coef[i]

        self.lmbd_derivative.coef.pop(0)

    def __calculate_error_polynomial(self):
        """Calculates the error polynomial."""

        for i in range(0, len(self.e)):
            if self.e.coef[i] != 0:
                self.e.coef[i] = GF.div(
                    self.omega(GF.pow(gf.alpha[i], -1)),
                    self.lmbd_derivative(GF.pow(gf.alpha[i], -1)),
                )
