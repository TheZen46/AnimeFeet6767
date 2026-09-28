# Definizione
$\begin{array}{l}X:\Omega\to\mathbb R&\text{Variabile aleatoria}\\\varphi:I\subseteq\mathbb R\to\mathbb R&\text{Funzione }y=\varphi(y)\end{array}\qquad\oplus\ \ x\in I=\text{dom}(\varphi)$

Definiamo una variabile aleatoria
$Y:\Omega\to\mathbb R$
$Y(\omega)=\varphi\left(\underbrace{X(\omega)}_x\right)$
$Y=\varphi(X)$    Funzione della variabile $X$

$y=\varphi(x)=\varphi(X(\omega)=Y(\omega)\qquad x\in I$

## Problema
Data la legge di $X$ determinare la legge di $Y$

### Caso 1
$X$ finita o discreta
#### Esempio
Vado in un casinò il cui ingresso costa $€11$
Gioco al "tavolo"
	Lancia una moneta equilibrata $4$ volte
	Il banco paga $(\text{numero di teste uscite})^2+(\text{numero di croci uscite}\cdot 2)$

$Y=\text{Guadagno (tenendo conto del biglietto d'ingresso)}$
$X=\text{Numero di teste}$

$Y=-11+X^2+2(4-X)=x^2-2x-3$

$x\in\{0,1,2,3,4\}$

| $x$ | $\mathbb P[X=x]$ |     | $y=\varphi(x)$ |
| --- | ---------------- | --- | -------------- |
| $0$ | $\frac1{16}$     |     | $-3$           |
| $1$ | $\frac4{16}$     |     | $-4$           |
| $2$ | $\frac6{16}$     |     | $-3$           |
| $3$ | $\frac4{16}$     |     | $0$            |
| $4$ | $\frac1{16}$     |     | $5$            |

Legge di $Y$

| $y$  | $\mathbb P[Y=y]$                   |
| ---- | ---------------------------------- |
| $-4$ | $\frac4{16}$                       |
| $-3$ | $\frac6{16}+\frac1{16}=\frac7{16}$ |
| $0$  | $\frac4{16}$                       |
| $5$  | $\frac1{16}$                       |


### Caso 2
$X$ con densità $f$

#### Esempio
$X$ ha densità $f(x)=\cases{0&x<0\\2x&0<x<1\\0&x>1}$
Area totale: $\frac12(1-0)2=1\checkmark$

$\varphi(x)=Y=-3x+1$

$0\le X\le 1\Rightarrow -2\le Y\le 1$

$f_Y(y)=\cases{0&y<-2\\\\0&y>1}$

$-2<y<1$

$F_Y(y)=\mathbb P[Y\le y]=f_Y(y)=F_Y'(y)$
