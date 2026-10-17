---

## corso: Ricerca Operativa lezione: 5 data: 2026-10-06 docente: Silvia Villa argomenti: [forma generale, poliedri senza rette, teorema fondamentale della programmazione lineare, problemi illimitati inferiormente, insieme delle soluzioni ottime, idea del metodo del simplesso, maledizione della dimensionalità, forma standard, variabili di slack, variabili di surplus, variabili libere, vertici in forma standard, colonne linearmente indipendenti] fonti: [trascrizione, appunti manuali, dispense] tags: [ricerca-operativa, lezione]

# Lezione 5 — Teorema fondamentale e forma standard

> [!info] Fonti di questa nota Trascrizione della lezione del 06/10/2026 (un'unica parte, comprensiva della ripresa dopo la pausa), appunti manuali (scansione della lezione 5, una sola pagina: arriva fino alla definizione di problema in forma standard) e note Obsidian _Vertici_di_poliedri_ e _Simplesso_ (prima metà: trasformazioni in forma standard, esercizio, caratterizzazione dei vertici e dimostrazione). Le dispense [@roma2023, §5.1–5.2, §6.1–6.2] e le note di Di Summa [@disumma2015, §1.1–1.2, §2.3] contengono gli stessi risultati; le parti prese solo da queste fonti, e i calcoli aggiunti per verifica, sono indicati esplicitamente.

La lezione chiude lo studio dei poliedri in forma generale con due risultati, la caratterizzazione dei poliedri che hanno vertici e il **teorema fondamentale della programmazione lineare**, e poi apre il capitolo sul **metodo del simplesso**. Il primo passo è riscrivere il problema in una forma diversa, la **forma standard**, e caratterizzarne i vertici guardando le **colonne** della matrice dei vincoli invece delle righe.

## Ripasso: poliedri in forma generale e vertici

Si considerano poliedri descritti da un numero finito di disuguaglianze, scritte tutte con "$\ge$":

$$ P = {, x \in \mathbb{R}^n \mid Ax \ge b ,}, \qquad A \in \mathbb{R}^{m \times n},\ b \in \mathbb{R}^m . $$

Come visto nella [[Lezione 04 - Convessità, poliedri e vertici|lezione 4]], ogni poliedro si può scrivere così. La docente introduce un termine nuovo: un poliedro scritto in questo modo si dice **descritto in forma generale**. Oggi si vedrà un'altra descrizione, più utile per il metodo del simplesso; la forma generale resta però quella comoda per caratterizzare i vertici.

Un punto $\bar x \in P$ è un **vertice** se non sta all'interno di un segmento con estremi in $P$. Con l'insieme dei vincoli attivi $I(\bar x) = { i \mid a_i^T \bar x = b_i }$, il teorema della lezione 4 dice che, **per $\bar x \in P$** (la docente insiste: il punto deve stare nel poliedro),

$$ \bar x \text{ è un vertice} \iff \operatorname{rk}\big(A_{I(\bar x)}\big) = n , $$

dove $A_{I(\bar x)}$ è la matrice formata dalle sole righe dei vincoli attivi.

## Quando un poliedro ha vertici

Il teorema permette di decidere se un **punto dato** è un vertice. C'è anche una caratterizzazione più geometrica, che serve a stabilire se un **poliedro** ha vertici. Si è già visto che esistono poliedri senza vertici: per esempio la striscia delimitata da due rette parallele, dove i vincoli sono due ma la matrice che li definisce ha rango 1.

> [!important] Proposizione — esistenza di vertici Sia $P = { x \in \mathbb{R}^n \mid Ax \ge b } \neq \varnothing$. Sono equivalenti:
> 
> 1. $P$ ha almeno un vertice;
> 2. $P$ non contiene rette.

La proposizione non è stata dimostrata ([@roma2023, Teorema 5.1.6] la riporta senza dimostrazione). Verrà usata come ipotesi: il fatto che un poliedro non contenga rette garantisce automaticamente l'esistenza di un vertice, e nel seguito interesseranno proprio poliedri con vertici.

> [!warning] Discrepanza tra fonti — enunciato della proposizione Nella nota _Vertici_di_poliedri_ la proposizione elenca tre punti, il secondo dei quali è incompleto ("2) e"). La scansione e la trascrizione riportano due sole condizioni equivalenti, come sopra.

## Il teorema fondamentale della programmazione lineare

Si torna al problema di ottimizzazione

$$ (\mathrm{PL}) \qquad \min\ c^T x \quad \text{s.t.} \quad Ax \ge b . $$

Con i risultati sui poliedri si può enunciare il teorema che caratterizza le soluzioni di questo problema.

> [!important] Teorema fondamentale della programmazione lineare Sia $P = { x \in \mathbb{R}^n \mid Ax \ge b } \neq \varnothing$ un poliedro che **non contiene rette**. Allora per il problema (PL) si verifica uno dei seguenti casi:
> 
> 1. (PL) è **illimitato inferiormente**;
> 2. (PL) **ammette soluzione ottima**, e una delle soluzioni ottime è un **vertice** di $P$.

"Illimitato inferiormente" significa che il minimo non esiste perché la funzione obiettivo si può abbassare in modo arbitrario sui punti ammissibili: se si vuole, il "minimo" è $-\infty$. Il termine si riferisce al fatto che si sta minimizzando, e quindi si va verso $-\infty$; non ha nulla a che vedere con la limitatezza del poliedro.

Ricapitolando, per un problema di programmazione lineare ci sono tre possibilità:

|situazione|esito|
|---|---|
|$P = \varnothing$|problema **inammissibile**|
|$P \neq \varnothing$, senza rette, $c^T x$ non limitata dal basso su $P$|problema **illimitato inferiormente**|
|$P \neq \varnothing$, senza rette, $c^T x$ limitata dal basso su $P$|il minimo **esiste** ed è assunto (anche) in un **vertice**|

Il teorema è interessante per due ragioni.

**Esclude un caso patologico.** Non può succedere che la funzione obiettivo sia limitata dal basso ma il minimo non sia assunto. In generale, per problemi di minimo, questo può succedere. L'esempio della docente è $f(x) = 1/x$ sulla semiretta positiva: $f$ è limitata dal basso da $0$ e si avvicina a $0$ quanto si vuole, ma non ci arriva mai, quindi non ha minimo. Per i problemi di programmazione lineare questo non accade, ed è la funzione obiettivo lineare a impedirlo: o si è limitati dal basso, e allora c'è una soluzione, oppure la funzione va a $-\infty$ sull'insieme ammissibile.

> [!warning] Dettaglio sull'esempio $1/x$ Negli appunti l'esempio è scritto su $P = { x \in \mathbb{R} \mid x \ge 0 }$. In $x = 0$ la funzione $1/x$ non è definita, quindi l'insieme corretto su cui leggere l'esempio è $x > 0$. Il senso non cambia: $\inf_{x > 0} 1/x = 0$ non è mai raggiunto.

**Localizza le soluzioni.** Se una soluzione esiste, una delle soluzioni è un vertice. È questo il punto di partenza del metodo del simplesso.

> [!example] Esempio — un problema illimitato inferiormente La docente ha disegnato un poliedro di $\mathbb{R}^2$ illimitato, con tre vincoli e due vertici; dagli appunti Obsidian si legge $$ P = {, (x_1, x_2) \mid x_1 \ge 0,\ x_2 \ge 0,\ x_2 \ge 1 - x_1 ,}, $$ con vertici $(0, 1)$ e $(1, 0)$. Non contiene rette, quindi soddisfa le ipotesi del teorema. Se il vettore $c$ è orientato in modo che la funzione decresca andando verso la parte illimitata del poliedro, la retta di livello si può spostare quanto si vuole nel verso di decrescita trovando sempre punti di $P$: il problema è illimitato inferiormente. Un esempio numerico (scelto qui, non dalla lezione) è $c = (1, -1)$: sui punti $(0, t) \in P$ si ha $c^T x = -t \to -\infty$ per $t \to +\infty$.

> [!tip] Approfondimento — Varianti del teorema fondamentale #approfondimento Le dispense enunciano il teorema con tre alternative mutuamente esclusive (inammissibile, illimitato, ottimo su un vertice) sotto l'ipotesi che $P$ non contenga rette [@roma2023, Teorema 5.2.1], e ne riportano senza dimostrazione una versione più forte che vale per **ogni** problema: inammissibile, illimitato oppure con soluzione ottima; l'ipotesi sui vertici serve solo a garantire che una soluzione ottima cada su un vertice [@roma2023, Teorema 5.2.2]. Le note di Di Summa seguono la stessa strada: il Teorema 1.1 dà le tre alternative per un programma lineare qualsiasi, e il Teorema 2.6 aggiunge che, per un problema in forma standard con soluzione ottima, ne esiste una che è una soluzione di base ammissibile [@disumma2015, Teoremi 1.1 e 2.6]. Lo stesso testo mostra che senza l'ipotesi i vertici possono mancare: il sistema $x_1 + x_2 + x_3 \le 1$, $x_1 + x_2 \ge 0$, $x_3 \ge 0$ ha soluzioni (per esempio l'origine) ma nessun vertice, perché non si trovano tre vincoli linearmente indipendenti.

## L'insieme delle soluzioni ottime

Del caso in cui le soluzioni esistono si può dire di più. Sia $m$ il valore minimo (qui $m$ è un numero, non il numero di righe di $A$) e sia

$$ S = {, \bar x \in P \mid c^T \bar x = \min_{x \in P} c^T x ,} = P \cap {, \bar x \mid c^T \bar x = m ,} . $$

Le soluzioni sono i punti del poliedro su cui la funzione obiettivo vale esattamente il minimo. Che insieme è $S$? È l'**intersezione** di due insiemi:

- $P$ è un poliedro, quindi convesso;
- ${ \bar x \mid c^T \bar x = m }$ è l'insieme delle soluzioni di un'equazione lineare: è un **iperpiano** (una retta in $\mathbb{R}^2$, un piano in $\mathbb{R}^3$), quindi convesso.

Intersecare un poliedro con un iperpiano dà ancora un poliedro, perché un poliedro è per definizione l'intersezione di un numero finito di semispazi ed eventualmente iperpiani.

> [!important] Proprietà dell'insieme delle soluzioni L'insieme $S$ delle soluzioni ottime di un problema di programmazione lineare è un **poliedro**, e quindi è **convesso**.

$S$ non può quindi avere "forme strane". Sullo stesso poliedro dell'esempio precedente la docente ha disegnato tre casi; i vettori $c$ numerici della tabella sono scelti qui per illustrarli (a lezione erano solo disegnati).

|funzione obiettivo|$S$|numero di soluzioni|
|---|---|---|
|rette di livello non parallele ad alcun lato (es. $c = (1, 2)$)|un solo vertice, $(1, 0)$, con valore $1$|una|
|rette di livello parallele al lato tra i due vertici (es. $c = (1, 1)$)|il segmento $[A, B]$ con $A = (0,1)$, $B = (1,0)$|infinite|
|$c = 0$|tutto $P$|infinite|

Nel secondo caso le soluzioni sono infinite: tra esse ci sono i vertici, come garantisce il teorema, ma anche punti che non sono vertici. Il terzo caso è "poco furbo, ma possibile": se $c = 0$ la funzione costo è costante e ogni punto ammissibile è ottimo. Infine $S$ può essere vuoto, se il problema è illimitato. In dimensione più alta ci sono più possibilità (facce di varie dimensioni), ma la struttura è la stessa.

> [!important] Conseguenza — o una soluzione o infinite Un problema di programmazione lineare **non** può avere un numero finito di soluzioni maggiore di uno. Se $x_1 \neq x_2$ sono due soluzioni, per la convessità di $S$ è soluzione l'intero segmento che le unisce, e quindi le soluzioni sono infinite.

> [!tip] Schema da disegnare Figura consigliata in Excalidraw: tre copie del poliedro ${x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \ge 1}$ affiancate. Nella prima, il vettore $c$ e la retta di livello ottima che tocca $P$ solo nel vertice $(1,0)$; nella seconda, $c$ perpendicolare al lato obliquo e il segmento ottimo $[A,B]$ evidenziato; nella terza, $c = 0$ e tutto $P$ colorato. Si può aggiungere una quarta copia con $c$ diretto in modo da rendere il problema illimitato.

## L'idea del metodo del simplesso

Si supponga che il poliedro sia non vuoto e non contenga rette, così da essere sicuri che abbia almeno un vertice. Per il teorema fondamentale la soluzione, se esiste, sta (anche) su un vertice; altrimenti il problema è illimitato inferiormente. Esclusa l'illimitatezza, un modo per risolvere il problema sarebbe prendere **tutti** i vertici, calcolare la funzione costo in ciascuno e scegliere quello con il valore più piccolo.

Il metodo del simplesso fa qualcosa di più intelligente. Parte da un vertice, calcola la funzione costo, poi si sposta in un altro vertice, e così via, un vertice alla volta. L'informazione in più è questa: **ogni volta che si sposta, la funzione costo diminuisce**. Così non si fanno conti inutili: una volta in un vertice di costo 10, non si calcola mai la funzione in vertici di costo più alto. La docente avverte che questo è l'algoritmo "ideale": a volte si faranno passi che lasciano nello stesso vertice e non diminuiscono il costo, ma l'idea sottostante resta questa.

Gli appunti schematizzano così le fasi del metodo:

1. si parte da un poliedro $P \neq \varnothing$ che non contiene rette;
2. si deve aver verificato che il problema non sia illimitato inferiormente (questi primi due sono "passi 0", controlli preliminari);
3. si seleziona un vertice e si verifica se è soluzione; se non lo è, ci si muove in un vertice con costo minore.

**Perché non l'enumerazione.** Evitare di controllare tutti i vertici è fondamentale, perché in dimensione alta il numero dei vertici cresce molto velocemente. L'esempio "stupido ma istruttivo" della docente è il cubo unitario $[0,1]^n$:

|$n$|poliedro|numero di vertici|
|---|---|---|
|2|quadrato $[0,1]^2$|$4 = 2^2$|
|3|cubo $[0,1]^3$|$8 = 2^3$ (4 davanti e 4 dietro)|
|4|ipercubo $[0,1]^4$|$2^4 = 16$|
|$n$|cubo $[0,1]^n$|$2^n$|

L'esponenziale cresce più velocemente di tutte le potenze positive: già con $2^{10}$ un poliedro molto semplice ha un numero di vertici ingestibile per una ricerca esaustiva. Questa crescita è la **maledizione della dimensionalità**. Il simplesso non la evita del tutto: nel caso peggiore esplora tutti i vertici, quindi termina in un numero finito di passi ma potenzialmente enorme. In pratica però questo non succede quasi mai, il metodo si usa su problemi con migliaia di variabili, e si usano trucchi pratici per accelerarlo.

> [!tip] Approfondimento — Il caso peggiore e il comportamento tipico #approfondimento Il caso peggiore evocato dalla docente esiste davvero. Klee e Minty hanno costruito, per ogni $n$, un cubo "deformato" di $\mathbb{R}^n$ (con $2^n$ vertici) su cui il simplesso con la regola di scelta classica di Dantzig, quella del costo ridotto più negativo che si vedrà nella [[Lezione 08 - Test di illimitatezza e cambio di base|lezione 8]], visita tutti i $2^n$ vertici prima di arrivare all'ottimo: il numero di iterazioni è esponenziale nella dimensione [@klee1972]. Il buon comportamento osservato in pratica ha invece ricevuto una spiegazione teorica con l'**analisi smussata** (_smoothed analysis_) di Spielman e Teng: se i dati del problema vengono perturbati con un piccolo rumore casuale, il numero atteso di iterazioni di una variante del simplesso è polinomiale [@spielman2004].

Il metodo del simplesso richiederà molte lezioni. Il primo passo è cambiare il modo di scrivere il poliedro.

## La forma standard

La forma generale è comoda per caratterizzare i vertici, e l'abbiamo usata per questo. Per il metodo del simplesso conviene invece manipolare il problema e scriverlo in **forma standard**.

> [!important] Definizione — problema in forma standard Un problema di programmazione lineare è in **forma standard** se è scritto come $$ \begin{cases} \min\ c^T x \ A x = b \ x \ge 0 \end{cases} \qquad A \in \mathbb{R}^{m \times n},\ b \in \mathbb{R}^m,\ c, x \in \mathbb{R}^n , $$ cioè con soli **vincoli di uguaglianza** e **vincoli di non negatività** su tutte le variabili. Il poliedro corrispondente è $P = { x \in \mathbb{R}^n \mid Ax = b,\ x \ge 0 }$.

Attenzione: la matrice $A$ ha ora un significato diverso da quello della forma generale. Contiene solo i coefficienti delle uguaglianze; i vincoli $x \ge 0$ non vi compaiono.

**Perché questa fatica.** Un poliedro in forma standard non vuoto **ha sempre vertici**. Per la proposizione vista sopra basta che non contenga rette, e infatti non ne contiene: $P$ sta nell'ortante positivo ${x \ge 0}$, e una retta prima o poi deve uscirne. In $\mathbb{R}^2$ lo si vede subito; in dimensione più alta il ragionamento è lo stesso: i vincoli di positività non possono essere verificati da tutti i punti di una retta. Scrivendo il problema in forma standard si possono quindi **saltare i passi 0 e 1** dello schema precedente: si parte da un poliedro che, se non è vuoto, ha certamente vertici.

> [!tip] Approfondimento — Perché l'ortante non contiene rette #approfondimento Il ragionamento della docente si formalizza in una riga (osservazione aggiunta). Se la retta ${x_0 + t,d \mid t \in \mathbb{R}}$, con $d \neq 0$, fosse contenuta in $P$, per ogni componente $j$ si avrebbe $x_{0,j} + t,d_j \ge 0$ per **ogni** $t \in \mathbb{R}$. Se $d_j > 0$ basta prendere $t$ molto negativo, se $d_j < 0$ basta prendere $t$ molto positivo, per violare la disuguaglianza. Quindi $d_j = 0$ per ogni $j$, cioè $d = 0$: contraddizione.

**È restrittivo?** Scrivendo così si considerano meno poliedri di prima? No, purché si accetti di **aggiungere variabili**. Un poliedro qualunque in generale non si descrive in forma standard con le stesse variabili, ma il **problema** sì: ogni problema con uguaglianze e disuguaglianze si trasforma in un problema equivalente in forma standard, e si dovrà farlo quasi sempre. Gli ostacoli sono due: i vincoli di disuguaglianza e le variabili non vincolate in segno.

### Primo trucco: vincoli di "$\le$" e variabili di slack

Si consideri un vincolo

$$ a_1 x_1 + a_2 x_2 + \dots + a_n x_n \le b . $$

Per i punti del poliedro la somma a sinistra è al più $b$: aggiungendole una quantità non negativa si arriva esattamente a $b$. Si introduce quindi una nuova variabile $s$ e si scrive

$$ a_1 x_1 + \dots + a_n x_n + s = b, \qquad s \ge 0 . $$

In termini di insiemi,

$$ { (x_1, \dots, x_n) \mid a_1 x_1 + \dots + a_n x_n \le b } = { (x_1, \dots, x_n) \mid a_1 x_1 + \dots + a_n x_n + s = b \text{ per qualche } s \ge 0 }. $$

Se $(x_1, \dots, x_n)$ verifica la disuguaglianza, basta prendere $s = b - (a_1 x_1 + \dots + a_n x_n) \ge 0$; viceversa, se esiste $s \ge 0$ che rende vera l'uguaglianza, la disuguaglianza vale. La variabile $s$ si chiama **variabile di slack** (di scarto): è "quello che manca per arrivare a $b$".

> [!example] Esempio — una variabile di slack Il punto $(1, 0)$ verifica $2x_1 + x_2 \le 3$, perché a sinistra si ottiene $2 < 3$. Nella forma con l'uguaglianza $$ 2 \cdot 1 + 1 \cdot 0 + \underbrace{1}_{s} = 3 : $$ la slack vale $s = 3 - 2 = 1$. Si aggiunge una dimensione, ma la disuguaglianza diventa un'uguaglianza.

> [!warning] Discrepanza nella trascrizione — slack o surplus A lezione la docente ha prima chiamato $s$ "variabile di surplus" e si è subito corretta: si chiama **slack**. Il nome _surplus_ spetta alla variabile del trucco successivo.

### Secondo trucco: vincoli di "$\ge$" e variabili di surplus

Per un vincolo $a_1 x_1 + \dots + a_n x_n \ge b$ la somma è più grande di $b$: per arrivare a $b$ bisogna **togliere** qualcosa di non negativo. Si introduce una variabile $u$ e si scrive

$$ a_1 x_1 + \dots + a_n x_n - u = b, \qquad u \ge 0 . $$

Il segno meno davanti a $u$ serve proprio a mantenere $u \ge 0$: si vogliono aggiungere solo variabili non negative, perché la forma standard le richiede. La variabile $u$ si chiama **variabile di surplus** (di eccedenza).

> [!warning] Discrepanza tra fonti — il vincolo con la surplus Nella nota _Simplesso_ l'uguaglianza ottenuta è scritta "$a_1 x_1 + \dots + a_n x_n + - = b$", con la variabile mancante. La forma corretta, detta a lezione, è $a_1 x_1 + \dots + a_n x_n - u = b$ con $u \ge 0$.

### Terzo trucco: variabili libere

Se una variabile $x$ non è vincolata in segno, la si scrive come differenza tra la sua **parte positiva** e la sua **parte negativa**:

$$ x = x^+ - x^-, \qquad x^+ \ge 0,\ x^- \ge 0 . $$

Per esempio $3 = 3 - 0$ e $-3 = 0 - 3$. Il segno meno davanti a $x^-$ permette di chiedere che entrambe le nuove variabili siano non negative. Per descrivere una variabile reale servono così due variabili non negative, e in tutto il problema (funzione obiettivo compresa) $x$ va sostituita con $x^+ - x^-$.

> [!tip] Approfondimento — Massimo, minimo e scelta delle parti #approfondimento Le note di Di Summa dimostrano formalmente che ogni programma lineare è equivalente a uno in forma standard [@disumma2015, Proposizione 1.2]. Due dettagli completano il quadro della lezione. Primo, in quelle note la forma standard è scritta con il **massimo**; si passa da una all'altra con $\min c^T x = -\max(-c^T x)$, e il corso usa il minimo come le dispense [@roma2023, §6.1]. Secondo, per una variabile libera $x_j$ una scelta naturale delle due parti è $x_j' = \max{0, x_j}$ e $x_j'' = \max{0, -x_j}$, che dà proprio $3 = 3 - 0$ e $-3 = 0 - 3$ come negli esempi della docente; la scomposizione però non è unica ($3 = 5 - 2$ va bene lo stesso), e questo non crea problemi perché interessa solo la differenza.

|ostacolo|trasformazione|nuove variabili|
|---|---|---|
|$a^T x \le b$|$a^T x + s = b$|slack $s \ge 0$|
|$a^T x \ge b$|$a^T x - u = b$|surplus $u \ge 0$|
|$x_j$ libera|$x_j = x_j^+ - x_j^-$|$x_j^+, x_j^- \ge 0$|

## Esercizio svolto: trasformazione in forma standard

> [!example] Testo Scrivere in forma standard il problema $$ \begin{cases} \min\ 12x_1 + x_2 + 5x_3 \ x_2 - 2x_3 \ge 7 \ 2x_1 + x_3 \le 10 \ 3x_1 - x_2 - 2x_3 = 3 \ x_1 \ge 0,\ x_3 \ge 0 \end{cases} $$

> [!warning] Discrepanza tra fonti — il secondo vincolo Nella nota _Simplesso_ il secondo vincolo è scritto "$2x_1x_3 \le 10$", senza operatore tra i due termini (un prodotto renderebbe il vincolo non lineare). La seconda riga della matrice $A$ riportata nella stessa nota, $(2, 0, 0, 1, 1, 0)$, corrisponde a $2x_1 + x_3 + s_1 = 10$: si assume quindi il "$+$".

Il problema ha tre variabili, tre vincoli più i due vincoli di segno. Si procede un ostacolo alla volta.

1. Il primo vincolo è un "$\ge$": si sottrae una surplus, $x_2 - 2x_3 - u_1 = 7$ con $u_1 \ge 0$.
2. Il secondo vincolo è un "$\le$": si aggiunge una slack, $2x_1 + x_3 + s_1 = 10$ con $s_1 \ge 0$.
3. Il terzo vincolo è già un'uguaglianza.
4. Manca $x_2$, che non ha vincolo di segno: si pone $x_2 = x_2^+ - x_2^-$ con $x_2^\pm \ge 0$, sia nei vincoli sia nella funzione obiettivo.

Si ottiene

$$ \begin{cases} \min\ 12x_1 + x_2^+ - x_2^- + 5x_3 \ x_2^+ - x_2^- - 2x_3 - u_1 = 7 \ 2x_1 + x_3 + s_1 = 10 \ 3x_1 - x_2^+ + x_2^- - 2x_3 = 3 \ x_1,\ x_2^+,\ x_2^-,\ x_3,\ s_1,\ u_1 \ge 0 . \end{cases} $$

Da tre variabili si è passati a **sei**, ma ora tutte le variabili sono non negative e tutti i vincoli sono uguaglianze: il problema è in forma standard. La docente osserva che i nomi $u_1, s_1, x_2^+, x_2^-$ servono solo a ricordare da dove vengono; le variabili sono tutte uguali e si possono rinominare $x_4, x_5, \dots$, il che rende più facile tenerne traccia. Ordinando le colonne come $(x_1, x_2^+, x_2^-, x_3, s_1, u_1)$:

$$ A = \begin{pmatrix} 0 & 1 & -1 & -2 & 0 & -1 \ 2 & 0 & 0 & 1 & 1 & 0 \ 3 & -1 & 1 & -2 & 0 & 0 \end{pmatrix}, \qquad b = \begin{pmatrix} 7 \ 10 \ 3 \end{pmatrix}, \qquad c = \begin{pmatrix} 12 \ 1 \ -1 \ 5 \ 0 \ 0 \end{pmatrix}. $$

$A$ è $3 \times 6$: il numero di righe è più piccolo del numero di colonne. Lo si assumerà sempre per i problemi in forma standard, almeno all'inizio. Qui il rango è 3 (verificato). La docente nota anche che a volte è comodo avere $b \ge 0$; se non lo è si cambiano i segni di qualche equazione, ma in questo caso è già a posto.

> [!warning] Discrepanza tra fonti — la matrice $A$ dell'esercizio Nella nota _Simplesso_ la matrice è scritta con due righe sbagliate: la prima come $(0, 1, -1, -2, 0, 1)$ e la terza come $(3, 1, 1, 2, 0, 0)$. Il coefficiente di $u_1$ nella prima riga è $-1$ (la surplus si sottrae); nella terza riga, sostituendo $x_2 = x_2^+ - x_2^-$ in $3x_1 - x_2 - 2x_3$, si ottengono i coefficienti $-1$ per $x_2^+$, $+1$ per $x_2^-$ e $-2$ per $x_3$. La lettura della prima riga nella trascrizione ("0, 1, meno 1, meno 2") concorda con la versione corretta. Nella stessa nota la funzione obiettivo finale conserva $x_2$, che va invece sostituita con $x_2^+ - x_2^-$, e compare una riga isolata "$\operatorname{rank} x_2 = x_2^- x_2^-$" priva di senso, probabilmente un residuo di "$x_2 = x_2^+ - x_2^-$". Infine la trascrizione riporta $b = (7, 10, 13)$, quasi certamente un errore di trascrizione per $(7, 10, 3)$, il termine noto del terzo vincolo.

**Prima di tutto la forma standard.** Quando si parte da un problema qualunque, il primo passo è sempre metterlo in forma standard.

## Le ipotesi di lavoro

D'ora in poi si lavora sotto due ipotesi, che sono quelle della cosiddetta **fase 2** del metodo del simplesso:

$$ \operatorname{rk}(A) = m \qquad \text{e} \qquad P \neq \varnothing . $$

Si vedrà prima la fase 2 e poi la **fase 1**, il cui compito sarà proprio garantire queste ipotesi. La prima implica $m \le n$: il rango non supera mai il minimo tra numero di righe e numero di colonne. Poiché $P$ non contiene rette, sotto queste ipotesi $P$ ha vertici.

## Vertici di un poliedro in forma standard

Per i poliedri in forma generale i vertici si riconoscono guardando le **righe** dei vincoli attivi. Per la forma standard la condizione si legge più comodamente sulle **colonne** di $A$.

> [!important] Teorema — vertici in forma standard Sia $P = { x \in \mathbb{R}^n \mid Ax = b,\ x \ge 0 }$ con $A \in \mathbb{R}^{m \times n}$, $\operatorname{rk}(A) = m$ e $P \neq \varnothing$, e sia $\bar x \in P$. Allora $$ \bar x \text{ è un vertice di } P \iff \text{le colonne di } A \text{ corrispondenti alle componenti strettamente positive di } \bar x \text{ sono linearmente indipendenti.} $$

Un punto di $P$ ha alcune componenti nulle e alcune strettamente positive. Il teorema dice di guardare **solo** le colonne di $A$ in corrispondenza delle componenti positive.

> [!example] Esempi — $m = 2$, $n = 4$ Sia $A$ una matrice $2 \times 4$ e sia $\bar x = (1, 0, 2, 0) \in P$. Le componenti strettamente positive sono la prima e la terza: $\bar x$ è un vertice se e solo se la **prima e la terza colonna** di $A$ sono linearmente indipendenti.
> 
> Sia ora $\bar x = (1, 1, 2, 0) \in P$. Senza sapere nient'altro di $P$ si può dire che **non è un vertice**: bisognerebbe che fossero indipendenti la prima, la seconda e la terza colonna di $A$, ma sono tre vettori di $\mathbb{R}^2$, e tre vettori di $\mathbb{R}^2$ non sono mai linearmente indipendenti. È la risposta che uno studente ha dato a lezione.

> [!important] Corollario — al più $m$ componenti non nulle Ogni vertice di un poliedro in forma standard ha **al più $m$ componenti non nulle**: le colonne di $A$ vivono in $\mathbb{R}^m$, e più di $m$ vettori di $\mathbb{R}^m$ sono sempre dipendenti.

Si possono riconoscere facilmente anche i vertici con **una sola** componente non nulla. Una colonna da sola è linearmente indipendente se e solo se non è nulla, quindi un punto di $P$ con una sola componente positiva è un vertice se la colonna corrispondente è non nulla. La docente si è chiesta se si possano supporre colonne nulle assenti. In effetti possono comparire: se una variabile ha solo il vincolo di positività e non compare nelle uguaglianze, la sua colonna in $A$ è nulla. Ma si tratta di una variabile "che non serve a niente": la si può eliminare dal problema (a lezione: si toglie $x_1$, ponendola uguale a $0$, e si cancella la sua colonna), quindi non è restrittivo supporre che non ci siano colonne nulle.

> [!tip] Osservazione aggiunta sulle colonne nulle Eliminare una variabile con colonna nulla ponendola a $0$ è corretto quando il suo costo è non negativo. Se invece il costo $c_j$ di quella variabile è negativo, la variabile può crescere senza violare alcun vincolo e il problema è illimitato inferiormente. In entrambi i casi la variabile si tratta a parte e poi si toglie.

## Dimostrazione del teorema

L'unico strumento disponibile per riconoscere un vertice è, per ora, il teorema sul rango dei vincoli attivi, che vale per la forma generale. La dimostrazione consiste quindi nel riscrivere $P$ in forma generale e nell'applicare quel teorema.

**Passo 1: forma generale.** L'uguaglianza $Ax = b$ equivale alla coppia $Ax \ge b$, $-Ax \ge -b$ (a lezione la seconda è stata scritta prima con un segno sbagliato e poi corretta). Con i vincoli di segno:

$$ \underbrace{\begin{pmatrix} A \ -A \ I_n \end{pmatrix}}_{(2m + n) \times n} x ;\ge; \begin{pmatrix} b \ -b \ 0 \end{pmatrix}. $$

**Passo 2: vincoli attivi.** In un punto $\bar x \in P$ sono attivi:

- tutti i vincoli $Ax \ge b$ e tutti i vincoli $-Ax \ge -b$, perché $A\bar x = b$;
- i vincoli di segno $x_j \ge 0$ per le componenti **nulle** di $\bar x$.

Sia $r$ il numero di componenti strettamente positive di $\bar x$. Senza perdita di generalità (basta rinominare le variabili) si supponga che siano le prime $r$, e che le ultime $n - r$ siano nulle:

$$ \bar x = (\bar x_1, \dots, \bar x_r, 0, \dots, 0), \qquad \bar x_1, \dots, \bar x_r > 0 . $$

**Passo 3: il rango.** Per il teorema della forma generale, $\bar x$ è un vertice se e solo se la matrice dei vincoli attivi ha rango $n$. Le righe di $-A$ sono le opposte di quelle di $A$, quindi si possono cancellare senza cambiare il rango. Restano le $m$ righe di $A$ e le $n - r$ righe dell'identità che corrispondono alle componenti nulle:

$$ \tilde A = \begin{pmatrix} A_{[1..r]} & A_{[r+1..n]} \ 0 & I_{n-r} \end{pmatrix} \in \mathbb{R}^{(m + n - r) \times n}, $$

dove $A_{[1..r]}$ indica le prime $r$ colonne di $A$. Le righe in basso sono i vettori della base canonica $e_{r+1}^T, \dots, e_n^T$: hanno zeri nelle prime $r$ posizioni e l'identità $(n-r) \times (n-r)$ nelle ultime. È un'"identità troncata", lunga $n$ e non $n - r$.

> [!warning] Discrepanza nella trascrizione — l'indice dell'identità A lezione la matrice è stata scritta prima come $\begin{pmatrix} A \ I_{n-r} \end{pmatrix}$, accostando una matrice con $n$ colonne a un blocco quadrato $(n-r) \times (n-r)$. La docente si è corretta a voce ("non posso metterci il quadratino $n-r$ per $n-r$") e all'inizio della lezione 6 ha avvertito che l'indice scritto la volta precedente era sbagliato. La forma corretta è quella sopra, con il blocco nullo $(n - r) \times r$ a sinistra dell'identità. Anche la nota _Simplesso_ riporta la versione con $I_{n-r}$ e passaggi intermedi incompleti.

Una matrice con $n$ colonne ha rango $n$ se e solo se il suo nucleo è banale: $\tilde A x = 0 \Rightarrow x = 0$. Si spezza $x$ in due blocchi, $y = (x_1, \dots, x_r)$ e $z = (x_{r+1}, \dots, x_n)$:

$$ \tilde A \begin{pmatrix} y \ z \end{pmatrix} = 0 \iff \begin{cases} A_{[1..r]}, y + A_{[r+1..n]}, z = 0 \ z = 0 \end{cases} \iff \begin{cases} A_{[1..r]}, y = 0 \ z = 0 . \end{cases} $$

Il blocco in basso dà subito $z = 0$, cosa che si sapeva già; sostituendo, delle righe di $A$ contano solo le prime $r$ componenti. Quindi il nucleo di $\tilde A$ è banale se e solo se $A_{[1..r]}, y = 0 \Rightarrow y = 0$, cioè se e solo se **le prime $r$ colonne di $A$ sono linearmente indipendenti** (la matrice $A_{[1..r]}$ ha rango $r$).

Detto con le colonne, come alla fine della lezione: in $\tilde A$ le ultime $n - r$ colonne contengono l'identità e sono comunque indipendenti; per avere $n$ colonne indipendenti servono anche le prime $r$, cioè quelle di $A$ relative alle componenti positive. Mettendo insieme le equivalenze:

$$ \bar x \text{ vertice} \iff \operatorname{rk}(\tilde A) = n \iff \text{le colonne } A_1, \dots, A_r \text{ sono linearmente indipendenti.} \qquad \square $$

> [!tip] Approfondimento — La stessa dimostrazione nei testi #approfondimento Le dispense dimostrano lo stesso risultato con lo stesso schema (riscrittura in forma generale e teorema dei vincoli attivi) [@roma2023, Teorema 6.2.1]. Nelle note di Di Summa l'enunciato compare come caratterizzazione delle **soluzioni di base** del sistema in forma standard: un punto con $Ax = b$ è soluzione di base se e solo se le colonne ${A_j}_{j \in S}$, con $S = { j \mid \bar x_j \neq 0 }$, sono linearmente indipendenti [@disumma2015, Corollario 2.4]. Il legame tra "soluzione di base" e "vertice" è l'argomento della [[Lezione 06 - Matrici di base e soluzioni di base ammissibili|lezione 6]].

La procedura che si ricava dal teorema è:

```pseudo
procedura VERTICE_FORMA_STANDARD(A, b, x̄)     // P = { x ∈ R^n : A x = b, x ≥ 0 },  A di taglia m × n, rk(A) = m
    // passo 0: x̄ deve stare in P
    se A x̄ ≠ b oppure esiste j con x̄_j < 0 allora
        restituisci "x̄ non appartiene a P"
    S ← { j : x̄_j > 0 }                        // indici delle componenti strettamente positive
    se |S| > m allora
        restituisci "più di m componenti positive: non è un vertice"
    A_S ← sottomatrice di A con le colonne di indice in S
    se rango(A_S) = |S| allora                  // colonne linearmente indipendenti
        restituisci "x̄ è un vertice"
    altrimenti
        restituisci "x̄ non è un vertice"
```

## Riepilogo

- Un poliedro scritto come ${x \mid Ax \ge b}$ è in **forma generale**. Se $P \neq \varnothing$: $P$ ha almeno un vertice $\iff$ $P$ non contiene rette.
- **Teorema fondamentale**: se $P \neq \varnothing$ non contiene rette, il problema $\min c^T x$, $Ax \ge b$ o è illimitato inferiormente, o ha soluzione ottima e una soluzione è un vertice. Non può essere limitato dal basso senza minimo (a differenza di $1/x$ su $x > 0$).
- L'insieme delle soluzioni $S = P \cap {c^T x = m}$ è un poliedro convesso: le soluzioni sono zero, una o infinite.
- **Idea del simplesso**: spostarsi di vertice in vertice diminuendo il costo, invece di enumerare i vertici (il cubo $[0,1]^n$ ne ha $2^n$). Nel caso peggiore li visita tutti, in pratica quasi mai.
- **Forma standard**: $\min c^T x$, $Ax = b$, $x \ge 0$. Un poliedro in forma standard non vuoto ha sempre vertici. Si ottiene con slack ($\le$), surplus ($\ge$) e $x = x^+ - x^-$ per le variabili libere, aggiungendo variabili.
- Ipotesi della fase 2: $\operatorname{rk}(A) = m$ (quindi $m \le n$) e $P \neq \varnothing$.
- **Vertici in forma standard**: $\bar x \in P$ è un vertice $\iff$ le colonne di $A$ relative alle componenti strettamente positive sono linearmente indipendenti. Quindi un vertice ha al più $m$ componenti non nulle. Si dimostra riscrivendo $P$ in forma generale con la matrice $\begin{pmatrix} A \ -A \ I \end{pmatrix}$.