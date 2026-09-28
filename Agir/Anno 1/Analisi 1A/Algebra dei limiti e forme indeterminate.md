### Osservazione
Dal teorema restano esclusi alcuni casi, detti forme indeterminate
1) $+\infty-\infty$
2) $\pm\infty\cdot0$
3) $\frac{\pm\infty}{\pm\infty}, \frac 0 0, \frac a 0, \frac{\pm\infty} 0$ 

## Osservazione
$\lim_{x\rightarrow\pm\infty}P(x),\ \ P(x)=a_0,a_1x+\ldots+a_n x^n$, polinomio di grado $n\ \ (a_n \ne 0)$
$P(x)=x^n(a_n+\frac{a_{n-1}}{x}+\ldots+{a_0}{x})=(a_n+0+\ldots+0)$

Concludiamo che
$\lim_{x\rightarrow\pm\infty}P(x)=a_n\cdot\begin{cases}+\infty\text{ se n è pari}\\\pm\infty\text{ se n è dispari}\\\end{cases}$



$\lim_{x\rightarrow\pm\infty}\frac{P(x)}{Q(X)},\ \ \begin{array}{}P(X)=a_0+a_1x+\ldots+a_n x^n (x\ne0)\\Q(X)=b_0+b_1x+\ldots+b_m x^m (x\ne0)\end{array}$
$\frac{P(X)}{Q(X)}=\frac{x^n(a_n+\frac{a_{n-1}}{X}+\ldots+\frac{a_0}{x^n})}{x^m(a_m+\frac{b_{m-1}}{X}+\ldots+\frac{b_0}{x^m})}=x^{n-m}\frac{a_n+0}{b_n+0}$
$\lim_{x\rightarrow\pm\infty}\frac{P(x)}{Q(X)}=\frac{a_n}{b_m}\cdot\lim_{x\rightarrow\pm\infty}n^{n-m}=\frac{a_n}{b_m}\cdot\begin{cases}+\infty,\ n>m,n-m\text{ pari}\\\pm\infty,\ n>m,n-m\text{ dispari}\\1,\ n=m\\0,\ n<m\end{cases}$


## Th (Guarda: continuità della funzione composta)
Guarda: Forme indeterminate esponenziali

$\lim_{x\rightarrow0}(1+x)^\frac1x=e$

$\lim_{x\rightarrow0^+}(1+x)^\frac1x\ \ ^{y\frac{1}{x}}\ \ \lim_{y\rightarrow0^+}(1+\frac1y)^y=e$ 
$\lim_{x\rightarrow0^-}(1+x)^\frac1x\ \ ^{y\frac{1}{x}}\ \ \lim_{y\rightarrow0^-}(1+\frac1y)^y=e$ 

# Teoremi di permanenza del segno, di esistenza degli zeri e di valori intermedi
## Teorema di permanenza del segno
Sia $f$ una funzione continua in $x_0$ e definita in un intorno di $x_0$
Se $f(x_0)>0$, allora esiste un intorno di $x_0$ in cui $f>0$, ovvero $f(x)>0\ \forall x\in I$
Se $f(x_0)<0$, allora esiste un intorno di $x_0$ in cui $f<0$, ovvero $f(x)<0\ \forall x\in I$

### Dimostrazione
Applico th. permanenza del segno per i limiti $a\ \ lim_{x\rightarrow x_0}f(x)=f(x_0)>0$

## Definizione (zero di una funzione)
Data una funzione $f$ a valori reali, si dice **zero** di $f$ un punto $x_0\in\text{dom }f$ tale che $f(x_0)=0$

## Teorema (esistenza degli zeri)
Sia $f$ una funzione continua nell'intervallo \[a,b].
Sia $f(a)\cdot f(b)<0$, allora esiste uno zero di $f$ in $(a,b)$, ovvero $\exists x_0\in(a,b)$ tale che $f(x_0)=0$
Inoltre, se $f$ è iniettiva su un intervallo \[a,b], allora tale zero è unico

Possiamo utilizzare $\text{th. }\exists\ 0$ per verificare che equazioni ottenute da funzioni continue ammettono soluzioni
$P(x)=a_n x^n+a_{n-1}x^{n-1}+\ldots+a_0$    n dispari, $a_n\ne0$    $P(x)=0$
$\lim\limits_{x\rightarrow\pm\infty}P(x)=(a_n)(\pm\infty)$
Da teorema di permanenza del segno trovo $a,b\in\mathbb{R}$ tale che $P(a)P(b)<0$

Siccome $P$ è continua su $\mathbb{R}$ allora è continua $[a,b]$
$\overset{\text{th. }\exists\ 0}{\Rightarrow} \exists x_0\in[a,b]:P(x_0)=0$



$e^x+sin(x)=0$
$x=0:e^0+sin(0)=1>0$
$x=-\frac\pi2:\underset{0<\ \ <1}{e^{-\frac\pi2}}+\underset{=-1}{sin(-\frac\pi2)}<0$

Allora $e^x+sin(x)$ è continua su $[-\frac\pi2, 0]$ e assume valori opposti agli estremi

$\overset{\text{th. }\exists\ 0}{\Rightarrow} \exists x_0\in[-\frac\pi2,0]:e^{x_0}+sin(x_0)=0$
$x_0$ è l'unica soluzione perché $e^x+sin(x)$ è strettamente crescente su $[-\frac\pi2,0]$

## Teorema (valori intermedi)
Sia $f$ una funzione continua su intervallo $[a,b]$
Allora $f$ assume tutti i valori compresi tra $f(a)$ e $f(b)$

