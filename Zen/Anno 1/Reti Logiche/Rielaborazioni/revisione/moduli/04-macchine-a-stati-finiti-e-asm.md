---
corso: Reti Logiche
modulo: 4
titolo: Macchine a stati finiti e progetto con ASM
programma: [RL-06, RL-07, RL-08]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 4 · Macchine a stati finiti e progetto con ASM

**In questo modulo.** Si usano le sintesi con le mappe del modulo 1 (*Algebra booleana e sintesi delle reti combinatorie*), i blocchi standard del modulo 2 (*Reti combinatorie standard, ritardi e aritmetica*) e i flip-flop, i registri e i contatori del modulo 3 (*Flip-flop, registri e contatori*). Si vede che ogni rete sequenziale sincrona è una **macchina a stati finiti**, nelle due varianti di Moore e di Mealy, e si impara a descriverla con i diagrammi **ASM**. Poi si segue la procedura completa di progetto, dalla specifica al circuito con FF D o JK, e quella inversa di analisi. Seguono le strutture che ricorrono negli esercizi, la gestione degli stati non usati, alcuni progetti completi, l'architettura controllore-datapath e la verifica con il simulatore. Alla fine del modulo si sa progettare a livello funzionale un semplice sistema digitale basato su macchine a stati finiti, che è il risultato atteso dal corso.

## 4.1 La macchina a stati finiti

Una **macchina a stati finiti** (MSF, in inglese FSM) sincrona è composta da tre parti (figura 4.1):

- il **registro di stato**, fatto di $k$ FF con lo stesso clock e lo stesso reset, che memorizza lo stato presente $X = X_{k-1} \dots X_0$;
- la **rete di calcolo dello stato successivo**, combinatoria, che dagli ingressi $I$ e dallo stato presente calcola lo stato successivo $X^+$, che il registro carica al prossimo fronte;
- la **rete di calcolo delle uscite**, combinatoria, che produce le uscite $U$.

![Figura 4.1](../figure/4-1.svg)

Con $k$ FF gli stati possibili sono al più $2^k$, da cui il nome. Nella **macchina di Moore** le uscite dipendono solo dallo stato presente, $U = f(X)$; nella **macchina di Mealy** dipendono anche dagli ingressi, $U = f(X, I)$, e la rete delle uscite riceve anche gli ingressi. Si suppone sempre che gli ingressi siano **sincronizzati** con il clock, cioè che cambino lontano dai fronti; un ingresso che arriva dall'esterno, come un pulsante, si sincronizza prima con un FF (paragrafo 4.5).

Il funzionamento si legge sul diagramma temporale: a ogni fronte il registro carica lo stato successivo, nel periodo seguente la rete combinatoria calcola il nuovo stato successivo dagli ingressi e dallo stato, e così via. Lo stato è una configurazione di bit, ma per ragionare conviene dargli un nome (a, b, c, …) e scrivere sul diagramma la sequenza degli stati invece dei singoli bit.

## 4.2 Il linguaggio ASM

Il diagramma **ASM** (*algorithmic state machine*) è un linguaggio grafico per descrivere il funzionamento di una MSF, simile a un diagramma di flusso ma con un significato temporale preciso. Gli elementi sono tre (figura 4.2).

> [!definizione] Elementi del diagramma ASM
>
> - Il **blocco di stato** è un rettangolo, uno per ogni stato, con il nome dello stato a lato e il suo codice sopra. Dentro si scrivono le uscite che valgono 1 in quello stato (le uscite di Moore); le uscite non scritte valgono 0.
> - Il **blocco decisionale** è un rombo con una condizione sugli ingressi e due uscite, 1 e 0. Si attraversa nello stesso periodo di clock dello stato da cui parte.
> - Il **blocco di uscita condizionata** è un ovale dopo un rombo, con le uscite che valgono 1 quando la macchina è nello stato e la condizione è vera (le uscite di Mealy).
>
> Lo stato di reset si indica con un segno sulla freccia che entra nel suo blocco. Ogni periodo di clock corrisponde al percorso da un blocco di stato al successivo: il blocco di stato con i rombi e gli ovali che lo seguono si chiama **blocco ASM**.

![Figura 4.2](../figure/4-2.svg)

> [!esempio] Contatore modulo 4
> Il contatore ha uscite $U_1$, $U_0$ e $TC$, e conta $0, 1, 2, 3, 0, \dots$ con $TC = 1$ nell'ultimo stato. L'ASM ha quattro blocchi di stato in fila, senza rombi, perché la macchina non ha ingressi oltre al clock e al reset (figura 4.3): nello stato 0 non c'è nessuna uscita, nello stato 1 c'è $U_0$, nello stato 2 $U_1$, nello stato 3 $TC$, $U_1$, $U_0$.
>
> | Stato | $TC$ | $U_1$ | $U_0$ |
> |---|---|---|---|
> | 0 | 0 | 0 | 0 |
> | 1 | 0 | 0 | 1 |
> | 2 | 0 | 1 | 0 |
> | 3 | 1 | 1 | 1 |

![Figura 4.3](../figure/4-3.svg)

> [!esempio] Contatore avanti e indietro
> Con un ingresso $U/D$ il contatore conta in avanti, $0, 1, 2, 3, 0, \dots$, se $U/D = 1$, e all'indietro, $3, 2, 1, 0, 3, \dots$, se $U/D = 0$. L'ASM ha gli stessi quattro blocchi di stato, ma dopo ciascuno c'è un rombo su $U/D$: con 1 si va allo stato successivo, con 0 al precedente (figura 4.4).

![Figura 4.4](../figure/4-4.svg)

## 4.3 La procedura di progetto

Il progetto di una MSF segue sempre gli stessi passi.

