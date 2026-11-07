# Modulo 1 — Fondamenti: Linux, dati, Python e C, reti

**Obiettivo del modulo.** Alla fine del modulo lo studente lavora con sicurezza in un sistema Linux, legge e trasforma dati in qualunque rappresentazione, scrive piccoli programmi in Python e in C per interagire con altri programmi, e capisce come comunicano i processi in rete. Sono le competenze che ogni categoria CTF (pwn, reverse, crypto, web, forensics, misc) dà per scontate.

**Durata.** 10 lezioni + 1 simulazione di gara. Ogni lezione richiede circa 2 ore di studio e 2–4 ore di esercizi.

**Ordine didattico.** Segue la sequenza del corso universitario CSE 365 di pwn.college (Arizona State University): *Linux Luminarium* → *Dealing with Data* → interazione con i programmi → *Access Control* → *Talking Web* → *Intercepting Communication*. Le lezioni di Python e C, che pwn.college distribuisce su più moduli, sono raccolte qui in due lezioni dedicate, perché il Modulo 2 (architettura) e il Modulo 3 (reverse engineering) le richiedono già.

**Formato di ogni lezione.** Obiettivi, prerequisiti, teoria con le fonti citate, esempi svolti, esercizi su tre livelli (base, intermedio, sfida), domande di autoverifica, breve ripasso delle lezioni precedenti. Le soluzioni sono in un file separato (`Modulo01_LezioneNN_Soluzioni.md`), da aprire solo dopo aver provato.

**Ambiente di lavoro.** Uno a scelta tra: il *dojo* di pwn.college (browser, nessuna installazione), una macchina virtuale Linux (Debian, Ubuntu o Kali), oppure WSL2 su Windows. Le lezioni assumono `bash` come shell.

---

## Lezioni

| # | Titolo | Contenuti principali |
|---|---|---|
| 1 | La riga di comando | terminale, shell e kernel; prompt; anatomia di un comando (argomenti e opzioni); tipi di comando e `PATH`; virgolette ed espansioni (introduzione); variabili di shell e d'ambiente; codice di uscita; documentazione (`man`, `help`, `--help`) |
| 2 | Il file system | gerarchia FHS, percorsi assoluti e relativi, `cd`/`pwd`/`ls`, inode, hard link e link simbolici, metadati (`stat`, `file`), file speciali (`/dev`, `/proc`) |
| 3 | Cercare e trasformare testo | glob, `find`, `grep` ed espressioni regolari, `sed`, `awk`, `cut`, `tr`, `sort`, `uniq`, `wc`, `strings` |
| 4 | Flussi, pipe e script | descrittori di file 0/1/2, redirezioni (`>`, `>>`, `<`, `2>`, `2>&1`, here-doc), pipe, `xargs`, `tee`, sostituzione di comando e di processo, script bash (condizioni, cicli, funzioni) |
| 5 | Processi e ambiente | PID e PPID, `ps`, `top`, `/proc/<pid>`, segnali e `kill`, job control (`&`, `fg`, `bg`), ciclo `fork`/`exec`/`wait`, ereditarietà di ambiente e descrittori |
| 6 | Utenti e permessi | UID/GID, `/etc/passwd` e `/etc/shadow`, bit `rwx` e notazione ottale, `umask`, setuid/setgid e sticky bit, `sudo`; modelli DAC e MAC |
| 7 | Rappresentare i dati | bit e byte, binario ed esadecimale, interi con e senza segno, complemento a due, endianness, ASCII e UTF-8, Base64, `xxd`/`hexdump`, CyberChef |
| 8 | Python per interagire con i programmi | `bytes` e `str`, `int.to_bytes`/`struct`, file e socket, `subprocess`, introduzione a `pwntools` (`process`, `remote`, `send`/`recv`, `p64`/`u64`) |
| 9 | C essenziale e toolchain | compilazione (`gcc`, preprocessore, linker), tipi e dimensioni, puntatori e array, stringhe C, `malloc`/`free`, chiamate di sistema (`open`, `read`, `write`), primo uso di `gdb` |
| 10 | Reti e comunicazione | modello TCP/IP, indirizzi e porte, TCP e UDP, socket, `nc`, DNS, HTTP e `curl`, catturare traffico con `tcpdump` e Wireshark |
| 11 | **Simulazione di gara** | 3 ore, 10–12 sfide jeopardy che combinano gli argomenti del modulo (misc, encoding, scripting, rete) |

