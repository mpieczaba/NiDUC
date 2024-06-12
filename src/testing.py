import unittest
from polynomial import Polynomial
from gf import GF
from encoder import Encoder
from decoder import Decoder
from medium import Medium
import random

class TestReedSolomon(unittest.TestCase):
    def setUp(self):
        self.p = Polynomial([1, 1, 0, 0, 1]) # Primitive polynomial for GF(2^4)
        self.gf = GF(self.p)
        self.m = 4  # Bits per symbol
        self.t = 6  # Number of correctable symbols
        self.n = 2 ** self.m - 1 # Length of codeword (for GF(2^4) can be up to 15)
        self.encoder = Encoder(self.t)
        self.decoder = Decoder(self.t)
        self.medium = Medium() # Transmission medium

    def run(self, result=None):
        self.num_passed = 0
        self.num_failed = 0
        super(TestReedSolomon, self).run(result=result)
        print(f"Tests Passed: {self.num_passed}/{self.num_passed + self.num_failed} ({(self.num_passed / (self.num_passed + self.num_failed)) * 100:.2f}% success rate)")

    def test_correctable_errors(self):
        TEST_COUNT = 100
        for i in range(1, self.t + 1):
            self.medium.set_errors(i)
            for j in range(TEST_COUNT):
                message_list = [random.randint(0, 15) for _ in range(self.n - 2 * self.t)]
                encoded_polynomial = self.encoder.encode(message_list)
                received_polynomial = self.medium.transmit(encoded_polynomial)
                retrieved_polynomial = self.decoder.decode(received_polynomial)
                test_message = f"Testing {i} errors [{j+1}/{TEST_COUNT}]: Expected {encoded_polynomial.to_list()}, got {retrieved_polynomial.to_list()}"
                try:
                    self.assertEqual(encoded_polynomial.to_list(), retrieved_polynomial.to_list(), test_message)
                    self.num_passed += 1
                except AssertionError as e:
                    self.num_failed += 1
                    print(f"\nTest Failed:\n{test_message}")
                    print(f"\nReason:\n{e}")

if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner())
