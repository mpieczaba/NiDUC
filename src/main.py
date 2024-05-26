from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from decoder import Decoder
from utils import convert_string_to_list, convert_list_to_string
from medium import Medium


class NiDUC:
    def main():
        
        # Settings
        # Create an instance of the primitive polynomial.
        p = Polynomial([1, 1, 0, 0, 1])
        # Set the number number of correctable symbols
        t = 6
        # Create an instance of the Galois field.
        gf = GF(p)
        # Create an instance of the encoder.
        encoder = Encoder(t)
        # Create an instance of the decoder.
        decoder = Decoder(t)
        # Set up the Medium simulation
        medium = Medium(0.02)


        # Initial message string
        user_message = input("Message: ")
        # Message list
        message_list = convert_string_to_list(user_message)
        # Encoded message polynomial
        encoded_polynomial = encoder.encode(message_list)
        print(encoded_polynomial)
        # Bytes sent
        bytes_sent = encoded_polynomial.to_bytes()
        
        # Bytes received
        bytes_received = medium.transmit(bytes_sent)
        # Received message polynomial
        received_polynomial = Polynomial.from_bytes(bytes_received)
        print(received_polynomial)
        # Received message string
        received_message = convert_list_to_string(received_polynomial.to_list())[-3:]
        
        # Decoded message polynomial
        retrieved_polynomial = decoder.decode(received_polynomial)
        # Retrieved message string
        retrieved_message = convert_list_to_string(retrieved_polynomial.to_list())[-3:]

        print(f"\nYour message: {user_message}")
        print(f"Received message: {received_message}")
        print(f"Retrieved message: {retrieved_message}")
        print("\nDetails: ")
        print(f"t = {t}")
        print(f"P(x) = {p}")
        print(f"G(x) = {encoder.g}")
        print(f"M = {message_list}")
        print(f"C(x) = {encoded_polynomial}")
        print(f"S(x) = {decoder.s}")
        print(f"Ω(x) = {decoder.omega}")
        print(f"Λ(x) = {decoder.lmbd}")
        print(f"E(x) = {decoder.e}")
        print(f"R(x) = {retrieved_polynomial}")
        

    if __name__ == "__main__":
        main()
