YAML

```
---
lezione: 2
data: 2026-09-21
argomenti: [Limited Direct Execution, Esecuzione Diretta, Trap, System Call, Context Switch, Cooperative vs Non-Cooperative Scheduling, Timer Interrupt]
---
```

# Meccanismo: Esecuzione Diretta Limitata (Limited Direct Execution)

Il problema fondamentale affrontato dal sistema operativo (OS) nella gestione della CPU è conciliare due esigenze contrastanti:

  

1. **Prestazioni (Performance):** Implementare la virtualizzazione senza aggiungere un _overhead_ (sovraccarico) eccessivo al sistema.
    
      
    
2. **Controllo (Control):** Eseguire i processi in modo efficiente mantenendo al contempo il controllo assoluto sulla CPU.
    
      
    

La soluzione architetturale adottata per soddisfare queste richieste prende il nome di **Limited Direct Execution (LDE)**, ovvero Esecuzione Diretta Limitata.

  

## Esecuzione Diretta (Senza Limiti)

Il metodo più semplice e veloce per eseguire un programma è l'**Esecuzione Diretta** (Direct Execution): si lascia che il programma giri nativamente sull'hardware della CPU.

  

Il flusso dell'esecuzione diretta sarebbe il seguente:

  

1. Il sistema operativo crea una nuova entry nella lista dei processi.
    
      
    
2. Alloca la memoria necessaria per il programma.
    
      
    
3. Carica il codice del programma in memoria.
    
      
    
4. Prepara lo stack con gli argomenti (es. `argc` e `argv`).
    
      
    
5. Azzera i registri.
    
      
    
6. Esegue la chiamata alla funzione `main()`.
    
      
    
7. Il programma esegue il suo codice (`main()`).
    
      
    
8. Il programma esegue il `return` dal `main()`.
    
      
    
9. Il sistema operativo libera la memoria del processo.
    
      
    
10. Rimuove il processo dalla lista.
    
      
    

> [!important] Il Problema dell'Esecuzione Diretta
> 
> Pur essendo estremamente efficiente, l'esecuzione diretta incondizionata presenta un difetto critico: **senza limiti sui programmi in esecuzione, il sistema operativo non avrebbe alcun controllo**. Se un programma decidesse di eseguire un loop infinito o di monopolizzare il disco, l'OS non potrebbe intervenire, riducendosi a essere "solo una libreria".
> 
>   

Da qui nasce la necessità di introdurre delle "limitazioni" all'esecuzione diretta, affrontando due problemi principali: l'esecuzione di operazioni limitate (Restricted Operations) e il passaggio da un processo all'altro (Switching Between Processes).

  

# Problema 1: Operazioni Limitate (Restricted Operations)

Se un processo sta eseguendo direttamente sulla CPU, cosa succede quando ha bisogno di eseguire un'operazione privilegiata o potenzialmente pericolosa, come ad esempio:

  

- Inoltrare una richiesta di Input/Output (I/O) a un disco?
    
      
    
- Ottenere l'accesso a ulteriori risorse di sistema, come altra CPU o memoria aggiuntiva?
    
      
    

La soluzione hardware/software per garantire l'efficienza mantenendo il controllo si basa sul **Protected Control Transfer** (Trasferimento di Controllo Protetto), che divide l'esecuzione in due modalità di privilegio distinte:

  

- **User Mode (Modalità Utente):** Le applicazioni vengono eseguite in questa modalità e non hanno pieno accesso alle risorse hardware. Se un programma tenta di eseguire un'istruzione privilegiata in User Mode, l'hardware solleva un'eccezione e il sistema operativo interviene, generalmente terminando il processo.
    
      
    
- **Kernel Mode (Modalità Kernel):** Il sistema operativo opera in questa modalità e ha accesso completo a tutte le risorse e alle istruzioni della macchina.
    
      
    

## L'Interfaccia delle System Call

Per consentire ai programmi utente di compiere operazioni essenziali ma riservate in modo sicuro, il kernel espone porzioni specifiche di funzionalità attraverso le **System Call** (Chiamate di Sistema). Le operazioni più comuni offerte tramite le system call includono:

  

- Accesso al file system.
    
      
    
- Creazione e distruzione di processi.
    
      
    
- Comunicazione inter-processo.
    
      
    
- Allocazione di ulteriore memoria.
    
      
    

L'esecuzione di una system call comporta il superamento del confine tra User Mode e Kernel Mode. Questo passaggio è orchestrato da due speciali istruzioni hardware:

  

1. **Istruzione Trap:** Quando un programma deve eseguire una system call, chiama l'istruzione di _trap_. Questa istruzione salta direttamente nel codice del kernel e contemporaneamente eleva il livello di privilegio alla modalità Kernel (Kernel Mode).
    
      
    
