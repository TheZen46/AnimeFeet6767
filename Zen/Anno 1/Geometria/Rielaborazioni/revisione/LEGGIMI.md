# Revisione di Geometria

Stato al 5 novembre 2026: **fasi 1-8 fatte. I marcatori di revisione sono tolti (fase 8): i moduli sono pronti per l'esportazione in PDF.** Le note di revisione restano in `03-registro.md` e `04-controllo.md`.

| File | Cosa contiene |
|---|---|
| `moduli/` | I 4 moduli da vendere |
| `corso-completo.md` | Tutti i moduli uniti, con frontespizio e indice |
| `figure/` | Le 2 figure ridisegnate (SVG) |
| `trascrizione/` | Indice delle 20 lezioni a mano |
| `00-inventario.md` | File, lezioni mancanti, problemi ed errori trovati |
| `01-copertura.md` | Confronto con il programma ufficiale e domande |
| `02-struttura.md` | Struttura in 4 moduli |
| `03-registro.md` | Correzioni ed esempi costruiti |
| `04-controllo.md` | Controllo finale |
| `notazione.md` | Simboli e convenzioni |
| `strumenti/` | `figure.py` (disegna le figure) e `verifica.py` (ricontrolla tutti i conti) |

Per rigenerare il corso completo: `python revisione/corso_completo.py geometria`.
