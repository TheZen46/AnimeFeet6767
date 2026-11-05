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

## Ampliamento del 5 novembre 2026

Dopo le risposte alle domande (`revisione/AMPLIAMENTO-ANNO-1.md`): GEO-1 nessun appunto della lezione 1; GEO-2 sì a un'appendice di esercizi d'esame, molto completa; GEO-3 il riassunto per capitoli è dell'autore, da rendere più argomentato e chiaro.

| Dove | Che cosa | ID |
|---|---|---|
| 4.8 (nuovo) | Forme quadratiche (segnatura, criterio del determinante) e classificazione affine delle coniche con gli invarianti, riduzione a forma canonica: è nel programma 2025/26 e mancava | GEO-05, GEO-06 |
| Moduli 1-4 | "Esercizi sul modello delle prove d'esame": 22 esercizi con dati nuovi sui tipi delle 13 prove 2024-2026 (complessi e polinomi, piani, proiezioni, sfere, sistemi con parametro, invertibilità e rango, sottospazi di $\mathbb{R}^4$, matrici associate, nucleo con parametro, diagonalizzazione su $\mathbb{R}$ e su $\mathbb{C}$, coniche) | GEO-02 … GEO-07 |
| Moduli 1-4 | 11 esercizi guidati e un formulario per modulo | tutti |

GEO-3: il riassunto per capitoli non è ripreso come testo; il suo contenuto (definizioni ed enunciati) è ora nei formulari di fine modulo, con le tabelle dei termini e delle domande per l'orale, collegati ai paragrafi in cui ogni enunciato è spiegato e dimostrato.

Un esercizio scritto in un primo momento (una matrice involutoria) coincideva con un tema d'esame del febbraio 2026 ed è stato sostituito. Controlli: `strumenti/verifica_ampliamento.py`, 47 controlli con sympy.
