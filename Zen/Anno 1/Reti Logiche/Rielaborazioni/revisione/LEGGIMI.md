# Revisione di Reti Logiche

Stato al 4 novembre 2026: **fasi 1-7 fatte, senza fermate intermedie come richiesto. Le domande sono raccolte per il passaggio finale; poi si fa la fase 8.**

| File | Cosa contiene |
|---|---|
| `moduli/` | I 4 moduli da vendere, già con front matter, figure e didascalie |
| `corso-completo.md` | Tutti i moduli uniti, con frontespizio e indice (37 pagine A4) |
| `figure/` | Le 25 figure ridisegnate (SVG) |
| `trascrizione/` | Trascrizione fedele delle 13 lezioni e dei fogli di esercizi: il testo di partenza |
| `00-inventario.md` | Lezioni presenti e mancanti, errori trovati negli appunti |
| `01-copertura.md` | Confronto con il programma ufficiale, domande per te, stato dopo le aggiunte |
| `02-struttura.md` | Struttura in 4 moduli, strada A |
| `03-registro.md` | Correzioni di sostanza (prima/dopo/motivo) e aggiunte, con le fonti |
| `04-controllo.md` | Controllo finale e cosa verificare prima di esportare |
| `notazione.md` | Simboli e convenzioni del corso |
| `strumenti/` | Lo script che disegna le figure (`python strumenti/figure.py figure`) e i controlli delle sintesi per tabella di verità |

Per rigenerare il corso completo dopo una modifica ai moduli: `python revisione/corso_completo.py reti-logiche`.
