class GF:
    """
    Represents a GF(2^m) Galois field.

    Parameters
    ----------
    p : Polynomial
        The primitive polynomial of the Galois field.
    """

    def __init__(self, p):
        self.p = p
        self.index = [0] * (2 ** p.degree())
        self.alpha = [0] * (2 ** p.degree() - 1)

        self.generate_gf()

    def generate_gf(self):
        """Generate index and alpha arrays of the Galois field."""
        x = 1

        for i in range(0, 2 ** self.p.degree() - 1):
            self.alpha[i] = x
            self.index[x] = i

            x *= 2
            if x & 2 ** self.p.degree():
                x ^= self.p(2)
