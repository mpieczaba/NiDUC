from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from Medium import Medium


class NiDUC:
    def main():
        print("NiDUC")
        
        # Set up the Medium simulation
        medium = Medium(0.02)

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

        print("t = " + str(t))
        print("P(x) = " + str(p))
        print("M(x) = " + str(m))
        print("C(x) = " + str(c))
        
        sent_message = c.to_bytes()
        received_message = medium.transmit(sent_message)
        print("Received C(x) = " + str(Polynomial.from_bytes(received_message)))

    if __name__ == "__main__":
        main()
