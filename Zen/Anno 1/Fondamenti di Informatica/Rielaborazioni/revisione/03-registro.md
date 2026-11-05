# Fondamenti di Informatica · registro delle revisioni

## Origine del testo

Il corso non ha appunti delle lezioni. Su indicazione dell'autore (ALT-1, 5 novembre 2026) i sette moduli sono stati **scritti in revisione** dalle slide e dalle esercitazioni del corso, riformulando; i temi d'esame 2016-2020 sono usati solo come modello: tutti gli esercizi hanno testo e dati nuovi.

## Scelte

| N. | Dove | Scelta | Motivo |
|---|---|---|---|
| 1 | tutti | stringhe e array "alla C", niente `vector` e `string` | come nelle slide e nelle prove |
| 2 | 1.1 | $\mathbb N$ senza lo zero, $\mathbb N_0$ con | notazione delle slide |
| 3 | 5.4, guidato 1 | chiamate ricorsive in istruzioni separate | l'ordine di valutazione degli operandi di `+` non è stabilito dal C++ |
| 4 | modulo 6 | convenzioni delle slide (`_attributo`, `get`/`set`, `const T& operator=`) | sono quelle richieste alla prova pratica |
| 5 | 6, esercizio 3 | matrice 4 × 6 invece di dimensioni d'esame | file di prova piccolo e controllabile a mano |

## Verifiche

`strumenti/verifica.py`: 127 controlli. I conti di matematica discreta dei moduli 1-2 (`discreta.py`, 31 controlli, anche per enumerazione); i 67 programmi dei moduli 3-7 compilati con `g++ -std=c++17 -Wall -Wextra` senza avvisi ed eseguiti con AddressSanitizer e UBSan (nessuna perdita di memoria, nessun accesso fuori dai limiti), con uscite confrontate con quelle scritte nel testo (`prove.py`, file di dati compresi).

## Correzioni durante la verifica

| N. | Dove | Prima | Dopo |
|---|---|---|---|
| 1 | 4, `array.cpp` | uscita attesa della ricerca binaria: posizione 3 | 4: con due 7 la ricerca binaria trova quello centrale, non il primo |
| 2 | 3, esercizio 2 | `1 / 0` nel codice | `1 / zero`: con la costante il compilatore avvisa |
| 3 | 6, esercizio 3 | conteggio degli studenti sotto il 70% sbagliato nel testo | 1, ricontrollato con il programma |
| 4 | 6, guidato 3 | parametro inutilizzato con nome | senza nome, come nel costruttore di copia |

## Aggiunte dopo le risposte alle domande (5 novembre 2026)

| Domanda | Dove | Che cosa |
|---|---|---|
| C1 (esercizi più difficili) | moduli 1-7, "Esercizi più impegnativi" | 4 esercizi di matematica discreta nei moduli 1 e 2; 13 programmi nei moduli 3-7: numeri perfetti, complemento, esponenziale, compressione, esami da file, spirale, merge sort, permutazioni, potenza veloce, polinomio, fusione di liste, coda con due pile, lista palindroma |
| C2 (stringhe C) | modulo 4 | confermate le stringhe "alla C" (`char[]`, `<cstring>`) |
| C4 (prova al calcolatore su Linux) | modulo 3, § 3.8 e formulario | compilare ed eseguire da terminale come all'esame: cartella vicina alla home, comando di compilazione completo ogni volta, lettura degli errori, consegna anche senza aver eseguito |

Conteggi dopo le aggiunte: 127 controlli e 67 programmi in `strumenti/verifica.py`, tutti senza avvisi.

