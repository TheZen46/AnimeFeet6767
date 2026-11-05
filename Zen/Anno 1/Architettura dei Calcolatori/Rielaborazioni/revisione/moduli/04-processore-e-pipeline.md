---
corso: Architettura dei Calcolatori
modulo: 4
titolo: Il processore, la pipeline e il parallelismo fra istruzioni
programma: [ADC-04, ADC-06, ADC-07]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 4 · Il processore, la pipeline e il parallelismo fra istruzioni

**In questo modulo.** Si usano le istruzioni e i formati del modulo 1, l'ALU del modulo 3 e le reti sequenziali di Reti Logiche (registri, multiplexer, memorie). Si costruisce prima il percorso dei dati (*datapath*) che esegue in un solo ciclo di clock le istruzioni `add`, `sub`, `and`, `or`, `lw`, `sw` e `beq`, con l'unità di controllo che lo comanda. Poi si vede perché il ciclo singolo è lento e come la pipeline a cinque stadi aumenti il numero di istruzioni completate per unità di tempo. La parte più lunga riguarda i conflitti (*hazard*) della pipeline: strutturali, sui dati e sul controllo, con gli stalli, il forwarding, l'unità di rilevamento dei conflitti, la previsione dei salti e le eccezioni. Chiudono le architetture che avviano più istruzioni per ciclo: VLIW, srotolamento dei cicli, superscalari ed esecuzione fuori ordine. Alla fine del modulo si sa disegnare il diagramma temporale di un frammento di codice, contare gli stalli con e senza forwarding, riordinare il codice per eliminarli e calcolare il CPI di un programma.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (RISC-V Pipelined Architecture 1 e 2, Control Hazards, Multiple Issue), appunto a mano *Datapath con pipeline* dell'autore; Patterson e Hennessy, *Struttura e progetto dei calcolatori*, edizione RISC-V, cap. 4 (ADC-04, ADC-06, ADC-07)
> Il modulo è scritto in revisione dal materiale del corso; l'appunto a mano dell'autore (lo schema del datapath con l'unità di forwarding e l'unità di rilevamento dei conflitti) è descritto alla fine di 4.7. Le slide usano in parte la notazione MIPS (i registri con il dollaro, il campo `Rt`): qui si usa quella RISC-V (`x1`, `rs1`, `rs2`, `rd`). I conteggi dei cicli sono controllati con `strumenti/pipe.py`.

## 4.1 Il datapath a ciclo singolo

Ogni istruzione RISC-V comincia allo stesso modo: si legge l'istruzione dalla memoria all'indirizzo contenuto nel PC (*program counter*) e si leggono uno o due registri, con i campi `rs1` e `rs2` che stanno sempre nella stessa posizione in tutti i formati. Poi le classi di istruzioni si separano, ma tutte usano l'ALU: le aritmetico-logiche per il calcolo, `lw` e `sw` per l'indirizzo, `beq` per il confronto. Infine `lw` e `sw` accedono alla memoria dati, le aritmetico-logiche e `lw` scrivono un registro, e il PC passa all'istruzione successiva ($PC + 4$) o alla destinazione del salto.

