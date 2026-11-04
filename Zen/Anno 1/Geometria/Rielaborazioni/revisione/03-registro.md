# Geometria · registro delle correzioni e delle aggiunte

Ogni esempio dei moduli è stato ricalcolato con `strumenti/verifica.py`. Qui sono elencate le correzioni di sostanza, gli esempi costruiti per i moduli e le aggiunte; le correzioni di forma non sono registrate una per una.

## Correzioni di sostanza

| # | Modulo | Dove | Prima | Dopo | Motivo | Fonte |
|---|---|---|---|---|---|---|
| 1 | 2 · es. 2 | L05 | Matrice da invertire con terza riga $(1, 4, 1)$ [lettura] | $(1, -4, 1)$ | Con $(1, 4, 1)$ il determinante è 0; i passaggi degli appunti (frazioni in ottavi) tornano solo con $-4$ | `verifica.py` |
| 2 | 2 · 2.4 | L06 | Determinante $4 \times 4$: il primo passaggio (scambio di righe e cambio di segno) senza commento | Spiegato che i due cambi di segno si compensano | Il risultato $-6$ è giusto, il passaggio era ambiguo | `verifica.py` |
| 3 | 1 · 1.4 | dispensa, § 5.1 | $(2 + 2i)^{100} = -8^{50}$ e $-2^{150}$ | $-2^{150}$ | Stessa quantità, una sola forma | – |
| 4 | 4 · 4.2 | L17-L18 | Polinomio caratteristico come $\det(A - \lambda I)$ e $\det(\lambda I - A)$ | $\det(A - tI)$ | Uniformità; le radici non cambiano | – |

## Esempi costruiti per i moduli

Gli appunti hanno gli argomenti ma non sempre un esempio leggibile o completo; questi sono stati scritti per i moduli e ricontrollati:

| Modulo · sezione | Esempio |
|---|---|
| 1 · 1.4 | Radici quadrate di $3 + 4i$ con il metodo algebrico |
| 1 · 1.9 | Distanza di un punto da un piano; distanza fra due rette sghembe |
| 1 · es. 2, 3 | Sfera e piano; radici cubiche dell'unità |
| 2 · 2.1 | Matrici che non commutano e divisori dello zero (con le matrici degli appunti rese esplicite) |
| 2 · es. 3 | Matrici $AA^T$ e scomposizione in parte simmetrica e antisimmetrica |
| 3 · es. 2, 3 | Sottospazio delle matrici simmetriche; equazione cartesiana di uno span |
| 3 · 3.7 | La derivata su $\mathbb{R}_2[x]$ |
| 4 · 4.3 | Matrice diagonalizzabile con autovalore doppio |
| 4 · 4.4 | Prodotto scalare definito da una matrice simmetrica $2 \times 2$ |
| 4 · es. 1 | Gram-Schmidt su $(1, 1, 0)$, $(1, 0, 1)$, $(0, 1, 1)$ (l'esempio degli appunti non è leggibile per intero) |
| 4 · es. 2 | Formula di Binet per Fibonacci (nella L16 c'è l'idea, non il conto) |
| 4 · es. 3 | Diagonalizzabilità con un parametro |

## Aggiunte

Nessun blocco `[!aggiunta]`: tutti gli argomenti del programma sono negli appunti (`01-copertura.md`).
