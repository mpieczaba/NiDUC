class GF:
    """
    Represents a GF(2^m) Galois field.

    Parameters
    ----------
    p : Polynomial
        The primitive polynomial of the Galois field.

    Attributes
    ----------
    p : Polynomial
        The primitive polynomial of the Galois field.
    index : array_like
        The array that maps exponent of the primitive element to index in the Galois field.
    alpha : array_like
        The array that maps index to exponent of the primitive element in the Galois field.
    """

    def __init__(self, p):
        self.p = p
        self.index = [0] * (2 ** p.degree())
        self.alpha = [0] * (2 ** p.degree() - 1)

        self.__generate_gf()

    def __generate_gf(self):
        """Generates index and alpha arrays of the Galois field."""

        x = 1
        for i in range(0, 2 ** self.p.degree() - 1):
            self.alpha[i] = x
            self.index[x] = i

            x *= 2
            if x & 2 ** self.p.degree():
                x ^= self.p(2)

    def mul(self, a, b):
        """
        Multiplies a and b in the Galois field.

        Parameters
        ----------
        a : int
            The multiplicand number.
        b : int
            The multiplier number.

        Returns
        -------
        res : int
            The product number.
        """

        if a == 0 or b == 0:
            return 0

        return self.alpha[(self.index[a] + self.index[b]) % 15]

    def div(self, a, b):
        """
        Divides a by b in the Galois field.

        Parameters
        ----------
        a : int
            The dividend number.
        b : int
            The divisor number.

        Returns
        -------
        res : int
            The quotient number.

        Raises
        ------
        err : ZeroDivisionError
            If `b` is equal to zero.
        """

        if a == 0:
            return 0
        if b == 0:
            ZeroDivisionError("Cannot divide by zero!")

        return self.alpha[(self.index[a] - self.index[b] + 15) % 15]
