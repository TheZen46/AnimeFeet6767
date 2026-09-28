$X$ e $Y$  variabili aleatorie
Sono dette indipendenti e $\mathbb P[\underbrace{X\in I}_E\text { e }\underbrace{Y\in J}_F]=\mathbb P[\underbrace{X\in I}_E]\cdot\mathbb P[\underbrace{Y\in J}_F]\ \ \forall I,J\in\mathbb R$
$X\perp\!\!\!\perp Y$
# Proprietà
Se $X$ e $Y$ sono indipendenti ($X\perp\!\!\!\perp Y$) allora $\varvarphiphiphi(x)$ e $\psi(y)$ sono indipendenti
	$\left(\varphi(x)\perp\!\!\!\perp\psi(y)\right)\qquad\begin{array}{l}\varphi:A\to\mathbb R&X\in A\\\psi:B\to\mathbb R&B\in B\end{array}$

## Esempio
Se $x\perp\!\!\!\perp Y$ allora $\underset{\varphi(x)}{X^2}\perp\!\!\!\perp\underset{\psi(y)}{Y^2}\qquad\underset{\varphi(x)}{X^2}\perp\!\!\!\perp\underset{\psi(y)}{Y^4}$

# Formula probabilità totale
$X$ variabile aleatoria finita/discreta
$X\in\{x_1,x_2,\ldots,x_n\}\qquad x_i\ne x_j\quad i\ne j$
Allora $\mathbb P[E]=\mathbb P[E|X=x_1]\cdot\mathbb P[X=x_1]+\ldots+\mathbb P[E|X=x_n]\cdot\mathbb P[X=x_n]$

# Esercizio
Lancio $2$ volte un dado equilibrato a $6$ facce
1) Qual'è la probabilità che la somma sia $8$?
2) Qual'è la probabilità che il risultato sia $3$ sapendo che la somma è $8$?

Somma$=X+Y\qquad\begin{array}{l}x=\text{primo tiro}\\y=\text{secondo tiro}\end{array}$

1) $\mathbb P[X+Y=8]$
2) $\mathbb P[X=3|X+Y=8]$

$\begin{array}{l}X&\in&\{1,\ldots,6\}\\Y&\in&\{1,\ldots,6\}\end{array}$

| $x$ | $\mathbb P[X=x]$ |
| --- | ---------------- |
| $1$ | $\frac16$        |
| $2$ | $\frac16$        |
| $3$ | $\frac16$        |
| $4$ | $\frac16$        |
| $5$ | $\frac16$        |
| $6$ | $\frac16$        |

| $y$ | $\mathbb P[Y=y]$ |
| --- | ---------------- |
| $1$ | $\frac16$        |
| $2$ | $\frac16$        |
| $3$ | $\frac16$        |
| $4$ | $\frac16$        |
| $5$ | $\frac16$        |
| $6$ | $\frac16$        |

$X\sim Y$
$X\perp\!\!\!\perp Y$

1) $\displaystyle\mathbb P[X+Y=8]=\sum\limits_{i=1}^6\mathbb P[X+Y=8|X=i]\cdot\mathbb P[X=i]=\frac16\sum\limits_{i=1}^6\mathbb P[X+Y=8|X=i]=\frac16\sum\limits_{i=1}^6 1_{\operatorname{supp}(Y)}(8-i)=\frac16\left(0+\mathbb P[Y=6]+\mathbb P[Y=5]+\mathbb P[Y=4]+\mathbb P[Y=3]+\mathbb P[Y=2]\right)=\frac16\frac56=\frac5{36}$
2) $\mathbb P[X=3|X+Y=8]=\frac{\mathbb P[X+Y=8|X=3]\mathbb P[X=3]}{\mathbb P[X+Y=8]}$
		$\mathbb P[X+Y=8|X=3]=\mathbb P[Y=5]$
	$\displaystyle\mathbb P[X=3|X+Y=8]=\frac{\frac16\frac16}{\frac5{36}}=\frac15$

