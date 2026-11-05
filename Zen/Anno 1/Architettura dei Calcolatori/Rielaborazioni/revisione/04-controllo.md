# Architettura dei Calcolatori · fase 7: controllo finale

Controllo del 5 novembre 2026.

| Controllo | Esito |
|---|---|
| Front matter comune, un solo `#`, sezioni `## N.k` | sì, in tutti e 5 i moduli |
| LaTeX valido | 0 errori con KaTeX |
| Anteprima PDF | 40 pagine A4 |
| Sintassi non esportabile | assente |
| Codice | blocchi `text`, righe entro 80 caratteri, eseguito nel simulatore |
| Conti | 63 controlli in `strumenti/verifica_ampliamento.py`, nessun errore |
| Nomi reali, compagni, docenti | assenti nei moduli |
| Testo copiato dalle slide | assente: tutto riformulato, dati degli esercizi nuovi |

| Modulo | Titolo per il catalogo | Parole | Esercizi | Guidati |
|---|---|---|---|---|
| 1 | Astrazione, prestazioni e l'ISA RISC-V | ~3500 | 5 | 3 |
| 2 | Programmazione in assembly RISC-V | ~3500 | 4 + frammenti | 3 |
| 3 | L'ALU e l'aritmetica del calcolatore | ~3800 | 7 | 3 |
| 4 | Il processore, la pipeline e il parallelismo fra istruzioni | ~5600 | 8 | 3 |
| 5 | La gerarchia di memoria, la cache e l'input/output | ~5000 | 9 | 3 |

Ogni modulo ha un solo blocco `[!aggiunta]` di apertura più quelli delle sezioni di esercizi e del formulario; nessun `[!dubbio]`.

Da controllare a mano prima di esportare:
1. Che lo stile dei moduli, scritti senza appunti, ti somigli abbastanza.
2. La conferma della vendita (conflitto con il libro, `01-copertura.md`, domanda 1).
3. I programmi del modulo 2 nel simulatore QtRvSim del corso.