### Dimostrazione (conseguenza immediata del th. esistenza zeri)
Considero y compreso tra $f(a)$ e $f(b)$
$g:[a,b]\rightarrow\mathbb{R},\ x\mapsto f(x)-y$
Applico $\text{th. }\exists\ 0$ a $y$

### Controesempi
$\begin{array}{}f:\mathbb{R}\rightarrow\mathbb{R}\\\ \ \ \ x\mapsto\frac1x\\\ \ \ 0\mapsto1\end{array}$

### Corollario
Sia $f$ una funzione continua su un intervallo $I$. Allora l'immagine $f(I)$ è un intervallo di estremi
$\text{inf}_I f=\text{inf}\{f(x):x\in I\},\ \text{sup}_I f=\text{sup}\{f(x):x\in I\}$

# Teoremi di Bolzano-Weierstrass e di Weierstrass

Data una successione reale $(a_n)_{n\ge \overline{n}}$ e una successione di indici $(n_k)_{k>0}$
$n_k\ge \overline{n}$, si definisce **sottosuccessione** (o **successione estratta**) la successione $(a_{n_k})_{k\ge 0}$

### Esempio
$(a_n=(-1)^n)_{n\ge 0}$
$n_k=2k,\ k\ge0$
$a_{n_k}=a_{2k}=(-1)^{2k}=1\Rightarrow (a_{n_k}=1)_{k\ge0}$

$n'_k=2k+1,\ k\ge0$
$a_{n'_k}=a_{2k+1}=(-1)^{2k+1}=-1\Rightarrow(a_{n'_k}=1)$



### Osservazione
Sia $(a_n)$ una successione che ammette limite $l$ (finito oppure $\pm\infty$).
Sia $(a_{n_k})$ una sottosuccessione di $(a_n)$
$\lim\limits_{K\rightarrow\infty}a_{n_k}=l$  per th. sostituzione

## Teorema di Bolzano-Weierstrass
Da ogni successione limitata è possibile estrarre una sottosuccessione convergente

### Dimostrazione (idea)
$(x_n)$    $a\le x_n\le b\ \ \ \ \forall\ n$

## Teorema di Weierstrass
Sia $f$ continua su $[a,b]$
Allora $f$ è limitata su $[a,b]$ e ammette in $[a,b]$
- sia minimo $m=\underset{x\in[a,b]}{\text{min}}=\text{min}\{f(x):x\in[a,b]\}$
- che massimo $M=\underset{x\in[a,b]}{\text{max}}=\text{max}\{f(x):x\in[a,b]\}$
Pertanto $f([a,b)]=[m,M]$

### Esempi

```functionplot
---
title: 
xLabel: x
yLabel: y
bounds: [-4,4, -4,4]
disableZoom: false
grid: true
---
f(x)=x^2
```

$[-1,1]$
$f([-1,1])=[0,1]$


$(-1,1)$
$1=\text{sup}\{x^2:-1<x<1\}$
$\nexists\text{ max}\{x^2:-1<x<1\}$

### Dimostrazione (Weierstrass)
$M:=\text{sup}\{f(x):x\in[a,b]\}$

Due casi: $M$ finito, oppure $M=+\infty$

Caso $M$ finito $\Rightarrow f$ è limitata superiormente
$M-\varepsilon\le f(x)\le M$
$\forall\varepsilon>0\ \  \exists\ x_n\in[a,b]$
$(x_n)$    $a\le x_n\le b$  successione limitata
Estraggo sottosuccessione convergente
$(x_{n_k})$ per th. B-W

$\lim\limits_{n\rightarrow+\infty}f(x_n)=M$
th. sostituzione
$\lim\limits_{k\rightarrow+\infty}f(x_{n_k})$ $\leftarrow$ f è continua su $[a,b]$ $=f(\overline{X})=M$

Sia $\overline{x}=\lim\limits_{k\rightarrow+\infty}x_{n_k}\in[a,b]$

Resta il caso in cui $M=+\infty$, $\Rightarrow f$ non è limitata superiormente
(speriamo di giungere a contraddizione)
$\forall\ n\ \ \exists\ x_n\in[a,b]:f(x_n)>n$
$\Rightarrow\lim\limits_{n\rightarrow+\infty}f(x_n)=+\infty$
$(x_n)\subseteq[a,b]$ limitata $\overset{\text{BW}}{\Rightarrow}(X_{n_k})$ sottosuccessione convergente a $\overline{X}\in[a,b]$

Scopro che $\lim\limits_{K\rightarrow+\infty}f(x_{n_k})=f(\overline{X})\in\mathbb{R}$    $\ne\lim\limits_{n\rightarrow+\infty}f(x_n)=+\infty$
Contraddice teorema di sostituzione

In maniera analoga si verifica che $\text{inf}\{f(x):x\in[a,b]\}=\text{min}=m$
Siccome sappiamo già che l'immagine di un intervallo tramite una funzione continua è un intervallo, deduciamo che $f([a,b])=[m,M]$

### Prop
$f$ funzione continua su intervallo $I$. Allora $f$ è iniettiva su $I$ se e solo se $f$ è strettamente monotona su $I$

#### Controesempio
$I=I1\cup I2$ è unione disgiunta di intervalli


### Prop
Sia $f$ una funzione continua e invertibile su un intervallo.
Allora l'inversa $f^{-1}$ è una funzione continua sull'intervallo $J=f(I)$
