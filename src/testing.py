import unittest
from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from decoder import Decoder
from utils import convert_string_to_list, convert_list_to_string
from medium import Medium

class TestReedSolomon(unittest.TestCase):
    def setUp(self):
        # Primitive polynomial for GF(2^4)
        self.p = Polynomial([1, 1, 0, 0, 1])
        self.gf = GF(self.p)
        self.t = 6  # Number of correctable symbols
        self.encoder = Encoder(self.t)
        self.decoder = Decoder(self.t)
        self.medium = Medium(0.02)  # 2% error rate

    def test_encoding_decoding(self):
        message = "abc"
        message_list = convert_string_to_list(message)
        encoded_polynomial = self.encoder.encode(message_list)
        bytes_sent = encoded_polynomial.to_bytes()
        
        for i in range(100):
            bytes_received = self.medium.transmit(bytes_sent)
            received_polynomial = Polynomial.from_bytes(bytes_received)
            retrieved_polynomial = self.decoder.decode(received_polynomial)
            retrieved_message = convert_list_to_string(retrieved_polynomial.to_list())[-3:]

            self.assertEqual(message, retrieved_message, f"{i}/100: Expected {message}, got {retrieved_message}")    


if __name__ == "__main__":
    unittest.main()