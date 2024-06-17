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
        The number of parity symbols.
    n : int
        The code word size.
    k : int
        The message size.
    generator_polynomial : Polynomial
        The instance of the generator polynomial.
    """

    def __init__(self, t):
        self.t = t
        self.n = 2**4 - 1
        self.k = self.n - 2 * self.t

        self.__generate_gen_poly()

    def encode(self, m):
        """
        Encodes given message array.

        Parameters
        ----------
        m : array_like
            The message array.

        Returns
        -------
        res : Polynomial
            The encoded code word polynomial.
        """

        parity_polynomial = Polynomial(m) * Polynomial([0] * 2 * self.t + [1])
        codeword_polynomial = parity_polynomial + (
            parity_polynomial % self.generator_polynomial
        )

        while len(codeword_polynomial) < 15:
            codeword_polynomial.coef.append(0)

        return codeword_polynomial

    def __generate_gen_poly(self):
        """Generates the generator polynomial."""

        self.generator_polynomial = Polynomial([1])

        for i in range(1, 2 * self.t + 1):
            self.generator_polynomial *= Polynomial([gf.alpha[i], 1])
