# NiDUC
Implementacja kodera i dekodera RS.

## Parametry implementacji

- symbole kodu z ciała Galois $GF(2^m)$, gdzie $m \in \set{ 3, 4, 5, 6, \dots }$
- zdolność korekcyjna kodu $t \gt 3$ symbole

## Schemat implementacji

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
