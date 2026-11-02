---
corso: Fisica 2
lezione: 12
data: 2026-10-30
argomenti: [resistenze in serie, resistenza equivalente, batterie reali in una maglia, differenza di potenziale tra due punti, legge dei nodi, circuiti a più maglie, resistenze in parallelo, partitore di corrente, circuiti RC, carica di un condensatore, scarica di un condensatore, costante di tempo]
bibliography: fisica2.bib
tags: [fisica2]
---

# Lezione 12 — Circuiti in corrente continua e circuiti RC

La lezione mette al lavoro la legge delle maglie della [[Fisica 2 - Lezione 11 - Forza elettromotrice e legge delle maglie|lezione 11]]. Si ricava la regola delle resistenze **in serie** e si risolve una maglia con due batterie reali, calcolando anche la differenza di potenziale tra due punti. Poi si aggiunge la seconda legge di Kirchhoff, quella dei **nodi**, e con le due leggi insieme si risolve un circuito a due maglie. Seguono le resistenze **in parallelo**. La parte nuova è il **circuito RC**: si scrive e si risolve l'equazione della carica e della scarica di un condensatore attraverso una resistenza, e compare la **costante di tempo** $RC$. Chiude un esercizio su una rete di quattro resistenze.

> [!warning] Sezione ricostruita — inizio
> Per questa lezione non c'è una trascrizione: l'unica fonte sono i tuoi **appunti a mano** (tre pagine, datati 30/10). L'intera nota è quindi ricostruita. Formule, figure ed esercizi vengono dagli appunti; le spiegazioni che li collegano sono mie, nello stile del docente nelle altre lezioni, e i calcoli li ho verificati. Dove negli appunti mancano i numeri li ho calcolati io, e lo dico. Dove c'è un errore lo segnalo nel punto in cui compare.

## Resistenze in serie

Si consideri una maglia con una batteria ideale di forza elettromotrice $\varepsilon$ e tre resistenze $R_1$, $R_2$, $R_3$ una dopo l'altra.

![[F2-L12-serie.svg]]

C'è un solo percorso, quindi la corrente $i$ è la **stessa** in tutti gli elementi: è la caratteristica degli elementi **in serie**. Si applica la legge delle maglie partendo dal punto $a$, sotto la batteria, e percorrendo il circuito nel verso della corrente. Attraversando la batteria dal polo negativo al positivo il potenziale sale di $\varepsilon$; attraversando ogni resistenza nel verso della corrente scende di $iR$:

$$
V_a \;\to\; V_a + \varepsilon \;\to\; V_a + \varepsilon - iR_1 \;\to\; V_a + \varepsilon - iR_1 - iR_2 \;\to\; V_a + \varepsilon - iR_1 - iR_2 - iR_3 = V_a .
$$

Quindi

$$
\varepsilon - i\,(R_1 + R_2 + R_3) = 0
\quad\Longrightarrow\quad
\varepsilon = i\,(R_1 + R_2 + R_3) = i\,R_{\text{eq}} .
$$

Le tre resistenze si comportano come un'unica resistenza $R_{\text{eq}}$, attraversata dalla stessa corrente con la stessa f.e.m.

> [!important] Resistenze in serie
> $$
> R_{\text{eq}} = \sum_{k=1}^{n} R_k .
> $$
> In serie le resistenze si **sommano**: la stessa corrente le attraversa tutte, e le cadute di tensione si sommano.

È la regola anticipata nella lezione 11 per la batteria reale, dove la resistenza interna $r$ e quella esterna $R$ erano in serie. Si noti il comportamento opposto a quello dei condensatori ([[Fisica 2 - Lezione 08 - Potenziale del disco e condensatori|lezione 8]]): per i condensatori in serie si sommano gli **inversi**, per le resistenze in serie si sommano le resistenze stesse.

## Esercizio — Una maglia con due batterie reali

