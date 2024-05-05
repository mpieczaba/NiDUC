from polynomial import Polynomial
from gf import GF
from encoder import Encoder


class NiDUC:
    def main():
        print("NiDUC")

        # Set the number number of correctable symbols
        t = 6

        # Create an instance of the primitive polynomial.
        p = Polynomial([1, 1, 0, 0, 1])

        # Create an instance of the Galois field.
        gf = GF(p)

        # Create an instance of the message polynomial.
        m = Polynomial([1, 2, 3], gf)

        # Create an instance of the encoder.
        e = Encoder(t, gf)

        # Encode the message.
        c = e.encode(m)

        print("t = " + str(t))
        print("P(x) = " + str(p))
        print("M(x) = " + str(m))
        print("C(x) = " + str(c))

    if __name__ == "__main__":
        main()
