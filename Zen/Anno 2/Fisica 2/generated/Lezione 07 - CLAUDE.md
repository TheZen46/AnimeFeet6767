---
corso: Fisica 2
lezione: 7
data: 2026-10-13
argomenti: [energia potenziale elettrica, potenziale elettrico, volt, forza conservativa, superfici equipotenziali, relazione tra campo e potenziale, gradiente, potenziale di una carica puntiforme, sovrapposizione dei potenziali, potenziale di distribuzioni continue, potenziale di un filo]
bibliography: fisica2.bib
tags: [fisica2]
---

# Lezione 7 — Energia potenziale e potenziale elettrico

Finora l'elettrostatica è stata descritta con forze e campi, cioè con grandezze vettoriali. Questa lezione introduce una descrizione equivalente basata sull'energia: l'**energia potenziale elettrica** e il **potenziale elettrico**. Il potenziale è uno scalare, e in molti problemi è più semplice da trattare del campo. Si dimostra che la forza di Coulomb è conservativa, si introducono le superfici equipotenziali e si ricava il legame tra potenziale e campo nei due versi, con un integrale e con il gradiente. Infine si calcolano i potenziali di una carica puntiforme, di sistemi di cariche e di un filo carico. Le convenzioni di colore delle figure sono quelle indicate nella [[Fisica 2 - Lezione 05 - Teorema di Gauss|lezione 5]].

## Perché l'energia potenziale

Il docente parte dall'analogia con la gravità, nota da Fisica 1. Un corpo sulla cima di una collina ha un'energia potenziale maggiore di quando si trova a valle: lo si sa senza fare calcoli. Per riportarlo in cima bisogna compiere un lavoro. Quando le forze in gioco sono di questo tipo, come la gravità o la forza elettrica, l'energia meccanica si conserva:

$$
K_i + U_i = K_f + U_f ,
$$

dove $K$ è l'energia cinetica e $U$ l'energia potenziale. Questo vale se il sistema è chiuso, cioè senza forze esterne. La conservazione permette di capire come evolve un sistema senza risolvere l'equazione di Newton, che spesso è difficile. L'energia potenziale elettrostatica e il potenziale elettrico offrono lo stesso vantaggio per i fenomeni elettrici.

## Energia potenziale elettrica

### Definizione

Si sposta una carica lungo una traiettoria $\gamma$ da un punto iniziale $i$ a un punto finale $f$, in presenza di un campo elettrico, che esercita sulla carica una forza $\vec F$. La variazione di energia potenziale è l'opposto del lavoro compiuto da quella forza:

$$
\Delta U = U_f - U_i = -W, \qquad W = \int_i^f \vec F\cdot d\vec s .
$$

Lo spostamento infinitesimo $d\vec s$ è sempre **tangente** alla traiettoria. Istante per istante si calcola il prodotto scalare tra forza e spostamento, poi si sommano tutti i contributi. È la definizione di lavoro di Fisica 1, applicata alla forza elettrica.

![[F2-L07-lavoro-traiettoria.svg]]

> [!warning] Quale lavoro?
> A lezione si parla a volte del "lavoro che facciamo per spostare il corpo". Nella relazione $\Delta U = -W$, $W$ è il lavoro compiuto dalla **forza del campo**. Il lavoro di un operatore esterno che sposta lentamente la carica, senza darle energia cinetica, è l'opposto: $W_{\text{est}} = +\Delta U$. Con questa lettura tutti i segni della lezione, e degli appunti, tornano.

### Lo zero dell'energia

Come tutte le energie, anche l'energia potenziale è definita a meno di una costante: in fisica conta solo la **variazione** di energia, non il suo valore assoluto. Si sceglie quindi un punto di riferimento in cui l'energia potenziale vale zero. Se il punto iniziale è il riferimento, $U_i = 0$ e $U = U_f$. Come per la pallina sulla collina, lo zero si può mettere dove si vuole, a valle o in cima: quello che conta è il lavoro compiuto, cioè la variazione.

