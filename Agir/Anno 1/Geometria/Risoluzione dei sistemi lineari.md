$$
\begin{cases}
a_{11}x_1+\ldots+a_{1n}x_n=b_1 \\
.\\.\\.\\
a_{m1}x_1+\ldots+a_{mn}x_n=b_m
\end{cases}
$$
$b_1,\ldots,B_m\in\mathbb{K}$

Cerchiamo tutte le n-uple $x_1,\ldots,x_n\in\mathbb{K}$ che risolvono le $m$ equazioni

$A=(a_{ij})\in\text{Mat}_{n\times m}$

$B=\begin{pmatrix}b_1\\.\\.\\.\\b_n\end{pmatrix}\in\text{Mat}_{n\times 1}$

$X=\begin{pmatrix}x_1\\.\\.\\.\\x_m\end{pmatrix}\in\text{Mat}_{n\times 1}$

$AX=B$

$\left(\begin{array}{c|c}A & B \end{array}\right)$
A "matrice dei coefficienti" (del sistema)
A|B "matrice completa" (del sistema)

Due sistemi si dicono **equivalenti** se hanno lo stesso insieme di soluzioni
Un sistema si dice **omogeneo** se la colonna B dei termini noti è $= 0$

Eseguire operazioni elementari sulla matrice associata ad un sistema lineare produce una matrice associata ad un sistema lineare equivalente
Un sistema lineare è risolubile se e solo se nella forma ridotta della matrice completa non c'è un pivot nell'ultima colonna

$\begin{cases} x_3+x_4=1 \\ 2x_1+2x_2+x_3-5x_4=5 \\ 3x_1+3x_2-x_3=0 \\ x_1+x_2-x_4=1\end{cases}$

$$
\left(
\begin{array}{cccc|c}
0 & 0 & 1 & 1 & 1\\
2 & 2 & 1 & -5 & 5 \\
3 & 3 & -1 & 0 & 0\\
1 & 1 & 0 & -1 & 1 \\
\end{array}
\right)
\rightarrow
\begin{array}\\
R_1\Leftrightarrow R_4 \\
R_2\rightarrow R_2-2R_4 \\
R_3\rightarrow R_3-3R_4
\end{array}
\left(
\begin{array}{cccc|c}
1 & 1 & 0 & 1 & 1\\
0 & 0 & 1 & -3 & 3 \\
0 & 0 & -1 & 3 & 3\\
0 & 0 & 1 & 1 & 1 \\
\end{array}
\right)
\rightarrow
\begin{array}\\
R_3\rightarrow R_3+R_2 \\
R_4\rightarrow R_4-R_2
\end{array}
\left(
\begin{array}{cccc|c}
1 & 1 & 0 & 1 & 1\\
0 & 0 & 1 & -3 & 3 \\
0 & 0 & 0 & 0 & 4\\
0 & 0 & 0 & 4 & -2 \\
\end{array}
\right)
\rightarrow
R_3\Leftrightarrow R_4
\left(
\begin{array}{cccc|c}
1 & 1 & 0 & 1 & 1\\
0 & 0 & 1 & -3 & 3 \\
0 & 0 & 0 & 4 & -2 \\
0 & 0 & 0 & 0 & 4 \\
\end{array}
\right)
\rightarrow
R_3\rightarrow\frac{1}{4}R_3
\left(
\begin{array}{cccc|c}
1 & 1 & 0 & 1 & 1\\
0 & 0 & 1 & -3 & 3 \\
0 & 0 & 0 & 1 & -\frac{1}{2} \\
0 & 0 & 0 & 0 & 4 \\
\end{array}
\right)
\rightarrow
$$
$$
\rightarrow
\begin{array}\\
R_1\rightarrow R_1-R_3 \\
R_2\rightarrow R_2-3R_3
\end{array}
\left(
\begin{array}{cccc|c}
1 & 1 & 0 & 0 & \frac{1}{2}\\
0 & 0 & 1 & 0 & \frac{3}{2} \\
0 & 0 & 0 & 1 & -\frac{1}{2} \\
0 & 0 & 0 & 0 & 4 \\
\end{array}
\right)\ \ \ \ 
\begin{cases}
x_1+x_2=\frac{1}{2}\\
x_3=\frac{3}{2}\\
x_4=-\frac{1}{2}
\end{cases}\ \ \ \
\{
(\frac{1}{2}-x_2, x_2, \frac{3}{2}, -\frac{1}{2})\ |\ x_2\in\mathbb{R}
\}
$$

