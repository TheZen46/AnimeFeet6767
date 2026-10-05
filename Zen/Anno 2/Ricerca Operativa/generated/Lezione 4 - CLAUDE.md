---

## corso: Ricerca Operativa lezione: 4 data: 2026-10-02 docente: Silvia Villa argomenti: [rette in forma parametrica, semirette, segmenti, insiemi convessi, intersezione di convessi, iperpiani, semispazi, poliedri, politopi, vertici, vincoli attivi, caratterizzazione dei vertici, rango, numero di vertici] fonti: [trascrizione, appunti manuali, dispense] tags: [ricerca-operativa, lezione]
---
# Lezione 4 — Convessità, poliedri e vertici

Questa lezione studia gli **aspetti geometrici** di un problema di programmazione lineare. Alcune cose sono già state viste nella [[Lezione 03 - Miscelazione, trasporto e risoluzione grafica|lezione 3]], ma la docente le riprende perché verranno usate moltissimo: in particolare la nozione di poliedro e quella di vertice saranno centrali per le prossime 7–8 lezioni, cioè per tutto lo studio del metodo del simplesso.

## Rette, semirette e segmenti in forma parametrica

Nella lezione precedente le rette sono state scritte con un'**equazione cartesiana**, $a_1x_1 + a_2x_2 = b$. C'è un altro modo di descriverle, la forma **parametrica**, che compare soprattutto nelle dimostrazioni e ricorda che certi insiemi sono rette.

Si fissano un punto $x_0 \in \mathbb{R}^n$ e una **direzione non nulla** $v \in \mathbb{R}^n$, $v \neq 0$. Nel disegno si è in $\mathbb{R}^2$, quindi $x_0$ ha due coordinate; la docente avverte che sugli assi non ci sono $x$ e $y$ ma $x_1$ e $x_2$. I punti della **retta** passante per $x_0$ con direzione $v$ sono quelli che si ottengono partendo da $x_0$ e aggiungendo un multiplo qualunque di $v$:

$$ { x \in \mathbb{R}^n \mid x = x_0 + t,v,\ t \in \mathbb{R} ,}. $$

Il parametro $t$ può essere positivo, negativo o nullo: con $t > 0$ ci si muove da una parte di $x_0$, con $t < 0$ dall'altra. Un punto della retta si scrive per esempio come $x_0 + \tfrac32 v$ oppure $x_0 - \tfrac32 v$.

Se si chiede invece $t \ge 0$, da $x_0$ ci si può muovere solo nel verso di $v$, e si ottiene una **semiretta** con origine in $x_0$:

$$ { x \in \mathbb{R}^n \mid x = x_0 + t,v,\ t \ge 0 ,}. $$

Infine, dati due punti $x_0, z \in \mathbb{R}^n$, l'insieme

$$ { x \in \mathbb{R}^n \mid x = (1 - t),x_0 + t,z,\ t \in [0, 1] ,} $$

è il **segmento** che unisce $x_0$ e $z$. Lo si riconosce riscrivendolo nella forma di prima:

$$ (1 - t),x_0 + t\cdot z = x_0 + t\cdot(z - x_0). $$

È ancora "punto più $t$ volte un vettore", con direzione $v = z - x_0$, il vettore che va da $x_0$ a $z$. Poiché $t$ è non negativo ci si muove verso $z$; poiché $t \le 1$ non si va oltre $z$. Per $t = 0$ si ottiene $x_0$, per $t = 1$ si ottiene $z$, e in mezzo tutti i punti fra i due. La scrittura $(1-t)x_0 + tz$ si chiama **combinazione convessa** di $x_0$ e $z$; la docente trova più naturale l'altra, $x_0 + t(z - x_0)$.

|oggetto|parametrizzazione|parametro|
|---|---|---|
|retta|$x_0 + t,v$, $v \neq 0$|$t \in \mathbb{R}$|
|semiretta|$x_0 + t,v$, $v \neq 0$|$t \ge 0$|
|segmento $[x_0, z]$|$x_0 + t,(z - x_0) = (1-t),x_0 + t,z$|$t \in [0, 1]$|

I tre oggetti hanno la stessa forma: cambia solo l'insieme in cui varia il coefficiente. Hanno anche la stessa **dimensione**. Fissati $x_0$ e $v$ (o $z$), l'unico parametro libero è il numero reale $t$, quindi ci si può muovere solo in uno spazio di dimensione 1, anche se $x_0$ e $v$ stanno in $\mathbb{R}^n$. In generale, la dimensione di un oggetto descritto da parametri liberi è il numero di quei parametri.

## Insiemi convessi

Nei problemi di ottimizzazione la **convessità** gioca un ruolo fondamentale.

> [!important] Definizione — insieme convesso Un insieme $C \subseteq \mathbb{R}^n$ si dice **convesso** se $$ \forall, x, z \in C,\ \forall, t \in [0, 1]: \qquad (1 - t),x + t,z \in C . $$ In parole: comunque si prendano due punti dell'insieme, il **segmento** che li unisce sta tutto nell'insieme.

