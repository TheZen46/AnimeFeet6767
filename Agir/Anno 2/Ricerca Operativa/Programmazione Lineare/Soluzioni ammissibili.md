$S=\text{insieme ammissibile}$
1) $s=\varnothing\text{ pb inammissibile}$
2) $\text{Se }S\ne\varnothing,\ x\in S\text{ si dice soluzione ammissibile}$
3) $\text{Se esiste }x_\star\in S\text{ tale che }f(x_\star)\ge f(x)\ \forall x\in S\mskip{16mu}x_\star\text{ si dice soluzione ottima, o punto di minimo globale o assoluto}$
	$f(x_\star)\text{ si dice minimo globale o assoluto}$

Spesso $s=\left\{x\in\mathbb R^n\vert\begin{aligned}g_x(x)&\ge b_1\\\vdots\\g_n(x)&\ge b_n\end{aligned}\right\}$

### Osservazione sui vincoli
**Non** è restrittivo usare $g(x)\le b$
Se ho: $3x_1+7x_2\le 3\Rightarrow -3x_1-7x_2\ge-3$
Oppure $8x_1-2x_2=1\Rightarrow\begin{cases}8x_1-2x_2\ge1\\8x_1-2x_2\le1\end{cases}\Rightarrow\begin{cases}\ \ \ 8x_1-2x_2\ge1\\-8x_1+2x_2\ge-1\end{cases}$

Dato un vincolo $g(x)\ge b$ e un punto $\overline x\in\mathbb R^n\ \ (g:\mathbb R^n\to\mathbb R)$
Diciamo che:
- $\overline x$ soddisfa il vincolo se $g(\overline x)\ge b$
- $\overline x$ viola il vincolo se $g(\overline x)<b$
- Il vincolo è attivo in $\overline x$ se $g(\overline x)=b$
- Il vincolo è ridondante se si può eliminare senza cambiare l'insieme $S$

## Modelli di allocazione ottima di risorse
Azienda automobilistica produce $3$ modelli: economica, normale, lusso
(Minuti impiegate in ogni reparto per produzione)

|                 | $E$      | $N$      | $L$      |     | $\max \frac{h}{\text{giorno}}$ |
| --------------- | -------- | -------- | -------- | --- | ------------------------------ |
| $A$             | $20$     | $30$     | $62$     |     | $8$                            |
| $B$             | $31$     | $42$     | $51$     |     | $8$                            |
| $C$             | $16$     | $81$     | $10$     |     | $5$                            |
|                 |          |          |          |     |                                |
| $\text{Prezzo}$ | $1\ 000$ | $1\ 500$ | $2\ 200$ |     |                                |

$\begin{array}{lr}\text{Automobili di lusso}&\le20\%\text{ totale}\\\text{Automobili economiche}&\ge40\%\text{ totale}\end{array}$

### Variabili
$\begin{array}{l}x_1:\text{auto prodotte di tipo }E\\x_2:\text{auto prodotte di tipo }N\\x_3:\text{auto prodotte di tipo }L\end{array}$

### Funzione obiettivo
$1\ 000x_1+1\ 500x_2+2\ 200x_3$

### Vincoli
$\begin{array}{lcl}20x_1+30x_2+62x_3&\le&480\\31x_1+42x_2+51x_3&\le&480\\16x_1+81x_2+10x_3&\le&300\\\end{array}$

$\left.\begin{array}{l}x_3\le\frac{20}{100}(x_1+x_2+x_3)\\x_1\ge\frac{40}{100}(x_1+x_2+x_3)\end{array}\right\}\text{Vincoli di mercato}$

$x_1\ge0,x_2\ge0,x_3\ge0$


|                 | $\overset1E$ | $\overset2N$ | $\overset3L$ |     | $\max \frac{h}{\text{giorno}}$ |
| --------------- | ------------ | ------------ | ------------ | --- | ------------------------------ |
| $\overset1A$    | $20$         | $30$         | $62$         |     | $8$                            |
| $\overset2B$    | $31$         | $42$         | $51$         |     | $8$                            |
| $\overset3C$    | $16$         | $81$         | $10$         |     | $5$                            |
|                 |              |              |              |     |                                |
| $\text{Prezzo}$ | $1\ 000$     | $1\ 500$     | $2\ 200$     |     |                                |
### Variabili
$x_{ij}:\ n\text{ di auto di tipo }j\text{ prodotte dal reparto }i\mskip{28mu}i=\underset1A,\underset2B,\underset3C\mskip{12mu}j=\underset1E,\underset2N,\underset3L$

### Funzione obiettivo
$1\ 000(x_{11}+x_{21}+x_{31})+1\ 500(x_{12}+x_{22}+x_{32})+2\ 200(x_{13}+x_{23}+x_{33})$

### Vincoli
$\begin{array}{lcl}20x_{11}+30x_{12}+62x_{13}&\le&480\\31x_{21}+42x_{22}+51x_{23}&\le&480\\16x_{31}+81x_{32}+10x_{33}&\le&300\\\end{array}$

$\left.\begin{array}{l}x_{13}+x_{23}+x_{33}\le\frac{20}{100}(\sum\limits_{i,j}x_{ij})\\x_{11}+x_{21}+x_{31}\ge\frac{40}{100}(\sum\limits_{i,j}x_{ij})\end{array}\right\}\text{Vincoli di mercato}$

## Modello generale
$\text{Prodotti }p_1,\ldots,p_n;\text{ Risorse }R_1,\ldots,R_m$

|          | $p_1$    | $p_2$    | $\ldots$ | $p_n$    |     |       |
| -------- | -------- | -------- | -------- | -------- | --- | ----- |
| $R_1$    | $a_{11}$ | $a_{12}$ |          | $a_{1n}$ |     | $b_1$ |
| $R_2$    | $a_{21}$ | $a_{22}$ |          | $a_{2n}$ |     | $b_2$ |
| $\vdots$ |          |          |          |          |     |       |
| $R_m$    | $a_{m1}$ | $a_{m2}$ |          | $a_{mn}$ |     | $b_m$ |
$C_j:\text{profitto per il prodotto }j$

### Variabili
$x_1,\ldots,x_n:\text{quantità di prodotto }P_1,\ldots,P_n$

### Vincoli
$\begin{cases}a_{11}x_1+a_{12}x_2+\ldots+a_{1n}x_n\le b_1\\a_{21}x_1+a_{22}x_2+\ldots+a_{2n}x_n\le b_2\\\vdots\\a_{m1}x_1+a_{m2}x_2+\ldots+a_{mn}x_n\le b_m\\x_i\ge 0\ \forall i\end{cases}$

$A=(a_{ij})_{\begin{array}{l}i=1,\ldots,n\\j=1,\ldots,m\end{array}}$
$x=\pmatrix{x_1\\\vdots\\x_n}\mskip{30mu}b=\pmatrix{b_1\\\vdots\\b_m}$
$Ax\le b$

$S=\left\{x\in\mathbb R^n\vert Ax\le b,\ x\ge0\right\}$
### Funzione obiettivo
$c_1x_1+\ldots+c_nx_n=\sum\limits_{j_1}^n c_jx_j=C^Tx$

$\cases{\max C^Tx\\Ax\le b\\x\ge 0}$
$x\in\mathbb R^n$

$m+n\text{ vincoli lineari}$
