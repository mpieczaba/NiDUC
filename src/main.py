from polynomial import Polynomial
from gf import GF


class NiDUC:
    def main():
        print("NiDUC")

        # Create the primitive polynomial instance.
        p = Polynomial([1, 1, 0, 0, 1])

        # Create the Galois field instance.
        gf = GF(p)

        # Create instances of the f and g polynomials.
        f = Polynomial([1, 2, 3], gf)
        g = Polynomial([4, 2, 1], gf)

        print("f(x) = " + str(f))
        print("g(x) = " + str(g))

        print("f(x) + g(x) = " + str(f + g))
        print("f(x) * g(x) = " + str(f * g))

    if __name__ == "__main__":
        main()