Gli elementi del datapath sono quindi il PC, la memoria delle istruzioni, il register file (due porte di lettura e una di scrittura), l'unità che estende in segno l'immediato, l'ALU, la memoria dei dati, un sommatore per $PC + 4$ e uno per l'indirizzo del salto ($PC + \text{immediato} \times 2$, perché nei salti l'immediato conta mezze parole). Dove un ingresso può arrivare da due sorgenti ci vuole un multiplexer: il secondo operando dell'ALU (registro o immediato, segnale **ALUSrc**), il dato da scrivere nel registro (uscita dell'ALU o della memoria, **MemtoReg**), il nuovo PC ($PC + 4$ o destinazione del salto, **PCSrc**). Gli elementi di stato (PC, registri, memorie) si aggiornano sul fronte del clock; tutto il resto è logica combinatoria.

Nel ciclo singolo ogni istruzione dura un ciclo, che deve bastare all'istruzione più lenta. Con i tempi delle slide (memorie e ALU 200 ps, register file 100 ps, il resto trascurabile):

| Istruzione | Mem. istr. | Lettura reg. | ALU | Mem. dati | Scrittura reg. | Totale |
|---|---|---|---|---|---|---|
| tipo R | 200 | 100 | 200 | – | 100 | 600 ps |
| `lw` | 200 | 100 | 200 | 200 | 100 | 800 ps |
| `sw` | 200 | 100 | 200 | 200 | – | 700 ps |
| `beq` | 200 | 100 | 200 | – | – | 500 ps |

Il clock deve durare 800 ps, quelli di `lw`, anche quando si esegue una `beq` che ne richiederebbe 500. È semplice da capire, ma usa male il tempo e anche l'area: un'unità funzionale si può usare una sola volta per ciclo, quindi servono due memorie separate e sommatori in più oltre all'ALU.

## 4.2 L'unità di controllo

L'unità di controllo legge il campo `opcode` dell'istruzione e genera i segnali che comandano i multiplexer, le scritture e l'ALU. Il controllo dell'ALU è a due livelli: l'unità principale produce un codice di due bit, **ALUOp**, e una piccola rete combina ALUOp con i campi `funct7` e `funct3` per ottenere i quattro bit di controllo del modulo 3. ALUOp = 00 vuol dire somma (per `lw` e `sw`, che calcolano l'indirizzo), 01 sottrazione (per `beq`, che confronta), 10 "guarda i campi funct" (per le istruzioni di tipo R).

| Istruzione | ALUSrc | MemtoReg | RegWrite | MemRead | MemWrite | Branch | ALUOp |
|---|---|---|---|---|---|---|---|
| tipo R | 0 | 0 | 1 | 0 | 0 | 0 | 10 |
| `lw` | 1 | 1 | 1 | 1 | 0 | 0 | 00 |
| `sw` | 1 | X | 0 | 0 | 1 | 0 | 00 |
| `beq` | 0 | X | 0 | 0 | 0 | 1 | 01 |

La X (indifferenza) di MemtoReg in `sw` e `beq` è possibile perché RegWrite vale 0: qualunque cosa arrivi al register file, non viene scritta. Il segnale PCSrc è l'AND di Branch e dell'uscita Zero dell'ALU: si salta solo se l'istruzione è un salto *e* i due registri sono uguali. Con le tabelle di verità di questi segnali l'unità di controllo è una rete combinatoria, che si sintetizza come nel corso di Reti Logiche; nei processori più complessi la si realizza anche come macchina a stati o con un microprogramma.

## 4.3 La pipeline

L'idea è quella della catena di montaggio: si comincia a eseguire l'istruzione successiva prima che la precedente sia finita. Si divide l'esecuzione in cinque **stadi**, uno per ogni risorsa principale:

1. **IF** (*instruction fetch*): lettura dell'istruzione e aggiornamento del PC;
2. **ID** (*instruction decode*): decodifica e lettura dei registri;
3. **EX** (*execute*): operazione dell'ALU o calcolo dell'indirizzo;
4. **MEM**: accesso alla memoria dati;
5. **WB** (*write back*): scrittura del risultato nel register file.

Fra uno stadio e l'altro si mettono i **registri di pipeline** (IF/ID, ID/EX, EX/MEM, MEM/WB), che conservano tutto ciò che serve agli stadi successivi, compresi i segnali di controllo: l'unità di controllo li genera in ID e li fa "viaggiare" con l'istruzione, e ogni stadio usa i suoi. Il ciclo di clock è fissato dallo stadio più lento, 200 ps nell'esempio, invece degli 800 del ciclo singolo.

La pipeline non accorcia la **latenza** di una singola istruzione (anzi, la allunga: 5 × 200 = 1000 ps contro 800), ma aumenta il **throughput**: a regime si completa un'istruzione per ciclo. Con $k$ stadi, ciclo $T_c$ e $n$ istruzioni senza conflitti,
$$T_{pipeline} = (k + n - 1)\, T_c,$$
perché la prima istruzione impiega $k$ cicli e le altre ne escono una per ciclo. Per $n$ grande l'accelerazione rispetto al ciclo singolo tende al rapporto fra i due cicli di clock, e se gli stadi fossero perfettamente bilanciati tenderebbe al numero di stadi. Nell'esempio tende a $800/200 = 4$, non a 5, perché gli stadi del register file usano solo 100 dei 200 ps.

L'ISA RISC-V è pensata per la pipeline: le istruzioni hanno tutte 32 bit (il fetch è sempre uguale), i campi dei registri stanno sempre nello stesso posto (si leggono i registri mentre si decodifica), gli operandi in memoria compaiono solo in `lw` e `sw` (l'indirizzo si calcola in EX e la memoria si usa in MEM) e gli accessi sono allineati.

## 4.4 I conflitti: strutturali e sui dati

Un **conflitto** (*hazard*) è una situazione in cui l'istruzione successiva non può avanzare nel ciclo previsto. Ce ne sono tre tipi.

**Conflitti strutturali.** Due istruzioni vogliono la stessa risorsa nello stesso ciclo. Con una sola memoria per istruzioni e dati, il fetch di un'istruzione e la `lw` di tre istruzioni prima si scontrerebbero: per questo la pipeline ha due memorie (in pratica due cache, una per le istruzioni e una per i dati). Il register file è usato in ID (lettura) e in WB (scrittura) da due istruzioni diverse nello stesso ciclo: si risolve scrivendo nella prima metà del ciclo e leggendo nella seconda, così un'istruzione in ID legge il valore appena scritto da quella in WB.

