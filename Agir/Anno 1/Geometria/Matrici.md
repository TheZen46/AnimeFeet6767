$\begin{pmatrix} a & b & c \\ e & f & g \end{pmatrix}$
$a, b, c, d, e, f$ coefficienti della matrice/matrix entries

$\rightarrow$ righe
$\downarrow$ colonne

Mat$(\mathbb{R/C/K})$
    mxn
	2x3
	
Modo di organizzare dei dati
	Molteplici applicazioni

$\begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{mn} \\ \dots & \dots & \dots & \dots \\ a_{m1} & a_{m2} & \dots & a_{mn}\end{pmatrix} \in$ Mat($\mathbb{K}$)

$Mat(\mathbb{K})$
mx1
"Colonne"

$Mat(\mathbb{K})$
1xn
"Righe"

$Mat(\mathbb{K}$
m
"Quadrate"
Mat$_m$

In una matrice $\in$ Mat$_m(\mathbb{K})$
	Gli elementi di posto $i,i$ formano "la diagonale"
	Se gli elementi fuori dalla diagonale sono = 0 la matrice si dice diagonale
	Se $\forall\ i<J\ a_{iJ}=0$ la matrice si dice "triangolare superiore"
	Se $\forall\ J<i\ a_{iJ}=0$ la matrice si dice "triangolare superiore"

### Somma
$A \in \text{ Mat}_{m\times n}(\mathbb{K})$
$m\times x$ è la **taglia** della matrice
$A = (a_{ij})_{i,j};\ a=1,\ldots, m;\ b=1,\ldots, n$

$A+B \in \text{Mat}_{m\times n}(\mathbb{K})$
$A+B=(a_{ij}+b_{ij})_{i,j}$

$$
\begin{pmatrix}
2 & 3 & 0 \\
-1 & 4 & 2
\end{pmatrix}
+
\begin{pmatrix}
-1 & 0 & -1 \\
-1 & 0 & 1
\end{pmatrix}
=
\begin{pmatrix}
1 & 3 & -1 \\
-2 & 4 & 3
\end{pmatrix}
$$
Per sommarle, le matrici devono avere la stessa taglia

La matrice $m\times n$ con tutti i coefficienti = 0 si dice "matrice nulla", indicata con 0
#### Proprietà
Valgono le usuali proprietà algebriche rispetto al +
	Associativa
	Commutativa
	Esistenza di 0
	Esistenza dell'opposto

### Prodotto
#### Prodotto riga colonna
Se $R\in \text{Mat}_{1\times n} \text{ e } C\in \text{Mat}_{n\times 1}\rightarrow R\cdot C\in \mathbb{K} = \text{Mat}_{1\times 1}(\mathbb{K})$ 
$$
\begin{pmatrix}
r_1 & r_2 & \ldots & r_n
\end{pmatrix}
\cdot
\begin{pmatrix}
c_1 \\ c_2 \\ \ldots \\ c_n
\end{pmatrix}
=
\begin{pmatrix}
r_1c_1+r_2c_2+\ldots+r_nc_n
\end{pmatrix}
$$

$$
\begin{pmatrix}
1 & 2 & 1 & 0
\end{pmatrix}
\cdot
\begin{pmatrix}
1 \\ -1 \\ -1 \\ -1
\end{pmatrix}
=
\begin{pmatrix}
1-2-1-0
\end{pmatrix}
\rightarrow
\begin{pmatrix}
-2
\end{pmatrix}
$$

#### Prodotto

$A\in \text{Mat}_{m\times n}\ \ B\in\text{Mat}_{n\times p}$

Il numero di colonne di A dev'essere uguale al numero di righe di B

$A\cdot B\in\text{Mat}_{m\times p}\rightarrow (AB)_{ij}=$ il prodotto tra la i-esima riga di A e la j-esima colonna di B = $\sum\limits_{K=1}^{n}{a_{iK}\cdot b_{KJ}}$



$$
\begin{pmatrix}
2 & 1 & 2 \\
-1 & 1 & 2
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & 0 & 1 \\
0 & 2 & 1 \\
0 & 0 & 3
\end{pmatrix}
=
\begin{pmatrix}
2\cdot1+1\cdot0+2\cdot0 & 2\cdot0+1\cdot2+2\cdot0 & 2\cdot1+1\cdot1+2\cdot3 \\
(-1)\cdot1+1\cdot0+2\cdot0 & (-1)\cdot0+1\cdot2+2\cdot0 & (-1)\cdot1+1\cdot1+2\cdot3
\end{pmatrix}
=
\begin{pmatrix}
2 & 2 & 9 \\
-1 & 2 & 6
\end{pmatrix}
$$
*(Moltiplichi riga i di A per colonna j di B, matrice C ha numero di colonne righe di A e numero di colonne di B (colonne A = righe B))*
$$
\begin{pmatrix}
1 & 2 & 3 \\
3 & 0 & 1\end{pmatrix}
\cdot
\begin{pmatrix}
1 & 0 \\
1 & 1 \\
-2 & -1
\end{pmatrix}
=
\begin{pmatrix}
1\cdot1+2\cdot1+3\cdot(-2) & 1\cdot0+2\cdot1+3\cdot(-1) \\
3\cdot1+0\cdot1+1\cdot(-2) & 3\cdot0+0\cdot1+1\cdot(-1) \\
\end{pmatrix}
=
\begin{pmatrix}
-3 & -1 \\
1 & -1
\end{pmatrix}
$$
#### Proprietà

Vale la proprietà associativa del prodotto

$A_{m\times n}\cdot B_{n\times p}\cdot C_{p\times r} = D_{m\times r}$
$a_{iJ}\cdot b_{iJ}\cdot c_{iJ}$

**NON VALE** la proprietà commutativa

$$
\begin{pmatrix}
1 & 1 \\
2 & 3
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & -1 \\
2 & 4 \\
\end{pmatrix}
=
\begin{pmatrix}
3 & 3 \\
8 & 10
\end{pmatrix}
$$
$$
\begin{pmatrix}
1 & -1 \\
2 & 4 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & 1 \\
2 & 3
\end{pmatrix}
=
\begin{pmatrix}
-1 & -2 \\
10 & 14
\end{pmatrix}
$$
$A\cdot B\ne B\cdot A$

Vale la proprietà distributiva (sia a destra che a sinistra)
$A,B\in\text{Mat}_n$
$(A+B)^2=(A+B)(A+B)=A(A+B)+B(A+B)=A^2+AB+BA+B^2\ne A^2+2AB+B^2$

**NON VALE** la legge dell'annullamento del prodotto

$$
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & -2 \\
-1 & 2
\end{pmatrix}
=
\begin{pmatrix}
-2 & 4 \\
-1 & 2
\end{pmatrix}
$$

$$
\begin{pmatrix}
1 & -2 \\
-1 & 2
\end{pmatrix}
\cdot
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
=
\begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}
$$

