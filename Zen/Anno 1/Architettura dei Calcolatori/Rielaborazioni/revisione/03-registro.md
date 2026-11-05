# Architettura dei Calcolatori · registro delle revisioni

## Origine del testo

Il corso non ha appunti delle lezioni (unico appunto a mano: lo schema del datapath con pipeline). Su indicazione dell'autore (ALT-1, 5 novembre 2026: "fatti tanto bene quanto il resto") i cinque moduli sono stati **scritti in revisione** dalle slide del corso e da Patterson e Hennessy, *Struttura e progetto dei calcolatori*, edizione RISC-V, riformulando: nessun testo delle slide è copiato, le figure non sono riprodotte. La soglia del 15% di aggiunte non si applica: tutto il corso è un'aggiunta dichiarata.

## Scelte di contenuto

| N. | Dove | Scelta | Motivo |
|---|---|---|---|
| 1 | tutti | notazione RISC-V al posto di quella MIPS delle slide | il corso è sul RISC-V; le differenze sono dette nel testo (delay slot, EPC/Cause, overflow) |
| 2 | 3.2, 4.7 | RISC-V non genera eccezioni per l'overflow | le slide MIPS citano l'eccezione di overflow; detto esplicitamente |
| 3 | 3.6 | IEEE 754 richiamato da Reti Logiche 2.8 | evita il doppione; qui solo somma, prodotto e arrotondamento |
| 4 | 4.5 | condizioni di forwarding con `rs1`, `rs2`, `rd` | le slide usano `Rs`, `Rt` |
| 5 | 4.6 | salto ritardato presentato come caratteristica MIPS | RISC-V non ha delay slot |
| 6 | 5.8 | memoria virtuale solo come cenno | nelle slide compare solo nella gerarchia e nella DMA |

## Esempi ed esercizi costruiti

Tutti nuovi, con dati diversi da quelli delle slide; controllati con `strumenti/verifica_ampliamento.py` (63 controlli, compresi i programmi del modulo 2 eseguiti con il simulatore `simrv.py`).

| Modulo | Svolti | Guidati | Strumenti |
|---|---|---|---|
| 1 | 5 (codifiche, CPI, Amdahl, `lui`, little endian) | 3 | `rv.py` |
| 2 | 4 più tutti i frammenti del testo (somma, strlen, max, traccia, fattoriale, Fibonacci, strcpy, reverse coding) | 3 | `simrv.py` |
| 3 | 7 (carry lookahead, add and shift, Booth, divisione, somma e prodotto in virgola mobile, Hamming) | 3 | funzioni nel verificatore |
| 4 | 8 (ciclo singolo e pipeline, controllo, stalli e riordino, catena di dipendenze, salti in ID, CPI, VLIW con srotolamento, dipendenze) | 3 | `pipe.py`, esecutore dei pacchetti VLIW |
| 5 | 9 (dimensionamento, tre cache, località spaziale, AMAT, CPI con L2, DRAM, write-back, memoria virtuale, polling e DMA) | 3 | `cache.py` |

## Correzioni durante la verifica

| N. | Dove | Prima | Dopo |
|---|---|---|---|
| 1 | verificatore, Booth | prova su tutti i moltiplicandi a 4 bit | escluso $M = -8$, che non si può negare in 4 bit (limite noto dell'algoritmo a $n$ bit) |
| 2 | 4.7, nota | appunto a mano descritto come schema del forwarding in EX | descritto com'è: anche comparatore e forwarding in ID e indirizzo del gestore delle eccezioni |
