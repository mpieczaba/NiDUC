# Reed-Solomon Code

## O projekcie

Implementacja kodera i dekodera RS zrealizowana w ramach zajęć projektowych _Niezawodność i Diagnostyka Układów Cyfrowych 2_ na Politechnice Wrocławskiej (2024).

Autorzy:

- Mikołaj Pieczaba
- Kamil Sobierajski

### Parametry implementacji

| Symbol | Nazwa parametru                                   | Wzór                  | Wartość |
| ------ | ------------------------------------------------- | --------------------- | ------- |
| m      | liczba bitów symbolu                              | N/A                   | 4       |
| k      | liczba symboli wiadomości                         | $k = n - 2t$          | 3       |
| t      | liczba symboli korekcyjnych (zdolność korekcyjna) | $t = \frac{n - k}{2}$ | 6       |
| n      | liczba symboli w słowie                           | $n = 2^m$             | 15      |
| N      | liczba bitów bloku kodowego                       | $N = n * m$           | 60      |

### Schemat implementacji

```mermaid
stateDiagram
    direction LR

    coder: Koder
    channel: Kanał transmisyjny
    decoder: Dekoder

    state coder {
        polynomial: Wyznaczenie wielomianu generującego kod
        evaluation: Wyznaczenie wartości wielomianu dla rozszerzonej dziedziny
        codeword: Wyznaczenie słowa kodującego

        [*] --> polynomial
        polynomial --> evaluation
        evaluation --> codeword
        codeword --> [*]
    }

    state channel {
        bitFlip: Błędy losowe
        burstError: Błąd typu wiązanka (burst error)

        [*] --> bitFlip
        bitFlip --> [*]
        [*] --> burstError
        burstError --> [*]
    }

    state decoder {
        syndromes: Ocena syndromów
        errorLocator: Wielomian wyszukiwania błędów
        errorLocations: Lokalizacje błędów
        errorMagnitudes: Ocena wielkości błędów
        errorCorrection: Korekcja błędów

        [*] --> syndromes
        syndromes --> errorMagnitudes
        syndromes --> errorLocator
        errorLocator --> errorLocations
        errorLocator --> errorCorrection
        errorLocations --> errorMagnitudes
        errorLocations --> errorCorrection
        errorMagnitudes --> errorCorrection
        errorCorrection --> [*]
    }

    [*] --> coder
    coder --> channel
    channel --> decoder
    decoder --> [*]
```

## Pomocne linki

- [Wikiversity: Reed–Solomon codes for coders](https://en.wikiversity.org/wiki/Reed%E2%80%93Solomon_codes_for_coders)
- [Practical Reed-Solomon for Programmers](https://berthub.eu/articles/posts/reed-solomon-for-programmers/)
- [NASA: Reed-Solomon Codes and the Exploration of the Solar System](https://dataverse.jpl.nasa.gov/api/access/datafile/34447?gbrecs=true)
- [UNB: Introduction to Reed Solomon (RS) Codes](https://www.ece.unb.ca/cgi-bin/tervo/rscodes.pl)
- [BBC: Reed-Solomon error correction](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP031.pdf)
