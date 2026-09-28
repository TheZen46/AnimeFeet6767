YAML

```
---
lezione: 1
data: 2026-09-21
argomenti: [Introduzione ai Sistemi Operativi, Virtualizzazione, Astrazione di Processo, System Call, Context Switch, API dei Processi]
---
```

# Introduzione ai Sistemi Operativi

Il sistema operativo (OS) è il software fondamentale incaricato di assicurare che l'intero sistema informatico operi in modo corretto ed efficiente. Le sue responsabilità principali includono il rendere semplice l'esecuzione dei programmi, permettere a tali programmi di condividere la memoria e consentire loro di interagire con i dispositivi hardware. In sintesi, il sistema operativo agisce come un gestore di risorse (resource manager), amministrando l'utilizzo di CPU, memoria e dischi fisici.

  

Il concetto fondamentale su cui si basa l'architettura di un sistema operativo è la **virtualizzazione**. Il sistema operativo prende una risorsa fisica (come il processore, la memoria o il disco) e la trasforma in una forma virtuale di se stessa, la quale risulta essere più generale, potente e facile da utilizzare per i programmi applicativi. Talvolta, per questo motivo, il sistema operativo stesso viene definito come una macchina virtuale.

  

## Virtualizzazione della CPU e della Memoria

La virtualizzazione della CPU permette di trasformare un singolo processore fisico in un numero apparentemente infinito di CPU virtuali. Questo meccanismo consente a molti programmi di sembrare in esecuzione simultaneamente, condividendo di fatto l'unica CPU fisica a disposizione.

  

Parallelamente, il sistema operativo gestisce la virtualizzazione della memoria. La memoria fisica è intrinsecamente un array di byte. Durante l'esecuzione, un programma mantiene tutte le sue strutture dati in memoria, leggendo (load) specificando un indirizzo per accedere ai dati, e scrivendo (store) specificando il dato e l'indirizzo di destinazione. Attraverso la virtualizzazione, ogni processo accede a un proprio spazio di indirizzamento virtuale privato. Il sistema operativo si occupa di mappare questo spazio di indirizzi sulla memoria fisica della macchina. Di conseguenza, il riferimento a una locazione di memoria fatto da un programma in esecuzione non influisce sullo spazio di indirizzamento degli altri processi, garantendo isolamento e protezione.

  

> [!important] Definizione: Time Sharing Il sistema operativo condivide la CPU fisica attraverso una tecnica chiamata **time sharing** (condivisione del tempo). Consiste nell'eseguire un processo per un breve lasso di tempo, fermarlo, e mandarne in esecuzione un altro, promuovendo così l'illusione che esistano molte CPU virtuali. Il costo potenziale di questa operazione è legato alle prestazioni, a causa del tempo speso per effettuare il cambio di contesto (context switch).
> 
>   

## Il Problema della Concorrenza e la Persistenza

Nel momento in cui il sistema operativo gestisce simultaneamente molteplici processi, o quando si eseguono programmi moderni di tipo multi-thread, emerge il problema della concorrenza. Un thread rappresenta l'unità di esecuzione all'interno di un processo; più thread di un medesimo processo condividono lo stesso spazio di memoria.

  

Se si scrive un programma con thread multipli, non vi è alcuna garanzia che le istruzioni si sincronizzino correttamente se non vengono eseguite in modo atomico (ovvero in modo indivisibile).

  

- L'incremento di un contatore condiviso, ad esempio tramite un'istruzione come `counter++`, non è un'operazione atomica.
    
      
    
- Tale operazione si divide in tre istruzioni distinte a livello hardware: caricare il valore del contatore dalla memoria in un registro, incrementare il valore nel registro e memorizzare il nuovo valore nuovamente in memoria.
    
      
    
- Poiché queste tre istruzioni non vengono eseguite atomicamente, se un context switch avviene nel mezzo di questa sequenza, i dati possono corrompersi, rendendo necessari meccanismi di sincronizzazione come i semafori.
    
      
    