+6### Identità
Wacom

$\forall\ A\in\text{Mat}_{m\times n}$
$A\cdot I_n=A$
$I_m\cdot A=A$

$$
\begin{pmatrix}
1 & 4 & -1 \\
3 & 2 & 1 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
=
\begin{pmatrix}
1\cdot1+4\cdot0+(-1)\cdot0 & 1\cdot0+4\cdot1+(-1)\cdot0 & 1\cdot0+4\cdot0+(-1)\cdot1 \\
3\cdot1+2\cdot0+1\cdot0 & 3\cdot0+2\cdot1+1\cdot0 & 3\cdot0+2\cdot0+1\cdot1 \\
\end{pmatrix}
=
\begin{pmatrix}
1 & 4 & -1 \\
3 & 2 & 1 \\
\end{pmatrix}
$$
$A\in\text{Mat}_n$ si dice invertibile se $\exists B\in\text{Mat}_n$ tale che $AB=BA=I_n$

$$
\begin{pmatrix}
3 & -1 \\
-5 & 2 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
2 & 1 \\
5 & 3
\end{pmatrix}
=
\begin{pmatrix}
6-5 & 3-3 \\
-10+10 & -5+6
\end{pmatrix}
=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$
$$
\begin{pmatrix}
3 & -1 \\
-5 & 2 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
2 & 1 \\
5 & 3
\end{pmatrix}
=
\begin{pmatrix}
6-5 & 3-3 \\
-10+10 & -5+6
\end{pmatrix}
=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$
$$A=\begin{pmatrix}
1 & -2 \\
-1 & 2
\end{pmatrix}
\ \ \ \
B=
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
\ \ \ \
BA=0
$$
Se esistesse $C\in\text{Mat}_2$ tale che $AC=I_2\rightarrow BAC=0C=0$

Insieme delle matrici invertibili indicato con ${GL}_n(\mathbb{R})=\{A\in\text{Mat}_n(\mathbb{R})|A\text{ è invertibile}\}$