**Conflitti sui dati.** Un'istruzione ha bisogno di un risultato che una precedente non ha ancora scritto (*read after write*). Nel frammento

```text
add  x1, x2, x3
sub  x4, x1, x5
and  x6, x1, x7
or   x8, x1, x9
```

`add` scrive `x1` in WB, al ciclo 5, ma `sub` lo legge in ID al ciclo 3 e `and` al ciclo 4: leggerebbero il valore vecchio. `or` lo legge al ciclo 5, nella seconda metà, e lo trova giusto. Senza altri accorgimenti la pipeline deve **fermarsi** (*stall*): l'istruzione dipendente resta in ID finché il dato è scritto, e negli stadi successivi passano delle **bolle**, istruzioni nulle che non fanno niente. Un'istruzione che dipende da quella immediatamente precedente aspetta 2 cicli, una che dipende da quella di due posti prima 1 ciclo, da tre posti prima in poi nessuno.

## 4.5 Il forwarding e lo stallo load-use

Il risultato di `add` in realtà esiste già alla fine di EX, nel registro EX/MEM: basta portarlo direttamente all'ingresso dell'ALU dell'istruzione successiva, senza aspettare che passi dal register file. È il **forwarding** (o *bypassing*). Due multiplexer davanti agli ingressi dell'ALU scelgono fra il valore letto dal register file (00), quello in EX/MEM (10) e quello in MEM/WB (01), comandati dall'**unità di forwarding** con queste condizioni.

*Conflitto in EX* (dall'istruzione precedente):
$$\text{se } \text{EX/MEM.RegWrite} \wedge \text{EX/MEM.rd} \ne 0 \wedge \text{EX/MEM.rd} = \text{ID/EX.rs1} \text{ allora ForwardA} = 10,$$
e lo stesso con `rs2` per ForwardB.

*Conflitto in MEM* (da due istruzioni prima): se MEM/WB.RegWrite, MEM/WB.rd ≠ 0, MEM/WB.rd = ID/EX.rs1 **e non** c'è già il conflitto in EX sullo stesso registro, allora ForwardA = 01 (e analogamente per `rs2`).

La condizione rd ≠ 0 serve perché `x0` vale sempre 0: un'istruzione che "scrive" `x0` non deve propagare il suo risultato. La clausola "non c'è già il conflitto in EX" serve per sequenze come

```text
add  x1, x1, x2
add  x1, x1, x3
add  x1, x1, x4
```

in cui per la terza istruzione sia EX/MEM sia MEM/WB contengono un valore di `x1`: quello giusto è il più recente, in EX/MEM.

**Lo stallo load-use.** Il forwarding non basta quando il dato viene da una `lw`: è pronto solo alla fine di MEM, mentre l'istruzione successiva lo vorrebbe all'inizio di EX nello stesso ciclo. Serve un ciclo di stallo, e poi il dato arriva con il forwarding da MEM/WB. Lo inserisce l'**unità di rilevamento dei conflitti** (*hazard detection unit*), che lavora in ID:
$$\text{se } \text{ID/EX.MemRead} \wedge (\text{ID/EX.rd} = \text{IF/ID.rs1} \vee \text{ID/EX.rd} = \text{IF/ID.rs2}) \text{ allora stallo}.$$
Per fermare la pipeline si impedisce la scrittura del PC e di IF/ID (le due istruzioni dietro restano dove sono) e si azzerano i segnali di controllo che entrano in ID/EX, così in EX passa una bolla.

**Riordinare il codice.** Il compilatore può spesso evitare lo stallo load-use mettendo fra la `lw` e l'istruzione che usa il dato un'istruzione indipendente. È un esempio di come l'hardware e il compilatore lavorino insieme sulle prestazioni (esercizio 3).

## 4.6 I conflitti sul controllo e la previsione dei salti

Il terzo tipo di conflitto riguarda il PC. Dopo una `beq` la pipeline deve leggere l'istruzione successiva, ma non sa ancora quale: nella pipeline di base la decisione è presa in MEM (il confronto in EX, la scrittura del PC dopo), e se il salto è preso le tre istruzioni lette nel frattempo vanno buttate. Le soluzioni sono quattro.

**Stallo.** Si aspetta la decisione: si perdono sempre dei cicli, anche quando il salto non è preso.

**Anticipare la decisione.** Si spostano in ID il sommatore dell'indirizzo di destinazione e un comparatore di uguaglianza fra i due registri (più veloce dell'ALU: basta lo XOR bit a bit e una NOR). Il salto si decide in ID e si perde al massimo un ciclo. Il prezzo: in ID servono anche il forwarding e gli stalli per gli operandi del confronto. Se la `beq` usa il risultato dell'istruzione aritmetica immediatamente precedente serve 1 ciclo di stallo, se usa quello di una `lw` immediatamente precedente ne servono 2.