Un altro ruolo cardine del sistema operativo è la gestione della **persistenza**. Poiché la memoria volatile (come la DRAM) perde i dati in assenza di alimentazione, hardware e software devono collaborare per memorizzare le informazioni in modo persistente. L'hardware fornisce dispositivi di I/O (come hard drive o SSD), mentre a livello software il sistema operativo mette a disposizione il _File System_, responsabile della gestione del disco, dell'archiviazione dei file creati dall'utente e della gestione dei crash di sistema durante le scritture.

  

# L'Astrazione: Il Processo

L'astrazione fondamentale fornita dal sistema operativo per rappresentare un programma in esecuzione è il **processo**. Un processo non coincide semplicemente con il codice del programma salvato su disco (che è un'entità inattiva), ma rappresenta la sua esecuzione attiva.

  

Ogni processo è costituito principalmente da:

  

- **Memoria (spazio di indirizzamento):** Contiene le istruzioni del programma (sezione testo/codice) e la sezione dei dati.
    
      
    
- **Registri:** Piccole locazioni di memoria ad altissima velocità vicine alla CPU che mantengono lo stato dell'esecuzione. Tra i più importanti vi sono il _Program Counter_ (PC), che indica l'indirizzo della prossima istruzione da eseguire, e lo _Stack Pointer_, che punta al vertice dello stack.
    
      
    

## Creazione e Layout in Memoria di un Processo

La creazione di un processo segue passaggi rigorosi orchestrati dal sistema operativo:

  

1. **Caricamento (Loading):** Il sistema operativo carica il codice del programma (che inizialmente risiede su disco come file eseguibile) e i dati statici nella memoria, allocandoli nello spazio di indirizzamento del processo. Questo processo di caricamento avviene in modo "pigro" (lazily), caricando frammenti di codice o dati solo quando sono effettivamente necessari durante l'esecuzione.
    
      
    
