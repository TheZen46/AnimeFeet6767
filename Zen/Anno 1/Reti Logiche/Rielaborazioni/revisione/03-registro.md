# Reti Logiche · registro delle correzioni e delle aggiunte

Fasi 4 e 5, svolte il 4 novembre 2026 sulla struttura di `02-struttura.md` (4 moduli), senza fermarsi per l'approvazione su indicazione dell'autore. Per le parti mancanti si è seguita la strada A: aggiunte complete, ciascuna in un blocco `[!aggiunta]` con la fonte.

Il testo di partenza è `trascrizione/`. "L02 p. 3" vuol dire Lezione 02, pagina 3 del PDF originale. Ogni sintesi, tabella e conto dei moduli è stato ricontrollato con la tabella di verità o con una simulazione (script in `strumenti/`); i casi segnati "verificato" sono passati senza differenze.

## 1. Correzioni di sostanza

| # | Modulo, sezione | Prima (appunti) | Dopo | Motivo | Fonte |
|---|---|---|---|---|---|
| 1 | 1, esercizio 1 | $F = ADC + \bar{C}(\bar{A}D + A(B+D))$ semplificata in $AD + \bar{C}D$ (L02 p. 1) | $AD + \bar{C}D + AB\bar{C}$ | Il termine $AB\bar{C}$ si perde all'ultimo passaggio; per $ABCD = 1100$ la rete vale 1 | verificato |
| 2 | 1.5 | Mappa con gli 1 in 000, 001, 010, 100, 101: $U = \bar{B} + \bar{A}$ (L02 p. 3) | $U = \bar{B} + \bar{A}\bar{C}$, con un `[!esempio]` sull'errore | La riga $\bar{A}$ ha 0 in 011 | verificato |
| 3 | 1.5 | Mappa con gli 1 in 001, 010, 100, 110: $\bar{A} + A\bar{C}$ [lettura incerta] (L02 p. 3) | $\bar{A}\bar{B}C + A\bar{C} + B\bar{C}$ | Sintesi sbagliata o mal letta | verificato |
| 4 | 1.4 | Esempio di Shannon con risultato $\bar{B}C + AB + AC$ (L02 p. 2) | Sostituito dall'esempio completo della tabella di L02 p. 1 ($\bar{A}\bar{B} + A\bar{C}$ e $(A + \bar{B})(\bar{A} + \bar{C})$) | $AC$ è il consenso degli altri due termini; la mappa di partenza non è leggibile con sicurezza | verificato |
| 5 | 1.4 | SH2 lasciata a $(A + \bar{B})(\bar{A} + B + \bar{C})(\bar{A} + \bar{B} + \bar{C})$ (L02 p. 1) | Completata: $(A + \bar{B})(\bar{A} + \bar{C})$ | Semplificazione non finita | verificato |
| 6 | 1.4 | Teorema di Shannon versione 1 lasciato in bianco (L02 p. 1) | Enunciato nelle due forme, con la dimostrazione | Mancava | Donzellini e altri |
| 7 | 1.1 | Specifica "$w = 1$ se uno solo degli ingressi è 1" con tre variabili, senza espressione (L01 p. 2) | Detto che non è uno XOR a tre ingressi e rimandato alle forme canoniche | Lo XOR a tre ingressi vale 1 anche per 111 | – |
| 8 | 1.6 | Sintesi OR-AND con il fattore $(C + \bar{B})$ [lettura] (L07 p. 1) | $(\bar{B} + \bar{C})$, con un `[!attenzione]` | Con $(C + \bar{B})$ la sintesi vale 0 in $\bar{A}B\bar{C}D$, dove la mappa ha 1 | verificato |
| 9 | 2.1 | Diagramma "lineare" come rappresentazione di una rete sequenziale (L02 p. 2) | Diagramma temporale di una rete combinatoria, tra le quattro rappresentazioni (1.1) | Le reti sequenziali vengono dopo | – |
| 10 | 2.3 | "I gruppi in più sono le alee" (L06 p. 1) | I gruppi in più (termini di consenso) eliminano le alee statiche | Inversione del significato | Donzellini e altri |
| 11 | 2.4 | 0001 → 2 nella tabella dei numeri a 4 bit [lettura] (L04 p. 1) | 0001 → 1 | Valore sbagliato | – |
| 12 | 2.6 | Intervallo del complemento a 2 $[-2^{n-1}, 2^{n-1}]$; tabella a 3 bit senza 111 (L04 p. 2) | $[-2^{n-1}, 2^{n-1} - 1]$; tabella completa con 111 = −1 | L'estremo superiore è $2^{n-1} - 1$ | verificato |
| 13 | 2.2 | Porta programmabile scritta con $S_1 S_0$ e $S_0 S_1$ in punti diversi | Tabella con l'ordine $S_0 S_1$, coerente con le sintesi | Con l'altro ordine le sintesi non tornano | verificato |
| 14 | 3.2, 3.3 | "Tabella di eccitazione" per la tabella S R → Q e J K → Q (L06 p. 2, L07 p. 2) | Tabella caratteristica; la tabella di eccitazione è quella inversa, con un `[!attenzione]` | Due nomi per due tabelle diverse | Donzellini e altri |
| 15 | 3.4 | "$T_{min}$ = frequenza massima del clock" (L08 p. 1) | $T_{min}$ periodo minimo, $f_{max} = 1/T_{min}$ | Grandezze diverse | – |
| 16 | 3.4 | Clock a 1 MHz → periodo 1 ms (L13 p. 1) | Periodo $1\ \mu$s, nel blocco `[!attenzione]` | Errore di un fattore 1000 | – |
| 17 | 3.6 | "Contatore modulo 8" con 4 FF T (L09 p. 1) | Contatore modulo 16; il modulo 10 trattato a parte | Con 4 FF si contano 16 stati | – |
| 18 | 3.6 | $TC = Q_{k-1} \cdots Q_0$ per il contatore universale (L09 p. 1) | Vale per il conteggio in avanti; all'indietro l'ultimo stato è $00\dots0$ | Precisazione | – |
| 19 | 4.6 | $J_X = IN\,\bar{X}$ (L11 p. 3, mappa con la colonna etichettata X invece di Y) | $J_X = IN \cdot Y$, con un `[!attenzione]` | Con $IN\,\bar{X}$ la macchina va da a in c | verificato |
| 20 | 4.8 | $J_Z = 1 + START \cdot L$ [lettura] (L12 p. 2) | $J_Z = X + Y + START \cdot L$, con un `[!attenzione]` | $1 + \dots = 1$ farebbe partire la lavatrice senza $START$ | verificato |
| 21 | 4.6 | Esercizio ENB/SEL con le mappe di $D_X$, $D_Y$ vuote (L11 p. 3) | $D_X = ENB(X + SEL\,\bar{Y})$, $D_Y = ENB(Y + \overline{SEL}\,\bar{X})$ | Esercizio non finito | verificato |
| 22 | 3.7 | Sequenze dell'esercizio con il registro a retroazione non compilate (L06 p. 4) | Sequenze complete per $IN$ fisso a 1 e per un solo impulso | Esercizio non finito | simulazione |
| 23 | 4.5 | Rilevatore di fronti "a 2 stati" con un diagramma a 4 stati (L09 p. 3) | Versione di Moore a 4 stati e di Mealy a 2 stati, con un `[!dubbio]` | Incoerenza interna | – |
| 24 | 4.5 | Titolo "Cronometro" per il rilevatore di impulso lungo (L10 p. 1-2) | "Rilevatore di impulso lungo" | Il nome non descrive la specifica | – |
| 25 | 2, esercizio 1 | Esercizio del MUX senza lo schema leggibile (L07 p. 2) | Presentato dalla tabella di verità, con la lettura $U = A \cdot \overline{B \oplus C}$ | Lo schema non si legge per intero | verificato |

