$x\in\{x_1,x_2,\ldots,x_n,\ldots\}$

| $x$      | $\mathbb P[X=x]$       |
| -------- | ---------------------- |
| $x_1$    | $p_1=\mathbb P[X=x_1]$ |
| $x_2$    | $p_2=\mathbb P[X=x_2]$ |
| $\vdots$ | $\vdots$               |
| $x_n$    | $p_n=\mathbb P[X=x_n]$ |
| $\vdots$ | $\vdots$               |

Legge è riassunta dalla successione $p_1,p_2,\ldots,p_n,\ldots$

$\array{p_i\ge0\\p_i\le1}\quad\forall\ i\ge1$

$p_1,p_2,\ldots,p_n,\ldots=1$



$p_1+\ldots+p_n+\ldots=\sum\limits_{n=0}^{+\infty}p_n=\lim\limits_{n\to+\infty}(p_1+\ldots+p_n)=1$


## Esempio
Lancio una moneta equilibrata finché non esce testa
$N=\text{numero di lanci fatti}$
$N=\{\underset{x_1}1,\underset{x_2}2,\ldots,\underset{x_n}n,\ldots\}=\mathbb N\setminus\{0\}$

| $n$      | $\mathbb P[N=n]$                                                                                                                                     |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| $1$      | $p_1=\mathbb P[N=1]=\mathbb P[T]=\frac12$                                                                                                            |
| $2$      | $p_1=\mathbb P[N=2]=\mathbb P[CT]=\frac12\cdot\frac12=\frac14$                                                                                       |
| $\vdots$ | $\vdots$                                                                                                                                             |
| $n$      | $p_1=\mathbb P[N=2]=\mathbb P[\underbrace{(C\ldots C)}_{n-1\text{ volte}}T]=\underbrace{\frac12\ldots\frac12}_{n-1\text{ croci}}\frac12=\frac1{2^n}$ |
| $\vdots$ | $\vdots$                                                                                                                                             |

$\array{p_n\ge0&p_n=\frac1{2^n}>0\\p_n\le1&p_n=\frac1{2^n}<1}\quad\forall\ n\ge1$

$1=\sum\limits_{n=1}^{+\infty}p_n=p_1+p_2+\ldots+p_n+\ldots=\frac12+\frac14+\ldots+\frac1{2^n}+\ldots=\text{base binaria}(0,1)_2+(0,01)_2+(0,001)_2+\ldots+(0,\underbrace{00\ldots00}_{n-1\text{ croci}}1)_1+\ldots=(0,11\ldots1\ldots1)_2=(0,\overline1)_2=1$

$\sum\limits_{n=1}^{+\infty}p_n=\sum\limits_{n=1}^{+\infty}(\frac12)^n=\underbrace{\sum\limits_{n=1}^{+\infty}q^n}_{\array{\text{serie geometrica}\\\text{di ordine }q=\frac12}}\underset{|q|<1}=\frac q{1-q}=\frac{\frac12}{1-\frac12}=\frac{\frac12}{\frac12}=1$

# Variabili aleatorie con densità
Una variabile aleatoria $X$ ha densità $f$ se $\mathbb P[a\le X\le b]=\int_a^b f(x)dx$ dove $f:I\to\mathbb R\quad I=\mathbb R\setminus\{x_1,\ldots,x_n\}$ tale che $\ \begin{array}{l}f\text{ è continua}\\f\text{è integrabile in senso improprio su }(-\infty,x_1),(x_1,x_2),(x_{N-1},x_N)\text{ e }(x_N,+\infty)\\f(x)\ge0\quad\forall\ x\in I\\\int_{-\infty}^{+\infty}f(x)dx=1\end{array}$


$\text{Area}=\int_a^b f(x)dx=\mathbb P[a\le X\le b]$

$f:\mathbb R\setminus\{x_1\}\to\mathbb R$

$a<x_1<b$

$\text{Area regione verde}=\mathbb P[a\le X\le b]$
Integrale in senso improprio = Area finita