> [!example] Testo (dagli appunti)
> Una maglia contiene due batterie reali, con $\varepsilon_1 = 4{,}4\ \mathrm V$, $r_1 = 2{,}3\ \Omega$ ed $\varepsilon_2 = 2{,}1\ \mathrm V$, $r_2 = 1{,}8\ \Omega$, e una resistenza $R = 5{,}5\ \Omega$. Le due batterie hanno entrambe il polo positivo verso il filo superiore, su cui si trova il punto $a$; il punto $b$ è nell'angolo in basso a sinistra. (a) Qual è la corrente nel circuito? (b) Quanto vale la differenza di potenziale $V_a - V_b$?

![[F2-L12-due-batterie.svg]]

> [!warning] Il tratto verticale nello schema degli appunti
> Nello schema degli appunti c'è un tratto verticale che scende dal filo superiore fino al punto $b$. Non può essere un filo: collegherebbe direttamente $a$ e $b$, la loro differenza di potenziale sarebbe nulla e il punto (b) non avrebbe senso. È con ogni probabilità un segno che accompagna la freccia del percorso. Nella figura l'ho omesso.

**(a) La corrente.** Le due batterie sono montate "una contro l'altra": entrambe cercano di spingere la corrente fuori dal proprio polo positivo, quindi in versi opposti lungo la maglia. Vince quella con la f.e.m. maggiore, $\varepsilon_1$: la corrente sale nel ramo di $\varepsilon_1$ e gira in senso orario. Si percorre la maglia partendo da $a$, verso destra, cioè nel verso della corrente:

- si scende attraverso $\varepsilon_2$ dal polo positivo al negativo: $-\varepsilon_2$;
- si attraversa $r_2$ nel verso della corrente: $-ir_2$;
- si attraversa $R$ nel verso della corrente: $-iR$;
- si sale attraverso $r_1$ nel verso della corrente: $-ir_1$;
- si attraversa $\varepsilon_1$ dal polo negativo al positivo: $+\varepsilon_1$.

$$
V_a - \varepsilon_2 - ir_2 - iR - ir_1 + \varepsilon_1 = V_a
\quad\Longrightarrow\quad
\varepsilon_1 - \varepsilon_2 - i\,(R + r_1 + r_2) = 0,
$$

$$
i = \frac{\varepsilon_1 - \varepsilon_2}{R + r_1 + r_2} > 0 .
$$

La corrente è positiva, quindi il verso scelto è quello giusto. Le resistenze sono tutte in serie e si sommano, e le due f.e.m. si sottraggono perché sono opposte. Con i numeri, che negli appunti non ci sono:

$$
i = \frac{4{,}4 - 2{,}1}{5{,}5 + 2{,}3 + 1{,}8}\ \mathrm A = \frac{2{,}3}{9{,}6}\ \mathrm A = 0{,}240\ \mathrm A .
$$

**(b) La differenza di potenziale tra $a$ e $b$.** Si parte da $a$ e si arriva a $b$ sommando le variazioni di potenziale lungo un percorso qualsiasi. Il potenziale è una funzione del punto ([[Fisica 2 - Lezione 07 - Potenziale elettrico|lezione 7]]), quindi ogni percorso deve dare lo stesso risultato. Negli appunti se ne fanno due.

Lungo il ramo di destra e la resistenza $R$:

$$
V_a - \varepsilon_2 - ir_2 - iR = V_b
\quad\Longrightarrow\quad
V_a - V_b = \varepsilon_2 + i\,(R + r_2) .
$$

Oppure lungo il ramo di sinistra, scendendo da $a$ a $b$. Si attraversa $\varepsilon_1$ dal polo positivo al negativo, $-\varepsilon_1$, e poi $r_1$ **contro** la corrente, che lì sale, $+ir_1$:

$$
V_a - \varepsilon_1 + ir_1 = V_b
\quad\Longrightarrow\quad
V_a - V_b = \varepsilon_1 - ir_1 .
$$

Che le due espressioni coincidano, $\varepsilon_1 - ir_1 = \varepsilon_2 + i(R + r_2)$, non è un caso: è proprio l'equazione della maglia del punto (a), riordinata. Con i numeri:

