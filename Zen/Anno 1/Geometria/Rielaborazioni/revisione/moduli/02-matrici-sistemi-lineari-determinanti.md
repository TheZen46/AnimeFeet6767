---
corso: Geometria
modulo: 2
titolo: Matrici, sistemi lineari e determinanti
programma: [GEO-04]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 2 · Matrici, sistemi lineari e determinanti

**In questo modulo.** Si usa solo il calcolo con i numeri reali e complessi del modulo 1. Si introducono le matrici e le loro operazioni, con le proprietà che valgono e quelle che non valgono (il prodotto non è commutativo), le matrici invertibili, le operazioni elementari e la riduzione a scala con l'algoritmo di Gauss. Con questi strumenti si risolvono i sistemi lineari e si calcola l'inversa di una matrice. Poi si definisce il determinante, con lo sviluppo di Laplace, la regola di Sarrus e il teorema di Binet, e lo si usa per l'inversa e per la regola di Cramer. Il modulo si chiude con il rango e il teorema di Rouché-Capelli, che dice quando un sistema ha soluzioni e quante. Alla fine si sa risolvere un sistema lineare, anche con un parametro, e calcolare inverse, determinanti e ranghi.

## 2.1 Matrici e operazioni

Una **matrice** $m \times n$ a coefficienti nel campo $\mathbb{K}$ è una tabella di $m$ righe e $n$ colonne, $A = (a_{ij})$ con $i = 1, \dots, m$ e $j = 1, \dots, n$; $a_{ij}$ è il coefficiente nella riga $i$ e nella colonna $j$. L'insieme si indica con $\mathrm{Mat}_{m \times n}(\mathbb{K})$, e con $\mathrm{Mat}_n(\mathbb{K})$ quello delle matrici **quadrate** $n \times n$. Le matrici $1 \times n$ e $m \times 1$ sono i vettori riga e colonna.

In una matrice quadrata gli elementi $a_{11}, \dots, a_{nn}$ formano la **diagonale**. La matrice è **diagonale** se ha zeri fuori dalla diagonale, **triangolare superiore** se $a_{ij} = 0$ per $i > j$ (zeri sotto la diagonale), triangolare inferiore nel caso opposto. La **matrice identità** $I_n$ è la diagonale con tutti 1, la **matrice nulla** ha tutti i coefficienti nulli.

Le matrici della stessa forma si sommano coefficiente per coefficiente, e si moltiplicano per uno scalare moltiplicando ogni coefficiente: con queste operazioni valgono le solite proprietà (associativa, commutativa, elemento neutro la matrice nulla, opposto).

> [!definizione] Prodotto righe per colonne
> Se $A \in \mathrm{Mat}_{m \times n}$ e $B \in \mathrm{Mat}_{n \times p}$, il prodotto $AB \in \mathrm{Mat}_{m \times p}$ ha coefficienti
> $$(AB)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk} = a_{i1}b_{1k} + \dots + a_{in}b_{nk},$$
> il prodotto della riga $i$ di $A$ per la colonna $k$ di $B$. Si può fare solo se il numero di colonne di $A$ è uguale al numero di righe di $B$.

Il prodotto è associativo, $(AB)C = A(BC)$, distributivo rispetto alla somma, e $AI_n = A$, $I_m A = A$. Due proprietà dei numeri invece **non** valgono:

- il prodotto **non è commutativo**: anche quando $AB$ e $BA$ esistono e hanno la stessa forma, in generale sono diversi. Per esempio
$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}.$$
Di conseguenza $(A + B)^2 = A^2 + AB + BA + B^2$, che è diverso da $A^2 + 2AB + B^2$;

- **non vale la legge di annullamento del prodotto**: $AB = 0$ non implica $A = 0$ o $B = 0$. Per esempio $\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 0$.

La **trasposta** $A^T$ di $A \in \mathrm{Mat}_{m \times n}$ si ottiene scambiando righe e colonne, $(A^T)_{ij} = a_{ji}$. Vale $(A^T)^T = A$, $(A + B)^T = A^T + B^T$ e, con l'ordine rovesciato, $(AB)^T = B^T A^T$. Una matrice quadrata è **simmetrica** se $A^T = A$, **antisimmetrica** se $A^T = -A$.

> [!definizione] Matrice invertibile
> $A \in \mathrm{Mat}_n(\mathbb{K})$ è **invertibile** se esiste $B \in \mathrm{Mat}_n(\mathbb{K})$ con $AB = BA = I_n$. La matrice $B$ è unica, si chiama **inversa** e si indica con $A^{-1}$. L'insieme delle matrici invertibili si indica con $\mathrm{GL}_n(\mathbb{K})$.

