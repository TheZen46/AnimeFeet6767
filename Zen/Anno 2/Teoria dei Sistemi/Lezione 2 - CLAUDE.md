---

## corso: Teoria dei Sistemi lezione: 2 data: 2026-09-24 argomenti: [proprietà del campionamento, derivata del prodotto, prodotto con impulsi di ordine superiore, salti e impulsi, finestra rettangolare, funzioni a tratti, trasformata di Laplace, ascissa di convergenza, proprietà della trasformata, trasformate notevoli] fonti: [trascrizione parte 1, appunti manuali, dispensa del docente] tags: [teoria-dei-sistemi, lezione]

---
# Lezione 2 — Funzioni generalizzate (seconda parte) e trasformata di Laplace

Questa nota ricostruisce la seconda lezione a partire dalla trascrizione della registrazione (parte 1), dagli appunti personali (note Obsidian e appunti a mano) e dalla dispensa del docente («Appunti di Teoria dei sistemi», cap. 1, pp. 10–15). La lezione completa lo studio delle funzioni generalizzate con le regole di derivazione e l'uso del gradino per descrivere funzioni definite a tratti, poi introduce la **trasformata di Laplace**, con le sue proprietà e le trasformate delle funzioni elementari.

## 1. Riepilogo della lezione precedente

Il docente riprende brevemente quanto visto in [[Lezione 01 - Sistemi dinamici e funzioni generalizzate]]. L'impulso di ordine zero $\delta(t)$ gode della proprietà del campionamento, anche nella forma estesa: per una funzione regolare $f$ vale $f(t),\delta(t-T) = f(T),\delta(t-T)$. Derivando l'impulso si ottengono gli impulsi di ordine positivo $\delta_k$, $k>0$, oggetti concentrati in un punto e impossibili da disegnare in modo significativo («frecce che salgono e scendono»). Integrando si scende di ordine: $\int_{0^-}^{t}\delta_k(\tau),d\tau = \delta_{k-1}(t)$. Gli impulsi di ordine negativo sono tutti nulli fino all'origine e poi diventano costanti, rette, parabole e così via: ogni integrazione aumenta di uno il grado del polinomio.

## 2. Regole di derivazione con le funzioni generalizzate

### 2.1 La derivata del prodotto

Il primo risultato della lezione è un principio che, dice il docente, va **ammesso più che dimostrato**: alle funzioni generalizzate si possono applicare le stesse regole di derivazione imparate in analisi.

> [!important] Derivata del prodotto 
> Se $f$ e $g$ sono due funzioni di cui **almeno una è derivabile nel senso ordinario**, vale $$\frac{d}{dt}\big(f,g\big) = \dot f,g + f,\dot g,$$ anche quando l'altra è una funzione generalizzata, e quindi di per sé non derivabile nel senso ordinario (un gradino, un impulso, ...).

La condizione è essenziale. Non si considerano prodotti di due funzioni generalizzate tra loro, come $1(t)\cdot1(t)$ o $\delta(t)\cdot\delta(t)$: le formule riguardano sempre una funzione ordinaria (pensiamola derivabile ovunque, ad esempio di classe $C^\infty$) moltiplicata per un oggetto generalizzato.

### 2.2 Il prodotto di una funzione per $\dot\delta$

Viene spontaneo pensare che, poiché tutti gli impulsi di ordine $\ge 0$ sono concentrati nell'origine, il prodotto di una funzione per uno qualsiasi di essi si limiti a campionare la funzione in quel punto. **Non è così**: il campionamento «semplice» vale solo per l'impulso di ordine zero. Per vedere che cosa succede con il doppietto basta derivare in due modi la stessa quantità $f(t),\delta(t)$.

Da un lato, con la regola del prodotto e poi il campionamento sul primo addendo:

$$\frac{d}{dt}\big[f(t),\delta(t)\big] = \dot f(t),\delta(t) + f(t),\dot\delta(t) = \dot f(0),\delta(t) + f(t),\dot\delta(t).$$

Dall'altro lato, per il campionamento $f(t),\delta(t) = f(0),\delta(t)$, dove $f(0)$ è un **numero**; quindi

$$\frac{d}{dt}\big[f(0),\delta(t)\big] = f(0),\dot\delta(t).$$

Le due espressioni derivano la stessa cosa e devono coincidere. Uguagliandole si ricava:

> [!important] Prodotto per il doppietto $$f(t),\dot\delta(t) = f(0),\dot\delta(t) - \dot f(0),\delta(t)$$ Il prodotto per $\dot\delta$ campiona **sia la funzione sia la sua derivata**. In particolare $f(t),\dot\delta(t) \neq f(0),\dot\delta(t)$.

Il meccanismo si estende agli ordini superiori. Moltiplicando per $\ddot\delta$ vengono campionate la funzione, la derivata prima e la derivata seconda. Moltiplicando per un impulso di ordine $37$, osserva il docente, si ottiene un'espressione «lunga un chilometro», in cui compaiono tutte le derivate della funzione fino alla trentasettesima, ciascuna moltiplicata per un impulso di ordine opportuno. Solo per l'impulso di ordine zero viene campionata la sola funzione.

> [!tip] Approfondimento: la formula generale #approfondimento 
> Iterando lo stesso procedimento (risultato non presentato a lezione, che si dimostra per induzione) si ottiene, per una funzione $f$ sufficientemente regolare, $$f(t),\delta_n(t) = \sum_{k=0}^{n} (-1)^k \binom{n}{k}, f^{(k)}(0);\delta_{n-k}(t).$$ Per $n=1$ si ritrova la formula precedente. Per $n=2$ si deriva $f(t)\dot\delta(t) = f(0)\dot\delta(t) - \dot f(0)\delta(t)$: il primo membro dà $\dot f,\dot\delta + f,\ddot\delta$, il secondo $f(0),\ddot\delta - \dot f(0),\dot\delta$. Applicando la formula per $n=1$ alla funzione $\dot f$, cioè $\dot f(t)\dot\delta(t) = \dot f(0)\dot\delta(t) - \ddot f(0)\delta(t)$, si ottiene $$f(t),\ddot\delta(t) = f(0),\ddot\delta(t) - 2\dot f(0),\dot\delta(t) + \ddot f(0),\delta(t).$$ I coefficienti sono quelli binomiali con segni alterni, come nella regola di Leibniz per la derivata $n$-esima di un prodotto.

> [!warning] Discrepanza negli appunti (nota «Funzioni generalizzate») Nella nota compare $$\tfrac{d}{dt}\big[f(t)\delta(t)\big] = \dot f(t)\delta(t) + f(t)\dot\delta(t) = f(0),\delta(t),$$ che non è corretta: la derivata di $f(0),\delta(t)$ è $f(0),\dot\delta(t)$, non $f(0),\delta(t)$. Gli appunti a mano riportano correttamente il risultato $f(t)\dot\delta(t) = f(0)\dot\delta(t) - \dot f(0)\delta(t)$, che coincide con la dispensa (p. 11).

### 2.3 Salti di una funzione e impulsi nella derivata

Si consideri ora il prodotto $f(t)\cdot1(t)$, con $f$ funzione ordinaria qualsiasi. Fino all'origine il prodotto è nullo, perché il gradino è nullo; dopo l'origine coincide con $f$. In $t=0$ la funzione compie quindi un **salto** da $0$ a $f(0^+)$. Che cosa diventa questo salto nella derivata?

La derivata misura come varia una funzione: integrandola su un intervallo si ottiene la variazione della funzione agli estremi. Scegliamo $t_1<0<t_2$:

$$\int_{t_1}^{t_2}\dot f(t),dt = f(t_2) - f(t_1).$$

