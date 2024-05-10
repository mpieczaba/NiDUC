from polynomial import Polynomial
import gf


class Encoder:
    """
    Represents a Reed-Solomon encoder.

    Parameters
    ----------
    t : int
        The number of symbols.

    Attributes
    ----------
    t : int
        The number of symbols.
    n : int
        The code word size.
    k : int
        The message size.
    g : Polynomial
        The instance of the generator polynomial.
    """

    def __init__(self, t):
        self.t = t
        self.n = 2**4 - 1
        self.k = self.n - 2 * self.t

        self.__generate_gen_poly()

    def encode(self, m):
        """
        Encodes given message polynomial.

        Parameters
        ----------
        m : array_like
            The message array.

        Returns
        -------
        res : Polynomial
            The code word polynomial.
        """

        p = Polynomial(m) * Polynomial([0] * 2 * self.t + [1])

        return p + p % self.g

    def __generate_gen_poly(self):
        """Generates the generator polynomial."""

        self.g = Polynomial([1])

        for i in range(1, 2 * self.t + 1):
            self.g *= Polynomial([gf.alpha[i], 1])