---

## Fonti per lezione

| # | Trascrizioni (cartella `C:\CTF_Transcripts\pwn.college`) | Libri (cartella `Libri`) | Allenamento pwn.college |
|---|---|---|---|
| 1 | 088 *Linux Luminarium 1 — The Command Line*; 091–095 *Introduction* (che cos'è la cybersecurity, etica) | *Linux Basics for Hackers* cap. 1 e 7 (variabili d'ambiente); Ethical Hacker Italiani (comandi base) | Linux Luminarium: *Hello Hackers*, *Digesting Documentation*, *Shell Variables* |
| 2 | 087 *The File System*; 086 *Symbolic Links* | *Linux Basics for Hackers* cap. 1 e 10; OSTEP cap. 39–40 (file e directory) | *Pondering Paths*, *Comprehending Commands*, *File Globbing* |
| 3 | 088 (ripresa) | *Linux Basics for Hackers* cap. 2; *Automate the Boring Stuff* cap. 7 (regex) | *Practicing Piping* (parte), *Untangling Users* (parte) |
| 4 | 078 *Data Dealings and Access Control* (parte su pipe) | *Linux Basics for Hackers* cap. 8 (scripting bash) | *Practicing Piping*, *Chaining Commands* |
| 5 | — | *Linux Basics for Hackers* cap. 6; OSTEP cap. 4–5 (processi, API dei processi); CSAPP cap. 8.2–8.5 | *Processes and Jobs* |
| 6 | 126 *Access Control — CSE365*; 078 | *Linux Basics for Hackers* cap. 5; *Security Engineering* (Anderson) cap. 6 (controllo d'accesso) | *Perceiving Permissions*, *Untangling Users*; modulo *Access Control* |
| 7 | 084–079 *Dealing with Data 1–6* (Binary Data, Hex, Encoding Text, Playing with Encodings, Base64, Gleaning Challenge Insight) | CSAPP cap. 2 (rappresentazione dell'informazione); FDI2 | modulo *Dealing with Data* |
| 8 | 079 *Gleaning Challenge Insight* | *Black Hat Python* cap. 1–2; *Automate the Boring Stuff* cap. 1–9 | modulo *Playing With Programs* (sfide di interazione) |
| 9 | 037 *Syllabus and Program Security* (parte introduttiva) | CSAPP cap. 1, 3.1–3.4, 7 (linking); Kernighan & Ritchie se disponibile | *Computing 101* / *Assembly Crash Course* (anteprima) |
| 10 | 139, 142, 145, 147 *Intercepting Communications — CSE365* | *Practical Packet Analysis* cap. 1–4; Reti Logico; *Black Hat Python* cap. 2 | moduli *Talking Web* e *Intercepting Communication* |

Nota sui nomi delle sfide: i nomi dei moduli del dojo vengono dall'elenco pubblico di pwn.college e possono cambiare tra un semestre e l'altro. Se un nome non corrisponde, va bene il modulo con l'argomento equivalente.

---

## Competenze CTF coperte

- **Misc**: navigazione e ricerca in file system sconosciuti, file con nomi ostili, manipolazione di testo, scripting rapido.
- **Encoding**: riconoscere e decodificare hex, Base64, binario, UTF-8 (base della categoria crypto del Modulo 5).
- **Pwn e reverse**: interazione automatizzata con un programma (pwntools), C e memoria, `gdb` di base (base dei Moduli 3 e 4).
- **Web e rete**: `nc`, `curl`, lettura di una cattura di traffico (base dei Moduli 6 e 7).

## Valutazione del modulo

- Esercizi di ogni lezione: completati e confrontati con le soluzioni.
- Simulazione di gara (lezione 11): soglia di superamento 60% del punteggio. Sotto soglia si ripetono le lezioni delle sfide mancate prima di passare al Modulo 2.

## Stato

- [x] Programma del modulo
- [x] Lezione 1 — `Modulo01_Lezione01_RigaDiComando.md` (+ soluzioni)
- [ ] Lezioni 2–10
- [ ] Simulazione di gara