**Previsione statica.** Si prevede che il salto non sia preso e si continua a leggere in sequenza; se poi il salto è preso, l'istruzione letta si scarta (*flush*: il registro IF/ID viene azzerato). Si perde un ciclo solo quando la previsione è sbagliata. La previsione "non preso" funziona bene per i salti in testa ai cicli, che escono di rado, male per quelli in fondo ai cicli, che sono quasi sempre presi: un'alternativa è prevedere presi i salti all'indietro e non presi quelli in avanti. Nell'architettura MIPS delle slide esiste anche il **salto ritardato** (*delayed branch*): l'istruzione dopo il salto viene eseguita sempre, e il compilatore ci mette un'istruzione utile e indipendente (*delay slot*). RISC-V non ha delay slot.

**Previsione dinamica.** Si usa la storia del salto: una **branch history table** (BHT), indirizzata dai bit bassi del PC e letta in IF, contiene per ogni salto l'esito recente. Con **un bit** si prevede l'ultimo esito, e un ciclo sbaglia due volte a ogni esecuzione completa: all'uscita, e alla prima iterazione della volta successiva. Con **due bit** (un contatore saturato con quattro stati: fortemente preso, debolmente preso, debolmente non preso, fortemente non preso) la previsione cambia solo dopo due errori consecutivi, e il ciclo sbaglia solo all'uscita: per un ciclo di 10 iterazioni si passa dall'80% al 90% di previsioni corrette. La BHT dice *se* saltare ma non *dove*: per non aspettare il calcolo dell'indirizzo, un **branch target buffer** (BTB) memorizza le destinazioni dei salti già incontrati.

Con un salto ogni 5-6 istruzioni, e pipeline sempre più lunghe, la previsione è decisiva per le prestazioni: la penalità di un errore cresce con il numero di stadi che precedono la decisione.

## 4.7 Le eccezioni

Un'**eccezione** è un evento che interrompe il normale flusso del programma; si chiama **interruzione** (*interrupt*) quando viene dall'esterno del processore, come una richiesta di un dispositivo di I/O. Per la pipeline è un conflitto sul controllo: bisogna fermare l'esecuzione, completare le istruzioni precedenti, scartare quella che ha causato l'eccezione e le successive, salvare l'indirizzo dell'istruzione (in RISC-V nel registro **SEPC**) e la causa (nel registro **SCAUSE**), e saltare a un indirizzo fisso dove si trova il gestore del sistema operativo.

| Evento | Stadio | Sincrono? |
|---|---|---|
| Istruzione non definita | ID | sì |
| Page fault, errore di accesso alla memoria | IF, MEM | sì |
| Overflow (nelle ISA che lo segnalano, come MIPS) | EX | sì |
| Richiesta di un dispositivo di I/O | qualsiasi | no |
| Malfunzionamento dell'hardware | qualsiasi | no |

Nello stesso ciclo ci possono essere più eccezioni, in stadi diversi: l'hardware dà la precedenza a quella dell'istruzione più vecchia, cioè più avanti nella pipeline. Le eccezioni gestite in modo che tutte le istruzioni precedenti siano completate e nessuna successiva abbia modificato lo stato si dicono **precise**.

> [!nota] Lo schema dell'appunto a mano
> L'appunto a mano disegna il datapath completo della fine del capitolo: i registri IF/ID, ID/EX, EX/MEM, MEM/WB; il comparatore di uguaglianza in ID per decidere i salti, con una sua unità di forwarding; l'unità di forwarding in EX che comanda i multiplexer davanti all'ALU; l'unità di rilevamento dei conflitti in ID; e, in ingresso al multiplexer del PC, l'indirizzo fisso del gestore delle eccezioni (nello schema quello MIPS delle slide, `8000 0180` esadecimale).

## 4.8 Più istruzioni per ciclo

La pipeline avvicina il CPI a 1. Per scendere sotto 1 bisogna avviare più istruzioni per ciclo (*multiple issue*); in questo caso si usa spesso il suo inverso, l'**IPC** (istruzioni per ciclo). Le strade sono due.

**Avvio multiplo statico (VLIW).** È il compilatore a raggruppare le istruzioni in **pacchetti** che partono insieme. Nell'esempio del corso il pacchetto ha due posti: uno per un'istruzione aritmetico-logica o un salto, uno per una `lw` o una `sw`. Servono più porte di lettura e scrittura nel register file e un sommatore in più per gli indirizzi. Il compilatore deve rispettare le dipendenze: in un pacchetto non ci possono essere due istruzioni dipendenti, il risultato di un'istruzione aritmetica si può usare nel pacchetto successivo, quello di una `lw` solo due pacchetti dopo; se non trova un'istruzione per un posto, ci mette una `nop`.