Prima di dare la definizione la docente ha disegnato un insieme con una "rientranza" e ha chiesto per alzata di mano se fosse convesso: la maggioranza ha risposto correttamente di no. Prendendo due punti dell'insieme ai lati della rientranza, il segmento che li unisce esce dall'insieme, e questo la convessità lo vieta. Un insieme convesso è invece "rotondo", "bombato": non ha rientranze, e contiene tutti i segmenti che uniscono coppie dei suoi punti. Basta un solo segmento che esce per rendere un insieme non convesso, mentre per la convessità la condizione deve valere per **ogni** coppia di punti.

La definizione è molto semplice e visibile dal punto di vista geometrico, ma **difficile da verificare**: in generale bisognerebbe prendere due punti qualsiasi e mostrare che il segmento sta sempre dentro. Guardando un disegno si "vede" che è vero per tutti i segmenti, ma una verifica matematica è un'altra cosa. Per questo sono utili le **operazioni che preservano la convessità**: si parte da insiemi semplici che si sa essere convessi, si fanno operazioni su di essi e la convessità si mantiene "gratis".

> [!important] Proposizione — intersezione di convessi Se $C_1$ e $C_2$ sono convessi, allora $C_1 \cap C_2$ è convesso. Più in generale, se $(C_i)_{i \in I}$ è una famiglia qualsiasi di insiemi convessi, allora $\bigcap_{i \in I} C_i$ è convesso.

_Dimostrazione._ Bisogna mostrare che per ogni $x, z \in C_1 \cap C_2$ e per ogni $t \in [0,1]$ il punto $(1-t)x + tz$ sta in $C_1 \cap C_2$, cioè sia in $C_1$ sia in $C_2$.

- $x, z \in C_1$ e $C_1$ è convesso, quindi $(1-t)x + tz \in C_1$.
- $x, z \in C_2$ e $C_2$ è convesso, quindi $(1-t)x + tz \in C_2$.

Il punto sta in entrambi, quindi nell'intersezione. $\square$

La stessa dimostrazione funziona per un numero arbitrario di insiemi: tre, quattro, infiniti, anche non numerabili. Nel corso si useranno soprattutto intersezioni di un **numero finito** di convessi (dispense, Teorema 5.1.1 e Corollario 5.1.7 [@roma2023]).

## Iperpiani

Si passa ora ai convessi che interessano davvero. Dati $a \in \mathbb{R}^n$ e $b \in \mathbb{R}$, si considera

$$ H = {, x \in \mathbb{R}^n \mid a^T x = b ,}. $$

**Caso degenere, $a = 0$.** Allora $a^T x = 0$ per ogni $x$. Quindi $H = \mathbb{R}^n$ se $b = 0$, oppure $H = \varnothing$ se $b \neq 0$. Non è un caso interessante, ma entrambi gli insiemi sono convessi: $\mathbb{R}^n$ contiene ogni segmento, e nell'insieme vuoto non ci sono punti, quindi non c'è nulla da verificare.

**Caso $a \neq 0$.** $H$ è l'insieme delle soluzioni di **un'equazione lineare** in $n$ incognite con coefficienti non tutti nulli. Se $b = 0$ è un **sottospazio vettoriale** di $\mathbb{R}^n$ di dimensione $n - 1$: ci sono $n$ incognite e un'equazione, quindi $n - 1$ parametri liberi. Se $b \neq 0$ non è un sottospazio, ma il sottospazio precedente **traslato** (un sottospazio affine). In entrambi i casi $H$ si chiama **iperpiano**.

- Per $n = 2$: $H = {(x_1, x_2) \mid a_1x_1 + a_2x_2 = b}$ ha dimensione $2 - 1 = 1$, cioè è una **retta**, scritta con l'equazione cartesiana.
- Per $n = 3$: $H = {(x_1, x_2, x_3) \mid a_1x_1 + a_2x_2 + a_3x_3 = b}$ ha dimensione 2, cioè è un **piano**.

Come per le rette, anche per i piani (e in generale per gli iperpiani) il vettore dei coefficienti $a = (a_1, a_2, a_3)$ è **perpendicolare** a $H$.

> [!important] Proposizione — gli iperpiani sono convessi $H = { x \in \mathbb{R}^n \mid a^T x = b }$ è un insieme convesso.

_Dimostrazione._ Si usa la definizione, l'unico strumento disponibile. Siano $x, z \in H$ e $t \in [0, 1]$; bisogna mostrare che $(1-t)x + tz \in H$, cioè che soddisfa l'equazione che definisce $H$. Il prodotto scalare è bilineare: si distribuisce rispetto alla somma e gli scalari ($1-t$ e $t$ sono numeri, non vettori) si portano fuori. Quindi

$$ a^T\big((1-t),x + t,z\big) = (1-t),a^T x + t,a^T z = (1-t),b + t,b = b , $$

dove si è usato $a^T x = b$ e $a^T z = b$, perché $x, z \in H$. $\square$

È un fatto quasi ovvio, perché un iperpiano è un insieme "piatto": se si prendono due punti su un piano e li si unisce con un segmento, il segmento sta nel piano.

## Semispazi

Un iperpiano divide lo spazio in due parti. In $\mathbb{R}^2$ una retta divide il piano in una parte "sopra" e una "sotto"; lo stesso fa un piano in $\mathbb{R}^3$. Queste due parti si chiamano **semispazi** (in $\mathbb{R}^2$, semipiani):

$$ H^+ = {, x \in \mathbb{R}^n \mid a^T x \ge b ,}, \qquad H^- = {, x \in \mathbb{R}^n \mid a^T x \le b ,}. $$

