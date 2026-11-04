# Reti Logiche · fase 1: inventario e integrità

Corso: Reti Logiche (6 CFU, 1° anno, 1° semestre). Programma di riferimento: `revisione/programmi/reti-logiche.md` (UniGe 2026/27).
Originali: `Reti Logiche/Appunti_mano/` (13 PDF scritti a mano su tablet), `Reti Logiche/Esercizi/` (5 PDF), `Reti Logiche/_da_verificare/` (1 PDF), `Reti Logiche/Materiale del docente/` (3 PDF di esercizi del simulatore). Nessun originale è stato modificato.

Gli appunti sono PDF scritti a mano senza testo selezionabile: il primo passo è stato trascriverli fedelmente in Markdown (`trascrizione/`). Le correzioni proposte qui sotto si applicano nella fase 4, sulla base delle trascrizioni.

## 1. File nell'ordine delle lezioni

| Lezione | Data | Pagine scritte | Parole trascritte | Argomento principale |
|---|---|---|---|---|
| 01 | mer 24/09/2025 | 2 di 4 | ~770 | Variabili booleane, funzioni di una e due variabili, le 16 funzioni di due variabili, porte logiche, XOR |
| 02 | lun 29/09/2025 | 4 di 5 | ~1190 | Teorema di Shannon (versione duale), SH1 e SH2, reti a due livelli, semplificazione algebrica, MUX 2→1, diagramma temporale, mappe di Karnaugh a 2, 3, 4 variabili |
| 03 | mer 01/10/2025 | 5 di 6 | ~1280 | Sintesi minima AND-OR e OR-AND, adiacenza, sole NAND, porta programmabile, indifferenze, MUX, DEMUX, decoder, MUX come porta universale, mappe a variabili riportate |
| 04 | mer 08/10/2025 | 3 di 4 | ~1140 | Numeri in base 2, 8, 16, BCD, codice Gray; somma, half e full adder, sottrazione, prodotto; complemento a 2; virgola fissa e mobile; sommatore a cascata, ALU, bit di parità |
| 05 | lun 13/10/2025 | 1 di 2 | ~70 | Una sola mappa con la sintesi OR-AND |
| 06 | mer 22/10/2025 | 4 di 6 | ~1030 | Ritardi e alee, dalla rete combinatoria alla rete sequenziale, latch SR (NOR, NAND), D, JK, latch con abilitazione, NET e PET; due schermate del simulatore |
| 07 | mer 29/10/2025 | 3 di 4 | ~730 | Esercizi in preparazione della prova: semplificazioni, mappe, variabili riportate, MUX, conversioni e operazioni binarie, flip flop |
| 08 | mer 05/11/2025 | 2 di 4 | ~670 | Flip flop D e JK con PR e CL, temporizzazioni ($t_s$, $t_h$, $t_p$, $t_w$, $T_{min}$), analisi di reti sincrone, contatore a 2 bit, registri PIPO, SISO, SIPO, PISO e universale |
| 09 | lun 10/11/2025 | 3 di 4 | ~860 | Flip flop T e contatore sincrono, contatore universale con sommatore, MSF di Moore, ASM, contatore modulo 4 e up/down, rilevatore di fronti, contatore con START |
| 10 | lun 17/11/2025 | 2 di 4 | ~660 | Sincronizzatore, generatore di sequenze, rilevatore di due pulsanti, rilevatore di impulso lungo; analisi di una MSF dal circuito all'ASM |
| 11 | senza data | 3 di 4 | ~950 | Procedura di progetto di una MSF: specifica, ASM, registro di stato, codifica, sintesi con FF D e con FF JK (luci a 6 stati, Es. 9, ENB/SEL) |
| 12 | lun 01/12/2025 | 2 di 4 | ~740 | Gestione degli errori (stati non usati), MSF di Mealy, ES. 10 in tre versioni, lavatrice con sintesi JK |
| 13 | mer 10/12/2025 | 1 di 3 | ~300 | Trasmettitore seriale (Moore e Mealy, ipotesi vera e falsa), gestione pulsanti |
| Esercizi | – | 7 | ~820 | Mappe e semplificazioni, specifica di un sistema con due FSM e un contatore, ricevitore con FF JK esterno, sintesi JK dell'esercitazione 09 |

In tutto ci sono circa 36 pagine scritte (su 54) e circa 11.000 parole trascritte, comprese le descrizioni delle figure. Le pagine vuote sono quelle finali di ogni file.

### Lezioni mancanti