Verificate e lasciate come negli appunti (con la sola riscrittura): le sintesi delle variabili riportate (L03, L07), la porta programmabile (L03), la mappa a scacchiera di L05, gli esercizi 1-2 di L07, il MUX di L07, conversioni, somme, sottrazioni e prodotti di L04 e L07, $-11$ in complemento a 2, il contatore a 2 bit di L08, l'analisi di L10, la macchina delle luci con FF D e JK (L11), l'Es. 9 con FF D (L11), l'ES. 10 in tre versioni (L12), la lavatrice a parte $J_Z$ (L12), le mappe dei fogli di esercizi.

## 2. Correzioni di forma

- Tutte le mappe riscritte come tabelle con le variabili in testa e l'ordine di Gray 00, 01, 11, 10 (in L11 e L12 l'ordine delle colonne era YZ = 00, 10, 11, 01).
- Notazione uniformata secondo `notazione.md`: negazione con la barra (niente "!" e apici), $Q^+$ per lo stato successivo, CK per il clock, SOP e POS al posto di SH1 e SH2.
- Tolti: date e aula delle prove (L01), "esercitazioni da fare in 2", rimandi alle slide e al libro, l'esercizio "1.6" del libro, disegni e scritte a margine, la frase con l'imprecazione (L08), "INUTILE" (L09).
- Le analogie ("come il tubo dell'acqua") sono sostituite dalla definizione del ritardo di propagazione.
- Le schermate del simulatore e le foto di ASM sono sostituite da figure ridisegnate; i testi battuti degli esercizi (L13) sono riscritti.
- 25 figure ridisegnate in SVG (`figure/`), numerate per modulo.

## 3. Aggiunte

Le parole sono contate nei blocchi `[!aggiunta]` dei moduli.

