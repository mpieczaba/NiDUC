import csv
from encoder import Encoder
from decoder import Decoder
from polynomial import Polynomial
from gf import GF
from medium import Medium
from utils import convert_list_to_string

def test_errors(error_type):
    m = 4
    MAX_SYMBOL = 1 << m
    t = 6
    p = Polynomial([1, 1, 0, 0, 1])
    gf = GF(p)
    n = (1 << m) - 1
    encoder = Encoder(t)
    decoder = Decoder(t)
    medium = Medium()

    with open(f'test_results_{error_type}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Error Type", "Number of Errors", "Recovery Status", "Should Recover",
                         "P(x)", "G(x)", "M", "C(x)", "C'(x)", "S(x)", "Ω(x)", "Λ(x)", "E(x)", "R(x)"])

        for errors in range(1, n):
            for i in range(MAX_SYMBOL):
                for j in range(MAX_SYMBOL):
                    for k in range(MAX_SYMBOL):
                        message = [i, j, k]
                        encoded_message = encoder.encode(message)
                        erroneous_message = medium.transmit(encoded_message, error_type, errors)
                        
                        try: recovered_message = decoder.decode(erroneous_message)
                        except: print(errors, i, j, k)

                        recovery_status = convert_list_to_string(encoded_message.coef) == convert_list_to_string(recovered_message.coef)
                        should_recover = errors <= t

                        writer.writerow([error_type, errors, recovery_status, should_recover, convert_list_to_string(p.coef),
                                         convert_list_to_string(encoder.generator_polynomial.coef), convert_list_to_string(message), convert_list_to_string(encoded_message.coef),
                                         convert_list_to_string(erroneous_message.coef), convert_list_to_string(decoder.s.coef),
                                         convert_list_to_string(decoder.omega.coef), convert_list_to_string(decoder.lmbd.coef), convert_list_to_string(decoder.e.coef), convert_list_to_string(recovered_message.coef)])

if __name__ == "__main__":
    test_errors("random")
    test_errors("burst")