Le lezioni sono il lunedì e il mercoledì. Fra il 24/09 e il 10/12 ci sono circa 22 date possibili e gli appunti sono 13. Il 3/11 c'era la prima prova intermedia (L01). Mancano gli appunti, ad esempio, del 6/10, 15/10, 20/10, 27/10, 12/11, 19/11, 24/11 (forse è la L11, senza data), 26/11, 3/12 e di tutto ciò che viene dopo il 10/12. Alcune di queste date erano probabilmente esercitazioni con il simulatore: L01 dice "esercitazioni in classe da fare in 2", e in `Materiale del docente/` ci sono tre esercizi del simulatore. Le domande sono in `01-copertura.md`.

### Doppioni e file da non usare

- `Esercizi/Note_261103_172930 - Copia.pdf` **non** è una copia: ha un contenuto diverso dall'originale (altre mappe e semplificazioni). Va tenuto e rinominato.
- `_da_verificare/Note_261103_172950.pdf`: un numero e scarabocchi senza testo. Non entra nel prodotto.
- `Materiale del docente/`: esercizi del simulatore Deeds (circuito stampato e sequenze da completare, compilate a mano). Servono come controllo; il circuito va ridisegnato e il testo riformulato, non copiati.

## 2. Problemi tecnici

Gli appunti sono immagini, quindi non ci sono problemi di codifica, di Markdown o di LaTeX nei file originali. I problemi sono di leggibilità e di completezza.

| Livello | Dove | Problema | Correzione proposta |
|---|---|---|---|
| DA CORREGGERE | quasi tutte le lezioni | Le mappe di Karnaugh sono disegnate con le etichette sui lati (stile del libro di testo) e l'ordine delle colonne cambia da un foglio all'altro: in L11 e L12 è YZ = 00, 10, 11, 01 | Nel modulo tutte le mappe in ordine di Gray 00, 01, 11, 10, con le variabili scritte in testa a righe e colonne, ridisegnate in SVG |
| DA CORREGGERE | L02 p. 3, L03 p. 1-2, L06 p. 1 | Mappe 4×4 colorate con letture incerte e senza la tabella di partenza | Rifatte come esempi nuovi e verificati, con la stessa idea |
| DA CORREGGERE | L02 p. 3, L03 p. 2 | Tabella del MUX 4→1 iniziata e non finita | Completata |
| DA CORREGGERE | L06 p. 2, L07 p. 2 | Tabella del FF D non compilata; diagrammi temporali da completare lasciati vuoti | Completati nel modulo 3 |
| DA CORREGGERE | L08 p. 1, L08 p. 2, L09 p. 3 | Diagrammi compilati solo per i primi colpi di clock | Completati |
| DA CORREGGERE | L11, L12 | Mappe di $D_X$, $D_Y$ dell'esercizio ENB/SEL lasciate vuote | Completate |
| NOTA | tutte | Descrizioni dei circuiti solo come disegni | Ogni circuito diventa una figura SVG ridisegnata, con didascalia |
| NOTA | L11 | Il file non ha la data | Domanda all'autore |

## 3. Errori di sostanza trovati

