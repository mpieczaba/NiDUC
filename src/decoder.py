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
    s : Polynomial
        The instance of the syndrome polynomial.
    omega : Polynomial
        The instance of the error magnitude polynomial.
    lmbd : Polynomial
        The instance of the error locator polynomial.
    """

    def __init__(self, t):
        self.t = t
        self.s = Polynomial([0] * 12)
        self.omega = Polynomial(self.s.coef)
        self.lmbd = Polynomial([1])

    # TODO: Return decoded messages.
    def decode(self, r):
        """
        Decodes given message array.

        Parameters
        ----------
        r : array_like
            The received message array.
        """

        # TODO: Implement transmission medium simulation.
        r.coef[0] ^= 5
        r.coef[3] ^= 10
        r.coef[-1] ^= 7
        r.coef[7] ^= 12

        self.__calculate_syndromes(r)
        self.__calculate_error_locator_and_magnitude_polynomials()

    def __calculate_syndromes(self, p):
        """Generates the syndrome polynomial."""

        for i in range(1, 13):
            self.s.coef[i - 1] = p(GF.pow(2, i))

    def __calculate_error_locator_and_magnitude_polynomials(self):
        """Generates the error locator and magnitude polynomials."""

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
