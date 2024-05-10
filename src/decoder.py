import gf
from gf import GF
from polynomial import Polynomial


class Decoder:
    # TODO: Return decoded messages.
    def decode(self, p):
        return self.__calculate_syndromes(p)

    def __calculate_syndromes(self, p):
        res = Polynomial([0] * 12)

        for i in range(1, 13):
            res.coef[i - 1] = p(GF.pow(2, i))

        return res