| Livello | Dove | Negli appunti | Corretto |
|---|---|---|---|
| BLOCCANTE | L02 p. 1 | $F = ADC + \bar{C}(\bar{A}D + A(B + D))$ semplificata in $AD + \bar{C}D$: il termine $AB\bar{C}$ si perde all'ultimo passaggio | $F = AD + \bar{C}D + AB\bar{C}$ |
| BLOCCANTE | L02 p. 3 | Mappa con gli 1 in 000, 001, 010, 100, 101: $U = \bar{B} + \bar{A}$ e circuito con una OR | $U = \bar{B} + \bar{A}\bar{C}$ (in 011 la funzione vale 0) |
| BLOCCANTE | L02 p. 3 | Mappa con gli 1 in 001, 010, 100, 110: $U = \bar{A} + A\bar{C}$ [lettura incerta] | $U = \bar{A}\bar{B}C + A\bar{C} + B\bar{C}$ |
| DA CORREGGERE | L02 p. 2 | Esempio con il risultato $\bar{B}C + AB + AC$ | $AC$ è il consenso degli altri due termini: la forma minima è $\bar{B}C + AB$ (lettura della mappa da confermare) |
| DA CORREGGERE | L02 p. 2 | "Diagramma lineare: modo di rappresentare una rete sequenziale" | È il diagramma temporale di una rete combinatoria; le reti sequenziali vengono dopo |
| DA CORREGGERE | L04 p. 1 | Tabella dei numeri a 4 bit: 0001 → 2 [lettura] | 0001 → 1 |
| DA CORREGGERE | L04 p. 2 | Intervallo del complemento a 2: $[-2^{n-1}, \dots, 2^{n-1}]$; tabella a 3 bit senza 111 = −1 | $[-2^{n-1}, 2^{n-1} - 1]$; aggiunta la riga 111 = −1 |
| DA CORREGGERE | L06 p. 1 | "Gruppi in più: sono le alee" | I gruppi in più (termini di consenso) **eliminano** le alee statiche |
| DA CORREGGERE | L06 p. 2, L07 p. 2 | "Tabella (tavola) di eccitazione" per la tabella S R → Q | È la tabella caratteristica; la tabella di eccitazione è quella inversa (transizione → ingressi), come in L11 |
| DA CORREGGERE | L07 p. 1 | Sintesi OR-AND $(\bar{A} + \bar{B})(D + \bar{C})(C + \bar{B})$ [lettura] | Con $(C + \bar{B})$ vale 0 in $\bar{A}B\bar{C}D$, dove la mappa ha 1: il terzo fattore è $(\bar{B} + \bar{C})$ |
| DA CORREGGERE | L08 p. 1 | "$T_{min}$ = frequenza massima del clock" | $T_{min}$ è il periodo minimo; $f_{max} = 1/T_{min}$ |
| DA CORREGGERE | L09 p. 1 | "Contatore modulo 8" per un contatore con 4 FF T | Con 4 FF il contatore è modulo 16; la tabella arriva a 9 (forse si parlava del contatore decimale) |
| DA CORREGGERE | L09 p. 1 | $TC = Q_{k-1} \cdots Q_0$ per il contatore universale | Vale per il conteggio in avanti; all'indietro il conteggio termina su tutti 0 |
| DA CORREGGERE | L11 p. 3 | $J_X = IN\,\bar{X}$ (mappa con la colonna etichettata X invece di Y) | $J_X = IN \cdot Y$ |
| DA CORREGGERE | L12 p. 2 | $J_Z = 1 + START \cdot L$ [lettura] | Dalla mappa $J_Z = X + Y + START \cdot L$ |
| DA CORREGGERE | L13 p. 1 | Clock a 1 MHz → periodo 1 ms | Periodo 1 µs |

Tutte le altre sintesi controllabili sono state verificate con la tabella di verità (script di controllo nella revisione) e sono corrette: L03 (variabili riportate, porta programmabile), L05, L07 (esercizi 1-2, variabili riportate, MUX, conversioni, somme, sottrazioni, prodotti, −11 in complemento a 2), L08 (contatore), L10 (analisi), L11 (luci con FF D e JK, Es. 9 con FF D), L12 (ES. 10, lavatrice tranne $J_Z$), fogli di esercizi.

## 4. Residui da togliere

| Dove | Residuo |
|---|---|
| L01 p. 1 | Date, orari e aula delle prove intermedie; "esercitazioni in classe da fare in 2" |
| L01 p. 1 | Elenco degli insiemi numerici con $\mathbb{N}$ usato per gli interi: è un'introduzione informale, non serve |
| L03 p. 2, L08 p. 1-2, L09 p. 1-2, L10 p. 2, L11 p. 3, Esercitazione 09 | Disegni e scritte a margine non pertinenti, in qualche caso con un nome utente |
| L08 p. 2 | Frase con un'imprecazione accanto al contatore |
| L09 p. 1 | "INUTILE" scritto in grande accanto al contatore |
| L06 p. 3, L08 p. 1 | "Guardare le slide del prof + libro", "dove mi esercito: al libro" |
| L04 p. 3 | "Spiegazione dell'es. 1.6" del libro |

## 5. Rischi per la vendita

| Livello | Dove | Rischio | Cosa fare |
|---|---|---|---|
| BLOCCANTE | L06 p. 3-4 | Due schermate del simulatore incollate dagli esercizi del docente (registro a scorrimento, LFSR con le sequenze da compilare) | Circuito ridisegnato in SVG, testo dell'esercizio riscritto, soluzione propria |
| BLOCCANTE | Esercizi 172951 | Schermata di un ASM del simulatore e foto di un ASM su carta | Ridisegnati |
| DA CORREGGERE | L13 p. 1 | Testo battuto, probabilmente il testo dell'esercizio del docente | Riformulato |
| NOTA | tutto il corso | Le figure sono nello stile del libro di testo (simboli delle porte, ASM) | Si ridisegnano tutte con simboli standard; nessuna figura del libro viene riprodotta |
| NOTA | – | Nessun nome di compagni; l'autore non compare per nome | – |
