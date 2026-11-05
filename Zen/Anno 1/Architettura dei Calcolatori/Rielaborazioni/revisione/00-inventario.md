# Architettura dei Calcolatori · fase 1: inventario

Inventario del 5 novembre 2026 (ampliamento del primo anno, risposta ALT-1: il corso va rivisto e messo in vendita).

## Materiale dell'autore

| File | Contenuto | Uso |
|---|---|---|
| `Appunti_mano/Datapath con pipeline (era in Fisica 1).pdf` | 3 pagine, solo la prima scritta: schema a mano del datapath con pipeline (registri di pipeline, unità di forwarding in ID e in EX, unità di rilevamento dei conflitti, comparatore in ID, indirizzo del gestore delle eccezioni) | descritto in 4.7 (nota) |

Non ci sono appunti delle lezioni: **tutto il testo dei moduli è scritto in revisione**, dal materiale del corso e dal libro di testo, nello stile degli altri corsi. Per questo ogni modulo è aperto da un blocco `[!aggiunta]` che lo dichiara.

## Materiale del corso (`Anno 1/NUOVO`, solo consultazione, non entra nella repository)

| File | Argomento | Modulo |
|---|---|---|
| `0-Introduzione`, `AstrazioneVirtualizzazione`, `VonNeumann`, `Intel_Nehalem` | introduzione, livelli di astrazione, macchine virtuali, modello di von Neumann, un processore reale | 1 |
| `1-RISCV-ISA` | ISA RISC-V | 1, 2 |
| `Funzioni`, `Fibonacci`, `MergeSort`, `ReverseCoding`, `Vettori_e_Matrici`, `QtRVsim`, `Simple.s`, `Strlen.s` | programmazione assembly e simulatore | 2 |
| `5-ALU`, `CodiciHamming` | ALU, aritmetica, codici di Hamming | 3 |
| `2-RISCV-Pipeline1`, `2-RISCV-Pipeline2`, `3-RISCV-ControlHazards`, `4-RISCV-MultipleIssue` | datapath, pipeline, conflitti, avvio multiplo | 4 |
| `5-MemoriaCache.pptx`, `8-InputOutput` | gerarchia di memoria e I/O | 5 |

Nelle slide alcune parti usano la notazione MIPS (`$t0`, `Rt`, delay slot, registri Cause/EPC): nei moduli si usa sempre RISC-V, e le differenze sono dette nel testo.

## Problemi e rischi

| Livello | Problema | Soluzione |
|---|---|---|
| NOTA | Nessun appunto delle lezioni | moduli scritti in revisione, dichiarati con `[!aggiunta]` |
| NOTA | Slide in parte in inglese e in notazione MIPS | testo riformulato in italiano, notazione RISC-V |
| NOTA | Nessun tema d'esame (l'esame è orale con un esercizio) | esercizi nuovi sul modello delle slide, domande ricorrenti nei formulari |
| DA DECIDERE | Il corso è la base del libro sul RISC-V dell'autore; nel catalogo era escluso "per non fargli concorrenza" | l'autore ha risposto di metterlo in vendita (ALT-1): da confermare prima della pubblicazione |
| NOTA | Figure delle slide (datapath) | non riprodotte; descritte nel testo e con tabelle |

Nessun dato personale, nessun nome di compagni; il nome del docente compare solo nel programma ufficiale (`revisione/programmi/`), non nei moduli.
