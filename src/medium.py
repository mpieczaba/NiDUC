import random

class Medium:
    def __init__(self, n):
        """
        Inicjalizuje klasę Medium.

        Args:
            n (int): Długość słowa kodowego.
        """
        self.n = n
        self.num_errors = 0

    def set_errors(self, num_errors):
        """
        Ustawia liczbę błędów do wprowadzenia.

        Args:
            num_errors (int): Liczba błędów.
        """
        self.num_errors = num_errors

    def introduce_errors(self, codeword):
        """
        Wprowadza błędy do słowa kodowego.

        Args:
            codeword (list): Słowo kodowe.

        Returns:
            list: Słowo kodowe z wprowadzonymi błędami.
        """
        erroneous_codeword = codeword.copy()
        error_positions = random.sample(range(self.n), self.num_errors)

        for pos in error_positions:
            erroneous_codeword.coef[pos] ^= 1  # Wprowadzenie błędu przez inwersję bitu
        
        return erroneous_codeword

    def transmit(self, codeword):
        """
        Symuluje przesyłanie słowa kodowego przez medium z błędami.

        Args:
            codeword (list): Słowo kodowe.

        Returns:
            list: Otrzymane słowo kodowe z wprowadzonymi błędami.
        """
        return self.introduce_errors(codeword)