$$
V_a - V_b = 4{,}4\ \mathrm V - (0{,}240\ \mathrm A)(2{,}3\ \Omega) = 3{,}85\ \mathrm V,
\qquad
2{,}1\ \mathrm V + (0{,}240\ \mathrm A)(7{,}3\ \Omega) = 3{,}85\ \mathrm V .
$$

$V_a - V_b = \varepsilon_1 - ir_1$ è anche la tensione ai morsetti della batteria 1, minore della sua f.e.m. perché la batteria eroga corrente (lezione 11).

> [!tip] Il bilancio energetico #approfondimento
> La batteria 1 fornisce la potenza $\varepsilon_1 i = 1{,}05\ \mathrm W$. Nella batteria 2 la corrente entra dal polo positivo ed esce dal negativo: la carica viene spinta "in discesa" contro la sua f.e.m., e la batteria **assorbe** la potenza $\varepsilon_2 i = 0{,}50\ \mathrm W$. Se fosse ricaricabile, la si starebbe ricaricando. Il resto, $i^2(R + r_1 + r_2) = 0{,}55\ \mathrm W$, viene dissipato nelle resistenze per effetto Joule. Il bilancio torna: $1{,}05 = 0{,}50 + 0{,}55$.

## La legge dei nodi

La seconda legge di Kirchhoff è quella dei nodi, già usata nella [[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]]. In un nodo la carica non si accumula, quindi la corrente totale che entra è uguale a quella che esce. Nell'esempio degli appunti, con $i_1$ e $i_3$ entranti e $i_2$ uscente:

> [!important] Legge dei nodi
> $$
> i_1 + i_3 = i_2, \qquad\text{in generale}\quad \sum i_{\text{entranti}} = \sum i_{\text{uscenti}} .
> $$

> [!warning] Quale legge è la "prima"
> Negli appunti la legge dei nodi è chiamata "seconda legge di Kirchhoff". Molti testi italiani numerano al contrario: prima legge quella dei nodi, seconda quella delle maglie. Per evitare ambiguità conviene chiamarle per nome, legge dei nodi e legge delle maglie.

## Un circuito a due maglie

> [!example] Testo (dagli appunti)
> Due batterie ideali $\varepsilon_1$ ed $\varepsilon_2$ e tre resistenze $R_1$, $R_2$, $R_3$ formano il circuito della figura: $R_1$, $R_3$ e $R_2$ sono tre rami verticali tra il filo superiore e quello inferiore, ed $\varepsilon_1$, $\varepsilon_2$ stanno sul filo superiore, ai due lati del nodo $a$. Trovare le correnti.

![[F2-L12-due-maglie.svg]]

Ci sono tre rami e quindi tre correnti incognite, $i_1$ in $R_1$, $i_3$ in $R_3$ e $i_2$ in $R_2$. I versi si scelgono a piacere; negli appunti $i_1$ scende in $R_1$, $i_3$ scende in $R_3$ e $i_2$ sale in $R_2$. Servono tre equazioni indipendenti.

La prima viene dal **nodo** in basso, dove arrivano $i_1$ e $i_3$ e parte $i_2$:

$$
i_1 + i_3 = i_2 .
$$

Le altre due vengono dalla **legge delle maglie**, applicata alle due maglie. Nella maglia di sinistra si parte da $a$ e si va verso sinistra. Si attraversa $\varepsilon_1$ dal polo negativo al positivo, $+\varepsilon_1$. Si scende in $R_1$ nel verso di $i_1$, $-i_1R_1$. Si risale in $R_3$ contro $i_3$, $+i_3R_3$:

$$
V_a + \varepsilon_1 - i_1R_1 + i_3R_3 = V_a
\quad\Longrightarrow\quad
\varepsilon_1 - i_1R_1 + i_3R_3 = 0 .
$$

Nella maglia di destra si parte dallo stesso nodo, chiamato $b$, e si scende in $R_3$ nel verso di $i_3$, $-i_3R_3$. Si risale in $R_2$ nel verso di $i_2$, $-i_2R_2$. Si torna a $b$ attraversando $\varepsilon_2$ dal polo positivo al negativo, $-\varepsilon_2$:

$$
V_b - i_3R_3 - i_2R_2 - \varepsilon_2 = V_b
\quad\Longrightarrow\quad
\varepsilon_2 + i_3R_3 + i_2R_2 = 0 .
$$

Si risolve il sistema. Dalla prima equazione di maglia, $i_3 = (i_1R_1 - \varepsilon_1)/R_3$. Si sostituisce, insieme a $i_2 = i_1 + i_3$, nella seconda e si moltiplica per $R_3$:

$$
\varepsilon_2R_3 + (i_1R_1 - \varepsilon_1)(R_2 + R_3) + i_1R_2R_3 = 0 ,
$$

da cui

$$
i_1 = \frac{\varepsilon_1R_2 + \varepsilon_1R_3 - \varepsilon_2R_3}{R_1R_2 + R_1R_3 + R_2R_3} .
$$

È il risultato degli appunti, che ho verificato. Note $i_1$, si ricavano $i_3$ dalla prima equazione di maglia e $i_2 = i_1 + i_3$ dal nodo. Negli appunti non ci sono valori numerici.

> [!tip] Osservazioni sul metodo #approfondimento
> La seconda equazione di maglia, $\varepsilon_2 + i_3R_3 + i_2R_2 = 0$, ha tutti i termini con lo stesso segno, se le correnti sono positive. Quindi $i_2$ e $i_3$ non possono essere entrambe positive: almeno una scorre nel verso opposto a quello scelto, e lo rivelerà il segno meno nel risultato. Non è un errore; si sceglie un verso a caso e il calcolo corregge da solo. Si poteva scrivere anche l'equazione della maglia esterna, quella che gira intorno a tutto il circuito, ma non avrebbe aggiunto informazione: è la somma delle due maglie interne. In generale servono tante equazioni indipendenti quante sono le correnti incognite.

## Resistenze in parallelo

> [!example] Esercizio (dagli appunti)
> Una batteria ideale di f.e.m. $\varepsilon$ alimenta tre resistenze $R_1$, $R_2$, $R_3$ collegate in parallelo. Trovare le correnti e la resistenza equivalente.

![[F2-L12-parallelo.svg]]

Le tre resistenze hanno i capi collegati agli stessi due fili, quindi hanno tutte la stessa tensione, quella della batteria: è la caratteristica degli elementi **in parallelo**. Ogni corrente si ricava dalla legge di Ohm, e la corrente totale dal nodo:

$$
i_1 = \frac{\varepsilon}{R_1}, \quad i_2 = \frac{\varepsilon}{R_2}, \quad i_3 = \frac{\varepsilon}{R_3},
\qquad
i = i_1 + i_2 + i_3 = \varepsilon\left(\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}\right) = \frac{\varepsilon}{R_{\text{eq}}} .
$$

> [!important] Resistenze in parallelo
> $$
> \frac{1}{R_{\text{eq}}} = \sum_{k=1}^{n}\frac{1}{R_k} .
> $$
> In parallelo si sommano gli **inversi** delle resistenze: la tensione è la stessa e le correnti si sommano. La resistenza equivalente è sempre minore della più piccola delle resistenze, perché ogni ramo aggiunto offre alla corrente una strada in più.

Per due sole resistenze, $R_{\text{eq}} = R_1R_2/(R_1 + R_2)$, con la stessa struttura della formula dei condensatori in serie.

## Circuiti RC

Un **circuito RC** contiene una resistenza e un condensatore. A differenza dei circuiti visti finora, la corrente non è costante: varia nel tempo mentre il condensatore si carica o si scarica.

### La carica del condensatore

Il circuito è formato da una batteria di f.e.m. $\varepsilon$, un interruttore $S$, una resistenza $R$ e un condensatore $C$, inizialmente scarico. All'istante $t = 0$ si chiude l'interruttore.

![[F2-L12-circuito-rc.svg]]