Per riempire i pacchetti si usa lo **srotolamento dei cicli** (*loop unrolling*): si copia più volte il corpo del ciclo, si aggiorna il puntatore una volta sola e si usano registri diversi per le varie copie. Così diminuiscono le istruzioni di controllo del ciclo e ci sono più istruzioni indipendenti da accoppiare (esercizio 7). L'uso di registri diversi elimina le **antidipendenze** fra le copie: è una ridenominazione dei registri fatta dal compilatore.

**Avvio multiplo dinamico (superscalare).** È l'hardware a decidere, durante l'esecuzione, quante e quali istruzioni avviare. Le istruzioni vengono lette e decodificate in ordine e messe in una coda; vengono **eseguite fuori ordine** (*out of order*), appena gli operandi sono disponibili, in unità funzionali con le loro stazioni di prenotazione; i risultati vengono scritti nei registri e in memoria di nuovo **in ordine** (*commit*), attraverso un buffer di riordino, così le eccezioni restano precise e le istruzioni eseguite per una previsione sbagliata (esecuzione **speculativa**) si possono annullare.

Con l'esecuzione fuori ordine non contano più solo le dipendenze vere. Fra due istruzioni $i$ e $j$, con $i$ prima di $j$:

- **dipendenza vera** (*read after write*, RAW): $j$ legge un registro scritto da $i$;
- **antidipendenza** (*write after read*, WAR): $j$ scrive un registro letto da $i$;
- **dipendenza di uscita** (*write after write*, WAW): $j$ e $i$ scrivono lo stesso registro.

Le dipendenze vere vengono dal flusso dei dati dell'algoritmo e non si possono togliere. Le altre due nascono solo perché i registri dell'ISA sono pochi e vengono riusati: sono in realtà conflitti strutturali, e l'hardware li elimina con la **ridenominazione dei registri** (*register renaming*), usando un insieme più grande di registri fisici.

I limiti: la tabella dei processori Intel delle slide mostra che dal Pentium 4 (fino a 31 stadi e 3,6 GHz, oltre 100 W) si è tornati a pipeline più corte e a più core per chip. Le pipeline lunghe e l'avvio multiplo sono frenati dal consumo e dal calore (*power wall*), dal parallelismo limitato presente nei programmi e dalla latenza della memoria.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle slide (Pipelined Architecture, Control Hazards, Multiple Issue); conteggi controllati con `strumenti/pipe.py` e `strumenti/verifica_ampliamento.py` (ADC-04, ADC-06, ADC-07)

**Esercizio 1. Ciclo singolo o pipeline?** Memorie 250 ps, ALU 150 ps, register file 100 ps. Si confrontino il ciclo singolo e la pipeline a 5 stadi su 1000 istruzioni senza conflitti.

Ciclo singolo: l'istruzione più lunga è `lw`, $250 + 100 + 150 + 250 + 100 = 850$ ps; il programma dura $1000 \times 850 = 850$ ns. Pipeline: il ciclo è quello dello stadio più lento, 250 ps; il programma dura $(5 + 999) \times 250 = 251$ ns. L'accelerazione è $850/251 \approx 3{,}39$. Il limite per $n \to \infty$ è $850/250 = 3{,}4$, lontano da 5 perché gli stadi sono sbilanciati: ID, EX e WB lavorano 100 o 150 ps su 250.

**Esercizio 2. I segnali di controllo di `lw` e `beq`.** Perché ALUSrc vale 1 in `lw` e 0 in `beq`, e perché ALUOp è diverso?

`lw x5, 8(x10)` somma il registro `x10` e l'immediato 8: il secondo operando dell'ALU è l'immediato, ALUSrc = 1, e l'operazione è una somma, ALUOp = 00. `beq x5, x6, L` confronta due registri: il secondo operando è un registro, ALUSrc = 0, e il confronto si fa con una sottrazione che accende Zero se il risultato è nullo, ALUOp = 01. L'immediato di `beq` serve, ma al sommatore della destinazione, non all'ALU.

**Esercizio 3. Stalli e riordino.** Si contino i cicli del frammento, con e senza forwarding, e lo si riordini per togliere gli stalli.

```text
lw   t0, 0(a0)
lw   t1, 4(a0)
add  t2, t0, t1
sw   t2, 8(a0)
addi a0, a0, 12
```

*Senza forwarding.* `add` legge `t1` in ID e deve aspettare che la seconda `lw` lo scriva in WB: 2 stalli. `sw` legge `t2`, prodotto da `add` subito prima: altri 2 stalli. In tutto $5 + 4 + 4 = 13$ cicli.

*Con forwarding.* Resta solo lo stallo load-use fra la seconda `lw` e `add`: 10 cicli. Il diagramma:

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| `lw t0` | IF | ID | EX | MEM | WB | | | | | |
| `lw t1` | | IF | ID | EX | MEM | WB | | | | |
| `add` | | | IF | ID | ID | EX | MEM | WB | | |
| `sw` | | | | IF | IF | ID | EX | MEM | WB | |
| `addi` | | | | | | IF | ID | EX | MEM | WB |