In elettrostatica la convenzione tipica è porre **$U = 0$ all'infinito**. Si immagina una carica di prova $q_0$ a distanza infinita dalle cariche che generano il campo, e la si porta in un punto generico dello spazio. La scelta nasce dalla legge di Coulomb. La forza va come $1/r^2$, quindi si annulla quando le cariche sono infinitamente lontane: all'infinito le cariche non "si sentono".

### Il segno del lavoro dipende dalla carica

Il lavoro dipende dal segno della carica che si sposta. A parità di campo e di spostamento, con una carica positiva la forza ha il verso del campo, con una carica negativa ha verso opposto. Se lo spostamento è opposto al campo, per $q_0 > 0$ si ha $\vec F\cdot d\vec s < 0$ e il lavoro è negativo. Per $q_0 < 0$ la forza è concorde con lo spostamento e il lavoro è positivo. La definizione non cambia, è sempre l'integrale di forza per spostamento, ma bisogna fare attenzione al segno della carica, perché da esso dipende se l'energia aumenta o diminuisce.

## Il potenziale elettrico

L'energia potenziale e il lavoro dipendono dalla carica di prova: con $q_0$ diverse si ottengono lavori diversi. Come per il campo elettrico, che si ottiene dividendo la forza di Coulomb per la carica di prova, si definisce una grandezza che non dipende da $q_0$: il lavoro per unità di carica.

> [!important] Potenziale elettrico
> $$
> V = \frac{U}{q_0}, \qquad \Delta V = \frac{\Delta U}{q_0} = -\frac{W}{q_0}
> $$
> Il potenziale è definito in ogni punto dello spazio e non dipende dalla carica di prova. La sua unità è il **volt**: $1\ \mathrm V = 1\ \mathrm J/\mathrm C$.

Un volt corrisponde a un joule di energia necessario per spostare una carica di un coulomb. L'analogia è precisa: l'energia potenziale sta al potenziale come la forza di Coulomb sta al campo elettrico. Noto il campo in un punto, si conosce la forza su qualsiasi carica posta lì. Noto il potenziale, si conosce l'energia potenziale di qualsiasi carica.

C'è però una differenza importante. Il potenziale, essendo un lavoro per unità di carica, è uno **scalare**. Forze e campi sono vettori, e nei calcoli bisogna sempre specificarne modulo, direzione e verso. Il potenziale contiene informazioni analoghe, ma con proprietà scalari, e questo a volte semplifica molto la trattazione.

## La forza di Coulomb è conservativa

La proprietà più interessante del potenziale elettrostatico è che deriva da una forza **conservativa**: il lavoro per spostare una carica da $A$ a $B$ non dipende dalla traiettoria, ma solo dai punti iniziale e finale. È esattamente quello che accade con l'energia gravitazionale, in assenza di forze dissipative. La conseguenza pratica è enorme: per calcolare un lavoro o un'energia non serve sapere quale percorso si segue.

Il docente lo dimostra per la forza tra una carica $q$ ferma e una carica $q_0$ che si sposta da $A$ a $B$, confrontando due percorsi.

**Percorso 1: radiale.** $A$ e $B$ stanno sulla stessa semiretta uscente da $q$, e si va lungo la congiungente. La forza di Coulomb è radiale, quindi parallela allo spostamento, e il prodotto scalare è semplicemente il prodotto dei moduli, con $ds = dr$:

$$
dW = \vec F\cdot d\vec s = k\,\frac{q q_0}{r^2}\,dr
\quad\Longrightarrow\quad
W = kqq_0\int_{r_A}^{r_B}\frac{dr}{r^2} = -kqq_0\left[\frac1r\right]_{r_A}^{r_B} = kqq_0\left(\frac{1}{r_A} - \frac{1}{r_B}\right).
$$

**Percorso 2: generico.** Lo spostamento lungo una curva qualsiasi si può approssimare con una successione di piccoli tratti radiali e piccoli archi di circonferenza centrati in $q$, come in una scalinata. È lo stesso trucco usato in meccanica per la forza peso. Sugli archi lo spostamento è perpendicolare alla forza, che è radiale, quindi il loro contributo è nullo. Restano solo i tratti radiali, che messi insieme percorrono la stessa variazione di distanza del percorso 1. L'integrale è lineare, quindi