Come visto nella lezione 3, il vettore $a$ punta verso $H^+$. Poiché contengono l'iperpiano $H$, questi si dicono **semispazi chiusi**. Se si usa la disuguaglianza stretta ($a^T x > b$) si ottiene un **semispazio aperto**: la docente lo ha precisato rispondendo a una domanda.

> [!important] Proposizione — i semispazi chiusi sono convessi $H^+$ e $H^-$ sono insiemi convessi.

A lezione la dimostrazione non è stata scritta: "è proprio uguale a prima, bisogna solo rimpiazzare l'uguale con il maggiore uguale". Vale la pena scriverla, perché c'è un dettaglio che conta. Per $x, z \in H^+$ e $t \in [0,1]$:

$$ a^T\big((1-t),x + t,z\big) = (1-t),a^T x + t,a^T z ;\ge; (1-t),b + t,b = b . $$

La disuguaglianza si conserva perché $1 - t \ge 0$ e $t \ge 0$: moltiplicare entrambi i membri di $a^T x \ge b$ per un numero **non negativo** non ne cambia il verso. È qui che serve $t \in [0,1]$ [@roma2023, Teorema 5.1.2]. Per $H^-$ il ragionamento è identico.

Nel corso si useranno semispazi chiusi con "$\ge$", per i motivi di esistenza della soluzione discussi nella lezione 2. La convessità però vale con entrambi i versi della disuguaglianza.

Ricapitolando questa prima parte: si è introdotta la convessità e si è visto che **iperpiani** e **semispazi** sono insiemi convessi.

## Poliedri

> [!important] Definizione — poliedro e politopo Un **poliedro** è l'intersezione di un numero **finito** di semispazi chiusi (ed eventualmente iperpiani). Un poliedro **limitato** si chiama **politopo**.

L'aggiunta "ed eventualmente iperpiani" non cambia nulla. Ogni iperpiano è l'intersezione dei suoi due semispazi chiusi,

$$ H = H^+ \cap H^- , $$

cioè un vincolo di uguaglianza equivale a due vincoli di disuguaglianza, come visto nella lezione 2. Includere gli iperpiani nella definizione è quindi ridondante, ma comodo.

La docente ha disegnato tre esempi in $\mathbb{R}^2$:

1. l'intersezione di **quattro** semipiani $H_1^+, \dots, H_4^+$, che dà un quadrilatero: il poliedro "classico", con i lati e una parte interna;
2. l'intersezione di **tre** semipiani che dà una regione **illimitata**. Uno studente ha chiesto perché fosse un poliedro: lo è perché è l'intersezione di un numero finito di semispazi chiusi, e la definizione non richiede la limitatezza. Probabilmente il dubbio veniva proprio dal fatto che non è limitato, e questo infatti non è un politopo;
3. un poliedro intersecato con un iperpiano (una retta), che dà un **segmento**: una versione "degenere", senza parte interna. È comunque un poliedro, e anche un politopo, perché è limitato.

Le dispense aggiungono che anche l'insieme vuoto e tutto $\mathbb{R}^n$ sono poliedri [@roma2023, §5.1.2].

> [!important] Osservazioni — poliedri e programmazione lineare
> 
> 1. **Un poliedro è convesso**, perché è l'intersezione di un numero finito di insiemi convessi (i semispazi). Non serve dimostrarlo ogni volta: segue dai risultati precedenti.
> 2. Un problema generico di programmazione lineare si scrive, come visto nella lezione 2, $$ \min\ c^T x \qquad \text{s.t.} \quad A x \ge b, \qquad A \in \mathbb{R}^{m \times n},\ x \in \mathbb{R}^n,\ b \in \mathbb{R}^m . $$ La disuguaglianza $Ax \ge b$ vale componente per componente: ogni riga $a_i^T x \ge b_i$ è un semispazio chiuso. L'insieme ammissibile $$ P = {, x \in \mathbb{R}^n \mid A x \ge b ,} $$ è quindi l'intersezione di $m$ semispazi chiusi: **è un poliedro, ed è convesso**. Da qui in poi l'insieme ammissibile, finora chiamato $S$, si chiamerà $P$, proprio per ricordare che è un poliedro.
> 3. Vale anche il viceversa: **ogni poliedro si scrive nella forma** ${x \mid Ax \ge b}$. I vincoli con "$\le$" si trasformano cambiando segno, e quelli di uguaglianza si sdoppiano in due disuguaglianze. Scrivere i poliedri così non è restrittivo.

## Dalla geometria all'algebra

"A me la geometria piace perché si vede", dice la docente: è bello fare disegni e capire le cose guardandoli, almeno nei casi facili. Ma un calcolatore non "vede" come noi, e ragionare sui disegni non è il modo computazionalmente giusto di trattare questi oggetti. Il lavoro delle prossime lezioni è tradurre la geometria in **algebra**. Un poliedro non va pensato come un esagono o un ottagono, ma come un insieme di vettori che verificano $m$ disuguaglianze algebriche lineari. Lo stesso va fatto per i **vertici**: prima se ne dà una definizione geometrica, per capire che cosa significano, e poi la si **caratterizza algebricamente**.

## Vertici