Al ciclo 5 in EX passa una bolla; `t1` arriva all'ALU di `add` al ciclo 6 dal registro MEM/WB.

*Riordino.* `addi` non dipende da nessuna delle istruzioni precedenti tranne che per `a0`, che le due `lw` leggono prima. La si sposta fra la seconda `lw` e `add`, correggendo lo spiazzamento della `sw`, che ora vede `a0` già aumentato di 12:

```text
lw   t0, 0(a0)
lw   t1, 4(a0)
addi a0, a0, 12
add  t2, t0, t1
sw   t2, -4(a0)
```

Con il forwarding non ci sono più stalli: 9 cicli, il minimo per 5 istruzioni. Senza forwarding servono 12 cicli.

**Esercizio 4. Una catena di dipendenze.**

```text
add  s1, s2, s3
sub  s4, s1, s5
and  s6, s1, s4
or   s7, s6, s2
sw   s7, 0(a0)
```

Ogni istruzione dipende da quella immediatamente precedente. Senza forwarding: 2 stalli per ciascuna delle ultime quattro, $9 + 8 = 17$ cicli. Con il forwarding nessuno stallo, perché nessun dato viene da una `lw`: 9 cicli. Il guidato 1 mostra da dove arriva ogni operando.

**Esercizio 5. Salti decisi in ID.** Quanti stalli in queste due coppie, con forwarding e salti decisi in ID?

```text
lw   t0, 0(a0)          addi t1, t1, 1
beq  t0, zero, fine     bne  t1, t2, ciclo
```

La `beq` confronta in ID, un ciclo prima di quando un'istruzione aritmetica userebbe l'operando in EX. Il valore di `lw` è pronto alla fine di MEM: se `lw` è in MEM al ciclo $c$, la `beq` può essere in ID solo al ciclo $c + 1$, cioè 2 stalli. Il valore di `addi` è pronto alla fine di EX: 1 stallo. In un ciclo conviene quindi mettere fra l'aggiornamento del contatore e il salto un'istruzione indipendente.

**Esercizio 6. Il CPI con stalli e salti.** In un programma il 25% delle istruzioni sono `lw`, e il 40% di queste è seguito da un'istruzione che usa il dato; il 15% sono salti, presi nel 60% dei casi. La pipeline ha il forwarding e prevede "non preso". Calcolare il CPI con salti decisi in ID e in MEM, e con un predittore dinamico corretto nel 90% dei casi (e un BTB) con decisione in ID.

Ogni stallo load-use costa 1 ciclo: $0{,}25 \times 0{,}4 = 0{,}1$ cicli per istruzione. Decisione in ID: un salto preso costa 1 ciclo, $0{,}15 \times 0{,}6 \times 1 = 0{,}09$; $\text{CPI} = 1 + 0{,}1 + 0{,}09 = 1{,}19$. Decisione in MEM: un salto preso costa 3 cicli, $0{,}15 \times 0{,}6 \times 3 = 0{,}27$; $\text{CPI} = 1{,}37$. Predittore dinamico: si paga 1 ciclo solo sugli errori, $0{,}15 \times 0{,}1 = 0{,}015$; $\text{CPI} = 1{,}115$.

**Esercizio 7. VLIW e srotolamento.** Il ciclo `b[i] = 2 * a[i]` su $n$ elementi ($n$ pari), con `a0` = indirizzo di `a`, `a1` = indirizzo di `b`, `a2` = indirizzo di fine di `a`, va schedulato su un processore a due vie (aritmetica o salto | `lw` o `sw`).

```text
lp:  lw   t0, 0(a0)
     slli t0, t0, 1
     sw   t0, 0(a1)
     addi a0, a0, 4
     addi a1, a1, 4
     bne  a0, a2, lp
```

*Senza srotolamento.* `slli` usa il dato della `lw`: almeno due pacchetti dopo. `sw` usa `slli`: un pacchetto dopo. Le due `addi` si possono anticipare, correggendo lo spiazzamento della `sw`:

```text
lp:  addi a0, a0, 4     |  lw   t0, 0(a0)
     addi a1, a1, 4     |  nop
     slli t0, t0, 1     |  nop
     bne  a0, a2, lp    |  sw   t0, -4(a1)
```

Nel primo pacchetto `lw` legge `a0` insieme ad `addi`, quindi il valore vecchio. Sono 6 istruzioni in 4 cicli: IPC 1,5.

*Srotolando due volte* (copie con `t0` e `t1`, puntatori aggiornati di 8):

```text
lp:  addi a0, a0, 8     |  lw   t0, 0(a0)
     addi a1, a1, 8     |  lw   t1, -4(a0)
     slli t0, t0, 1     |  nop
     slli t1, t1, 1     |  sw   t0, -8(a1)
     bne  a0, a2, lp    |  sw   t1, -4(a1)
```