Si applica la legge delle maglie partendo dal punto $a$ e seguendo la corrente. La batteria fa salire il potenziale di $\varepsilon$. La resistenza lo fa scendere di $iR$. Il condensatore, con carica $q$ in quell'istante, lo fa scendere di $q/C$, perché si va dall'armatura positiva a quella negativa:

$$
V_a + \varepsilon - iR - \frac{q}{C} = V_a
\quad\Longrightarrow\quad
\varepsilon - iR - \frac{q}{C} = 0 .
$$

Qui c'è la novità. La corrente che scorre nel circuito è quella che porta carica sul condensatore, quindi $i = dq/dt$. Sostituendo si ottiene un'equazione che contiene la carica e la sua derivata, cioè un'**equazione differenziale**:

$$
\varepsilon - R\,\frac{dq}{dt} - \frac{q}{C} = 0 .
$$

Il termine $q/C$ è la tensione ai capi del condensatore. All'inizio il condensatore è scarico, la sua tensione è nulla e tutta la f.e.m. cade sulla resistenza: la corrente è massima. Man mano che il condensatore si carica, la sua tensione cresce, sulla resistenza resta sempre meno tensione e la corrente diminuisce. Alla fine il condensatore ha ai capi tutta la f.e.m. e la corrente si ferma.

Negli appunti la soluzione è scritta e poi verificata. Si può anche ricavarla, separando le variabili. Si riscrive l'equazione come

$$
R\,\frac{dq}{dt} = \varepsilon - \frac{q}{C} = -\frac{1}{C}\,(q - C\varepsilon)
\quad\Longrightarrow\quad
\frac{dq}{q - C\varepsilon} = -\frac{dt}{RC} .
$$

Si integra da $t = 0$, con $q = 0$, a un istante generico $t$:

$$
\ln\frac{q - C\varepsilon}{-C\varepsilon} = -\frac{t}{RC}
\quad\Longrightarrow\quad
q - C\varepsilon = -C\varepsilon\,e^{-t/RC} .
$$

> [!important] Carica di un condensatore
> $$
> q(t) = C\varepsilon\left(1 - e^{-t/RC}\right),
> \qquad
> i(t) = \frac{dq}{dt} = \frac{\varepsilon}{R}\,e^{-t/RC} .
> $$

La corrente si ottiene derivando: la derivata di $-e^{-t/RC}$ è $\frac{1}{RC}e^{-t/RC}$, e $C\varepsilon\cdot\frac{1}{RC} = \frac{\varepsilon}{R}$.

Negli appunti c'è anche la **verifica**: sostituendo $q(t)$ e $i(t)$ nell'equazione della maglia,

$$
\varepsilon - R\,\frac{\varepsilon}{R}\,e^{-t/RC} - \frac1C\,C\varepsilon\left(1 - e^{-t/RC}\right)
= \varepsilon - \varepsilon\,e^{-t/RC} - \varepsilon + \varepsilon\,e^{-t/RC} = 0 . \quad\checkmark
$$

> [!warning] Due errori negli appunti
> Nella formula evidenziata degli appunti c'è $q(t) = C\varepsilon(1 - e^{t/RC})$, senza il segno meno all'esponente. Così $e^{t/RC}$ crescerebbe senza limite e la carica diventerebbe negativa e infinita. La forma corretta è $1 - e^{-t/RC}$, quella usata subito dopo negli appunti stessi per la derivata e la verifica. Inoltre gli appunti chiamano "tempo scala o tempo caratteristico" la quantità $1/RC$. Il tempo caratteristico è $RC$, che si misura in secondi; $1/RC$ ha le dimensioni dell'inverso di un tempo.

![[F2-L12-carica-rc.svg]]

> [!important] Costante di tempo
> $$
> \tau = RC .
> $$
> È il tempo caratteristico del circuito. Si misura in secondi: $\Omega\cdot\mathrm F = \dfrac{\mathrm V}{\mathrm A}\cdot\dfrac{\mathrm C}{\mathrm V} = \dfrac{\mathrm C}{\mathrm A} = \mathrm s$.

I grafici mostrano i comportamenti limite, che negli appunti sono indicati accanto alle curve:

- per $t = 0$, $e^{0} = 1$: la carica è nulla, $q(0) = 0$, e la corrente è massima, $i(0) = \varepsilon/R$, come se il condensatore fosse un filo;
- per $t \gg RC$, $e^{-t/RC}\to0$: la carica tende al valore finale $q(\infty) = C\varepsilon$ e la corrente tende a zero, come se il condensatore fosse un circuito aperto.

La costante di tempo dice quanto in fretta avviene il passaggio. Dopo un tempo $\tau$ la carica ha raggiunto $1 - e^{-1} \simeq 63\%$ del valore finale e la corrente è scesa al $37\%$ del valore iniziale. Dopo $5\tau$ la carica è al $99{,}3\%$: in pratica il condensatore è carico. Più grandi sono $R$ e $C$, più lenta è la carica. Una resistenza grande limita la corrente, e un condensatore grande ha bisogno di più carica.

> [!tip] Metà dell'energia va persa #approfondimento
> Durante la carica la batteria sposta la carica $C\varepsilon$ attraverso la f.e.m. $\varepsilon$, quindi compie il lavoro $C\varepsilon^2$. Il condensatore alla fine immagazzina $\tfrac12C\varepsilon^2$ ([[Fisica 2 - Lezione 09 - Energia dei condensatori e dielettrici|lezione 9]]). L'altra metà viene dissipata nella resistenza: $\int_0^\infty i^2R\,dt = \dfrac{\varepsilon^2}{R}\displaystyle\int_0^\infty e^{-2t/RC}\,dt = \dfrac{\varepsilon^2}{R}\cdot\dfrac{RC}{2} = \tfrac12C\varepsilon^2$. Il risultato non dipende da $R$: è la stessa perdita incontrata quando si collegano condensatori carichi, nella lezione 9.

### La scarica del condensatore

Ora il condensatore è carico, con carica $q_0$ (ad esempio $q_0 = C\varepsilon$ dopo una carica completa), e lo si fa scaricare attraverso la resistenza, senza batteria. Nella legge delle maglie manca la f.e.m. Restano la tensione del condensatore, $q/C$, e la caduta sulla resistenza, che devono compensarsi. Ora la corrente **toglie** carica al condensatore, quindi la sua intensità è $|i| = -dq/dt$, positiva perché $dq/dt < 0$. Percorrendo la maglia nel verso della corrente, il condensatore fa salire il potenziale di $q/C$ e la resistenza lo fa scendere di $|i|R$:

$$
\frac{q}{C} - |i|\,R = 0
\quad\Longrightarrow\quad
\frac{q}{C} + R\,\frac{dq}{dt} = 0
\quad\Longrightarrow\quad
R\,\frac{dq}{dt} + \frac{q}{C} = 0 .
$$

Con la stessa separazione delle variabili, da $q(0) = q_0$:

> [!important] Scarica di un condensatore
> $$
> q(t) = q_0\,e^{-t/RC},
> \qquad
> i(t) = \frac{dq}{dt} = -\frac{q_0}{RC}\,e^{-t/RC} .
> $$

Qui, come negli appunti, $i$ indica $dq/dt$. Il segno meno dice soltanto che la carica diminuisce: la corrente scorre in verso opposto a quello che aveva durante la carica. Negli appunti infatti si disegna il modulo $|i(t)|$. All'inizio $q(0) = q_0$ e la corrente ha modulo massimo, $q_0/RC$, che con $q_0 = C\varepsilon$ vale $\varepsilon/R$. Per $t\to\infty$ carica e corrente tendono a zero, con la stessa costante di tempo $RC$.

![[F2-L12-scarica-rc.svg]]

> [!warning] Segni delle due equazioni negli appunti
> Negli appunti compaiono "$-R\,dq/dt - q/C = 0$" come *equazione della carica* e "$R\,dq/dt - q/C = 0$" come *equazione della scarica*. Le etichette e i segni non tornano. L'equazione della carica contiene la f.e.m.: $\varepsilon - R\,dq/dt - q/C = 0$. L'equazione della scarica è $R\,dq/dt + q/C = 0$, che equivale alla prima riga degli appunti, $-R\,dq/dt - q/C = 0$, moltiplicata per $-1$. È questa l'equazione risolta da $q_0e^{-t/RC}$. Con "$R\,dq/dt - q/C = 0$" la soluzione sarebbe $q_0e^{+t/RC}$, una carica che cresce senza limite.