Il prodotto di matrici invertibili è invertibile, **MA** $(AB)^{-1}=B^{-1}A^{-1}\ne A^{-1}B^{-1}$
$(AB)(B^{-1}A^{-1})=I=A(B\cdot B^{-1})A^{-1}=AIA^{-1}=A\cdot A^{-1}=I$

### Matrice scalare
Le matrici scalari sono le matrici diagonali in cui gli elementi diagonali sono tutti uguali tra loro

$$
\text{Mat}_3
\ \ \ \
2AB
\ \ \ \
2=2I_3=
\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}
$$

### Trasposta
$\forall\in\text{Mat}_{m\times n}$
La **trasposta** di A è la matrice $\in\text{Mat}_{n\times m}$ ottenuta scambiando le righe con le colonne
$A^T$ / $^tA$
$A=(a_{ij})\ \ \ \ A^T=(a_{ji})$

$$
\begin{pmatrix}
2 & 1 & 5 \\
-1 & 3 & 2
\end{pmatrix}^T
=
\begin{pmatrix}
2 & -1\\
1 & 3\\
5 & 2
\end{pmatrix}
$$
$\forall\ A,B\in\text{Mat}_{m\times n}$
$(A^T)^T=A$
$(A+B)^T=A^T+B^T$

$\forall\ A\in\text{Mat}_{m\times n}, B\in\text{Mat}_{n\times p}$
$(AB)^T=B^T\cdot A^T$

#### Simmetria
Sia $A\in\text{Mat}_n$
Se $A=A^T$ A si dice **simmetrica**
Se $A=-A^T$ A si dice **antisimmetrica**

Una matrice $A\in\text{Mat}_n$ tale che $\exists\ K\ A^K=0$ si dice impotente

### Operazioni elementari (per righe)
1) Scambiare 2 righe
2) Sommare a una riga un multiplo di un altra riga
3) Moltiplicare una riga per un coefficiente scalare
$$
\begin{pmatrix}
2 & 1 & 5 \\
-1 & 3 & 2
\end{pmatrix}
\Rightarrow^{R1\rightarrow R2}
\begin{pmatrix}
-1 & 3 & 2 \\
2 & 1 & 5
\end{pmatrix}
$$
$$
\begin{pmatrix}
1 & 2 \\
1 & -1\\
3 & 4
\end{pmatrix}
\Rightarrow^{R1\rightarrow R1+R2}
\begin{pmatrix}
3 & 0 \\
1 & -1\\
3 & 4
\end{pmatrix}
$$

$$
\begin{pmatrix}
1 & 1 \\
1 & 2 \\
\end{pmatrix}
\Rightarrow^{R1\rightarrow R1+R2}
\begin{pmatrix}
3 & 0 \\
1 & -1
\end{pmatrix}
$$

Le **matrici elementari** sono le matrici ottenute dell'identità tramite operazioni elementari

$$
I_n=
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\ \ \ \
E_{13}=
\begin{pmatrix}
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$
$$
I_n=
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\ \ \ \
E_{23}(7)=
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 7 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$
$$
E_{i}(\lambda)=
\begin{pmatrix}
1 &  &  &  \\
 & 1 &  &  \\
 &  & \lambda &  \\
 &  &  & 1
\end{pmatrix}
$$
$$
E_{4}(2)=
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 2
\end{pmatrix}
$$
$A\in\text{Mat}_{n\times m}$
$E_{ij}\in\text{Mat}_m$
$E_{ij}\ A$ è la matrice ottenuta da A scambiando le righe $i$ e $j$-esime

$$
\begin{pmatrix}
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\ 
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
1 & 4 \\ 
-1 & 7 \\
2 & 2 
\end{pmatrix}
\rightarrow
\begin{pmatrix}
-1 & 7 \\
1 & 4 \\ 
1 & 2 \\
2 & 2 
\end{pmatrix}
$$$$
\begin{pmatrix}
1 & 4 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
5 & 6
\end{pmatrix}
\Rightarrow
\begin{pmatrix}
13 & 18 \\
3 & 4 \\
5 & 6
\end{pmatrix}
$$$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\ 
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 2
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
2 & 0 \\ 
4 & -3 \\
1 & 2
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & -1 \\
2 & 0 \\ 
4 & -3 \\
2 & 4
\end{pmatrix}
$$
$E_{ij}\cdot E_{ij}=I$
$E_{ij}(\lambda)\cdot E_{ij}(-\lambda)=I$
$E_{ij}(\lambda)\cdot E_{ij}(\frac{1}{\lambda})=I\ (\lambda\ne0)$


