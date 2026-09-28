$x\in X\leftarrow\text{variabili}$
$D:X\to\mathbb R\leftarrow f\text{ obiettivo}$
$S\subseteq X\leftarrow\text{vincoli}$

$\min\limits_{x\in S}f(x)\mskip{36mu}\max\limits_{x\in S}f(x)$

Esempio
[[Anno 2/Ricerca Operativa/Introduzione#^77438c]]
$\forall i=1,\ldots,70\qquad\forall j=1,\ldots,70$

Definisco
$X_{ij}=\begin{cases}1&\text{se il }R_i\text{ fa il lavoro }L_i\\0&\text{altrimenti}\end{cases}$

$70^2\text{variabili}$

$\forall j=1,\ldots,70\quad\sum\limits_{i=1}^{70}X_{ij}=1$
$\forall i=1,\ldots,70\quad\sum\limits_{j=1}^{70}X_{ij}=1$

|          | $L_1$ | $L_2$ | $\dots$ | $L_{70}$ |
| -------- | ----- | ----- | ------- | -------- |
| $R_1$    | 0     | 0     |         |          |
| $R_2$    | 0     | 1     |         |          |
| $\vdots$ |       |       |         |          |
| $R_{70}$ | 0     | 0     |         | $C_{ij}$ |
$C_{ij}\leftarrow\text{tempo impiegato}$
$\displaystyle\sum\limits_{i=1}^{70}\sum\limits_{j=1}^{70}X_{ij}C_{ij}$

$\min\displaystyle\sum\limits_{i=1}^{70}\sum\limits_{j=1}^{70}X_{ij}C_{ij}$
$\forall j\sum\limits_{i=1}^{70}X_{ij}=1\qquad \forall i\sum\limits_{j=1}^{70}X_{ij}=1\quad X_{ij}\in\{0,1\}$