Sono 9 istruzioni in 5 cicli: IPC 1,8, cioè 2,5 cicli per elemento invece di 4. Il secondo `lw` vede `a0` già aumentato di 8, per questo il suo spiazzamento è −4 (cioè $+4$ rispetto al valore vecchio). Senza il secondo registro `t1` le due copie si pesterebbero i piedi: è la ridenominazione fatta dal compilatore.

**Esercizio 8. Dipendenze e ridenominazione.**

```text
mul  t0, t1, t2      # 1
add  t3, t0, t4      # 2
sub  t0, t5, t6      # 3
and  t4, t0, t3      # 4
```

Dipendenze vere: 1 → 2 su `t0`, 3 → 4 su `t0`, 2 → 4 su `t3`. Antidipendenze: 2 legge `t0` che 3 scrive (2 → 3); 2 legge `t4` che 4 scrive (2 → 4). Dipendenza di uscita: 1 e 3 scrivono `t0`. Ridenominando il `t0` scritto da 3 in un registro fisico nuovo `p1` (e il `t4` scritto da 4 in `p2`), la 3 diventa `sub p1, t5, t6` e la 4 `and p2, p1, t3`: la 3 può partire subito, in parallelo alla `mul`, che è lenta.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni controllate con `strumenti/pipe.py` e `strumenti/verifica_ampliamento.py` (ADC-04, ADC-06)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. I segnali di forwarding.** Per il frammento dell'esercizio 4, dire per ogni istruzione che valori hanno ForwardA e ForwardB quando è in EX.

*Passo 1: che cosa c'è negli stadi.* Quando l'istruzione $i$ è in EX, la $i - 1$ è in MEM (il suo risultato è in EX/MEM) e la $i - 2$ in WB (il risultato è in MEM/WB).

*Passo 2: `sub s4, s1, s5`.* In EX/MEM c'è `add`, con rd = `s1` = rs1: ForwardA = 10. `s5` viene dal register file: ForwardB = 00.

*Passo 3: `and s6, s1, s4`.* In EX/MEM c'è `sub` (rd = `s4` = rs2): ForwardB = 10. In MEM/WB c'è `add` (rd = `s1` = rs1), e EX/MEM non scrive `s1`: ForwardA = 01.

*Passo 4: `or s7, s6, s2`.* In EX/MEM c'è `and` (rd = `s6` = rs1): ForwardA = 10. `s2` non è scritto da nessuna delle due: ForwardB = 00.

*Passo 5: `sw s7, 0(a0)`.* Il dato da scrivere `s7` (rs2) viene da `or` in EX/MEM: ForwardB = 10; `a0` (rs1) dal register file: ForwardA = 00.

**Guidato 2. Predittore a 1 e a 2 bit su un ciclo annidato.** Il ciclo interno ha 4 iterazioni e viene eseguito molte volte: il suo salto in fondo dà la sequenza preso, preso, preso, non preso, ripetuta. Che percentuale di previsioni corrette danno i due predittori a regime?

