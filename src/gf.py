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

        global index
        index = [0] * (2 ** p.degree())
        global alpha
        alpha = [0] * (2 ** p.degree() - 1)

        self.__generate_gf()

    def __generate_gf(self):
        """Generates index and alpha arrays of the Galois field."""

        x = 1
        for i in range(0, 2 ** self.p.degree() - 1):
            alpha[i] = x
            index[x] = i

            x *= 2
            if x & 2 ** self.p.degree():
                x ^= self.p(2)

    def mul(a, b):
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

        Raises
        ------
        err : ValueError
            If alpha or index array is empty.
        """

        if alpha is None or index is None:
            raise ValueError("Galois field is not set!")

        if a == 0 or b == 0:
            return 0

        return alpha[(index[a] + index[b]) % 15]

    def div(a, b):
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
        err : ValueError
            If alpha or index array is empty.
        zero_div_err : ZeroDivisionError
            If `b` is equal to zero.
        """

        if alpha is None or index is None:
            raise ValueError("Galois field is not set!")

        if a == 0:
            return 0
        if b == 0:
            ZeroDivisionError("Cannot divide by zero!")

        return alpha[(index[a] - index[b] + 15) % 15]