0. **Specifica**: si capisce che cosa deve fare la macchina, quali sono gli ingressi e le uscite, e lo si scrive in modo preciso, di solito con un diagramma temporale di esempio.
1. **Descrizione formale**: si disegna l'ASM. Esistono anche linguaggi testuali di descrizione dell'hardware, come VHDL e Verilog, che servono allo stesso scopo.
2. **Registro di stato**: si sceglie il numero di FF, almeno $\lceil \log_2(\text{numero di stati}) \rceil$, e si assegna un codice a ogni stato.
3. **Reti combinatorie**: si scrivono la tabella delle uscite e la tabella degli stati (stato presente e ingressi → stato successivo), si ricavano gli ingressi dei FF (con i D coincidono con lo stato successivo, con i JK si usa la tabella di eccitazione) e si sintetizzano con le mappe.

**Scelta della codifica.** Codifiche diverse danno reti diverse, e non c'è una regola che garantisca la migliore. Alcuni criteri pratici: dare codici adiacenti (che differiscono per un bit) a stati collegati da una transizione; dare allo stato di reset il codice $00\dots0$, così il reset si fa con i $\overline{CL}$; scegliere i codici in modo che le uscite coincidano con qualche bit dello stato, così la rete delle uscite sparisce. All'estremo opposto c'è la codifica **one-hot**, con un FF per ogni stato e un solo FF a 1 alla volta: più FF, ma reti dello stato successivo molto semplici.

> [!esempio] Sequenza di luci
> **Specifica.** Tre luci $A$, $B$, $C$ (1 accesa, 0 spenta) si accendono in sequenza: nessuna, $A$, $A$ e $B$, tutte e tre, $B$ e $C$, solo $C$, poi si ricomincia. La macchina non ha ingressi.
>
> **ASM.** Sei stati in fila, senza rombi: a (nessuna uscita), b ($A$), c ($A$, $B$), d ($A$, $B$, $C$), e ($B$, $C$), f ($C$).
>
> **Registro di stato.** Sei stati richiedono 3 FF, con variabili $X$, $Y$, $Z$. Si usano i codici binari in ordine: a = 000, b = 001, c = 010, d = 011, e = 100, f = 101. I codici 110 e 111 non sono usati e nelle mappe sono indifferenze.
>
> **Uscite.** Mappe con righe $X$ e colonne $YZ$:
>
> | $X \backslash YZ$ | 00 | 01 | 11 | 10 |
> |---|---|---|---|---|
> | $A$: 0 | 0 | 1 | 1 | 1 |
> | $A$: 1 | 0 | 0 | – | – |
> | $B$: 0 | 0 | 0 | 1 | 1 |
> | $B$: 1 | 1 | 0 | – | – |
> | $C$: 0 | 0 | 0 | 1 | 0 |
> | $C$: 1 | 1 | 1 | – | – |
>
> Da cui $A = Y + \bar{X}Z$, $B = Y + X\bar{Z}$, $C = X + YZ$.
>
> **Stato successivo.**
>
> | Stato | $XYZ$ | $X^+ Y^+ Z^+$ |
> |---|---|---|
> | a | 000 | 001 |
> | b | 001 | 010 |
> | c | 010 | 011 |
> | d | 011 | 100 |
> | e | 100 | 101 |
> | f | 101 | 000 |
>
> Con i FF D gli ingressi sono le colonne dello stato successivo, e con le mappe (indifferenze in 110 e 111): $D_X = X\bar{Z} + YZ$, $D_Y = Y\bar{Z} + \bar{X}\bar{Y}Z$, $D_Z = \bar{Z}$.
>
> Con i FF JK si applica la tabella di eccitazione bit per bit. Per $X$: nelle righe con $X = 0$ serve $J_X = 1$ solo nella transizione $011 \to 100$, e nelle righe con $X = 1$ serve $K_X = 1$ solo in $101 \to 000$; le altre celle sono indifferenze. Si ottengono $J_X = YZ$, $K_X = Z$, $J_Y = \bar{X}Z$, $K_Y = Z$, $J_Z = K_Z = 1$: il FF di $Z$ commuta a ogni fronte. Con i JK la rete dello stato successivo è più semplice, come anticipato nel paragrafo 3.3.

## 4.4 Analisi di una MSF

L'analisi fa il percorso inverso: dal circuito alla descrizione del comportamento.

