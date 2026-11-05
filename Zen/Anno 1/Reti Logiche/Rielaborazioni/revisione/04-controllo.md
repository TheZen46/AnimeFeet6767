# Reti Logiche · fase 7: controllo finale

Controllo del 4 novembre 2026 sui moduli in `moduli/` e su `corso-completo.md`.

## 1. Integrità tecnica

| Controllo | Esito |
|---|---|
| Front matter comune (corso, modulo, titolo, programma, anno_accademico, autore: Mobius, versione) | presente in tutti e 4 i moduli |
| Un solo `#` per file, sezioni `## N.k` in ordine | sì |
| `$` bilanciati | sì (conteggio pari in tutti i moduli) |
| LaTeX valido | sì: 0 errori con KaTeX su tutte le formule |
| Sintassi non esportabile (`[[…]]`, `![[…]]`, Dataview, Templater) | assente |
| Liste dentro i callout | precedute da una riga vuota, così si esportano anche con Pandoc |
| Figure | 25 SVG in `figure/`, tutte referenziate, nessun riferimento mancante |
| Tabelle | le più larghe hanno 7 colonne (encoder, DEMUX): stanno in A4 verticale |
| Anteprima PDF | 37 pagine A4, generata con Pandoc e KaTeX senza errori |

## 2. Copertura

Tutti gli argomenti del programma sono coperti (tabella al § 5 di `01-copertura.md`). RL-07 e RL-08 sono scritti come aggiunte, in attesa della domanda 3.

## 3. Marcatori ancora presenti

