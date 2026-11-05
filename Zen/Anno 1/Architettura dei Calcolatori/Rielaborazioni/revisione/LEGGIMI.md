# Revisione di Architettura dei Calcolatori

Stato al 5 novembre 2026: **fasi 1-7 fatte; corso scritto in revisione** (non ci sono appunti delle lezioni). Le domande sono in `01-copertura.md`.

| File | Cosa contiene |
|---|---|
| `moduli/` | I 5 moduli da vendere |
| `corso-completo.md` | Tutti i moduli uniti, con frontespizio e indice |
| `00-inventario.md` | Materiale disponibile e problemi |
| `01-copertura.md` | Confronto con il programma e domande |
| `02-struttura.md` | Struttura in 5 moduli |
| `03-registro.md` | Scelte, esercizi costruiti, correzioni |
| `04-controllo.md` | Controllo finale |
| `notazione.md` | Simboli e convenzioni |
| `strumenti/` | `rv.py` (codifiche), `simrv.py` (simulatore RV32I), `pipe.py` (cicli della pipeline), `cache.py` (simulatore di cache), `verifica_ampliamento.py` (ricontrolla tutto) |

Per ricontrollare: `cd strumenti && python verifica_ampliamento.py`. Per rigenerare il corso completo: `python revisione/corso_completo.py architettura-dei-calcolatori`.