Sia $AX=B$ un sistema lineare risolubile (o compatibile)
Sia $n$ il numero di incognite (numero di colonne di $A$)
Sia $p$ il numero di pivot nella matrice ridotta (se parto da $A$ o da $A|B$)
Quindi $p\le n$
Se $p=n$ il sistema ha un'unica soluzione
Se $p<n$ il sistema ha infinite soluzioni, che possiamo parametrizzare in termini di $n-p$ indeterminate (l'insieme delle soluzioni ha dimensione $n-p$)

### Osservazione
I sistemi omogenei sono sempre risolubili
$$
\left(
\begin{array}{cccc|c}
1 & 1 & 0 & 0 & \frac{1}{2}\\
0 & 0 & 1 & 0 & \frac{3}{2} \\
0 & 0 & 0 & 1 & -\frac{1}{2} \\
0 & 0 & 0 & 0 & 4 \\
\end{array}
\right)\ \ \ \ 
$$

### Determinante
Sia $A\in\text{Mat}_n$ (quadrata)
Il determinante di $A$ è un numero scalare determinante $A$ che contiene molta informazione sulla matrice $A$

Data una matrice $A\in\text{Mat}_{n\times m}$, un **minore** di $A$ è una matrice ottenuta da $A$ scartando alcune righe e colonne

$$
\begin{pmatrix}
1 && 2 && 3 \\
4 && 5 && 6
\end{pmatrix} 
\rightarrow^{\text{minore}}
\begin{pmatrix}
1 && 2 \\
4 && 5
\end{pmatrix} \ \
/ 
\ \ 
\begin{pmatrix}
3 \\
6
\end{pmatrix}
$$
Se $A\in\text{Mat}_n$
$i,j=1$

$A_{ij}$ è il minore $\in\text{Mat}_{n-1}$ ottenuto cancellando la riga i e la colonna j

n=1 (a) det A=a
n=2 $\begin{pmatrix}a && b \\c && d \end{pmatrix}$ det A = $ad-bc$

n=3$\begin{pmatrix}a_{11} && a_{12} && a_{13} \\ a_{21} && a_{22} && a_{23} \\ a_{31} && a_{32} && a_{33} \end{pmatrix}$ det A=$a_{11}\left|\ \begin{array}\ a_{22} & a_{23} \\ a_{32} & a_{33}\\\end{array}\ \right| -a_{12}\left|\ \begin{array}\ a_{21} & a_{23} \\ a_{31} & a_{33}\\\end{array}\ \right| +a_{13}\left|\ \begin{array}\ a_{21} & a_{22} \\ a_{31} & a_{32}\\\end{array}\ \right|$


$n\ge3$ $\text{det }A=\sum_{n}^{i=1}{(-1)^na_{1i}}\cdot \text{det}A_{1i}$

$$
\left|
\
\begin{array}
-1 & 0 & 2\\
2 & 1 & 2\\
-1 & 1 & 4
\end{array}
\ \
\right|
=(-1)
\left|
\
\begin{array}\
1 & 2 \\
1 & 4\\
\end{array}
\
\right|
-0
\left|
\
\begin{array}\
2 & 2 \\
-1 & 4\\
\end{array}
\
\right|
+2
\left|
\
\begin{array}\
2 & 1 \\
-1 & 1\\
\end{array}
\
\right|
=
(-1)
(1\cdot4 - 1\cdot2)
+2
(2\cdot1 - (-1)1)
=
(-1)2 + 2\cdot3
=
6-2
=
4
$$
det $I_n$=1
det $E_i(\alpha)=\alpha$

det$\begin{pmatrix}d_1 && 0 \\0 && d_n \end{pmatrix}$ = $\prod_{i=1}^{n}d_i=d_1\cdot d_2\cdot\ldots\cdot d_n$

det$\begin{pmatrix}d_1 && 0 \\0 && d_n \end{pmatrix} = d_1\cdot \text{det}\begin{pmatrix}d_2 && 0 \\0 && d_n \end{pmatrix}=d_1\cdot d_2\cdot \text{det}\begin{pmatrix}d_3 && 0 \\0 && d_n \end{pmatrix} = \ldots = d_1\cdot\ldots\cdot d_{n-1}\text{det}(d_n)=d_1\cdot\ldots\cdot d_n$

det$E_ij(\alpha)=1$ 
det $E_{ij}=-1$

#### Teorema di Binet
Siano $A,B\in\text{Mat}_n$
$\text{det}(AB)=(\text{det}A)(\text{det}B)$


- Scambiando due righe, il determinante si moltiplica per -1
- $R_i\Rightarrow R_i+\alpha R_j$ il determinante non cambia
- $R_i\Rightarrow \alpha R_i$ il determinante si moltiplica per $\alpha$

Il determinante di una matrice triangolare è il prodotto degli elementi sulla diagonale 

$A\in\text{Mat}_n$ è invertibile $\iff \text{det}A\ne0$
Se $A$ è invertibile, $\text{det}(A^{-1})=\frac{1}{\text{det(a)}}$
Se $A$ ha due righe uguali, il suo det è 0
Se A ha una riga di 0, il suo det è 0
$\text{det}A=\text{det}A^t$

#### Teorema di Laplace
$A\in\text{Mat}_n$
$\forall\ i=1,\ldots,n$
$\text{det}A=\sum_{j=1}{n}{(-1)^{i+j}}\cdot a_{ij}\cdot\text{det}A_{ij}$
$\forall\ j=1,\ldots,n$
$\text{det}A=\sum_{i=1}{n}{(-1)^{i+j}}\cdot a_{ij}\cdot\text{det}A_{ij}$


#### Regola di Sarrus
$$
a_{11}\left|\ \begin{array}\ a_{22} & a_{23} \\ a_{32} & a_{33}\\\end{array}\ \right|
-a_{12}\left|\ \begin{array}\ a_{21} & a_{23} \\ a_{31} & a_{33}\\\end{array}\ \right|
+a_{13}\left|\ \begin{array}\ a_{21} & a_{22} \\ a_{31} & a_{32}\\\end{array}\ \right|
= a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}
 -a_{12}a_{21}a_{33}+a_{12}a_{31}a_{23}
 +a_{13}a_{21}a_{32}-a_{13}a_{31}a_{22}