Il prodotto di matrici invertibili è invertibile, con $(AB)^{-1} = B^{-1}A^{-1}$ (ancora con l'ordine rovesciato). Una matrice con una riga o una colonna nulla non è invertibile, e nemmeno un divisore dello zero: se $AB = 0$ con $B \neq 0$ e $A$ fosse invertibile, si avrebbe $B = A^{-1}AB = 0$.

## 2.2 Operazioni elementari e riduzione di Gauss

> [!definizione] Operazioni elementari sulle righe
>
> 1. scambiare due righe, $R_i \leftrightarrow R_j$;
> 2. sommare a una riga un multiplo di un'altra, $R_i \to R_i + c R_j$ con $j \neq i$;
> 3. moltiplicare una riga per uno scalare non nullo, $R_i \to c R_i$ con $c \neq 0$.

Ogni operazione elementare si ottiene moltiplicando a sinistra per una **matrice elementare**, cioè la matrice che si ottiene facendo la stessa operazione sull'identità. Per esempio in $\mathrm{Mat}_3$ la matrice $E$ che somma alla seconda riga due volte la prima è l'identità con un 2 in posizione $(2, 1)$, e $EA$ è $A$ con $R_2 \to R_2 + 2R_1$. Le matrici elementari sono invertibili, e l'inversa è la matrice dell'operazione opposta ($R_2 \to R_2 - 2R_1$).

> [!definizione] Forma a scala
> Una matrice è **a scala** se ogni riga non nulla comincia con più zeri della precedente e le righe nulle sono in fondo. Il primo coefficiente non nullo di ogni riga si chiama **pivot**. La forma è **totalmente ridotta** se inoltre ogni pivot vale 1 ed è l'unico elemento non nullo della sua colonna.

> [!teorema] Algoritmo di Gauss
> Ogni matrice si riduce a una forma a scala, e poi a una forma totalmente ridotta, con un numero finito di operazioni elementari sulle righe.

Il procedimento: si cerca la prima colonna non nulla, si porta in prima riga (con uno scambio) una riga che ha un elemento non nullo in quella colonna, il pivot, e con operazioni del tipo 2 si annullano gli elementi sotto di esso; poi si ripete sulla sottomatrice che resta togliendo la prima riga. Per la forma totalmente ridotta si dividono le righe per i pivot e si annullano anche gli elementi sopra ogni pivot, risalendo dall'ultimo.

**Calcolo dell'inversa.** Se $A$ è quadrata, si riduce la matrice affiancata $(A \mid I_n)$. Se la forma totalmente ridotta della parte sinistra è $I_n$, la matrice è invertibile e a destra compare $A^{-1}$: infatti le operazioni fatte sono il prodotto per matrici elementari $E_k \cdots E_1$ con $E_k \cdots E_1 A = I_n$, quindi $E_k \cdots E_1 = A^{-1}$, e questo è ciò che compare al posto di $I_n$. Se invece nella parte sinistra compare una riga nulla, $A$ non è invertibile. Ne segue anche che ogni matrice invertibile è un prodotto di matrici elementari.

> [!esempio] Inverse con l'algoritmo di Gauss
> Per $A = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$:
> $$\left(\begin{array}{cc|cc} 3 & -1 & 1 & 0 \\ -5 & 2 & 0 & 1 \end{array}\right) \xrightarrow{R_1 \to \frac13 R_1} \left(\begin{array}{cc|cc} 1 & -\frac13 & \frac13 & 0 \\ -5 & 2 & 0 & 1 \end{array}\right) \xrightarrow{R_2 \to R_2 + 5R_1} \left(\begin{array}{cc|cc} 1 & -\frac13 & \frac13 & 0 \\ 0 & \frac13 & \frac53 & 1 \end{array}\right)$$
> e poi, con $R_1 \to R_1 + R_2$ e $R_2 \to 3R_2$, si arriva a $\left(\begin{array}{cc|cc} 1 & 0 & 2 & 1 \\ 0 & 1 & 5 & 3 \end{array}\right)$: $A^{-1} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$, e si verifica che $AA^{-1} = I_2$.
>
> Per $\begin{pmatrix} 1 & 2 \\ -1 & -2 \end{pmatrix}$ l'operazione $R_2 \to R_2 + R_1$ produce una riga nulla a sinistra: la matrice non è invertibile.

## 2.3 Sistemi lineari

Un **sistema lineare** di $m$ equazioni in $n$ incognite è
$$\begin{cases} a_{11}x_1 + \dots + a_{1n}x_n = b_1 \\ \quad\vdots \\ a_{m1}x_1 + \dots + a_{mn}x_n = b_m \end{cases} \qquad \text{cioè} \qquad AX = B,$$
con $A = (a_{ij})$ la **matrice dei coefficienti**, $X$ la colonna delle incognite e $B$ quella dei termini noti. Il sistema è **omogeneo** se $B = 0$. La matrice $(A \mid B)$ è la **matrice completa**. Una soluzione è una $n$-upla di $\mathbb{K}^n$ che verifica tutte le equazioni; il sistema è **compatibile** (risolubile) se ne ha almeno una.

Le operazioni elementari sulle righe della matrice completa trasformano il sistema in uno **equivalente** (con le stesse soluzioni), perché sono invertibili. Quindi si riduce $(A \mid B)$ a scala e si legge la risposta:

> [!teorema] Soluzioni di un sistema ridotto a scala
> Sia $(A' \mid B')$ una forma a scala della matrice completa.
>
> 1. Il sistema è compatibile se e solo se non c'è un pivot nell'ultima colonna, cioè nessuna riga del tipo $(0 \ \cdots \ 0 \mid c)$ con $c \neq 0$ (che corrisponde all'equazione impossibile $0 = c$).
> 2. Se è compatibile e $p$ è il numero di pivot: con $p = n$ la soluzione è unica; con $p < n$ le soluzioni sono infinite e dipendono da $n - p$ **parametri** liberi, le incognite delle colonne senza pivot.

Il sistema omogeneo è sempre compatibile (ha almeno la soluzione nulla). Si risolve "all'indietro": dall'ultima equazione si ricava l'ultima incognita con pivot in funzione dei parametri, e si sostituisce nelle precedenti; oppure si arriva alla forma totalmente ridotta, dove ogni incognita con pivot è già espressa con i parametri.

> [!esempio] Un sistema con infinite soluzioni
> $$\begin{cases} x_3 + x_4 = 1 \\ 2x_1 + 2x_2 + x_3 - 5x_4 = 5 \\ 3x_1 + 3x_2 - x_3 = 0 \\ x_1 + x_2 - x_4 = 1 \end{cases}$$
> Si porta in prima riga l'ultima equazione e si riduce: $R_2 \to R_2 - 2R_1$, $R_3 \to R_3 - 3R_1$, poi si usano le righe con pivot nella terza colonna. La forma totalmente ridotta è
> $$\left(\begin{array}{cccc|c} 1 & 1 & 0 & 0 & \frac12 \\ 0 & 0 & 1 & 0 & \frac32 \\ 0 & 0 & 0 & 1 & -\frac12 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right):$$
> tre pivot su quattro incognite, quindi $4 - 3 = 1$ parametro, $x_2$. Le soluzioni sono
> $$\left\{\left(\tfrac12 - x_2,\ x_2,\ \tfrac32,\ -\tfrac12\right) \;\middle|\; x_2 \in \mathbb{R}\right\}.$$

## 2.4 Determinante

Il determinante è un numero associato a una matrice quadrata che dice se è invertibile.

> [!definizione] Determinante (sviluppo di Laplace)
> Per $n = 1$, $\det(a) = a$. Per $n \ge 2$, detta $A_{ij}$ la sottomatrice $(n-1) \times (n-1)$ ottenuta togliendo la riga $i$ e la colonna $j$, si sviluppa lungo la prima riga:
> $$\det A = \sum_{j=1}^{n} (-1)^{1+j}\, a_{1j}\, \det A_{1j}.$$
> Il numero $(-1)^{i+j}\det A_{ij}$ si chiama **cofattore** (o complemento algebrico) di $a_{ij}$.

Per $n = 2$: $\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$. Per $n = 3$ lo sviluppo dà sei termini, che si ricordano con la **regola di Sarrus**: si riscrivono a destra le prime due colonne, si sommano i prodotti delle tre diagonali che scendono verso destra e si sottraggono quelli delle tre che salgono:
$$\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}.$$
Sarrus vale solo per $n = 3$. In generale il determinante è la somma, su tutte le permutazioni $\sigma$ di $\{1, \dots, n\}$, dei prodotti $a_{1\sigma(1)} \cdots a_{n\sigma(n)}$ con il segno della permutazione (formula di Leibniz): $n!$ termini, troppi per calcolarlo così.

> [!teorema] Proprietà del determinante
>
> 1. Si può sviluppare lungo una riga o una colonna qualsiasi: $\det A = \sum_j (-1)^{i+j} a_{ij} \det A_{ij}$ per ogni $i$, e lo stesso per colonne. Quindi $\det A^T = \det A$.
> 2. Il determinante di una matrice triangolare (o diagonale) è il prodotto degli elementi della diagonale; $\det I_n = 1$.
> 3. Operazioni elementari: scambiare due righe cambia il segno; sommare a una riga un multiplo di un'altra non cambia il determinante; moltiplicare una riga per $c$ moltiplica il determinante per $c$.
> 4. Se due righe sono uguali o proporzionali, o una riga è nulla, $\det A = 0$.
> 5. **Teorema di Binet**: $\det(AB) = \det A \cdot \det B$.
> 6. $A$ è invertibile se e solo se $\det A \neq 0$, e in tal caso $\det(A^{-1}) = \frac{1}{\det A}$.

Le proprietà 2 e 3 danno il modo più veloce per calcolare un determinante grande: si riduce a scala, tenendo conto dei cambi di segno, e si moltiplicano i pivot. Conviene anche sviluppare lungo la riga o la colonna con più zeri.

> [!esempio] Un determinante $4 \times 4$
> $$\begin{vmatrix} 0 & 1 & 2 & 4 \\ -1 & 1 & 2 & 0 \\ 3 & 1 & 0 & 4 \\ 0 & 1 & 1 & 1 \end{vmatrix} = \begin{vmatrix} 1 & -1 & -2 & 0 \\ 0 & 1 & 2 & 4 \\ 3 & 1 & 0 & 4 \\ 0 & 1 & 1 & 1 \end{vmatrix} = \begin{vmatrix} 1 & -1 & -2 & 0 \\ 0 & 1 & 2 & 4 \\ 0 & 4 & 6 & 4 \\ 0 & 1 & 1 & 1 \end{vmatrix} = \begin{vmatrix} 1 & -1 & -2 & 0 \\ 0 & 1 & 2 & 4 \\ 0 & 0 & -2 & -12 \\ 0 & 0 & -1 & -3 \end{vmatrix}.$$
> Nel primo passaggio si scambiano le prime due righe e si cambia segno alla nuova prima riga: due cambi di segno, il determinante non cambia. Poi $R_3 \to R_3 - 3R_1$ e, con la seconda riga, $R_3 \to R_3 - 4R_2$, $R_4 \to R_4 - R_2$. Sviluppando lungo la prima colonna due volte resta $\begin{vmatrix} -2 & -12 \\ -1 & -3 \end{vmatrix} = 6 - 12 = -6$.

**Inversa con i cofattori.** Si dimostra con lo sviluppo di Laplace che la trasposta della matrice dei cofattori, la **matrice aggiunta** $A^* = \big((-1)^{i+j}\det A_{ij}\big)^T$, verifica $A^* A = A A^* = (\det A) I_n$. Quindi, se $\det A \neq 0$,
$$A^{-1} = \frac{1}{\det A} A^*, \qquad \text{in particolare} \quad \begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.$$

> [!esempio] Inversa con la matrice aggiunta
> Per $A = \begin{pmatrix} -1 & 2 & 3 \\ 0 & 0 & 1 \\ 1 & 1 & 4 \end{pmatrix}$, sviluppando lungo la seconda riga $\det A = (-1)^{2+3}\cdot 1 \cdot \begin{vmatrix} -1 & 2 \\ 1 & 1 \end{vmatrix} = -(-3) = 3$. I cofattori, riga per riga, sono $(-1, 1, 0)$, $(-5, -7, 3)$, $(2, 1, 0)$; trasponendo e dividendo per 3:
> $$A^{-1} = \frac13\begin{pmatrix} -1 & -5 & 2 \\ 1 & -7 & 1 \\ 0 & 3 & 0 \end{pmatrix}.$$

> [!teorema] Regola di Cramer
> Se $A \in \mathrm{Mat}_n(\mathbb{K})$ e $\det A \neq 0$, il sistema $AX = B$ ha un'unica soluzione $X = A^{-1}B$, e
> $$x_i = \frac{\det A_i}{\det A},$$
> dove $A_i$ è la matrice $A$ con la colonna $i$ sostituita dalla colonna $B$.

La formula segue da $X = \frac{1}{\det A}A^*B$: la componente $i$ di $A^*B$ è lo sviluppo di $\det A_i$ lungo la colonna $i$. È comoda per sistemi piccoli o per trovare una sola incognita.

> [!esempio] Cramer per un sistema $3 \times 3$
> $$\begin{cases} 2x_1 - x_3 = 1 \\ x_1 + x_2 - x_3 = 2 \\ x_1 + 2x_2 + x_3 = 5 \end{cases} \qquad \det A = \begin{vmatrix} 2 & 0 & -1 \\ 1 & 1 & -1 \\ 1 & 2 & 1 \end{vmatrix} = 2(1 + 2) - 0 - (2 - 1) = 5.$$
> Allora $x_1 = \frac15\begin{vmatrix} 1 & 0 & -1 \\ 2 & 1 & -1 \\ 5 & 2 & 1 \end{vmatrix} = \frac15\big(1 \cdot 3 - 0 - (4 - 5)\big) = \frac45$, e allo stesso modo $x_2 = \frac95$, $x_3 = \frac35$.

## 2.5 Rango e teorema di Rouché-Capelli

> [!definizione] Rango
> Il **rango** $\mathrm{rk}(A)$ di una matrice $A \in \mathrm{Mat}_{m \times n}$ è il numero di pivot di una sua forma a scala.

Il numero di pivot non dipende dalla forma a scala scelta (lo si vedrà nel modulo 3: è la dimensione dello spazio generato dalle righe, o dalle colonne). Il rango non cambia con le operazioni elementari e con la trasposizione, e $\mathrm{rk}(A) \le \min(m, n)$. Una matrice quadrata $n \times n$ ha rango $n$ se e solo se è invertibile.

> [!esempio] Una matrice di rango 2
> $$\begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 1 & 1 & -1 \\ 1 & 1 & -1 & 0 \\ 1 & 0 & -2 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 1 & 1 & -1 \\ 0 & -1 & -1 & 1 \\ 0 & -2 & -2 & 2 \end{pmatrix} \to \begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}:$$
> due pivot, rango 2.

