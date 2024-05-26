from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from decoder import Decoder
from utils import convert_string_to_list, convert_list_to_string


class NiDUC:
    def main():
        
        # Settings
        # Create an instance of the primitive polynomial.
        p = Polynomial([1, 1, 0, 0, 1])
        # Create an instance of the Galois field.
        gf = GF(p)
        # Set the number number of correctable symbols
        t = 6
        # Create an instance of the encoder.
        e = Encoder(t)
        # Create an instance of the decoder.
        d = Decoder(t)
        
        message = input("Message: ")

        # Create an instance of the message array.
        m = convert_string_to_list(message)

        # Encode the message.
        c = e.encode(m)

        # Decode the message.
        r = d.decode(c)
        
        # Retrieved message string
        retrieved_message = convert_list_to_string(r.to_list())[-3:]

        print(f"\nYour message: {message}")
        print(f"Retrieved message: {retrieved_message}")
        print("\nDetails: ")
        print("t = " + str(t))
        print("P(x) = " + str(p))
        print("G(x) = " + str(e.g))
        print("M = " + str(m))
        print("C(x) = " + str(c))
        print("S(x) = " + str(d.s))
        print("Ω(x) = " + str(d.omega))
        print("Λ(x) = " + str(d.lmbd))
        print("E(x) = " + str(d.e))
        print("R(x) = " + str(r))
        

    if __name__ == "__main__":
        main()