$$

### Formula di Leibniz
$A\in\text{Mat}_n$
$\text{det}A=\sum_{\sigma\in S_n}{(-1)^\sigma}\prod_{i=1}^{n}{a_{i\sigma(i)}}$
$\{\sigma:\{1,\ldots,n\}\rightarrow\{1,\ldots,n\} \text{ biunivoche}\}$


$A=(a_{ij}), \in\text{Mat}_n$
$(((-1)^{i_j}\text{det}A_{ij})_{ij})^T\cdot A=(\text{det}A)I_n$
Se $A$ è invertibile, $A^{-1}=\frac{1}{\text{det}A}\cdot((-1)^{i+j}\text{det}A_{ij})_{ij}$

$$
\begin{pmatrix}
a && b \\
c && d
\end{pmatrix}
\rightarrow
\begin{pmatrix}
d && -c \\
-b && a
\end{pmatrix}^T
\text{"Matrice aggiunta"}
=
\begin{pmatrix}
d && -b \\
-c && a
\end{pmatrix}
\text{ "Matrice dei cofattori"}
$$

$$
\begin{pmatrix}
a && b \\
c && d
\end{pmatrix}
\cdot
\begin{pmatrix}
d && -b \\
-c && a
\end{pmatrix}
=
(ad-bc)
\begin{pmatrix}
1 && 1 \\
0 && 0
\end{pmatrix}
$$
$$
\begin{pmatrix}
a && b \\
c && d
\end{pmatrix}^{-1}
=
\frac{1}{ad-bc}
\begin{pmatrix}
d && -b \\
-c && a
\end{pmatrix}
$$


Sia $A\in\text{Mat}_{n\times m}$
Il **rango** di $A$ è l'ordine massimo di un minore quadrato invertibile di $A$
Sia $B\in\text{Mat}_{K}$, l'ordine è K

$$
\begin{pmatrix}
1 && 2 && 3 && -1 \\
2 && 4 && 6 && -2 \\
1 && 5 && 3 && 2
\end{pmatrix}
$$
$\left|\begin{array}\ \ 1 & 2\  \\2 & 4\ \end{array}\right| =4-4=0$

$\left|\begin{array}\ \ 1 & -1\  \\1 & 2\ \end{array}\right| =2+1=3\ne0$

$\left|\begin{array}\ \ 1 & 2 & 3\  \\2 & 4 & 3\ \\1 & 5 & 3\end{array}\right|= \left|\begin{array}\ \ 4 & 6\  \\5 & 3\ \end{array}\right| -2\left|\begin{array}\ \ 2 & 3\  \\5& 3\ \end{array}\right| + \left|\begin{array}\ \ 2 & 3\  \\4 & 6\ \end{array}\right| =12-30-2(6-15)+12-12=-18-2\cdot(-9)+0=0$