In un poliedro "da bambini", un vertice è un punto in cui si incontrano due lati. Un modo di vederlo è questo: un vertice non può stare **all'interno** di un segmento contenuto nel poliedro. Se si prende un segmento del poliedro che contiene il vertice, il vertice deve esserne un estremo.

> [!important] Definizione — vertice Sia $P$ un poliedro. Un punto $x \in P$ è un **vertice** di $P$ se **non esistono** $x_1, x_2 \in P$ tali che $x$ appartenga al segmento che congiunge $x_1$ e $x_2$ e sia $x \neq x_1$, $x \neq x_2$.

Un punto interno al poliedro sta nel mezzo di tanti segmenti, e così anche un punto interno a un lato (basta prendere un segmento lungo il lato). Un vertice invece no. È la formalizzazione dell'idea anticipata dal prof. Molinari nella lezione 3: un vertice non si può ottenere "combinando" altri due punti dell'insieme, dove "combinare" va inteso come combinazione convessa.

> [!tip] Approfondimento — Vertice o punto estremo? #approfondimento Le dispense [@roma2023, Def. 5.1.12 e nota 2] precisano un dettaglio terminologico. Nella letteratura la definizione data qui è propriamente quella di **punto estremo** di un insieme convesso, mentre "vertice" indica di solito una proprietà più complessa. Per i **poliedri**, gli unici insiemi convessi considerati nel corso, le due nozioni coincidono: un punto di un poliedro è un vertice se e solo se è un punto estremo. Nei testi si troveranno quindi entrambi i termini.

Questa definizione è "carina perché geometrica", ma non è utilizzabile in pratica: non si possono controllare tutte le coppie di punti del poliedro. Serve un teorema che dica come trovare i vertici di un poliedro scritto nella forma $Ax \ge b$ in modo **algebrico**. Prima però serve una definizione.

## Vincoli attivi

Sia $P = {x \in \mathbb{R}^n \mid Ax \ge b}$ e si indichino le **righe** di $A$ con $a_1^T, a_2^T, \dots, a_m^T$:

$$ A = \begin{pmatrix} a_1^T \ a_2^T \ \vdots \ a_m^T \end{pmatrix}. $$

> [!important] Definizione — vincolo attivo e insieme dei vincoli attivi Sia $\bar x \in P$. Il vincolo $i$ si dice **attivo** in $\bar x$ se $$ a_i^T \bar x = b_i , $$ cioè se in corrispondenza della riga $i$ vale l'uguaglianza e non la disuguaglianza stretta. L'insieme degli indici dei vincoli attivi in $\bar x$ si indica con $$ I(\bar x) = {, i \in {1, \dots, m} \mid a_i^T \bar x = b_i ,}. $$

Il concetto era già stato visto nella lezione 2; qui gli si dà un nome e una notazione. La docente ha fatto un esempio con un poliedro di $\mathbb{R}^2$ delimitato da tre vincoli (vettori $a_1, a_2, a_3$):

- per $\bar x$ **interno** al poliedro nessun vincolo vale con l'uguaglianza: $I(\bar x) = \varnothing$;
- per $\bar x$ su un **lato**, quello della terza retta, solo il terzo vincolo è attivo: $I(\bar x) = {3}$;
- per $\bar x$ nel **vertice** in cui si incontrano la seconda e la terza retta: $I(\bar x) = {2, 3}$.

In $\mathbb{R}^2$, a un vertice corrispondono **due** vincoli attivi. In generale, in $\mathbb{R}^n$, per avere un vertice servono **$n$ vincoli attivi**, ma con una qualificazione: devono essere "fatti bene", tutti significativi, non uno scritto sopra l'altro in modo diverso. In termini precisi devono essere **linearmente indipendenti**. Nel disegno, le due rette che si incontrano nel vertice non sono parallele: i vettori $a_2$ e $a_3$ non sono uno multiplo dell'altro.

## Il teorema di caratterizzazione dei vertici

> [!important] Teorema — caratterizzazione algebrica dei vertici Sia $P = {x \in \mathbb{R}^n \mid Ax \ge b}$, con $A \in \mathbb{R}^{m \times n}$ e $b \in \mathbb{R}^m$, un poliedro **non vuoto** (in generale un poliedro può essere vuoto), e sia $\bar x \in P$. Indicata con $A_{I(\bar x)}$ la sottomatrice di $A$ formata dalle righe $a_i^T$ con $i \in I(\bar x)$, e con $b_{I(\bar x)}$ il corrispondente sottovettore di $b$, sono **equivalenti**:
> 
> 1. $\bar x$ è un **vertice** di $P$;
> 2. esistono $n$ righe di $A$ **linearmente indipendenti** corrispondenti a **vincoli attivi** in $\bar x$;
> 3. $\bar x$ è l'**unica soluzione** del sistema lineare $A_{I(\bar x)}, x = b_{I(\bar x)}$;
> 4. $\operatorname{rk}\big(A_{I(\bar x)}\big) = n$, che è il massimo possibile.

> [!warning] Discrepanza tra fonti — termine noto del sistema Negli appunti scansionati il sistema del punto 3 è scritto $A_{I(\bar x)}, x = b$. Il termine noto corretto è il **sottovettore** $b_{I(\bar x)}$ dei soli vincoli attivi, altrimenti le dimensioni non sono compatibili: $A_{I(\bar x)}$ ha tante righe quanti sono i vincoli attivi, non $m$. È la formulazione delle dispense [@roma2023, Corollario 5.1.16].

