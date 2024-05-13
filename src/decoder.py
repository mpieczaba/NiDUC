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
        self.s = Polynomial([0] * 12)
        self.omega = Polynomial(self.s.coef)
        self.lmbd = Polynomial([1])

    # TODO: Return decoded messages.
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

        # TODO: Implement transmission medium simulation.
        self.r.coef[0] ^= 5
        self.r.coef[3] ^= 10
        self.r.coef[-1] ^= 7
        self.r.coef[7] ^= 12

        self.__calculate_syndrome_polynomial()
        self.__calculate_error_locator_and_magnitude_polynomials()
        self.__calculate_error_locations()
        self.__calculate_error_locator_polynomial_derivative()
        self.__calculate_error_polynomial()

        return self.r + self.e

    def __calculate_syndrome_polynomial(self):
        """Calculates the syndrome polynomial."""

        for i in range(1, 13):
            self.s.coef[i - 1] = self.r(GF.pow(2, i))

    def __calculate_error_locator_and_magnitude_polynomials(self):
        """Calculates the error locator and magnitude polynomials."""

        prev1 = Polynomial([0] * 2 * self.t + [1])
        prev2 = Polynomial([0])

        while self.omega.degree() > self.t:
            temp1 = self.omega
            temp2 = self.lmbd

            self.lmbd = prev2 + self.lmbd * (prev1 / self.omega)
            self.omega = prev1 % self.omega

            prev1 = temp1
            prev2 = temp2

        self.omega /= Polynomial([self.lmbd.coef[0]])
        self.lmbd /= Polynomial([self.lmbd.coef[0]])

    def __calculate_error_locations(self):
        """Calculates error locations."""

        self.e = Polynomial([0] * len(self.r))

        for i in range(0, len(gf.alpha)):
            if self.lmbd(gf.alpha[i]) == 0:
                self.e.coef[(15 - i) % 15] = 1

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