Facciamo ora tendere $t_1$ a zero da sinistra e $t_2$ a zero da destra. L'intervallo di integrazione si riduce fino a «$[0^-, 0^+]$», ma il secondo membro non tende a zero: tende al salto $f(0^+) - 0 = f(0^+)$, un numero finito. Perché l'integrale di qualcosa su un intervallo infinitamente piccolo resti un numero diverso da zero, quel qualcosa deve essere infinitamente grande in quell'intervallo («base microscopica, altezza gigantesca»), altrimenti l'area sarebbe nulla. L'unico oggetto che dà un'area finita su un intervallo nullo è, per definizione, l'impulso. Nel punto del salto la derivata deve dunque contenere un impulso, di area pari all'ampiezza del salto.

> [!important] Salti e impulsi Se una funzione presenta in $t_0$ un salto di ampiezza $\Delta = f(t_0^+) - f(t_0^-)$, la sua derivata contiene il termine $$\Delta\cdot\delta(t - t_0),$$ cioè un impulso centrato nel punto del salto, rivolto verso l'alto se il salto è positivo e verso il basso se è negativo.

La regola del prodotto conferma il ragionamento grafico. Derivando $f(t)\cdot1(t)$ e usando il campionamento:

$$\frac{d}{dt}\big[f(t),1(t)\big] = \dot f(t),1(t) + f(t),\delta(t) = \dot f(t),1(t) + f(0),\delta(t).$$

La parte ordinaria della derivata è $\dot f$ «accesa» dall'origine in poi. In più compare un impulso di area $f(0)$, esattamente l'ampiezza del salto. Gli appunti a mano riassumono il ragionamento con la scrittura $\int_{t_1}^{t_2} f(0^+),\delta(t),dt = f(t_2) - f(t_1)$ nel limite $t_1\to0^-$, $t_2\to0^+$.

Lo stesso ragionamento si applica a tutti i livelli di derivazione:

- una discontinuità **a gradino** della funzione produce un impulso nella derivata prima;
- una discontinuità **a rampa**, cioè una funzione continua la cui derivata passa bruscamente da un valore a un altro (un punto angoloso), produce un gradino nella derivata prima e quindi un impulso nella derivata seconda;
- una funzione di classe $C^\infty$ non ha nessuna di queste discontinuità, quindi nessuna sua derivata contiene gradini o impulsi.

In generale, se la derivata $n$-esima di una funzione ha un salto, la derivata $(n+1)$-esima contiene un impulso. Una funzione derivabile con continuità fino all'ordine $25$, la cui derivata $26$-esima ha valori diversi a destra e a sinistra di un punto, ha in quel punto una discontinuità di cui si troverà traccia sotto forma di impulso nella derivata successiva.

### 2.4 Due esempi dalla dispensa: seno e coseno «accesi» nell'origine

La dispensa (p. 12) applica la regola alle funzioni $\sin t\cdot1(t)$ e $\cos t\cdot1(t)$:

$$\frac{d}{dt}\big[\sin t\cdot1(t)\big] = \cos t\cdot1(t) + \sin t\cdot\delta(t) = \cos t\cdot1(t),$$

$$\frac{d}{dt}\big[\cos t\cdot1(t)\big] = -\sin t\cdot1(t) + \cos t\cdot\delta(t) = -\sin t\cdot1(t) + \delta(t).$$

Il confronto è istruttivo. $\sin t\cdot1(t)$ è continua nell'origine, perché $\sin 0 = 0$: non c'è salto, e infatti l'impulso si annulla per campionamento. $\cos t\cdot1(t)$ salta invece da $0$ a $\cos 0 = 1$, e nella derivata compare un impulso di area $1$.

> [!warning] Refuso nella dispensa A p. 12 la seconda formula è scritta con risultato $\sin(t)\cdot1(t) + \delta(t)$: manca il segno meno davanti al seno. Il risultato corretto è $-\sin t\cdot1(t) + \delta(t)$, perché la derivata del coseno è $-\sin t$.

## 3. La finestra rettangolare e le funzioni definite a tratti

### 3.1 Costruzione della finestra

Il gradino permette di costruire un oggetto molto utile. Si considerino due gradini traslati, $1(t-T_1)$ e $1(t-T_2)$ con $T_1<T_2$, e se ne faccia la differenza. Conviene esaminare i tre intervalli separatamente:

- per $t<T_1$ entrambi i gradini valgono $0$, e la differenza è $0-0=0$;
- per $T_1\le t<T_2$ il primo gradino vale $1$ e il secondo ancora $0$, e la differenza è $1$;
- per $t\ge T_2$ entrambi valgono $1$, e la differenza torna a $1-1=0$.

> [!important] Finestra rettangolare $$1(t-T_1) - 1(t-T_2) = \begin{cases} 1, & T_1 \le t < T_2 \ 0, & \text{altrove} \end{cases} \qquad (T_1<T_2)$$ È un impulso rettangolare di altezza unitaria compreso tra $T_1$ e $T_2$. Il docente lo chiama _boxcar_ («scatoletta»); negli appunti compare come _gate pulse_.

La dispensa (p. 11) affianca a questi oggetti il gradino «rovesciato» $1(T-t)$, che ha comportamento opposto a quello del gradino: vale $1$ prima di $T$ e $0$ dopo.

### 3.2 Scrivere una funzione a tratti in una sola riga

Moltiplicare una funzione per la finestra significa **fotografarla** soltanto nell'intervallo in cui la finestra vale $1$:

$$f(t),\big[1(t-T_1) - 1(t-T_2)\big] = \begin{cases} f(t), & T_1 \le t < T_2 \ 0, & \text{altrove.} \end{cases}$$

L'immagine proposta dal docente è quella di un visore largo $T_2-T_1$ posato davanti alla funzione: si vede solo la porzione inquadrata. Spostando il visore avanti o indietro si fotografa la funzione in qualunque punto.

Questo meccanismo ha due conseguenze pratiche. Una funzione definita a tratti, che normalmente richiederebbe una lunga parentesi graffa, si scrive in **una sola riga**: si somma ogni tratto moltiplicato per la sua finestra. Inoltre la sua derivata si calcola applicando le regole di derivazione ordinarie (regola del prodotto e campionamento), «senza preoccuparsi di niente». I salti e i punti angolosi vengono gestiti automaticamente dagli impulsi e dai gradini che compaiono derivando le finestre.

### 3.3 Esempio svolto a lezione

> [!example] Coseno e rampa a tratti Si consideri la funzione che:
> 
> - vale $\cos t$ tra $0$ e $\pi/2$;
> - è nulla tra $\pi/2$ e $\pi$;
> - tra $\pi$ e $4$ è una retta che parte da $0$ in $t=\pi$ e raggiunge il valore $1$ in $t=4$;
> - è nulla dopo $t=4$ (e prima di $0$).
> 
> La retta deve annullarsi in $\pi$, quindi contiene il fattore $(t-\pi)$. Deve valere $1$ in $t=4$, quindi va divisa per $4-\pi$: il coefficiente angolare è il rapporto tra l'altezza raggiunta, $1$, e il cateto su cui poggia l'angolo, $4-\pi$. Con le finestre: $$f(t) = \cos t,\Big[1(t) - 1\big(t-\tfrac{\pi}{2}\big)\Big] + \frac{t-\pi}{4-\pi},\Big[1(t-\pi) - 1(t-4)\Big].$$ Nell'intervallo $[\pi/2, \pi)$ la funzione è nulla e non serve scrivere nulla: si scrivono solo i tratti diversi da zero. La formula vale per ogni $t$ e restituisce sempre il valore giusto.

