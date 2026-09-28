Variabile aleatoria $X:\Omega\to\mathbb R$
$F_X:\mathbb R\to\mathbb R$
$F_X(x)=\mathbb P[X\le x]\qquad x\in\mathbb R$

$x\in\{x_1,\ldots,x_n\}$

``` mermaid
xychart-beta
    title "Finito"
    x-axis [x1, x2, X, xn-1, xn]
    y-axis " "
    bar [3, 5, 2, 4, 1]
```

| $x$      | $\mathbb P[X= x]$               |
| -------- | ------------------------------- |
| $x_1$    | $\mathbb P_1=\mathbb P[X= x_1]$ |
| $x_2$    | $\mathbb P_2=\mathbb P[X= x_2]$ |
| $\vdots$ | $\vdots$                        |
| $x_n$    | $\mathbb P_n=\mathbb P[X= x_n]$ |

$F_X(x)=\sum_{x_k\le x}\mathbb P[X=x_k]$

``` mermaid
xychart-beta
    title " "
    x-axis [x1, x2, X, xn-1, xn]
    y-axis " "
    bar [3, 8, 10, 15, 16]
```


Caso $X$ con densità $f$

$y=f(x)$

$F_X(x)=\mathbb P[X\le x]=\underbrace{\int_{-\infty}^x f(t)dt}_{\text{funzione integrale}}$

# Esempio
Lancio una moneta equilibrata $3$ volte

$X=\text{numero di teste}$
$F_X(x)=\mathbb P[X\le x]$

| $x$ | $\mathbb P[X=x]$ | $F_X(x)$  |
| --- | ---------------- | --------- |
| $0$ | $\frac18$        | $\frac18$ |
| $1$ | $\frac38$        | $\frac48$ |
| $2$ | $\frac38$        | $\frac78$ |
| $3$ | $\frac18$        | $\frac88$ |
$\mathbb P[T]=\mathbb P[C]=\frac12$

``` mermaid
xychart-beta
    title "Numero di teste"
    x-axis [0, 1, 2, 3]
    y-axis " "
    bar [1, 3, 3, 1, 0]
```




$X\text{ ha densità }f(x)=\cases{0&x<0\\1&0<x<1\\0&x>1}$
Area totale 1
$F_X(x)=\mathbb P[X\le x]=\int_{-\infty}^x f(t)dt$

$F_X(x)=\cases{0&x<0\\1x(x-0)&0<x<1\\0&x>1}\quad=\cases{0&x<0\\x&0<x<1\\0&x>1}$




$X\text{ ha densità }f(x)=\frac1\pi\frac1{1+x^2}$
Area totale 1
$\displaystyle F_X(x)=\int_{-\infty}^xf(t)dt=\int_{-\infty}^x\frac1\pi\frac1{1+t^2}dt=\lim\limits_{a\to-\infty}\int_a^x\frac1\pi\frac1{1+t^2}dt=\lim\limits_{a\to-\infty}\frac1\pi\int_a^x\frac1{1+t^2}dt=\lim\limits_{a\to-\infty}\left.\frac1\pi\arctan(t)\right|_a^x=\frac1\pi\lim\limits_{a\to-\infty}\left[\arctan(x)-\arctan(a)\right]=\frac1\pi\left[\arctan(x)+\frac\pi2\right]$

# Proprietà
- $F_X$ è crescente    se $x_1\le x_2$ allora $F_X(x_1)\le F_X(x_2)$
- $\lim\limits_{x\to-\infty}F_X(x)=0\qquad\lim\limits_{x\to+\infty}F_X(x)=1$
- $\lim\limits_{x\to{\underset{\in\mathbb R}{x_0}}^+)}F_X(x)=F(x_0)\qquad \lim\limits_{x\to{x_0}^-}F_X(x)=F(x_0)-\mathbb P[X=x_0]$
- Se $X$ ha densità $f$ ($\Rightarrow\mathbb R[X=x_0]=0\ \ \forall\ x_0\in\mathbb R$) $\lim\limits_{x\to{x_0}^+}F(x)=F(x_0)\iff F_X(x)\text{ è continua in }x=x_0$
- $0\le F_X(x)\le 1\quad\forall\ x\in\mathbb R$
- $\underbrace{X\sim Y}_{\text{stessa legge}}\iff F_X(x)=F_Y(x)\quad\forall\ x\in\mathbb R$
- $\mathbb P[x_1<X\le x_2]=F_X(x_2)-F_X(x_1)\quad x_1<x_2$
- Se $X$ ha densità $F:I\to\mathbb R\qquad I=(-\infty,x_1)\cup(x_1,x_2)\cup\dots\cup(x_n,+\infty)$
	$F_X$ è di classe $C^1$ su $I$        $F_X$ è derivabile $\forall\ x\in I$        $F_X'(x)$ è continua $\forall\ x\in I$        $F_X'(x)=f(x)\quad\forall\ x\in I$

## Esempio
$X\text{ ha densità }f(x)=\cases{0&x<0\\1&0<x<1\\0&x>1}$
$F_X(x)=\cases{0&x<0\\x&0<x<1\\0&x>1}$
