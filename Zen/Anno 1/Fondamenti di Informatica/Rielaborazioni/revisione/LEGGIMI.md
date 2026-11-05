# Revisione di Fondamenti di Informatica

Stato al 5 novembre 2026: **fasi 1-8 fatte. I marcatori di revisione sono tolti (fase 8): i moduli sono pronti per l'esportazione in PDF.** Le note di revisione restano in `03-registro.md` e `04-controllo.md`.

| File | Cosa contiene |
|---|---|
| `moduli/` | I 7 moduli da vendere |
| `corso-completo.md` | Tutti i moduli uniti, con frontespizio e indice |
| `00-inventario.md` | Materiale disponibile e problemi |
| `01-copertura.md` | Confronto con il programma e domande |
| `02-struttura.md` | Struttura in 7 moduli |
| `03-registro.md` | Scelte, verifiche, correzioni |
| `04-controllo.md` | Controllo finale |
| `notazione.md` | Simboli e convenzioni |
| `strumenti/` | `verifica.py` (compila ed esegue tutti i programmi), `discreta.py` (conti dei moduli 1-2), `prove.py` (ingressi e uscite attese) |

Per ricontrollare: `cd strumenti && python verifica.py` (servono `g++` e AddressSanitizer). Per rigenerare il corso completo: `python revisione/corso_completo.py fondamenti-di-informatica`.
