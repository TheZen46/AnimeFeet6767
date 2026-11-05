# Statistica · fase 7: controllo finale

Controllo del 4 novembre 2026.

| Controllo | Esito |
|---|---|
| Front matter comune, un solo `#`, sezioni `## N.k` | sì, in tutti e 4 i moduli |
| LaTeX valido | 0 errori con KaTeX |
| Sintassi non esportabile (plugin, `[[link]]`, incorporamenti) | assente |
| Elenchi e tabelle dentro i callout | preceduti da una riga vuota, si esportano con Pandoc |
| Figure | 7 SVG, tutte referenziate |
| Conti | 157 controlli in `strumenti/verifica.py`, nessun errore |
| Anteprima PDF | 37 pagine A4 (circa 17.600 parole) |
| Residui (matricola, segnaposto delle figure, tabella incollata) | assenti nei moduli |
| Nomi reali, compagni, docenti | assenti nei moduli |
| Build del sito, test | `python build.py`, 91 test Python e 34 test Node superati |

| Modulo | Titolo per il catalogo | Parole | `[!aggiunta]` | Quota aggiunte | `[!dubbio]` |
|---|---|---|---|---|---|
| 1 | Statistica descrittiva | ~3700 | 4 | ~12% | 0 |
| 2 | Probabilità e variabili aleatorie | ~4800 | 1 | ~2% | 0 |
| 3 | Valori attesi, leggi notevoli e teoremi limite | ~5000 | 1 | ~2% | 0 |
| 4 | Inferenza: stima, intervalli e test | ~4100 | 5 | ~37% | 0 |

Copertura: STA-01…13 e STA-17, 18 dagli appunti (con brevi aggiunte); STA-14, 15, 16 solo da aggiunte (`01-copertura.md`).

Da controllare a mano prima di esportare:
1. La domanda 1 di `01-copertura.md`: il modulo 4 ha sezioni intere (4.5-4.8) che non vengono dai tuoi appunti.
2. La sezione 1.7 sulla regressione, costruita dal formulario (domanda 2).
3. Gli esempi costruiti per il modulo, segnati nel registro: paradosso di Simpson, differenza di medie, ANOVA.
4. Le sette figure.

Poi la fase 8: si tolgono i marcatori `[!aggiunta]`, si aggiorna la versione e si rigenera `corso-completo.md`.# Statistica · fase 7: controllo finale

Controllo del 4 novembre 2026.

| Controllo | Esito |
|---|---|
| Front matter comune, un solo `#`, sezioni `## N.k` | sì, in tutti e 4 i moduli |
| LaTeX valido | 0 errori con KaTeX |
| Sintassi non esportabile (plugin, `[[link]]`, incorporamenti) | assente |
| Elenchi e tabelle dentro i callout | preceduti da una riga vuota, si esportano con Pandoc |
| Figure | 7 SVG, tutte referenziate |
| Conti | 157 controlli in `strumenti/verifica.py`, nessun errore |
| Anteprima PDF | 37 pagine A4 (circa 17.600 parole) |
| Residui (matricola, segnaposto delle figure, tabella incollata) | assenti nei moduli |
| Nomi reali, compagni, docenti | assenti nei moduli |
| Build del sito, test | `python build.py`, 91 test Python e 34 test Node superati |

| Modulo | Titolo per il catalogo | Parole | `[!aggiunta]` | Quota aggiunte | `[!dubbio]` |
|---|---|---|---|---|---|
| 1 | Statistica descrittiva | ~3700 | 4 | ~12% | 0 |
| 2 | Probabilità e variabili aleatorie | ~4800 | 1 | ~2% | 0 |
| 3 | Valori attesi, leggi notevoli e teoremi limite | ~5000 | 1 | ~2% | 0 |
| 4 | Inferenza: stima, intervalli e test | ~4100 | 5 | ~37% | 0 |

Copertura: STA-01…13 e STA-17, 18 dagli appunti (con brevi aggiunte); STA-14, 15, 16 solo da aggiunte (`01-copertura.md`).

Da controllare a mano prima di esportare:
1. La domanda 1 di `01-copertura.md`: il modulo 4 ha sezioni intere (4.5-4.8) che non vengono dai tuoi appunti.
2. La sezione 1.7 sulla regressione, costruita dal formulario (domanda 2).
3. Gli esempi costruiti per il modulo, segnati nel registro: paradosso di Simpson, differenza di medie, ANOVA.
4. Le sette figure.

Poi la fase 8: si tolgono i marcatori `[!aggiunta]`, si aggiorna la versione e si rigenera `corso-completo.md`.

## Fase 8 (5 novembre 2026)

| Controllo | Esito |
|---|---|
| Marcatori `[!aggiunta]` | 24 tolti, lasciando il testo (le fonti restano in `03-registro.md`) |
| `[!dubbio]`, `[!figura]` senza immagine | nessuno |
| Conti e programmi | verificatori in `strumenti/` rieseguiti dopo la pulizia, nessun errore |
| KaTeX, spaziatura, frasi di servizio | nessun errore; tolte le frasi che rimandavano agli strumenti di revisione |
| Anteprima PDF | 42 pagine A4 (valore usato in `catalog.yaml`) |
| Parole | circa 24.400 |
| `corso-completo.md` | rigenerato |