$$
\int_{A\,(2)}^{B}\vec F\cdot d\vec s = \int_{\text{tratti radiali}}\vec F\cdot d\vec r = kqq_0\left(\frac{1}{r_A} - \frac{1}{r_B}\right),
$$

identico al percorso 1.

![[F2-L07-forza-conservativa.svg]]

Il campo elettrostatico è quindi conservativo, e gli si può associare un potenziale. Per il principio di sovrapposizione, il risultato si estende al campo di qualsiasi distribuzione di cariche ferme. Il lavoro per spostare una carica dipende solo dai punti iniziale e finale.

> [!tip] Approfondimento — Lavoro su un percorso chiuso #approfondimento
> Una formulazione equivalente: il lavoro del campo elettrostatico lungo **qualsiasi percorso chiuso** è nullo, $\oint \vec E\cdot d\vec s = 0$. Basta spezzare il giro chiuso in un'andata da $A$ a $B$ e un ritorno da $B$ ad $A$ lungo un'altra strada: i due lavori sono uguali e opposti. Questa proprietà distingue il campo elettrostatico dal campo elettrico indotto da campi magnetici variabili, che si incontrerà con la legge di Faraday.

## Superfici equipotenziali

Poiché il potenziale è definito in tutto lo spazio, si possono definire le **superfici equipotenziali**: le superfici su cui il potenziale ha lo stesso valore in ogni punto. Nello spazio ci saranno una superficie con potenziale $V_1$, un'altra con $V_2$, un'altra ancora con $V_3$, e così via. La loro forma dipende dalle cariche che generano il campo: ogni configurazione produce superfici diverse, anche complicate a piacere.

Le superfici equipotenziali danno un'idea immediata del lavoro, senza calcoli.

- **Spostarsi su una superficie equipotenziale non richiede lavoro.** Se $A$ e $B$ stanno sulla stessa superficie, $V_B - V_A = 0$, e quindi $W = -q_0\,\Delta V = 0$.
- **Il percorso non conta.** Anche se si parte da $A$, si esce dalla superficie passando per quella con potenziale $V_2$ e si torna in $B$, il lavoro totale è zero, perché il campo è conservativo.
- **Il punto di arrivo su una superficie non conta.** Il lavoro per passare dalla superficie $V_1$ alla superficie $V_3$ è $-q_0(V_3 - V_1)$, qualunque sia il punto di arrivo su $V_3$: tutti i punti di $V_3$ hanno lo stesso potenziale.

![[F2-L07-superfici-equipotenziali.svg]]

Non sempre è facile visualizzarle, ma a volte ragionare in termini di superfici equipotenziali semplifica molto i problemi.

> [!tip] Approfondimento — Equipotenziali e linee di campo #approfondimento
> Le superfici equipotenziali sono sempre **perpendicolari** alle linee di campo. Se il campo avesse una componente lungo la superficie, spostandosi su di essa si compirebbe lavoro, contro la definizione di superficie equipotenziale. Per una carica puntiforme le equipotenziali sono sfere concentriche, attraversate radialmente dalle linee di campo. Inoltre, come si vedrà con il gradiente, il campo punta verso i potenziali **decrescenti**.

## Il legame tra potenziale e campo elettrico

### Dal campo al potenziale

Il lavoro si può scrivere in due modi. Da una parte, con la forza $\vec F = q\vec E$: $W = q\int\vec E\cdot d\vec s$. Dall'altra, dalla definizione di potenziale: $W = -q\,\Delta V$. Uguagliando, la carica si semplifica:

> [!important] Potenziale dal campo
> $$
> \Delta V = V_f - V_i = -\int_i^f \vec E\cdot d\vec s
> $$
> L'integrale si calcola lungo una traiettoria qualsiasi da $i$ a $f$, perché il campo è conservativo.

Dato il campo elettrico, si ricava il potenziale. Tutta l'elettrostatica è stata costruita sul campo elettrico, ma grazie a questa relazione si può descrivere anche in termini di potenziale: sono descrizioni equivalenti.