# Speranza
$\text{Speranza}\longleftrightarrow\text{Media empirica}$
$\mathbb E[X]=\sum{i=1}^n i\cdot\mathbb P[X=i]$

## Esercizio
$X\text{ ha densità }f$

$y=f(x)$

$\text{Area}=\mathbb P[a\le x\le b]=\int_a^bf(x)dx$

$\mathbb E[X]=\int_{-\infty}^{+\infty}x\cdot f(x)dx\qquad\text{Speranza di }X$


# Esempio
Lancio una moneta truccata $2$ volte
$p=\mathbb P[T]$
$X=\text{Numero di teste}\qquad\mathbb P[C]=(1-p)$

| $x$         | $\mathbb P[X=x]$   |
| ----------- | ------------------ |
| $\cancel 0$ | $\cancel{(1-p)^2}$ |
| $1$         | $2p(1-p)$          |
| $2$         | $p^2$              |

$\mathbb E[X]=1\qquad 2p(1-p)+2p^2=2p\left[(1-\cancel y)+\cancel y\right]$
$\mathbb E[X]=2p$
$p=\frac13\quad\text{allora }\mathbb E[X]=\frac23\notin\{0,1,2\}$

## Esempio
Lancio un dado equilibrato a $6$ facce
$X=\text{Faccia uscita}\in\{1,\ldots,6\}\qquad\mathbb P[X=n]=\frac16\quad n=1,\ldots,6$
$\mathbb E[X]=1\mathbb P[X=1]+\ldots+6\mathbb P[X=6]=\frac16\left(1+\ldots+6\right)=\frac1{\cancel6}\frac{\cancel6\cdot7}2=\frac72\checkmark\qquad\qquad\displaystyle\small(1+\ldots+n)=\frac{n(n+1)}2$

## Esempio
$X\text{ ha densità }f(x)=\cases{0&x<0\\2x&0<x<1\\0&x>1}$
$\mathbb E[X]=\int_{-\infty}^{+\infty}x\cdot f(x)dx=\int_0^1x\cdot f(x)dx=\int_0^1x\cdot 2xdx=2\int_0^2x^2dx=2\cdot\left.\frac{x^3}3\right|_0^1=\frac23\left(1^3-0^3\right)=\frac23$

