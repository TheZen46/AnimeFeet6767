# Analisi Matematica 1A · fase 7: controllo finale

Controllo del 3 novembre 2026 sui moduli in `moduli/` e su `corso-completo.md`.

## 1. Controlli della fase 1 ripetuti

| Controllo | Esito |
|---|---|
| Un solo `#` per modulo, sezioni `## N.k` in ordine | ok in tutti e 5 |
| Formule: `$` e `$$` bilanciati, LaTeX valido | ok: tutte le formule passano il controllo con KaTeX (0 errori) |
| Sintassi non esportabile (`[[link]]`, `![[…]]`, `%%`, blocchi di plugin) | assente |
| Residui (TODO, ???, abbreviazioni da appunto, disegni, espressioni colloquiali) | assenti |
| Rimandi a pagine o appendici del libro | tolti. Resta il nome del testo nelle fonti delle aggiunte, che sparisce nella fase 8 |
| Figure | 19, tutte ridisegnate in `figure/` (SVG) e inserite con una didascalia numerata (Figura N.k) |
| Callout | solo quelli ammessi (definizione, teorema, esempio, nota, attenzione), più i marcatori di revisione `[!aggiunta]` |

## 2. Copertura

Tutti i 18 argomenti del programma sono coperti (`01-copertura.md`, § 5). Uno solo resta da confermare: AM1A-18, l'induzione, aggiunta nel paragrafo 1.4 senza sapere se è stata fatta a lezione.

## 3. Marcatori ancora presenti

| Modulo | `[!aggiunta]` | `[!dubbio]` | `[!figura]` |
|---|---|---|---|
| 1 · Numeri reali e funzioni | 6 | 0 | 0 |
| 2 · Successioni e limiti | 5 | 0 | 0 |
| 3 · Continuità e confronto locale | 4 | 0 | 0 |
| 4 · Derivate e teoremi del valor medio | 2 | 0 | 0 |
| 5 · Monotonia, convessità, studio di funzione e Taylor | 5 | 0 | 0 |

Nessun dubbio aperto nel testo: le domande per te sono in `01-copertura.md`, § 4.

## 4. Nomi e testo copiato

| Controllo | Esito |
|---|---|
| Firma | solo "Mobius" (front matter e frontespizio) |
| Nomi di persone | nessuno, a parte gli autori dei teoremi e dei testi citati |
| Testo copiato | le aggiunte sono riformulate. Gli enunciati standard (definizioni, teoremi) sono scritti in forma propria |

## 5. Dimensioni

Le pagine sono misurate sull'anteprima A4 di `corso-completo.md`, con figure e callout. Le parole contano anche le formule.

| Modulo | Titolo | Parole | Pagine A4 |
|---|---|---|---|
| 1 | Numeri reali e funzioni | ~4800 | 9 |
| 2 | Successioni e limiti | ~3800 | 7 |
| 3 | Continuità e confronto locale | ~3400 | 6 |
| 4 | Derivate e teoremi del valor medio | ~3600 | 8 |
| 5 | Monotonia, convessità, studio di funzione e Taylor | ~3600 | 7 |
| | **Corso completo** (con frontespizio e indice) | ~19.200 | **38** |

## 6. Catalogo

I titoli dei moduli coincidono con quelli già in `catalog.yaml`, quindi non c'è niente da cambiare. Dopo la fase 8 si può aggiungere `pagine: 38` alla voce del corso, così la scheda sul sito mostra la lunghezza.

## 7. Da controllare a mano prima di esportare

1. **Le aggiunte** (22 blocchi, elenco in `03-registro.md`). Contano soprattutto le parti che sostituiscono le lezioni mancanti: i teoremi sui limiti (2.6), esponenziali, logaritmi e trigonometria (1.8), applicazioni di Taylor (5.8). Verifica che siano coerenti con quanto fatto a lezione.
2. **Le 28 correzioni di sostanza** del registro, in particolare le cinque bloccanti (§ 1, righe 1-5).
3. **Le figure:** che corrispondano a quelle che avevi disegnato e che si leggano bene una volta esportate.
4. **Le risposte alle domande** di `01-copertura.md`, § 4. Se arriva materiale delle lezioni del 14/10 e del 28/10, le aggiunte dei paragrafi 1.8 e 2.6 si confrontano con quello.
5. **I numeri di capitolo del Canuto-Tabacco** citati nelle fonti, sull'edizione che usi.
6. **L'esportazione da Obsidian:** A4 verticale, figure SVG visibili, callout resi come riquadri. L'anteprima fatta qui ha 38 pagine, quella di Obsidian può variare di qualche pagina.

Dopo le tue verifiche si passa alla fase 8: si tolgono i marcatori `[!aggiunta]` lasciando il testo, si aggiorna la versione e si rigenera `corso-completo.md` con `python revisione/corso_completo.py analisi-matematica-1a`.# Analisi Matematica 1A · fase 7: controllo finale

Controllo del 3 novembre 2026 sui moduli in `moduli/` e su `corso-completo.md`.

## 1. Controlli della fase 1 ripetuti