### Dal potenziale al campo: il gradiente

Spesso conviene fare il contrario, cioè ricavare il campo dal potenziale. Invertire un integrale richiede le derivate. Poiché il potenziale è una funzione di più variabili, $V(x,y,z)$, servono le **derivate parziali**, che insieme formano il **gradiente**. Il docente ne dà una giustificazione intuitiva, rimandando a Metodi Matematici per la trattazione rigorosa. Il prodotto scalare tra $\vec E$ e lo spostamento infinitesimo $d\vec s = (dx, dy, dz)$ è

$$
dV = -\vec E\cdot d\vec s = -\left(E_x\,dx + E_y\,dy + E_z\,dz\right).
$$

Muovendosi solo lungo $x$, la variazione del potenziale per unità di spostamento è la derivata parziale rispetto a $x$: $\partial V/\partial x = -E_x$. Lo stesso vale per $y$ e per $z$.

> [!important] Campo dal potenziale
> $$
> \vec E = -\nabla V = -\left(\frac{\partial V}{\partial x},\ \frac{\partial V}{\partial y},\ \frac{\partial V}{\partial z}\right)
> $$
> Dato $V$ in tutto lo spazio, se ne calcolano le derivate rispetto a $x$, $y$ e $z$ e si costruisce il vettore campo elettrico. Tra $V$ ed $\vec E$ c'è una corrispondenza biunivoca.

## Potenziale di una carica puntiforme

Si calcola il potenziale generato da una carica puntiforme positiva $q$ in un punto $P$ a distanza $R$. Si usa la relazione integrale con un percorso radiale da $P$ all'infinito, dove il potenziale è zero per convenzione. Lungo il percorso il campo è radiale e uscente, concorde con lo spostamento $d\vec r$:

$$
V(\infty) - V(R) = -\int_R^{\infty}\vec E\cdot d\vec r = -\int_R^{\infty}\frac{kq}{r^2}\,dr = -kq\left[-\frac1r\right]_R^{\infty} = -\frac{kq}{R}.
$$

Per $r \to \infty$ il termine $1/r$ si annulla, e resta solo il contributo in $R$. Con $V(\infty) = 0$:

> [!important] Potenziale di una carica puntiforme
> $$
> V(R) = k\,\frac{q}{R} = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{R}
> $$
> con lo zero all'infinito. Il potenziale ha il segno della carica: positivo per $q>0$, negativo per $q<0$.

### Più cariche: sovrapposizione

I campi elettrici godono del principio di sovrapposizione, quindi anche i potenziali. Il potenziale di $n$ cariche in un punto è la somma dei potenziali delle singole cariche:

$$
V = \sum_{i=1}^{n} V_i = k\sum_{i=1}^{n}\frac{q_i}{r_i},
$$

dove $r_i$ è la distanza della carica $i$-esima dal punto. La somma è di **scalari**, con il segno delle cariche: niente direzioni né versi.

![[F2-L07-potenziale-carica-puntiforme.svg]]

### Esempio: quattro cariche ai vertici di un quadrato

> [!example] Esempio
> Quattro cariche $q_1, q_2, q_3, q_4$ si trovano ai vertici di un quadrato di lato $d$. Calcolare il potenziale nel centro $P$.
>
> Tutte le cariche sono alla stessa distanza dal centro, pari a metà diagonale. Dal triangolo rettangolo con cateti $d/2$ e $d/2$:
> $$
> r^2 = \frac{d^2}{4} + \frac{d^2}{4} = \frac{d^2}{2} \quad\Longrightarrow\quad r = \frac{d}{\sqrt2}.
> $$
> Quindi
> $$
> V(P) = k\left(\frac{q_1}{r} + \frac{q_2}{r} + \frac{q_3}{r} + \frac{q_4}{r}\right) = \frac{\sqrt2\,k}{d}\left(q_1 + q_2 + q_3 + q_4\right).
> $$