2. **Istruzione Return-from-trap:** Una volta che il sistema operativo ha terminato il lavoro relativo alla system call, chiama l'istruzione di _return-from-trap_. Questa istruzione decrementa il livello di privilegio, tornando alla modalità Utente (User Mode), e restituisce il controllo al programma chiamante.
    
      
    

## Inizializzazione della Trap Table

Un dettaglio fondamentale di questo meccanismo è che il programma utente non può scegliere a proprio piacimento _quale_ indirizzo di memoria eseguire nel kernel. Se potesse, potrebbe aggirare le protezioni ed eseguire codice arbitrario con privilegi massimi.

  

Per evitare questo, il sistema operativo, al momento del boot (quando è ancora in Kernel Mode e ha il controllo assoluto), configura la **Trap Table**. Questa tabella dice all'hardware quali sono gli indirizzi di memoria esatti (i _trap handler_ o _syscall handler_) da eseguire quando si verifica una specifica eccezione o chiamata di sistema.

  

## Protocollo Limited Direct Execution: System Call

Il ciclo di vita di una system call che usa l'esecuzione diretta limitata coinvolge tre attori: OS (in Kernel Mode), Hardware e Programma (in User Mode).

  

|**Fase**|**Sistema Operativo (Kernel Mode)**|**Hardware**|**Programma (User Mode)**|
|---|---|---|---|
|**Boot**|Inizializza la trap table|Memorizza l'indirizzo del syscall handler||
|**Avvio Processo**|Crea l'entry per il processo, alloca memoria, carica il programma, imposta lo stack. Riempie il kernel stack con registri/PC. Esegue `return-from-trap`|Ripristina i registri dal kernel stack. Passa a User Mode. Salta a `main()`||
|**Esecuzione**|||Esegue il codice in `main()`. Richiede una System Call tramite istruzione **trap**|
|**Trap (Salvataggio)**||Salva i registri sul kernel stack. Passa a Kernel Mode. Salta al trap handler||
|**Gestione Syscall**|Gestisce la trap. Esegue il lavoro della syscall. Chiama `return-from-trap`|||
|**Ripristino**||Ripristina i registri dal kernel stack. Passa a User Mode. Salta al Program Counter (PC) successivo alla trap||
|**Continuazione**|||Continua l'esecuzione... Torna dal `main()` provocando un'ultima trap (`exit()`)|
|**Terminazione**|Libera la memoria del processo. Rimuove il processo dalla lista|||

# Problema 2: Lo Switch tra Processi (Switching Between Processes)

Se il processo è in esecuzione diretta sulla CPU in User Mode, significa che il sistema operativo _non_ è in esecuzione in quel momento. Se il sistema operativo non è in esecuzione, come può riprendere il controllo per fermare il processo corrente e schedularne un altro (ad esempio, se il primo ha monopolizzato la CPU o è andato in blocco infinito)?

  

La letteratura dei sistemi operativi distingue due approcci storici a questo problema.

  

## 1. Approccio Cooperativo (Wait for system calls)

Nell'approccio cooperativo, il sistema operativo confida nel fatto che i processi si comportino in modo ragionevole e cedano periodicamente il controllo della CPU.

  

Come avviene la cessione del controllo:

  

- I processi effettuano regolarmente chiamate di sistema (come la syscall esplicita `yield()`).
    
      
    
- Le applicazioni trasferiscono il controllo all'OS quando compiono operazioni illegali (es. divisione per zero o tentativo di accesso a memoria non consentita).
    
      
    

Quando il processo cede il controllo, il sistema operativo ne approfitta per decidere se riassegnare la CPU allo stesso task o a un task differente.

  

> [!warning] Criticità dell'Approccio Cooperativo
> 
> Sistemi vecchi come le prime versioni di Mac OS o il sistema Xerox Alto utilizzavano questo approccio. Il difetto critico è che se un processo entra accidentalmente (o malevolmente) in un loop infinito senza chiamare alcuna system call, il sistema operativo non ha alcun modo per interromperlo. L'unica soluzione in caso di stallo è il riavvio (reboot) dell'intera macchina.
> 
>   

## 2. Approccio Non-Cooperativo: Il Timer Interrupt (L'OS prende il controllo)

L'approccio universale moderno è di tipo **non-cooperativo** (noto anche come _preemptive scheduling_). Il sistema operativo non aspetta l'azione del programma, ma si riappropria attivamente del controllo grazie a un meccanismo hardware: il **Timer Interrupt**.

  

Durante la sequenza di avvio (boot), il sistema operativo avvia un timer hardware.

Il timer è programmato per sollevare un interrupt a intervalli regolari (ogni X millisecondi).

  

Quando viene scatenato un interrupt del timer:

  

1. Il processo attualmente in esecuzione viene immediatamente interrotto (halted) dall'hardware.
    
      
    
