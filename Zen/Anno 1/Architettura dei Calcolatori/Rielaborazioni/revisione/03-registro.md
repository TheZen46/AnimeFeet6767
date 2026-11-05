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

## Riscrittura schematica (5 novembre 2026)

Dopo le risposte B1-B3 e A1 di `revisione/DOMANDE-APERTE.md`.

| Richiesta | Che cosa è cambiato |
|---|---|
| B1: schematico, senza approfondimenti inutili | la teoria dei 5 moduli è riscritta in tabelle ed elenchi brevi; gli esercizi sono rimasti |
| B1: mancano gli schemi (datapath, memorie) | 23 figure nuove in `figure/`: formati (1.1), memoria del programma e stack (2.1, 2.2), ALU a 1 e 32 bit, anticipo del riporto, moltiplicatore, IEEE 754, somma in virgola mobile (3.1-3.6), datapath a ciclo singolo, pipeline, propagazione, load-use, salti in ID con rilevamento ed eccezioni, predittore a 2 bit, BTB, superscalare (4.1-4.8), gerarchia, cache diretta, posizionamento, cache a 2 vie, DRAM, traduzione con TLB (5.1-5.6) |
| B1: usare le bozze del libro come base | il libro dell'autore (*Stati*, PDF in `Architettura dei Calcolatori/`) è servito per scegliere che cosa disegnare e che cosa dire; le figure sono ridisegnate da zero con i nomi dei segnali del corso (Patterson-Hennessy), non quelli del libro, e il testo è nuovo |
| B2: orale (disegnare e argomentare) | in ogni paragrafo un blocco "All'orale" con domande *perché / come / che errore copre / che errori causa*; § 4.9 con la scaletta per ridisegnare il datapath |
| B2: scritto (dal C all'assembly, motivando) | § 2.8 con il metodo; esercizi 5-8 del modulo 2: ordinamento a bolle con procedura di scambio, quicksort, merge sort, ricerca binaria ricorsiva, ognuno con la tabella delle scelte |
| B3: previsione statica e dinamica | § 4.6 con la tabella delle differenze teoriche e nel datapath, figure 4.5-4.7 |
| B3: ordine e campi dei formati | § 1.5 con la figura 1.1 e il perché di ogni disposizione |
| A1: prezzo simile al libro | `valore: 5` in `catalog.yaml`: 23,99 € |

Controlli: le quattro tracce d'esame sono eseguite su 25 vettori (anche casuali, con ripetizioni e negativi) e confrontate con `sorted`; dopo ogni esecuzione `sp` deve essere tornato al valore iniziale e i registri `s0`-`s11` devono avere i valori di prima. La ricerca binaria è provata su tutti i valori da 0 a 14. Il conteggio della figura 4.4 (load-use) è ricontrollato con `strumenti/pipe.py`: 9 cicli, uno stallo. Il simulatore ora esegue anche `srai` e `srli`.

Correzioni durante la riscrittura:

| Dove | Prima | Dopo |
|---|---|---|
| 4.7, nota | "Le figure 4.3 e 4.5" | le figure dello schema completo sono 4.2, 4.3 e 4.5 |
| 2.4, figura 2.1 | indirizzi esadecimali delle zone (quelli del libro di testo sono a 64 bit) | solo i puntatori `sp`, `gp`, `pc`: il corso usa RV32 |