``` chart
type: line
labels: [-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.3, 4.4, 4.5]
series:
  - title: "f(t)"
    data: [0, 0, 0, 0, 0, 1, 0.995, 0.98, 0.955, 0.921, 0.878, 0.825, 0.765, 0.697, 0.622, 0.54, 0.454, 0.362, 0.267, 0.17, 0.071, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.068, 0.185, 0.301, 0.418, 0.534, 0.651, 0.767, 0.884, 0, 0, 0, 0, 0, 0]
tension: 0
width: 80%
labelColors: false
fill: false
beginAtZero: true
```

Il grafico è campionato ogni $0{,}1$: i salti in $t=0$ e in $t=4$, che nella funzione sono verticali, appaiono come tratti molto ripidi.

**Derivata letta dal grafico.** Prima di fare i conti, conviene prevedere la derivata guardando la funzione. Si procede da sinistra a destra:

- per $t<0$ la funzione è nulla, e la derivata pure;
- in $t=0$ la funzione salta da $0$ a $\cos 0 = 1$: per la regola del §2.3 la derivata contiene un **impulso di area $1$** (di ordine zero), $+\delta(t)$;
- tra $0$ e $\pi/2$ la derivata è quella del coseno, $-\sin t$, che scende da $0$ a $-1$;
- in $t=\pi/2$ la funzione è continua ($\cos\frac{\pi}{2} = 0$) ma ha un punto angoloso: la derivata passa da $-1$ a $0$ con un salto, senza impulsi;
- tra $\pi/2$ e $\pi$ la funzione è piatta e la derivata è nulla;
- in $t=\pi$ la funzione è ancora continua ma la derivata salta da $0$ a $\frac{1}{4-\pi}$: altro salto della derivata, senza impulsi;
- tra $\pi$ e $4$ la derivata è il coefficiente angolare della retta, $\frac{1}{4-\pi}$;
- in $t=4$ la funzione **salta** da $1$ a $0$: la derivata contiene un impulso rivolto verso il basso, $-\delta(t-4)$;
- dopo $t=4$ tutto è nullo.

L'ultimo impulso è quello che, in un primo momento, il docente stesso aveva dimenticato, accorgendosene solo durante i conti. È un errore tipico: i salti «di chiusura» di una funzione a tratti sono facili da trascurare.

**Derivata calcolata con le regole.** Si applica la regola del prodotto a ciascun addendo:

$$\begin{aligned} \dot f(t) ={}& -\sin t,\Big[1(t) - 1\big(t-\tfrac{\pi}{2}\big)\Big] + \cos t,\Big[\delta(t) - \delta\big(t-\tfrac{\pi}{2}\big)\Big] \ &+ \frac{1}{4-\pi},\Big[1(t-\pi) - 1(t-4)\Big] + \frac{t-\pi}{4-\pi},\Big[\delta(t-\pi) - \delta(t-4)\Big]. \end{aligned}$$

Ai termini con gli impulsi si applica la proprietà del campionamento, sostituendo a $t$ il punto in cui ciascun impulso è concentrato:

- $\cos t\cdot\delta(t) = \cos 0\cdot\delta(t) = \delta(t)$;
- $\cos t\cdot\delta(t-\frac{\pi}{2}) = \cos\frac{\pi}{2}\cdot\delta(t-\frac{\pi}{2}) = 0$;
- $\frac{t-\pi}{4-\pi},\delta(t-\pi) = \frac{\pi-\pi}{4-\pi},\delta(t-\pi) = 0$;
- $\frac{t-\pi}{4-\pi},\delta(t-4) = \frac{4-\pi}{4-\pi},\delta(t-4) = \delta(t-4)$.

Si ottiene

$$\dot f(t) = -\sin t,\Big[1(t) - 1\big(t-\tfrac{\pi}{2}\big)\Big] + \delta(t) + \frac{1}{4-\pi},\Big[1(t-\pi) - 1(t-4)\Big] - \delta(t-4).$$

