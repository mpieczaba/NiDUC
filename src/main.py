from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from decoder import Decoder


class NiDUC:
    def main():
        print("NiDUC")

        # Set the number number of correctable symbols
        t = 6

        # Create an instance of the primitive polynomial.
        p = Polynomial([1, 1, 0, 0, 1])

        # Create an instance of the Galois field.
        gf = GF(p)

        # Create an instance of the message array.
        m = [1, 2, 3]

        # Create an instance of the encoder.
        e = Encoder(t)

        # Encode the message.
        c = e.encode(m)

        # Create an instance of the decoder.
        d = Decoder(t)

        # Decode the message.
        s = d.decode(c)

        print("t = " + str(t))
        print("P(x) = " + str(p))
        print("G(x) = " + str(e.g))
        print("M(x) = " + str(m))
        print("C(x) = " + str(c))
        print("S(x) = " + str(d.s))
        print("Ω(x) = " + str(d.omega))
        print("Λ(x) = " + str(d.lmbd))

    if __name__ == "__main__":
        main()