| Controllo | Esito |
|---|---|
| Un solo `#` per modulo, sezioni `## N.k` in ordine | ok in tutti e 5 |
| Formule: `$` e `$$` bilanciati, LaTeX valido | ok: tutte le formule passano il controllo con KaTeX (0 errori) |
| Sintassi non esportabile (`[[link]]`, `![[…]]`, `%%`, blocchi di plugin) | assente |
| Residui (TODO, ???, abbreviazioni da appunto, disegni, espressioni colloquiali) | assenti |
| Rimandi a pagine o appendici del libro | tolti. Resta il nome del testo nelle fonti delle aggiunte, che sparisce nella fase 8 |
| Figure | 19, tutte ridisegnate in `figure/` (SVG) e inserite con una didascalia numerata (Figura N.k) |
| Callout | solo quelli ammessi (definizione, teorema, esempio, nota, attenzione), più i marcatori di revisione `[!aggiunta]` |

## 2. Copertura

Tutti i 18 argomenti del programma sono coperti (`01-copertura.md`, § 5). Uno solo resta da confermare: AM1A-18, l'induzione, aggiunta nel paragrafo 1.4 senza sapere se è stata fatta a lezione.

## 3. Marcatori ancora presenti

| Modulo | `[!aggiunta]` | `[!dubbio]` | `[!figura]` |
|---|---|---|---|
| 1 · Numeri reali e funzioni | 6 | 0 | 0 |
| 2 · Successioni e limiti | 5 | 0 | 0 |
| 3 · Continuità e confronto locale | 4 | 0 | 0 |
| 4 · Derivate e teoremi del valor medio | 2 | 0 | 0 |
| 5 · Monotonia, convessità, studio di funzione e Taylor | 5 | 0 | 0 |

Nessun dubbio aperto nel testo: le domande per te sono in `01-copertura.md`, § 4.

## 4. Nomi e testo copiato

| Controllo | Esito |
|---|---|
| Firma | solo "Mobius" (front matter e frontespizio) |
| Nomi di persone | nessuno, a parte gli autori dei teoremi e dei testi citati |
| Testo copiato | le aggiunte sono riformulate. Gli enunciati standard (definizioni, teoremi) sono scritti in forma propria |

## 5. Dimensioni

Le pagine sono misurate sull'anteprima A4 di `corso-completo.md`, con figure e callout. Le parole contano anche le formule.

| Modulo | Titolo | Parole | Pagine A4 |
|---|---|---|---|
| 1 | Numeri reali e funzioni | ~4800 | 9 |
| 2 | Successioni e limiti | ~3800 | 7 |
| 3 | Continuità e confronto locale | ~3400 | 6 |
| 4 | Derivate e teoremi del valor medio | ~3600 | 8 |
| 5 | Monotonia, convessità, studio di funzione e Taylor | ~3600 | 7 |
| | **Corso completo** (con frontespizio e indice) | ~19.200 | **38** |

## 6. Catalogo

I titoli dei moduli coincidono con quelli già in `catalog.yaml`, quindi non c'è niente da cambiare. Dopo la fase 8 si può aggiungere `pagine: 38` alla voce del corso, così la scheda sul sito mostra la lunghezza.

## 7. Da controllare a mano prima di esportare

1. **Le aggiunte** (22 blocchi, elenco in `03-registro.md`). Contano soprattutto le parti che sostituiscono le lezioni mancanti: i teoremi sui limiti (2.6), esponenziali, logaritmi e trigonometria (1.8), applicazioni di Taylor (5.8). Verifica che siano coerenti con quanto fatto a lezione.
2. **Le 28 correzioni di sostanza** del registro, in particolare le cinque bloccanti (§ 1, righe 1-5).
3. **Le figure:** che corrispondano a quelle che avevi disegnato e che si leggano bene una volta esportate.
4. **Le risposte alle domande** di `01-copertura.md`, § 4. Se arriva materiale delle lezioni del 14/10 e del 28/10, le aggiunte dei paragrafi 1.8 e 2.6 si confrontano con quello.
5. **I numeri di capitolo del Canuto-Tabacco** citati nelle fonti, sull'edizione che usi.
6. **L'esportazione da Obsidian:** A4 verticale, figure SVG visibili, callout resi come riquadri. L'anteprima fatta qui ha 38 pagine, quella di Obsidian può variare di qualche pagina.

Dopo le tue verifiche si passa alla fase 8: si tolgono i marcatori `[!aggiunta]` lasciando il testo, si aggiorna la versione e si rigenera `corso-completo.md` con `python revisione/corso_completo.py analisi-matematica-1a`.

## Fase 8 (5 novembre 2026)

| Controllo | Esito |
|---|---|
| Marcatori `[!aggiunta]` | 40 tolti, lasciando il testo (le fonti restano in `03-registro.md`) |
| `[!dubbio]`, `[!figura]` senza immagine | nessuno |
| Conti e programmi | verificatori in `strumenti/` rieseguiti dopo la pulizia, nessun errore |
| KaTeX, spaziatura, frasi di servizio | nessun errore; tolte le frasi che rimandavano agli strumenti di revisione |
| Anteprima PDF | 52 pagine A4 (valore usato in `catalog.yaml`) |
| Parole | circa 30.700 |
| `corso-completo.md` | rigenerato |