Il rango si legge anche con i determinanti. Un **minore** di ordine $k$ di $A$ è il determinante di una sottomatrice $k \times k$ (scegliendo $k$ righe e $k$ colonne).

> [!teorema] Rango e minori (teorema degli orlati di Kronecker)
> $\mathrm{rk}(A)$ è il massimo ordine di un minore non nullo di $A$. Inoltre $\mathrm{rk}(A) = r$ se e solo se esiste un minore $M$ di ordine $r$ non nullo e tutti i minori di ordine $r + 1$ che lo contengono (gli **orlati** di $M$) sono nulli.

Il teorema degli orlati riduce il lavoro: trovato un minore non nullo di ordine $r$, basta controllare i suoi $(m - r)(n - r)$ orlati invece di tutti i minori di ordine $r + 1$.

> [!teorema] Teorema di Rouché-Capelli
> Il sistema $AX = B$ in $n$ incognite è compatibile se e solo se $\mathrm{rk}(A) = \mathrm{rk}(A \mid B)$. In tal caso, se $r$ è il rango comune: con $r = n$ la soluzione è unica; con $r < n$ le soluzioni sono infinite e dipendono da $n - r$ parametri.

È la versione con il rango del teorema del paragrafo 2.3: un pivot nell'ultima colonna vuol dire proprio che la matrice completa ha un rango in più di quella dei coefficienti.