$$
\begin{cases}
2x+y-z=1 \\
3x+2z=1 \\
2y+z=0
\end{cases}
\begin{cases}
x+\frac{y}{2}-\frac{z}{2}=\frac{1}{2} \\
3x+2z=1 \\
2y+z=0
\end{cases}
\begin{cases}
x+\frac{y}{2}-\frac{z}{2}=\frac{1}{2} \\
-\frac{3}{2}+y\frac{7}{2}z=\frac{-1}{2} \\
2y+z=0
\end{cases}
\begin{cases}
x+\frac{y}{2}-\frac{z}{2}=\frac{1}{2} \\
y-\frac{7}{3}z=\frac{1}{3} \\
2y+z=0
\end{cases}
\begin{cases}
x+\frac{y}{2}-\frac{z}{2}=\frac{1}{2} \\
y-\frac{7}{3}z=\frac{1}{3} \\
\frac{17}{3}z=\frac{2}{3}
\end{cases}
$$
Algoritmo di eliminazione (o riduzione) di Gauss
Una matrice è ridotta ("a scala", "a scalini")
$$
\begin{pmatrix}
x &  &  &  \\
0 & x &  &  \\ 
0 & 0 & x &  \\
0 & 0 & 0 & x
\end{pmatrix}
$$
In ogni riga, sotto al primo elemento $\ne0$ ci sono solo 0
$\forall\in\text{Mat}_{n\times m}\ \ \ \ \forall\ i=1\ m\text{ se } a_{ij}\ne0]\text{ e }\forall\ K<j\ \ \ \ a_{ik}=0 \text{ allora } \forall K>i\ \ \forall\ h\ge j\ \ \ \ a_{kh}=0$

$$
\begin{pmatrix}
1 & 2 & 0 & 4 & 2 & 5 & 1\\
0 & 1 & 0 & 0 & 3 & -1 & 0 \\ 
0 & 0 & 0 & 0 & 0 & 0 & 4
\end{pmatrix}
$$
Pivot
Per ogni riga, il primo coefficiente diverso da 0


Vogliamo eseguire op elementari che portino una matrice qualunque in forma ridotta

$$
\begin{pmatrix}
1 & -2 & 0 & 3 \\
2 & -1 & 1 & 2 \\
3 & 0 & 2 & 3
\end{pmatrix}
\rightarrow
^{R_2\rightarrow R_2-2R_1\ \ R3\rightarrow R_3-3R_1}
\begin{pmatrix}
1 & -2 & 0 & 3 \\
0 & 3 & 1 & -4 \\
0 & 6 & 2 & 6
\end{pmatrix}
\rightarrow
^{R_3\rightarrow R_3-2R_2}
\begin{pmatrix}
1 & -2 & 0 & 3 \\
0 & 3 & 1 & -4 \\
0 & 0 & 0 & 2
\end{pmatrix}
$$

Partiamo da una matrice $A\in\text{Mat}_{n\times m}$
Supponiamo che la prima colonna non sia tutta di 0
Se $a_{11}=0\ 0<$, altrimenti sia $i$ il minimo indice t.c. $a_{1i}\ne0$ e scambio la riga $i$ con la riga 1

Per ogni $i=2,\ n, R_i\rightarrow R_i-a_{11}R_1$

Sia K l'indice del primo colonna $\ne0$ sulla seconda riga

$$
\begin{pmatrix}
0 & 0 & 1 & 1 & 1\\
2 & 2 & 1 & -5 & 5 \\ 
3 & 3 & -1 & 0 & 0 \\ 
1 & 1 & 0 & -1 & 1
\end{pmatrix}
\rightarrow
^{R_1\Leftrightarrow R_2}
\begin{pmatrix}
2 & 2 & 1 & -5 & 5 \\
0 & 0 & 1 & 1 & 1\\ 
3 & 3 & -1 & 0 & 0 \\ 
1 & 1 & 0 & -1 & 1
\end{pmatrix}
\rightarrow
^{R_3\rightarrow R_3-\frac{3}{2}R_1\ \ R_4\rightarrow R_4-\frac{1}{2}3R_1}
\begin{pmatrix}
2 & 2 & 1 & -5 & 5 \\
0 & 0 & 1 & 1 & 1\\ 
0 & 0 &  & 0 & 0 \\ 
1 & 1 & 0 & -1 & 1
\end{pmatrix}
$$