**Il significato del teorema.** L'idea fondamentale è che i vertici si caratterizzano come **soluzioni di sistemi lineari**, cosa che dal punto di vista computazionale si sa fare molto bene. I sistemi in questione sono speciali: quelli in cui il rango della matrice è **massimo**, cioè $n$. Non può essere più di $n$, perché la matrice ha $n$ colonne. In pratica:

1. si prendono i vincoli attivi in $\bar x$;
2. si scrive il sistema lineare corrispondente. Può essere quadrato, ma anche avere più di $n$ equazioni, se in $\bar x$ passano più di $n$ rette di bordo;
3. si guarda quante soluzioni ha. Se ne ha **una sola** (che è necessariamente $\bar x$, perché $\bar x$ lo risolve per costruzione), $\bar x$ è un vertice; se ne ha più di una, non lo è.

**Un richiamo sul rango.** Una matrice si può guardare come una collezione di vettori riga o come una collezione di vettori colonna. Il **rango** è il massimo numero di righe linearmente indipendenti, che coincide (per fortuna) con il massimo numero di colonne linearmente indipendenti. Il rango è legato al numero di soluzioni di un sistema lineare (teorema di Rouché–Capelli): se il sistema ha soluzioni, ne ha $\infty^{,n - \operatorname{rk}}$, dove $n$ è il numero di incognite. Quindi la soluzione è **unica** esattamente quando il rango è $n$, ed è questo che rende banalmente equivalenti i punti 3 e 4. Il punto 2 dice la stessa cosa del 4 in altre parole: trovare $n$ righe indipendenti tra quelle dei vincoli attivi significa che il rango di $A_{I(\bar x)}$ è $n$.

La parte non banale è l'equivalenza tra il punto 1 (geometrico) e gli altri (algebrici). La dimostrazione non è stata fatta a lezione: la docente se ne è dispiaciuta, perché collega le due parti della lezione, e ha promesso di mettere online delle note. Le dispense la riportano per intero.

> [!tip] Approfondimento — Dimostrazione dell'equivalenza tra (1) e (2) #approfondimento Dalle dispense [@roma2023, Teorema 5.1.5]; non svolta a lezione.
> 
> **(1) ⇒ (2).** Sia $\bar x$ un vertice e si supponga per assurdo che i vincoli attivi linearmente indipendenti siano $k < n$. Allora il sistema omogeneo $a_i^T d = 0$, $i \in I(\bar x)$, ha rango minore di $n$ e quindi ha una soluzione $d \neq 0$. Per i vincoli **non attivi** vale $a_i^T \bar x > b_i$: sono un numero finito, quindi per $\varepsilon > 0$ abbastanza piccolo i punti $$ y = \bar x - \varepsilon d, \qquad z = \bar x + \varepsilon d $$ soddisfano ancora $a_i^T y \ge b_i$ e $a_i^T z \ge b_i$ per $i \notin I(\bar x)$. Per i vincoli **attivi**, $a_i^T y = a_i^T \bar x - \varepsilon, a_i^T d = b_i$, e lo stesso per $z$. Quindi $y, z \in P$, entrambi diversi da $\bar x$, e $\bar x = \tfrac12 y + \tfrac12 z$ è il punto medio del segmento $[y, z]$: $\bar x$ non è un vertice, contraddizione.
> 
> **(2) ⇒ (1).** Siano $n$ vincoli attivi in $\bar x$ linearmente indipendenti e si supponga per assurdo che $\bar x$ non sia un vertice. Allora $\bar x = \lambda y + (1-\lambda) z$ con $y, z \in P$ diversi da $\bar x$ e $\lambda \in (0,1)$. Per ogni $i \in I(\bar x)$: $$ b_i = a_i^T \bar x = \lambda, a_i^T y + (1 - \lambda), a_i^T z \ge \lambda b_i + (1-\lambda) b_i = b_i , $$ e l'uguaglianza vale solo se $a_i^T y = b_i$ e $a_i^T z = b_i$. Quindi anche $y$ e $z$ risolvono il sistema $a_i^T x = b_i$, $i \in I(\bar x)$, che però ha rango $n$ e dunque un'unica soluzione: assurdo, perché $y \neq \bar x$.

La procedura che il teorema suggerisce, e che si applica negli esercizi, si può riassumere così:

```pseudo
procedura VERIFICA_VERTICE(A, b, x̄)        // P = { x ∈ R^n : A x ≥ b },  A di taglia m × n
    // passo 0: il teorema richiede x̄ ∈ P
    se esiste i tale che a_iᵀ x̄ < b_i allora
        restituisci "x̄ non appartiene a P: non è un vertice"
    // passo 1: vincoli attivi
    I ← { i ∈ {1, …, m} : a_iᵀ x̄ = b_i }
    se |I| < n allora
        restituisci "meno di n vincoli attivi: non è un vertice"
    // passo 2: indipendenza lineare dei vincoli attivi
    A_I ← sottomatrice di A con le righe di indice in I
    se rango(A_I) = n allora                // se |I| = n basta verificare det(A_I) ≠ 0
        restituisci "x̄ è un vertice"
    altrimenti
        restituisci "x̄ non è un vertice"
```

## Conseguenze: quanti vertici ha un poliedro?