| Modulo | `[!aggiunta]` | `[!dubbio]` | `[!figura]` senza immagine |
|---|---|---|---|
| 1 | 4 | 0 | 0 |
| 2 | 5 | 0 | 0 |
| 3 | 5 | 1 (collegamento di $K$ nell'esempio dei due FF, § 3.7) | 0 |
| 4 | 4 | 2 (rilevatore di fronti § 4.5; stato finale della lavatrice § 4.8) | 0 |

## 4. Rischi per la vendita

- Nessun nome reale dell'autore, nessun nome di compagni, nessun nome utente: i disegni a margine che lo contenevano non sono stati trascritti nei moduli.
- Nessun testo copiato: le definizioni sono riformulate, le schermate del simulatore e la foto dell'ASM sono sostituite da figure ridisegnate, il testo battuto del trasmettitore è riscritto.
- Nessun residuo di lezione (date, aule, rimandi alle slide, imprecazioni).

## 5. Dimensioni

| Modulo | Titolo proposto per il catalogo | Parole | Pagine A4 (stima a 500 parole) |
|---|---|---|---|
| 1 | Algebra booleana e sintesi delle reti combinatorie | ~4850 | ~10 |
| 2 | Reti combinatorie standard, ritardi e aritmetica | ~4250 | ~9 |
| 3 | Flip-flop, registri e contatori | ~3650 | ~8 (più figure) |
| 4 | Macchine a stati finiti e progetto con ASM | ~4750 | ~10 |
| Corso completo | – | ~17400 | 37 nell'anteprima PDF |

I titoli e gli argomenti dei moduli, le pagine (37) e tre pagine di anteprima sono già nel catalogo, così la scheda del sito mostra l'indice e il programma.

## 6. Cosa controllare a mano prima di esportare

1. Le risposte alle domande di `01-copertura.md` § 4, in particolare la 3 (controllore-datapath e simulazione) e le letture incerte (6, 7, 8, 9).
2. I tre `[!dubbio]` dei moduli 3 e 4.
3. Le figure, una per una, contro i circuiti degli appunti: sono state ridisegnate da zero e semplificate.
4. Le fonti delle aggiunte sulla propria copia del libro di testo, che non era tra i file forniti.
5. Gli esercizi svolti nuovi (segnati nel registro, § 3): sono stati ricalcolati con uno script, ma vanno letti.

Dopo le verifiche si fa la fase 8: si tolgono i marcatori `[!aggiunta]` lasciando il testo, si risolvono i `[!dubbio]`, si aggiorna la versione e si rigenera `corso-completo.md` con `python revisione/corso_completo.py reti-logiche`.# Reti Logiche · fase 7: controllo finale

Controllo del 4 novembre 2026 sui moduli in `moduli/` e su `corso-completo.md`.

## 1. Integrità tecnica

| Controllo | Esito |
|---|---|
| Front matter comune (corso, modulo, titolo, programma, anno_accademico, autore: Mobius, versione) | presente in tutti e 4 i moduli |
| Un solo `#` per file, sezioni `## N.k` in ordine | sì |
| `$` bilanciati | sì (conteggio pari in tutti i moduli) |
| LaTeX valido | sì: 0 errori con KaTeX su tutte le formule |
| Sintassi non esportabile (`[[…]]`, `![[…]]`, Dataview, Templater) | assente |
| Liste dentro i callout | precedute da una riga vuota, così si esportano anche con Pandoc |
| Figure | 25 SVG in `figure/`, tutte referenziate, nessun riferimento mancante |
| Tabelle | le più larghe hanno 7 colonne (encoder, DEMUX): stanno in A4 verticale |
| Anteprima PDF | 37 pagine A4, generata con Pandoc e KaTeX senza errori |

## 2. Copertura

Tutti gli argomenti del programma sono coperti (tabella al § 5 di `01-copertura.md`). RL-07 e RL-08 sono scritti come aggiunte, in attesa della domanda 3.

## 3. Marcatori ancora presenti

| Modulo | `[!aggiunta]` | `[!dubbio]` | `[!figura]` senza immagine |
|---|---|---|---|
| 1 | 4 | 0 | 0 |
| 2 | 5 | 0 | 0 |
| 3 | 5 | 1 (collegamento di $K$ nell'esempio dei due FF, § 3.7) | 0 |
| 4 | 4 | 2 (rilevatore di fronti § 4.5; stato finale della lavatrice § 4.8) | 0 |

## 4. Rischi per la vendita

- Nessun nome reale dell'autore, nessun nome di compagni, nessun nome utente: i disegni a margine che lo contenevano non sono stati trascritti nei moduli.
- Nessun testo copiato: le definizioni sono riformulate, le schermate del simulatore e la foto dell'ASM sono sostituite da figure ridisegnate, il testo battuto del trasmettitore è riscritto.
- Nessun residuo di lezione (date, aule, rimandi alle slide, imprecazioni).

## 5. Dimensioni

| Modulo | Titolo proposto per il catalogo | Parole | Pagine A4 (stima a 500 parole) |
|---|---|---|---|
| 1 | Algebra booleana e sintesi delle reti combinatorie | ~4850 | ~10 |
| 2 | Reti combinatorie standard, ritardi e aritmetica | ~4250 | ~9 |
| 3 | Flip-flop, registri e contatori | ~3650 | ~8 (più figure) |
| 4 | Macchine a stati finiti e progetto con ASM | ~4750 | ~10 |
| Corso completo | – | ~17400 | 37 nell'anteprima PDF |

I titoli e gli argomenti dei moduli, le pagine (37) e tre pagine di anteprima sono già nel catalogo, così la scheda del sito mostra l'indice e il programma.

## 6. Cosa controllare a mano prima di esportare

1. Le risposte alle domande di `01-copertura.md` § 4, in particolare la 3 (controllore-datapath e simulazione) e le letture incerte (6, 7, 8, 9).
2. I tre `[!dubbio]` dei moduli 3 e 4.
3. Le figure, una per una, contro i circuiti degli appunti: sono state ridisegnate da zero e semplificate.
4. Le fonti delle aggiunte sulla propria copia del libro di testo, che non era tra i file forniti.
5. Gli esercizi svolti nuovi (segnati nel registro, § 3): sono stati ricalcolati con uno script, ma vanno letti.

Dopo le verifiche si fa la fase 8: si tolgono i marcatori `[!aggiunta]` lasciando il testo, si risolvono i `[!dubbio]`, si aggiorna la versione e si rigenera `corso-completo.md` con `python revisione/corso_completo.py reti-logiche`.

## Fase 8 (5 novembre 2026)

| Controllo | Esito |
|---|---|
| Marcatori `[!aggiunta]` | 32 tolti, lasciando il testo (le fonti restano in `03-registro.md`) |
| `[!dubbio]`, `[!figura]` senza immagine | nessuno |
| Conti e programmi | verificatori in `strumenti/` rieseguiti dopo la pulizia, nessun errore |
| KaTeX, spaziatura, frasi di servizio | nessun errore; tolte le frasi che rimandavano agli strumenti di revisione |
| Anteprima PDF | 55 pagine A4 (valore usato in `catalog.yaml`) |
| Parole | circa 30.800 |
| `corso-completo.md` | rigenerato |