## Esercizio
$X\text{ ha densità }f(x)=\cases{0&x<0\\\frac1L e^{-\frac xL}&x<0}\qquad\small L>0$
$\mathbb E[X]=\int_{-\infty}^{+\infty}x\cdot f(x)dx=\int_0^{+\infty}x\cdot \frac1Le^{-\frac xL}dx=\lim_{b\to+\infty}\int_0^bx\cdot \frac1Le^{-\frac xL}dx$
	$\int\frac xLe^{-\frac xL}dx$
		$t=\frac xL\qquad dt=\frac1Ldx\qquad dx=L\ dt$
	$\int t\cdot e^{-t}L\ dt=L\int \underset{f(x)}{t}\cdot\underset{g'(t)}{e^{-t}}$
		$\begin{array}{l}f(t)=t&f'(t)=1\\g(t)=-e^{-t}&g't=e^{-t}\end{array}$
	$L\bigg((t)(-e^{-t})\int 1(-e^{-t})dt\bigg)=L\bigg(-t(e^{-t})-e^{-t}+c\bigg)=L\bigg(-e^{-t}(t+1)+c\bigg)=-L\bigg(e^{-\frac xL}(\frac xL+1)+c\bigg)$
$\mathbb E[X]=\lim\limits_{b\to+\infty}\bigg(-L\ e^{-\frac xL}(\frac xL+1)\bigg)\Bigg|_0^b=-L\lim\limits_{b\to+\infty}\bigg(\underbrace{\underset{\to0}{e^{-\frac xL}}(\underset{\to\infty}{\frac xL+1})}_{\to0}-1\bigg)=-L(-1)=L$
$\mathbb E[X]=L$


# Proprietà
- Se $X\sim Y$ allora $\mathbb E[X]=\mathbb E[Y]$
- Se $X=c\quad\mathbb E[X]=c$
- **Linearità:** $\mathbb E[\underbrace{a\ \!X+b\ \!Y}_{\text{Comb. lin.}}]=a\ \mathbb E[X]+b\ \mathbb E[Y]$
- **Indipendenza:** Se $X\perp\!\!\!\perp Y$ allora $\mathbb E[XY]\underset{\mathbb E[]}{=}\mathbb E[X]\cdot\mathbb E[Y]$
- Monotonia: $\begin{array}{l}\text{se }X\ge0&\mathbb E[X]\ge0\\\text{se }x\le Y&\mathbb E[X]\le\mathbb E[Y]\\\text{se }m\le X\le0&m\le\mathbb E[X]\le M\end{array}$
- **Formula di trasferimento:** $\mathbb E[\varphi(x)]$
	**Caso finito:** $\mathbb E[\varphi(x)]=\varphi(x_1)\mathbb P[X=x_1]+\ldots+\varphi(x_n)\mathbb P[X=x_n]$
	**Caso con densità:** $\mathbb E[\varphi(x)]=\int_{-\infty}^{+\infty}\varphi(x)f(x)dx$
- **Integrazione sulle code:** Se $X\in\mathbb N\quad x\in\{0,1,\ldots,n\}$
	$\begin{array}{l}\mathbb E[X]&\mskip -12mu=&\mskip -2mu\mathbb P[X>0]+\mskip 10mu\mathbb P[X>1]+\ldots+\mskip 12mu1\mathbb [X>n]&\mskip -12mu=&\mskip -12mu\sum\limits_{j=0}^{+\infty}\,\phantom{n}\mathbb P[X>j]\\&\mskip -12mu=&\mskip -12mu1\mathbb P[X=1]+2\mathbb P[X=2]+\ldots+n\mathbb P[X=n]&\mskip -12mu=&\mskip -12mu\sum\limits_{j=0}^{+\infty}\,n\mathbb P[X=n]\end{array}$
## Esercizio
Lancio una moneta truccata due volte
$\mathbb P[T]=p$
$X=\begin{cases}1&\text{testa al primo lancio}\\0&\text{croce al primo lancio}\end{cases}\mskip{40mu} Y=\begin{cases}1&\text{testa al secondo lancio}\\0&\text{croce al secondo lancio}\end{cases}$
$\mathbb E[X+Y]=\mathbb E[X]+\mathbb E[Y]=2\mathbb E[X]=2p$
**Linearità**    $x\sim y\Rightarrow \mathbb E[X]=\mathbb E[Y]$

$X+Y=\text{Numero di teste su due lanci}$


$\mathbb E[2XY+3]=2\mathbb E[XY]+\mathbb E[3]=\mathbb E[X]\mathbb E[Y]+3\mskip30mu X\perp\mskip-9mu\perp Y$
	$=2(\mathbb E[X])^2+3=2p^2+3$

$\mathbb E[X^2]=\mathbb E[X\cdot X]=\begin{array}{l}{\color{#F44}\mathbb E[X]\cdot\mathbb E[X]=p^2}&{\color{#F44}\boldsymbol\times}\\0^2\mathbb P[X=0]+1^2\mathbb P[x=1]=p&{\color{#7C4}\checkmark}\end{array}$



$\displaystyle\mathbb E[\frac{\cos(\pi X)}{1+Y}]=\mathbb E\left[\underset{{\color{#7BD}\varphi(X)}}{\cos(\pi X)}+\underset{{\color{#7D7}\psi(Y)}}{\frac1{1+Y}}\right]=\mathbb E\left[\cos(\pi x)\right]\cdot\mathbb E\left[\frac1{1+y}\right]=\left(\right)$
