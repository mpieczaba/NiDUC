from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from decoder import Decoder
from utils import convert_string_to_list, convert_list_to_string
from medium import Medium


class NiDUC:
    def main():
        
        # SETTINGS
        # Set the number of bits per symbol
        m = 4
        # Set the number of symbols
        n = 2 ** m - 1
        # Set the number number of correctable symbols
        t = 6
        # Number of message symbols
        k = n - 2 * t
        # Number of errors
        num_errors = 1
        # Create an instance of the primitive polynomial.
        primitive_polynomial = Polynomial([1, 1, 0, 0, 1])
        # Create an instance of the Galois field.
        gf = GF(primitive_polynomial)
        # Create an instance of the encoder.
        encoder = Encoder(t)
        # Set up the Medium simulation
        medium = Medium(n)
        medium.set_errors(num_errors)
        # Create an instance of the decoder.
        decoder = Decoder(t)
        
        ans = True
        while(ans):
            # SENDING
            # -------
            # Initial message string
            user_message = input("Message: ")
            # Message list
            message_list = convert_string_to_list(user_message[:k])
            # Encoded message polynomial
            encoded_polynomial = encoder.encode(message_list)
            
            # RECEIVING
            # ---------
            # Received message polynomial
            received_polynomial = medium.transmit(encoded_polynomial)
            # Received message string
            received_message = convert_list_to_string(received_polynomial.to_list())[-k:]
            
            # RETRIEVING
            # ----------
            # Decoded message polynomial
            retrieved_polynomial = decoder.decode(received_polynomial)
            # Retrieved message string
            retrieved_message = convert_list_to_string(retrieved_polynomial.to_list())[-k:]

            print(f"\nYour message: {user_message}")
            print(f"Received message: {received_message}")
            print(f"Retrieved message: {retrieved_message}")
            ans = "y" == input(f"\nPrint details? [y/n]: ")
            if(ans):
                print("\nSettings: ")
                print(f"t = {t}")
                print(f"P(x) = {primitive_polynomial}")
                print(f"G(x) = {encoder.generator_polynomial}")
                print("\nCoding details: ")
                print(f"M = {message_list}")
                print(f"C(x) = {encoded_polynomial}")
                print(f"Received polynomial = {received_polynomial}")
                print(f"S(x) = {decoder.s}")
                print(f"Ω(x) = {decoder.omega}")
                print(f"Λ(x) = {decoder.lmbd}")
                print(f"E(x) = {decoder.e}")
                print(f"R(x) = {retrieved_polynomial}")
            ans = "y" == input(f"\nWish to continue the program? [y/n]: ")

    if __name__ == "__main__":
        main()
