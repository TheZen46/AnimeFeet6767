---
corso: Reti Logiche
modulo: 3
titolo: Flip-flop, registri e contatori
programma: [RL-04, RL-05]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-04
---

# 3 · Flip-flop, registri e contatori

**In questo modulo.** Si usano l'algebra e le mappe del modulo 1 (*Algebra booleana e sintesi delle reti combinatorie*), i multiplexer, i ritardi e i sommatori del modulo 2 (*Reti combinatorie standard, ritardi e aritmetica*). Si passa dalle reti combinatorie alle **reti sequenziali**, le cui uscite dipendono anche da ciò che è successo prima. Si vede come una retroazione crei un elemento di memoria, il latch, e perché nelle reti sincrone si usino i flip-flop che cambiano solo sul fronte del clock. Poi si studiano i parametri temporali che fissano la frequenza massima di una rete, e i due blocchi costitutivi delle reti sequenziali: i registri e i contatori. Alla fine del modulo si sa scegliere e usare i flip-flop D, JK e T, calcolare il periodo minimo del clock, progettare registri e contatori sincroni e analizzare una rete sincrona disegnandone il diagramma temporale.

## 3.1 Dalla retroazione alla memoria

In una rete combinatoria l'uscita dipende solo dagli ingressi presenti. Se però un'uscita viene riportata in ingresso (**retroazione**), la rete può ricordare. Si prenda una OR con un ingresso $A$ e l'altro collegato alla propria uscita $U$. Finché $A = 0$ e $U = 0$ la situazione è stabile; se $A$ fa un impulso a 1, $U$ va a 1 e, attraverso la retroazione, resta a 1 anche quando $A$ torna a 0. La rete ha memorizzato un 1, ma non può più dimenticarlo.

Per poterlo cancellare si mette sulla retroazione una AND con un secondo ingresso: $U = A + \bar{R}\,U$. Con $R = 1$ la retroazione è interrotta e $U$ torna a 0; con $R = 0$ e $A = 0$ l'uscita conserva il suo valore. I due comandi si chiamano **set** ($S$, porta l'uscita a 1) e **reset** ($R$, la porta a 0). C'è un punto che una rete combinatoria non ha: all'accensione, se nessuno dà un comando, il valore dell'uscita non è definito. Ogni rete sequenziale ha quindi bisogno di un comando di inizializzazione.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-04)
> **Stato ed equazione caratteristica.** Il valore memorizzato si chiama **stato** e si indica con $Q$; il valore che assumerà dopo un comando si indica con $Q^+$. Per la rete appena vista, scritta con $S$ al posto di $A$, l'equazione caratteristica è $Q^+ = S + \bar{R}\,Q$: lo stato successivo dipende dagli ingressi e dallo stato presente. È la differenza fra una rete sequenziale e una combinatoria.

## 3.2 Latch

Il **latch SR** si realizza con due porte NOR incrociate: ciascuna riceve un ingresso esterno e l'uscita dell'altra (figura 3.1). Le uscite sono $Q$ e $\bar{Q}$, che in funzionamento normale sono una la negazione dell'altra.

![Figura 3.1](../figure/3-1.svg)

| $S$ | $R$ | $Q^+$ | $\bar{Q}^+$ | Comando |
|---|---|---|---|---|
| 0 | 0 | $Q$ | $\bar{Q}$ | memorizzazione: conserva lo stato |
| 0 | 1 | 0 | 1 | reset |
| 1 | 0 | 1 | 0 | set |
| 1 | 1 | – | – | non ammesso |

Questa è la **tabella caratteristica** del latch: dagli ingressi e dallo stato presente dà lo stato successivo. La combinazione $S = R = 1$ non è ammessa perché porta entrambe le uscite a 0, e $\bar{Q}$ non è più la negazione di $Q$. C'è anche un problema peggiore: se da $S = R = 1$ i due ingressi tornano a 0 nello stesso istante, le due NOR cercano di commutare insieme e il risultato dipende da quale è più veloce. In un circuito perfettamente simmetrico le uscite oscillerebbero; nella realtà nessun circuito è perfetto e una delle due vince, ma non si sa quale. La figura 3.2 mostra un diagramma temporale con le configurazioni stabili e questo caso finale.