Il confronto con la previsione grafica è completo. Gli impulsi sono uno positivo di area unitaria in $t=0$ e uno negativo di area unitaria in $t=4$. La parte ordinaria vale $-\sin t$ tra $0$ e $\pi/2$, zero tra $\pi/2$ e $\pi$ (nessun termine «acceso» in quell'intervallo), la costante $\frac{1}{4-\pi}$ tra $\pi$ e $4$, e zero dopo. Come ripete il docente, «se due cose sono uguali, sono uguali»: i due procedimenti non possono dare risultati diversi, e confrontarli è un ottimo controllo.

> [!warning] Discrepanza negli appunti (nota «Funzioni generalizzate») 
> Nella nota il terzo e il quarto termine della derivata sono scritti con le finestre del primo tratto, $\big[1(t) - 1(t-\frac{\pi}{2})\big]$ e $\big[\delta(t) - \delta(t-\frac{\pi}{2})\big]$, anziché con quelle del secondo tratto, $\big[1(t-\pi) - 1(t-4)\big]$ e $\big[\delta(t-\pi) - \delta(t-4)\big]$. L'errore si propaga al risultato finale, dove compare $\frac{1}{4-\pi}\big[1(t) - 1(t-\frac{\pi}{2})\big]$. La versione corretta è quella riportata sopra, che coincide con gli appunti a mano.

### 3.4 Esempio dalla dispensa: un segnale di controllo a tratti

La dispensa (pp. 11–12, Esempio PM 1) applica lo stesso metodo a un segnale di controllo $u(t)$ formato da segmenti:

- sale linearmente da $0$ a $2$ tra $t=0$ e $t=1$;
- resta costante a $2$ fino a $t=2$;
- in $t=2$ crolla a $0$;
- risale linearmente fino a $1$ in $t=3$;
- ridiscende a $0$ in $t=4$.

> [!example] Esempio PM 1 (dispensa) 
> Individuate le quattro finestre corrispondenti agli intervalli $[0,1)$, $[1,2)$, $[2,3)$, $[3,4)$, si scrive l'andamento della funzione in ciascuna: $$u(t) = 2t,\big[1(t)-1(t-1)\big] + 2,\big[1(t-1)-1(t-2)\big] + (t-2),\big[1(t-2)-1(t-3)\big] + (4-t),\big[1(t-3)-1(t-4)\big].$$ Raccogliendo i coefficienti di ciascun gradino si ottiene la forma compatta: $$u(t) = 2t\cdot1(t) + 2(1-t)\cdot1(t-1) + (t-4)\cdot1(t-2) - 2(t-3)\cdot1(t-3) + (t-4)\cdot1(t-4).$$ Il coefficiente di $1(t-1)$, ad esempio, è $-2t+2$; quello di $1(t-3)$ è $-(t-2)+(4-t) = 6-2t$.
> 
> Derivando con la regola del prodotto: $$\begin{aligned} \dot u(t) ={}& 2\cdot1(t) + 2t,\delta(t) - 2\cdot1(t-1) + 2(1-t),\delta(t-1) + 1(t-2) + (t-4),\delta(t-2) \ &- 2\cdot1(t-3) - 2(t-3),\delta(t-3) + 1(t-4) + (t-4),\delta(t-4). \end{aligned}$$ Per campionamento tutti gli impulsi si annullano tranne quello in $t=2$, dove $(t-4),\delta(t-2) = (2-4),\delta(t-2) = -2,\delta(t-2)$. Quindi $$\dot u(t) = 2\cdot1(t) - 2\cdot1(t-1) + 1(t-2) - 2\cdot1(t-3) + 1(t-4) - 2,\delta(t-2).$$ Graficamente la derivata vale $2$ su $[0,1)$, $0$ su $[1,2)$, $1$ su $[2,3)$ e $-1$ su $[3,4)$, poi $0$. In $t=2$ c'è un impulso verso il basso di area $2$: è l'unico salto della funzione, che passa da $2$ a $0$. La dispensa lascia il termine nella forma $(t-4),\delta(t-2)$, che per campionamento è proprio $-2,\delta(t-2)$.

### 3.5 A che cosa serve

Una cosa del genere può sembrare un esercizio fine a sé stesso, ma il docente porta un esempio concreto: le centraline delle automobili moderne. Con acceleratore e freno _by wire_, il pedale non agisce meccanicamente sull'impianto: la centralina riceve il comando e applica un **profilo** (di accelerazione, di frenata) scelto in base alla situazione, ad esempio per non bloccare le ruote. Questi profili sono fatti proprio così: pezzi di funzioni (rette che salgono, tratti costanti, rette che scendono) raccordati l'uno all'altro secondo le varie fasi della manovra.

C'è poi un'utilità più vicina al corso. Con i metodi visti in analisi, un'equazione differenziale con un termine forzante a tratti si risolve un pezzo alla volta. Si trova la soluzione fino al primo punto di raccordo, si calcolano le condizioni in quel punto, le si usano come condizioni iniziali del tratto successivo, e così via per ogni tratto (cinquanta volte, se i tratti sono cinquanta). Scrivendo la forzante in una sola riga con le finestre, la trasformata di Laplace risolverà l'equazione in un colpo solo, gestendo automaticamente tutti i salti.

## 4. Comunicazioni sul corso

Quest'anno il corso è rivolto ai soli studenti di Ingegneria Informatica. Gli studenti di Ingegneria Biomedica del nuovo ordinamento seguono un insegnamento diverso, con contenuti ridotti, e non possono sostenere questo esame. Possono invece sostenerlo, con questi contenuti, quelli del vecchio ordinamento.

Il docente ricorda di avere la facoltà di verificare, all'esame, che lo studente possieda le conoscenze di base necessarie. Chi non sa calcolare la derivata di una funzione, o non conosce le regole del prodotto matrice per vettore e matrice per matrice, viene invitato a ripassarle prima di tornare. Per lo stesso motivo, durante il corso non si soffermerà troppo sui dettagli matematici già noti. Ad esempio, che un integrale su un dominio semi-infinito richieda alla funzione integranda condizioni di decrescenza adeguate è qualcosa che gli studenti devono sapere da sé.

## 5. La trasformata di Laplace

### 5.1 Un operatore da conoscere a fondo

Il docente premette un'osservazione di metodo. In quasi ogni corso i concetti davvero fondamentali si riducono a tre o quattro; tutto il resto è l'uso ripetuto degli stessi concetti visti da angolazioni diverse. In Teoria dei Sistemi uno di questi è la **trasformata di Laplace**. La si definisce una volta e poi la si usa per studiare una proprietà, poi un'altra, poi un'altra ancora, ma l'operatore è sempre lo stesso. Chi lo conosce bene segue il corso con facilità. Chi non lo conosce ha l'impressione che ogni argomento sia nuovo, mentre è sempre la stessa cosa applicata a un caso diverso.

### 5.2 Notazione e definizione

Per tutto il corso vale una **convenzione di notazione**:

- una funzione del tempo si indica con una lettera **minuscola**, ad esempio $f(t)$;
- la sua trasformata si indica con la **stessa lettera maiuscola**, ad esempio $F(s)$, funzione della variabile complessa $s$.

Quando si vede una lettera minuscola si sa che si tratta di una funzione del tempo; quando se ne vede una maiuscola si sa che è una trasformata. Gli argomenti sono di natura diversa: il tempo, reale, in un caso; la variabile complessa $s$ nell'altro.

> [!important] Trasformata di Laplace La trasformata di Laplace della funzione $f(t)$ è $$\mathcal{L}{f(t)} = F(s) \triangleq \int_{0^-}^{\infty} f(t),e^{-st},dt, \qquad s\in\mathbb{C}.$$ L'operatore fa passare dal **dominio del tempo** al **dominio di $s$**: $;f(t)\ \longrightarrow\ \mathcal{L}{\cdot}\ \longrightarrow\ F(s)$.

Il simbolo $\triangleq$ («uguale per definizione») indica che l'uguaglianza è una definizione e non il risultato di un calcolo. Nell'integrale compaiono sia $t$ sia $s$. Integrando rispetto a $t$, la variabile di integrazione sparisce e il risultato dipende soltanto da $s$.

Due osservazioni sull'estremo inferiore. La trasformata «vede» solo ciò che accade **da $0^-$ in avanti**: il comportamento della funzione per $t<0$ non le interessa e non può essere ricostruito dalla trasformata. Inoltre partire da $0^-$ significa includere nell'integrale anche ciò che è concentrato nell'origine, come un impulso.

> [!tip] Approfondimento: perché $0^-$ e non $0^+$ #approfondimento La scelta dell'estremo inferiore non è un dettaglio. Lundberg, Miller e Trumper hanno analizzato le incongruenze che nascono nei testi quando non è chiaro se l'origine sia inclusa o meno [@lundberg2007]. Sostengono la forma con estremo $0^-$, accompagnata dalla regola della derivata $\mathcal{L}{\dot f} = sF(s) - f(0^-)$, proprio quella adottata nel corso. Con questa convenzione gli impulsi nell'origine sono sempre inclusi, e le condizioni iniziali sono quelle «pre-iniziali», cioè lo stato del sistema prima che l'ingresso intervenga. Ne risulta un trattamento coerente dei transitori con ingressi discontinui o impulsivi.

### 5.3 Esistenza e ascissa di convergenza

L'integrale che definisce la trasformata è esteso a un dominio semi-infinito, e non è detto che converga: la funzione potrebbe divergere all'infinito. Il docente ricorda che, perché l'integrale esista, l'integranda deve tendere a zero abbastanza in fretta (più rapidamente di $1/t$). Qui interviene il ruolo di $s$. Scrivendo $s$ in parte reale e parte immaginaria, $s = \sigma + j\omega$, l'esponenziale si spezza nel prodotto di due fattori:

$$F(s) = \int_{0^-}^{\infty} f(t),e^{-\sigma t},e^{-j\omega t},dt .$$

Il fattore $e^{-j\omega t}$ ha modulo unitario: oscilla senza crescere né decrescere. Il fattore $e^{-\sigma t}$ è un esponenziale reale che, per $\sigma>0$, tende a zero. Anche se la funzione cresce, il crollo a zero dell'esponenziale può controbilanciarne la crescita, purché sia più rapido. A meno che $f$ non sia una funzione patologica che cresce più velocemente di qualunque esponenziale (un esempio classico è $e^{t^2}$), esiste quindi un valore di $\sigma$ oltre il quale l'integrale converge. La trasformata non deve esistere per ogni $s$: basta che esista per gli $s$ con parte reale abbastanza grande.

> [!important] Ascissa di convergenza Se esiste la trasformata di $f$, esiste un valore critico $\bar\sigma$ tale che l'integrale converge per $\mathrm{Re}(s) = \sigma > \bar\sigma$ e non converge per $\sigma < \bar\sigma$. Tale valore si chiama **ascissa di convergenza**. Sul piano complesso (piano di Gauss) la regione di convergenza è il semipiano a destra della retta verticale $\mathrm{Re}(s) = \bar\sigma$.

Per esempio, per il gradino il calcolo diretto (dispensa, p. 13) dà

$$\mathcal{L}{1(t)} = \int_{0^-}^{\infty} e^{-st},dt = \Big[-\frac{1}{s},e^{-st}\Big]_{0}^{\infty} = \frac{1}{s},$$

e il termine all'infinito si annulla solo se $\mathrm{Re}(s)>0$. L'ascissa di convergenza è quindi $\bar\sigma = 0$. Per $e^{at}$ (§5.5) si troverà $\bar\sigma = a$. Il docente chiude qui il discorso sull'esistenza e non ci tornerà più: nel corso si considereranno sempre funzioni per cui la trasformata esiste.

C'è infine una convenzione d'uso. Poiché la trasformata considera solo ciò che accade da $0^-$ in avanti, scrivere $f(t)$ oppure $f(t)\cdot1(t)$ è indifferente ai fini del calcolo: l'integrale è lo stesso. Il docente di solito **omette** il gradino. Lo scrive solo quando vuole sottolineare che la funzione non va considerata prima di un certo istante, cioè nei casi in cui la trasformata è sensibile a questo aspetto, come la traslazione nel tempo (§5.4).

### 5.4 Proprietà

Il docente elenca le proprietà invece di calcolare una per una le trasformate delle varie funzioni. Il motivo è che, per le funzioni che servono nel corso, **tutte le trasformate necessarie si ricavano dalla trasformata dell'impulso di ordine zero applicando solo le proprietà**, senza mai calcolare un integrale. L'unico integrale da calcolare è quello dell'impulso, e anche lì basta la proprietà del campionamento.

#### Linearità

> [!important] Linearità $$\mathcal{L}{\alpha f_1(t) + \beta f_2(t)} = \alpha F_1(s) + \beta F_2(s)$$ per ogni coppia di costanti $\alpha,\beta$.

La proprietà discende dalla linearità dell'integrale. A lezione $\alpha$ e $\beta$ sono introdotti come numeri reali, ma la proprietà vale anche per costanti **complesse**, e lo si sfrutterà per calcolare la trasformata del seno.

#### Trasformata della derivata

> [!important] Derivata $$\mathcal{L}{\dot f(t)} = s,F(s) - f(0^-)$$

Qui la notazione va letta con attenzione. $F(s)$ è la trasformata della funzione **originale** $f$, non della derivata $\dot f$. $f(0^-)$ è il valore della **funzione del tempo** in $0^-$, cioè una lettera minuscola, e non la trasformata calcolata in zero, che non avrebbe alcun significato.

La dimostrazione, l'unica di questo tipo svolta per esteso dal docente, è un'integrazione per parti:

$$\begin{aligned} \mathcal{L}{\dot f(t)} &= \int_{0^-}^{\infty}\dot f(t),e^{-st},dt = \Big[f(t),e^{-st}\Big]_{0^-}^{\infty} - \int_{0^-}^{\infty} f(t),\big(-s,e^{-st}\big),dt [4pt] &= \underbrace{\lim_{t\to\infty} f(t),e^{-st}}_{=,0} ;-; f(0^-) ;+; s\int_{0^-}^{\infty} f(t),e^{-st},dt = s,F(s) - f(0^-). \end{aligned}$$

Il termine all'infinito è nullo, perché altrimenti l'integrale che definisce $F(s)$ non esisterebbe. In $0^-$ l'esponenziale vale $1$.

Applicando la proprietà due volte si ottiene la trasformata della derivata seconda, che la dispensa usa nel paragrafo sulla risoluzione delle equazioni differenziali:

$$\mathcal{L}{\ddot f(t)} = s,\mathcal{L}{\dot f(t)} - \dot f(0^-) = s^2F(s) - s,f(0^-) - \dot f(0^-),$$

e in generale ogni derivazione moltiplica per $s$ e sottrae una condizione iniziale. Questa è la proprietà che trasformerà le equazioni differenziali in equazioni algebriche.

#### Trasformata dell'integrale

> [!important] Integrale $$\mathcal{L}\left{\int_{0^-}^{t} f(\tau),d\tau\right} = \frac{1}{s},F(s)$$

La dispensa dimostra la proprietà per parti. Una via più rapida è usare la proprietà precedente. Posto $g(t) = \int_{0^-}^{t} f(\tau),d\tau$, si ha $\dot g = f$ e $g(0^-) = 0$, quindi $F(s) = s,G(s) - 0$, cioè $G(s) = F(s)/s$. Derivare nel tempo corrisponde a moltiplicare per $s$; integrare a dividere per $s$.

#### Traslazione nel tempo

> [!important] Traslazione nel tempo (ritardo) Per $T>0$: $$\mathcal{L}{f(t-T)\cdot1(t-T)} = e^{-sT},F(s)$$

La dimostrazione (dispensa, p. 13) usa il cambio di variabile $\tau = t-T$. Il gradino annulla l'integranda prima di $T$:

$$\int_{0^-}^{\infty} f(t-T),1(t-T),e^{-st},dt = \int_{T^-}^{\infty} f(t-T),e^{-st},dt = \int_{0^-}^{\infty} f(\tau),e^{-s(\tau+T)},d\tau = e^{-sT}F(s).$$

Il docente insiste sul **perché serve il gradino** $1(t-T)$. La trasformata di $f$ «pesca» solo ciò che succede da zero in avanti: quanto valesse $f$ in $t=-7$, la trasformata non lo sa. Se si trasla la sola $f(t)$ in avanti di $T$, senza troncarla, nell'intervallo di integrazione entra anche il pezzo di funzione che prima stava a sinistra dell'origine, e che la trasformata originale non aveva mai considerato. Le due trasformate si potrebbero allora legare solo in modo molto complicato, ricostruendo ciò che è entrato nello spostamento. Moltiplicando invece per $1(t-T)$ si trasla la funzione **troncata**: ciò che entra nell'intervallo di integrazione è esattamente la stessa area di prima, spostata in avanti, senza pezzi sconosciuti. La regola si applica quindi solo a espressioni della forma $f(t-T)\cdot1(t-T)$: una funzione traslata **e** accesa dal gradino traslato della stessa quantità.

> [!tip] Schema consigliato La differenza tra «traslare la funzione» e «traslare la funzione troncata» si capisce bene disegnando una stessa $f$ non nulla anche per $t<0$, la sua traslata e la sua traslata moltiplicata per $1(t-T)$. In questo punto può essere utile uno schizzo con Excalidraw.

#### Moltiplicazione per un esponenziale (traslazione in $s$)

> [!important] Traslazione in $s$ $$\mathcal{L}{e^{at},f(t)} = F(s-a)$$

La dimostrazione è immediata: $\int_{0^-}^{\infty} e^{at}f(t),e^{-st},dt = \int_{0^-}^{\infty} f(t),e^{-(s-a)t},dt = F(s-a)$. Moltiplicare per un esponenziale nel tempo corrisponde a traslare la trasformata nel dominio di $s$ della quantità $a$, che può anche essere complessa.

#### Moltiplicazione per $t$

> [!important] Moltiplicazione per $t$ $$\mathcal{L}{t,f(t)} = -\frac{d}{ds}F(s), \qquad \text{e in generale}\qquad \mathcal{L}{t^n f(t)} = (-1)^n,\frac{d^n}{ds^n}F(s).$$

Derivando la definizione rispetto a $s$ sotto il segno di integrale (dispensa, p. 14) si ottiene $\frac{d}{ds}\int_{0^-}^{\infty} f(t),e^{-st},dt = \int_{0^-}^{\infty} \big(-t,f(t)\big),e^{-st},dt$, da cui la tesi.

Dagli appunti personali emerge una conseguenza utile. Se $F(s) = N(s)/D(s)^\alpha$, allora

$$-\frac{d}{ds}\frac{N}{D^\alpha} = -\frac{N'D^\alpha - \alpha D^{\alpha-1}D'N}{D^{2\alpha}} = -\frac{N'D - \alpha D'N}{D^{\alpha+1}},$$

cioè **ogni moltiplicazione per $t$ aumenta di uno la potenza del denominatore**.

#### Attenzione: il prodotto

> [!warning] Da «scrivere col sangue» Date due funzioni del tempo $f$ e $g$: $$\mathcal{L}{f(t),g(t)} \neq F(s),G(s).$$ La trasformata del prodotto **non** è il prodotto delle trasformate.

Il prodotto delle trasformate corrisponde a un'altra operazione nel tempo, l'**integrale di convoluzione**. La sua definizione non è stata data in questa lezione; per funzioni nulle prima dell'origine è $(f_g)(t) = \int_{0^-}^{t} f(\tau),g(t-\tau),d\tau$, e vale $\mathcal{L}{f_g} = F(s),G(s)$.

Il docente aggiunge un avvertimento per chi segue o seguirà corsi di teoria dei segnali o di comunicazioni. La trasformata di Fourier e quella di Laplace sono «parenti» e a prima vista si assomigliano molto, ma in realtà si assomigliano solo un po'. Capire fino in fondo il loro legame richiederebbe un corso a sé, e le domande che si possono porre in proposito sono di una densità inimmaginabile. Il consiglio è di prenderne atto («si assomigliano») e andare avanti.

#### Riepilogo delle proprietà

|Nel tempo|Nel dominio di $s$|Nome|
|:--|:--|:--|
|$\alpha f_1(t) + \beta f_2(t)$|$\alpha F_1(s) + \beta F_2(s)$|linearità|
|$\dot f(t)$|$s,F(s) - f(0^-)$|derivata|
|$\ddot f(t)$|$s^2F(s) - s,f(0^-) - \dot f(0^-)$|derivata seconda|
|$\int_{0^-}^{t} f(\tau),d\tau$|$F(s)/s$|integrale|
|$f(t-T)\cdot1(t-T)$|$e^{-sT}F(s)$|traslazione nel tempo|
|$e^{at}f(t)$|$F(s-a)$|traslazione in $s$|
|$t,f(t)$|$-\dfrac{d}{ds}F(s)$|moltiplicazione per $t$|
|$f(t),g(t)$|**non** $F(s)G(s)$|attenzione|

### 5.5 Trasformate notevoli

Si ricavano ora le trasformate delle funzioni elementari partendo dall'impulso e usando soltanto le proprietà. A volte le strade per arrivarci sono più di una: se si percorrono entrambe, il risultato deve essere lo stesso.

#### Impulso

Per la proprietà del campionamento, l'integrale dell'impulso per la funzione $e^{-st}$ restituisce l'esponenziale calcolato dove l'impulso è concentrato, cioè in $t=0$:

$$\mathcal{L}{\delta(t)} = \int_{0^-}^{\infty}\delta(t),e^{-st},dt = e^{-s\cdot 0} = 1.$$

Qui si vede perché l'estremo inferiore è $0^-$. Partire da $-\infty$ non cambierebbe nulla, ma partire da $0^+$ escluderebbe l'impulso e darebbe zero.

#### Gradino e costante

Il gradino è l'integrale dell'impulso (impulso di ordine $-1$). Per la proprietà dell'integrale:

$$\mathcal{L}{1(t)} = \mathcal{L}\left{\int_{0^-}^{t}\delta(\tau),d\tau\right} = \frac{1}{s}\cdot 1 = \frac{1}{s}.$$

Che cosa cambia se al posto del gradino si trasforma la costante $1$? Nulla: l'integrale parte comunque da $0^-$, e da lì in avanti gradino e costante coincidono. Quindi anche $\mathcal{L}{1} = 1/s$. **Per la trasformata di Laplace gradino e costante sono la stessa cosa.**

#### Rampa e potenze di $t$

La rampa $t\cdot1(t)$ si può vedere in due modi, ed entrambi portano allo stesso risultato:

- come **integrale del gradino**: $\mathcal{L}{t\cdot1(t)} = \frac{1}{s}\cdot\frac{1}{s} = \frac{1}{s^2}$;
- come **gradino moltiplicato per $t$**: $\mathcal{L}{t\cdot1(t)} = -\frac{d}{ds}\frac{1}{s} = \frac{1}{s^2}$.

Proseguendo con le integrazioni successive, ogni integrale porta un ulteriore fattore $1/s$:

$$\mathcal{L}\left{\frac{t^k}{k!},1(t)\right} = \frac{1}{s^{k+1}}.$$

Il fattoriale a denominatore è proprio quello prodotto dalle integrazioni successive ($t$, poi $t^2/2$, poi $t^3/6$, ...). Si ha così una lettura unitaria di tutti gli impulsi, presente anche negli appunti: poiché $\delta_k$ è la derivata $k$-esima di $\delta$ (con condizioni nulle in $0^-$) e $\delta_{-(k+1)} = \frac{t^k}{k!}1(t)$,

$$\mathcal{L}{\delta_k(t)} = s^k \qquad \text{per ogni intero } k$$

($s$ per il doppietto, $1$ per l'impulso, $1/s$ per il gradino, $1/s^2$ per la rampa, ...).

#### Esponenziale

Applicando la traslazione in $s$ alla trasformata del gradino:

$$\mathcal{L}{e^{at}\cdot1(t)} = \frac{1}{s-a}, \qquad\qquad \mathcal{L}\left{\frac{t^k}{k!},e^{at}\right} = \frac{1}{(s-a)^{k+1}}.$$

#### Seno e coseno

Per il seno il docente evita di calcolare l'integrale e usa la scrittura con gli esponenziali complessi. Dalle formule di Eulero $e^{j\omega t} = \cos\omega t + j\sin\omega t$ ed $e^{-j\omega t} = \cos\omega t - j\sin\omega t$, sottraendo i coseni si elidono e resta $2j\sin\omega t$:

$$\sin\omega t = \frac{e^{j\omega t} - e^{-j\omega t}}{2j}.$$

Per linearità, che vale anche con coefficienti complessi, e per la trasformata dell'esponenziale con $a = \pm j\omega$:

$$\mathcal{L}{\sin\omega t} = \frac{1}{2j}\left(\frac{1}{s-j\omega} - \frac{1}{s+j\omega}\right) = \frac{1}{2j}\cdot\frac{(s+j\omega) - (s-j\omega)}{s^2+\omega^2} = \frac{1}{2j}\cdot\frac{2j\omega}{s^2+\omega^2} = \frac{\omega}{s^2+\omega^2}.$$

Il denominatore è il prodotto di due numeri complessi coniugati: $(s-j\omega)(s+j\omega) = s^2+\omega^2$.

Per il coseno esistono due strade:

- con gli esponenziali: $\cos\omega t = \frac{e^{j\omega t}+e^{-j\omega t}}{2}$, quindi $\mathcal{L}{\cos\omega t} = \frac{1}{2}\left(\frac{1}{s-j\omega}+\frac{1}{s+j\omega}\right) = \frac{s}{s^2+\omega^2}$;
- con le funzioni generalizzate (dispensa, p. 15): $\frac{d}{dt}\big[\sin\omega t\cdot1(t)\big] = \omega\cos\omega t\cdot1(t)$, perché l'impulso si annulla essendo $\sin 0 = 0$. Allora $\mathcal{L}{\cos\omega t} = \frac{1}{\omega}\big(s\cdot\frac{\omega}{s^2+\omega^2} - 0\big) = \frac{s}{s^2+\omega^2}$.

> [!important] Trasformate reali di funzioni reali La trasformata di una funzione reale è sempre una funzione della variabile complessa $s$ **a coefficienti reali**. Nei passaggi possono comparire quantità complesse, come $\frac{1}{2j}$ e $\frac{1}{s\mp j\omega}$, ma quando si mettono insieme tutte le parti complesse si semplificano.

#### Funzioni smorzate e moltiplicate per $t$

Con la traslazione in $s$:

$$\mathcal{L}{e^{at}\sin\omega t} = \frac{\omega}{(s-a)^2+\omega^2}, \qquad \mathcal{L}{e^{at}\cos\omega t} = \frac{s-a}{(s-a)^2+\omega^2}.$$

Moltiplicando ulteriormente per $t$ (vedi l'esercizio §6.1):

$$\mathcal{L}{t,e^{at}\sin\omega t} = \frac{2\omega(s-a)}{\big[(s-a)^2+\omega^2\big]^2}, \qquad \mathcal{L}{t,e^{at}\cos\omega t} = \frac{(s-a)^2-\omega^2}{\big[(s-a)^2+\omega^2\big]^2}.$$

Il docente osserva che le funzioni che si incontrano nel corso non sono tutte le funzioni dell'universo. Il caso più complicato che può capitare è il **prodotto di un polinomio nel tempo, di un esponenziale e di un seno o coseno** (il nome con cui il docente indica questa classe non è comprensibile nella registrazione). Un esempio citato è del tipo $\frac{t^4}{4!},e^{-3t}\sin(\sqrt2,t)$, ricostruito da un passaggio poco chiaro. Anche per funzioni così la trasformata si ottiene senza calcolare integrali, applicando una proprietà alla volta. Ogni fattore $t$ aggiuntivo eleva di uno la potenza del denominatore, per cui una funzione con $\frac{t^k}{k!}$ ha denominatore $\big[(s-a)^2+\omega^2\big]^{k+1}$. Il numeratore non ha una forma generale semplice e va ricavato caso per caso.

#### Tabella riassuntiva

|$f(t)$|$F(s)$|
|:--|:--|
|$\delta(t)$|$1$|
|$\delta_k(t)$|$s^k$|
|$1(t)$, oppure la costante $1$|$\dfrac{1}{s}$|
|$t\cdot1(t)$|$\dfrac{1}{s^2}$|
|$\dfrac{t^k}{k!},1(t)$|$\dfrac{1}{s^{k+1}}$|
|$e^{at}$|$\dfrac{1}{s-a}$|
|$\dfrac{t^k}{k!},e^{at}$|$\dfrac{1}{(s-a)^{k+1}}$|
|$\sin\omega t$|$\dfrac{\omega}{s^2+\omega^2}$|
|$\cos\omega t$|$\dfrac{s}{s^2+\omega^2}$|
|$e^{at}\sin\omega t$|$\dfrac{\omega}{(s-a)^2+\omega^2}$|
|$e^{at}\cos\omega t$|$\dfrac{s-a}{(s-a)^2+\omega^2}$|
|$t,e^{at}\sin\omega t$|$\dfrac{2\omega(s-a)}{\big[(s-a)^2+\omega^2\big]^2}$|
|$t,e^{at}\cos\omega t$|$\dfrac{(s-a)^2-\omega^2}{\big[(s-a)^2+\omega^2\big]^2}$|

### 5.6 Una nota sulle radici dei polinomi

Poiché più avanti si dovranno calcolare le radici di polinomi in $s$, il docente chiarisce che cosa è richiesto. Nessuno chiederà di calcolare a mano le radici di polinomi di grado $3$ o $4$, né tanto meno di grado $5$, per il quale non esiste nemmeno una formula generale. Le radici dei polinomi di **secondo grado** vanno invece sapute calcolare con facilità. Lo stesso vale per le **equazioni binomie** del tipo $s^{10} = 27$.

> [!example] Le radici di $s^{10} = 27$ Nel campo complesso l'equazione ha **dieci** radici. Hanno tutte lo stesso modulo, $\sqrt[10]{27}\approx 1{,}39$, e argomenti equispaziati di $2\pi/10$: $$s_k = \sqrt[10]{27};e^{,j\frac{2\pi k}{10}}, \qquad k = 0,1,\dots,9 .$$ Geometricamente sono i vertici di un **decagono regolare** inscritto nella circonferenza di raggio $\sqrt[10]{27}$ centrata nell'origine. Una delle radici è reale positiva ($k=0$) e una reale negativa ($k=5$).
> 
> Nella trascrizione il raggio compare con un valore diverso, quasi certamente per un errore di trascrizione: il modulo comune delle radici è necessariamente $\sqrt[10]{27}$.

## 6. Esercizi svolti

### 6.1 Esercizio di fine lezione

> [!example] Calcolare $\mathcal{L}{t,e^{at}\sin\omega t}$ Conviene leggere la funzione come $t\cdot\big(e^{at}\sin\omega t\big)$ e procedere dall'interno verso l'esterno.
> 
> 1. Trasformata del seno: $\mathcal{L}{\sin\omega t} = \dfrac{\omega}{s^2+\omega^2}$.
> 2. Moltiplicazione per $e^{at}$, cioè traslazione in $s$: $\mathcal{L}{e^{at}\sin\omega t} = \dfrac{\omega}{(s-a)^2+\omega^2}$.
> 3. Moltiplicazione per $t$, cioè derivata cambiata di segno: $$\mathcal{L}{t,e^{at}\sin\omega t} = -\frac{d}{ds},\frac{\omega}{(s-a)^2+\omega^2} = \frac{\omega\cdot 2(s-a)}{\big[(s-a)^2+\omega^2\big]^2} = \frac{2\omega(s-a)}{\big[(s-a)^2+\omega^2\big]^2}.$$
> 
> Come anticipato dal docente, il denominatore è il polinomio di secondo grado della trasformata smorzata **elevato al quadrato**.

> [!warning] Discrepanza negli appunti (nota «Laplace») Nella nota il calcolo è introdotto come $\mathcal{L}{e^{at}\sin\omega t} = \mathcal{L}{t,(e^{at}\sin\omega t)} = \dots$. Il primo membro andrebbe scritto $\mathcal{L}{t,e^{at}\sin\omega t}$: la trasformata di $e^{at}\sin\omega t$ e quella di $t,e^{at}\sin\omega t$ sono diverse. Il risultato finale riportato più sotto nella nota è invece corretto.

### 6.2 Esempi dalla dispensa

> [!example] Esempio PM 2 (dispensa, p. 15): $\mathcal{L}{e^{-2(t-3)},1(t-3)}$ La funzione ha esattamente la forma $g(t-3)\cdot1(t-3)$ con $g(t) = e^{-2t}$: è l'esponenziale traslato e acceso dal gradino traslato della stessa quantità. Per la traslazione nel tempo: $$\mathcal{L}{e^{-2(t-3)},1(t-3)} = e^{-3s},\mathcal{L}{e^{-2t}\cdot1(t)} = \frac{e^{-3s}}{s+2}.$$

> [!example] Esempio PM 3 (dispensa, p. 15) Calcolare $\mathcal{L}\big{t,e^{-3t}\cdot1(t) + \delta(t-4)\cdot1(t-5) + e^{-2(t-2)}\sin(t-2)\cdot1(t-2)\big}$.
> 
> Il **secondo termine è nullo**. L'impulso è concentrato in $t=4$, dove il gradino $1(t-5)$ vale ancora zero: per campionamento $\delta(t-4),1(t-5) = 1(4-5),\delta(t-4) = 0$.
> 
> Il primo termine è $t$ per $e^{-3t}$, e dà $\dfrac{1}{(s+3)^2}$. Il terzo ha la forma $g(t-2),1(t-2)$ con $g(t) = e^{-2t}\sin t$, la cui trasformata è $\dfrac{1}{(s+2)^2+1}$. Quindi $$\mathcal{L}{\dots} = \frac{1}{(s+3)^2} + \frac{e^{-2s}}{(s+2)^2+1}.$$

### 6.3 Esercizi dagli appunti personali

> [!warning] Provenienza Gli esercizi di questo paragrafo compaiono nella nota personale «Laplace» ma **non** nella parte di trascrizione disponibile. Potrebbero appartenere alla seconda parte della lezione o a una lezione successiva; se arriverà la relativa trascrizione, verranno ricollocati e confrontati con quanto detto dal docente. Le soluzioni sono state verificate anche per integrazione diretta.

> [!example] $\mathcal{L}{1(t-3) + \delta(t) + t\cdot1(t)}$ Per linearità si trasforma un termine alla volta: il gradino traslato dà $e^{-3s}/s$, l'impulso $1$, la rampa $1/s^2$. $$\mathcal{L}{\dots} = \frac{e^{-3s}}{s} + 1 + \frac{1}{s^2} = \frac{s,e^{-3s} + s^2 + 1}{s^2} = 1 + \frac{s,e^{-3s}+1}{s^2}.$$

> [!example] $\mathcal{L}{e^{a(t-T)}\cos\omega(t-T)\cdot1(t-T)}$ La funzione è $g(t-T),1(t-T)$ con $g(t) = e^{at}\cos\omega t$, quindi $$\mathcal{L}{\dots} = e^{-sT},\frac{s-a}{(s-a)^2+\omega^2}.$$ Nella nota il risultato è corretto, ma nel codice LaTeX la parentesi graffa dell'esponente racchiude per errore tutta la funzione, che risulta quindi stampata come esponente.

> [!example] Trasformata della funzione a tratti del §3.3 (segnata «RIFARE» negli appunti) Si vuole trasformare $$f(t) = \cos t,\Big[1(t) - 1\big(t-\tfrac{\pi}{2}\big)\Big] + \frac{t-\pi}{4-\pi},\Big[1(t-\pi) - 1(t-4)\Big].$$ Si separano i quattro termini: $$f(t) = \underbrace{\cos t\cdot1(t)}_{(a)} - \underbrace{\cos t\cdot1\big(t-\tfrac{\pi}{2}\big)}_{(b)} + \frac{1}{4-\pi}\Big[\underbrace{(t-\pi)\cdot1(t-\pi)}_{(c)} - \underbrace{(t-\pi)\cdot1(t-4)}_{(d)}\Big].$$
> 
> **(a)** È il coseno con $\omega = 1$: $\dfrac{s}{s^2+1}$.
> 
> **(b)** Il coseno non è scritto come funzione di $t-\frac{\pi}{2}$, quindi la traslazione non si applica direttamente. Bisogna prima riscriverlo: $\cos t = \cos\big((t-\tfrac{\pi}{2}) + \tfrac{\pi}{2}\big) = -\sin\big(t-\tfrac{\pi}{2}\big)$. Allora $(b) = -\sin\big(t-\frac{\pi}{2}\big),1\big(t-\frac{\pi}{2}\big)$, che si trasforma in $-e^{-\pi s/2}\dfrac{1}{s^2+1}$.
> 
> **(c)** È una rampa traslata in $\pi$: $\dfrac{e^{-\pi s}}{s^2}$.
> 
> **(d)** Anche qui bisogna esprimere tutto in funzione di $t-4$: $t-\pi = (t-4) + (4-\pi)$. Quindi $(d) = (t-4),1(t-4) + (4-\pi),1(t-4)$, che si trasforma in $\dfrac{e^{-4s}}{s^2} + (4-\pi)\dfrac{e^{-4s}}{s}$.
> 
> Mettendo insieme, con i segni corretti: $$F(s) = \frac{s}{s^2+1} + \frac{e^{-\pi s/2}}{s^2+1} + \frac{e^{-\pi s} - e^{-4s}}{(4-\pi),s^2} - \frac{e^{-4s}}{s}.$$
> 
> **Verifica con la proprietà della derivata.** Poiché $f(0^-) = 0$, deve valere $\mathcal{L}{\dot f} = s,F(s)$. Si trasforma termine per termine la derivata trovata nel §3.3, usando $\sin t = \cos\big(t-\frac{\pi}{2}\big)$ per il termine traslato: $$\mathcal{L}{\dot f} = -\frac{1}{s^2+1} + \frac{s,e^{-\pi s/2}}{s^2+1} + 1 + \frac{e^{-\pi s} - e^{-4s}}{(4-\pi),s} - e^{-4s}.$$ Moltiplicando $F(s)$ per $s$ e usando $\frac{s^2}{s^2+1} = 1 - \frac{1}{s^2+1}$ si ottiene esattamente la stessa espressione. Il confronto conferma il risultato: un altro caso di «se due cose sono uguali, sono uguali».

> [!warning] Errori nel tentativo presente negli appunti Il tentativo nella nota «Laplace» contiene quattro errori:
> 
> - il fattore $\frac{t-\pi}{4-\pi}$ viene portato fuori dalla trasformata, ma per linearità si possono portare fuori solo le **costanti**, non quantità che dipendono da $t$;
> - la trasformata del coseno è scritta $\frac{s}{s^2+\omega^2}$ anziché $\frac{s}{s^2+1}$ (qui $\omega = 1$);
> - il termine $\cos t\cdot1(t-\frac{\pi}{2})$ è rimasto incompleto: va riscritto come $-\sin(t-\frac{\pi}{2}),1(t-\frac{\pi}{2})$ prima di applicare la traslazione;
> - la rampa traslata dà $\frac{1}{s^2}$, non $\frac{1}{s}$.
> 
> Inoltre la formula generale in fondo alla nota, $\mathcal{L}\big{\frac{t^k}{k!}e^{at}\sin/\cos\big}$, ha il numeratore vuoto. Per $k=0$ e $k=1$ i numeratori sono quelli della tabella del §5.5; per $k$ generico non esiste una forma semplice.

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. _Perché $f(t),\dot\delta(t) \neq f(0),\dot\delta(t)$?_ Derivando in due modi $f(t)\delta(t) = f(0)\delta(t)$ compare anche il termine $-\dot f(0),\delta(t)$: il doppietto campiona anche la derivata.
2. _Perché un salto nella funzione produce un impulso nella derivata?_ L'integrale della derivata su un intervallo che si restringe attorno al salto tende all'ampiezza del salto, un numero finito non nullo. Solo un impulso ha area finita su un intervallo nullo.
3. _Perché nella proprietà di traslazione serve il gradino $1(t-T)$?_ Senza troncamento entrerebbe nell'intervallo di integrazione la parte di $f$ a sinistra dell'origine, ignota alla trasformata originale.
4. _Perché l'estremo inferiore della trasformata è $0^-$?_ Per includere ciò che è concentrato nell'origine (ad esempio $\mathcal{L}{\delta} = 1$) e far comparire nella regola della derivata le condizioni prima dell'origine, $f(0^-)$.
5. _Perché per la trasformata di Laplace gradino e costante sono la stessa cosa?_ L'integrale parte da $0^-$, e da lì in avanti le due funzioni coincidono.
6. _Perché la trasformata di una funzione reale ha coefficienti reali, anche se nei passaggi compaiono numeri complessi?_ Le quantità complesse compaiono in coppie coniugate, ad esempio $s\mp j\omega$, e nella somma le parti immaginarie si elidono.