## Esercizio — Una rete di quattro resistenze

> [!example] Testo (dagli appunti)
> Nel circuito della figura $R_1 = R_2 = 20\ \Omega$, $R_3 = 30\ \Omega$, $R_4 = 8\ \Omega$ ed $\varepsilon = 12\ \mathrm V$. Trovare (a) la corrente $i$ erogata dalla batteria, (b) la corrente $i_2$ in $R_2$, (c) la corrente $i_3$ in $R_3$.

![[F2-L12-quattro-resistenze.svg]]

**(a)** $R_2$ e $R_3$ sono collegate agli stessi due nodi, quello in alto tra $R_1$ e $R_3$ e quello in basso: sono **in parallelo**.

$$
\frac{1}{R_{23}} = \frac{1}{R_2} + \frac{1}{R_3} = \frac{R_2 + R_3}{R_2R_3}
\quad\Longrightarrow\quad
R_{23} = \frac{R_2R_3}{R_2 + R_3} = \frac{20\cdot30}{50}\ \Omega = 12\ \Omega .
$$

Il blocco $R_{23}$ è poi in serie con $R_1$ e $R_4$, attraversate tutte dalla corrente della batteria:

$$
R_{\text{eq}} = R_1 + R_4 + R_{23} = (20 + 8 + 12)\ \Omega = 40\ \Omega,
\qquad
i = \frac{\varepsilon}{R_{\text{eq}}} = \frac{12}{40}\ \mathrm A = 0{,}3\ \mathrm A .
$$

**(b)** Al nodo superiore la corrente si divide: $i = i_2 + i_3$. La seconda equazione viene dalla maglia formata da $R_2$ e $R_3$, percorsa come indicato negli appunti. Si attraversa $R_3$ nel verso di $i_3$ e $R_2$ contro $i_2$:

$$
-i_3R_3 + i_2R_2 = 0 \quad\Longrightarrow\quad i_2R_2 = i_3R_3 .
$$

È la condizione di parallelo: le due resistenze hanno la stessa tensione ai capi. Si sostituisce $i_3 = i - i_2$:

$$
i_2 = \frac{R_3}{R_2}\,(i - i_2)
\quad\Longrightarrow\quad
i_2\left(1 + \frac{R_3}{R_2}\right) = \frac{R_3}{R_2}\,i
\quad\Longrightarrow\quad
i_2 = \frac{R_3}{R_2 + R_3}\,i = \frac{30}{50}\,(0{,}3\ \mathrm A) = 0{,}18\ \mathrm A .
$$

**(c)** Dal nodo:

$$
i_3 = i - i_2 = (0{,}3 - 0{,}18)\ \mathrm A = 0{,}12\ \mathrm A .
$$

Il controllo è immediato: $i_2R_2 = 0{,}18\cdot20 = 3{,}6\ \mathrm V$ e $i_3R_3 = 0{,}12\cdot30 = 3{,}6\ \mathrm V$, la stessa tensione, pari anche a $iR_{23} = 0{,}3\cdot12\ \mathrm V$.

> [!tip] Il partitore di corrente #approfondimento
> La formula $i_2 = \dfrac{R_3}{R_2 + R_3}\,i$ è il **partitore di corrente**: due resistenze in parallelo si dividono la corrente totale, e al numeratore compare la resistenza **dell'altro** ramo. La corrente preferisce la strada più facile, quindi la resistenza più piccola porta la corrente maggiore. La struttura è la stessa del partitore capacitivo della [[Fisica 2 - Lezione 11 - Forza elettromotrice e legge delle maglie|lezione 11]], $V_1 = \dfrac{C_2}{C_1 + C_2}V$.

> [!warning] Sezione ricostruita — fine