*Passo 1: un bit.* All'inizio di un'esecuzione il bit vale "non preso" (l'ultimo esito). Prima iterazione: previsto non preso, è preso, errore; il bit diventa "preso". Seconda e terza: giuste. Quarta: previsto preso, non preso, errore. Due errori su quattro: 50%.

*Passo 2: due bit.* A regime il contatore è a "fortemente preso" durante il ciclo; all'uscita sbaglia e scende a "debolmente preso". Alla prima iterazione successiva prevede ancora preso e indovina, tornando a "fortemente preso". Un errore su quattro: 75%.

*Passo 3: il confronto.* Più il ciclo è corto, più conta il secondo bit: per 10 iterazioni si passa da 80% a 90%, per 4 da 50% a 75%.

**Guidato 3. Diagramma con un salto preso.** Con forwarding, salti decisi in ID e previsione "non preso", quanti cicli impiega questo frammento se il salto è preso e la destinazione è `fine: sub t3, t0, t1`?

```text
     addi t1, t1, 1
     beq  t1, t2, fine
     add  t4, t4, t1
fine: sub  t3, t0, t1
```

*Passo 1: lo stallo.* `beq` usa `t1` da `addi` immediatamente prima, e la decide in ID: 1 stallo.

*Passo 2: il flush.* Mentre `beq` è in ID (al secondo tentativo, ciclo 4), in IF c'è `add`. Il salto è preso: `add` si scarta e al ciclo 5 si legge `sub`.

*Passo 3: il conto.* `sub` è in IF al ciclo 5 e in WB al ciclo 9. In tutto 9 cicli per 3 istruzioni utili: i cicli persi sono uno per lo stallo e uno per il flush.

## Riepilogo

Il datapath a ciclo singolo esegue ogni istruzione in un ciclo lungo quanto quella più lenta; l'unità di controllo genera dai campi dell'istruzione i segnali dei multiplexer, delle scritture e dell'ALU, con il controllo dell'ALU a due livelli. La pipeline a cinque stadi IF, ID, EX, MEM, WB, con i registri di pipeline, completa a regime un'istruzione per ciclo: aumenta il throughput, non riduce la latenza, e il ciclo è fissato dallo stadio più lento. I conflitti strutturali si evitano con memorie separate e con il register file che scrive e legge nelle due metà del ciclo. I conflitti sui dati si risolvono con il forwarding da EX/MEM e da MEM/WB; resta lo stallo load-use, inserito dall'unità di rilevamento dei conflitti e spesso evitabile riordinando il codice. I conflitti sul controllo si riducono decidendo i salti in ID e con la previsione statica o dinamica (BHT a uno o due bit, BTB). Le eccezioni sono conflitti sul controllo gestiti salvando l'indirizzo e la causa. Per avviare più istruzioni per ciclo ci sono il VLIW, in cui il compilatore forma i pacchetti aiutandosi con lo srotolamento dei cicli, e i processori superscalari, che eseguono fuori ordine, eliminano antidipendenze e dipendenze di uscita con la ridenominazione e scrivono i risultati in ordine.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (ADC-04, ADC-06, ADC-07)

### Tempi

$$T_{\text{ciclo singolo}} = n \cdot T_{\text{istr. più lenta}}, \qquad T_{pipeline} = (k + n - 1) T_c, \qquad T_c = \max(\text{stadi}), \qquad \text{accelerazione} \to \frac{T_{\text{ciclo singolo}}}{T_c}.$$

$$\text{CPI} = 1 + \sum (\text{frequenza} \times \text{cicli di stallo}), \qquad \text{IPC} = 1/\text{CPI}.$$

### Stalli nella pipeline a 5 stadi

| Situazione | Senza forwarding | Con forwarding |
|---|---|---|
| uso subito dopo un'istruzione aritmetica | 2 | 0 |
| uso due istruzioni dopo | 1 | 0 |
| uso subito dopo una `lw` | 2 | 1 |
| salto in ID subito dopo un'aritmetica | 2 | 1 |
| salto in ID subito dopo una `lw` | 2 | 2 |
| salto preso con previsione "non preso" | 1 (decisione in ID), 3 (in MEM) | uguale |

### Condizioni

Forwarding da EX/MEM: RegWrite ∧ rd ≠ 0 ∧ rd = rs1 (rs2) → 10. Da MEM/WB: RegWrite ∧ rd ≠ 0 ∧ rd = rs1 (rs2) ∧ non dal precedente → 01. Load-use: ID/EX.MemRead ∧ ID/EX.rd ∈ {IF/ID.rs1, IF/ID.rs2} → stallo (PC e IF/ID fermi, controlli azzerati).

### Segnali di controllo

| | ALUSrc | MemtoReg | RegWrite | MemRead | MemWrite | Branch | ALUOp |
|---|---|---|---|---|---|---|---|
| R | 0 | 0 | 1 | 0 | 0 | 0 | 10 |
| `lw` | 1 | 1 | 1 | 1 | 0 | 0 | 00 |
| `sw` | 1 | X | 0 | 0 | 1 | 0 | 00 |
| `beq` | 0 | X | 0 | 0 | 0 | 1 | 01 |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Throughput, latenza | istruzioni completate per unità di tempo; durata di una istruzione |
| Registro di pipeline | conserva dati e controlli fra due stadi |
| Hazard strutturale, sui dati, sul controllo | risorsa contesa; dato non pronto; PC non noto |
| Stallo, bolla | fermare le istruzioni dietro; istruzione nulla che avanza |
| Forwarding | portare un risultato all'ALU prima della scrittura nei registri |
| Load-use | uso del dato di una `lw` subito dopo: 1 stallo |
| Flush | scartare le istruzioni lette per errore |
| BHT, BTB | tabella degli esiti dei salti; tabella delle destinazioni |
| Eccezione precisa | prima completate, dopo nessun effetto |
| VLIW, superscalare | avvio multiplo deciso dal compilatore; dall'hardware |
| RAW, WAR, WAW | dipendenza vera, antidipendenza, di uscita |
| Register renaming | registri fisici in più per eliminare WAR e WAW |

### Domande che tornano spesso

- Disegnare il datapath a ciclo singolo e spiegare i segnali di controllo per `lw`, `sw`, `beq` e tipo R.
- Perché la pipeline aumenta il throughput ma non riduce la latenza? Formula dell'accelerazione.
- Tipi di conflitti e soluzioni; condizioni del forwarding e dello stallo load-use.
- Come si riducono i conflitti sul controllo? Predittori a uno e due bit.
- Come gestisce le eccezioni la pipeline?
- VLIW e superscalare: differenze; srotolamento dei cicli; dipendenze e ridenominazione.
