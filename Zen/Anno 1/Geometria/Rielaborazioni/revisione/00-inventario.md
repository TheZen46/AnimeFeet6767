# Geometria · fase 1: inventario e integrità

Corso: Geometria (6 CFU, 1° anno, 1° semestre). Programma di riferimento: `revisione/programmi/geometria.md` (UniGe 2026/27).
Originali: cartella `Geometria/` sul computer dell'autore. Nessun originale è stato modificato.

## 1. File e uso

| File | Pagine | Tipo | Uso |
|---|---|---|---|
| `Appunti_mano/Lezione 02…21` | 62 (34 scritte) | a mano, una o più pagine fitte per lezione | Inventario, copertura, esempi; base del modulo 2 |
| `Rielaborazioni/NumeriComplessi.pdf` | 11 | battuta (~4000 parole) | Base del modulo 1 (complessi e polinomi) |
| `Rielaborazioni/GeometriaAnalitica.pdf` | 15 | battuta (~3800) | Base del modulo 1 (geometria analitica) |
| `Rielaborazioni/SpaziVettoriali.pdf`, `Esercizio_SpaziVettoriali.pdf` | 13 + 6 | battute (~7000) | Base del modulo 3 |
| `Rielaborazioni/Lineare.pdf`, `esercizio_LINREARE.pdf` | 17 + 7 | battute (~5500) | Base dei moduli 3 e 4 |
| `Formulari e riassunti/` (6 file) | 26 | a mano | Controllo; insiemi numerici (modulo 1) |
| `Esercizi/` (4 file) | 17 | a mano, esercizi d'esame svolti | Non usati nei moduli (domanda 2) |
| `_da_verificare/Note_261103_172832.pdf` | 2 | – | Pagine bianche |

Un file della cartella `_da_verificare/` è stato escluso su indicazione dell'autore e non è stato aperto. L'indice delle lezioni è in `trascrizione/L - indice delle lezioni.md`.

### Lezioni mancanti

Manca la **lezione 1** (le lezioni sono il martedì e il giovedì e la 2 è del 30/09/2025, quindi la 1 è probabilmente del 25/09). Il contenuto atteso (insiemi numerici, prime operazioni con i complessi) è coperto dalla dispensa sui numeri complessi e dal riassunto degli insiemi numerici.

## 2. Problemi tecnici

| Livello | Dove | Problema | Correzione |
|---|---|---|---|
| DA CORREGGERE | Dispense battute (soprattutto i due "Esercizio") | Rimandi `[cite: …]` rimasti nel testo, residuo dello strumento di scrittura | Non ripresi: i moduli sono riscritti |
| DA CORREGGERE | `NumeriComplessi.pdf` | Titolo "Analisi Matematica: I Numeri Complessi" | Il materiale è del corso di Geometria |
| DA CORREGGERE | Dispense battute | "Figura N" senza figura, rimandi a "pag. 5 degli appunti" | Due figure ridisegnate (radici seste, prodotto vettoriale) |
| NOTA | `esercizio_LINREARE.pdf` | Frase fuori contesto sul "motion capture" | Non ripresa |
| NOTA | Lezioni | Grafia molto fitta | Lette a 80 dpi per l'inventario, ingrandite a 170 dpi dove servivano gli esempi |

## 3. Errori di sostanza trovati

| Livello | Dove | Negli appunti | Corretto |
|---|---|---|---|
| DA CORREGGERE | L05, inversa $3 \times 3$ | La terza riga della matrice si legge $(1, 4, 1)$ [lettura]; con questa riga la matrice ha determinante 0 e non è invertibile | Il calcolo degli appunti torna con $(1, -4, 1)$ ($\det = 8$, frazioni in ottavi): si usa questa |
| NOTA | `NumeriComplessi.pdf` § 5.1 | $(2 + 2i)^{100}$ scritto come $-8^{50}$ negli appunti e $-2^{150}$ nella dispensa | Uguali; si usa $-2^{150}$ |

Gli esempi delle dispense e delle lezioni ripresi nei moduli sono stati ricalcolati tutti (`strumenti/verifica.py`, 70 controlli senza errori): complessi, divisione di polinomi, prodotti vettoriali e distanze, inverse, determinanti, ranghi, sistemi, coordinate, intersezioni di sottospazi, autovalori e diagonalizzazioni, Gram-Schmidt.

## 4. Rischi per la vendita

| Livello | Rischio | Cosa fare |
|---|---|---|
| DA CORREGGERE | Le dispense battute sono state scritte con uno strumento di scrittura assistita (rimandi `[cite]`, frasi fuori contesto) | Usate per la struttura e gli esempi; il testo dei moduli è riscritto |
| NOTA | Il riassunto di 12 pagine segue una numerazione per capitoli (Def 2.1.1, Teorema 2.2.17…) simile a quella di un libro di testo | Usato solo per controllo; nessun testo ripreso (domanda 3) |
| NOTA | Nessun nome di docenti o compagni nei moduli | – |