Il rango di una matrice è il numero di pivot al termine della riduzione di Gauss
$nK(A)=nK(A^t)$
(perché $\forall B\text{ quadrata det }B=\text{det }B^t$)

Il numero corrispondente ai pivot è triangolare superiore
Se $E$ è una matrice elementare, $A$ matrice qualunque
$nK(A)=nK(EA)$, di conseguenza $\forall A\in\text{Mat}_{n \times m}$, $\forall B\in\text{GL}_{m}$    $nK(A)=nK(BA)$ $\{M\in\text{Mat}_m\ |\ M\text{ è invertibile} \}$

$A\in\text{Mat}_{n\times m}$
$nK(A)\le\text{min}(m,n)$
Se $A\in\text{Mat}_{n\times m}$  $nK(A)=n \iff A \text{ è invertibile}$

$$
\begin{pmatrix}
1 && 2 && 0 && -1 \\
0 && 1 && 1 && -1 \\
1 && 1 && -1 && 0 \\
1 && 0 && -2 && -1
\end{pmatrix}
\begin{pmatrix}
1 && 2 && 0 && -1 \\
0 && 1 && 1 && -1 \\
0 && -1 && -1 && -1 \\
0 && -2 && -2 && 2
\end{pmatrix}
\begin{pmatrix}
1 && 2 && 0 && -1 \\
0 && 1 && 1 && -1 \\
0 && 0 && 0 && 0 \\
0 && 0 && 0 && 0
\end{pmatrix}
\ \ \ \ 
\text{ha rango 2}
$$
$$
\begin{pmatrix}
a && -1 && 2a && 1 \\
0 && 2 && 1 && -2
\end{pmatrix}
$$

### Teorema degli orlati di Kronecker

$$
m
\overset{n}{
\begin{pmatrix}
&&&&\\&&&&
\end{pmatrix}
}
\ \ \ \ 
nK=r
$$
$A\in\text{Mat}_{n\times m}$
$(m-r)(n-r)$

$nK(A)=r \iff$:
- $\exists$ un minore $M\ r\times r$ invertibile
- Tutti i minori $(r+1)\times(r+1)$ che contengono $M$ come minor
- 
- e hanno det $=0$

$$
\begin{pmatrix}
-3 && 2h && -2 \\
-3 && 2+2h && -1 \\
h && 0 && 1
\end{pmatrix}
$$
$(-3)$ invertibile, $nK\ge1$
$\left|\ \begin{array}\ -3 & -2 \\ -3 & -1\\\end{array}\ \right|=3-6\ne0$, $nk\ge2$

$\text{det}=h(-2h+2(2+2h))+(-3(2+2h)+6h)=h(4+2h)-6=2h^2+4h-6=2(h+3)(h-1)$
se $h \ne1,-3$ il rango è 3
se $h =1,-3$ il rango è 2

### Teorema di Cramer
Sia $A\in\text{Mat}_n$ e $B\in\text{Mat}_{n\times m}$
Il sistema lineare $AX=B$ ha una sola soluzione $\iff\text{det}A\ne0$
In questo caso $X=A^{-1}B=\frac{1}{\text{det}A}A^*B$ ($A^*$ matrice aggiunta)

Esplicitamente
$$
x_i
=
\frac
{
\left|
\begin{array}\ \ 
| & | & | & | & |\ \\ \
c_1 & c_{i-1} & B & c_{i+1} & c_n\ \\ \
| & | & | & | & |\ \\
\end{array}
\right|
}
{\text{det}A}
$$
$C_j$ le colonne di A
$A^*\ \ \ \ (((-1)^{i+j}\text{det}A_{ij})_{ij})$

Sviluppiamo il determinante lungo la colonna i
$(-1)^{i+1}\ b_1\ \text{det}A_{1i}+(-1)^{2+i}\ b_2\ \text{det}A_{2i}\ +\ -\ +\ldots$
$\sum_{k=1}^{n}(-1)^{k+i}\ b_k\ \text{det}A_{ki}$

#### Osservazione
Se $A\in\text{GL}_n(\mathbb{Z})$ i coefficienti di $A^{-1}$ hanno come denominatore un divisore di $\text{det}A$
### Teorema di Rouché - Capelli
Il sistema $AX=B$ (non necessariamente quadrato) ha soluzioni $\iff rk(A)=rk(AB)$
Se $rk(A)=rk(AB)=n$ il sistema ha una sola soluzione
Se $rk(A)=rk(AB)<n$ il sistema ha infinite soluzioni che formano uno spazio di dimensione $n-rk(A)$