2. L'hardware salva uno stato sufficiente del programma (i registri) per poterne garantire la ripresa futura.
    
      
    
3. L'hardware passa il controllo a un gestore di interrupt (interrupt handler) pre-configurato dall'OS, in esecuzione in Kernel Mode.
    
      
    

> [!important] Il Timer Interrupt
> 
> Un timer interrupt restituisce all'OS la capacità di eseguire il proprio codice sulla CPU in modo indipendente dalla volontà del programma in esecuzione, permettendogli di riprendere il controllo del sistema in totale autonomia.
> 
>   

# Salvataggio e Ripristino del Contesto (Context Switch)

Una volta che il sistema operativo ha riottenuto il controllo (tramite una system call o un timer interrupt), lo scheduler del sistema prende una decisione vitale: deve continuare a eseguire il processo corrente o deve passare a un processo differente?

  

Se la decisione è di effettuare lo switch, l'OS esegue un'operazione chiamata **Context Switch** (Cambio di Contesto).

  

Il context switch è un pezzo di codice assembly di basso livello che ha il compito di:

  

1. **Salvare** alcuni valori chiave dei registri (General purpose registers, Program Counter e Kernel Stack pointer) del processo attualmente in esecuzione, copiandoli nel suo Kernel Stack e nella sua struttura dati di controllo (es. il PCB).
    
      
    
2. **Ripristinare** i registri del processo che sta per andare in esecuzione, andandoli a prelevare dal suo corrispondente Kernel Stack e PCB.
    
      
    
3. **Cambiare** (Switch) l'esecuzione in modo che la CPU cominci a utilizzare il Kernel Stack del nuovo processo in procinto di eseguire.
    
      
    

## Protocollo Limited Direct Execution: Timer Interrupt e Switch

Analizziamo il flusso completo dell'esecuzione diretta limitata gestita tramite Timer Interrupt e cambio di contesto, assumendo due processi, A e B.

  

|**Fase**|**Sistema Operativo (Kernel Mode)**|**Hardware**|**Processo A / Processo B (User Mode)**|
|---|---|---|---|
|**Boot**|Inizializza la trap table. Avvia il timer di interrupt|Memorizza gli indirizzi dei syscall handler e del timer handler. Avvia il timer.||
|**Esecuzione A**|||Processo A è in esecuzione|
|**Timer Interrupt**||Il timer interrompe la CPU dopo X millisecondi. Salva i registri di A sul kernel stack di A (k-stack(A)). Passa a Kernel Mode. Salta al trap handler||
|**Gestione Interrupt e Switch**|Gestisce la trap (scheduler). Decide di cambiare e chiama la routine `switch()`:<br><br>  <br>  <br><br>- Salva i registri di A nella _proc-struct_(A).<br><br>  <br>  <br><br>- Ripristina i registri di B dalla _proc-struct_(B).<br><br>  <br>  <br><br>- Cambia puntatore al kernel stack, passando al k-stack(B).<br><br>  <br>  <br><br>Chiama `return-from-trap` (ora verso il contesto B)|||
|**Ripristino B**||Ripristina i registri di B dal kernel stack di B (k-stack(B)). Passa a User Mode. Salta al Program Counter (PC) di B||
|**Esecuzione B**|||Processo B riprende l'esecuzione da dove era stato interrotto|

> [!tip] #approfondimento
> 
> Il codice assembly del context switch (ad esempio in kernel didattici come _xv6_ della MIT) illustra chiaramente l'essenza di questa operazione: la funzione `swtch` riceve i puntatori al vecchio e al nuovo contesto. Esegue il salvataggio manuale dei registri nello spazio di memoria del vecchio contesto e subito dopo il prelievo dei registri dallo spazio di memoria del nuovo contesto. Il salvataggio del _Stack Pointer_ (`%esp`) e dell'_Instruction Pointer_ (Program Counter) è ciò che consente il "salto" invisibile da un ambiente d'esecuzione a un altro completamente differente.
> 
>   

## Problemi di Concorrenza (Concurrency)

Cosa succede se, mentre il sistema operativo sta elaborando un'interruzione o una trap, l'hardware segnala l'arrivo di _un altro_ interrupt? Questo scenario porterebbe a corruzione dei dati se le strutture interne del kernel venissero manipolate contemporaneamente da routine concorrenti.

  

I sistemi operativi gestiscono queste problematiche (Concurrency Issues) adottando strategie di protezione. Le due metodologie principali sono:

  

1. **Disabilitazione degli Interrupt:** Il sistema operativo disabilita l'arrivo di ulteriori interrupt durante il processamento critico di un interrupt corrente.
    
      
    
2. **Schemi di Locking (Blocco):** Utilizzo di sofisticati meccanismi di sincronizzazione (lock) per proteggere e regolare l'accesso concorrente alle strutture dati interne del sistema operativo.