$\int_a^b f(x)dx={\color{#F44}\int_a^{x_1} f(x)dx}+{\color{#74F}\int_{x_1}^b f(x)dx}$

${\color{#F44}\int_a^{x_1} f(x)dx}=\lim\limits_{l\to{x_1}^-}\int_a^l f(x)dx\in\mathbb R$
${\color{#74F}\int_{x_1}^b f(x)dx}=\lim\limits_{l\to{x_1}^+}\int_l^b f(x)dx\in\mathbb R$


$\mathbb P[X\in\mathbb R]=\mathbb P[X\in(-\infty,+\infty)]=1=\text{area}=\int_{-\infty}^{+\infty}f(x)dx$

## Esempio
Estraggo un numero reale a caso tra $\frac12$ e $1$
Qual'è la probabilità che il numero estratto sia più piccolo di $\frac34$?

$X=\text{numero estratto}\qquad x\in[\frac12,1]$

$\mathbb P[x<\frac34]=\mathbb P[x\le\frac34]=\int_{-\infty}^{\frac34}f(x)dx$

$f(x)=\begin{cases}0&x<\frac12\\c&\frac12<x<1\\0&x>1\end{cases}$

$c\ge0$
$\text{area positive probabilità}>0$
$\int_{-\infty}^{+\infty}f(x)dx=1=\mathbb P[x\in\mathbb R]=\text{base}\cdot\text{altezza}=(1-\frac12)c$

$1=\frac12c\quad c=2$

$f(x)=\begin{cases}0&x<\frac12\\2&\frac12<x<1\\0&x>1\end{cases}$
$I=\text{dom}(f)=(-\infty,\frac12)\cup(\frac12,1)\cup(1,+\infty)$

$f(x)\ge\frac12$

$\mathbb P[a\le X\le b]=\int_ab f(x)dx\in[0,1]$

$\mathbb P[X\le\frac34]=(\frac34-\frac12)\cdot2=\frac12$

## Proprietà
$X\text{ variabile con densità }f$
- $\mathbb P[X=x]=0\quad\forall\ x\in\mathbb R$
- $\mathbb P[a\le X\le b]=\mathbb P[a< X< b]$
- $\array{\mathbb R[X\le a]=\mathbb R[X<a]\\\mathbb R[X\ge b]=\mathbb R[X<b]}$
- $m\le X\le M\iff x\in[m,M]\iff\mathbb P[X\in[m,M]]=1$

### Esercizio
$X\text{ variabile con densità }f$
$f(x)=\cases{0&x<0\\mx&0<x<1\\0&x>1}$

Calcolare la probabilità che $\mathbb P[2x^2-1=0]$ e $\mathbb P[|x|\le\frac12]$

$\text{Dom}(f)=(-\infty,0)\cup(0,1)\cup(1,+\infty))$
$f\text{ è "bella" = posso calcolare le aree}$
$m\ge0$

$\int_{-\infty}^{+\infty}f(x)dx=1=\frac12(1-0)(m-0)=\frac m2=1\qquad m=2$
$f(x)=\cases{0&x<0\\2x&0<x<1\\0&x>1}$

$\mathbb P[2x^2-1=0]=\mathbb P[x^2=\frac12]=\mathbb P\left[x=\pm\sqrt\frac12\right]=\mathbb P\left[\{x=\sqrt12\}\cup\{x=-\sqrt\frac12\}\right]=\mathbb P\left[x=\sqrt\frac12\right]+\mathbb P\left[x=-\sqrt\frac12\right]=0+0=0$

$\mathbb P\left[|x|\le\frac12\right]=\mathbb P\left[-\frac12\le X\le 12\right]=\frac12(\frac12-0)\cdot 1=\frac14$





$X\text{ variabile aleatoria con densità }f$
$f(x)=c\frac1{1+x^2}$
Calcolare la probabilità che $x\ge1$
$c>0$

$\text{Area totale}=\int_{-\infty}^{+\infty}f(x)dx=\int_{-\infty}^{+\infty}c\frac1{1+x^2}=c\int_{-\infty}^{+\infty}\frac1{1+x^2}=2c\int_0^{+\infty}\frac1{1+x^2}dx$

$1=2c\lim\limits_{b\to+\infty}\int_0^b\frac1{1+x^2}dx$

$\int\frac1{1+x^2}dx=\arctan x+const$
$\int_0^b\frac1{1+x^2}dx=\left[\arctan x\right]_0^b=\arctan b-\arctan 0=\arctan b$

$1=2c\lim\limits_{b\to+\infty}\int_0^b\frac1{1+x^2}dx=2c\lim\limits_{b\to+\infty}\arctan b=\cancel2c\frac\pi{\cancel2}\qquad c=\frac1\pi$
$f(x)=\frac1\pi\cdot\frac1{1+x^2}$

$\mathbb P[x\le 1]=\int_1^{+\infty}\frac1\pi\frac1{1+x^2}dx=\frac1\pi\int_1^{+\infty}\frac1{1+x^2}dx=\frac1\pi\left[\arctan x\right]_1^{+\infty}=\frac1\pi(\underbrace{\arctan(+\infty)}_{\lim\limits_{x\to+\infty}\arctan(x)}-\arctan(1))=\frac1\pi[\frac\pi2-\frac\pi4]=\frac1{\cancel\pi}\frac{\cancel\pi}4=\frac14$

$\mathbb P[x\le1]=\frac1-\mathbb P[x>1]=1-\frac14=\frac34$





$X\text{ variabile con densità}$
$f(x)=\begin{cases}a&-1<x<0\\b&1\le x\le\frac32\\0&\text{altrove}\end{cases}$

Determinare $a$ e $b$

$\begin{cases}a\ge0\\b\ge0\\\\\int_{-\infty}^{+\infty}f(x)dx=1\end{cases}$

$1=(0-(-1))\cdot a+(\frac12)\cdot b$
$1=1a+\frac12b$

$2=2a+b$
$b=2-2a$

$$