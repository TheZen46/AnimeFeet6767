# Analisi Matematica 1B · fase 1: inventario e integrità

Corso: Analisi Matematica 1B (6 CFU, 1° anno, 2° semestre). Programma di riferimento: `revisione/programmi/analisi-matematica-1b.md` (UniGe 2026/27).
Originali: `Analisi/1B/Appunti_mano/` (22 lezioni e 3 fascicoli tematici, scritti a mano), `Analisi/1B/Esercizi/` (5 PDF), `Analisi/1B/Rielaborazioni/` (4 dispense battute, con testo selezionabile). Nessun originale è stato modificato.

## 1. Come sono stati usati gli originali

Il corso ha, oltre alle lezioni a mano, quattro **dispense battute** del giugno 2026 (Calcolo integrale, Serie numeriche, Spazi euclidei, Equazioni differenziali, ~20.000 parole in tutto) che riscrivono in forma estesa le stesse lezioni. Il loro testo è stato estratto in `trascrizione/D1`…`D4` ed è la base testuale dei moduli. Le lezioni a mano sono state lette tutte per l'inventario e la copertura (`trascrizione/L - indice delle lezioni.md`) e ingrandite dove servivano per controllare esempi ed esercizi; non sono state trascritte parola per parola, perché il loro contenuto è già nelle dispense.

| File | Pagine | Parole | Contenuto |
|---|---|---|---|
| D1 Calcolo integrale | 15 | ~5.300 | Primitive, metodi, razionali, Riemann, media, teorema fondamentale, impropri |
| D2 Serie numeriche | 17 | ~3.500 | Definizioni, geometrica e telescopiche, condizione necessaria, criteri, Leibniz |
| D3 Spazi euclidei | 17 | ~6.100 | $\mathbb{R}^n$, topologia, limiti, derivate, differenziabilità, Hessiana, estremi |
| D4 Equazioni differenziali | 15 | ~5.500 | Modelli, separabili, lineari, secondo ordine, sistemi, stabilità |
| 22 lezioni a mano | 36 di 66 | – | Indice in `trascrizione/` |
| Esercizi | 7 | – | Primitive, integrali, integrali definiti, due fogli sparsi |

### Lezioni mancanti

Le lezioni sono il martedì e il giovedì. Manca la **lezione 22** (presumibilmente 19/05/2026); dopo la 23 (21/05) non ci sono altri file. Le dispense coprono anche la stabilità dei sistemi lineari, che nelle lezioni a mano presenti non compare: probabilmente era nella lezione 22.

### Doppioni

Le quattro dispense in `_da_verificare/doppioni/` hanno gli stessi titoli di quelle in `Rielaborazioni/` e dimensioni quasi uguali (pochi KB di differenza): sono probabilmente altre esportazioni degli stessi file. Non sono state aperte né usate.

## 2. Problemi tecnici delle dispense

| Livello | Dove | Problema | Correzione |
|---|---|---|---|
| BLOCCANTE | D1, D2, D4 | ~390 rimandi `[cite: …]` rimasti nel testo, residuo dello strumento con cui sono state scritte | Tolti |
| BLOCCANTE | D1, D2, D3 | Due numeri di matricola nel frontespizio ("Rielaborato da S… e S…") | Tolti; domanda 1 |
| BLOCCANTE | D4 § 5.2.2 | Esempio di sistema con autovalore carente segnato "[Nota: … VERIFICARE]": la matrice data ha polinomio caratteristico $-\lambda^3 + 4\lambda - 4$, non $-\lambda(\lambda - 2)^2$, e i conti successivi non tornano | Sostituito con un esempio nuovo verificato |
| DA CORREGGERE | D1, D2, D3, D4 | "Spazio riservato a uno schema", "Figura N: spazio per diagramma": figure mai disegnate | Tre figure ridisegnate (somme di Riemann, criterio integrale, curve di livello); le altre sostituite dal testo |
| DA CORREGGERE | D4 § 4.2 | "Figura 2: ritratto stilizzato di un personaggio, somigliante ai disegni dei fumetti" (disegno a margine) | Tolto |
| DA CORREGGERE | D2 § 4.4 | Le conclusioni del criterio del rapporto e della radice sono ripetute due volte | Unificate |
| DA CORREGGERE | D3 § 2.3 | Definizione di insieme connesso illeggibile (le barre delle chiusure sono andate perse) | Riscritta |
| DA CORREGGERE | D4 | Notazione $f(y, t)$ nei sistemi e $f(t, y)$ altrove | Uniformata a $f(t, y)$ |
| NOTA | D3 | Usa il grassetto per i vettori, gli appunti la sottolineatura | Si usa il carattere normale, detto una volta |

## 3. Errori di sostanza trovati

| Livello | Dove | Nelle dispense o negli appunti | Corretto |
|---|---|---|---|
| BLOCCANTE | D4 § 5.2.2 | Esempio dell'autovalore carente (vedi sopra) | Esempio nuovo, verificato |
| DA CORREGGERE | D4 § 3.1, teorema 3.1 | Domini di $g$ e $h$ scambiati rispetto alla definizione; unicità "se $h \in C^1$ **e** $h(y_0) \neq 0$" | Unicità se $h \in C^1$ (o localmente lipschitziana) **oppure** se $h(y_0) \neq 0$ |
| DA CORREGGERE | D4 § 3.2, Peano | Soluzione resa come "$\frac{2}{3}t^{3/2}$" [lettura dell'estrazione] | $\left(\frac{2t}{3}\right)^{3/2}$, che è quella che risolve $y' = \sqrt[3]{y}$ |
| DA CORREGGERE | L06 p. 1 | $\frac{1}{x^2\sin x} \sim \frac{1}{x^3}$ "di ordine 4" [lettura] | Ordine 3 (la conclusione, divergenza, resta) |
| DA CORREGGERE | D1 § 3.3 | Integrabili "le funzioni continue (anche a tratti)" | Limitate e con un numero finito di discontinuità |
| NOTA | D1 § 2.3 | "Sia $f$ integrabile in $J$ con primitiva $F$" | Basta l'esistenza della primitiva |
| NOTA | D3 § 7.2 | Fermat enunciato per $f$ differenziabile | Basta la derivabilità |

Tutti gli esempi e gli esercizi dei moduli sono stati ricalcolati con uno script simbolico (`strumenti/verifica.py`): primitive, integrali, somme di serie, gradienti, punti critici, soluzioni delle equazioni e dei sistemi. Gli esempi delle dispense che tornano sono stati tenuti.

## 4. Rischi per la vendita

| Livello | Rischio | Cosa fare |
|---|---|---|
| BLOCCANTE | Le dispense sono firmate con **due** matricole: potrebbe esserci un coautore | Domanda 1, prima di mettere in vendita |
| DA CORREGGERE | Le dispense sono state scritte con uno strumento di scrittura assistita (lo dicono i rimandi `[cite]`): il testo è stato riformulato nei moduli, non copiato | Fatto |
| NOTA | Nessun testo copiato da libri o slide; nessun nome di compagni o docenti nei moduli | – |