**Procedura di analisi.** (1) Si individuano i FF che formano il registro di stato, la rete dello stato successivo e la rete delle uscite. (2) Si scrivono le equazioni degli ingressi dei FF e delle uscite in funzione dello stato e degli ingressi. (3) Si ricava la tabella degli stati: per ogni stato presente e ogni combinazione degli ingressi, lo stato successivo (con i JK attraverso l'equazione caratteristica). (4) Si dà un nome a ogni stato e si disegna l'ASM. (5) Si controlla il risultato con un diagramma temporale.

> [!esempio] Dal circuito all'ASM
> Un circuito ha due FF D con uscite $X_1$, $X_0$, un ingresso $R$ e le reti
> $$D_0 = \bar{R}\,\bar{X}_0, \qquad D_1 = \bar{R}\,(X_0 \oplus X_1), \qquad U_0 = X_0, \quad U_1 = X_1, \quad TC = X_1 X_0.$$
> Con $R = 0$ lo stato successivo è $X_1^+ X_0^+ = (X_1 \oplus X_0,\ \bar{X}_0)$, cioè $00 \to 01 \to 10 \to 11 \to 00$: è il contatore modulo 4. Con $R = 1$ lo stato successivo è sempre $00$. Gli stati si chiamano a (00), b (01), c (10), d (11); nell'ASM ogni blocco di stato è seguito da un rombo su $R$, che con 0 porta allo stato successivo e con 1 riporta in a. È un contatore modulo 4 con **reset sincrono**: a differenza del $\overline{RES}$ sui $\overline{CL}$, il comando $R$ agisce solo al fronte.

## 4.5 Strutture base

Alcune macchine piccole ricorrono in quasi tutti gli esercizi, da sole o come parti di sistemi più grandi.

**Sincronizzatore.** Specifica: l'uscita $OUT$ vale 1 per il tempo in cui l'ingresso $IN$ vale 1, ma cambia solo sui fronti. Bastano due stati: a, con $OUT = 0$, in cui si resta finché $IN = 0$ e da cui si passa in b quando $IN = 1$; b, con $OUT$, in cui si resta finché $IN = 1$. È un solo FF D con $D = IN$. Un impulso di $IN$ che comincia e finisce fra due fronti non viene visto: gli ingressi devono variare con una frequenza molto più bassa di quella del clock.

**Rilevatore di fronti.** Specifica: $OUT$ vale 1 per un periodo di clock dopo ogni fronte di $IN$, sia di salita sia di discesa (figura 4.5). In una macchina di Moore servono quattro stati: a ($IN$ era 0), b ($IN$ è appena salito: $OUT$), c ($IN$ è 1 da più di un periodo), d ($IN$ è appena sceso: $OUT$). Da a si va in b quando $IN = 1$; da b e da c si va in c se $IN = 1$ e in d se $IN = 0$; da d si va in b se $IN = 1$ e in a se $IN = 0$. In una macchina di Mealy bastano due stati, che ricordano il valore precedente di $IN$: lo stato è un FF D con $D = IN$, e l'uscita condizionata è $OUT = IN \oplus X$, che vale 1 finché il nuovo valore di $IN$ è diverso da quello memorizzato.

![Figura 4.5](../figure/4-5.svg)

> [!nota]
> Negli appunti di L09 il rilevatore di fronti è chiamato "macchina a 2 stati", ma il diagramma della lezione ha quattro stati, a, b, c, d: è la versione di Moore descritta sopra. I due stati sono quelli della versione di Mealy, che si vede nell'esercizio 3 alla fine del modulo.

**Rilevatore di impulso lungo.** Specifica: $OUT = 1$ per un periodo se $IN$ resta a 1 per almeno due periodi. Stati: a (attesa, si resta finché $IN = 0$), b ($IN$ è 1 da un fronte: se torna a 0 si torna in a), c ($OUT$: $IN$ è 1 da due fronti), d (attesa che $IN$ torni a 0, senza uscita). Da c si va in d se $IN = 1$ e in a se $IN = 0$.

**Generatore di sequenze.** Specifica: alla transizione di $IN$ da 0 a 1 la macchina genera sulle uscite $A$, $B$ la sequenza $A = 1$, poi $B = 1$, poi $A = B = 1$, e torna in attesa. Stati: a (attesa, rombo su $IN$), b ($A$), c ($B$), d ($A$, $B$), e (attesa che $IN$ torni a 0, rombo su $IN$). Lo stato e serve a reagire alla *transizione* e non al livello: senza, se $IN$ restasse a 1 la sequenza ripartirebbe subito.

**Rilevatore di due ingressi.** Specifica: la macchina genera una sequenza quando entrambi gli ingressi $A$ e $B$ valgono 1. Nell'ASM si può scrivere un rombo per $A$ seguito da un rombo per $B$, oppure un solo rombo con la condizione $A \cdot B$: le due forme sono equivalenti.

## 4.6 Moore e Mealy a confronto

In una macchina di Moore le uscite cambiano solo dopo un fronte, perché dipendono solo dallo stato: sono sincrone e prive delle alee degli ingressi, ma arrivano un periodo dopo la condizione che le provoca. In una macchina di Mealy le uscite condizionate reagiscono subito al cambiamento degli ingressi, nello stesso periodo (si dice che l'uscita è **anticipata**), e spesso servono meno stati; in cambio le uscite seguono gli ingressi in modo asincrono, con le loro variazioni e le loro alee (figura 4.6).

![Figura 4.6](../figure/4-6.svg)

> [!esempio] Lo stesso problema in tre macchine
> **Specifica.** Ingressi $ENB$, $SEL$; uscite $GO$, $HLT$. La macchina attende $ENB = 1$; poi attiva $GO$ se $SEL = 1$ e $HLT$ se $SEL = 0$. Le uscite restano attive finché $ENB = 1$; quando $ENB$ torna a 0 la macchina torna in attesa.
>
> **M1, Moore, tre stati.** a (attesa) con un rombo su $ENB$ e uno su $SEL$; b ($HLT$) e c ($GO$), ciascuno con un rombo su $ENB$ che lo tiene fermo finché $ENB = 1$ e lo riporta in a quando torna a 0. Con a = 00, b = 01, c = 10: $HLT = Y$, $GO = X$ e, con l'indifferenza in 11,
> $$D_X = ENB\,(X + SEL\,\bar{Y}), \qquad D_Y = ENB\,(Y + \overline{SEL}\,\bar{X}).$$
>
> **M2 e M3, Mealy, due stati.** a (attesa) e b (attivo), con un solo FF: $D_X = ENB$. Nello stato b le uscite sono condizionate da $SEL$: $GO = SEL \cdot X$, $HLT = \overline{SEL} \cdot X$.
>
> Le macchine non sono equivalenti: in M1 il valore di $SEL$ si legge una volta, quando $ENB$ sale, e dopo non conta più; in M2 e M3 le uscite seguono $SEL$ per tutto il tempo in cui $ENB = 1$, quindi se $SEL$ cambia nel frattempo l'uscita attiva cambia. M2 e M3 sono due disegni dello stesso comportamento: $M1 \neq M2 \sim M3$. Quale sia giusta dipende da come si legge la specifica, ed è il tipo di ambiguità da chiarire al passo 0.

> [!esempio] Impulso sul fronte e segnalazione di attesa
> **Specifica.** Ingresso $IN$; uscite $OUT$ e $WT$. $OUT$ è un impulso di un periodo alla transizione di $IN$ da 0 a 1; $WT$ si attiva a 1 se $IN$ resta a 1 per più di un periodo, e resta attivo (la macchina si blocca) fino al reset.
>
> **ASM e codifica.** a = 00 (attesa: con $IN = 1$ va in b), b = 01 ($OUT$: con $IN = 0$ torna in a, con $IN = 1$ va in c), c = 10 ($WT$, resta in c). Il codice 11 non è usato.
>
> | Stato | $IN$ | $XY$ | $X^+ Y^+$ |
> |---|---|---|---|
> | a | 0 | 00 | 00 |
> | a | 1 | 00 | 01 |
> | b | 0 | 01 | 00 |
> | b | 1 | 01 | 10 |
> | c | – | 10 | 10 |
>
> Uscite: $OUT = Y$, $WT = X$. Con i FF D: $D_X = X + IN \cdot Y$, $D_Y = IN\,\bar{X}\,\bar{Y}$. Con i FF JK, dalla tabella di eccitazione: $J_X = IN \cdot Y$, $K_X = 0$, $J_Y = IN \cdot \bar{X}$, $K_Y = 1$.

> [!attenzione]
> Nella mappa di $J_X$ le colonne sono quelle di $Y$: l'1 condizionato ($J_X = IN$) è nella cella $XY = 01$, quindi $J_X = IN \cdot Y$. Con $J_X = IN \cdot \bar{X}$ la macchina passerebbe da a direttamente in c al primo fronte con $IN = 1$.

## 4.7 Stati non usati ed errori

Con $k$ FF e meno di $2^k$ stati restano dei codici non usati. Nella sintesi conviene trattarli come indifferenze, ma così lo stato successivo di un codice non usato è quello che la minimizzazione ha scelto per caso. In condizioni normali la macchina non ci arriva mai; ci può arrivare però per un disturbo, per esempio un **bit flip** di un FF dovuto a un impulso elettrico o a una radiazione, o all'accensione se il reset manca. Il pericolo è che i codici non usati formino un ciclo da cui la macchina non esce più.

Per la sequenza di luci del paragrafo 4.3 il controllo si fa sulle equazioni: da 110 si va in 111, e da 111 in 100, che è lo stato e. La macchina rientra da sola nella sequenza dopo due fronti.

Quando non basta, il progetto si rende più sicuro definendo anche le transizioni dei codici non usati. Per una macchina a tre stati a (000), b (001), c (010) con 3 FF, i cinque codici liberi possono diventare stati di errore ERR, ciascuno con un anello su se stesso e un'uscita di allarme, oppure portare direttamente allo stato di reset. Si rinuncia a qualche indifferenza, e la rete viene un po' più grande.

## 4.8 Progetti completi

> [!esempio] Controllo di una lavatrice
> **Specifica.** Ingressi $START$ (inizio del lavaggio sulla transizione da 0 a 1) e $L$ (0 lavaggio normale, 1 lavaggio lungo); uscite $LAV$ (lavaggio), $RIS$ (risciacquo), $CEN$ (centrifuga). Ogni fase dura un periodo di clock, e il lavaggio lungo ha due periodi di $LAV$ invece di uno.
>
> **ASM.** Una prima versione ha due rami separati dopo il rombo su $L$: $LAV, RIS, CEN$ per il normale e $LAV, LAV, RIS, CEN$ per il lungo. Si ottimizza osservando che i rami finiscono allo stesso modo: il ramo lungo fa un periodo di $LAV$ in più e poi si unisce al normale. Stati: wait (000, rombo su $START$ e poi su $L$), LL (001, $LAV$, solo per il lavaggio lungo), L1 (010, $LAV$), L2 (011, $RIS$), L3 (100, $CEN$), stop (101). Da wait si va in LL se $START \cdot L$, in L1 se $START \cdot \bar{L}$; poi LL → L1 → L2 → L3 → stop.
>
> **Uscite**, con le indifferenze in 110 e 111: $LAV = Y\bar{Z} + \bar{X}\bar{Y}Z$, $RIS = YZ$, $CEN = X\bar{Z}$.
>
> **Sintesi con i FF JK.** Dalla tabella di eccitazione, bit per bit:
> $$J_X = YZ, \quad K_X = 0; \qquad J_Y = \bar{X}Z + \bar{X}\,\bar{Z}\cdot START\,\bar{L}, \quad K_Y = Z; \qquad J_Z = X + Y + START \cdot L, \quad K_Z = \bar{X}.$$
> $J_Y$ si può scrivere anche $\bar{X}(Z + START\,\bar{L})$. Lo stato stop resta fermo: $K_Z = \bar{X}$ vale 0 per $X = 1$, e $J_X$, $J_Y$ valgono 0.

> [!attenzione]
> Nella mappa di $J_Z$ le celle con $X = 1$ o $Y = 1$ sono 1 o indifferenze, e resta il termine $START \cdot L$ della cella di wait: $J_Z = X + Y + START \cdot L$. Scrivere $J_Z = 1 + START \cdot L$ vorrebbe dire $J_Z = 1$, e la macchina lascerebbe lo stato wait anche senza $START$.

> [!nota]
> Lo stato stop ha solo un anello su se stesso: finito il ciclo, la lavatrice resta ferma fino al reset, come nella specifica della lezione. Se si volesse ripartire con un nuovo $START$, basterebbe aggiungere in stop un rombo su $START$ che riporta in wait quando $START = 0$, così che il ciclo successivo parta solo con una nuova transizione da 0 a 1.

> [!esempio] Trasmettitore seriale
> **Specifica.** Ingressi $GO$, $D_0$, $D_1$; uscita $LN$ (la linea). Alla transizione di $GO$ da 0 a 1 la macchina trasmette su $LN$ il pacchetto $1, D_0, D_1, 0$, un bit per periodo: un bit di start a 1, i due bit di dato, un bit di stop a 0.
>
> **Se $D_0$ e $D_1$ non cambiano durante la trasmissione**, la macchina li legge mentre li trasmette. Con Moore servono sette stati: init (attesa, rombo su $GO$), s (start: $LN$), due stati per il bit $D_0$ (uno con $LN$ e uno senza, scelti da un rombo su $D_0$), due per $D_1$, e lo stato di stop, in cui si attende che $GO$ torni a 0 prima di rientrare in init. Con Mealy bastano cinque stati, perché i bit di dato diventano uscite condizionate: in b0 l'ovale $LN$ dopo il rombo su $D_0$, in b1 l'ovale $LN$ dopo il rombo su $D_1$.
>
> **Se $D_0$ e $D_1$ possono cambiare** dopo la transizione di $GO$, vanno letti tutti e due nell'istante in cui $GO$ sale. Nell'ASM, dopo il rombo su $GO$ ci sono i rombi su $D_0$ e su $D_1$, che separano quattro rami (00, 01, 10, 11), ciascuno con la sua sequenza fissa di stati con e senza $LN$. Il numero di stati cresce con il numero di bit; con pacchetti più lunghi conviene memorizzare i dati in un registro, ed è l'idea del paragrafo 4.9.

## 4.9 Controllore e datapath

Un sistema digitale appena più grande degli esempi precedenti si divide in due parti. Il **datapath** contiene i blocchi che elaborano e memorizzano i dati: registri, contatori, sommatori, MUX. Il **controllore** è una MSF che non tocca i dati ma comanda il datapath con i **segnali di controllo** (carica, azzera, abilita, scegli) e decide che cosa fare in base ai **segnali di stato** che il datapath gli restituisce (il terminal count di un contatore, l'esito di un confronto). Così la MSF resta piccola anche quando i dati sono molti bit: il numero di stati dipende dai passi dell'algoritmo, non dai valori dei dati.

**Esempio: misura della durata di un impulso.** Specifica: l'ingresso $IN$ vale di solito 0 e ogni tanto fa un impulso lungo da 1 a 7 periodi di clock. Il sistema misura la durata di ogni impulso e la trasmette sulla linea seriale $SER$ con il pacchetto: bit di start 1, $Q_0$, $Q_1$, $Q_2$, bit di stop 0. Il datapath ha un contatore $CNT$ a 3 bit con abilitazione $EN$ e azzeramento sincrono $CL$, e un MUX che porta su $SER$ la costante 1, uno dei bit $Q_i$ o la costante 0. Il controllo è diviso in due macchine (figura 4.7).

- **FSM-A** misura. Nello stato A0 attiva $BSY$ (il sistema è alla ricerca di un impulso) e, finché $IN = 0$, l'uscita condizionata $CL$ tiene il contatore a zero; quando $IN = 1$ attiva l'uscita condizionata $EN$, così il primo periodo dell'impulso è già contato, e passa in A1. In A1, finché $IN = 1$, attiva $EN$; quando $IN$ torna a 0 passa in A2, che attiva $TRG$ per un periodo: in $Q_2 Q_1 Q_0$ c'è la durata. In A3 aspetta $ETX$ e poi torna in A0.
- **FSM-B** trasmette. Nello stato B0 aspetta $TRG$; poi cinque stati B1…B5 scelgono sul MUX, nell'ordine, 1, $Q_0$, $Q_1$, $Q_2$, 0. In B5 attiva anche $ETX$, per dire a FSM-A che il dato è stato inviato, e torna in B0.

Il contatore non cambia durante la trasmissione, perché FSM-A in A3 non attiva né $EN$ né $CL$: è il motivo dello scambio $TRG$/$ETX$ fra le due macchine.

![Figura 4.7](../figure/4-7.svg)

## 4.10 Simulazione

Prima di costruire un circuito lo si verifica con un **simulatore**, un programma che calcola le uscite di uno schema o di un ASM per una sequenza di ingressi assegnata. Il procedimento è: (1) disegnare il circuito o l'ASM; (2) preparare gli stimoli, cioè il clock, il reset all'inizio e gli ingressi, facendoli cambiare lontano dai fronti; (3) scrivere a mano, prima di simulare, il diagramma temporale atteso; (4) confrontare il risultato della simulazione con quello atteso e spiegare ogni differenza. Conviene provare anche i casi limite: un impulso più breve di un periodo, due ingressi che cambiano insieme, il comportamento dopo il reset e dai codici non usati (che si possono forzare con i preset). Gli esercizi del corso con il simulatore chiedono proprio di completare a mano le sequenze temporali, come nell'esempio del registro con retroazione del paragrafo 3.7.

## Esempi ed esercizi svolti

**Esercizio 1.** Verificare le equazioni di M1 (paragrafo 4.6). Dallo stato a (00): con $ENB = 1$ e $SEL = 1$, $D_X = 1 \cdot (0 + 1 \cdot 1) = 1$ e $D_Y = 1 \cdot (0 + 0) = 0$, quindi si va in c (10, $GO$); con $SEL = 0$, $D_X = 0$ e $D_Y = 1 \cdot (0 + 1 \cdot 1) = 1$, quindi si va in b (01, $HLT$). Da b con $ENB = 1$: $D_X = 1 \cdot (0 + SEL \cdot 0) = 0$, $D_Y = 1 \cdot (1 + \dots) = 1$, si resta in b qualunque sia $SEL$. Con $ENB = 0$ entrambe le equazioni danno 0 e si torna in a.

**Esercizio 2.** Che cosa fa la macchina delle luci se all'accensione si trova nello stato 110? Dalle equazioni dei FF D: $X^+ = X\bar{Z} + YZ = 1$, $Y^+ = Y\bar{Z} + \bar{X}\bar{Y}Z = 1$, $Z^+ = \bar{Z} = 1$, quindi va in 111; da 111, $X^+ = 1$, $Y^+ = 0$, $Z^+ = 0$, quindi va in 100 (stato e) e da lì prosegue normalmente. Per le uscite, in 110 si ha $A = B = 1$, $C = 1$, e in 111 lo stesso: per due periodi le luci sono tutte accese.

**Esercizio 3.** Progettare il rilevatore di fronti di Mealy. Un FF D memorizza il valore precedente dell'ingresso: $D = IN$, stato $X$. L'uscita è $OUT = IN \oplus X$: subito dopo un fronte di $IN$ e fino al fronte successivo del clock, $IN$ e $X$ sono diversi e $OUT = 1$; al fronte del clock $X$ si aggiorna e $OUT$ torna a 0. L'impulso di uscita comincia con il fronte di $IN$ e non con il clock, quindi dura meno di un periodo: è la differenza con la versione di Moore.

### Esercizi del laboratorio con il simulatore

In laboratorio l'analisi delle reti sequenziali si fa prima a mano, su carta, per due sequenze d'ingresso, e poi si controlla con la simulazione. Le reti che seguono hanno la stessa struttura di quelle dell'esercitazione: si scrivono le equazioni, si calcola lo stato fronte per fronte e si riconosce che cosa fa la macchina.

**Esercizio 4. Analisi: due FF JK e un ingresso.** Due FF JK con uscite $Q_1$, $Q_0$ e reset iniziale a $00$ hanno $J_0 = K_0 = X$ e $J_1 = K_1 = X\,Q_0$; l'uscita è $Z = X\,Q_1 Q_0$. Calcolare gli stati per $X = 1, 1, 0, 1, 1, 1$ (valori appena prima dei fronti) e dire che cosa fa la rete.

Con $J = K$ ogni FF è un T: $Q_0$ commuta quando $X = 1$, $Q_1$ commuta quando $X = 1$ e $Q_0 = 1$.

| Fronte | $X$ | $Q_1 Q_0$ prima | $T_1 = X Q_0$ | $T_0 = X$ | $Q_1 Q_0$ dopo |
|---|---|---|---|---|---|
| 1 | 1 | 00 | 0 | 1 | 01 |
| 2 | 1 | 01 | 1 | 1 | 10 |
| 3 | 0 | 10 | 0 | 0 | 10 |
| 4 | 1 | 10 | 0 | 1 | 11 |
| 5 | 1 | 11 | 1 | 1 | 00 |
| 6 | 1 | 00 | 0 | 1 | 01 |

È un contatore modulo 4 con abilitazione $X$: conta quando $X = 1$ e si ferma quando $X = 0$ (fronte 3). $Z$ vale 1 nel periodo prima del fronte 5, quando lo stato è $11$ e $X = 1$: è il terminal count abilitato del paragrafo 3.6, ed è un'uscita di Mealy perché dipende da $X$.

**Esercizio 5. Analisi: riconoscere la funzione.** Due FF D con uscite $Q_1$, $Q_0$ e reset a $00$ hanno $D_0 = X$ e $D_1 = X\,Q_0$; l'uscita è $Z = Q_1$. (a) Disegnare l'ASM. (b) Calcolare gli stati per la sequenza A: $X = 1, 1, 1, 0, 1, 0, 1, 1$. (c) Dire che cosa fa la macchina.

(a) Dalla tabella degli stati: da $00$ con $X = 1$ si va in $01$, con $X = 0$ si resta in $00$; da $01$ con $X = 1$ si va in $11$, con $X = 0$ in $00$; da $11$ con $X = 1$ si resta in $11$, con $X = 0$ si va in $00$. Il codice $10$ non si raggiunge dal reset (e da $10$ si andrebbe in $00$ o $01$). Gli stati sono a = 00, b = 01, c = 11, con $Z$ solo in c; dopo ogni blocco di stato c'è un rombo su $X$.

(b)

| Fronte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $X$ | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |
| $Q_1 Q_0$ dopo | 01 | 11 | 11 | 00 | 01 | 00 | 01 | 11 |
| $Z$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |

(c) $Q_0$ è $X$ ritardato di un periodo e $Q_1$ è il prodotto dei due ultimi campioni di $X$: $Z = 1$ quando gli ultimi due campioni di $X$ valevano 1. È un **rilevatore della sequenza 11**, con sovrapposizione (dopo tre 1 di fila $Z$ resta a 1). Il riconoscimento delle sequenze è un tipo di esercizio che si ritrova nella guida 1 qui sotto.

**Esercizio 6. Analisi: un contatore che cambia verso.** Due FF T con uscite $Q_1$, $Q_0$ e reset a $00$ hanno $T_0 = 1$ e $T_1 = Q_0 \oplus DN$. Calcolare gli stati con $DN = 0$ per quattro fronti e poi $DN = 1$ per quattro fronti.

Con $DN = 0$, $T_1 = Q_0$: è il contatore in avanti, $00 \to 01 \to 10 \to 11 \to 00$. Con $DN = 1$, $T_1 = \bar{Q}_0$: $Q_1$ commuta quando $Q_0 = 0$, e partendo da $00$ si ha $00 \to 11 \to 10 \to 01 \to 00$, cioè $0, 3, 2, 1, 0$: il conteggio all'indietro. È il contatore avanti e indietro del paragrafo 4.2, fatto con due FF T e una XOR. La XOR fa da "invertitore comandato": con $DN = 1$ nega $Q_0$, e il bit alto cambia quando quello basso passa da 0 a 1 all'indietro, cioè quando vale 0 prima del fronte.

**Esercizio 7. Un ricevitore seriale.** La linea $LN$ è a 0 quando è a riposo. Un pacchetto è formato da cinque bit, uno per periodo di clock: due bit di start a 1, un bit di dato $B$, due bit di stop a 0, cioè $1\,1\,B\,0\,0$. Il ricevitore deve attivare $VAL$ per un periodo alla fine di un pacchetto corretto, con $DAT = B$ nello stesso periodo, e attivare $ERR$ se un pacchetto cominciato non finisce con i due 0. Un 1 isolato sulla linea, seguito da 0, è un disturbo e si ignora. Progettare l'ASM di Moore e dire quanti FF servono.

*Gli stati ricordano quanto del pacchetto è arrivato.*

| Stato | Che cosa si è ricevuto | Uscite | $LN = 0$ | $LN = 1$ |
|---|---|---|---|---|
| I | riposo | – | I | S1 |
| S1 | primo 1 | – | I (disturbo) | S2 |
| S2 | $1\,1$ | – | B0 | B1 |
| B0 | $1\,1\,0$ | – | P0 | E |
| B1 | $1\,1\,1$ | – | P1 | E |
| P0 | $1\,1\,0\,0$ | – | V0 | E |
| P1 | $1\,1\,1\,0$ | – | V1 | E |
| V0 | pacchetto con $B = 0$ | $VAL$ | I | S1 |
| V1 | pacchetto con $B = 1$ | $VAL$, $DAT$ | I | S1 |
| E | stop sbagliato | $ERR$ | I | E |

Il bit di dato non si può "ricordare" in un FF a parte senza un datapath, quindi la macchina lo ricorda nello stato: i rami B0-P0-V0 e B1-P1-V1 sono uguali, ma uno sa che $B = 0$ e l'altro che $B = 1$. Dagli stati V0 e V1 si può ripartire subito con un nuovo pacchetto, perché un 1 sulla linea è il primo bit di start. Dallo stato E si esce quando la linea torna a 0. Gli stati sono dieci, quindi servono $\lceil \log_2 10 \rceil = 4$ FF (o 10 con la codifica one-hot).

*Perché non basta un registro a scorrimento.* Viene l'idea di far scorrere la linea in un registro a 5 bit e di riconoscere con una AND la configurazione $1\,1\,B\,0\,0$. Ma con $B = 1$, un periodo dopo un pacchetto corretto il registro contiene $1\,1\,0\,0\,0$, cioè gli ultimi quattro bit del pacchetto seguiti dallo 0 di riposo, che sembra un secondo pacchetto con $B = 0$. La macchina a stati non sbaglia perché sa dove comincia il pacchetto: parte sempre dallo stato di riposo. È lo stesso motivo per cui nel paragrafo 4.5 il generatore di sequenze ha bisogno dello stato di attesa.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Rilevatore della sequenza 101 (Moore).** L'ingresso $X$ è sincronizzato con il clock. L'uscita $Z$ deve valere 1 per un periodo dopo che gli ultimi tre campioni di $X$ sono stati $1, 0, 1$. Le sequenze possono sovrapporsi: in $1\,0\,1\,0\,1$ la sequenza compare due volte.

*Passo 1: che cosa deve ricordare la macchina.* Il pezzo più lungo della sequenza già ricevuto: niente (a), "1" (b), "10" (c), "101" (d, con $Z$).

*Passo 2: le transizioni.* Da a: con 1 si va in b, con 0 si resta. Da b: con 1 si resta in b (l'ultimo 1 può essere l'inizio), con 0 si va in c. Da c: con 1 si va in d, con 0 si torna in a (l'ultimo pezzo "100" non è l'inizio di niente). Da d: con 1 si va in b, con 0 si va in c, perché l'ultimo 1 di "101" seguito da 0 dà già "10". Questa è la sovrapposizione.

*Passo 3: codifica e tabella.* a = 00, b = 01, c = 10, d = 11, così $Z = Q_1 Q_0$.

| $Q_1 Q_0$ | $X$ | $Q_1^+ Q_0^+$ |
|---|---|---|
| 00 | 0 | 00 |
| 00 | 1 | 01 |
| 01 | 0 | 10 |
| 01 | 1 | 01 |
| 10 | 0 | 00 |
| 10 | 1 | 11 |
| 11 | 0 | 10 |
| 11 | 1 | 01 |

*Passo 4: la sintesi con i FF D.* La colonna $Q_0^+$ vale 1 esattamente quando $X = 1$: $D_0 = X$. La colonna $Q_1^+$ vale 1 per $(01, 0)$, $(11, 0)$ e $(10, 1)$; le prime due formano il gruppo $Q_0\bar{X}$, la terza è isolata:
$$D_1 = Q_0\bar{X} + Q_1\bar{Q}_0 X, \qquad D_0 = X, \qquad Z = Q_1 Q_0.$$

*Passo 5: controllo con una sequenza.* Per $X = 1, 0, 1, 0, 1, 1$: stati $01, 10, 11, 10, 11, 01$, e $Z = 1$ dopo il terzo e il quinto fronte, cioè proprio dopo ognuno dei due "101".

**Guidato 2. Lo stesso rilevatore in versione Mealy.** Rifare il guidato 1 con un'uscita di Mealy.

*Passo 1.* Con Mealy l'uscita può dipendere dall'ingresso presente: quando la macchina ha già ricevuto "10" e arriva un 1, l'uscita si attiva subito, nello stesso periodo. Lo stato d non serve più: bastano a (niente), b ("1"), c ("10").

*Passo 2: transizioni e uscita.* Da a: 1 → b, 0 → a. Da b: 1 → b, 0 → c. Da c: 1 → b con l'uscita condizionata $Z$, 0 → a.

*Passo 3: codifica e sintesi.* a = 00, b = 01, c = 10, codice 11 indifferente. Si va in b con ogni 1, quindi $D_0 = X$; si va in c solo da b con $X = 0$, e con l'indifferenza $D_1 = Q_0\bar{X}$. L'uscita è $Z = Q_1 X$.

*Passo 4: confronto.* La versione di Mealy ha uno stato in meno (tre invece di quattro, anche se i FF restano due) e reti più semplici; l'uscita arriva un periodo prima, ma segue $X$ in modo asincrono e ne ricopia le eventuali variazioni durante il periodo, come spiegato nel paragrafo 4.6.

## Riepilogo

Ogni rete sequenziale sincrona è una macchina a stati finiti, con un registro di stato, una rete dello stato successivo e una rete delle uscite; nella macchina di Moore le uscite dipendono solo dallo stato, in quella di Mealy anche dagli ingressi. Il diagramma ASM la descrive con blocchi di stato, blocchi decisionali e uscite condizionate, e ogni periodo di clock percorre un blocco ASM. Il progetto va dalla specifica all'ASM, dalla scelta e codifica degli stati alla tabella degli stati e alla sintesi degli ingressi dei FF, D o JK; l'analisi fa il percorso inverso. Sincronizzatore, rilevatore di fronti, rilevatore di impulso lungo e generatore di sequenze sono le strutture che ricorrono; Moore e Mealy risolvono gli stessi problemi con tempi e numeri di stati diversi, e una specifica ambigua può dare macchine non equivalenti. I codici non usati vanno controllati perché la macchina non vi resti intrappolata. Nei sistemi più grandi una MSF fa da controllore di un datapath fatto di registri e contatori, e ogni progetto si verifica con il simulatore confrontando il diagramma temporale ottenuto con quello atteso.

## Formulario

Struttura, procedure e termini delle macchine a stati finiti, con il paragrafo in cui sono spiegati.

### Struttura

| Che cosa | Formula o regola | Par. |
|---|---|---|
| Parti di una MSF | registro di stato, rete dello stato successivo, rete delle uscite | 4.1 |
| Stato successivo | $X^+ = f(X, I)$, caricato al fronte | 4.1 |
| Uscite di Moore | $U = g(X)$: cambiano solo dopo un fronte | 4.1 |
| Uscite di Mealy | $U = g(X, I)$: reagiscono subito agli ingressi | 4.1 |
| Numero di FF | almeno $\lceil \log_2(\text{stati}) \rceil$; one-hot: uno per stato | 4.3 |
| Ingressi dei FF D | coincidono con lo stato successivo | 4.3 |
| Ingressi dei FF JK | dalla tabella di eccitazione, con molte indifferenze | 3.3, 4.3 |

### Il diagramma ASM

- Blocco di stato (rettangolo): nome, codice, uscite di Moore attive.
- Blocco decisionale (rombo): condizione sugli ingressi, uscite 1 e 0, nello stesso periodo.
- Uscita condizionata (ovale): uscita di Mealy, attiva nello stato se la condizione è vera.
- Un blocco ASM (stato con i suoi rombi e ovali) corrisponde a un periodo di clock.

### Procedure

*Progetto.* (0) Specifica e diagramma temporale di esempio; (1) ASM; (2) numero di FF e codifica; (3) tabella delle uscite e tabella degli stati; (4) ingressi dei FF e sintesi con le mappe; (5) controllo dei codici non usati; (6) verifica con un diagramma temporale o con il simulatore.

*Analisi.* (1) Si riconoscono registro di stato e reti; (2) equazioni dei FF e delle uscite; (3) tabella degli stati (con i JK tramite $Q^+ = J\bar{Q} + \bar{K}Q$); (4) nomi degli stati e ASM; (5) diagramma temporale.

*Criteri di codifica.* Codici adiacenti a stati collegati; $00\dots0$ allo stato di reset; uscite uguali a bit dello stato quando possibile.

### Strutture ricorrenti

| Struttura | Stati | Idea |
|---|---|---|
| Sincronizzatore | 2 | un FF D con $D = IN$ |
| Rilevatore di fronti | 4 (Moore), 2 (Mealy) | Mealy: $OUT = IN \oplus X$ con $D = IN$ |
| Rilevatore di impulso lungo | 4 | conta i periodi in cui $IN$ resta a 1 |
| Generatore di sequenze | uno per passo più l'attesa | lo stato di attesa fa reagire alla transizione, non al livello |
| Riconoscitore di sequenza | uno per prefisso ricevuto | la sovrapposizione decide dove si torna |
| Controllore e datapath | dipende dall'algoritmo | la MSF comanda registri e contatori e legge i loro segnali di stato |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Macchina a stati finiti | rete sequenziale sincrona con un numero finito di stati |
| Macchina di Moore / di Mealy | uscite funzione del solo stato / dello stato e degli ingressi |
| Uscita anticipata | uscita di Mealy, attiva già nel periodo in cui cambia l'ingresso |
| Ingresso sincronizzato | ingresso che cambia lontano dai fronti, di solito tramite un FF |
| Tabella degli stati | stato presente e ingressi → stato successivo |
| Codifica one-hot | un FF per stato, uno solo a 1 alla volta |
| Codici non usati | combinazioni dei FF che non corrispondono a stati; vanno controllate |
| Bit flip | cambio spontaneo di un FF per un disturbo |
| Reset sincrono / asincrono | agisce al fronte / subito, tramite il clear |
| Datapath | parte che elabora e memorizza i dati |
| Controllore | MSF che comanda il datapath con i segnali di controllo |
| Segnali di stato | segnali che il datapath restituisce al controllore |
| Simulazione | calcolo delle uscite di uno schema per una sequenza di stimoli |

### Domande che tornano spesso

- Disegnare la struttura di una MSF e spiegare la differenza fra Moore e Mealy, con un diagramma temporale.
- Quali sono gli elementi del diagramma ASM? Che cosa succede in un periodo di clock?
- Quanti FF servono per $n$ stati? Che vantaggi ha la codifica one-hot?
- Progettare il rilevatore di fronti nelle due versioni.
- Perché una specifica può dare macchine non equivalenti? Esempio delle macchine M1 e M2.
- Che cosa sono i codici non usati, e come si rende sicura una macchina?
- A che cosa serve la divisione fra controllore e datapath?