## Esempi ed esercizi svolti

**Esercizio 1 (un sistema con un parametro).** Al variare di $\lambda \in \mathbb{R}$, discutere
$$\begin{cases} x + \lambda y = 1 \\ x + 2y = \lambda - 1 \\ 2x + \lambda^2 y = \lambda \end{cases}$$
La matrice $A$ dei coefficienti è $3 \times 2$, quindi $\mathrm{rk}(A) \le 2$, mentre la completa è $3 \times 3$. Il suo determinante, con Sarrus, è
$$\begin{vmatrix} 1 & \lambda & 1 \\ 1 & 2 & \lambda - 1 \\ 2 & \lambda^2 & \lambda \end{vmatrix} = -\lambda^3 + 3\lambda^2 - 4 = -(\lambda + 1)(\lambda - 2)^2.$$
Per $\lambda \neq -1, 2$ la completa ha rango 3 e $A$ al più 2: per Rouché-Capelli il sistema non ha soluzioni. Per $\lambda = -1$ il minore $\begin{vmatrix} 1 & -1 \\ 1 & 2 \end{vmatrix} = 3 \neq 0$ dà $\mathrm{rk}(A) = 2 = \mathrm{rk}(A \mid B)$ e $n = 2$: una sola soluzione, che dalle prime due equazioni $x - y = 1$, $x + 2y = -2$ è $(x, y) = (0, -1)$ (e verifica anche la terza). Per $\lambda = 2$ le tre righe della completa diventano $(1, 2 \mid 1)$, $(1, 2 \mid 1)$, $(2, 4 \mid 2)$, tutte proporzionali: rango 1 per entrambe, quindi infinite soluzioni con $2 - 1 = 1$ parametro, $x = 1 - 2y$.