![Figura 3.2](../figure/3-2.svg)

Con le leggi di De Morgan lo stesso latch si realizza con due NAND incrociate. In questo caso gli ingressi sono **attivi bassi**: il comando arriva quando valgono 0, e si indicano con $\bar{S}$ e $\bar{R}$. La combinazione vietata è $\bar{S} = \bar{R} = 0$.

Un **latch con abilitazione** aggiunge un ingresso $EN$: due porte davanti al latch lasciano passare $S$ e $R$ solo quando $EN = 1$. Con $EN = 0$ il latch conserva lo stato qualunque cosa facciano $S$ e $R$; con $EN = 1$ si comporta come il latch SR. Collegando $S = D$ e $R = \bar{D}$ si ottiene il **latch D**: con $EN = 1$ l'uscita copia $D$, con $EN = 0$ conserva l'ultimo valore. Il latch D non ha combinazioni vietate, perché $S$ e $R$ non valgono mai 1 insieme (figura 3.3).

| $EN$ | $D$ | $Q^+$ |
|---|---|---|
| 0 | – | $Q$ |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

![Figura 3.3](../figure/3-3.svg)

Il **latch JK** elimina la combinazione vietata in un altro modo: le due porte d'ingresso ricevono anche le uscite incrociate, così $J$ agisce solo se $Q = 0$ e $K$ solo se $Q = 1$.

| $J$ | $K$ | $Q^+$ | Comando |
|---|---|---|---|
| 0 | 0 | $Q$ | memorizzazione |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | $\bar{Q}$ | commutazione |

Con $J = K = 1$ lo stato si inverte. Ma in un latch la commutazione non si ferma: appena $Q$ cambia, la retroazione cambia gli ingressi delle porte, e lo stato si inverte di nuovo, finché l'abilitazione resta attiva. L'uscita oscilla.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-04)
> **Trasparenza e metastabilità.** Un latch abilitato è **trasparente**: ogni variazione dell'ingresso arriva subito all'uscita. In una rete in cui l'uscita di un latch, attraverso una rete combinatoria, torna all'ingresso dello stesso latch, finché l'abilitazione è attiva i segnali girano nell'anello senza fermarsi, come nel latch JK. Per questo nelle reti sincrone si usano elementi che campionano l'ingresso in un solo istante: i flip-flop del paragrafo 3.3.
>
> Se l'ingresso di un latch cambia proprio mentre l'abilitazione si chiude, l'uscita può restare per un tempo non prevedibile a un livello intermedio prima di decidere fra 0 e 1. È la **metastabilità**, la versione reale dell'oscillazione del latch SR, e si evita rispettando i tempi del paragrafo 3.4.

## 3.3 Flip-flop sul fronte

Un **flip-flop** (FF) cambia stato solo in corrispondenza di un **fronte** del clock $CK$: il fronte di salita, da 0 a 1, per i FF **PET** (*positive edge triggered*), il fronte di discesa per i FF **NET** (*negative edge triggered*). Fra un fronte e l'altro l'uscita resta ferma qualunque cosa facciano gli ingressi. Nei simboli il fronte si indica con un triangolino sull'ingresso del clock, e un pallino davanti al triangolino indica un FF NET. In questo corso si usano i FF PET.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-04)
> **Come si ottiene il fronte.** Un modo è lo schema **master-slave**: due latch D in serie, il primo (master) abilitato quando $CK = 0$ e il secondo (slave) quando $CK = 1$. Mentre il clock è basso il master segue l'ingresso e lo slave è chiuso; quando il clock sale il master si chiude sul valore che aveva in quel momento e lo slave lo copia in uscita. L'uscita cambia quindi solo sul fronte di salita, e non c'è mai un percorso trasparente dall'ingresso all'uscita.

I tre FF che servono sono il D, il JK e il T, tutti con la stessa idea: la tabella dice quale sarà lo stato dopo il prossimo fronte.

