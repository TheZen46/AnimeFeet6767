# Geometria · fase 7: controllo finale

Controllo del 4 novembre 2026.

| Controllo | Esito |
|---|---|
| Front matter comune, un solo `#`, sezioni `## N.k` | sì, in tutti e 4 i moduli |
| LaTeX valido | 0 errori con KaTeX |
| Sintassi non esportabile | assente |
| Elenchi e tabelle dentro i callout | preceduti da una riga vuota |
| Figure | 2 SVG, tutte referenziate |
| Conti | 70 controlli in `strumenti/verifica.py`, nessun errore |
| Anteprima PDF | 35 pagine A4 (circa 13.700 parole) |
| Residui (`[cite]`, frasi fuori contesto, segnaposto delle figure) | assenti nei moduli |
| Nomi reali, compagni, docenti | assenti nei moduli |
| Build del sito, test | `python build.py`, 91 test Python e 34 test Node superati |

| Modulo | Titolo per il catalogo | Parole | `[!aggiunta]` | `[!dubbio]` |
|---|---|---|---|---|
| 1 | Numeri complessi, polinomi e geometria analitica | ~3800 | 0 | 0 |
| 2 | Matrici, sistemi lineari e determinanti | ~3700 | 0 | 0 |
| 3 | Spazi vettoriali e applicazioni lineari | ~3500 | 0 | 0 |
| 4 | Autovalori, diagonalizzazione e teorema spettrale | ~2900 | 0 | 0 |

Copertura: GEO-01…07 tutti coperti dagli appunti (`01-copertura.md`).

Da controllare a mano prima di esportare:
1. L'esempio dell'inversa $3 \times 3$ del modulo 2 (terza riga letta come $(1, -4, 1)$, registro n. 1).
2. Gli esempi costruiti per i moduli, elencati nel registro.
3. Le due figure.

Poi la fase 8: si aggiorna la versione e si rigenera `corso-completo.md` (non ci sono marcatori da togliere).