Dalla caratterizzazione segue subito, "gratis", una stima del numero massimo di vertici di un poliedro.

> [!important] Corollario 1 — ogni poliedro ha un numero finito di vertici Un poliedro $P = {x \in \mathbb{R}^n \mid Ax \ge b}$ con $A \in \mathbb{R}^{m \times n}$ ha **al più** $$ \binom{m}{n} = \frac{m!}{n!,(m-n)!} $$ vertici.

Il ragionamento è il seguente. Ogni vertice è l'unica soluzione di un sistema formato da $n$ righe indipendenti di $A$. Ogni scelta di $n$ righe tra le $m$ disponibili individua quindi al più un vertice, e i vertici non possono essere più delle scelte possibili, cioè dei sottoinsiemi di $n$ righe in un insieme di $m$ righe. È una stima grossolana, una **sovrastima**: non è detto che le righe scelte siano indipendenti, né che la soluzione del sistema stia in $P$.

> [!example] Esempio — $n = 2$, $m = 4$ Sia $A$ una matrice con quattro righe $a_1^T, a_2^T, a_3^T, a_4^T$ in $\mathbb{R}^2$. Senza disegnare nulla si può dire che il poliedro ${x \mid Ax \ge b}$ ha al più tanti vertici quante sono le coppie di righe: $$ {1,2},\ {1,3},\ {1,4},\ {2,3},\ {2,4},\ {3,4} \quad\Rightarrow\quad 3 + 2 + 1 = 6 = \binom{4}{2} = \frac{4!}{2!,2!}. $$ Ogni poliedro descritto da 4 disuguaglianze in $\mathbb{R}^2$ ha al più 6 vertici.

**Perché interessa.** A breve si vedrà il **teorema fondamentale della programmazione lineare**: i punti che possono essere soluzioni ottime di un problema di programmazione lineare sono i **vertici**. Sapere che i vertici sono in numero finito significa che anche i candidati a soluzione sono in numero finito. L'algoritmo del simplesso sfrutta pesantemente questa informazione.

> [!tip] Approfondimento — Finito non vuol dire piccolo #approfondimento Il numero di vertici è finito, ma la stima $\binom{m}{n}$ cresce molto in fretta (valori calcolati): $\binom{7}{4} = 35$, $\binom{20}{10} = 184,756$, $\binom{100}{50} \approx 1.01 \times 10^{29}$. Un problema con 50 variabili e 100 vincoli è piccolo per gli standard applicativi, eppure enumerare tutti i possibili sistemi $50 \times 50$ è impraticabile: è la stessa situazione dell'esempio di Dantzig della [[Lezione 01 - Introduzione alla Ricerca Operativa|lezione 1]]. Il metodo del simplesso evita l'enumerazione e si sposta da un vertice all'altro migliorando ogni volta la funzione obiettivo.

> [!important] Corollario 2 — se $m < n$ non ci sono vertici Se il numero di righe di $A$ è minore di $n$ ($m < n$), il poliedro **non ha vertici**: non si possono trovare $n$ righe indipendenti se di righe ce ne sono meno di $n$. Più in generale, nelle dispense, non ci sono vertici se le righe linearmente indipendenti di $A$ sono meno di $n$, cioè se $\operatorname{rk}(A) < n$ [@roma2023, Corollario 5.1.15].

Alcuni esempi "banali, ma per dare un'idea":

- in $\mathbb{R}^2$, con **una sola** disuguaglianza il poliedro è un semipiano e non ha vertici;
- in $\mathbb{R}^3$, con **due** piani, anche se indipendenti, il poliedro (per esempio la regione che sta "sopra" entrambi) ha uno **spigolo**, ma non ha vertici: servirebbe un terzo piano;
- in $\mathbb{R}^2$, **due righe non bastano** se sono dipendenti. Si consideri $$ P = {, x \in \mathbb{R}^2 \mid x_1 - x_2 \ge -1,\ \ x_1 - x_2 \ge 1 ,}, \qquad A = \begin{pmatrix} 1 & -1 \ 1 & -1 \end{pmatrix}, \quad b = \begin{pmatrix} -1 \ 1 \end{pmatrix}. $$ La prima disuguaglianza individua il semipiano sotto la retta $x_2 = x_1 + 1$ (che passa per $(0, 1)$), la seconda quello sotto la retta parallela $x_2 = x_1 - 1$; il vettore $a_1 = a_2 = (1, -1)$ punta in basso a destra, verso i semipiani. L'intersezione è il secondo semipiano, quindi in effetti il primo vincolo è ridondante. La matrice $A$ ha due righe, ma **rango 1**: "è come se ne avessi una". Non si trovano due righe indipendenti, quindi $P$ non ha vertici.

> [!tip] Approfondimento — Vertici e rette contenute nel poliedro #approfondimento Le dispense [@roma2023, Teorema 5.1.6, senza dimostrazione] danno un criterio geometrico che spiega tutti questi esempi: **un poliedro non vuoto ha almeno un vertice se e solo se non contiene rette**. Un poliedro contiene una retta se esiste un suo punto $\tilde x$ e una direzione $d \neq 0$ tali che $\tilde x + \lambda d \in P$ per ogni $\lambda \in \mathbb{R}$. Il semipiano, la regione di $\mathbb{R}^3$ sopra due piani (che contiene la retta dello spigolo) e il semipiano dell'ultimo esempio contengono tutti delle rette, e infatti non hanno vertici. Il poliedro illimitato della miscelazione (lezione 3) contiene semirette ma non rette, e ha vertici.