| FF | Ingressi | $Q^+$ | Equazione caratteristica |
|---|---|---|---|
| D | $D = 0$ / $D = 1$ | 0 / 1 | $Q^+ = D$ |
| JK | $JK = 00, 01, 10, 11$ | $Q$, 0, 1, $\bar{Q}$ | $Q^+ = J\bar{Q} + \bar{K}Q$ |
| T | $T = 0$ / $T = 1$ | $Q$ / $\bar{Q}$ | $Q^+ = T \oplus Q$ |

Nel FF JK la combinazione $J = K = 1$ non fa più oscillare: lo stato si inverte una volta per fronte. Il FF **T** (*toggle*) si ottiene da un JK con $J = K = T$, oppure da un D con $D = T \oplus Q$.

I FF hanno spesso due ingressi **asincroni**, attivi bassi, che agiscono subito senza aspettare il clock: $\overline{PR}$ (*preset*) forza lo stato a 1 quando vale 0, $\overline{CL}$ (*clear*) lo forza a 0. Si usano per l'inizializzazione: il segnale $\overline{RES}$ di una rete va sui $\overline{CL}$ di tutti i FF, e quando non servono si collegano a 1.

Per il progetto serve la tabella inversa di quella caratteristica: data la transizione $Q \to Q^+$ che si vuole ottenere, quali ingressi bisogna dare. È la **tabella di eccitazione**.

| $Q \to Q^+$ | $D$ | $J$ | $K$ | $T$ |
|---|---|---|---|---|
| 0 → 0 | 0 | 0 | – | 0 |
| 0 → 1 | 1 | 1 | – | 1 |
| 1 → 0 | 0 | – | 1 | 1 |
| 1 → 1 | 1 | – | 0 | 0 |

Per il JK ci sono sempre indifferenze: per passare da 0 a 1 si può dare il set ($JK = 10$) o la commutazione ($JK = 11$), quindi $K$ non conta. Le indifferenze sono il motivo per cui le reti che comandano i JK vengono spesso più semplici di quelle che comandano i D.

> [!attenzione]
> La tabella che dagli ingressi dà lo stato successivo è la tabella **caratteristica**; quella che dalla transizione dà gli ingressi è la tabella di **eccitazione**. Negli esercizi si usano entrambe, e non vanno confuse.

## 3.4 Temporizzazioni

Un FF reale funziona correttamente solo se gli ingressi rispettano alcuni tempi rispetto al fronte del clock (figura 3.4).

> [!definizione] Parametri temporali di un flip-flop
>
> - **Tempo di setup** $t_s$ (minimo): l'ingresso deve essere stabile almeno da $t_s$ prima del fronte.
> - **Tempo di hold** $t_h$ (minimo): l'ingresso deve restare stabile almeno per $t_h$ dopo il fronte.
> - **Tempo di propagazione** $t_p$ (massimo): l'uscita cambia al più $t_p$ dopo il fronte; si distingue $t_{PLH}$ per la salita dell'uscita e $t_{PHL}$ per la discesa.
> - **Durata minima dell'impulso** $t_w$: gli impulsi del clock e dei comandi asincroni devono durare almeno $t_w$.

![Figura 3.4](../figure/3-4.svg)

Se uno di questi tempi non è rispettato il FF può prendere il valore sbagliato o diventare metastabile. Da questi parametri dipende la velocità massima di una rete sincrona.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-05)
> **Periodo minimo di una rete sincrona.** In una rete in cui le uscite dei FF passano per una rete combinatoria e tornano agli ingressi dei FF, dopo un fronte le uscite cambiano entro $t_p$, la rete combinatoria le elabora entro il suo ritardo massimo $t_{comb}$, e il risultato deve arrivare agli ingressi almeno $t_s$ prima del fronte successivo. Il periodo del clock deve quindi rispettare
> $$T_{CK} \ge T_{min} = t_p + t_{comb} + t_s, \qquad f_{max} = \frac{1}{T_{min}}.$$
> Con $t_p = 10$ ns, $t_{comb} = 25$ ns e $t_s = 5$ ns si ha $T_{min} = 40$ ns e $f_{max} = 25$ MHz. C'è anche un vincolo dall'altra parte: il nuovo valore non deve arrivare troppo presto, prima che sia passato il tempo di hold del fronte appena avvenuto. Serve che il percorso più veloce rispetti $t_{p,min} + t_{comb,min} \ge t_h$, condizione che con i FF commerciali è quasi sempre soddisfatta.

