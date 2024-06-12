import random
from polynomial import Polynomial

class Medium:
    def __init__(self):
        """
        Inicjalizuje klasę Medium.
        """

    def introduce_random_errors(self, codeword, num_errors):
        """
        Wprowadza losowe błędy do słowa kodowego.

        Args:
            codeword (list): Słowo kodowe.
            num_errors (number): Liczba błędów losowych

        Returns:
            list: Słowo kodowe z wprowadzonymi losowymi błędami.
        """
        erroneous_codeword = codeword.copy()
        error_positions = random.sample(range(len(codeword)), num_errors)

        for pos in error_positions:
            erroneous_codeword[pos] ^= 1  # Wprowadzenie błędu przez inwersję bitu

        return Polynomial(erroneous_codeword)

    def introduce_burst_errors(self, codeword, burst_length):
        """
        Wprowadza błędy typu burst do słowa kodowego.

        Args:
            codeword (list): Słowo kodowe.
            burst_length (number): Długość bloku błędu.

        Returns:
            list: Słowo kodowe z wprowadzonymi błędami typu burst.
        """
        erroneous_codeword = codeword.copy()
        start_position = random.randint(0, len(codeword) - burst_length)

        for i in range(burst_length):
            erroneous_codeword[start_position + i] ^= 1  # Wprowadzenie błędu przez inwersję bitu

        return Polynomial(erroneous_codeword)

    def transmit(self, codeword, error_type='random', n=0):
        """
        Symuluje przesyłanie słowa kodowego przez medium z błędami.

        Args:
            codeword (Polynomial): Słowo kodowe.
            error_type (str): Typ błędów ('random' lub 'burst').
            n (number): Liczba błędów podanego typu

        Returns:
            list: Otrzymane słowo kodowe z wprowadzonymi błędami.
        """
        if n == 0:
            return codeword
        elif error_type == 'random':
            return self.introduce_random_errors(codeword.coef, n)
        elif error_type == 'burst':
            return self.introduce_burst_errors(codeword.coef, n)
        else:
            raise ValueError("Invalid error type. Use 'random' or 'burst'.")