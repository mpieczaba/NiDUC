import random

class Medium:
    def __init__(self, error_rate=0.01):
        """
        Initialize the Medium with a given error rate.
        
        :param error_rate: Probability of flipping any individual bit (0.01 = 1% chance)
        """
        if not (0 <= error_rate <= 1):
            raise ValueError("Error rate must be between 0 and 1.")
        self.error_rate = error_rate

    def transmit(self, data):
        """
        Simulate transmission of data through a noisy medium by randomly flipping bits.
        :param data: A bytes object representing encoded data
        :return: A bytes object with some bits flipped according to the error rate
        """
        # Convert the data to a list of bits
        bit_list = ''.join(format(byte, '08b') for byte in data)

        # Flip bits with the given probability
        corrupted_bits = [
            str(int(not int(bit))) if random.random() < self.error_rate else bit
            for bit in bit_list
        ]

        # Convert back to bytes
        corrupted_data = bytearray()
        for i in range(0, len(corrupted_bits), 8):
            corrupted_data.append(int(''.join(corrupted_bits[i:i + 8]), 2))

        return bytes(corrupted_data)