$$
\begin{pmatrix}
1 & 2 \\
-1 & 3
\end{pmatrix}
\rightarrow^{R_2\rightarrow R_2+R_1}
\begin{pmatrix}
1 & 2 \\
0 & 5
\end{pmatrix}
\rightarrow^{R_2\rightarrow \frac{R_2}{5}}
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
\rightarrow^{R_1\rightarrow R_1-R_2}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$
$$
\begin{pmatrix}
1 & 2 \\
-1 & -2
\end{pmatrix}
\rightarrow^{R_2\rightarrow R_2+R_1}
\begin{pmatrix}
1 & 2 \\
0 & 0
\end{pmatrix}
$$

Data una matrice quadrata $A\in\text{Mat}_n$ la forma totalmente ridotta è
- o $I_n$ (se $A$ è invertibile) (se e solo se $A$ è prodotto di matrici elementari)
- o $\begin{pmatrix} \\ \\ 0 & --- & 0 \end{pmatrix}$ una matrice con l'ultima riga di zeri (se $A$ non è invertibile)

Sia $B$ la forma totalmente ridotta della matrice $A$
$B=E_r\cdot\ldots\cdot E_2\cdot E_1\cdot A$ ($E$ matrici elementari)
$A=E_1^{-1}\cdot E_2^{-1}\cdot\ldots\cdot E_r^{-1}\cdot B$

$A$ prodotto di matrici elementari $\iff B=I_n$
Implica: $A$ è invertibile

Supponiamo $A$ invertibile
Dimostriamo $B=I_n$
Allora $B$ è invertibile, perché prodotto di matrici invertibili
Se $B$ non fosse $I_n$, avrebbe l'ultima riga $= 0$, ma una tale matrice non può essere invertibile

riga $i$ - $\begin{pmatrix} \\ 0 & --- & 0 \\ \\ \end{pmatrix} \begin{pmatrix} \\  &  &  \\ \\ \end{pmatrix} = \begin{pmatrix} \\ 0 & --- & 0 \\ \\ \end{pmatrix}$
Non può essere identità, dato che una riga di 0, indipendentemente dalle matrici con cui viene moltiplicata, può contenere un 1

$B=E_r\cdot\ldots\cdot E_2\cdot E_1\cdot A$ 
se $A$ è invertibile
$A^{-1}=E_r\cdot\ldots\cdot E_1$

$$
\begin{pmatrix}
3 & -1 \\
-5 & 2
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

$$
\left(
\begin{array}{cc|cc}
3 & -1 & 1 & 0 \\
-5 & 2 & 0 & 1
\end{array}
\right)
\rightarrow^{R_1\rightarrow \frac{R_1}{3}}
\left(
\begin{array}{cc|cc}
1 & \frac{-1}{3} & \frac{1}{3} & 0 \\
-5 & 2 & 0 & 1
\end{array}
\right)
\rightarrow^{R_2\rightarrow R_2+5R_1}
\left(
\begin{array}{cc|cc}
1 & \frac{-1}{3} & \frac{1}{3} & 0 \\
0 & \frac{1}{3} & \frac{5}{3} & 1
\end{array}
\right)
\rightarrow^{R_1\rightarrow R_1+R_2}
\left(
\begin{array}{cc|cc}
1 & 0 & 2 & 1 \\
0 & \frac{1}{3} & \frac{5}{3} & 1
\end{array}
\right)
\rightarrow^{R_2\rightarrow 3R_2}
\left(
\begin{array}{cc|cc}
1 & 0 & 2 & 1 \\
0 & 1 & 5 & 3
\end{array}
\right)
$$
$$
\begin{pmatrix}
3 & -1 \\
-5 & 2
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
5 & 3
\end{pmatrix}
=
\begin{pmatrix}
6-5 & 3-3 \\
-10+10 & -2+6
\end{pmatrix}
=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$
$$
\left(
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
-1 & -2 & 0 & 1
\end{array}
\right)
\rightarrow^{R_2\rightarrow R_2+R_1}
\left(
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
0 & 0 & 1 & 1
\end{array}
\right)
\rightarrow^{R_2\rightarrow R_2+R_1}
\left(
\begin{array}{cc|cc}
1 & 2 & 0 & 0 \\
0 & 0 & 1 & 1
\end{array}
\right)
\text{ non invertibile}
$$