**Esercizio 2 (inversa di una matrice $3 \times 3$).** Per $A = \begin{pmatrix} 0 & 1 & -1 \\ 1 & 3 & 2 \\ 1 & -4 & 1 \end{pmatrix}$ si riduce $(A \mid I_3)$: si scambiano le prime due righe, poi $R_3 \to R_3 - R_1$ e $R_3 \to R_3 + 7R_2$, che lascia la terza riga $(0, 0, -8 \mid 7, -1, 1)$. Dividendo per $-8$ e risalendo si ottiene
$$A^{-1} = \frac18\begin{pmatrix} 11 & 3 & 5 \\ 1 & 1 & -1 \\ -7 & 1 & -1 \end{pmatrix},$$
coerente con $\det A = 8$ (il pivot $-8$ moltiplicato per $-1$ dello scambio e per i pivot 1).

**Esercizio 3 (prodotto e trasposta).** Se $A$ è una qualsiasi matrice $m \times n$, le matrici $AA^T$ (di ordine $m$) e $A^TA$ (di ordine $n$) sono simmetriche: $(AA^T)^T = (A^T)^T A^T = AA^T$. Ogni matrice quadrata si scrive come somma di una simmetrica e di una antisimmetrica: $A = \frac{A + A^T}{2} + \frac{A - A^T}{2}$.

