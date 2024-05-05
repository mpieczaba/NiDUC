from polynomial import Polynomial


class Encoder:
    """
    Represents a Reed-Solomon encoder.

    Parameters
    ----------
    t: int
        The number of symbols.
    gf : GF
        The instance of the GF class.
    """

    def __init__(self, t, gf):
        self.t = t
        self.n = 2**4 - 1
        self.k = self.n - 2 * self.t
        self.gf = gf

        self.__generate_gen_poly()

    # TODO: Change the method of providing the encoder with data.
    def encode(self, p):
        """
        Encodes given message polynomial.

        Parameters
        ----------
        p: Polynomial
            The message polynomial.

        Returns
        -------
        res : Polynomial
            The code word polynomial.
        """

        p *= Polynomial([0] * 2 * self.t + [1], self.gf)

        return p + p % self.g

    def __generate_gen_poly(self):
        """Generates the generator polynomial."""

        self.g = Polynomial([1], self.gf)

        for i in range(1, 2 * self.t + 1):
            self.g *= Polynomial([self.gf.alpha[i], 1], self.gf)