## Esercizio svolto: vertici di un poliedro in $\mathbb{R}^4$

> [!example] Testo Sia $P \subseteq \mathbb{R}^4$ il poliedro definito da $$ \begin{cases} x_1 + x_2 + 2x_3 + x_4 \le 5 \ x_1 - x_2 + 2x_3 - x_4 \le 1 \ 2x_1 + 4x_3 \le 6 \ x_2 - 4x_3 + x_4 \le 0 \ x_1 \ge 0 \ x_2 \ge 0 \ x_3 \ge 0 \end{cases} $$ Dire se i punti $(-1, 0, 0, 0)$, $(1, 0, 0, 0)$, $(1, 1, 1, 1)$ e $\left(0, \tfrac52, \tfrac54, 0\right)$ sono vertici di $P$.

Si noti che su $x_4$ **non c'è** vincolo di segno.

**Passo preliminare: scrivere $P$ nella forma $Ax \ge b$.** Il teorema si applica a poliedri scritti come ${x \mid Ax \ge b}$, e come sempre, prima di applicare un teorema, bisogna verificarne le ipotesi. I primi quattro vincoli sono con "$\le$": si cambiano tutti i segni.

$$ A = \begin{pmatrix} -1 & -1 & -2 & -1 \ -1 & 1 & -2 & 1 \ -2 & 0 & -4 & 0 \ 0 & -1 & 4 & -1 \ 1 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \ 0 & 0 & 1 & 0 \end{pmatrix}, \qquad b = \begin{pmatrix} -5 \ -1 \ -6 \ 0 \ 0 \ 0 \ 0 \end{pmatrix}. $$

$A$ è $7 \times 4$: $m = 7$ vincoli, $n = 4$ incognite. Poiché $m \ge n$ "c'è speranza", cioè ci possono essere vertici; per esserlo, un punto deve avere almeno 4 vincoli attivi linearmente indipendenti.

**Passo 0: i punti stanno in $P$?** Il teorema parte da un punto $\bar x \in P$, quindi prima di tutto bisogna verificarlo. La tabella riporta, per ogni vincolo $a_i^T x \ge b_i$, il valore di $a_i^T \bar x$ (in grassetto i vincoli attivi):

|$i$|vincolo $a_i^T x \ge b_i$|$b_i$|$(-1,0,0,0)$|$(1,0,0,0)$|$(1,1,1,1)$|$(0,\tfrac52,\tfrac54,0)$|
|---|---|---|---|---|---|---|
|1|$-x_1 - x_2 - 2x_3 - x_4$|$-5$|$1$|$-1$|$\mathbf{-5}$|$\mathbf{-5}$|
|2|$-x_1 + x_2 - 2x_3 + x_4$|$-1$|$1$|$\mathbf{-1}$|$\mathbf{-1}$|$0$|
|3|$-2x_1 - 4x_3$|$-6$|$2$|$-2$|$\mathbf{-6}$|$-5$|
|4|$-x_2 + 4x_3 - x_4$|$0$|$\mathbf{0}$|$\mathbf{0}$|$2$|$\tfrac52$|
|5|$x_1$|$0$|$-1$ ✗|$1$|$1$|$\mathbf{0}$|
|6|$x_2$|$0$|$\mathbf{0}$|$\mathbf{0}$|$1$|$\tfrac52$|
|7|$x_3$|$0$|$\mathbf{0}$|$\mathbf{0}$|$1$|$\tfrac54$|

Il punto $(-1, 0, 0, 0)$ viola il vincolo $x_1 \ge 0$ ($-1 \ge 0$ è falso): **non sta in $P$**, quindi non è un vertice. Gli altri tre punti stanno in $P$, e questo mostra anche che $P \neq \varnothing$, come richiesto dal teorema. Restano tre candidati.

**Passo 1–2: vincoli attivi e indipendenza.**

_Punto $(1, 0, 0, 0)$._ Il vincolo 1 non è attivo ($-1 > -5$), il 2 sì ($-1 = -1$), il 3 no, il 4 sì ($0 = 0$). Il 5 non è attivo: $x_1 = 1$ è strettamente maggiore di $0$, ed è attivo solo un vincolo verificato con l'uguaglianza (a lezione è stato chiesto proprio questo). I vincoli 6 e 7 sono attivi. Quindi

$$ I(1,0,0,0) = {2, 4, 6, 7}: $$

ci sono 4 vincoli attivi, tanti quanti le incognite, quindi il punto è un **candidato vertice**. Resta da verificare che le righe corrispondenti siano indipendenti. La sottomatrice è quadrata, $4 \times 4$, e il suo rango è 4 se e solo se il **determinante** è diverso da zero:

$$ A_{I(1,0,0,0)} = \begin{pmatrix} -1 & 1 & -2 & 1 \ 0 & -1 & 4 & -1 \ 0 & 1 & 0 & 0 \ 0 & 0 & 1 & 0 \end{pmatrix}. $$

A lezione il determinante non è stato calcolato ("credetemi, fate sto determinante se non mi credete"). Il calcolo è semplice: sviluppando lungo la prima colonna, che ha un solo elemento non nullo, e poi il minore $3 \times 3$ lungo la sua seconda riga,