2. **Allocazione dello Stack:** Viene allocato lo stack di runtime del programma. Lo stack viene utilizzato per le variabili locali, i parametri delle funzioni e gli indirizzi di ritorno. Viene inoltre inizializzato con gli argomenti della funzione `main()` (come `argc` e l'array `argv`).
    
      
    
3. **Creazione dell'Heap:** Viene creata l'area heap per i dati allocati dinamicamente. I programmi richiedono questo spazio chiamando funzioni come `malloc()` e lo rilasciano tramite `free()`.
    
      
    
4. **Inizializzazioni di sistema:** Il sistema operativo esegue altri compiti di inizializzazione, come la preparazione dell'I/O. Di default, ogni processo in sistemi simil-UNIX ha tre descrittori di file aperti: standard input, standard output e standard error.
    
      
    
5. **Avvio:** Il sistema operativo trasferisce il controllo della CPU al processo appena creato, avviando l'esecuzione a partire dal punto d'ingresso `main()`.
    
      
    

Snippet di codice

```
block-beta
  columns 3
  CPU["CPU"]
  space
  Memoria["Memoria Processo"]
  
  block:Processo:1
    Codice["Codice"]
    DatiStatici["Dati Statici"]
    Heap["Heap (cresce verso il basso)"]
    SpazioVuoto["..."]
    Stack["Stack (cresce verso l'alto)"]
  end
  
  space
  Disco["Disco (Programma)"]
  
  Disco --> Codice
  Disco --> DatiStatici
```

> [!tip] #approfondimento Lo schema di organizzazione della memoria del processo è standardizzato in modo da separare le aree che crescono dinamicamente. Posizionando l'Heap nella parte superiore (dopo codice e dati statici) in modo che cresca verso il basso, e lo Stack nella parte inferiore in modo che cresca verso l'alto, il sistema operativo massimizza lo spazio contiguo a disposizione per l'allocazione dinamica della memoria, minimizzando il rischio che le due aree entrino in collisione precocemente.
> 
>   

## Gli Stati del Processo

Durante il suo ciclo di vita, dal punto di vista del processore, un processo attraversa diversi stati operativi.

  

Snippet di codice

```
stateDiagram-v2
    [*] --> Ready
    Ready --> Running : Scheduled (Schedulato)
    Running --> Ready : Descheduled (Deschedulato)
    Running --> Blocked : I/O initiate (Richiesta pendente)
    Blocked --> Ready : I/O done (Risorsa disponibile)
```

- **Running (In Esecuzione):** Il processo è attualmente in esecuzione sul processore; sta attivamente consumando cicli di CPU.
    
      
    
- **Ready (Pronto):** Il processo è pronto per essere eseguito e vorrebbe eseguire le proprie istruzioni, ma per una specifica ragione il sistema operativo ha scelto di non assegnargli la CPU in questo preciso istante. Tutti i processi in questo stato risiedono nella _Ready Queue_ (coda dei processi pronti).
    
      
    
- **Blocked (Bloccato):** Il processo ha eseguito un'operazione che non può essere completata immediatamente, ad esempio l'inizializzazione di una richiesta I/O verso il disco, o l'attesa per l'acquisizione di un semaforo occupato da un altro thread. Il processo diventa bloccato in modo che un altro processo possa utilizzare il processore in modo utile, e tornerà nello stato Ready non appena l'operazione in attesa si concluderà.
    
      
    

## Il Process Control Block (PCB)

Per amministrare le transizioni di stato e garantire la correttezza esecutiva del Time Sharing, il sistema operativo necessita di strutture dati chiave, la principale delle quali è il **Process Control Block (PCB)**, storicamente noto come _proc structure_ (o _proc-struct_) in alcune implementazioni kernel come xv6.

  

Il PCB è una struttura (in linguaggio C) che raccoglie e archivia le informazioni critiche relative a ciascun processo del sistema. Tra le informazioni salvate troviamo:

  

- Lo stato attuale del processo (ad esempio, Runnable, Running, Sleeping, Zombie).
    
      
    
- L'identificatore del processo (PID - Process ID).
    
      
    
- I puntatori alla memoria del processo (inizio, fine, grandezza).
    
      
    
- La lista dei file aperti.
    
      
    
- Il **Register Context (Contesto dei Registri)**: una copia di sicurezza di tutti i registri della CPU vitali per il processo (tra cui l'Instruction Pointer / Program Counter e lo Stack Pointer). Questo contesto viene salvato e ripristinato ad ogni interruzione dell'esecuzione del processo per permetterne la successiva ripresa.
    
      
    
- Il puntatore al Kernel Stack del processo: uno stack privato gestito in modalità kernel, distinto dallo stack utente, dedicato alla memorizzazione dei dati durante l'esecuzione di chiamate di sistema o routine di interruzione.
    
      
    

# Controllo dell'Esecuzione: System Call e Privilege Mode

Il problema centrale del time sharing è: come possiamo implementare la virtualizzazione senza aggiungere un sovraccarico (overhead) eccessivo al sistema, mantenendo però al contempo il completo controllo del sistema operativo sulla CPU? Se un processo fosse eseguito direttamente e senza limiti (Direct Execution), il sistema operativo si ridurrebbe a una mera libreria e perderebbe ogni autorità.

  

Per ottenere un controllo sicuro, i moderni processori forniscono due diverse modalità di privilegio (Protected Control Transfer):

  

1. **User Mode (Modalità Utente):** Il livello in cui girano le applicazioni. In questa modalità il codice non possiede pieno accesso alle risorse hardware, né può inviare liberamente richieste di I/O o allocare memoria illimitata.
    
      
    
2. **Kernel Mode (Modalità Kernel):** Il livello privilegiato dove opera il sistema operativo, avente totale accesso e giurisdizione sulle risorse della macchina.
    
      
    

## Le System Call

Se un programma in user mode necessita di eseguire un'operazione privilegiata (leggere da disco, creare un processo), deve richiederla al sistema operativo attraverso una **System Call** (Chiamata di Sistema). Le System Call sono l'interfaccia (spesso richiamate tramite le librerie standard del C) attraverso le quali il kernel espone attentamente porzioni chiave di funzionalità ai programmi applicativi.

  

Il meccanismo di transizione da User Mode a Kernel Mode avviene tramite un'istruzione hardware speciale:

  

- **Trap Instruction:** Permette al programma di "saltare" nel kernel e contestualmente alza il livello di privilegio, passando in Kernel Mode. Al momento del salto, i registri del programma in esecuzione vengono salvati nel suo _Kernel Stack_ e il flusso passa al _trap handler_ predefinito dal sistema operativo.
    
      
    
- **Return-from-trap Instruction:** Una volta terminata la System Call, il kernel esegue questa istruzione, che decrementa il privilegio, ripristina i registri dal Kernel Stack e restituisce il controllo al programma chiamante, esattamente all'istruzione successiva alla trap.
    
      
    

Per evitare che i processi applicativi eseguano codice kernel malevolo, la CPU hardware si basa su una **Trap Table** (inizializzata all'avvio del sistema dal kernel) che associa ogni possibile richiesta (identificata da un numero) all'esatto indirizzo di memoria del gestore (handler) corrispondente all'interno del sistema operativo.

  

# Switch di Contesto e Timer Interrupt

Sorge un interrogativo: se un processo sta eseguendo un loop infinito o non chiama mai una System Call, come fa il sistema operativo a riconquistare il controllo della CPU?

  

Si distinguono due approcci teorici per restituire il controllo al SO:

  

- **Approccio Cooperativo:** Si affida alla buona fede dei programmatori. I processi rilasciano volontariamente il controllo tramite System Call dedicate come `yield()` o quando compiono operazioni illegali (come la divisione per zero). Tale sistema (impiegato storicamente nelle prime versioni di Mac OS) si dimostra fallace se un programma si blocca in un ciclo infinito senza compiere chiamate di sistema, richiedendo il riavvio della macchina.
    
      
    
- **Approccio Non-Cooperativo (Preemptive):** Utilizza un **Timer Interrupt** hardware. Durante l'avvio (boot), il sistema operativo fa partire un timer fisico che solleva un'interruzione (interrupt) a scadenze prefissate (es. ogni tot millisecondi).
    
      
    

## Il Context Switch

Quando il Timer Interrupt viene scatenato, la CPU interrompe forzatamente il processo in corso, salva il suo stato hardware nel Kernel Stack, passa in modalità Kernel e invoca il codice del gestore degli interrupt (Interrupt Handler). Questo è il momento in cui l'algoritmo di scheduling del sistema operativo decide se il processo corrente ha esaurito il suo quanto di tempo e se deve essere sostituito.

  

Se il sistema operativo opta per la sostituzione, esegue un **Context Switch** (Cambio di Contesto). Si tratta di una routine in linguaggio assembly di bassissimo livello che:

  

1. Salva i registri generali, il Program Counter (PC) e il Kernel Stack Pointer del processo attualmente in esecuzione all'interno della sua struttura PCB.
    
      
    
2. Ripristina i registri del processo subentrante precedentemente salvati nel relativo PCB.
    
      
    
3. Modifica lo Stack Pointer in modo che punti al Kernel Stack del nuovo processo.
    
      
    
4. Chiama la return-from-trap, passando il controllo del processore al nuovo processo (che riprenderà dal punto esatto indicato dal suo PC appena ripristinato).
    
      
    

> [!important] La temporizzazione e il timer interrupt sono gli elementi cardine che prevengono la monopolizzazione della CPU, garantendo che lo scheduler venga invocato e, conseguentemente, operi lo switch di contesto mantenendo attiva l'illusione della concorrenza. Qualora, durante la gestione di un interrupt, ne insorga un altro, il sistema operativo interviene o disabilitando la gestione dei nuovi interrupt provvisoriamente, o sfruttando sofisticati schemi di locking.
> 
>   

# API di Processo: Creazione ed Esecuzione in UNIX

Le API messe a disposizione ai programmatori per gestire processi nei moderni sistemi operativi offrono funzionalità di creazione, distruzione, attesa e controllo. Nei sistemi operativi della famiglia UNIX, la genesi e l'esecuzione di nuovi programmi segue un pattern molto peculiare separato in due chiamate di sistema distinte: `fork()` ed `exec()`.

  

## La System Call `fork()`

La chiamata `fork()` viene invocata per creare un nuovo processo (il processo _figlio_) a partire da quello che ha effettuato la chiamata (il processo _padre_). La peculiarità fondamentale della `fork()` è che non avvia un nuovo programma da zero: **crea in memoria una copia esatta e identica del processo padre** al momento della chiamata.

  

- Questo include l'intero spazio di indirizzamento, il codice, l'heap, i registri e lo stack (nonché il Program Counter, il che implica che il nuovo processo riprenderà la sua esecuzione esattamente sull'istruzione immediatamente successiva alla `fork()`).
    
      
    

L'unico elemento che distingue il padre dal figlio all'istante di creazione è il **valore di ritorno** della `fork()`:

  

- Nel processo **padre**, la `fork()` restituisce il PID (Process ID) del figlio appena creato.
    
      
    
- Nel processo **figlio**, la `fork()` restituisce `0`.
    
      
    
- (Restituisce un valore negativo `< 0` se la creazione fallisce).
    
      
    

## La System Call `wait()`

Tipicamente, il processo padre desidera sospendere la propria esecuzione fino al termine del lavoro del figlio. Per fare questo, utilizza la chiamata `wait()` (o `waitpid()`).

  

- La `wait(NULL)` pone il padre in uno stato "Blocked", dal quale non uscirà finché non verrà notificato del completamento del figlio e della sua corretta chiusura (tramite la chiamata `exit()`).
    
      
    

## La System Call `exec()`

Se la `fork()` crea solo un duplicato, come si fa a far eseguire al sistema un programma totalmente differente? Si ricorre alla famiglia di chiamate `exec()` (come `execvp()`).

  

- Quando il processo figlio chiama `exec()`, il sistema operativo **sostituisce interamente il codice in memoria del processo chiamante** con le istruzioni del nuovo eseguibile indicato.
    
      
    
- Anche l'area dati, lo stack e l'heap vengono re-inizializzati e distrutti; lo spazio di memoria diventa quello del nuovo programma fornito tramite stringhe e parametri.
    
      
    
- Una chiamata `exec()` riuscita non restituisce mai il controllo al codice originale che l'ha chiamata: l'esecuzione riparte dal `main()` del nuovo programma e cancella il vecchio.
    
      
    

> [!example] Creare un Processo Figlio per Contare le Parole
> 
>   
> 
> C
> 
> ```
> #include <stdio.h>
> #include <stdlib.h>
> #include <unistd.h>
> #include <string.h>
> #include <sys/wait.h>
> 
> int main(int argc, char *argv[]){
> 	int rc = fork();
> 	if (rc < 0) {
> 		fprintf(stderr, "fork failed\n");
> 		exit(1);
> 	} else if (rc == 0) { 
>       // Codice del FIGLIO
> 		char *myargs[3];
> 		myargs[0] = strdup("wc");      // Programma: "wc" (word count)
> 		myargs[1] = strdup("p3.c");    // Argomento: il file da contare
> 		myargs[2] = NULL;              // Marca la fine dell'array
> 		execvp(myargs[0], myargs);     // Sostituisce il processo e avvia "wc"
> 		printf("Questa istruzione non verrà mai stampata se execvp ha successo");
> 	} else { 
>       // Codice del PADRE
> 		int wc = wait(NULL);           // Il padre si blocca in attesa
> 		printf("Figlio completato.\n");
> 	}
> 	return 0;
> }
> ```
> 
> Questo frammento dimostra il classico workflow `fork()` -> `exec()` utilizzato, ad esempio, dalle Shell e dai terminali dei sistemi UNIX. Il terminale prima effettua una `fork` di se stesso, poi il figlio invoca `exec()` sostituendosi con l'eseguibile lanciato dall'utente.
> 
>   

## Redirezione dell'I/O (Redirection)

Questa peculiare architettura che separa la creazione (`fork`) dal caricamento (`exec`) si rivela eccezionalmente potente e versatile per manipolare l'ambiente di esecuzione prima che il nuovo programma si avvii. Il sistema operativo assegna ai flussi Standard Input, Standard Output e Standard Error gli identificatori predefiniti `0`, `1` e `2`.

  

Grazie alla separazione descritta, all'interno del processo figlio ma _prima_ di eseguire `exec()`, è possibile chiudere il descrittore associato allo standard output (`close(STDOUT_FILENO)`) e chiamare la funzione `open()` per creare e aprire un file. Il kernel riassegnerà al nuovo file appena aperto il descrittore libero dal valore più basso (in questo caso l' `1` appena rilasciato). Nel momento in cui la `exec()` andrà in esecuzione, il nuovo programma ignorerà lo scambio e manderà le stampe a schermo verso il descrittore `1`, scrivendo inconsapevolmente sul file fisico invece che sul monitor.