### Esercizi sul modello delle prove d'esame

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle prove scritte 2024-2026 e dei fogli "Matrici e sistemi lineari"; soluzioni verificate con `strumenti/verifica_ampliamento.py` (GEO-04)
> L'esercizio tipico è un sistema con un parametro: per quali valori è risolubile, quando la soluzione è unica, e la soluzione per un valore fissato.

**Esercizio 4. Un sistema con un parametro.** Discutere al variare di $a \in \mathbb{R}$ e risolvere
$$\begin{cases} x + y + z = 1 \\ x + ay + z = a \\ x + y + az = a^2 \end{cases}$$

*Determinante.* Sottraendo la prima riga dalle altre, la matrice dei coefficienti diventa triangolare con diagonale $1, a - 1, a - 1$: $\det A = (a - 1)^2$.

*$a \ne 1$.* $\det A \ne 0$: per Cramer (o Rouché-Capelli) la soluzione esiste ed è unica. Sottraendo la prima equazione dalla seconda, $(a - 1)y = a - 1$, cioè $y = 1$; dalla terza, $(a - 1)z = a^2 - 1$, cioè $z = a + 1$; infine $x = 1 - y - z = -a - 1$. Controllo nella terza: $-a - 1 + 1 + a(a + 1) = a^2$.

*$a = 1$.* Le tre equazioni diventano tutte $x + y + z = 1$: rango della matrice e della completa uguale a 1, il sistema è risolubile con $3 - 1 = 2$ parametri liberi: $(x, y, z) = (1 - s - t, s, t)$.

**Esercizio 5. Invertibilità con un parametro.** Per quali $h$ è invertibile $A_h = \begin{pmatrix} 1 & h & 0 \\ 0 & 1 & h \\ h & 0 & 1 \end{pmatrix}$? Calcolare l'inversa per $h = 1$.

Con Laplace sulla prima colonna: $\det A_h = 1 \cdot (1 - 0) + h \cdot (h^2 - 0) = 1 + h^3$. È nullo solo per $h = -1$ (unica radice reale di $h^3 = -1$). Per $h = 1$, $\det = 2$, e con Gauss-Jordan su $(A \mid I)$ o con la matrice dei complementi algebrici:
$$A_1^{-1} = \frac12\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}.$$
Controllo della prima riga di $A_1 A_1^{-1}$: $(1, 1, 0) \cdot$ colonne $= \frac12(1 + 1,\ -1 + 1,\ 1 - 1) = (1, 0, 0)$.