$$ \det A_{I} = (-1) \cdot \det \begin{pmatrix} -1 & 4 & -1 \ 1 & 0 & 0 \ 0 & 1 & 0 \end{pmatrix} = (-1) \cdot \left[ 1 \cdot (-1)^{2+1} \det \begin{pmatrix} 4 & -1 \ 1 & 0 \end{pmatrix} \right] = (-1) \cdot \left[ -(0 + 1) \right] = 1 \neq 0 . $$

Le quattro righe sono linearmente indipendenti: **$(1, 0, 0, 0)$ è un vertice**.

> [!warning] Discrepanza tra fonti — sottomatrice dei vincoli attivi Negli appunti scansionati la prima riga di $A_{I(1,0,0,0)}$ è scritta $(-1, 1, 2, 1)$. La riga 2 di $A$ è $(-1, 1, -2, 1)$: il coefficiente di $x_3$ nel vincolo $x_1 - x_2 + 2x_3 - x_4 \le 1$ cambia segno quando lo si porta nella forma "$\ge$". Il risultato non cambia, perché nello sviluppo lungo la prima colonna quel coefficiente non interviene, ma la matrice corretta è quella riportata sopra.

_Punto $(1, 1, 1, 1)$._ Sono attivi i primi tre vincoli ($-5 = -5$, $-1 = -1$, $-6 = -6$), mentre il quarto vale $2 > 0$ e i vincoli di segno valgono $1 > 0$:

$$ I(1,1,1,1) = {1, 2, 3}. $$

Solo **tre** vincoli attivi, mentre per un vertice in $\mathbb{R}^4$ ne servono almeno quattro indipendenti: **$(1, 1, 1, 1)$ non è un vertice**. Tra l'altro i tre vincoli attivi non sono nemmeno indipendenti: la riga 3 è la somma delle righe 1 e 2, quindi $\operatorname{rk} A_{I} = 2$ (osservazione aggiunta).

_Punto $\left(0, \tfrac52, \tfrac54, 0\right)$._ La docente lo ha lasciato come esercizio ("questo è difficile perché ho cinque mezzi e cinque quarti").

> [!example] Svolgimento dell'esercizio lasciato (calcolo non svolto a lezione) Dalla tabella: il vincolo 1 è attivo ($-0 - \tfrac52 - \tfrac52 - 0 = -5$); il 2 no ($0 > -1$); il 3 no ($-5 > -6$); il 4 no ($-\tfrac52 + 5 = \tfrac52 > 0$); il 5 sì ($x_1 = 0$); il 6 e il 7 no ($x_2 = \tfrac52 > 0$, $x_3 = \tfrac54 > 0$). Quindi $$ I\left(0, \tfrac52, \tfrac54, 0\right) = {1, 5}. $$ Due soli vincoli attivi, meno di $n = 4$: il punto sta in $P$ ma **non è un vertice**.

|punto|in $P$?|$I(\bar x)$|vertice?|
|---|---|---|---|
|$(-1, 0, 0, 0)$|no (viola $x_1 \ge 0$)|—|no|
|$(1, 0, 0, 0)$|sì|${2, 4, 6, 7}$, rango 4|**sì**|
|$(1, 1, 1, 1)$|sì|${1, 2, 3}$|no|
|$\left(0, \tfrac52, \tfrac54, 0\right)$|sì|${1, 5}$|no|

La docente ha insistito sull'importanza di **fare i conti da soli**, perché all'esame bisogna saperli fare e serve allenamento.

## Riepilogo

- Retta, semiretta e segmento hanno la stessa forma $x_0 + t,v$: cambia l'insieme del parametro ($\mathbb{R}$, $t \ge 0$, $[0,1]$ con $v = z - x_0$).
- $C$ è **convesso** se contiene il segmento tra due suoi punti qualsiasi: $(1-t)x + tz \in C$. L'intersezione di convessi, anche infiniti, è convessa.
- **Iperpiani** ${a^T x = b}$ ($a \neq 0$: dimensione $n-1$; retta in $\mathbb{R}^2$, piano in $\mathbb{R}^3$) e **semispazi chiusi** ${a^T x \ge b}$, ${a^T x \le b}$ sono convessi.
- Un **poliedro** è l'intersezione di un numero finito di semispazi chiusi; un **politopo** è un poliedro limitato. Ogni poliedro è convesso e si scrive come ${x \mid Ax \ge b}$; l'insieme ammissibile di un problema di PL è il poliedro $P = {x \mid Ax \ge b}$.
- $\bar x \in P$ è un **vertice** se non sta all'interno di un segmento di $P$. Vincolo $i$ **attivo** in $\bar x$: $a_i^T \bar x = b_i$; $I(\bar x)$ è l'insieme dei vincoli attivi.
- **Teorema**: $\bar x$ è un vertice $\iff$ esistono $n$ vincoli attivi linearmente indipendenti $\iff$ $\bar x$ è l'unica soluzione di $A_{I(\bar x)}x = b_{I(\bar x)}$ $\iff$ $\operatorname{rk} A_{I(\bar x)} = n$.
- **Corollari**: un poliedro ha al più $\binom{m}{n}$ vertici (quindi un numero finito); se $m < n$ (o più in generale $\operatorname{rk} A < n$) non ha vertici.