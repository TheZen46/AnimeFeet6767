# Modulo 1 — Lezione 5: Processi e ambiente

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 5 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. dare una definizione precisa di **processo**, distinguerlo dal programma e dal thread, ed elencare che cosa il kernel tiene in memoria per ognuno di essi;
2. spiegare il ciclo di vita di un processo: `fork`, `execve`, `exit`, `wait`, e da qui che cosa sono un **zombie** e un **orfano** e perché esistono;
3. leggere senza esitazioni l'output di `ps`, `pstree`, `top`, e interrogare direttamente `/proc/<PID>` per sapere tutto di un processo: argomenti, ambiente, directory corrente, eseguibile, file aperti, mappa della memoria, segnali, identità;
4. spiegare che cos'è un **segnale**, quali sono le azioni predefinite, come un processo li ignora o li intercetta, che cosa resta di queste scelte attraverso `fork` ed `exec`, e usare `kill`, `pkill` e `trap` con precisione;
5. usare il **job control** (`&`, Ctrl-Z, `jobs`, `fg`, `bg`, `disown`, `nohup`) e spiegarlo in termini di gruppi di processi, sessioni e terminale di controllo;
6. controllare priorità e risorse di un processo (`nice`, `renice`, `ulimit`, `timeout`) e capire come funziona, e come si previene, una *fork bomb*;
7. dire esattamente che cosa un processo figlio **eredita** dal padre, che cosa cambia con `exec`, e come si muove l'**ambiente**;
8. riconoscere i problemi di sicurezza legati ai processi: informazioni che trapelano da `/proc`, `ptrace`, riuso dei PID, gestori di segnale non sicuri, esaurimento delle risorse, e le tecniche di ricognizione sui processi che si usano in una CTF.

**Prerequisiti:** Lezioni 1–4. In particolare: `argv`, ambiente e `export` (L1 §10–12), inode, `/proc` e i file speciali (L2 §8, §12), descrittori, pipe e il meccanismo `pipe`/`fork`/`dup2`/`execve` (L4 §1, §4), `trap` (L4 §13.1).

**Tempo:** circa 4–5 ore di lettura e prove, 3–4 ore di esercizi. Molte prove richiedono **due terminali** aperti sulla stessa macchina: tienili a portata di mano.

**Ripasso dalle lezioni precedenti.**
- Nella Lezione 1 abbiamo detto che ogni comando esterno è un **processo figlio** della shell, che riceve `argv` e una copia dell'ambiente (L1 §10.2). Oggi apriamo quella scatola.
- Nella Lezione 2 abbiamo visto che `/proc` è un file system virtuale, costruito dal kernel al momento della lettura (L2 §8.3). Oggi è il nostro strumento principale.
- Nella Lezione 4 abbiamo descritto la shell che crea una pipeline: `pipe`, poi due `fork`, poi `dup2` ed `execve` in ogni figlio, poi `wait` (L4 §4.1). Oggi guardiamo lo stesso schema dal punto di vista dei processi: chi nasce, chi aspetta chi, che cosa succede quando qualcuno muore.
- Nella Lezione 4 abbiamo usato `trap ... EXIT` per pulire i file temporanei (L4 §13.1). `trap` è il modo in cui bash gestisce i **segnali**, che oggi studiamo per intero.

**Convenzione tipografica.** Come nelle lezioni precedenti: `$` è il prompt di un utente normale, `#` quello di root, le righe senza prompt sono output. Quando servono due terminali scriviamo `[T1]` e `[T2]`. I PID negli esempi sono quelli della macchina su cui sono stati provati: i tuoi saranno diversi.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Che cos'è un processo | 1–4 | Che cosa c'è dentro un processo, come nasce, come muore? |
| II. Osservare i processi | 5–7 | Come vedo quali processi esistono e che cosa stanno facendo? |
| III. Controllare i processi | 8–11 | Come li fermo, li sospendo, li sposto, li limito? |
| IV. Eredità, ambiente e sicurezza | 12–13 | Che cosa passa da padre a figlio? Dove sono le vulnerabilità? |
| V. La pratica | 14–19 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — Che cos'è un processo

## 1. Programma, processo, thread

### 1.1 La definizione

Un **programma** è un file: una sequenza di byte su disco, ad esempio `/usr/bin/sleep`, che contiene istruzioni macchina e dati iniziali in un formato preciso (su Linux il formato **ELF**, che studieremo nel Modulo 2). Un programma, da solo, non fa niente: è come una ricetta scritta su un foglio.

Un **processo** è un programma **in esecuzione**. È la definizione da cui parte il libro di Arpaci-Dusseau (*OSTEP*, cap. 4): *"a process is a running program"*. Più precisamente, un processo è l'insieme di tutto ciò che serve al sistema operativo per far avanzare quell'esecuzione e per riprenderla dopo averla interrotta. Questo insieme si chiama **stato della macchina** del processo, e comprende:

1. **lo spazio di indirizzamento** (*address space*): la memoria che il processo vede. È *virtuale*: ogni processo crede di avere a disposizione tutta la memoria da un indirizzo basso a uno alto, e il kernel, con l'aiuto dell'hardware, traduce quegli indirizzi in posizioni della memoria fisica. Al suo interno si distinguono alcune **regioni**:
   - il **codice** (*text*), le istruzioni lette dal file del programma;
   - i **dati** inizializzati e non inizializzati (*data*, *bss*), cioè le variabili globali;
   - lo **heap**, la memoria chiesta durante l'esecuzione (`malloc` in C);
   - lo **stack**, dove vivono le variabili locali e gli indirizzi di ritorno delle funzioni, e in cima al quale il kernel ha copiato `argv` e l'ambiente al momento dell'avvio;
   - le **mappature** (*mmap*) delle librerie condivise, come `libc.so.6`, e di file mappati in memoria;
2. **i registri del processore**: il contatore di programma (*instruction pointer*, `rip` su x86-64), il puntatore allo stack (`rsp`), i registri generali. Quando il processo non è in esecuzione, il kernel li ha salvati da qualche parte, per poterli ricaricare;
3. **le risorse del sistema operativo** collegate al processo: la tabella dei **descrittori di file** aperti (L4 §1), la **directory corrente**, la directory radice, la maschera dei permessi (`umask`), le **credenziali** (utente e gruppi), le **disposizioni dei segnali**, i limiti sulle risorse, la priorità.

Queste tre categorie sono esattamente ciò che `/proc/<PID>` ci farà vedere nella Parte II: `maps` per lo spazio di indirizzamento, `syscall` e `stat` per i registri, `fd`, `cwd`, `root`, `status`, `limits` per le risorse.

**Un programma, molti processi.** Se in tre terminali lanci `sleep 100`, ci sono **un** programma (`/usr/bin/sleep`) e **tre** processi. Le pagine di codice sono condivise in memoria fisica tra i tre (il kernel le carica una volta sola), ma ogni processo ha il suo stack, i suoi registri, i suoi descrittori e il suo PID.

**Un processo, più programmi nel tempo.** Viceversa, un processo può cambiare programma durante la sua vita: è ciò che fa `execve` (§4.2). La shell che esegue `exec sleep 100` resta lo **stesso processo**, con lo stesso PID, ma da quel momento esegue il codice di `sleep`.

### 1.2 Il punto di vista del kernel: il descrittore di processo

Per ogni processo il kernel Linux tiene in memoria una struttura C chiamata `struct task_struct`, definita in `include/linux/sched.h`. È grande (alcuni kilobyte) e contiene, tra le altre cose: lo stato (§3), il PID, i puntatori al padre e ai figli, un puntatore alla struttura della memoria (`mm_struct`), un puntatore alla tabella dei file (`files_struct`), le credenziali (`cred`), le informazioni sui segnali (`signal_struct`, `sighand_struct`), i dati per lo scheduler. Nei libri di sistemi operativi questa struttura si chiama genericamente **PCB** (*Process Control Block*) o *descrittore di processo* (OSTEP, cap. 4.4; CSAPP, cap. 8.2).

L'aspetto importante per noi: molte di queste parti sono **puntatori a strutture separate**, che possono essere **condivise**. Due processi possono puntare alla stessa `files_struct` (condividono la tabella dei descrittori), alla stessa `mm_struct` (condividono la memoria), e così via. È proprio questo che distingue un processo da un thread.

### 1.3 Thread

Un **thread** è un flusso di esecuzione: un insieme di registri e uno stack. Un processo "classico" ha un solo thread; un processo **multithread** ne ha più d'uno, che eseguono in parallelo **dentro lo stesso spazio di indirizzamento**, con gli stessi file aperti e le stesse credenziali.

Linux implementa i thread in modo particolare: per il kernel **ogni thread è un task**, con la sua `task_struct`. La differenza tra "creare un processo" e "creare un thread" sta solo in che cosa il nuovo task **condivide** con chi lo crea: la chiamata di sistema `clone` riceve una serie di flag (`CLONE_VM` per la memoria, `CLONE_FILES` per i descrittori, `CLONE_SIGHAND` per i gestori dei segnali, `CLONE_THREAD` per entrare nello stesso gruppo...). `fork` è, in pratica, un `clone` che non condivide niente; `pthread_create` è un `clone` che condivide quasi tutto.

Da qui nasce una piccola ambiguità di nomi, che conviene chiarire subito:

| Termine nello spazio utente | Termine nel kernel | Dove si vede |
|---|---|---|
| PID del processo | **TGID** (*thread group ID*) | `Tgid:` in `/proc/<PID>/status`; `getpid()` |
| ID del thread | **PID** del task (detto anche **TID**) | `/proc/<PID>/task/<TID>`; `gettid()` |

Il primo thread di un processo ha TID uguale al PID. Gli altri thread hanno TID diversi, ma tutti condividono lo stesso TGID, ed è questo il numero che `ps` mostra come PID. Per vedere i thread:

```
$ ps -eLf | head -3          # -L: una riga per thread; colonne LWP (TID) e NLWP (numero di thread)
$ ls /proc/1/task/           # una directory per ogni thread del processo 1
$ grep Threads /proc/1/status
```

In questa lezione, quando diciamo "processo" intendiamo il gruppo di thread nel suo insieme; i dettagli sui thread tornano nel Modulo 4, a proposito delle *race condition*.

### 1.4 La virtualizzazione della CPU

Su una macchina con 4 core girano facilmente 200 processi. Come è possibile? Il kernel fa a ciascun processo un'**illusione**: quella di avere un processore tutto per sé. È la **virtualizzazione della CPU** (OSTEP, cap. 4), e si regge su due meccanismi:

- un **meccanismo** a basso livello, il **cambio di contesto** (*context switch*): il kernel interrompe il processo in esecuzione (perché è scaduto il suo quanto di tempo, segnalato da un'interruzione del timer, o perché il processo stesso ha fatto una chiamata di sistema che deve aspettare), salva i suoi registri nella sua `task_struct`, carica i registri di un altro processo e riprende quest'ultimo dal punto in cui era rimasto;
- una **politica** ad alto livello, lo **scheduler**, che decide **quale** processo eseguire dopo. Lo scheduler di Linux è stato per anni il *Completely Fair Scheduler* (CFS); dalla versione 6.6 (2023) è stato sostituito da **EEVDF** (*Earliest Eligible Virtual Deadline First*). Entrambi cercano di dare a ogni processo una quota di CPU proporzionale al suo **peso**, che dipende dal valore di *nice* (§11.1).

Il cambio di contesto non è gratuito: costa qualche microsecondo, e svuota in parte le cache. `/proc/<PID>/status` conta quante volte è successo a un processo: `voluntary_ctxt_switches` (il processo ha ceduto la CPU da solo, ad esempio perché aspettava dati) e `nonvoluntary_ctxt_switches` (gli è stata tolta). Un processo che fa molti cambi volontari è legato all'I/O; uno che ne subisce molti involontari è legato alla CPU.

### 1.5 Modalità utente e modalità kernel

Un processo esegue quasi sempre in **modalità utente** (*user mode*): può usare i registri e la propria memoria, ma non può toccare l'hardware né la memoria degli altri. Per fare qualunque cosa che riguardi il mondo esterno (leggere un file, creare un processo, mandare un pacchetto) deve chiedere al kernel con una **chiamata di sistema** (*system call*): un'istruzione speciale (`syscall` su x86-64) fa passare il processore in **modalità kernel**, esegue il codice del kernel a nome del processo, e torna. È il confine di sicurezza più importante del sistema: tutto il Modulo 4 parlerà di che cosa succede quando qualcuno riesce ad attraversarlo senza permesso.

Le chiamate di sistema di questa lezione sono poche e fondamentali: `fork`/`clone`, `execve`, `exit`, `wait4`/`waitid`, `kill`, `rt_sigaction`, `getpid`/`getppid`, `setsid`, `setpgid`. Puoi vederle in azione con `strace` (Lezione 9), ad esempio `strace -f -e trace=process bash -c 'ls | wc -l'`.

## 2. L'identità di un processo

### 2.1 PID e PPID

Ogni processo ha un numero che lo identifica, il **PID** (*Process ID*), assegnato dal kernel al momento della creazione. Ogni processo, tranne il primo, è stato creato da un altro processo, il suo **padre**, e ne conosce il PID: è il **PPID** (*Parent PID*). La shell li espone come `$$` (il PID della shell) e `$PPID`:

```
$ echo "io sono $$, mio padre è $PPID"
io sono 2417, mio padre è 2398
$ bash -c 'echo "io sono $$, mio padre è $PPID"'
io sono 2502, mio padre è 2417
```

Il secondo comando crea un nuovo bash, figlio della shell 2417: il suo padre è proprio la shell da cui l'hai lanciato. Attenzione a una sottigliezza: dentro una **subshell** creata con `( ... )`, `$$` **non cambia** (bash lo definisce come il PID della shell principale), mentre `$BASHPID` riporta il PID vero del processo corrente:

```
$ echo $$ $BASHPID; ( echo $$ $BASHPID )
2417 2417
2417 2533
```

### 2.2 Come si assegnano i PID

I PID sono assegnati **in ordine crescente** fino a un massimo, letto in `/proc/sys/kernel/pid_max` (32768 per tradizione; molti sistemi moderni usano 4194304, cioè 2^22). Raggiunto il massimo, il kernel **ricomincia dal basso**, saltando i numeri ancora in uso. Due conseguenze:

1. un PID **identifica un processo solo finché quel processo esiste**: dopo la sua morte (e dopo che il padre lo ha raccolto, §4.4) lo stesso numero può essere dato a un processo del tutto diverso. È la radice delle *race* sui PID del §13.3;
2. i PID sono **prevedibili**: il prossimo processo creato avrà, con buona probabilità, il PID successivo all'ultimo. Per molto tempo alcuni programmi hanno usato il PID come sorgente di "casualità" (per nomi di file temporanei, per inizializzare generatori di numeri casuali): è un errore di sicurezza classico, che ritroveremo nel Modulo 5 (`srand(getpid())`) e che abbiamo già incontrato con `/tmp/file.$$` (L4 §14.4).

### 2.3 L'albero dei processi

Poiché ogni processo ha un padre, i processi formano un **albero**. Alla radice ci sono due processi speciali, creati dal kernel all'avvio:

- **PID 1**, `init`: il primo processo dello spazio utente. Sulle distribuzioni moderne è quasi sempre **systemd**; in passato era *SysV init*, nei container è spesso la shell o il programma principale del container, e su sistemi minimali può essere *BusyBox init* o *runit*. Il PID 1 ha un ruolo speciale: **adotta gli orfani** (§4.5), non riceve i segnali per cui non ha installato un gestore (neppure `SIGKILL` inviato dall'interno del suo namespace), e se termina il kernel va in *panic*;
- **PID 2**, `kthreadd`: il padre di tutti i **thread del kernel**, processi che eseguono solo codice del kernel e non hanno uno spazio di indirizzamento utente. `ps` li mostra con il nome tra **parentesi quadre**: `[kthreadd]`, `[ksoftirqd/0]`, `[kworker/0:1]`, `[rcu_sched]`. Hanno PPID 2 (tranne `kthreadd` stesso, che ha PPID 0).

Il PPID 0 non corrisponde a nessun processo reale: indica "creato direttamente dal kernel". Lo vedrai solo per i PID 1 e 2.

Per visualizzare l'albero:

```
$ pstree -p | head          # -p mostra i PID; -u gli utenti quando cambiano; -a gli argomenti
$ ps -ef --forest | tail    # l'albero disegnato con caratteri ASCII nella colonna CMD
$ ps -o pid,ppid,cmd -p $$  # una riga: la tua shell e suo padre
```

Risalendo da una shell di un terminale grafico troverai qualcosa come `systemd → systemd (utente) → gnome-terminal-server → bash`; da una connessione remota `systemd → sshd → sshd → sshd → bash`. Leggere l'albero dice **come** un processo è nato, ed è uno degli indizi più utili in un'analisi forense (Modulo 7): una shell figlia di un server web, ad esempio, è quasi sempre il segno di una compromissione.

### 2.4 I namespace dei PID, in breve

I container (Docker, Podman, LXC) usano i **namespace**: viste separate di alcune risorse del kernel. In un **namespace dei PID** i processi hanno una numerazione propria, che parte da 1: il primo processo del container vede sé stesso come PID 1, anche se nel sistema "esterno" ha, diciamo, PID 48211. Le righe `NSpid:` e `NStgid:` di `/proc/<PID>/status` mostrano il PID in ogni namespace, dal più esterno al più interno. È il primo indizio, in una CTF, per capire se sei dentro un container: un PID 1 che non è `systemd` né `init`, e pochissimi processi in `ps`. Le macchine di pwn.college, ad esempio, sono container: il loro PID 1 è un piccolo programma di avvio.

## 3. Gli stati di un processo

### 3.1 Il modello a tre stati

Nella teoria dei sistemi operativi (OSTEP, cap. 4.4) un processo si trova sempre in uno di tre stati:

- **Running** (in esecuzione): sta eseguendo istruzioni su un processore;
- **Ready** (pronto): potrebbe eseguire, ma in questo momento il processore è occupato da qualcun altro; aspetta il suo turno;
- **Blocked** (bloccato): non può proseguire finché non accade qualcosa, ad esempio finché non arrivano dati da un disco, da una rete o da una tastiera.

Le transizioni sono: *ready → running* quando lo scheduler lo sceglie (*scheduled*), *running → ready* quando il kernel gli toglie la CPU (*descheduled*), *running → blocked* quando avvia un'operazione che deve aspettare, *blocked → ready* quando l'operazione si completa.

### 3.2 Gli stati di Linux

Linux usa un insieme di stati più ricco, che `ps` mostra con una lettera nella colonna `STAT` (o `S`) e che `/proc/<PID>/status` riporta per esteso nella riga `State:`.

| Lettera | Nome nel kernel | Significato |
|---|---|---|
| `R` | `TASK_RUNNING` | in esecuzione **o pronto**: Linux non distingue i due stati del modello teorico |
| `S` | `TASK_INTERRUPTIBLE` | in attesa di un evento (dati, timer, un figlio); un segnale lo può svegliare. È lo stato della stragrande maggioranza dei processi |
| `D` | `TASK_UNINTERRUPTIBLE` | in attesa che **non** può essere interrotta da segnali, tipicamente I/O su disco o su un file system di rete. Neppure `SIGKILL` ha effetto finché l'attesa non finisce |
| `T` | `TASK_STOPPED` | **fermato** da un segnale di stop (`SIGSTOP`, `SIGTSTP`, Ctrl-Z): congelato, finché non riceve `SIGCONT` |
| `t` | `TASK_TRACED` | fermato da un **debugger** (`ptrace`), ad esempio su un *breakpoint* di `gdb` |
| `Z` | `EXIT_ZOMBIE` | **terminato**, ma il padre non ne ha ancora raccolto lo stato di uscita (§4.4) |
| `X` | `EXIT_DEAD` | morto e in fase di rimozione; non dovresti mai vederlo |
| `I` | `TASK_IDLE` | thread del kernel inattivo (una variante di `D` che non conta nel carico) |

Il **carico medio** (*load average*), i tre numeri che `uptime` e `top` mostrano, è la media esponenziale su 1, 5 e 15 minuti del numero di processi in stato `R` **più** quelli in stato `D`. Su una macchina con 4 core, un carico di 4 significa "tutti i core occupati, nessuno in coda"; un carico di 12 significa che in media 8 processi aspettano. Un carico alto con CPU quasi inattiva indica di solito molti processi in `D`, cioè un problema di disco o di rete. Lo stesso dato si legge in `/proc/loadavg`, che aggiunge `in_esecuzione/totali` e l'ultimo PID assegnato:

```
$ cat /proc/loadavg
0.00 0.00 0.00 1/111 428
```

Su questa macchina: carico nullo, 1 processo eseguibile su 111 task, l'ultimo PID assegnato è 428.

### 3.3 Le lettere aggiuntive di `ps`

Nella sintassi BSD (`ps aux`), dopo la lettera dello stato possono comparire dei modificatori:

| Simbolo | Significato |
|---|---|
| `<` | priorità alta (*nice* negativo) |
| `N` | priorità bassa (*nice* positivo) |
| `L` | ha pagine bloccate in memoria (`mlock`) |
| `s` | è un **leader di sessione** (§10) |
| `l` | è multithread |
| `+` | appartiene al **gruppo in primo piano** del suo terminale (§10) |

Così `Ss` è una shell di login in attesa, leader della sua sessione; `R+` è il comando che sta girando in primo piano nel terminale; `SLl` (lo vedremo nell'output reale del §5) è un processo in attesa, con memoria bloccata, multithread; `Z` è uno zombie; `T` è un job sospeso con Ctrl-Z.

## 4. Il ciclo di vita: `fork`, `exec`, `exit`, `wait`

Unix crea i processi con un'idea che all'inizio sembra strana e che invece si rivela potentissima: la creazione di un processo e il caricamento di un programma sono **due operazioni separate** (OSTEP, cap. 5; CSAPP, cap. 8.4).

### 4.1 `fork`: un processo diventa due

La chiamata `fork()` crea un nuovo processo che è una **copia quasi esatta** di chi la chiama. Dopo `fork` ci sono due processi che eseguono **lo stesso programma, dallo stesso punto**: entrambi stanno "tornando" da `fork`. L'unica differenza visibile è il **valore di ritorno**:

- nel **padre**, `fork` restituisce il PID del figlio (un numero positivo);
- nel **figlio**, `fork` restituisce **0**;
- se la creazione fallisce (troppi processi, memoria esaurita), restituisce **-1** nel padre, e nessun figlio nasce.

Si dice che `fork` "viene chiamata una volta e ritorna due volte". Ecco il programma C minimo (lo compileremo davvero nella Lezione 9; per ora leggilo come pseudocodice preciso):

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
    int x = 1;
    pid_t pid = fork();
    if (pid == 0) {                 /* figlio */
        x = x + 1;
        printf("figlio: pid=%d ppid=%d x=%d\n", getpid(), getppid(), x);
        return 7;                   /* codice di uscita del figlio */
    }
    int status;
    waitpid(pid, &status, 0);       /* padre: aspetta il figlio */
    printf("padre: pid=%d figlio=%d x=%d uscita=%d\n",
           getpid(), pid, x, WEXITSTATUS(status));
    return 0;
}
```

Output tipico:

```
figlio: pid=3101 ppid=3100 x=2
padre: pid=3100 figlio=3101 x=1
```

Osserva `x`: il figlio la incrementa, il padre vede ancora 1. Dopo `fork` i due processi hanno **spazi di indirizzamento separati**: ognuno ha la propria copia di ogni variabile. È lo stesso motivo per cui `echo 42 | read n` non imposta `n` nella shell (L4 §4.4): `read` gira in un figlio, e il figlio modifica solo la propria copia.

**Copy-on-write.** Copiare tutta la memoria del padre a ogni `fork` sarebbe lentissimo. Il kernel usa un trucco: dopo `fork`, padre e figlio **condividono** le stesse pagine di memoria fisica, marcate in sola lettura. Solo quando uno dei due prova a **scrivere** su una pagina, il processore genera un'eccezione, e il kernel copia **quella** pagina per chi sta scrivendo. Così `fork` costa poco, e un figlio che subito dopo chiama `exec` non copia quasi niente. È la tecnica **copy-on-write** (COW).

**Che cosa il figlio riceve.** Il figlio riceve una copia di: memoria, registri (tranne il valore di ritorno), descrittori di file (che puntano alle **stesse** voci della tabella dei file aperti, con offset condiviso: L4 §1.3), directory corrente, `umask`, ambiente, credenziali, disposizioni dei segnali e maschera dei segnali bloccati, limiti delle risorse, priorità, gruppo di processi e sessione. **Non** riceve: il PID (ne ha uno nuovo), i segnali pendenti, i timer (`alarm`), i *lock* sui file presi con `fcntl`, l'uso di CPU accumulato. La tabella completa è nel §12.

### 4.2 `execve`: cambiare programma

La chiamata `execve(percorso, argv, envp)` **sostituisce** il programma in esecuzione nel processo corrente con quello contenuto nel file `percorso`. Il kernel:

1. controlla che il file esista, sia eseguibile per l'utente, e abbia un formato riconosciuto (ELF, oppure uno script con `#!`, L1 §10);
2. butta via l'intero spazio di indirizzamento del processo;
3. ne costruisce uno nuovo, mappando le sezioni del file, caricando il *dynamic loader* se il programma usa librerie condivise, e copiando in cima allo stack le stringhe di `argv` e di `envp`;
4. imposta il contatore di programma all'**entry point** del nuovo programma.

Se `execve` riesce, **non ritorna**: il codice che l'ha chiamata non esiste più. Se ritorna, è fallita (restituisce -1 ed `errno` dice perché: `ENOENT`, `EACCES`, `ENOEXEC`...).

Che cosa **resta** dopo `execve`? Il **PID** e il PPID, i **descrittori di file** (tranne quelli marcati *close-on-exec*, `O_CLOEXEC`), la directory corrente e la radice, la `umask`, i limiti, la priorità, il gruppo e la sessione, la maschera dei segnali bloccati e i segnali pendenti, i segnali **ignorati**. Che cosa **cambia**: la memoria (tutta nuova), i gestori dei segnali (riportati al comportamento predefinito, perché il codice dei vecchi gestori non esiste più), e le credenziali **se** il file ha il bit *setuid* o *setgid* o delle *capability* (Lezione 6).

Esistono diverse funzioni di libreria che chiamano `execve` con interfacce più comode: `execl`, `execlp`, `execv`, `execvp`, `execle`, `execvpe`. La `p` indica che cercano il programma nel `PATH`; la `l` che gli argomenti si passano come lista; la `v` come vettore; la `e` che si passa l'ambiente esplicitamente.

### 4.3 Perché separare `fork` ed `exec`

Separare le due operazioni lascia un **momento**, tra `fork` ed `exec`, in cui il figlio esegue ancora il codice del padre e può **preparare l'ambiente** del nuovo programma: chiudere o duplicare descrittori (le redirezioni e le pipe di L4 §4.1), cambiare directory, cambiare utente, impostare limiti, ignorare segnali. Il nuovo programma eredita tutto questo **senza saperlo**. È il motivo per cui `ls` non ha bisogno di sapere niente di redirezioni: la shell fa `fork`, nel figlio fa `open` e `dup2`, poi `execve("/usr/bin/ls", ...)`. OSTEP (cap. 5.4) lo chiama "il modo giusto" di costruire una shell.

In bash puoi vedere i tre casi:

```
$ ls                  # fork + exec: ls è un nuovo processo, figlio della shell
$ cd /tmp             # builtin: nessun fork; cd deve cambiare la directory della shell stessa
$ exec ls             # solo exec: la shell diventa ls, e quando ls finisce il terminale si chiude
```

Il secondo caso spiega perché alcuni comandi **devono** essere builtin: `cd`, `export`, `exit`, `umask`, `ulimit` modificano lo stato del processo corrente, e se fossero programmi esterni modificherebbero solo un figlio destinato a morire subito.

Il builtin `exec` ha un'opzione utile in questa lezione: `exec -a NOME programma` imposta `argv[0]` a `NOME`. Il programma eseguito è sempre lo stesso, ma `ps` e `/proc/<PID>/cmdline` mostreranno il nome scelto. È un modo banale di **camuffare** un processo, che la mini-CTF userà.

### 4.4 `exit` e `wait`: morire e farsi raccogliere

Un processo termina in due modi: **volontariamente**, chiamando `exit(codice)` (o ritornando da `main`), o **per un segnale** che lo uccide (§8). In entrambi i casi il kernel libera quasi tutto: memoria, descrittori, e così via. Ma conserva una piccola parte della `task_struct`: il PID, lo **stato di uscita** e le statistiche d'uso. Il motivo è che il padre potrebbe volerli leggere.

Il padre li legge con una delle chiamate della famiglia **`wait`**: `wait(&status)` aspetta un figlio qualunque, `waitpid(pid, &status, opzioni)` un figlio preciso (con `WNOHANG` non si blocca), `waitid` è la versione più generale. Quando il padre ha raccolto lo stato, il kernel libera anche l'ultimo pezzo, e il PID torna disponibile.

Lo **stato** restituito da `wait` è un intero che codifica che cosa è successo. Le macro di `<sys/wait.h>` lo decodificano:

| Macro | Vero se... | E allora... |
|---|---|---|
| `WIFEXITED(s)` | il figlio ha chiamato `exit` | `WEXITSTATUS(s)` dà il codice (0–255) |
| `WIFSIGNALED(s)` | il figlio è stato ucciso da un segnale | `WTERMSIG(s)` dà il numero del segnale; `WCOREDUMP(s)` dice se ha prodotto un core dump |
| `WIFSTOPPED(s)` | il figlio è stato fermato (solo con `WUNTRACED`) | `WSTOPSIG(s)` dà il segnale di stop |

Su Linux la codifica concreta è: codice di uscita negli 8 bit alti del secondo byte (`status >> 8`), numero del segnale nei 7 bit bassi, bit 0x80 per il core dump. La shell la traduce in un solo numero, `$?`: il codice di uscita se il figlio è uscito normalmente, **128 + numero del segnale** se è stato ucciso (L1 §11). Da qui i valori che vedrai continuamente:

| `$?` | Significato |
|---|---|
| 130 | 128 + 2: ucciso da `SIGINT` (Ctrl-C) |
| 137 | 128 + 9: ucciso da `SIGKILL` (spesso dall'*OOM killer*, il meccanismo che uccide un processo quando la memoria finisce) |
| 139 | 128 + 11: ucciso da `SIGSEGV`, cioè un *segmentation fault*: il segnale più familiare a chi fa *pwn* |
| 141 | 128 + 13: ucciso da `SIGPIPE` (L4 §4.2) |
| 143 | 128 + 15: ucciso da `SIGTERM` |

In bash il builtin `wait` fa la stessa cosa per i job in background: `wait` aspetta tutti i figli, `wait PID` uno solo e restituisce il suo stato, `wait -n` il primo che termina.

### 4.5 Zombie e orfani

Dal meccanismo appena descritto nascono due situazioni con nomi pittoreschi.

**Zombie.** Un figlio che è terminato ma il cui stato non è ancora stato raccolto dal padre è uno **zombie**: è morto, non esegue più niente, non occupa memoria utente, ma esiste ancora come voce nella tabella dei processi, con il suo PID. `ps` lo mostra con stato `Z` e la parola `<defunct>`. Ogni figlio è zombie per un istante, tra la sua morte e la `wait` del padre; il problema nasce quando il padre **non chiama mai** `wait`. Uno zombie non si può uccidere (è già morto: `kill -9` non fa niente). Si elimina solo facendo chiamare `wait` al padre, oppure uccidendo il padre: a quel punto lo zombie diventa orfano, e viene raccolto da chi lo adotta. Molti zombie sono il sintomo di un programma scritto male, e un numero enorme di zombie esaurisce i PID.

Quando un figlio muore, il kernel manda al padre il segnale **`SIGCHLD`**. Un padre ben scritto lo intercetta e chiama `waitpid(-1, &s, WNOHANG)` in un ciclo; un padre che non è interessato agli stati può **ignorare esplicitamente** `SIGCHLD` (`signal(SIGCHLD, SIG_IGN)`), e Linux in quel caso non crea zombie.

**Orfani.** Se il **padre** muore prima del figlio, il figlio diventa **orfano**. Il kernel non lo lascia senza padre: lo **ri-assegna** (*reparenting*) al PID 1, oppure al più vicino antenato che si sia dichiarato *subreaper* (con `prctl(PR_SET_CHILD_SUBREAPER)`: lo fanno `systemd --user` e alcuni gestori di container). Il nuovo padre ha il compito di chiamare `wait` quando l'orfano morirà. `init` lo fa sempre: per questo gli orfani non diventano zombie eterni.

Puoi provocare entrambe le situazioni dalla shell:

```
$ bash -c 'sleep 1 & exec sleep 30' &      # zombie: il figlio sleep 1 muore, ma il padre ora è "sleep 30"
$ sleep 2; ps -o pid,ppid,stat,cmd --ppid $!
    PID    PPID STAT CMD
   3187    3186 Z    [sleep] <defunct>
```

Il trucco: `bash -c` crea in background `sleep 1`, poi si **sostituisce** con `sleep 30` tramite `exec`. Il processo 3186 è ancora il padre del primo `sleep`, ma ora esegue il programma `sleep`, che non sa niente di figli e non chiama mai `wait`. Quando `sleep 1` termina, resta zombie per 30 secondi, finché anche 3186 muore e lo zombie, orfano, viene raccolto da `init`.

```
$ bash -c 'sleep 30 & echo "figlio: $!"'   # orfano: bash termina subito, sleep 30 resta
figlio: 3201
$ ps -o pid,ppid,stat,cmd -p 3201
    PID    PPID STAT CMD
   3201       1 S    sleep 30
```

Il PPID di `sleep` è diventato 1 (o il PID di un *subreaper*, ad esempio `systemd --user`, su un desktop). Questo è anche il principio dei **demoni** (§10.4): un processo che vuole staccarsi dal terminale fa in modo di diventare orfano.

---

# Parte II — Osservare i processi

## 5. `ps` e i suoi parenti

### 5.1 Due sintassi in un solo comando

`ps` (*process status*) fotografa i processi in un istante. Ha una storia complicata: le sue opzioni derivano da **due tradizioni** diverse, BSD e System V, e la versione di Linux (pacchetto *procps-ng*) le accetta entrambe, più una terza in stile GNU. La regola pratica:

- le opzioni **senza trattino** sono in stile **BSD**: `ps aux`;
- le opzioni **con un trattino** sono in stile **UNIX/POSIX**: `ps -ef`;
- le opzioni **con due trattini** sono estensioni GNU: `ps --forest`, `ps --sort`.

Per questo `ps aux` e `ps -aux` non sono la stessa cosa (in teoria il secondo chiede i processi dell'utente "x"; se quell'utente non esiste, procps ripiega sull'interpretazione BSD). Le due forme che userai sempre sono queste.

**`ps aux`** (BSD): `a` tutti i processi con un terminale, `x` anche quelli senza terminale, `u` formato orientato all'utente.

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.1  0.0  28712  7464 ?        SLl  18:35   0:00 /process_api --firecracker-init ...
root         2  0.0  0.0      0     0 ?        S    18:35   0:00 [kthreadd]
```

(Questo è l'output reale della macchina virtuale su cui sono stati provati gli esempi: il suo PID 1 non è `systemd` ma un programma di avvio, come nei container del §2.4.)

| Colonna | Significato |
|---|---|
| `USER` | utente **effettivo** del processo (Lezione 6) |
| `PID` | identificatore |
| `%CPU` | tempo di CPU usato diviso il tempo di vita, in percentuale: **non** è l'uso istantaneo (per quello serve `top`) |
| `%MEM` | memoria fisica residente sul totale |
| `VSZ` | dimensione **virtuale** in KiB: tutto lo spazio di indirizzamento mappato, anche se mai toccato |
| `RSS` | *resident set size*, in KiB: le pagine **effettivamente in memoria fisica** |
| `TTY` | terminale di controllo (§10); `?` se non ne ha |
| `STAT` | stato e modificatori (§3.2–3.3) |
| `START` | ora (o data) di avvio |
| `TIME` | tempo di CPU totale consumato |
| `COMMAND` | la riga di comando, cioè `argv` unito da spazi; tra parentesi quadre se il processo non ne ha (thread del kernel) |

**`ps -ef`** (UNIX): `-e` tutti i processi, `-f` formato completo.

```
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 18:35 ?        00:00:00 /process_api --firecracker-init ...
root         2     0  0 18:35 ?        00:00:00 [kthreadd]
```

Ha il pregio di mostrare il **PPID**; `C` è l'uso di CPU in percentuale intera, `STIME` l'ora di avvio.

### 5.2 Scegliere che cosa vedere

Il modo più potente di usare `ps` è dire esattamente quali colonne si vogliono con `-o` e quali processi con i selettori:

```
$ ps -o pid,ppid,user,stat,ni,etime,cmd -p 1,$$         # colonne a scelta, per due PID
$ ps -u root -o pid,cmd | head                           # i processi dell'utente root
$ ps -C sshd -o pid,ppid,cmd                             # per nome di comando
$ ps --ppid 1 -o pid,cmd                                 # i figli diretti di init
$ ps -eo pid,rss,cmd --sort=-rss | head -5               # i 5 processi che occupano più memoria
$ ps -eo pid,lstart,cmd                                  # data di avvio completa
$ ps -o pid= -C bash                                     # "=" dopo il nome: senza intestazione
```

Alcuni nomi di colonna utili, oltre a quelli già visti: `comm` (nome breve del comando, §5.3), `args` (riga di comando completa, sinonimo di `cmd`), `etime` (tempo trascorso dall'avvio, `[[gg-]hh:]mm:ss`), `etimes` (lo stesso in secondi), `ni` (*nice*), `pri` (priorità), `pgid`, `sid`, `tpgid`, `tty` (§10), `ruser`, `euser`, `suser` (utenti reale, effettivo, salvato: Lezione 6), `wchan` (la funzione del kernel in cui il processo è addormentato), `nlwp` (numero di thread). L'elenco completo è nella sezione *STANDARD FORMAT SPECIFIERS* di `man ps`.

`ps -ef --forest` e `ps axjf` disegnano l'albero; quest'ultimo mostra anche PPID, PGID, SID, TTY e TPGID, ed è il modo più rapido di vedere i job del §10.

### 5.3 `comm` e `args`: due nomi diversi

Ogni processo ha **due** nomi, ed è importante non confonderli:

- **`args`** (o `cmd`): il contenuto di `argv`, letto dalla memoria del processo, in `/proc/<PID>/cmdline`. Il processo lo può **modificare**: è memoria sua. Un programma può sovrascrivere `argv[0]` (lo fanno i server per mostrare il proprio stato, ad esempio `sshd: utente [priv]`), e la shell può sceglierlo con `exec -a`;
- **`comm`**: un campo della `task_struct`, lungo al massimo **15 caratteri** (più il terminatore), in `/proc/<PID>/comm`. Il kernel lo imposta all'`execve` con il **nome del file eseguito** (troncato), e il processo può cambiarlo con `prctl(PR_SET_NAME)`.

```
$ bash -c 'exec -a finto_nome sleep 60' &
$ ps -o pid,comm,args -p $!
    PID COMMAND         COMMAND
   3310 sleep           finto_nome 60
```

Quindi, per sapere **che programma** sta davvero girando, né `comm` né `args` sono affidabili. L'informazione corretta è il link `/proc/<PID>/exe` (§7.2), che punta al file eseguito e che il processo non può falsificare.

### 5.4 `pgrep`, `pkill`, `pidof`, `pstree`

Cercare un processo con `ps aux | grep nome` funziona, ma trova anche `grep` stesso (perché la riga di comando di `grep` contiene `nome`). Il trucco classico è scrivere `grep '[n]ome'`: la regex `[n]ome` corrisponde a `nome` ma la riga di `grep` contiene `[n]ome`, che non le corrisponde. Più semplice usare gli strumenti appositi.

**`pgrep MODELLO`** stampa i PID dei processi il cui **nome** (`comm`) corrisponde all'espressione regolare estesa `MODELLO`. Opzioni principali:

| Opzione | Effetto |
|---|---|
| `-f` | confronta con la **riga di comando completa** (`args`) invece che con `comm` |
| `-a` | stampa anche la riga di comando, non solo il PID |
| `-l` | stampa anche il nome |
| `-x` | corrispondenza **esatta** (tutto il nome, non una parte) |
| `-u UTENTE` | solo i processi di quell'utente (effettivo) |
| `-P PPID` | solo i figli di quel padre |
| `-n`, `-o` | solo il più nuovo / il più vecchio |
| `-c` | conta invece di elencare |
| `-d SEP` | separatore tra i PID (utile per `-d,` e poi `ps -p`) |

Attenzione: `pgrep sleep` cerca nel **nome**, quindi trova anche un processo il cui `argv[0]` è stato cambiato, purché il file eseguito si chiami `sleep`; `pgrep -f custode` cerca nella **riga di comando**, quindi trova un processo che si fa chiamare `custode` qualunque programma sia. Nella mini-CTF ti servirà la seconda forma. E attento anche al contrario: `pgrep -f modello` trova anche la **shell** che ha nella sua riga di comando la parola `modello`, ad esempio un `bash -c '... modello ...'`. Per questo negli esempi useremo spesso `^`: `pgrep -f '^custode'` richiede che la riga di comando **inizi** con quel nome.

**`pkill MODELLO`** accetta le stesse opzioni di selezione e invia un segnale (di default `SIGTERM`) a ogni processo trovato: `pkill -USR1 -f '^sentinella'`. È comodo e **pericoloso**: con un modello troppo generico uccidi processi che non volevi. Prima di un `pkill`, prova sempre lo stesso modello con `pgrep -a`.

**`pidof PROGRAMMA`** stampa i PID dei processi che eseguono quel programma (per nome esatto). **`pstree`** disegna l'albero (§2.3): `pstree -p PID` il sotto-albero di un processo, `pstree -s PID` i suoi antenati.

## 6. `top` e l'osservazione nel tempo

### 6.1 Leggere `top`

`ps` è una fotografia; **`top`** è un film: aggiorna lo schermo ogni 3 secondi (di default). La parte alta mostra lo stato del sistema:

```
top - 18:52:01 up 17 min,  1 user,  load average: 0.08, 0.03, 0.01
Tasks: 112 total,   1 running, 111 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   7937.6 total,   7301.2 free,    312.5 used,    323.9 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   7451.0 avail Mem
```

- la prima riga è l'output di `uptime`: ora, da quanto è acceso il sistema, utenti collegati, carico medio (§3.2);
- `Tasks`: conteggio per stato. Un numero di **zombie** diverso da zero merita un'occhiata;
- `%Cpu(s)`: come si divide il tempo di CPU: `us` utente, `sy` kernel (*system*), `ni` processi con *nice* positivo, `id` inattivo, `wa` attesa di I/O, `hi`/`si` interruzioni hardware e software, `st` tempo "rubato" dall'hypervisor se sei in una macchina virtuale;
- memoria e swap: `buff/cache` è memoria usata come cache dei file, che il kernel libera se serve; per questo la cifra da guardare è `avail Mem`, non `free`.

Sotto, una riga per processo con colonne simili a `ps aux`: `PR` e `NI` (priorità e *nice*), `VIRT` (come `VSZ`), `RES` (come `RSS`), `SHR` (memoria condivisa), `S` (stato), `%CPU` (questa volta **istantaneo**, nell'ultimo intervallo; può superare 100% per un processo multithread su più core).

### 6.2 I comandi interattivi

Dentro `top`, i tasti più utili sono: `P` ordina per CPU, `M` per memoria, `T` per tempo, `k` uccide un processo (chiede PID e segnale), `r` cambia il *nice* (`renice`), `1` mostra ogni CPU separatamente, `H` mostra i thread, `c` alterna nome breve e riga di comando completa, `u` filtra per utente, `f` sceglie le colonne, `q` esce. In uno script si usa la modalità *batch*: `top -b -n 1 | head -15`.

**`htop`**, se installato, offre la stessa informazione con colori, barre, albero (`F5`) e mouse. **`watch`** esegue un comando a intervalli e mostra l'output a schermo intero: `watch -n 1 "ps -o pid,stat,cmd --ppid $$"` è un ottimo modo di osservare i job della Parte III mentre li muovi dal terminale. Nota le virgolette **doppie**: `watch` esegue il comando con `sh -c`, quindi con le virgolette semplici `$$` verrebbe espanso dentro quella `sh`, e indicherebbe il PID sbagliato; con le doppie lo espande subito la tua shell.

### 6.3 Misurare il tempo: `time`

`time comando` esegue il comando e poi stampa tre numeri:

```
$ time sleep 1
real    0m1.002s
user    0m0.001s
sys     0m0.001s
```

- `real`: il tempo trascorso sull'orologio (*wall clock*);
- `user`: il tempo di CPU passato in modalità utente;
- `sys`: il tempo di CPU passato nel kernel a nome del processo (chiamate di sistema).

`sleep` passa un secondo reale quasi senza usare CPU: è sempre in stato `S`. Un programma che calcola usa `user ≈ real`; un programma multithread su più core può avere `user > real`. In bash `time` è una **parola riservata** che misura un'intera pipeline (`time a | b`); il programma `/usr/bin/time` è un'altra cosa, e con `-v` riporta anche memoria massima, cambi di contesto e *page fault*.

Nelle CTF il tempo di esecuzione può essere un **canale laterale**: un controllo di password che confronta un carattere alla volta e si ferma al primo errato impiega più tempo quando i primi caratteri sono giusti. Lo studieremo come *timing attack* nel Modulo 5.

## 7. `/proc/<PID>`: il processo messo a nudo

### 7.1 Una directory per processo

Nella Lezione 2 abbiamo detto che `/proc` non è su disco: ogni lettura è servita dal kernel, che costruisce il contenuto sul momento (L2 §8.3). Per ogni processo esiste una directory `/proc/<PID>`, più il link simbolico **`/proc/self`**, che punta sempre alla directory del processo **che lo sta leggendo**: `cat /proc/self/status` mostra lo stato di `cat`, `ls -l /proc/self` mostra un numero diverso ogni volta. La shell ha anche `/proc/$$`.

L'accesso alle voci segue regole precise: alcune sono leggibili da tutti (`cmdline`, `status`, `stat`, `comm`, `maps` su molti sistemi), altre solo dal **proprietario** del processo e da root, ed eventualmente solo se un controllo di `ptrace` lo permetterebbe (`environ`, `cwd`, `exe`, `root`, `fd`, `mem`). È questa distinzione che rende `/proc` interessante dal punto di vista della sicurezza (§13.1).

Ecco le voci che userai di più:

| Voce | Tipo | Contenuto |
|---|---|---|
| `cmdline` | file | `argv`, con gli argomenti separati da byte **NUL** (`\0`) |
| `comm` | file | il nome breve (§5.3) |
| `environ` | file | l'ambiente **iniziale**, voci `NOME=valore` separate da NUL |
| `status` | file | riepilogo leggibile: nome, stato, PID, PPID, utenti, gruppi, memoria, segnali, capability |
| `stat` | file | le stesse informazioni in una riga di numeri, per i programmi (`ps` legge questo) |
| `cwd` | link | la directory corrente |
| `exe` | link | il file eseguibile |
| `root` | link | la directory radice del processo (diversa da `/` dopo un `chroot` o in un container) |
| `fd/` | directory | un link per ogni descrittore aperto (L4 §1) |
| `fdinfo/` | directory | per ogni descrittore: offset (`pos`), flag di apertura |
| `maps` | file | la mappa dello spazio di indirizzamento (§7.4) |
| `mem` | file | la memoria del processo, leggibile con le regole di `ptrace` (§13.2) |
| `limits` | file | i limiti sulle risorse (§11.2) |
| `task/` | directory | una sottodirectory per ogni thread |
| `wchan` | file | dove dorme nel kernel |
| `io` | file | byte letti e scritti |
| `ns/` | directory | i namespace a cui appartiene |

### 7.2 Gli argomenti, l'ambiente e l'eseguibile

Poiché `cmdline` ed `environ` usano NUL come separatore, `cat` li mostra tutti attaccati. Si leggono con `tr`:

```
$ sleep 300 &
[1] 3412
$ cat /proc/3412/cmdline; echo
sleep300
$ tr '\0' ' ' < /proc/3412/cmdline; echo
sleep 300
$ tr '\0' '\n' < /proc/3412/environ | grep -E '^(HOME|PATH|USER)='
HOME=/home/zen
PATH=/usr/local/bin:/usr/bin:/bin
USER=zen
$ xargs -0 -n1 < /proc/3412/cmdline          # un argomento per riga, metodo alternativo
```

Una precisazione importante su `environ`: contiene l'ambiente **così come era al momento dell'`execve`**, cioè l'area di memoria in cima allo stack dove il kernel ha copiato `envp`. Se il programma in seguito modifica il proprio ambiente con `setenv` o `putenv`, la libreria C di solito alloca le nuove stringhe altrove, e `environ` non le mostra. Per una shell, le variabili create **dopo** l'avvio (anche se esportate) non compaiono nel suo `/proc/$$/environ`, ma compariranno in quello dei figli che lancerà. Viceversa, una variabile passata a un programma resta visibile in `environ` per tutta la vita del processo, anche se il programma la cancella: è un dettaglio che conta quando si passano segreti nell'ambiente (§13.1).

I tre link dicono **chi è** davvero il processo:

```
$ ls -l /proc/3412/exe /proc/3412/cwd /proc/3412/root
lrwxrwxrwx 1 zen zen 0 ... /proc/3412/cwd -> /home/zen
lrwxrwxrwx 1 zen zen 0 ... /proc/3412/exe -> /usr/bin/sleep
lrwxrwxrwx 1 zen zen 0 ... /proc/3412/root -> /
$ readlink /proc/3412/cwd
/home/zen
```

Due proprietà di questi link sono preziose in una CTF e in un'analisi forense:

1. **sono link "magici"**: non sono semplici stringhe, ma riferimenti diretti all'oggetto aperto dal kernel. Se il file eseguibile viene **cancellato** mentre il processo gira, `exe` mostra `/percorso (deleted)`, ma aprirlo dà ancora accesso al contenuto originale: `cp /proc/PID/exe recuperato` **recupera il binario**. Lo stesso vale per un file aperto e poi cancellato, raggiungibile da `/proc/PID/fd/N` (L2 §12.2): un trucco che il dojo *Processes and Jobs* e diversi livelli di pwn.college usano spesso;
2. **attraversano** `chroot` e namespace: da fuori, `/proc/PID/root/` dà accesso al file system come lo vede il processo.

### 7.3 `status`: la carta d'identità

`/proc/<PID>/status` è il file più ricco. Ecco quello di `cat` stesso (`cat /proc/self/status`), sulla macchina di prova, con le righe meno utili omesse:

```
Name:	cat
Umask:	0022
State:	R (running)
Tgid:	421
Pid:	421
PPid:	416
TracerPid:	0
Uid:	0	0	0	0
Gid:	0	0	0	0
FDSize:	64
Groups:
NSpid:	421
VmPeak:	    2864 kB
VmRSS:	    1632 kB
Threads:	1
SigQ:	0/64267
SigPnd:	0000000000000000
ShdPnd:	0000000000000000
SigBlk:	0000000000000000
SigIgn:	0000000000000000
SigCgt:	0000000000000000
CapInh:	0000000000000000
CapPrm:	000001fffeffffff
CapEff:	000001fffeffffff
CapBnd:	000001fffeffffff
CapAmb:	0000000000000000
NoNewPrivs:	0
Seccomp:	0
voluntary_ctxt_switches:	1
nonvoluntary_ctxt_switches:	0
```

Leggiamolo a gruppi.

- **Identità**: `Name` (= `comm`), `State`, `Tgid`/`Pid` (§1.3), `PPid`. **`TracerPid`** è il PID del processo che lo sta tracciando con `ptrace` (un debugger, `strace`), 0 se nessuno: alcuni programmi delle sfide di *reversing* leggono questa riga per accorgersi di essere sotto debugger e comportarsi diversamente. È una tecnica *anti-debug* che studieremo nel Modulo 3.
- **Credenziali**: `Uid` e `Gid` contengono **quattro** numeri: utente **reale**, **effettivo**, **salvato**, e del **file system**. Sono uguali per un processo normale; diventano diversi quando un programma *setuid* è in esecuzione. È l'argomento centrale della Lezione 6: per ora ricorda che il permesso di fare le cose dipende dall'utente **effettivo**. `Groups` sono i gruppi supplementari.
- **Memoria**: `VmPeak`, `VmSize` (virtuale), `VmRSS` (residente), `VmData`, `VmStk`, `VmExe`, `VmLib`: le dimensioni delle regioni del §1.1.
- **Segnali**: cinque **maschere** di 64 bit in esadecimale. `SigPnd` e `ShdPnd` i segnali **pendenti** (arrivati ma non ancora consegnati) per il thread e per l'intero processo; `SigBlk` quelli **bloccati**; `SigIgn` quelli **ignorati**; `SigCgt` quelli **intercettati** (*caught*) da un gestore. Il §8.6 spiega come decodificarle.
- **Capability**: cinque maschere (`CapInh`, `CapPrm`, `CapEff`, `CapBnd`, `CapAmb`). Linux spezza i poteri di root in una quarantina di **capability** separate (`CAP_NET_BIND_SERVICE` per aprire porte sotto 1024, `CAP_KILL` per mandare segnali a chiunque, `CAP_SYS_PTRACE`, `CAP_SETUID`, ...). Qui `CapEff` ha quasi tutti i bit a 1: il processo gira come root. Un processo di un utente normale ha `CapEff: 0000000000000000`. Si decodificano con `capsh --decode=000001fffeffffff`. Le rivedremo nella Lezione 6 e nel Modulo 4.
- **Protezioni**: `NoNewPrivs` (1 se il processo non può più guadagnare privilegi con `execve` di un setuid) e `Seccomp` (0 nessun filtro, 2 filtro sulle chiamate di sistema attivo: molte sfide *pwn* usano seccomp per vietare `execve` e costringerti a leggere la flag con `open`/`read`/`write`).

### 7.4 `maps`: la memoria

`/proc/<PID>/maps` elenca le regioni dello spazio di indirizzamento, una per riga:

```
$ cat /proc/self/maps
5583c2a4a000-5583c2a4c000 r--p 00000000 08:01 1835    /usr/bin/cat
5583c2a4c000-5583c2a51000 r-xp 00002000 08:01 1835    /usr/bin/cat
5583c2a51000-5583c2a53000 r--p 00007000 08:01 1835    /usr/bin/cat
5583c2a54000-5583c2a55000 rw-p 00009000 08:01 1835    /usr/bin/cat
5583c3b0e000-5583c3b2f000 rw-p 00000000 00:00 0       [heap]
7f2e41c00000-7f2e41c28000 r--p 00000000 08:01 2207    /usr/lib/x86_64-linux-gnu/libc.so.6
7f2e41c28000-7f2e41dbd000 r-xp 00028000 08:01 2207    /usr/lib/x86_64-linux-gnu/libc.so.6
...
7ffd8a1f3000-7ffd8a214000 rw-p 00000000 00:00 0       [stack]
7ffd8a2fc000-7ffd8a300000 r--p 00000000 00:00 0       [vvar]
7ffd8a300000-7ffd8a302000 r-xp 00000000 00:00 0       [vdso]
```

Le colonne sono: intervallo di indirizzi, permessi (`r` lettura, `w` scrittura, `x` esecuzione, `p` privata o `s` condivisa), offset nel file, dispositivo, inode, file. Si riconoscono tutte le regioni del §1.1: le sezioni dell'eseguibile (solo il codice è `r-x`), lo heap, la libc, lo stack. Due osservazioni che diventeranno fondamentali nel Modulo 4:

- nessuna regione è insieme `w` ed `x`: è la protezione **W^X** (o NX), che impedisce di scrivere codice in memoria e poi eseguirlo;
- gli indirizzi **cambiano a ogni esecuzione** (prova `cat /proc/self/maps` due volte): è l'**ASLR** (*Address Space Layout Randomization*). Una vulnerabilità che permette di leggere `maps`, o un indirizzo qualunque, di un processo vittima, "rompe" l'ASLR. Per questo l'accesso a `maps` di un processo altrui è regolato dagli stessi controlli di `ptrace`.

### 7.5 Chi usa un file: `lsof` e `fuser`

Spesso la domanda è rovesciata: non "che cosa ha aperto questo processo?" ma "quale processo ha aperto questo file?". Si può rispondere scorrendo tutti i `/proc/*/fd`, ma esistono strumenti appositi.

```
$ lsof -p 3412                 # tutti i file aperti dal processo 3412 (anche librerie e cwd)
$ lsof /var/log/syslog         # chi ha aperto questo file
$ lsof +D /tmp                 # chi ha aperto qualcosa sotto /tmp
$ lsof -u zen -a -c bash       # aperti da processi bash dell'utente zen (-a = AND)
$ lsof +L1                     # file aperti ma cancellati (numero di link < 1)
$ lsof -i :8080                # chi usa la porta 8080 (Lezione 10)
$ fuser -v /tmp/prova.txt      # PID e tipo di accesso
$ fuser -v -n tcp 8080         # chi usa la porta TCP 8080
```

`lsof +L1` è il comando che, in un'analisi forense, trova i file "cancellati ma non ancora spariti" (L2 §7.4): un attaccante che cancella il suo log mentre il processo lo tiene aperto non ha cancellato niente. Senza privilegi, `lsof` e `fuser` vedono solo i processi del tuo utente.

---

# Parte III — Controllare i processi

## 8. I segnali

### 8.1 Che cos'è un segnale

Un **segnale** è una **notifica asincrona** che il kernel consegna a un processo per dirgli che è accaduto un evento (CSAPP, cap. 8.5). È il meccanismo di comunicazione più antico e più semplice di Unix: il messaggio non porta dati, solo un **numero**, che identifica il tipo di evento.

I segnali hanno tre origini:

1. **eccezioni del processore** causate dal processo stesso: un accesso a memoria non valida diventa `SIGSEGV`, una divisione intera per zero `SIGFPE`, un'istruzione illegale `SIGILL`, un'istruzione di *breakpoint* `SIGTRAP`. Si dicono segnali **sincroni**, perché sono la conseguenza diretta di un'istruzione;
2. **eventi del kernel**: un figlio è terminato (`SIGCHLD`), una pipe senza lettori (`SIGPIPE`), un timer scaduto (`SIGALRM`), il terminale si è chiuso (`SIGHUP`), è stato premuto Ctrl-C (`SIGINT`, generato dal driver del terminale), la finestra ha cambiato dimensione (`SIGWINCH`);
3. **altri processi**, con la chiamata di sistema `kill(pid, segnale)`, che dalla shell si usa con il comando omonimo.

Il meccanismo, dentro il kernel, ha due tempi. **Generare** (o inviare) un segnale significa solo accendere un bit nella maschera dei segnali **pendenti** del processo destinatario. **Consegnare** il segnale significa eseguire l'azione corrispondente, e avviene la prossima volta che il processo torna dal kernel alla modalità utente (ad esempio al termine di una chiamata di sistema o di un'interruzione del timer). Tra i due momenti il segnale è **pendente**. Due conseguenze:

- i segnali "standard" (1–31) **non si accumulano**: se lo stesso segnale arriva tre volte prima di essere consegnato, il bit era già acceso, e il processo lo vede **una volta sola**. Un programma che conta i `SIGCHLD` per sapere quanti figli sono morti sbaglia: deve chiamare `waitpid` in un ciclo finché ce ne sono;
- un processo può **bloccare** temporaneamente un segnale (maschera `SigBlk`): il segnale resta pendente e verrà consegnato quando lo sblocca.

I segnali **real-time** (dal 34, `SIGRTMIN`, al 64, `SIGRTMAX`) invece si accodano e possono portare un piccolo dato; li usano librerie e programmi specializzati.

### 8.2 La tabella dei segnali

`kill -l` elenca nomi e numeri. I numeri che seguono valgono per Linux su x86 e ARM; su altre architetture (MIPS, SPARC, Alpha) alcuni sono diversi. Per questo negli script si usano **sempre i nomi**.

| N. | Nome | Azione predefinita | Quando arriva |
|---|---|---|---|
| 1 | `SIGHUP` | Term | il terminale di controllo si è chiuso (*hang up*); per convenzione, ai demoni: "rileggi la configurazione" |
| 2 | `SIGINT` | Term | Ctrl-C dal terminale (*interrupt*) |
| 3 | `SIGQUIT` | Core | Ctrl-\ dal terminale |
| 4 | `SIGILL` | Core | istruzione illegale |
| 5 | `SIGTRAP` | Core | *breakpoint* o *single step* di un debugger |
| 6 | `SIGABRT` | Core | `abort()`: è quello che vedi quando la libc rileva una corruzione dello heap o dello stack (`*** stack smashing detected ***`) |
| 7 | `SIGBUS` | Core | accesso a memoria fisicamente impossibile (ad esempio un file mappato e poi troncato) |
| 8 | `SIGFPE` | Core | errore aritmetico (divisione intera per zero) |
| 9 | `SIGKILL` | Term | **uccisione immediata**: non si può intercettare, bloccare né ignorare |
| 10 | `SIGUSR1` | Term | libero, a disposizione dei programmi |
| 11 | `SIGSEGV` | Core | accesso a memoria non valida (*segmentation violation*) |
| 12 | `SIGUSR2` | Term | libero, a disposizione dei programmi |
| 13 | `SIGPIPE` | Term | scrittura su una pipe o un socket senza lettori (L4 §4.2) |
| 14 | `SIGALRM` | Term | scadenza del timer impostato con `alarm()` |
| 15 | `SIGTERM` | Term | **richiesta cortese di terminare**: è il segnale predefinito di `kill` |
| 17 | `SIGCHLD` | Ign | un figlio è terminato, si è fermato o è ripartito |
| 18 | `SIGCONT` | Cont | riprendi, se eri fermato |
| 19 | `SIGSTOP` | Stop | **fermati**: non si può intercettare, bloccare né ignorare |
| 20 | `SIGTSTP` | Stop | Ctrl-Z dal terminale (*terminal stop*): a differenza di `SIGSTOP`, si può intercettare |
| 21 | `SIGTTIN` | Stop | un processo in background ha provato a leggere dal terminale |
| 22 | `SIGTTOU` | Stop | un processo in background ha provato a scrivere sul terminale (solo con `stty tostop`) |
| 28 | `SIGWINCH` | Ign | la finestra del terminale ha cambiato dimensione |

Le **azioni predefinite** sono cinque (`man 7 signal`):

- **Term**: il processo termina;
- **Core**: il processo termina e, se i limiti lo permettono, il kernel scrive un **core dump** (§8.7);
- **Ign**: il segnale viene scartato;
- **Stop**: il processo viene fermato (stato `T`);
- **Cont**: il processo, se fermato, riprende.

### 8.3 Le disposizioni: predefinita, ignorata, intercettata

Per ogni segnale un processo ha una **disposizione**, cioè una regola su che cosa fare quando gli viene consegnato. Le possibilità sono tre:

1. **predefinita** (`SIG_DFL`): l'azione della tabella;
2. **ignorata** (`SIG_IGN`): il segnale viene scartato;
3. **intercettata**: il processo ha registrato una **funzione gestore** (*signal handler*), con `sigaction` o `signal`. Al momento della consegna, il kernel interrompe il flusso normale del programma, costruisce sullo stack un piccolo *frame* con il contesto salvato, e salta al gestore; quando il gestore ritorna, una chiamata speciale (`rt_sigreturn`) ripristina il contesto e il programma riprende da dove era stato interrotto.

Due segnali fanno eccezione: **`SIGKILL` e `SIGSTOP` non possono essere né ignorati né intercettati né bloccati**. Sono la garanzia che l'amministratore (o il kernel) possa sempre fermare o eliminare un processo, qualunque cosa questo faccia. Per gli altri, la gerarchia della buona educazione è: prima `SIGTERM` (il programma può salvare il lavoro, chiudere le connessioni, cancellare i file temporanei), poi, se dopo qualche secondo non è servito, `SIGKILL`. `systemd`, `docker stop` e lo spegnimento del sistema fanno esattamente così.

Un gestore di segnale è un pezzo di codice che può partire **in qualunque momento**, a metà di qualunque istruzione del programma principale. Questo lo rende delicato: un gestore può chiamare solo funzioni **async-signal-safe** (elenco in `man 7 signal-safety`: `write`, `_exit`, `kill`... ma **non** `printf`, `malloc`, `free`, `syslog`), perché se il segnale arriva mentre il programma principale è dentro `malloc` e il gestore chiama a sua volta `malloc`, le strutture interne dello heap si corrompono. È una sorgente di vulnerabilità reali (§13.5).

### 8.4 Mandare segnali: `kill` e compagni

```
$ kill 3412                  # SIGTERM al processo 3412
$ kill -TERM 3412            # lo stesso, esplicito
$ kill -s TERM 3412          # forma POSIX
$ kill -15 3412              # per numero (sconsigliato negli script)
$ kill -9 3412               # SIGKILL
$ kill -STOP 3412; kill -CONT 3412
$ kill -USR1 3412 3413 3414  # più PID insieme
$ kill -0 3412               # nessun segnale: controlla solo che esista e che tu possa segnalarlo
$ kill -- -3400              # PID negativo: a tutto il GRUPPO di processi 3400 (§10)
$ kill -l 137                # traduce uno stato di uscita: stampa KILL
$ kill -l TERM               # traduce un nome: stampa 15
```

`kill` esiste sia come builtin di bash (che accetta anche i job: `kill %1`) sia come programma `/usr/bin/kill`. Il **segnale 0** merita attenzione: non viene consegnato niente, ma il kernel esegue tutti i controlli. Se `kill -0 PID` ha successo, il processo esiste e tu hai il permesso di segnalarlo; se fallisce con *No such process* non esiste; se fallisce con *Operation not permitted* esiste ma non è tuo. È il modo standard di controllare se un processo è vivo.

`killall NOME` invia un segnale a tutti i processi con quel nome (su Linux; su altri Unix, come Solaris, `killall` uccideva **tutti** i processi, letteralmente). `pkill` (§5.4) è più flessibile. Nessuno dei due andrebbe usato con modelli generici sui server.

**Chi può segnalare chi.** Un processo può inviare un segnale a un altro se l'utente **reale o effettivo** del mittente è uguale all'utente **reale o salvato** del destinatario, oppure se il mittente ha la capability `CAP_KILL` (root ce l'ha). C'è un'eccezione per `SIGCONT`, che si può mandare a qualunque processo della stessa sessione. Quindi un utente normale può uccidere i propri processi, non quelli degli altri; e, nota bene, **può mandare segnali a un programma setuid che lui stesso ha avviato**, perché ne è l'utente reale. Questo dettaglio permette attacchi in cui si interrompe un programma privilegiato in un momento delicato (Lezione 6 e Modulo 4).

### 8.5 I segnali in bash: `trap`

Bash gestisce i segnali con il builtin **`trap`**, che abbiamo già usato per la pulizia (L4 §13.1):

```bash
trap 'comandi' SEGNALE...     # installa un gestore
trap '' SEGNALE...            # IGNORA il segnale (stringa vuota)
trap - SEGNALE...             # ripristina la disposizione predefinita
trap -p                       # mostra i gestori installati
trap -l                       # elenca i segnali (come kill -l)
```

Oltre ai segnali veri, `trap` accetta quattro pseudo-segnali di bash: `EXIT` (all'uscita della shell, in qualunque modo), `ERR` (quando un comando fallisce, con le stesse regole di `set -e`), `DEBUG` (prima di ogni comando) e `RETURN` (all'uscita da una funzione).

```bash
#!/usr/bin/env bash
# conta_usr1.sh — conta i SIGUSR1 ricevuti; termina in modo pulito con SIGTERM
n=0
trap 'n=$((n+1)); echo "USR1 numero $n"' USR1
trap 'echo "ricevuto TERM dopo $n USR1, esco"; exit 0' TERM
echo "PID $$: mandami USR1 e poi TERM"
while :; do sleep 1; done
```

Da un altro terminale: `kill -USR1 PID` più volte, poi `kill PID`. Osserverai un comportamento importante: bash **esegue il gestore solo quando il comando in primo piano è terminato**. Se lo script è fermo in `sleep 1`, il gestore parte entro un secondo; se fosse fermo in `sleep 1000`, partirebbe dopo 1000 secondi. Per una risposta immediata si lancia il comando lungo in background e si usa `wait`, che **viene interrotto** dall'arrivo di un segnale intercettato:

```bash
sleep 1000 & wait $!     # wait ritorna subito (con stato > 128) quando arriva un segnale con trap
```

Il gestore di bash non è una funzione C, quindi non ha il problema delle funzioni async-signal-safe: bash registra internamente che il segnale è arrivato, e esegue i tuoi comandi in un punto sicuro.

### 8.6 Leggere le maschere di `/proc/<PID>/status`

Le righe `SigIgn`, `SigCgt`, `SigBlk`, `SigPnd` sono maschere di 64 bit in esadecimale: il **bit n−1** (contando da 0 a destra) corrisponde al **segnale n**. Esempi reali:

```
$ nohup sleep 300 >/dev/null 2>&1 &
$ grep SigIgn /proc/$!/status
SigIgn:	0000000000000001
```

`0x1` = bit 0 = segnale 1 = **SIGHUP**: è esattamente ciò che fa `nohup` (§9.5). Un esempio più ricco, una bash con `trap ... USR1` lanciata in background da uno script:

```
SigIgn:	0000000000000004
SigCgt:	0000000000010202
```

`SigIgn 0x4` = bit 2 = segnale 3 = `SIGQUIT`. `SigCgt 0x10202` = bit 1, 9 e 16 = segnali 2 (`SIGINT`), 10 (`SIGUSR1`, il nostro `trap`) e 17 (`SIGCHLD`, che bash intercetta sempre per sapere quando i figli muoiono). Una piccola funzione per decodificare una maschera:

```bash
decodifica() {          # uso: decodifica 0000000000010202
  local m=$((16#$1)) n
  for ((n = 1; n <= 64; n++)); do
    (( (m >> (n - 1)) & 1 )) && printf '%d(%s) ' "$n" "$(kill -l "$n")"
  done; echo
}
$ decodifica 0000000000010202
2(INT) 10(USR1) 17(CHLD)
```

Questa lettura è uno strumento di **ricognizione**: senza leggere il codice di un programma, sai a quali segnali reagisce (`SigCgt`) e quali lo lasciano indifferente (`SigIgn`). Nella mini-CTF serve proprio a questo.

### 8.7 Core dump

Quando un processo muore per un segnale con azione *Core*, il kernel può scrivere un **core dump**: un file con l'immagine della sua memoria e dei suoi registri al momento della morte, che un debugger può aprire (`gdb programma core`) per vedere dove e perché è crollato. Due impostazioni lo controllano:

- il limite `ulimit -c` (dimensione massima del core, §11.2): su molti sistemi è **0** di default, cioè niente core dump. `ulimit -c unlimited` li abilita per la shell corrente e i suoi figli;
- il file `/proc/sys/kernel/core_pattern`: il nome del file (ad esempio `core`, nella directory corrente del processo) o, se inizia con `|`, un programma che riceve il core. Sulle distribuzioni con systemd è di solito `|/usr/lib/systemd/systemd-coredump ...`, e i core si gestiscono con `coredumpctl list` e `coredumpctl gdb`.

Il core dump di un programma che conteneva segreti in memoria (password, chiavi) **contiene quei segreti**. Per questo i programmi setuid, per default, non producono core dump leggibili dall'utente (`/proc/sys/fs/suid_dumpable`), e un `core_pattern` scrivibile o un programma di gestione dei core mal scritto sono stati più volte una via per diventare root.

### 8.8 I segnali nelle CTF

Tre segnali compaiono continuamente nelle sfide:

- **`SIGSEGV`**: quando un exploit *pwn* sbaglia un indirizzo, il programma muore con *Segmentation fault* (stato 139). È il primo indizio che hai raggiunto e corrotto qualcosa, e il core dump o `dmesg` dicono a quale indirizzo;
- **`SIGALRM`**: quasi tutti i binari delle sfide chiamano `alarm(60)` o simili all'inizio, per uccidersi dopo un minuto e non tenere occupato il server. Quando li analizzi in locale con un debugger, il timer scade mentre stai ragionando: in `gdb` si risolve con `handle SIGALRM ignore` (o `nopass`), oppure modificando il binario (Modulo 3);
- **`SIGPIPE`** e **`SIGCHLD`**: un servizio remoto che scrive su una connessione chiusa muore di `SIGPIPE`; un server che fa `fork` per ogni cliente e non raccoglie i figli accumula zombie.

E un'idea che ritroveremo: se un programma installa un gestore per `SIGSEGV` o `SIGALRM`, quel gestore è **codice raggiungibile dall'esterno** in un momento scelto dall'attaccante.

## 9. Il job control

### 9.1 Primo piano e sfondo

Una shell interattiva esegue normalmente un comando alla volta in **primo piano** (*foreground*): aspetta che finisca prima di mostrarti di nuovo il prompt, e il comando riceve ciò che scrivi sulla tastiera. Il **job control** permette di avere più comandi in vita contemporaneamente, di sospenderli e di spostarli tra primo piano e **sfondo** (*background*). Un **job** è una pipeline lanciata dalla shell, con tutti i suoi processi.

| Azione | Come | Che cosa succede |
|---|---|---|
| lanciare in background | `comando &` | la shell non aspetta; stampa `[numero del job] PID dell'ultimo processo` |
| sospendere il job in primo piano | **Ctrl-Z** | il terminale invia `SIGTSTP` al job, che si ferma (stato `T`) |
| elencare i job | `jobs` (`-l` con i PID, `-p` solo i PID, `-r`/`-s` solo in esecuzione / fermati) | |
| riportare in primo piano | `fg` oppure `fg %n` | la shell gli manda `SIGCONT` se era fermo, e lo aspetta |
| far ripartire in background | `bg` oppure `bg %n` | `SIGCONT`, senza aspettarlo |
| interrompere il job in primo piano | **Ctrl-C** | `SIGINT` a tutto il job |
| uccidere un job | `kill %n` | `SIGTERM` a tutto il job |
| aspettare | `wait %n` | |

I job si indicano con `%`: `%1` il job numero 1, `%+` (o `%%`) il job corrente, cioè l'ultimo sospeso o lanciato, `%-` il precedente, `%sleep` il job il cui comando inizia con `sleep`, `%?parola` quello il cui comando contiene `parola`. `$!` è il PID dell'ultimo processo lanciato in background.

Una sessione tipica:

```
$ sleep 300 &
[1] 4101
$ vim note.txt            # lavori, poi premi Ctrl-Z
[2]+  Stopped                 vim note.txt
$ jobs -l
[1]-  4101 Running                 sleep 300 &
[2]+  4108 Stopped                 vim note.txt
$ kill %1
[1]-  Terminated              sleep 300
$ fg                      # torna in vim
```

### 9.2 Il ruolo del terminale

Ctrl-C, Ctrl-Z e Ctrl-\ non sono gestiti dalla shell, ma dal **driver del terminale** nel kernel (la *line discipline*): quando legge quei caratteri, invece di passarli al programma, invia un segnale (`SIGINT`, `SIGTSTP`, `SIGQUIT`) a **tutti i processi del gruppo in primo piano** del terminale (§10). `stty -a` mostra la configurazione: `intr = ^C; quit = ^\; susp = ^Z; eof = ^D`... (Ctrl-D non è un segnale: dice al terminale di consegnare subito l'input, e su una riga vuota il programma legge 0 byte, cioè fine del file.) Se un programma mette il terminale in modalità *raw* (come fanno `vim`, `less` e le shell remote di una CTF ben fatta), questi caratteri arrivano al programma come byte normali.

Un processo in **background** che prova a **leggere** dal terminale riceve `SIGTTIN` e si ferma: per questo `cat &` compare subito come `Stopped (tty input)`. Uno che **scrive** invece, di default, ci riesce, e il suo output si mescola al tuo prompt (a meno di `stty tostop`, che lo fa fermare con `SIGTTOU`).

### 9.3 `SIGHUP`: quando il terminale si chiude

Quando chiudi la finestra del terminale o cade la connessione SSH, il kernel invia `SIGHUP` al **leader della sessione** (la shell), e la shell, prima di morire, lo inoltra a **tutti i suoi job**. L'azione predefinita di `SIGHUP` è terminare: ecco perché un lungo comando lanciato con `&` muore quando chiudi il terminale. Per farlo sopravvivere ci sono tre strumenti:

- **`nohup comando &`**: avvia il comando con `SIGHUP` **ignorato** (lo abbiamo visto nella maschera `SigIgn: ...1` del §8.6). Poiché i segnali ignorati restano ignorati attraverso `exec`, il programma non muore. In più, se lo standard output è un terminale, `nohup` lo redirige in `nohup.out`;
- **`disown %n`**: toglie il job dalla tabella dei job della shell, che quindi non gli inoltrerà `SIGHUP`. `disown -h %n` lo lascia nella tabella ma non gli inoltra `SIGHUP`. Funziona anche su un job già lanciato, quando ti accorgi troppo tardi che durerà ore;
- **`setsid comando`**: avvia il comando in una **nuova sessione**, senza terminale di controllo (§10.3): `SIGHUP` non lo raggiunge per costruzione.

L'opzione `shopt -s huponexit` fa sì che bash mandi `SIGHUP` ai job anche quando esci normalmente da una shell di login con `exit`.

### 9.4 Multiplexer: `tmux` e `screen`

La soluzione più comoda per i lavori lunghi, specialmente su un server remoto, è un **multiplexer di terminale**: `tmux` (o il più vecchio `screen`) crea un server che possiede dei terminali virtuali; tu ti colleghi e ti scolleghi, e i processi continuano a girare. Comandi minimi di `tmux`: `tmux new -s ctf` crea una sessione, `Ctrl-b d` si scollega, `tmux ls` elenca, `tmux attach -t ctf` si ricollega, `Ctrl-b %` e `Ctrl-b "` dividono lo schermo, `Ctrl-b c` crea una nuova finestra. In una gara è normale avere una finestra con il risolutore che gira, una con il debugger e una con le note.

### 9.5 Job control negli script

Negli script il job control è **disattivato** (si riattiva con `set -m`): `&` funziona, ma non ci sono `fg`, `bg`, né notifiche. C'è anche una regola meno nota, che abbiamo verificato nel §8.6: in una shell **non interattiva**, i comandi lanciati con `&` partono con `SIGINT` e `SIGQUIT` **ignorati** (`SigIgn: ...6`), perché altrimenti un Ctrl-C dato allo script ucciderebbe anche i processi che lo script ha voluto staccare. Per fermarli servono `kill` espliciti, ad esempio in un `trap ... EXIT`:

```bash
trap 'kill $(jobs -p) 2>/dev/null' EXIT   # alla fine, termina tutti i job lanciati dallo script
```

## 10. Gruppi di processi, sessioni e terminale di controllo

### 10.1 Tre livelli di raggruppamento

Il job control si regge su due raggruppamenti che il kernel conosce (*The Linux Programming Interface*, cap. 34; CSAPP, cap. 8.5.2):

- un **gruppo di processi** (*process group*) è un insieme di processi con lo stesso **PGID**. Il processo il cui PID è uguale al PGID è il **leader del gruppo**. Ogni pipeline lanciata da una shell interattiva diventa un gruppo: in `ls | grep x | wc -l` i tre processi hanno lo stesso PGID, quello del primo. Per questo Ctrl-C ferma l'intera pipeline: il terminale manda il segnale al gruppo, e `kill -- -PGID` fa lo stesso;
- una **sessione** è un insieme di gruppi, con lo stesso **SID**. La crea il **leader di sessione**, di solito la shell di login (il modificatore `s` di `ps`);
- una sessione può avere un **terminale di controllo** (*controlling terminal*), ad esempio `/dev/pts/0`. Di tutti i gruppi della sessione, uno solo alla volta è il **gruppo in primo piano** del terminale (**TPGID**): è quello che riceve l'input della tastiera e i segnali di Ctrl-C/Ctrl-Z. Gli altri sono in background. `fg` e `bg` non fanno altro che cambiare il TPGID (con `tcsetpgrp`) e mandare `SIGCONT`.

```
$ sleep 300 | cat &
$ ps -o pid,ppid,pgid,sid,tpgid,tty,stat,cmd
    PID    PPID    PGID     SID   TPGID TT       STAT CMD
   4200    4190    4200    4200    4250 pts/0    Ss   bash
   4231    4200    4231    4200    4250 pts/0    S    sleep 300
   4232    4200    4231    4200    4250 pts/0    S    cat
   4250    4200    4250    4200    4250 pts/0    R+   ps -o pid,...
```

Leggiamo: tutti nella sessione 4200 (la shell, leader `Ss`); la pipeline `sleep | cat` è un gruppo (4231) in background; `ps` è il gruppo 4250, in primo piano (`TPGID` = 4250, e infatti ha `+`).

### 10.2 Perché esiste tutto questo

Questi meccanismi risolvono un problema preciso: più programmi condividono un solo terminale, e qualcuno deve decidere chi legge la tastiera e chi deve ricevere Ctrl-C. Il kernel tiene la regola (solo il gruppo in primo piano legge; gli altri ricevono `SIGTTIN`), la shell la usa per dare all'utente i comandi `fg` e `bg`. Gli stessi concetti tornano in una CTF quando ottieni una *reverse shell* senza terminale (una "shell stupida", senza job control né Ctrl-C): il primo gesto di un giocatore esperto è procurarsi un vero terminale, ad esempio con `python3 -c 'import pty; pty.spawn("/bin/bash")'`, che crea uno pseudo-terminale e una sessione. Lo vedremo nel Modulo 6.

### 10.3 `setsid` e i demoni

Un processo che **non** è leader di un gruppo può chiamare `setsid()`: crea una nuova sessione e un nuovo gruppo, di cui diventa leader, **senza terminale di controllo**. Il comando `setsid programma` fa questo prima di eseguire il programma.

Un **demone** (*daemon*) è un processo che vive in background, indipendente da qualunque terminale e utente collegato: `sshd`, `cron`, un server web. La ricetta classica per "demonizzare" un programma (Stevens, *Advanced Programming in the UNIX Environment*, cap. 13) è:

1. `fork`, e il padre esce: il figlio non è leader di gruppo, ed è orfano (adottato da init);
2. `setsid`: nuova sessione, niente terminale;
3. un secondo `fork`, e di nuovo il padre esce: il nipote non è leader di sessione, quindi non potrà mai riacquistare un terminale di controllo per errore;
4. `chdir("/")` per non tenere occupata una directory (che impedirebbe di smontare un disco), `umask(0)` o un valore noto;
5. chiudere i descrittori ereditati e aprire 0, 1, 2 su `/dev/null` o su un log.

Oggi questa ricetta si usa sempre meno: su un sistema con **systemd** un servizio è un programma normale che resta in primo piano e scrive su stdout; è systemd che lo avvia come figlio proprio, gli prepara ambiente, utente e limiti, ne raccoglie l'output nel *journal*, e lo riavvia se muore. I comandi da conoscere:

```
$ systemctl status ssh             # stato del servizio, PID principale, ultime righe di log
$ systemctl list-units --type=service --state=running
$ journalctl -u ssh --since "1 hour ago"
$ systemctl cat ssh                # il file di unità: ExecStart, User, ...
```

In una ricognizione (§13.6) i file di unità dicono quale programma gira con quale utente, e se qualcuno di quei file o di quei programmi è scrivibile da te.

### 10.4 Il demone dei lavori pianificati: `cron`

Un altro modo in cui nascono processi senza terminale è la **pianificazione**. Il demone `cron` legge ogni minuto le tabelle `/etc/crontab`, `/etc/cron.d/*`, `/var/spool/cron/crontabs/<utente>` (ognuna modificabile con `crontab -e`), ed esegue i comandi all'ora indicata, con il formato `minuto ora giorno-del-mese mese giorno-della-settimana comando`:

```
*/5 * * * *  root  /opt/backup.sh        # ogni 5 minuti, come root (formato di /etc/crontab)
```

`systemd` ha un equivalente, i *timer* (`systemctl list-timers`). Dal punto di vista della sicurezza, un lavoro pianificato eseguito da root che usa un file scrivibile da altri è uno dei vettori di *privilege escalation* più comuni nelle CTF di tipo *boot2root* (L4 §14.7, Esercizio 16).

## 11. Priorità e risorse

### 11.1 `nice` e `renice`

Ogni processo ha un valore di **nice** tra **−20** (priorità massima) e **19** (minima); il valore predefinito è 0. Il nome dice tutto: un processo con nice alto è "gentile" con gli altri, e lascia loro la CPU. Lo scheduler (§1.4) assegna a ogni livello un **peso**: ogni livello in più riduce la quota di circa il 10% rispetto al livello precedente, quindi due processi che consumano CPU, uno a nice 0 e uno a nice 10, si dividono il processore circa 90% e 10%.

```
$ nice -n 10 ./calcolo_lungo &     # avvia con nice 10
$ renice -n 15 -p 4310             # cambia il nice di un processo esistente
$ ps -o pid,ni,pri,cmd -p 4310
```

Un utente normale può solo **alzare** il nice dei propri processi (renderli più gentili); per abbassarlo, o per usare valori negativi, serve root (o la capability `CAP_SYS_NICE`, o un limite `RLIMIT_NICE` configurato). Esiste un analogo per i dischi, `ionice`.

### 11.2 I limiti: `ulimit` e `prlimit`

Il kernel impone a ogni processo dei **limiti sulle risorse** (*resource limits*, `getrlimit`/`setrlimit`), ereditati dai figli. Ogni limite ha due valori: il **soft limit**, quello in vigore, e lo **hard limit**, il tetto massimo fino a cui il processo può alzare il soft. Un utente normale può abbassare entrambi e alzare il soft fino all'hard; solo root può alzare l'hard. Il builtin `ulimit` li mostra e li imposta per la shell corrente e, quindi, per tutti i suoi figli:

```
$ ulimit -a                        # tutti i limiti soft
core file size              (blocks, -c) 0
open files                          (-n) 20000
max user processes                  (-u) 64267
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
...
$ ulimit -Hn                       # lo hard limit dei file aperti
$ ulimit -c unlimited              # abilita i core dump (§8.7)
$ ( ulimit -t 2; while :; do :; done )   # dopo 2 secondi di CPU il processo muore
$ cat /proc/$$/limits              # la tabella completa, soft e hard
$ prlimit --pid 4310 --nofile=1024:4096    # modifica i limiti di un altro processo
```

Nell'esempio del ciclo infinito, al superamento del soft limit il kernel manda `SIGXCPU`, e al superamento dello hard limit `SIGKILL`; poiché `ulimit` senza `-S` o `-H` imposta **entrambi**, i due momenti coincidono e la subshell muore con stato 137. L'esempio con le parentesi mostra il modo corretto di provare un limite: dentro una **subshell**, così il limite muore con lei e non resta nella tua shell (un limite abbassato non si può rialzare oltre l'hard, e se abbassi anche l'hard non torni più indietro). I limiti più importanti per la sicurezza sono `-u` (numero di processi per utente), `-n` (descrittori aperti), `-c` (core), `-s` (dimensione dello stack: un limite `unlimited` cambia il modo in cui il kernel dispone la memoria, e su vecchi kernel indeboliva l'ASLR), `-v` (memoria virtuale), `-t` (tempo di CPU).

Su un sistema moderno, oltre ai limiti per processo, ci sono i **cgroup** (*control groups*), che limitano gruppi interi di processi: memoria, CPU, numero di task. Sono il meccanismo con cui systemd e i container contengono i servizi (`systemctl show -p TasksMax utente@1000.service`).

### 11.3 La fork bomb

La riga più famosa (e più pericolosa) della shell è questa:

```
:(){ :|:& };:
```

**Non eseguirla** su una macchina che ti serve. Riscritta con un nome leggibile:

```bash
bomba() { bomba | bomba & }   # una funzione che lancia due copie di sé stessa, in background
bomba                          # e la chiamata iniziale
```

`:` è un nome di funzione valido. Ogni chiamata crea **due** processi (i due lati della pipe) e ritorna subito (per via di `&`); ognuno dei due fa lo stesso. Il numero di processi raddoppia a ogni generazione: dopo 20 generazioni sono un milione. In pochi secondi la tabella dei processi o la memoria si esauriscono, `fork` comincia a fallire per tutti, e la macchina non risponde più: non puoi nemmeno lanciare `kill`, perché lanciare un comando richiede un `fork`. È un **attacco di negazione del servizio** (DoS) per esaurimento delle risorse.

La difesa è un limite sul numero di processi: `ulimit -u` per utente (impostato in modo permanente in `/etc/security/limits.conf`), o il limite `TasksMax` del cgroup dell'utente in systemd. Con un limite, la bomba si ferma quando il suo utente raggiunge il tetto, e il resto del sistema continua a funzionare. Se ti capita di avviarla, la via d'uscita è usare da root una shell **già aperta** e `pkill -STOP -u utente` (fermare prima di uccidere, perché un processo ucciso lascia un posto libero a uno nuovo) seguito da `pkill -KILL -u utente`.

### 11.4 Limitare nel tempo: `timeout` e `sleep`

`timeout DURATA comando` esegue il comando e, se non è finito entro la durata, gli manda `SIGTERM`; esce con **124** se è scaduto il tempo. `timeout -k 5 30 comando` manda `SIGTERM` dopo 30 secondi e `SIGKILL` 5 secondi dopo, se serve; `timeout -s KILL 10 comando` usa direttamente `SIGKILL` (uscita 137). Nelle CTF `timeout` è indispensabile per provare in sicurezza un programma che potrebbe bloccarsi o per un attacco a forza bruta in cui ogni tentativo deve avere una durata massima. Le durate accettano suffissi: `0.5`, `30s`, `5m`, `1h`.

---

# Parte IV — Eredità, ambiente e sicurezza

## 12. Che cosa passa da padre a figlio

### 12.1 La tabella completa

Abbiamo visto pezzo per pezzo che cosa sopravvive a `fork` e a `execve`. Ecco il quadro d'insieme, che vale la pena studiare a memoria perché è la chiave di molte vulnerabilità: un programma privilegiato che lancia un figlio gli passa **tutto ciò che sta in questa tabella**, anche quello a cui non ha pensato. (Fonti: `man 2 fork`, `man 2 execve`, *TLPI* cap. 28.4.)

| Attributo | Dopo `fork` (nel figlio) | Dopo `execve` |
|---|---|---|
| PID | **nuovo** | uguale |
| PPID | il PID del padre | uguale |
| memoria (codice, dati, heap, stack) | copia (copy-on-write) | **sostituita** dal nuovo programma |
| descrittori di file | copiati, **condividono** offset e flag di stato | restano aperti, tranne quelli con *close-on-exec* |
| directory corrente, directory radice | uguali | uguali |
| `umask` | uguale | uguale |
| ambiente | copia | quello passato in `envp` (la shell passa le variabili esportate) |
| UID e GID reale, effettivo, salvato; gruppi | uguali | uguali, **tranne** se il file è setuid/setgid (effettivo e salvato cambiano) |
| capability | uguali | ricalcolate secondo le regole dei file (Lezione 6) |
| disposizioni dei segnali | uguali (anche i gestori) | i **gestori** tornano a predefiniti; gli **ignorati** restano ignorati |
| maschera dei segnali bloccati | uguale | uguale |
| segnali pendenti | **vuoti** | uguali |
| limiti delle risorse (`rlimit`) | uguali | uguali |
| nice, politica di scheduling | uguali | uguali |
| gruppo di processi, sessione, terminale di controllo | uguali | uguali |
| timer `alarm` | **azzerato** | conservato |
| lock sui file (`fcntl`) | **non** ereditati | conservati |
| namespace, cgroup | uguali | uguali |
| `NoNewPrivs`, filtri seccomp | uguali | uguali (non si possono togliere) |
| tempo di CPU accumulato | azzerato | conservato |

Tre righe meritano un commento per la sicurezza:

- **descrittori**: un processo privilegiato che ha aperto un file riservato (diciamo `/etc/shadow`, o la flag) e poi esegue un programma scelto dall'utente senza chiudere il descrittore, gli consegna il file **già aperto**, e i controlli dei permessi non vengono rifatti: il permesso si verifica all'`open`, non al `read`. È la CWE-403 (*Exposure of File Descriptor to Unintended Control Sphere*), e un tema di diversi livelli di pwn.college. Lo si vede in `/proc/<PID>/fd` del figlio;
- **segnali ignorati**: un programma che si aspetta di poter essere interrotto con Ctrl-C, o di ricevere `SIGPIPE`, si comporterà diversamente se il padre glieli ha fatti ereditare come ignorati. Il caso di `SIGPIPE` ignorato è tipico dei programmi lanciati da Python (che lo ignora per sé), e produce errori `EPIPE` invece della morte silenziosa;
- **ambiente**: tutto ciò che sta nell'ambiente del padre arriva al figlio, a meno che il padre non lo ripulisca. È il tema del prossimo paragrafo.

### 12.2 L'ambiente, rivisto

Nella Lezione 1 (§12) abbiamo introdotto l'ambiente come un insieme di coppie `NOME=valore` che ogni processo riceve dal padre. Ora possiamo essere precisi.

1. **Dove sta.** L'ambiente è un array di stringhe che il kernel copia in cima allo stack del nuovo programma durante `execve`, subito sopra `argv`. La libc ne conserva un puntatore nella variabile globale `environ`; `getenv`, `setenv` e `unsetenv` lavorano su di essa. `/proc/<PID>/environ` mostra l'area originale (§7.2).
2. **Chi lo decide.** Chi chiama `execve` passa l'ambiente che vuole: le funzioni `execl`, `execv`, `execvp` passano quello corrente, `execle` e `execve` uno scelto esplicitamente. Un programma privilegiato che vuole essere sicuro dovrebbe passare un ambiente **costruito da zero**.
3. **Come lo usa la shell.** Bash tiene due insiemi di variabili: quelle di shell e quelle **esportate**. A un figlio passa solo le esportate (`export NOME`, `declare -x`), più quelle indicate davanti al comando:

```
$ X=1; bash -c 'echo "X=[$X]"'            # X non è esportata
X=[]
$ X=1 bash -c 'echo "X=[$X]"'             # solo per questo comando
X=[1]
$ export X=1; bash -c 'echo "X=[$X]"'
X=[1]
$ env -i bash -c 'env'                    # ambiente vuoto: bash aggiunge da sé PWD, SHLVL e _
PWD=/home/zen
SHLVL=0
_=/usr/bin/env
$ env -u HOME bash -c 'echo "[$HOME]"'    # tutto tranne HOME
[]
$ env | wc -l                             # quante variabili hai esportato
```

4. **Perché conta.** Molte variabili d'ambiente **cambiano il comportamento** di programmi che non le hai scritte tu: `PATH` decide quale programma viene eseguito quando un altro programma ne chiama uno per nome; `LD_PRELOAD` e `LD_LIBRARY_PATH` dicono al *dynamic loader* di caricare librerie aggiuntive o alternative, cioè codice tuo, dentro qualunque programma dinamico; `IFS`, `BASH_ENV`, `ENV` cambiano il comportamento delle shell; `PYTHONPATH`, `PERL5LIB`, `NODE_OPTIONS` quello degli interpreti; `HOME`, `TMPDIR`, `EDITOR`, `PAGER`, `LESSOPEN` quello di molti strumenti. Per questo il loader **ignora** `LD_PRELOAD` e le variabili simili quando esegue un programma setuid (modalità *secure-execution*, `AT_SECURE`), e `sudo` ripulisce l'ambiente prima di eseguire un comando (opzione `env_reset`), lasciando passare solo una lista ristretta. Ogni eccezione a queste regole (`env_keep+=LD_PRELOAD` in `sudoers`, o un wrapper setuid scritto a mano che chiama `system("tar ...")`) è una classica via verso root, che studieremo nella Lezione 6.

### 12.3 Lo stack iniziale di un processo

Per completezza, ecco come il kernel prepara lo stack prima di saltare all'*entry point* (CSAPP, cap. 7.9; `man 3 getauxval`). Dall'indirizzo più basso al più alto:

```
rsp →  argc
       argv[0] ... argv[argc-1], NULL       (puntatori)
       envp[0] ... envp[n-1], NULL          (puntatori)
       auxv: coppie (tipo, valore) ... AT_NULL   (vettore ausiliario)
       ... spazio di riempimento ...
       stringhe di argv e di envp           (i caratteri veri)
       nome del file eseguito
       (fine dello stack)
```

Il **vettore ausiliario** (`auxv`) contiene informazioni che il kernel passa al loader: l'indirizzo delle intestazioni del programma (`AT_PHDR`), la dimensione della pagina (`AT_PAGESZ`), l'indirizzo del vDSO (`AT_SYSINFO_EHDR`), un puntatore a 16 byte casuali (`AT_RANDOM`, usati per il *canary* dello stack), il flag `AT_SECURE`. Lo puoi vedere con `LD_SHOW_AUXV=1 /bin/true`. Questa struttura spiega perché nelle sfide *pwn* lo stack contiene sempre, in alto, le variabili d'ambiente: a volte la flag, o un indirizzo utile, sono lì. Ci torneremo nel Modulo 4.

## 13. I processi e la sicurezza

### 13.1 Informazioni che trapelano da `/proc`

Per default, su Linux, **ogni utente può vedere tutti i processi** di tutti gli utenti, con la loro riga di comando completa (`/proc/<PID>/cmdline` è leggibile da tutti) e il loro stato (`status`). Ne seguono rischi concreti:

- **segreti negli argomenti** (CWE-214, *Invocation of Process Using Visible Sensitive Information*): `mysql -u root -pPassword123`, `curl -u utente:password`, `sshpass -p segreto`, uno script di backup con la chiave sulla riga di comando. Chiunque esegua `ps aux` nel momento giusto la legge. La correzione è passare i segreti in un file con permessi ristretti, sullo standard input, o in una variabile d'ambiente (che è protetta, vedi sotto). L'avevamo già notato in L4 §14.6;
- **ricognizione**: la lista dei processi dice quali servizi girano, con quale utente, con quali file di configurazione, da quale directory. Per un attaccante che ha ottenuto una shell con un utente qualunque è la prima mossa (§13.6).

L'**ambiente**, invece, è leggibile solo dal proprietario del processo e da root (`/proc/<PID>/environ` ha permessi `r--------` e un controllo di tipo `ptrace`). Lo stesso vale per `cwd`, `exe`, `fd`, `mem`. Attenzione però: se l'attaccante è **lo stesso utente** del processo (ad esempio ha compromesso un servizio web e gira come `www-data`), vede l'ambiente di **tutti** i processi di quell'utente, comprese le chiavi delle API passate come variabili. È un errore comune pensare che l'ambiente sia un posto segreto: è solo un po' meno esposto degli argomenti.

L'amministratore può restringere la visibilità montando `/proc` con l'opzione **`hidepid`**: `mount -o remount,hidepid=2 /proc` (nei kernel recenti `hidepid=invisible`) fa sì che ogni utente veda solo i propri processi. È diffuso sui server condivisi e su alcune piattaforme di CTF.

### 13.2 `ptrace`: guardare dentro un altro processo

La chiamata di sistema **`ptrace`** permette a un processo (il *tracer*) di controllare un altro processo (il *tracee*): fermarlo, leggerne e scriverne memoria e registri, intercettarne le chiamate di sistema e i segnali. È il fondamento di `gdb`, `strace` e `ltrace`. Un processo sotto `ptrace` mostra il PID del tracer in `TracerPid` (§7.3) e lo stato `t` quando è fermo.

Ovviamente non si può fare `ptrace` su chiunque. Le regole di base: puoi tracciare un processo se hai **lo stesso UID** (reale, effettivo e salvato tutti uguali al tuo) e il processo **non** ha guadagnato privilegi con un `execve` setuid o di capability; root (con `CAP_SYS_PTRACE`) può tracciare tutti. Su questa regola il modulo di sicurezza **Yama** aggiunge un'ulteriore restrizione, regolata da `/proc/sys/kernel/yama/ptrace_scope`:

| Valore | Significato |
|---|---|
| 0 | classico: ogni processo può tracciare qualunque altro processo dello stesso utente |
| 1 | ristretto (default su Ubuntu e altre): solo un **antenato** può tracciare, oppure un processo esplicitamente autorizzato con `prctl(PR_SET_PTRACER)`. `gdb ./prog` funziona (gdb è il padre); `gdb -p PID` su un processo non figlio no, se non da root |
| 2 | solo con `CAP_SYS_PTRACE` |
| 3 | nessun `ptrace`, irreversibile fino al riavvio |

(Se il file non esiste, come sulla macchina di prova di questa lezione, Yama non è attivo e valgono le regole di base.)

Le stesse regole proteggono `/proc/<PID>/mem`, il file che rappresenta la memoria del processo: con il permesso giusto puoi leggerlo (e scriverlo!) agli indirizzi indicati da `maps`. In una CTF, se riesci a far girare un processo con le credenziali giuste (ad esempio lo stesso utente di un servizio che tiene la flag in memoria), `ptrace` o `/proc/<PID>/mem` ti danno accesso diretto ai suoi segreti.

### 13.3 Il riuso dei PID e le race condition

Abbiamo visto (§2.2) che un PID identifica un processo solo finché esiste. Molti script e demoni salvano il PID di un servizio in un *pidfile* (ad esempio `/run/servizio.pid`) e più tardi fanno `kill $(cat /run/servizio.pid)`. Se nel frattempo il servizio è morto e il PID è stato riassegnato, il segnale colpisce **un processo diverso**. È una race condition del tipo **TOCTOU** (*Time Of Check to Time Of Use*, CWE-367): il controllo ("questo PID è il mio servizio") e l'uso (`kill`) non sono atomici. Se un attaccante può influire sulla creazione dei processi, o se il pidfile è scrivibile da lui, il problema diventa un attacco: un servizio privilegiato può essere indotto a segnalare un processo scelto.

Le difese moderne: far gestire il servizio da un supervisore che ne è il **padre** (systemd: un padre sa con certezza quando il figlio muore, perché lo raccoglie con `wait`, e fino ad allora il PID non può essere riusato); usare i **pidfd** (`pidfd_open`, Linux 5.3), descrittori di file che si riferiscono a **un** processo preciso e non vengono mai confusi con un altro; per i pidfile, verificare anche l'ora di avvio (`ps -o lstart= -p PID`) o il percorso di `/proc/PID/exe` prima di agire.

### 13.4 Esaurimento delle risorse

La fork bomb (§11.3) è il caso estremo di una classe di difetti: un programma che permette a un utente di creare **risorse senza limite** (processi, descrittori, memoria, connessioni). Le CWE corrispondenti sono la **CWE-400** (*Uncontrolled Resource Consumption*) e la **CWE-770** (*Allocation of Resources Without Limits or Throttling*). Un server che fa `fork` per ogni connessione senza un tetto, uno script che crea un file temporaneo per ogni richiesta senza cancellarlo, un servizio che non raccoglie i figli zombie: sono tutti DoS potenziali. La difesa è sempre la stessa: limiti espliciti (`ulimit`, cgroup, un numero massimo di figli contemporanei nel codice) e una gestione corretta della fine della vita (`wait`, chiusura dei descrittori, `trap ... EXIT`).

### 13.5 Gestori di segnale non sicuri

Un gestore di segnale che chiama funzioni non *async-signal-safe* (§8.3) può corrompere lo stato del programma se il segnale arriva nel momento sbagliato. La classe è la **CWE-364** (*Signal Handler Race Condition*), e non è teorica. L'esempio più noto è **regreSSHion** (CVE-2024-6387, luglio 2024): nel server OpenSSH, il gestore di `SIGALRM` che scatta quando un client non completa l'autenticazione entro il tempo massimo (*LoginGraceTime*) chiamava, attraverso la funzione di log, funzioni come `syslog` e `free`, non sicure in un gestore. Un attaccante remoto, senza autenticarsi, poteva aprire connessioni e farle scadere in modo che il segnale interrompesse `sshd` proprio dentro `malloc` o `free`; ripetendo il tentativo migliaia di volte, riusciva a corrompere lo heap e a eseguire codice come **root**. La vulnerabilità era la regressione di un difetto già corretto nel 2006 (CVE-2006-5051), da cui il nome.

La lezione per chi programma: in un gestore si imposta solo una variabile di tipo `volatile sig_atomic_t` e si torna, e il programma principale controlla la variabile; oppure si usa `signalfd` per ricevere i segnali come dati da un descrittore, in un punto scelto.

### 13.6 La ricognizione sui processi in una CTF

Quando in una sfida ottieni una shell su una macchina (dopo aver sfruttato un servizio, o perché la sfida ti dà un accesso SSH), una parte fondamentale della ricognizione riguarda i processi. Una lista di controllo:

1. **chi sono e dove sono**: `id`, `echo $$`, `ps -o pid,ppid,user,cmd -p $$,$PPID`, `cat /proc/1/comm` (sono in un container?), `cat /proc/self/status | grep -E 'Uid|Cap|NoNewPrivs|Seccomp'`;
2. **che cosa gira, e come chi**: `ps auxww` (le due `w` evitano di troncare le righe lunghe), `ps -eo user,pid,cmd --forest`. Cerca processi di **root** o di altri utenti che eseguono script o programmi in posizioni insolite (`/opt`, `/home`, `/tmp`), righe di comando con password, servizi in ascolto;
3. **che cosa partirà**: i lavori pianificati (`cat /etc/crontab`, `ls -la /etc/cron.*`, `systemctl list-timers`), i servizi (`systemctl list-units --type=service`). Un lavoro pianificato che dura un istante non si vede con `ps` fatto a mano: lo strumento **pspy** scorre `/proc` decine di volte al secondo e registra ogni processo che nasce, con la sua riga di comando, **senza bisogno di privilegi**. Puoi imitarlo con un ciclo bash (Esercizio 15);
4. **che cosa è aperto**: `ls -l /proc/*/fd 2>/dev/null` sui processi tuoi, `lsof -u $(id -u)`; cerca descrittori ereditati che puntano a file che non potresti aprire (§12.1), o file cancellati (`(deleted)`) che contengono ancora dati;
5. **che cosa sanno i processi del tuo utente**: `cat /proc/*/environ` (solo i tuoi) alla ricerca di chiavi e password, `cwd` e `exe` di ogni processo, file recuperabili da `exe` o `fd` dei processi i cui file sono stati cancellati.

Il dojo *Processes and Jobs* di pwn.college allena proprio questi gesti: trovare un processo, leggerne gli argomenti, mandargli il segnale giusto, sospenderlo e riprenderlo, sfruttare ciò che eredita.

---

# Parte V — La pratica

## 14. Esempi svolti

### Esempio 1 — Vedere `fork`, `exec` e `wait` con `strace`

`strace` intercetta le chiamate di sistema di un processo (lo studieremo nella Lezione 9). Con `-f` segue anche i figli, con `-e trace=process` mostra solo quelle che creano, trasformano e raccolgono processi. Ecco una pipeline eseguita da `bash -c`:

```
$ strace -f -e trace=process -o traccia.txt bash -c 'ls / | wc -l' > /dev/null; cat traccia.txt
737   execve("/usr/bin/bash", ["bash", "-c", "ls / | wc -l"], 0x7ffd766b2728 /* 199 vars */) = 0
737   clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, ...) = 738
737   clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, ...) = 739
737   wait4(-1,  <unfinished ...>
738   execve("/usr/bin/ls", ["ls", "/"], 0x55e0fd297b30 /* 199 vars */) = 0
739   execve("/usr/bin/wc", ["wc", "-l"], 0x55e0fd297b30 /* 199 vars */) = 0
738   exit_group(0)                     = ?
738   +++ exited with 0 +++
737   <... wait4 resumed>[{WIFEXITED(s) && WEXITSTATUS(s) == 0}], 0, NULL) = 738
737   wait4(-1,  <unfinished ...>
739   exit_group(0)                     = ?
739   +++ exited with 0 +++
737   <... wait4 resumed>[{WIFEXITED(s) && WEXITSTATUS(s) == 0}], 0, NULL) = 739
737   --- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=738, si_uid=0, si_status=0, ...} ---
737   wait4(-1, 0x7ffeef3cb010, WNOHANG, NULL) = -1 ECHILD (No child processes)
737   exit_group(0)                     = ?
```

Ogni riga è una tappa della Parte I:

1. il processo 737 diventa bash con `execve` (prima era il processo creato da `strace`);
2. bash crea **due** figli con `clone` (la forma moderna di `fork`: i flag non contengono `CLONE_VM` né `CLONE_FILES`, quindi è una copia, non un thread). Il valore di ritorno nel padre è il PID del figlio: 738 e 739. Il flag `SIGCHLD` dice quale segnale il padre riceverà alla morte del figlio;
3. il padre si mette in attesa con `wait4(-1, ...)`: "un figlio qualunque";
4. ogni figlio esegue `execve` con il suo programma; nota che l'ambiente (`/* 199 vars */`) è lo stesso per entrambi: è quello di bash;
5. quando `ls` termina (`exit_group(0)`), il `wait4` del padre ritorna con lo stato già decodificato da strace: `WIFEXITED(s) && WEXITSTATUS(s) == 0`;
6. arriva anche `SIGCHLD`; bash, che lo intercetta, chiama `wait4` con `WNOHANG` per raccogliere eventuali altri figli, e scopre che non ce ne sono (`ECHILD`).

Le chiamate `pipe` e `dup2` non compaiono perché non sono "di processo": aggiungi `-e trace=process,pipe2,dup2,close` per vedere anche quelle, e confronta con L4 §4.1.

### Esempio 2 — Smascherare un processo camuffato

Un processo dichiara di chiamarsi `kworker`: è davvero un thread del kernel?

```
$ bash -c 'exec -a "[kworker/0:2]" sleep 600' &
[1] 5120
$ ps -o pid,ppid,comm,args -p 5120
    PID    PPID COMMAND         COMMAND
   5120    4200 sleep           [kworker/0:2] 600
$ readlink /proc/5120/exe
/usr/bin/sleep
$ grep -E 'Kthread|PPid' /proc/5120/status
PPid:	4200
Kthread:	0
```

Tre indizi lo tradiscono: un vero thread del kernel ha **PPID 2**, `exe` che non punta a niente (`readlink` fallisce) e `Kthread: 1` (riga presente nei kernel recenti); e i thread del kernel non hanno argomenti, quindi la riga di comando non può contenere ` 600`. Il nome tra parentesi quadre era solo `argv[0]`. È un trucco usato davvero dai malware sui server Linux, e il metodo per scoprirlo (confrontare `args` con `exe`, il padre, `Kthread`) è quello che userai nella mini-CTF e nell'analisi forense del Modulo 7.

### Esempio 3 — Recuperare un eseguibile cancellato

```
$ cp /usr/bin/sleep ./programma_segreto
$ ./programma_segreto 600 &
[1] 5200
$ rm programma_segreto                 # il file non c'è più...
$ ls -l /proc/5200/exe
lrwxrwxrwx 1 zen zen 0 ... /proc/5200/exe -> /home/zen/l5/programma_segreto (deleted)
$ cp /proc/5200/exe recuperato         # ...ma il kernel lo tiene ancora
$ cmp recuperato /usr/bin/sleep && echo identico
identico
$ kill %1
```

Spiegazione con la Lezione 2 (§7.4): `rm` toglie un **nome**, ma l'inode resta finché qualcuno lo usa, e un programma in esecuzione usa il proprio file. Il link magico `exe` dà accesso all'inode, non al nome. Lo stesso vale per i file aperti in `/proc/PID/fd/`. Nota anche che, mentre il programma gira, il file non si può **modificare** (`ETXTBSY`, *Text file busy*): il kernel lo impedisce perché le pagine di codice sono mappate dal file.

### Esempio 4 — Scegliere il segnale giusto leggendo le maschere

Un processo sconosciuto non reagisce a `kill`. Che cosa fa?

```
$ bash -c 'trap "" TERM; trap "echo ricevuto > /tmp/eco.txt" USR2; while :; do sleep 1; done' &
[1] 5301
$ kill 5301; sleep 1; kill -0 5301 && echo "ancora vivo"
ancora vivo
$ grep -E 'SigIgn|SigCgt' /proc/5301/status
SigIgn:	0000000000004004
SigCgt:	0000000000010802
```

Decodifichiamo con la funzione del §8.6, o a mano:

- `SigIgn 0x4004` = bit 2 e bit 14 = segnali 3 (`QUIT`) e **15 (`TERM`)**: ecco perché `kill` non fa niente. (Il `QUIT` ignorato viene dal fatto che è stato lanciato in background da una shell non interattiva, §9.5; da un terminale interattivo vedresti solo `0x4000`.)
- `SigCgt 0x10802` = bit 1, 11, 16 = segnali 2 (`INT`, intercettato da bash), **12 (`USR2`)** e 17 (`CHLD`, sempre intercettato da bash).

Quindi il processo **ascolta** `USR2`:

```
$ kill -USR2 5301; sleep 1.5; cat /tmp/eco.txt
ricevuto
$ kill -KILL 5301          # TERM è ignorato, KILL non si può ignorare
[1]+  Killed               bash -c ...
```

### Esempio 5 — Interpretare gli stati di uscita

```
$ sleep 100 & p=$!; kill -INT $p; wait $p; echo $?
130
$ sleep 100 & p=$!; kill -KILL $p; wait $p; echo $? "$(kill -l $?)"
137 KILL
$ timeout 1 sleep 5; echo $?
124
$ timeout -s KILL 1 sleep 5; echo $?
137
$ bash -c 'kill -SEGV $$'; echo $?
Segmentation fault
139
$ bash -c 'exit 300'; echo $?
44
```

Questi comandi vanno scritti in una shell **interattiva**: in uno script il primo non funzionerebbe, perché lì i processi lanciati con `&` hanno `SIGINT` ignorato (§9.5) e `kill -INT` non li toccherebbe. Gli ultimi due meritano attenzione. Un processo può uccidersi da solo con un segnale, e la shell non sa distinguere un *segfault* vero da un `kill -SEGV`: vede solo lo stato. Se i core dump sono abilitati (`ulimit -c unlimited`, §8.7) la shell scrive *Segmentation fault (core dumped)*; con il limite a 0, come qui, solo *Segmentation fault*. E un codice di uscita è un byte: `exit 300` diventa 300 mod 256 = 44. Per questo, per convenzione, i codici "normali" stanno tra 0 e 125, e quelli sopra 128 indicano un segnale.

### Esempio 6 — Un piccolo `pspy` in bash

Vogliamo vedere i processi che nascono e muoiono troppo in fretta per `ps`, ad esempio quelli lanciati da `cron`.

```bash
#!/usr/bin/env bash
# spia.sh — stampa ogni nuovo processo che compare, per N secondi (default 10)
declare -A visto
for d in /proc/[0-9]*; do visto[${d#/proc/}]=1; done      # i processi già esistenti
fine=$((SECONDS + ${1:-10}))
while (( SECONDS < fine )); do
  for d in /proc/[0-9]*; do
    p=${d#/proc/}
    [[ -n ${visto[$p]} ]] && continue
    visto[$p]=1
    c=$(tr '\0' ' ' < "$d/cmdline" 2>/dev/null) || continue   # può essere già morto
    [[ -n $c ]] && printf '%(%T)T  uid=%-5s pid=%-6s %s\n' -1 "$(stat -c %u "$d" 2>/dev/null)" "$p" "$c"
  done
  sleep 0.05
done
```

```
$ bash spia.sh 5 &
$ bash -c 'sleep 0.3; echo segreto > /dev/null'
18:48:12  uid=0     pid=674    bash -c sleep 0.3; echo segreto > /dev/null
18:48:12  uid=0     pid=675    sleep 0.3
```

Il proprietario della directory `/proc/<PID>` è l'utente effettivo del processo, per questo `stat -c %u` ci dà l'UID. Osserva che cosa abbiamo catturato: la riga di comando di una shell, compreso il "segreto" che contiene. In una CTF, lasciare girare questo script per qualche minuto rivela i lavori pianificati di root e i loro argomenti. Il limite di questa versione: un processo che vive meno di 50 ms può sfuggire (prova con `/bin/echo ciao`), e il vero `pspy` usa anche `inotify` sugli eseguibili per svegliarsi al momento giusto.

## 15. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Lavora in una directory di prova (`mkdir ~/l5 && cd ~/l5`) e tieni aperti due terminali. Alla fine di ogni esercizio controlla con `jobs` e `pgrep -a -u "$USER" sleep` di non aver lasciato processi in giro.

### ★ Base

1. **Identità.** Stampa il PID e il PPID della tua shell. Poi risali l'albero fino al PID 1 usando **solo** `ps -o ppid= -p PID` ripetuto (o un ciclo `while`), e confronta con `pstree -s -p $$`. Che cosa vedi sopra la tua shell, e che cosa ti dice su come ti sei collegato?
2. **Leggere `ps`.** Con `ps aux`: (a) trova un processo in stato `Ss`, uno con `R+`, un thread del kernel; spiega ogni lettera. (b) Con `ps -eo` mostra PID, utente, nice, tempo trascorso e comando dei 5 processi che hanno usato più CPU. (c) Conta quanti processi appartengono a root e quanti a te. (d) Perché `%CPU` di `ps` e quello di `top` danno spesso numeri diversi?
3. **`/proc`.** Lancia `sleep 1000 &`. Usando solo `/proc/$!` (niente `ps`) ricava: nome, stato, PPID, utente reale ed effettivo, riga di comando, directory corrente, eseguibile, numero di descrittori aperti e a che cosa puntano, la variabile `HOME` del suo ambiente. Poi uccidilo.
4. **Segnali di base.** Con `sleep 1000 &`: fermalo con `SIGSTOP` e verifica lo stato con `ps`; fallo ripartire; uccidilo con `SIGTERM` e stampa lo stato di uscita con `wait`. Ripeti con `SIGKILL` e con `SIGINT`. Infine traduci con `kill -l` i numeri 130, 137, 139, 143.
5. **Job control.** In una shell interattiva: lancia `sleep 300` in primo piano e sospendilo; lancia `sleep 400 &`; lancia `cat` in background e spiega perché si ferma subito; elenca i job con i PID; porta `sleep 300` in background, poi `cat` in primo piano e chiudilo con Ctrl-D; termina tutto usando solo la notazione `%`.

### ★★ Intermedio

6. **Zombie e orfani.** (a) Crea uno zombie con il trucco del §4.5, trovalo con `ps` (con quale filtro sullo stato?) e dimostra che `kill -9` sul suo PID non lo elimina. Come lo fai sparire? (b) Crea un orfano e mostra chi lo ha adottato. Se non è il PID 1, che processo è e perché?
7. **Copia o condivisione?** Spiega l'output di questo comando riga per riga, poi verificalo: `x=1; ( x=2; echo "sub: $x $BASHPID" ); echo "shell: $x $BASHPID"; echo $$ | { read y; echo "y=$y"; }; echo "fuori: [$y]"`. Che cosa è copiato e che cosa no?
8. **Maschere.** Scrivi lo script `maschere.sh PID` che stampa, per un processo, i nomi dei segnali ignorati, intercettati e bloccati, decodificando le righe di `/proc/PID/status` (riusa e migliora la funzione del §8.6). Provalo su: la tua shell interattiva, un `nohup sleep 100 &`, uno `sleep 100 &` lanciato da uno script, il processo dell'Esempio 4.
9. **`trap` e tempi di risposta.** Scrivi uno script che intercetta `USR1` (stampa l'ora), `TERM` (stampa "chiusura" ed esce con 0) e ignora `INT`. Verifica: (a) con il ciclo `while :; do sleep 1; done` il gestore parte entro un secondo; (b) con `sleep 60` in primo piano il gestore aspetta; (c) con `sleep 60 & wait $!` risponde subito, e `wait` restituisce un valore che devi interpretare.
10. **Ereditarietà.** Dimostra con un esperimento (usando `/proc/<PID>/status` e `/proc/<PID>/fd`) ciascuna di queste affermazioni: (a) un segnale ignorato resta ignorato dopo `exec`; (b) un gestore installato con `trap` **non** sopravvive a `exec`; (c) un descrittore aperto con `exec 3< /etc/hostname` passa al figlio; (d) `umask` e directory corrente passano al figlio; (e) una variabile non esportata non passa, ma resta visibile in `set`.
11. **Gruppi e sessioni.** Lancia `sleep 500 | sleep 501 &` e `setsid sleep 502 &`. Con `ps -o pid,ppid,pgid,sid,tpgid,tty,stat,cmd` spiega PGID, SID, TTY e lo stato di ognuno. Poi uccidi la pipeline con **un solo** `kill` che usa il PGID. Che cosa succederebbe ai tre processi chiudendo il terminale?
12. **Limiti.** In una subshell: (a) impedisci la creazione di file più grandi di 10 KiB (`ulimit -f`) e prova a scriverne uno con `head -c 20000 /dev/zero > f`: quale segnale arriva e con quale codice esce? (b) Limita i descrittori a 5 e prova `exec 5< /etc/passwd` e `exec 6< /etc/passwd`. (c) Mostra la differenza tra soft e hard limit con `ulimit -S` e `ulimit -H`, e dimostra che dopo aver abbassato l'hard non puoi più rialzarlo.

### ★★★ Sfida

13. **Fork, exec, wait in C (anteprima).** Senza compilarlo, prevedi l'output di questo programma; poi, se hai `gcc`, verificalo (`gcc -o f f.c && ./f`). Quante volte compare "ciao"? Perché l'ordine delle righe può cambiare tra un'esecuzione e l'altra? Che cosa cambia se togli `fflush` e mandi l'output in una pipe (`./f | cat`), e perché (L4 §3)?
    ```c
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/wait.h>
    int main(void) {
        printf("ciao "); fflush(stdout);
        fork(); fork();
        printf("[%d figlio di %d] ", getpid(), getppid());
        while (wait(NULL) > 0) ;
        printf("\n");
        return 0;
    }
    ```
14. **Mini-CTF.** Nella cartella di questa lezione c'è `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea `~/l5_sfida` e avvia **quattro processi** che custodiscono i quattro pezzi della flag `L5{...}`. **Non leggere il codice dello script**: trova e interroga i processi con gli strumenti di questa lezione. Leggi `LEGGIMI.txt`. Alla fine termina tu tutti e quattro i processi (uno farà resistenza).
15. **Spiare i lavori pianificati.** (a) Migliora lo `spia.sh` dell'Esempio 6: aggiungi il PPID e il nome dell'utente invece dell'UID, e un'opzione `-u UTENTE` per mostrare solo i processi di un utente. (b) Simula un lavoro pianificato con `while :; do bash -c 'tar czf /tmp/b.tgz /etc/hostname 2>/dev/null; sleep 0.2'; sleep 3; done &` e cattura le sue esecuzioni. (c) Spiega perché `ps aux` lanciato a mano non lo vedrebbe quasi mai, e in quale stato si trova il ciclo esterno quando lo guardi.
16. **Revisione di sicurezza.** Un amministratore usa questo script, lanciato come root da `cron` ogni minuto, per tenere in vita un servizio. Trova **almeno cinque** problemi (riusa le CWE di questa lezione e della precedente) e scrivi la versione corretta, oppure spiega perché la soluzione giusta è un'unità di systemd.
    ```bash
    #!/bin/bash
    PIDFILE=/tmp/servizio.pid
    if ! kill -0 $(cat $PIDFILE) 2>/dev/null; then
        cd /opt/servizio
        ./servizio --db-password=Sup3rS3gr3t0 &
        echo $! > $PIDFILE
    fi
    ```
17. **Teoria.** Rispondi in modo argomentato (mezza pagina ciascuna): (a) perché Unix separa `fork` ed `exec`, e quali alternative esistono (`posix_spawn`, `vfork`, `clone3`)? Cerca nell'articolo *"A fork() in the road"* (Baumann et al., HotOS 2019) le critiche moderne a `fork`. (b) Perché `SIGKILL` e `SIGSTOP` non si possono intercettare, e che cosa succederebbe se si potesse? (c) Spiega regreSSHion (§13.5) a un compagno che non conosce i segnali, partendo da che cosa vuol dire "async-signal-safe".

### Allenamento su pwn.college

Il dojo *Linux Luminarium* ha un modulo dedicato: **Processes and Jobs** (elencare i processi, uccidere, interrompere, sospendere, riprendere, mandare in background, aspettare, i job, lo stato di uscita) e, nello stesso dojo, **Perceiving Permissions** e **Untangling Users** preparano la Lezione 6. Fai tutti i livelli di *Processes and Jobs*: con questa lezione dovresti risolverli tutti senza suggerimenti, e per ognuno dovresti saper dire **quale chiamata di sistema** sta dietro al comando che usi (ad esempio `fg` → `tcsetpgrp` + `kill(SIGCONT)`).

## 16. Domande di autoverifica

1. Qual è la differenza tra programma, processo e thread? Che cosa distingue, in Linux, un thread da un processo?
2. Che cosa contiene lo stato di un processo? Indica, per ogni parte, dove la vedi in `/proc/<PID>`.
3. Che cosa sono PID 0, 1 e 2? Perché il PID 1 è speciale?
4. Descrivi gli stati `R`, `S`, `D`, `T`, `t`, `Z`. Quali contano nel *load average*?
5. Che cosa restituisce `fork`, e a chi? Che cos'è il *copy-on-write* e perché rende `fork` economica?
6. Che cosa resta e che cosa cambia dopo `execve`? Perché i gestori dei segnali vengono azzerati ma i segnali ignorati no?
7. Come nasce uno zombie e come scompare? Come nasce un orfano e chi lo adotta?
8. Perché `comm` e `args` non bastano per sapere quale programma gira? Che cosa usi invece?
9. Che cosa sono la consegna e la pendenza di un segnale? Perché i segnali standard non si accumulano?
10. Quali sono le cinque azioni predefinite? Quali segnali non si possono intercettare?
11. Come si decodifica `SigCgt: 0000000000010202`?
12. Chi può mandare un segnale a chi?
13. Spiega con gruppi di processi, sessioni e terminale di controllo che cosa succede quando premi Ctrl-Z e poi scrivi `bg`.
14. Perché un job in background muore quando chiudi il terminale? Tre modi per evitarlo e la differenza tra loro.
15. Che cos'è una fork bomb e come si difende un sistema?
16. Elenca cinque problemi di sicurezza legati ai processi e una contromisura per ciascuno.

## 17. Riepilogo

- Un **processo** è un programma in esecuzione: uno spazio di indirizzamento, uno stato dei registri, e risorse del kernel (descrittori, directory, credenziali, segnali, limiti). Il kernel lo rappresenta con una `task_struct`; un thread è un task che condivide memoria e risorse con altri.
- I processi formano un **albero**: PID 1 (init/systemd) e PID 2 (kthreadd) alla radice. I PID vengono riusati.
- Stati: `R` in esecuzione o pronto, `S` in attesa, `D` in attesa non interrompibile, `T`/`t` fermato, `Z` zombie.
- **`fork`** duplica (copy-on-write), **`execve`** sostituisce il programma mantenendo PID e risorse, **`exit`** termina, **`wait`** raccoglie lo stato. Senza `wait` restano **zombie**; senza padre si diventa **orfani** adottati da init.
- `ps aux`, `ps -ef`, `ps -o`, `pgrep -af`, `pstree -p`, `top`, `lsof` osservano; `/proc/<PID>` è la fonte di verità: `cmdline`, `environ`, `status` (identità, UID, maschere dei segnali, capability), `exe`, `cwd`, `fd`, `maps`, `limits`.
- Un **segnale** è un numero consegnato in modo asincrono. Disposizioni: predefinita, ignorata, intercettata; `SIGKILL` e `SIGSTOP` sono inesorabili. Si mandano con `kill`, `pkill`; bash li gestisce con `trap`. Stato di uscita 128+n.
- Il **job control** (`&`, Ctrl-Z, `jobs`, `fg`, `bg`, `disown`, `nohup`, `setsid`, `tmux`) si basa su **gruppi di processi**, **sessioni** e **terminale di controllo**. I demoni si staccano da tutto; oggi li gestisce systemd.
- **Risorse**: `nice`/`renice`, `ulimit` (soft e hard), cgroup, `timeout`. La fork bomb si ferma con un limite sui processi.
- Un figlio **eredita** quasi tutto, comprese le cose pericolose: descrittori aperti, segnali ignorati, ambiente. `execve` di un setuid cambia le credenziali e attiva la modalità sicura del loader.
- **Sicurezza**: segreti negli argomenti (CWE-214), `ptrace` e `/proc/PID/mem`, riuso dei PID (CWE-367), esaurimento delle risorse (CWE-400/770), gestori di segnale non sicuri (CWE-364, regreSSHion), descrittori trapelati (CWE-403). In una CTF, la ricognizione sui processi (`ps auxww`, cron, `pspy`, `/proc/*/environ`, `exe` e `fd` cancellati) è uno dei primi passi.

## 18. Fonti

- **OccupyTheWeb**, *Linux Basics for Hackers*, cap. 6 (*Process Management*): `ps`, `top`, `nice`/`renice`, `kill` e i segnali, processi in background, `at` e `cron`.
- **R. e A. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces*, cap. 4 (*The Abstraction: The Process*: definizione, stato della macchina, stati, strutture dati) e cap. 5 (*Interlude: Process API*: `fork`, `wait`, `exec`, e la costruzione della shell), cap. 6 (*Limited Direct Execution*: modalità utente e kernel, cambio di contesto).
- **R. E. Bryant, D. R. O'Hallaron**, *Computer Systems: A Programmer's Perspective*, cap. 8.2–8.5 (processi, chiamate di sistema per il controllo dei processi, `fork`, `waitpid`, `execve`, segnali, gruppi di processi, gestori sicuri) e cap. 7.9 (caricamento ed esecuzione, struttura dello stack iniziale).
- **M. Kerrisk**, *The Linux Programming Interface*, cap. 20–22 (segnali), 24–28 (creazione, terminazione, monitoraggio dei figli, `execve`), 34 (gruppi, sessioni, job control), 36 (limiti). Non è tra i libri della tua cartella, ma è il riferimento più completo: utile da consultare per singoli capitoli.
- **W. R. Stevens, S. Rago**, *Advanced Programming in the UNIX Environment*, cap. 13 (processi demone).
- **pwn.college**, dojo *Linux Luminarium*, modulo *Processes and Jobs*; dojo *Computing 101* per la visione dei processi dal lato dell'assembly.
- **Pagine di manuale**: `ps(1)`, `top(1)`, `pgrep(1)`, `kill(1)`, `proc(5)` (descrizione di ogni voce di `/proc`), `signal(7)`, `signal-safety(7)`, `fork(2)`, `execve(2)`, `wait(2)`, `credentials(7)`, `ptrace(2)`, `setsid(2)`, `getrlimit(2)`; `man bash` sezioni *JOB CONTROL* e *SIGNALS*, builtin `trap`, `wait`, `jobs`, `disown`, `ulimit`.
- **Documentazione del kernel**: `Documentation/admin-guide/LSM/Yama.rst` (ptrace_scope), `Documentation/filesystems/proc.rst` (hidepid e campi di `status`).
- **Qualys Threat Research Unit**, *regreSSHion: Remote Unauthenticated Code Execution Vulnerability in OpenSSH server* (CVE-2024-6387), luglio 2024.
- **A. Baumann et al.**, *A fork() in the road*, HotOS 2019.
- **MITRE CWE**: CWE-214, CWE-364, CWE-367, CWE-400, CWE-403, CWE-770.

## 19. Prossima lezione

**Lezione 6 — Utenti e permessi**: utenti e gruppi, `/etc/passwd`, `/etc/shadow` e `/etc/group`, il modello dei permessi `rwx` su file e directory, `chmod`, `chown`, `umask`, i bit speciali *setuid*, *setgid* e *sticky*, UID reale, effettivo e salvato (che oggi abbiamo visto solo come quattro numeri in `status`), `sudo` e `su`, le capability, e la prima *privilege escalation* della tua vita.
