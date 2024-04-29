# Na 29.04:
# - wielomian generujący (w tym funkcja mnożenia wielomianów przez siebie), może być ewentualnie na kartce
# - dzielenie wielomianów (!)
# - dzielenie M(x)/G(X) - samo xorowanie, wartość reszty (!)
# - koder (!)
# - przeczytać Mochnackiego, zobaczyć jak działa dekoder

from pyfinite import ffield

p = 2  # Charakterystyka ciała
n = 4  # Stopień rozszerzenia

GF = ffield.FField(n)  # Tworzenie ciała Galois GF(2^4)

# Wypisanie elementów ciała Galois GF(2^4)
print("Elementy ciała Galois GF(2^4):")
for i in range(2**n):
    print(i, ": ", GF.ShowPolynomial(i))

# def generate_GF_elements(m):
#     # Wielomian generujący P(x) = x^m + x + 1
#     poly_coeffs = [1, 0, 1, 1]

#     # Wygenerowanie reszt z dzielenia x^n przez P(x)
#     GF_elements = []
#     for n in range(2 ** m):
#         element = 0
#         for i, coef in enumerate(poly_coeffs[::-1]):
#             if coef:
#                 element ^= (n << ((m - 1 - i) % m)) % (2 ** m)
#         GF_elements.append(element)

#     return GF_elements

# # Generowanie elementów ciała GF(16)
# GF_8 = generate_GF_elements(3)
# print("Elementy ciała GF(8):", GF_8)

# # Generowanie elementów ciała GF(16)
# GF_16 = generate_GF_elements(4)
# print("Elementy ciała GF(16):", GF_16)