**Esercizio 6. Rango con un parametro.** Rango di $C_k = \begin{pmatrix} 1 & 2 & k \\ 2 & 4 & 2 \\ k & 2 & 1 \end{pmatrix}$ al variare di $k$.

$\det C_k = 1(4 - 4) - 2(2 - 2k) + k(4 - 4k) = -4 + 4k + 4k - 4k^2 = -4(k - 1)^2$. Per $k \ne 1$ il rango è 3. Per $k = 1$ tutte le righe sono multiple di $(1, 2, 1)$: rango 1. Non c'è nessun valore con rango 2: lo si vede anche dal minore $\begin{vmatrix} 2 & k \\ 4 & 2 \end{vmatrix} = 4 - 4k$, nullo proprio per $k = 1$.

**Esercizio 7. Una matrice che è la propria inversa.** Sia $B = \begin{pmatrix} 1 & 0 & 0 \\ 2 & -1 & 0 \\ 3 & 0 & -1 \end{pmatrix}$. Mostrare che $B^2 = I$ e dedurre $B^{-1}$.

Riga per colonna: la prima riga di $B^2$ è $(1, 0, 0)$; la seconda è $(2 \cdot 1 + (-1) \cdot 2,\ (-1)^2,\ 0) = (0, 1, 0)$; la terza è $(3 \cdot 1 + (-1) \cdot 3,\ 0,\ (-1)^2) = (0, 0, 1)$. Quindi $B^2 = I$ e $B^{-1} = B$. Come applicazione, $f(x) = Bx$ soddisfa $f(f(x)) = x$: è un'**involuzione**. Il determinante deve valere $\pm 1$, perché $\det(B)^2 = \det(B^2) = 1$ (Binet); qui è triangolare e vale $1 \cdot (-1) \cdot (-1) = 1$.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni verificate con `strumenti/verifica_ampliamento.py` (GEO-04)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Rouché-Capelli passo per passo.** Discutere $\begin{cases} x + 2y = 3 \\ 2x + ky = 6 \end{cases}$ al variare di $k$.

*Passo 1: il determinante.* $\det A = k - 4$.

*Passo 2: $k \ne 4$.* Soluzione unica: dalla seconda meno due volte la prima, $(k - 4)y = 0$, quindi $y = 0$ e $x = 3$.

*Passo 3: $k = 4$, i ranghi.* $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ ha rango 1; la completa $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$ ha rango 1 (la seconda riga è il doppio della prima).

*Passo 4: conclusione per $k = 4$.* Ranghi uguali: risolubile, con $2 - 1 = 1$ parametro: $(3 - 2t, t)$. Se il termine noto della seconda equazione fosse stato diverso da 6, la completa avrebbe avuto rango 2 e il sistema sarebbe stato impossibile.

**Guidato 2. L'inversa con Gauss-Jordan.** Invertire $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.

*Passo 1.* Si scrive $(A \mid I) = \left(\begin{smallmatrix} 2 & 1 & | & 1 & 0 \\ 5 & 3 & | & 0 & 1 \end{smallmatrix}\right)$.

*Passo 2.* $R_2 \to 2R_2 - 5R_1$: $\left(\begin{smallmatrix} 2 & 1 & | & 1 & 0 \\ 0 & 1 & | & -5 & 2 \end{smallmatrix}\right)$.

*Passo 3.* $R_1 \to R_1 - R_2$, poi $R_1 \to \frac12 R_1$: $\left(\begin{smallmatrix} 1 & 0 & | & 3 & -1 \\ 0 & 1 & | & -5 & 2 \end{smallmatrix}\right)$.

*Passo 4.* $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$. Con la formula delle $2 \times 2$, $\frac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ con $\det A = 1$, si ritrova lo stesso risultato.

**Guidato 3. Un determinante $4 \times 4$ con le proprietà.** Calcolare $\det\begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 3 \\ 0 & 1 & 1 & 0 \\ 1 & 2 & 0 & 2 \end{pmatrix}$.

*Passo 1: fare zeri.* $R_2 \to R_2 - 2R_1$ dà $(0, 0, 1, 1)$; $R_4 \to R_4 - R_1$ dà $(0, 0, 0, 1)$. Il determinante non cambia.

