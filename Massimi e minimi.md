# Definizione
## Punto critico
$f:D\subset\mathbb R^n\to\mathbb R$
$D$ aperto
$f\in C^1$
$\hat x\in D$ è un punto critico o stazionario per $f$
$\displaystyle \nabla_{\hat x}f=0\iff \frac{\partial f}{\partial e_1}(\hat x)=0,\frac{\partial f}{\partial e_2}(\hat x)=0,\ldots,\frac{\partial f}{\partial e_n}(\hat x)=0$

## Minimo
$f:D\subset\mathbb R^n\to\mathbb R$
$D$ aperto
$f\in C^1$
$\hat x\in D$ è un punto di minimo locale se $\exists B(\hat x,r)\mskip{12mu} f(x)\ge f(\hat x)\mskip{20mu} x\in B(\hat x,r)$

### Minimo stretto
$\hat x\in D$ è un punto di minimo locale stretto se $\exists B(\hat x,r)\mskip{12mu} f(x)> f(\hat x)\mskip{20mu} x\in B(\hat x,r)\setminus\{\hat x\}$
## Massimo
$f:D\subset\mathbb R^n\to\mathbb R$
$D$ aperto
$f\in C^1$
$\hat x\in D$ è un punto di massimo locale se $\exists B(\hat x,r)\mskip{12mu} f(x)\le f(\hat x)\mskip{20mu} x\in B(\hat x,r)$

### Massimo stretto
$\hat x\in D$ è un punto di massimo locale stretto se $\exists B(\hat x,r)\mskip{12mu} f(x)< f(\hat x)\mskip{20mu} x\in B(\hat x,r)\setminus\{\hat x\}$


# Teorema
$f:D\subset\mathbb R^n\to\mathbb R$
$D$ aperto
$f\in C^1$
Se $\hat x$ è di massimo o minimo locale $\Rightarrow\hat x$ è un punto critico

## Dimostrazione
$\displaystyle \frac{\partial f}{\partial e_1}(\hat x)\overset?=0\mskip{20mu}\text{scegliamo }j=1$

$\displaystyle g(y)\coloneqq f(y,\hat x_2,\hat x_3,\ldots,\hat x_n)$
$y\in I\subset \mathbb R$

$\hat x$ sia di minimo
In $\hat x_1\ \ g$ ammette minimo locale
$y\in(\hat x_1-\alpha,\hat x_1+\alpha)$
$0\le g(y)-g(\hat x_1)$ perché la $f$ ammette minimo locale in $\hat x$ e quindi $g$ ammette minimo locale in $\hat x_1$

$g$ è di classe $C_1$
$\displaystyle 0\le g(y)-g(\hat x_1)=\frac{\partial}{\partial y}g(\xi)(y-\hat x_1)\mskip{20mu}\exists\ \xi\in(y,\hat x_1)$
$y<\xi<x_1$
	$\displaystyle \underbrace{\frac{\partial}{\partial y}g(\xi)}_{\ge0}\underbrace{(y-\hat x_1)}_{\ge0}\ge0$

$y>\xi>x_1$
	$\displaystyle \underbrace{\frac{\partial}{\partial y}g(\xi)}_{\le0}\underbrace{(y-\hat x_1)}_{\le0}\ge0$

$\displaystyle \frac{\partial g}{\partial y}$ è continua
$\displaystyle \frac{\partial g}{\partial y}(\xi)\ge0\Rightarrow\displaystyle \frac{\partial g}{\partial y}(\hat x_1)=0\mskip{36mu}\frac{\partial f}{\partial e_1}(\hat x)=0$

Massimo o minimo locale $\Rightarrow\ \hat x$ punto stazionario
$\hat x\in D\mskip{24mu}\nabla_{\hat x}f=0$
$\cases{\partial_1 f(\hat x_1,\ldots,\hat x_n)=0\\\vdots\\\partial_n f(\hat x_1,\ldots,\hat x_n)=0}$