Il docente insiste sul confronto con il campo elettrico. L'espressione del potenziale vale **sempre**, con cariche positive, negative, uguali o diverse: basta sommarle con il loro segno. Per il campo, invece, ogni carica dà un vettore con la propria direzione e la propria intensità. Bisogna sommarli vettorialmente, e il risultato può avere qualsiasi direzione e modulo. L'esempio è ancora più evidente con sei cariche disposte su una circonferenza di raggio $R$ attorno a $P$. Il potenziale nel centro è $V = (k/R)\sum q_i$ qualunque sia la disposizione delle cariche sulla circonferenza, mentre il campo dipende in modo complicato dalla disposizione.

![[F2-L07-cariche-quadrato.svg]]

In generale, nessuna delle due descrizioni è sempre migliore. Per i problemi legati all'energia, il potenziale è tipicamente più comodo: permette di passare all'energia potenziale e di calcolare il lavoro in modo immediato, ad esempio come differenza tra due superfici equipotenziali. In altri casi conviene il campo.

## Potenziale di distribuzioni continue

Per una distribuzione continua si procede come per il campo: si suddivide il corpo in elementi così piccoli da poterli trattare come cariche puntiformi, si scrive il potenziale di ciascuno e si integra:

$$
dV = k\,\frac{dq}{r} \quad\Longrightarrow\quad V = \int k\,\frac{dq}{r},
$$

dove $r$ è la distanza dell'elemento dal punto. Rispetto al campo c'è un vantaggio: l'integrale è di scalari, quindi non serve scomporre in componenti né ragionare sulle simmetrie per capire quali componenti si cancellano.

### Esempio: filo carico di lunghezza $L$

> [!example] Esempio
> Un filo rettilineo di lunghezza $L$ è carico uniformemente con densità lineare $\lambda$. Calcolare il potenziale nel punto $P$ che si trova a distanza $d$ da un estremo del filo, sulla perpendicolare al filo passante per quell'estremo.
>
> Si mette l'origine nell'estremo del filo sotto $P$ e l'asse $x$ lungo il filo. Un elemento di lunghezza $dx$ a distanza $x$ dall'origine porta la carica $dq = \lambda\,dx$, e la sua distanza da $P$ si ricava dal triangolo rettangolo di cateti $x$ e $d$: $r = \sqrt{x^2 + d^2}$. Quindi
> $$
> dV = k\,\frac{\lambda\,dx}{\sqrt{x^2+d^2}} .
> $$
> L'integrale è noto: $\int\frac{dx}{\sqrt{x^2+d^2}} = \ln\left(x + \sqrt{x^2+d^2}\right)$. Integrando da $0$ a $L$:
> $$
> V = k\lambda\left[\ln\left(L + \sqrt{L^2+d^2}\right) - \ln d\right] = k\lambda\,\ln\frac{L + \sqrt{L^2+d^2}}{d}.
> $$

![[F2-L07-potenziale-filo.svg]]

Il docente lo presenta come uno di quei calcoli che si fanno una volta e poi si ricordano. Il messaggio generale è che in qualsiasi situazione si discretizza il corpo, si calcola il potenziale dell'elemento infinitesimo e si integra. Il più delle volte l'integrale non si sa fare analiticamente, ma in alcuni casi si arriva fino in fondo.

> [!tip] Approfondimento — Verifica della primitiva e filo molto lungo #approfondimento
> Derivando $\ln\left(x + \sqrt{x^2+d^2}\right)$ si ottiene
> $$
> \frac{1 + \frac{x}{\sqrt{x^2+d^2}}}{x + \sqrt{x^2+d^2}} = \frac{1}{\sqrt{x^2+d^2}},
> $$
> come deve essere. Per un filo molto lungo, $L \gg d$, il risultato diventa $V \simeq k\lambda\ln(2L/d)$, che **diverge** per $L\to\infty$. Per un filo infinito, quindi, non si può mettere lo zero del potenziale all'infinito. Si fissa lo zero a una distanza di riferimento finita e si calcolano solo differenze di potenziale, ad esempio dal campo $\lambda/(2\pi\varepsilon_0 r)$ della lezione 6.