*Passo 2: Laplace sulla prima colonna.* Resta un solo elemento non nullo, l'1 in alto a sinistra: il determinante è quello della $3 \times 3$ con righe $(0, 1, 1)$, $(1, 1, 0)$, $(0, 0, 1)$.

*Passo 3: Laplace sull'ultima riga.* $1 \cdot \begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} = -1$.

*Passo 4: risultato.* $\det = -1$. Senza le operazioni di riga lo sviluppo di Laplace avrebbe richiesto quattro determinanti $3 \times 3$.

## Riepilogo

Le matrici si sommano coefficiente per coefficiente e si moltiplicano righe per colonne; il prodotto è associativo e distributivo ma non commutativo, e ammette divisori dello zero. La trasposta rovescia l'ordine dei prodotti; una matrice quadrata è invertibile se ha un'inversa da entrambi i lati, e le invertibili formano $\mathrm{GL}_n$. Le operazioni elementari sulle righe corrispondono al prodotto per matrici elementari, e con l'algoritmo di Gauss portano ogni matrice a scala e poi in forma totalmente ridotta: riducendo $(A \mid I)$ si trova l'inversa, riducendo $(A \mid B)$ si risolve il sistema, che è compatibile se non c'è un pivot nell'ultima colonna e ha $n - p$ parametri liberi. Il determinante si calcola con Laplace lungo una riga o una colonna, con Sarrus per $n = 3$, o riducendo a scala; cambia segno con gli scambi, è multiplicativo (Binet) e non nullo esattamente per le matrici invertibili, la cui inversa è l'aggiunta divisa per il determinante. Ne seguono la regola di Cramer e il rango come ordine massimo di un minore non nullo (orlati di Kronecker); per Rouché-Capelli un sistema è compatibile se e solo se $A$ e $(A \mid B)$ hanno lo stesso rango $r$, e allora le soluzioni dipendono da $n - r$ parametri.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (GEO-04)
> Operazioni, determinante, rango e sistemi, con i termini per l'orale.

### Matrici

$$(AB)^T = B^T A^T, \quad (AB)^{-1} = B^{-1}A^{-1}, \quad \begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}, \quad A^{-1} = \frac{1}{\det A}\operatorname{adj}(A).$$

Il prodotto non è commutativo; $AB = 0$ non implica $A = 0$ o $B = 0$.

### Determinante

- Laplace lungo la riga $i$: $\det A = \sum_j (-1)^{i+j}a_{ij}\det A_{ij}$.
- Scambiare due righe cambia il segno; moltiplicare una riga per $c$ moltiplica per $c$; sommare a una riga un multiplo di un'altra non cambia nulla.
- $\det(AB) = \det A \det B$ (Binet), $\det A^T = \det A$, $\det A^{-1} = \frac{1}{\det A}$, $\det(cA) = c^n\det A$.
- Triangolare: prodotto della diagonale. $\det A \ne 0 \iff A$ invertibile $\iff$ righe indipendenti.

### Rango e sistemi

Il rango è il numero di pivot dopo la riduzione, cioè il massimo ordine di un minore non nullo. **Rouché-Capelli**: $AX = B$ è risolubile se e solo se $\operatorname{rk} A = \operatorname{rk}(A \mid B)$; allora le soluzioni dipendono da $n - \operatorname{rk} A$ parametri. **Cramer**: se $A$ è quadrata e invertibile, $x_i = \frac{\det A_i}{\det A}$, con $A_i$ ottenuta mettendo $B$ al posto della colonna $i$.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Matrice ridotta per righe | il primo elemento non nullo di ogni riga sta a destra di quello sopra |
| Matrice totalmente ridotta | ridotta, con pivot 1 e zeri sopra e sotto ogni pivot |
| Matrice elementare | ottenuta dall'identità con una sola operazione elementare |
| Matrice invertibile | esiste $A^{-1}$ con $AA^{-1} = A^{-1}A = I$ |
| Rango | dimensione dello spazio delle righe (o delle colonne) |
| Sistema omogeneo | termini noti nulli: ha sempre la soluzione nulla |
| Complemento algebrico | $(-1)^{i+j}\det A_{ij}$ |

### Domande che tornano spesso

- Che cosa sono le operazioni elementari e perché non cambiano le soluzioni di un sistema?
- Caratterizzazioni delle matrici invertibili.
- Proprietà del determinante; enunciare Binet e Laplace.
- Enunciare e dimostrare Rouché-Capelli; struttura delle soluzioni (soluzione particolare più omogeneo).
- Enunciare Cramer.
