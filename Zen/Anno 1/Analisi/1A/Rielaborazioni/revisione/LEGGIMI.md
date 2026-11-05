# Revisione di Analisi Matematica 1A

Stato al 5 novembre 2026: **fasi 1-8 fatte. I marcatori di revisione sono tolti (fase 8): i moduli sono pronti per l'esportazione in PDF.** Le note di revisione restano in `03-registro.md` e `04-controllo.md`.

| File | Cosa contiene |
|---|---|
| `moduli/` | I 5 moduli da vendere, già con front matter, figure e didascalie |
| `corso-completo.md` | Tutti i moduli uniti, con frontespizio e indice (circa 38 pagine A4) |
| `figure/` | Le 19 figure ridisegnate (SVG) |
| `trascrizione/` | Trascrizione fedele delle lezioni e del formulario: il testo di partenza |
| `00-inventario.md` | Lezioni presenti e mancanti, errori trovati negli appunti |
| `01-copertura.md` | Confronto con il programma ufficiale, domande per te, stato dopo le aggiunte |
| `02-struttura.md` | Struttura approvata (5 moduli, strada A) |
| `03-registro.md` | Correzioni di sostanza (prima/dopo/motivo) e aggiunte, con le fonti |
| `04-controllo.md` | Controllo finale e cosa verificare prima di esportare |
| `notazione.md` | Simboli e convenzioni del corso |

Per rigenerare il corso completo dopo una modifica ai moduli: `python revisione/corso_completo.py analisi-matematica-1a`.