> [!attenzione]
> $T_{min}$ è un periodo, e si misura in secondi; la frequenza massima del clock è il suo inverso. Un clock a 1 MHz ha periodo $1\ \mu\text{s}$, non 1 ms.

## 3.5 Registri

Un **registro** a $n$ bit è un gruppo di $n$ FF D con lo stesso clock, che memorizza una parola di $n$ bit. A seconda di come entrano ed escono i dati si hanno quattro tipi.

- **PIPO** (*parallel input, parallel output*): ogni FF ha il suo ingresso $P_i$ e la sua uscita $Q_i$; a ogni fronte il registro carica tutti i bit insieme. Si disegna come un blocco con un bus di ingresso e uno di uscita a $n$ fili.
- **SISO** (*serial input, serial output*): i FF sono in fila, l'uscita di ciascuno è l'ingresso del successivo, il dato entra da $S_{in}$ un bit per fronte ed esce da $S_{out}$ dopo $n$ fronti. È il **registro a scorrimento** (*shift register*) (figura 3.5).
- **SIPO** (*serial input, parallel output*): è un SISO di cui si prendono tutte le uscite; converte un dato seriale in parallelo.
- **PISO** (*parallel input, serial output*): davanti a ogni FF un selettore comandato da $LD$ sceglie fra l'ingresso parallelo $P_i$ (caricamento, $LD = 1$) e l'uscita del FF precedente (scorrimento, $LD = 0$); converte un dato parallelo in seriale.

![Figura 3.5](../figure/3-5.svg)