| Modulo, sezione | Aggiunta | ID | Fonte | Parole |
|---|---|---|---|---|
| 1.3 | Proprietà dell'algebra di Boole in tabella, principio di dualità | RL-01 | Donzellini e altri | ~250 |
| 1.4 | Mintermini e maxtermini | RL-01 | Donzellini e altri | ~90 |
| 1.5 | Implicanti primi ed essenziali, procedimento di copertura | RL-02 | Donzellini e altri | ~110 |
| 1.7 | Da POS a sole NOR | RL-02 | Donzellini e altri | ~50 |
| 2.2 | Encoder ed encoder con priorità | RL-02 | Donzellini e altri | ~140 |
| 2.3 | Termine di consenso contro le alee statiche | RL-02 | Donzellini e altri | ~120 |
| 2.6 | Estensione del segno | RL-03 | Donzellini e altri | ~50 |
| 2.6 | Overflow in complemento a 2, sottrattore | RL-03 | Donzellini e altri | ~150 |
| 2.7 | Comparatore | RL-03 | Donzellini e altri | ~80 |
| 3.1 | Stato ed equazione caratteristica | RL-04 | Donzellini e altri | ~80 |
| 3.2 | Trasparenza e metastabilità | RL-04 | Donzellini e altri | ~140 |
| 3.3 | Schema master-slave | RL-04 | Donzellini e altri | ~90 |
| 3.4 | Periodo minimo di una rete sincrona e vincolo di hold | RL-05 | Donzellini e altri | ~140 |
| 3.6 | Contatore modulo N, abilitazione e cascata | RL-05 | Donzellini e altri | ~130 |
| 4.3 | Scelta della codifica degli stati | RL-06 | Donzellini e altri | ~110 |
| 4.4 | Procedura di analisi di una MSF | RL-06 | Donzellini e altri | ~80 |
| 4.9 | Controllore e datapath, con l'esempio della misura di un impulso svolto sulla specifica dei fogli | RL-07 | Donzellini e altri; Esercizi 172948 | ~360 |
| 4.10 | Verifica con il simulatore | RL-08 | obiettivi del corso; Donzellini e altri | ~140 |

Le aggiunte pesano l'11% del modulo 1, il 13% del 2, il 15% del 3 e il 14% del 4: meno della stima della fase 3, perché le parti scritte negli appunti si sono rivelate più complete una volta trascritte.

Sono stati scritti anche esempi ed esercizi svolti nuovi, fuori dai blocchi di aggiunta perché applicano solo ciò che è già nel testo: la mappa a quattro variabili di 1.5, il generatore di parità, la frequenza massima del contatore, il registro universale, il FF T da un FF D, il comportamento della macchina delle luci dagli stati non usati, il rilevatore di fronti di Mealy.

> Il testo di Donzellini e altri non era tra i file forniti: le aggiunte seguono gli argomenti del programma con nozioni standard, e le fonti sono citate senza numero di capitolo. Conviene controllarle sulla propria copia del libro (domanda nell'elenco finale).

## Ampliamento del 5 novembre 2026

Dopo le risposte alle domande (`revisione/AMPLIAMENTO-ANNO-1.md`).

| Dove | Che cosa | Motivo |
|---|---|---|
| 2.8 (nuovo) | Virgola mobile e IEEE 754: formato a 32 e 64 bit, esponente polarizzato, bit nascosto, valori speciali, somma | RL-4: non chiesto all'esame, da spiegare |
| 3.3 | FF D con abilitazione (E-PET) | usato negli esercizi del simulatore |
| 3.7 | Il dubbio sul JK di L07-L08 diventa una nota: un JK con $K = \overline{IN}$ è un FF D | dubbio non risolvibile dagli appunti |
| 4.5 | Rilevatore di fronti: 4 stati come nel diagramma (Moore), 2 nella versione Mealy | RL-8 |
| 4.8 | Lavatrice: lo stato stop resta fermo fino al reset | RL-7 |
| Esercizi dei moduli 1-4 | 27 esercizi del laboratorio sul modello delle esercitazioni Deeds, con testi, dati e soluzioni nuovi | RL-1, RL-3, RL-11 |
| 4, esercizio 7 | Ricevitore seriale del pacchetto $1\,1\,B\,0\,0$, specifica ricostruita | RL-12: specifica non trovata nei file |
| Tutti i moduli | Sezione "Esercizi guidati" (12 esercizi passo per passo) e "Formulario" con termini e domande per l'orale | richiesta del 5/11 |

RL-9: la semplificazione dell'esercizio 1 del modulo 1 è stata ricontrollata ($F = AD + \bar{C}D + AB\bar{C}$, verificata su tutte le combinazioni in `strumenti/verifica_modulo1.py`). RL-5: il contatore della lezione 9 è quello modulo 16 a 4 FF, ora svolto anche con i FF D (esercizio 12 del modulo 3). RL-2, RL-6: senza risposta, il testo resta com'era.

Tutti gli esercizi nuovi sono controllati da `strumenti/verifica_ampliamento.py` (induzione perfetta sulle espressioni, simulazione fronte per fronte delle sequenze, conversioni IEEE 754 con la libreria standard).
