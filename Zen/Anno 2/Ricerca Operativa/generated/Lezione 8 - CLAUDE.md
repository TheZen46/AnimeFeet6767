---

## corso: Ricerca Operativa lezione: 8 data: 2026-10-16 docente: Silvia Villa argomenti: [fase 2 del simplesso, forma canonica, costi ridotti, unicità della soluzione ottima, test di illimitatezza, semiretta di decrescita, cambio di base, variabile entrante, variabile uscente, criterio del rapporto minimo, regole di scelta, pivot degenere] fonti: [trascrizione, appunti manuali, dispense] tags: [ricerca-operativa, lezione]

# Lezione 8 — Test di illimitatezza e cambio di base

> [!info] Fonti di questa nota Trascrizione della lezione del 16/10/2026 (un'unica parte), appunti manuali (scansione della lezione 8, due pagine) e nota Obsidian _Simplesso_ (seconda metà: esempio numerico, criteri, esercizio, aggiornamento della SBA). Le dispense [@roma2023, §6.4.1–6.4.3, §6.4.6] usano la stessa notazione ($\gamma$, $B^{-1}N$, indice entrante $h$, indice uscente $k$) e contengono lo stesso esempio grande della lezione; le note di Di Summa [@disumma2015, §3.2, §3.5] svolgono la stessa iterazione in forma tableau. Le parti prese solo da queste fonti, e i calcoli aggiunti per verifica, sono indicati esplicitamente.

La lezione completa la **fase 2** del metodo del simplesso. Dopo un ripasso del test di ottimalità, con un'aggiunta sull'unicità della soluzione, si vedono il **test di illimitatezza** e la **costruzione di una nuova soluzione di base ammissibile**: quale variabile entra in base, quale esce e di quanto ci si sposta (**criterio del rapporto minimo**).

## Il punto di partenza

Il problema è in forma standard,

$$ \begin{cases} \min\ c^T x \ Ax = b \ x \ge 0 \end{cases} \qquad c, x \in \mathbb{R}^n,\ A \in \mathbb{R}^{m \times n},\ b \in \mathbb{R}^m, \qquad P = { x \in \mathbb{R}^n \mid Ax = b,\ x \ge 0 }, $$

con le ipotesi aggiuntive della fase 2: $\operatorname{rk}(A) = m$ e $P \neq \varnothing$. La fase 2 parte assumendo di avere una **base ammissibile** $B$ ($m$ colonne linearmente indipendenti di $A$) e la corrispondente **SBA** $\bar x$, con $\bar x_B = B^{-1} b$ e $\bar x_N = 0$: un vertice del poliedro. I passi sono:

1. test di ottimalità;
2. test di illimitatezza;
3. costruzione di una nuova SBA.

Il primo è stato visto nella [[Lezione 07 - Vertici degeneri e fase 2 del simplesso|lezione 7]]; oggi si vedono il secondo e il terzo. Tutto si basa sulla **forma canonica** rispetto a $B$:

$$ \begin{cases} \min\ c_B^T B^{-1} b + \left( c_N^T - c_B^T B^{-1} N \right) x_N \ x_B = B^{-1} b - B^{-1} N x_N \ x_B \ge 0,\ x_N \ge 0 \end{cases} \qquad \gamma^T = c_N^T - c_B^T B^{-1} N \ \text{(costi ridotti)} . $$

Perché questa forma è vantaggiosa? Le componenti $x_B$ sono determinate direttamente dalla scelta di $x_N$: si sceglie $x_N \ge 0$, si calcola $x_B$ con la formula, e se il risultato è non negativo si ha un punto del poliedro. Tutte le coppie $(x_B, x_N)$ che verificano l'equazione verificano automaticamente $Ax = b$, perché quella è solo una riscrittura di $Ax = b$. Inoltre la funzione obiettivo è scritta usando **solo** $x_N$. Nel vertice corrente $x_N = 0$, quindi il valore è $c_B^T B^{-1} b$; ma la stessa scrittura permette di calcolare il valore in **altri** punti del poliedro, che avranno $x_N \neq 0$, semplicemente usando le loro coordinate fuori base.

> [!example] Esempio — calcolare la funzione obiettivo da $\gamma$ Si supponga che $\bar x = (1, 1, 0, 0)$ sia una SBA con indici in base $I_B = {1, 2}$, cioè $\bar x_B = (1, 1)$ e $\bar x_N = (0, 0)$; che il vettore dei costi ridotti sia $\gamma^T = (-1, 0)$ (due componenti, come le variabili fuori base); e che, posto $f(x) = c^T x$, sia $f(\bar x) = 12$. Quanto vale la funzione obiettivo nel punto $(1, 1, 3, 0)$, supposto ammissibile?
> 
> Il problema non è stato scritto, ma non serve. Le coordinate in base del nuovo punto sono le prime due, $(1, 1)$, quelle fuori base sono $x_N = (3, 0)$. Quindi $$ f(x) = c_B^T B^{-1} b + \gamma^T x_N = 12 + (-1, 0) \begin{pmatrix} 3 \ 0 \end{pmatrix} = 12 - 3 = 9 . $$

## Ottimalità e unicità

Il criterio di ottimalità dice che se $\gamma \ge 0$ la SBA corrente è ottima. È una condizione **sufficiente ma non necessaria**: potrebbero esserci soluzioni ottime con qualche costo ridotto negativo, ma se $\gamma \ge 0$ l'ottimalità è garantita. La docente aggiunge un'osservazione che non serve per l'algoritmo ma è utile.

> [!important] Proposizione — unicità della soluzione ottima Sia $B$ una matrice di base ammissibile. Se il vettore dei costi ridotti ha tutte le componenti **strettamente** positive, $$ \gamma > 0 , $$ allora la SBA $\bar x$ è l'**unica** soluzione ottima.

_Dimostrazione._ Sia $x \in P$ con $x \neq \bar x$. Allora $x_N$ ha almeno una componente non nulla: se fosse $x_N = 0$, dalla formula $x_B = B^{-1} b - B^{-1} N x_N$ seguirebbe $x_B = B^{-1} b$, cioè $x = \bar x$. Poiché $x_N \ge 0$ con almeno una componente positiva e $\gamma$ ha tutte le componenti strettamente positive, $\gamma^T x_N > 0$, e quindi

$$ f(x) = c^T x = c_B^T B^{-1} b + \gamma^T x_N ;>; c_B^T B^{-1} b = c^T \bar x = f(\bar x) . $$

Ogni altro punto del poliedro ha valore strettamente maggiore. $\square$

Quando si applica il test di ottimalità si può quindi capire anche se la soluzione è unica. Nella [[Lezione 05 - Teorema fondamentale e forma standard|lezione 5]] si era visto un poliedro con la funzione obiettivo parallela a un lato e infinite soluzioni (un segmento): la condizione $\gamma > 0$ esclude questa possibilità, perché c'è un solo vertice che tocca la retta di livello ottima. Il risultato è anche nelle dispense [@roma2023, Corollario 6.4.1].

## Il test di illimitatezza

Se si arriva al test di illimitatezza, il test di ottimalità è fallito: il vettore dei costi ridotti non ha tutte le componenti $\ge 0$, quindi ne ha almeno una **strettamente negativa**. Sia $h$ un indice con $\gamma_h < 0$; attenzione, $h$ indica una posizione tra le variabili **fuori base**, non un indice qualsiasi di ${1, \dots, n}$. Si guarda la colonna corrispondente di $B^{-1} N$.

> [!important] Teorema — criterio di illimitatezza Sia $B$ una matrice di base ammissibile e sia $h$ un indice tale che
> 
> 1. $\gamma_h < 0$;
> 2. la colonna $h$-esima di $B^{-1} N$, indicata con $[B^{-1} N]_h$, ha tutte le componenti **negative o nulle**: $[B^{-1} N]_h \le 0$.
> 
> Allora il problema è **illimitato inferiormente**.

A lezione la docente ha prima scritto "tutte entrate negative" e si è corretta: "negative o nulle, per essere precisi; anche lo $0$ va bene". Ha anche detto, per un lapsus, "il problema è limitato" intendendo "illimitato".

_Dimostrazione._ L'idea è simile a quella del criterio di ottimalità. Si costruisce una famiglia di punti del poliedro su cui la funzione obiettivo scende indefinitamente.

**Il punto.** Al posto di $x_N$, che nella SBA corrente è tutto nullo, si mette un valore non nullo solo nella componente $h$:

$$ x_N = t, e_h = t, (0, \dots, 0, \underset{h}{1}, 0, \dots, 0)^T, \qquad t > 0 , $$

dove $e_h$ è il vettore $h$-esimo della base canonica di $\mathbb{R}^{n-m}$, e si definisce

$$ x_B = B^{-1} b - B^{-1} N x_N . $$

Per costruzione la coppia $(x_B, x_N)$ verifica $Ax = b$: è come scrivere $Ax = b$.

**È nel poliedro.** Poiché $t > 0$, $x_N \ge 0$: le sue componenti sono $0$ oppure $t$. Per $x_B$, il prodotto di una matrice per un vettore della base canonica **seleziona la colonna** corrispondente:

$$ x_B = B^{-1} b - B^{-1} N \begin{pmatrix} 0 \ \vdots \ t \ \vdots \ 0 \end{pmatrix} = \underbrace{B^{-1} b}_{\ge 0} - \underbrace{[B^{-1} N]_h}_{\le 0}\ t ;\ge; 0 . $$

$B^{-1} b \ge 0$ perché si è partiti da una soluzione di base ammissibile. A ogni sua componente si sottrae $t$ volte la componente corrispondente della colonna $[B^{-1}N]_h$, che è negativa o nulla: "meno per meno fa più", si aggiunge qualcosa di non negativo. Quindi $x_B \ge 0$ **qualunque sia $t > 0$**. Geometricamente: partendo dal vertice corrente ci si muove lungo una **semiretta**, al variare di $t \ge 0$, che sta tutta dentro il poliedro, perché le sue coordinate verificano $Ax = b$ e sono non negative.

**La funzione obiettivo decresce.** Sulla semiretta

$$ f(x) = c_B^T B^{-1} b + \gamma^T x_N = c_B^T B^{-1} b + \gamma^T (t, e_h) = c_B^T B^{-1} b + t, \gamma_h , $$

perché il prodotto scalare di $\gamma$ con $e_h$ è la componente $h$-esima di $\gamma$. Poiché $\gamma_h < 0$ (scelto apposta), per esempio $-3$,

$$ \lim_{t \to +\infty} \left( c_B^T B^{-1} b + t, \gamma_h \right) = -\infty . $$

A lezione qualcuno ha risposto "più infinito": se tendesse a $+\infty$ non sarebbe un problema, perché si sta cercando il minimo. Si è trovata un'intera semiretta di punti ammissibili su cui la funzione obiettivo diminuisce sempre di più: il problema è illimitato inferiormente. $\square$

> [!tip] Schema da disegnare Figura consigliata in Excalidraw: un poliedro illimitato di $\mathbb{R}^2$ con un vertice $\bar x$ da cui partono due spigoli; uno dei due è una semiretta che va all'infinito. Sulla semiretta si segnano alcuni punti $x(t) = \bar x + t,d$ per $t = 1, 2, 3$ con i valori decrescenti della funzione obiettivo, e il vettore $-c$ che punta nello stesso verso della semiretta.

> [!tip] Approfondimento — La direzione di illimitatezza come certificato #approfondimento I punti della semiretta si scrivono $x(t) = \bar x + t, r$ con la direzione $r$ data da $r_N = e_h$ e $r_B = -[B^{-1}N]_h$. Le note di Di Summa osservano che questa direzione funziona da **qualunque** punto ammissibile, non solo da $\bar x$: per ogni $x \in P$ e ogni $t \ge 0$ la semiretta $x + t,r$ sta in $P$ e lungo di essa la funzione obiettivo diverge. Il vettore $r$, detto **raggio**, è quindi una "prova" dell'illimitatezza che si può verificare indipendentemente dall'algoritmo [@disumma2015, §3.2] (in quel testo il problema è di massimo, quindi la funzione cresce a $+\infty$). Nelle dispense il criterio è il Teorema 6.4.2, dimostrato allo stesso modo [@roma2023].

## Esercizio: un problema illimitato

> [!example] Testo $$ \begin{cases} \min\ -x_1 - x_2 \ x_1 - x_2 + x_3 = 1 \ -x_1 + x_2 + x_4 = 1 \ x_1, x_2, x_3, x_4 \ge 0 \end{cases} \qquad A = \begin{pmatrix} 1 & -1 & 1 & 0 \ -1 & 1 & 0 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \ 1 \end{pmatrix}. $$ Mostrare che il problema è illimitato inferiormente.

> [!warning] Discrepanza tra fonti — il primo vincolo Nella nota _Simplesso_ il primo vincolo è scritto "$x_1 - x_2 = x_3 = 1$", con un "$=$" al posto del "$+$". La matrice $A$, concorde nella nota, negli appunti scansionati e nella trascrizione, fissa il vincolo $x_1 - x_2 + x_3 = 1$.

Ci sarebbe una base molto naturale da cui partire, l'identità formata dalle colonne 3 e 4. "Ci avvantaggiamo un po'" e si parte invece dalla base formata dalle **colonne 1 e 4**:

$$ B = \begin{pmatrix} 1 & 0 \ -1 & 1 \end{pmatrix}, \quad \det B = 1, \quad B^{-1} = \begin{pmatrix} 1 & 0 \ 1 & 1 \end{pmatrix}, \quad B^{-1} b = \begin{pmatrix} 1 \ 2 \end{pmatrix} \ge 0 . $$

$B$ è una matrice di base ammissibile e $\bar x = (1, 0, 0, 2)$ è una SBA: prima e quarta componente in base, $\bar x_B = (1, 2)$, $\bar x_N = (0, 0)$.

**Con le formule.** Il vettore costo è $c = (-1, -1, 0, 0)$, quindi

$$ c_B^T = (-1,\ 0), \quad c_N^T = (-1,\ 0), \quad N = \begin{pmatrix} -1 & 1 \ 1 & 0 \end{pmatrix}, \quad B^{-1} N = \begin{pmatrix} 1 & 0 \ 1 & 1 \end{pmatrix} \begin{pmatrix} -1 & 1 \ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 1 \ 0 & 1 \end{pmatrix}, $$

$$ \gamma^T = c_N^T - c_B^T B^{-1} N = (-1,\ 0) - (-1,\ 0) \begin{pmatrix} -1 & 1 \ 0 & 1 \end{pmatrix} = (-1,\ 0) - (1,\ -1) = (-2,\ 1) . $$

Il vettore dei costi ridotti ha un'entrata negativa, $\gamma_1 = -2$: il test di ottimalità fallisce e si passa al test di illimitatezza. La prima colonna di $B^{-1} N$ è $(-1, 0)^T$: entrate negative o nulle. **Il problema è illimitato**: non ha minimo, la funzione obiettivo va a $-\infty$.

**A mano.** Dopo la pausa l'esercizio è stato rifatto "senza sapere niente", per capire che cosa succede. Si scrivono le variabili in base, $x_1$ e $x_4$, in funzione di quelle fuori base, $x_2$ e $x_3$. Dalla prima equazione $x_1 = 1 + x_2 - x_3$; dalla seconda $x_4 = 1 + x_1 - x_2 = 2 - x_3$. Sostituendo la prima nella funzione obiettivo, $-x_1 - x_2 = -1 - 2x_2 + x_3$:

$$ \begin{cases} \min\ -1 - 2x_2 + x_3 \ x_1 = 1 + x_2 - x_3 \ x_4 = 2 - x_3 \ x \ge 0 . \end{cases} $$

Si riconoscono il valore nella SBA corrente, $c_B^T B^{-1} b = -1$, e il vettore dei costi ridotti $(-2, 1)$. La matrice $B^{-1} N$ si rilegge dai coefficienti delle variabili fuori base, **cambiati di segno** perché $x_B = B^{-1}b - B^{-1}N x_N$: per $x_1$, il coefficiente di $x_2$ è $+1$ e quello di $x_3$ è $-1$, quindi la riga è $(-1, 1)$; per $x_4$ manca $x_2$ e il coefficiente di $x_3$ è $-1$, quindi la riga è $(0, 1)$.

Che cosa si vede? $x_2$ ha coefficiente negativo nella funzione obiettivo, quindi aumentandolo la funzione diminuisce. D'altra parte $x_2$ ha coefficienti positivi o nulli nelle uguaglianze: aumentando $x_2$ (con $x_3 = 0$), $x_1 = 1 + x_2$ resta positiva e $x_4 = 2$ non cambia. Problemi di positività non ce ne sono, si può aumentare $x_2$ quanto si vuole e la funzione obiettivo diminuisce quanto si vuole. "È la terza volta che vediamo il teorema": prima l'enunciato, poi l'esempio con le formule, infine la spiegazione concreta.

> [!example] Verifica — la semiretta esplicita (calcolo aggiunto) Con $x_2 = t \ge 0$ e $x_3 = 0$: $x(t) = (1 + t,\ t,\ 0,\ 2)$. Controllo: $(1 + t) - t + 0 = 1$ e $-(1 + t) + t + 2 = 1$, tutte le componenti sono non negative, e $f(x(t)) = -(1 + t) - t = -1 - 2t \to -\infty$. È la formula generale $c_B^T B^{-1} b + t, \gamma_1 = -1 - 2t$.

## Quando nessuno dei due test conclude

Se entrambi i test falliscono:

- il test di ottimalità non è superato, quindi esiste $\gamma_h < 0$;
- il test di illimitatezza non è superato, quindi **in corrispondenza di ogni** entrata strettamente negativa di $\gamma$, la colonna corrispondente di $B^{-1} N$ ha almeno un elemento **strettamente positivo**.

Si fissa allora un indice $h$ con $\gamma_h < 0$; esiste un elemento $[B^{-1} N]_{ih} > 0$. Non si può dire né che la soluzione corrente sia ottima né che il problema sia illimitato: bisogna **cambiare la soluzione di base ammissibile**.

## La costruzione della nuova SBA

Più avanti si vedrà un modo molto algoritmico di farlo, senza calcolare inverse; prima si capisce che cosa si fa. Il metodo del simplesso cambia la SBA "in maniera economica": rende positiva **una sola** componente fuori base. Come nel test di illimitatezza:

$$ \begin{cases} \bar x_B = B^{-1} b \ \bar x_N = 0 \end{cases} \quad \longrightarrow \quad \begin{cases} x_B = B^{-1} b - B^{-1} N, t, e_h \ x_N = t, e_h . \end{cases} $$

Geometricamente: si è in un vertice del poliedro e ci si muove lungo uno spigolo (una semiretta, la stessa di prima); il modo in cui ci si muove garantirà di finire in un altro vertice. Restano due domande:

1. **in che direzione ci si muove**, cioè quale variabile fuori base far crescere;
2. **quando ci si ferma**, cioè quanto prendere grande $t$ senza uscire dal poliedro.

> [!warning] Discrepanza nella notazione — l'indice $k$ A lezione (e nella nota _Simplesso_) il vettore della base canonica è scritto prima $e_k$, con $k$ "da scegliere"; poi si sceglie $k = h$, e la lettera $k$ viene riusata per l'indice della variabile **uscente** ("ho fatto una pessima scelta di $k$", commenta la docente). In questa nota, come nelle dispense, $h$ indica sempre la variabile **entrante** e $k$ quella **uscente**.

**La direzione: chi entra.** L'obiettivo è **diminuire la funzione obiettivo**. Lungo la direzione $e_h$ il valore è $c_B^T B^{-1} b + t,\gamma_h$; se $\gamma_h < 0$, la funzione diminuisce al crescere di $t$. Si sceglie quindi di aumentare una variabile fuori base con **costo ridotto negativo**: la variabile $(x_N)_h$ con $\gamma_h < 0$ **entra in base**. Le altre variabili fuori base restano nulle.

**Il passo: quanto vale $t$.** Il nuovo punto deve essere ammissibile. $x_N = t,e_h \ge 0$ per costruzione; per $x_B$, componente per componente,

$$ (x_B)_j = (B^{-1} b)_j - [B^{-1} N]_{jh}\ t ;\ge; 0 \qquad \text{per ogni } j = 1, \dots, m . $$

Ci sono due casi.

- Se $[B^{-1} N]_{jh} \le 0$, allora $(x_B)_j \ge 0$ **per ogni** $t \ge 0$: è esattamente la situazione del test di illimitatezza, e in quella direzione la positività è garantita.
- Se $[B^{-1} N]_{jh} > 0$, i problemi ci sono: risolvendo la disuguaglianza, $$ t \le \frac{(B^{-1} b)_j}{[B^{-1} N]_{jh}} . $$

Per garantire che $(x_B, x_N)$ sia ammissibile bisogna rispettare **tutti** questi vincoli, quindi prendere $t$ non più grande del più piccolo. C'è almeno un $j$ con denominatore strettamente positivo, perché il test di illimitatezza è fallito.

> [!important] Criterio del rapporto minimo Sia $h$ l'indice della variabile entrante ($\gamma_h < 0$). Si sceglie $$ t = \min_{, j ,:, [B^{-1} N]_{jh} > 0} \ \frac{(B^{-1} b)_j}{[B^{-1} N]_{jh}} $$ e sia $k$ un indice su cui si ottiene il minimo. La nuova SBA si ottiene
> 
> - facendo **entrare** in base $(x_N)_h$, la variabile fuori base con $\gamma_h < 0$;
> - facendo **uscire** di base $(x_B)_k$, la variabile in base corrispondente al rapporto minimo.

Perché $t$ esattamente uguale al minimo, e non più piccolo? Con $t$ uguale al minimo, nella componente $k$ si ottiene $(x_B)_k = 0$: almeno una variabile in base si annulla (forse più di una, ma una di certo). È quella che esce: se ne entra una, ne deve uscire una. Il nuovo punto ha ancora $m$ variabili "in base" e le altre nulle, ed è una nuova SBA; il valore della funzione obiettivo è $c_B^T B^{-1} b + t,\gamma_h$, **minore o uguale** a quello corrente, e si è cambiata una sola variabile fuori base.

> [!warning] Discrepanza tra fonti — chi esce di base Nell'ultima riga della nota _Simplesso_ si legge "facendo uscire $(x_B)_h$". La variabile uscente è $(x_B)_k$, quella con indice $k$ del rapporto minimo, come riportato poche righe sopra nella stessa nota e nella scansione.

> [!tip] Approfondimento — Perché la nuova matrice è di base, e quando il passo è nullo #approfondimento Che le nuove colonne siano ancora linearmente indipendenti segue da un conto sul determinante. Indicando con $B'$ la matrice ottenuta da $B$ sostituendo la colonna uscente con quella entrante, si ha $B^{-1} B' = E$, dove $E$ è l'identità con la colonna $k$ sostituita da $[B^{-1}N]_h$; quindi $\det E = [B^{-1}N]_{kh} > 0$, e $B' = B,E$ è invertibile [@disumma2015, §3.2]. Le dispense formalizzano la scelta come Teorema 6.4.4 e osservano due fatti utili [@roma2023, Osservazioni 6.4.7 e 6.4.8]. Primo, se il minimo è raggiunto su più indici, la nuova SBA è **degenere**: si annullano tutte le variabili in base relative agli indici del minimo. Secondo, il passo $t$ è nullo se e solo se $(B^{-1}b)_k = 0$, il che richiede che la SBA corrente sia degenere: in quel caso cambia la base ma **non** il punto (si parla di _pivot degenere_), ed è il fenomeno annunciato nella lezione 5 dei "passi che ci tengono nello stesso vertice".

## Le regole di scelta

Ci sono due punti in cui l'algoritmo deve scegliere.

**Chi entra.** Se più costi ridotti sono negativi, la regola che si usa di solito, e che si userà sempre nel corso, è far entrare la variabile con il **costo ridotto più negativo**. È un'euristica di buon senso: si vuole diminuire la funzione obiettivo, e un costo ridotto $-3$ la fa diminuire di $3$ per ogni unità della variabile, contro $1$ per un costo ridotto $-1$. Non garantisce però di diminuire di più, perché il passo $t$ può essere diverso nelle due direzioni; e nessuno obbliga a sceglierla.

**Chi esce.** Se il rapporto minimo è raggiunto su più indici, per convenzione esce la variabile corrispondente all'**indice più piccolo**. "Vedremo che ha un senso."

> [!important] Attenzione — l'errore tipico all'esame I rapporti $(B^{-1} b)_j / [B^{-1} N]_{jh}$ si calcolano **solo** per i $j$ con $[B^{-1} N]_{jh} > 0$, non sulle entrate negative o nulle: su quelle non c'è alcun vincolo per $t$.

L'iterazione completa della fase 2 si può scrivere così:

```pseudo
procedura ITERAZIONE_FASE_2(A, b, c, I_B)      // I_B: indici di una base ammissibile
    I_N ← {1, …, n} \ I_B
    B ← colonne di A con indici in I_B;  N ← colonne di A con indici in I_N
    x̄_B ← B⁻¹ b;  x̄_N ← 0                       // SBA corrente
    γᵀ ← c_Nᵀ − c_Bᵀ B⁻¹ N                        // costi ridotti
    // 1. test di ottimalità
    se γ ≥ 0 allora
        restituisci "x̄ è ottima"                  // unica se γ > 0
    // 2. test di illimitatezza
    per ogni h con γ_h < 0:
        se [B⁻¹N]_h ≤ 0 allora
            restituisci "problema illimitato inferiormente"
    // 3. cambio di base
    h ← indice con γ_h minimo (il più negativo)  // regola usata nel corso
    t ← min { (B⁻¹b)_j / [B⁻¹N]_jh  :  [B⁻¹N]_jh > 0 }
    k ← il più piccolo indice j su cui si ottiene il minimo
    entra in base (x_N)_h, esce di base (x_B)_k
    restituisci la nuova base I_B                 // e si ripete dal passo 1
```

## Esempio: la prima iterazione su un problema più grande

> [!example] Testo $$ \begin{cases} \min\ x_1 + 2x_2 + x_3 + x_4 + x_5 + x_6 \ x_1 + 2x_2 + 3x_3 + x_4 = 3 \ 2x_1 - x_2 - 5x_3 + x_5 = 2 \ x_1 + 2x_2 - x_3 + x_6 = 1 \ x \ge 0 \end{cases} \qquad A = \begin{pmatrix} 1 & 2 & 3 & 1 & 0 & 0 \ 2 & -1 & -5 & 0 & 1 & 0 \ 1 & 2 & -1 & 0 & 0 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 3 \ 2 \ 1 \end{pmatrix}. $$ Con $x \ge 0$ si intende che tutte le componenti sono non negative.

> [!warning] Discrepanza tra fonti — la funzione obiettivo Nella trascrizione la funzione obiettivo è letta come "$x_1 + x_2 + x_3 + x_4 + x_5$", probabilmente in modo incompleto. Gli appunti scansionati riportano $x_1 + 2x_2 + x_3 + x_4 + x_5 + x_6$, coerente con i vettori $c_B = (1, 1, 1)$ e $c_N = (1, 2, 1)$ letti a lezione; si segue la scansione. È anche il problema dell'Esempio 6.4.2 delle dispense [@roma2023].

Si è fortunati: il problema è già in forma standard. $\operatorname{rk}(A) = 3$, perché nelle ultime tre colonne c'è la matrice identità; il numero di righe è minore del numero di colonne. E il poliedro non è vuoto: con la base identità, formata dalle colonne di $x_4, x_5, x_6$,

$$ B = I, \qquad B^{-1} b = \begin{pmatrix} 3 \ 2 \ 1 \end{pmatrix} \ge 0 , $$

quindi la SBA corrente è $\bar x = (0, 0, 0, 3, 2, 1)$, con $\bar x_B = (3, 2, 1)$, $\bar x_N = (0, 0, 0)$, $I_B = {4, 5, 6}$, $I_N = {1, 2, 3}$. Il valore della funzione obiettivo è $c_B^T B^{-1} b = 3 + 2 + 1 = 6$ (calcolo aggiunto).

**1. Test di ottimalità.** Poiché $B = I$, si ha $B^{-1} N = N$, le prime tre colonne di $A$. Con $c_B^T = (1, 1, 1)$ e $c_N^T = (1, 2, 1)$:

$$ \gamma^T = c_N^T - c_B^T B^{-1} N = (1,\ 2,\ 1) - (1,\ 1,\ 1) \begin{pmatrix} 1 & 2 & 3 \ 2 & -1 & -5 \ 1 & 2 & -1 \end{pmatrix} = (1,\ 2,\ 1) - (4,\ 3,\ -3) = (-3,\ -1,\ 4) . $$

$\gamma_1$ e $\gamma_2$ sono negativi: la SBA corrente non soddisfa il criterio di ottimalità.

**2. Test di illimitatezza.** Per $\gamma_1 < 0$ si guarda la prima colonna di $B^{-1} N$, $(1, 2, 1)^T$: ha elementi strettamente positivi. Per $\gamma_2 < 0$ la seconda colonna, $(2, -1, 2)^T$: ha elementi strettamente positivi. Il test di illimitatezza fallisce: **non si può affermare** che il problema sia illimitato.

> [!warning] Discrepanza tra fonti — l'esito del test di illimitatezza Negli appunti scansionati si legge "il problema non è illimitato". La docente lo ha scritto così avvertendo che è sbagliato: la cosa giusta da scrivere è che **non si può affermare** che il problema sia illimitato, perché a un'iterazione successiva il test potrebbe risultare soddisfatto.

**3. Cambio di base.** Entra la variabile con il costo ridotto più negativo, $\gamma_1 = -3$. Attenzione: entra in base $x_1$ non perché sia "$x_1$", ma perché è la **prima variabile fuori base**; qui $I_N = {1, 2, 3}$ e le due cose coincidono. Si calcolano i rapporti tra le componenti di $B^{-1} b = (3, 2, 1)$ e quelle della prima colonna di $B^{-1} N$, che sono tutte strettamente positive, quindi i rapporti sono tre:

|$j$|variabile in base|$(B^{-1} b)_j$|$[B^{-1} N]_{j1}$|rapporto|
|---|---|---|---|---|
|1|$x_4$|$3$|$1$|$3$|
|2|$x_5$|$2$|$2$|$\mathbf{1}$|
|3|$x_6$|$1$|$1$|$\mathbf{1}$|

Il minimo, $t = 1$, è raggiunto su due indici: potrebbe uscire sia la seconda variabile in base sia la terza. Per convenzione esce quella di indice più piccolo, la **seconda**, cioè $x_5$. Entra la prima variabile fuori base ed esce la seconda in base: $x_1$ prende il posto di $x_5$ e viceversa.

$$ I_B^{(1)} = {4, 1, 6}, \qquad I_N^{(1)} = {5, 2, 3} . $$

I conti con la nuova base sono rimandati alla lezione successiva, dove si vedrà "un modo furbo", che peraltro si conosce già, per farli.

> [!warning] Discrepanze nella trascrizione e negli appunti — rapporti e variabile uscente Nella trascrizione i rapporti sono letti in modo confuso ("3 fratto 1, già è uguale a 2; 2 fratto 2, già è uguale a 3"), ma subito dopo la docente riassume correttamente "3, 1, 1"; i valori in tabella sono quelli degli appunti scansionati e sono verificati. Negli appunti il passo è intitolato "Variabile entrante: criterio r.m.": il criterio del rapporto minimo seleziona la variabile **uscente**.

> [!example] Verifica — la nuova SBA (calcolo non svolto a lezione) Con $x_N = t,e_1$ e $t = 1$: $$ x_B = B^{-1} b - [B^{-1}N]_1, t = \begin{pmatrix} 3 \ 2 \ 1 \end{pmatrix} - \begin{pmatrix} 1 \ 2 \ 1 \end{pmatrix} = \begin{pmatrix} 2 \ 0 \ 0 \end{pmatrix}, \qquad x_1 = 1 . $$ La nuova SBA è $x = (1, 0, 0, 2, 0, 0)$, con $(x_4, x_1, x_6) = (2, 1, 0)$ rispetto alla base ${4, 1, 6}$. Il valore della funzione obiettivo è sceso da $6$ a $6 + t,\gamma_1 = 6 - 3 = 3$ (controllo diretto: $1 + 2 = 3$). La nuova SBA è **degenere**: $x_6$ è in base ma vale $0$, conseguenza del pareggio nel rapporto minimo (si sono annullate sia $x_5$ sia $x_6$).

> [!tip] Approfondimento — Come prosegue l'esempio #approfondimento Lo stesso problema è trattato nelle dispense, che mostrano che $(1, 0, 0, 2, 0, 0)$ è l'**unica** soluzione ottima: con la base ${1, 3, 4}$ i costi ridotti sono $(10/3, 1/3, 7/3) > 0$ [@roma2023, Esempio 6.4.2]. Con la base ${1, 4, 6}$ raggiunta qui, invece, i costi ridotti relativi a $(x_2, x_3, x_5)$ sono $(-5/2, -7/2, 3/2)$: il test di ottimalità fallisce anche se la soluzione è già ottima [@roma2023, Esempio 6.4.3]. È il caso "sufficiente ma non necessario" della lezione 7. Applicando ancora le regole del corso (calcolo di verifica, da confrontare con la prossima lezione) entra $x_3$, il rapporto minimo vale $0$ ed esce $x_6$: un pivot degenere porta alla base ${4, 1, 3}$, nello stesso punto, dove il criterio di ottimalità è finalmente soddisfatto.

## Esempio: completamento dell'esempio della lezione 7

> [!example] Svolgimento (calcolo non svolto a lezione) Si riprende il problema della lezione 7, $$ \min\ 2x_1 + x_2 + x_3 - x_4, \quad x_1 + 2x_2 + x_3 - x_4 = 1, \quad x_2 + x_3 = 1, \quad x \ge 0, $$ dalla base $I_B = {1, 3}$, SBA $(0, 0, 1, 0)$ (degenere), con $B^{-1} b = (0, 1)$, $B^{-1} N = \begin{pmatrix} 1 & -1 \ 1 & 0 \end{pmatrix}$ (colonne relative a $x_2, x_4$) e $\gamma = (-2, 1)$.
> 
> _Iterazione 1._ Entra $x_2$ ($\gamma = -2$). La colonna $(1, 1)^T$ ha entrate positive, quindi il test di illimitatezza non conclude. Rapporti: $0/1 = 0$ (riga di $x_1$) e $1/1 = 1$ (riga di $x_3$). Il minimo è $t = 0$: esce $x_1$. È un **pivot degenere**: la nuova base è ${2, 3}$ ma il punto resta $(0, 0, 1, 0)$, con valore $1$.
> 
> _Iterazione 2._ Con $I_B = {2, 3}$: $x_2 = x_4 - x_1$, $x_3 = 1 + x_1 - x_4$, e la funzione obiettivo diventa $1 + 2x_1 - x_4$, quindi $\gamma = (2, -1)$ per $(x_1, x_4)$. Entra $x_4$; la sua colonna in $B^{-1}N$ è $(-1, 1)^T$ (coefficienti cambiati di segno), con un solo elemento positivo, nella riga di $x_3$: rapporto $1/1 = 1$, esce $x_3$. Nuova base ${2, 4}$, nuova SBA $(0, 1, 0, 1)$, valore $1 + 1 \cdot (-1) = 0$.
> 
> _Iterazione 3._ Con $I_B = {2, 4}$: $x_2 = 1 - x_3$, $x_4 = 1 + x_1 - x_3$, funzione obiettivo $x_1 + x_3$, quindi $\gamma = (1, 1) > 0$. La soluzione $(0, 1, 0, 1)$ è l'**unica** soluzione ottima, con valore $0$. È il vertice non degenere trovato nell'esercizio per casa della lezione 7.

## Approfondimento: il ciclaggio

> [!tip] Approfondimento — Pivot degeneri, ciclaggio e regola di Bland #approfondimento Con le regole del corso (entra il costo ridotto più negativo, esce l'indice più piccolo) il metodo del simplesso può, in rari casi, **ciclare**: una sequenza di pivot degeneri, tutti nello stesso vertice, riporta a una base già visitata, e da lì la sequenza si ripete all'infinito. Le dispense riportano un esempio classico dovuto a Beale in cui, partendo dalla base $(a_1, a_2, a_3)$ e con scelte "molto naturali, e coerenti con le scelte usate in classe", dopo sei cambi di base si torna alla base iniziale senza mai raggiungere quella ottima [@roma2023, Esempio 6.4.15]. Il rimedio più semplice è la **regola di Bland**: tra le variabili candidate a entrare si sceglie quella di indice più piccolo, e lo stesso per quelle candidate a uscire. Con questa regola il simplesso non visita mai due volte la stessa base e termina sempre [@bland1977; @roma2023, Teorema 6.4.8; @disumma2015, Teorema 3.4]. La convenzione del corso per la variabile uscente è già la metà di Bland; quella per la variabile entrante no. In pratica, osservano le dispense, il ciclaggio è raro e le regole anti-ciclaggio si possono attivare anche ad algoritmo iniziato. Si noti che la regola di Bland si riferisce agli **indici delle variabili**; nell'esempio della lezione le due letture della convenzione (posizione in base o indice della variabile) danno lo stesso risultato, $x_5$.

## Riepilogo

- Fase 2: dati una base ammissibile $B$ e la SBA $\bar x$, si eseguono test di ottimalità, test di illimitatezza e cambio di base. In forma canonica $f(x) = c_B^T B^{-1} b + \gamma^T x_N$ per ogni $x \in P$.
- $\gamma \ge 0 \Rightarrow \bar x$ ottima; $\gamma > 0 \Rightarrow \bar x$ unica soluzione ottima.
- **Test di illimitatezza**: se $\gamma_h < 0$ e $[B^{-1} N]_h \le 0$, la semiretta $x_N = t,e_h$, $x_B = B^{-1}b - [B^{-1}N]_h, t$ sta in $P$ per ogni $t \ge 0$ e $f = c_B^T B^{-1} b + t,\gamma_h \to -\infty$: problema illimitato.
- $B^{-1} N$ si legge dalla forma esplicita: coefficienti delle variabili fuori base cambiati di segno.
- Se entrambi i test falliscono, ogni $\gamma_h < 0$ ha almeno un $[B^{-1}N]_{jh} > 0$. **Entra** $(x_N)_h$ con $\gamma_h < 0$ (regola: il più negativo); **esce** $(x_B)_k$ con $k$ che realizza il **rapporto minimo** $t = \min_{[B^{-1}N]_{jh} > 0} (B^{-1}b)_j / [B^{-1}N]_{jh}$ (pareggi: indice più piccolo). Rapporti solo sulle entrate positive.
- Il nuovo valore è $c_B^T B^{-1} b + t,\gamma_h \le$ valore corrente; $t = 0$ (pivot degenere) solo se la SBA corrente è degenere. Un pareggio nel rapporto minimo produce una SBA degenere.