Il **registro universale** mette davanti a ogni FF un MUX 4→1 che sceglie che cosa caricare al prossimo fronte. Numerando i bit da destra ($Q_0$ è l'LSB e $Q_{n-1}$ il più a sinistra), il bit $i$ riceve:

| $S_0 S_1$ | Ingresso del FF $i$ | Operazione |
|---|---|---|
| 00 | $Q_i$ | memorizzazione |
| 01 | $Q_{i+1}$ | scorrimento a destra |
| 10 | $Q_{i-1}$ | scorrimento a sinistra |
| 11 | $P_i$ | caricamento parallelo |

Ai due estremi gli ingressi mancanti ($Q_n$ per il bit più a sinistra, $Q_{-1}$ per il bit 0) sono ingressi seriali esterni.

## 3.6 Contatori

Un **contatore** è un registro che a ogni fronte passa al numero successivo. Nella sequenza binaria il bit $Q_0$ cambia a ogni passo, e il bit $Q_i$ cambia quando tutti i bit alla sua destra valgono 1:

| $N$ | $Q_3 Q_2 Q_1 Q_0$ | | $N$ | $Q_3 Q_2 Q_1 Q_0$ |
|---|---|---|---|---|
| 0 | 0000 | | 5 | 0101 |
| 1 | 0001 | | 6 | 0110 |
| 2 | 0010 | | 7 | 0111 |
| 3 | 0011 | | 8 | 1000 |
| 4 | 0100 | | 9 | 1001 |

Con i FF T la regola si traduce direttamente: $T_0 = 1$, $T_1 = Q_0$, $T_2 = Q_1 Q_0$, $T_3 = Q_2 Q_1 Q_0$. È il **contatore sincrono** a 4 bit, che conta da 0 a 15 e poi riparte (contatore modulo 16, figura 3.6). Tutti i FF ricevono lo stesso clock, quindi le uscite cambiano insieme.

![Figura 3.6](../figure/3-6.svg)

Con i FF D lo stesso contatore si progetta dalle equazioni. Per 2 bit: $Q_0$ si inverte sempre, $D_0 = \bar{Q}_0$ (il FF è in configurazione *toggle*); $Q_1$ si inverte quando $Q_0 = 1$, $D_1 = Q_1 \oplus Q_0$. Il contatore modulo 4 conta $0, 1, 2, 3, 0, \dots$ e ha un'uscita **TC** (*terminal count*) che vale 1 nell'ultimo stato, $TC = Q_1 Q_0$ (figura 3.7).

![Figura 3.7](../figure/3-7.svg)

Un **contatore universale** si ottiene con un registro e un sommatore: a ogni fronte il registro carica $Q + N$. Con $N = 00\dots01$ conta in avanti; con $N = 11\dots11$, che in complemento a 2 vale $-1$, conta all'indietro. Il terminal count del conteggio in avanti è lo stato con tutti i bit a 1, $TC = Q_{k-1} Q_{k-2} \cdots Q_1 Q_0$; nel conteggio all'indietro l'ultimo stato è quello con tutti i bit a 0.

> [!aggiunta] Aggiunta in revisione · fonte: Donzellini e altri, *Introduzione al progetto di sistemi digitali* (RL-05)
> **Contatore modulo N e cascata.** Per contare da 0 a $N - 1$ con $N$ non potenza di 2 si riconosce lo stato $N - 1$ e si forza lo stato successivo a 0. Per il contatore decimale (0…9), fra gli stati usati solo il 9 ($1001$) ha $Q_3 = 1$ e $Q_0 = 1$, quindi $TC = Q_3 Q_0$, e lo stato successivo è $Q^+ = \overline{TC} \cdot (Q + 1)$: un reset sincrono comandato da $TC$.
>
> Un contatore con **abilitazione** $EN$ conta solo quando $EN = 1$ e dà $TC$ solo se è abilitato. Collegando il $TC$ di un contatore all'$EN$ del successivo si ottiene un contatore con più cifre: il secondo avanza di uno ogni volta che il primo ricomincia, come le cifre di un contachilometri.

## 3.7 Analisi di reti sincrone

Analizzare una rete sincrona vuol dire ricavarne il comportamento dal circuito. Si scrivono le equazioni degli ingressi dei FF in funzione degli ingressi della rete e delle uscite dei FF, si calcola lo stato dopo ogni fronte, e si disegna il diagramma temporale. Conviene ricordare due regole: i valori si leggono **appena prima** del fronte, e le uscite dei FF cambiano **appena dopo**.

> [!esempio] Due flip-flop in cascata
> L'ingresso $IN$ va a un primo FF, la cui uscita $U_0$ va all'ingresso $D$ di un secondo FF con uscita $U_1$; i due FF hanno lo stesso clock e lo stesso $\overline{RES}$. Finché $\overline{RES} = 0$ le uscite sono a 0. Poi, a ogni fronte, $U_0$ prende il valore che $IN$ aveva appena prima del fronte, e $U_1$ quello che $U_0$ aveva appena prima: $U_1$ è $U_0$ ritardato di un periodo di clock. Un impulso di $IN$ che comincia e finisce fra due fronti non viene visto affatto.

> [!dubbio]
> Negli appunti (L08 e L07) il primo FF è un JK con $IN$ su $J$, ma non si legge dove sia collegato $K$. Se $K = \overline{IN}$, il JK si comporta come un FF D e il diagramma è quello descritto sopra. Va confermato sul circuito.

> [!esempio] Un registro a scorrimento con retroazione
> Quattro FF D sono in fila con uscite $D$, $C$, $B$, $A$ (il primo è $D$). L'ingresso del primo FF è $IN \oplus B \oplus A$, l'uscita di ogni FF è l'ingresso del successivo; il reset porta tutto a $0000$ (figura 3.8).
>
> ![Figura 3.8](../figure/3-8.svg)
>
> Lo stato successivo di $DCBA$ è $(IN \oplus B \oplus A,\ D,\ C,\ B)$. Con $IN$ fisso a 1 dopo il reset si ottiene la sequenza
>
> $0000 \to 1000 \to 1100 \to 1110 \to 0111 \to 1011 \to 1101 \to 0110 \to 0011 \to 1001 \to 0100 \to 1010 \to 0101 \to 0010 \to 0001 \to 0000$
>
> che si ripete ogni 15 fronti (lo stato $1111$ non compare). Con $IN = 1$ per un solo fronte e poi sempre 0, la rete parte da $1000$ e attraversa tutti i 15 stati diversi da $0000$:
>
> $1000 \to 0100 \to 0010 \to 1001 \to 1100 \to 0110 \to 1011 \to 0101 \to 1010 \to 1101 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 1000$
>
> È un **registro a scorrimento con retroazione lineare** (LFSR): con la sola XOR sulla retroazione genera una sequenza lunga, che sembra casuale, e si usa per esempio per produrre bit di prova. Se $IN$ resta a 0 dal reset in poi, la rete resta in $0000$ per sempre: serve almeno un 1 per farla partire.

## Esempi ed esercizi svolti

**Esercizio 1.** Completare la tabella del latch SR a NAND. Gli ingressi sono $\bar{S}$, $\bar{R}$, attivi bassi: $\bar{S}\bar{R} = 11$ memorizza, $01$ (set attivo) dà $Q = 1$, $10$ (reset attivo) dà $Q = 0$, $00$ non è ammesso perché porta entrambe le uscite a 1.

**Esercizio 2.** Ottenere un FF T da un FF D. Dalla tabella di eccitazione del D, $D = Q^+$; dal T, $Q^+ = T \oplus Q$. Quindi $D = T \oplus Q$: una XOR fra $T$ e l'uscita del FF davanti all'ingresso $D$.

**Esercizio 3.** Quale frequenza massima ha un contatore sincrono a 4 bit con FF T, se $t_p = 8$ ns, $t_s = 4$ ns e ogni AND ha un ritardo di 5 ns? Il percorso più lungo va da $Q_0$, $Q_1$, $Q_2$ attraverso la AND che dà $T_3$: se la AND è una sola porta a tre ingressi, $t_{comb} = 5$ ns e $T_{min} = 8 + 5 + 4 = 17$ ns, cioè $f_{max} \approx 58{,}8$ MHz. Se invece $T_3$ si ottiene in cascata, come $T_3 = T_2 \cdot Q_2$ con due AND in serie, $t_{comb} = 10$ ns e $T_{min} = 22$ ns ($f_{max} \approx 45{,}5$ MHz).

**Esercizio 4.** Un registro universale a 4 bit contiene $Q_3 Q_2 Q_1 Q_0 = 1011$, con ingresso seriale a destra 0 e a sinistra 0. Dopo un fronte con $S_0 S_1 = 01$ (scorrimento a destra, ogni bit prende il valore del vicino di sinistra) contiene $0101$; dopo un fronte con $S_0 S_1 = 10$ (a sinistra) partendo da $1011$ contiene $0110$.

## Riepilogo

Una retroazione trasforma una rete combinatoria in un elemento di memoria: il latch SR, con due NOR o due NAND incrociate, conserva lo stato e risponde ai comandi di set e reset, con una combinazione vietata. Con l'abilitazione si ottengono il latch D, senza combinazioni vietate, e il latch JK, che però oscilla con $J = K = 1$ perché è trasparente. I flip-flop cambiano solo sul fronte del clock e risolvono il problema; i tipi D, JK e T hanno equazioni caratteristiche $Q^+ = D$, $Q^+ = J\bar{Q} + \bar{K}Q$, $Q^+ = T \oplus Q$, e per il progetto si usa la tabella di eccitazione. I tempi di setup, hold, propagazione e durata minima vanno rispettati, e il periodo minimo di una rete sincrona è $t_p + t_{comb} + t_s$. I registri memorizzano parole di bit e possono caricare in parallelo o scorrere, e il registro universale sceglie l'operazione con un MUX per bit. I contatori sincroni si fanno con FF T ($T_i$ uguale al prodotto dei bit più bassi) o con FF D, segnalano l'ultimo stato con il terminal count e si collegano in cascata con l'abilitazione. Per analizzare una rete sincrona si scrivono le equazioni dei FF e si calcola lo stato fronte per fronte.
