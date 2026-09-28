### Definizione (Funzione)
Data una funzione $f:X\rightarrow Y$ e sottoinsiemi $A\subseteq X, B\subseteq Y$, diremo immagine di $A$ tramite $f$ l'insieme $f(A):=\{f(x):x\in A\}\subseteq Y$
Controimmagine di $B$ tramite $f$
	$f^{-1}(B):=\{x\in X:f(x)\in B\}\subseteq X$
Esempio: $B\{Y\}\ \ f^{-1}(fy)=f^-1(Y)$

Insieme di coppie ordinate (x,y)

### Osservazione
(facile)
$A\subseteq f^{-1}(f(A))$
$f(f^{-1}(B))=B\cap\text{ in }f$

#### Esempio
$f:\mathbb{R}\rightarrow\mathbb{R}, x\mapsto x^4$
$\mathcal{D}$ / $\mathcal{I}$
$f((0,1)) = (0,1)$
$f((0,1]) = (0,1]$
$f([0,1)) = [0,1)$
$f([0,1]) = [0,1]$

$\mathcal{I}$ / $\mathcal{D}$
$f^{-1}((0,1)) = (-1,0)\cup(0,1)$
$f^{-1}((0,1]) = [-1,0)\cup(0,1]$
$f^{-1}([0,1)) = (-1,1)$
$f^{-1}([0,1]) = [-1,1]$
$f^{-1}((-\infty,0)) = \varnothing$

### Definizioni (in, sur, bi)
Una funzione $f:X\rightarrow Y$ è detta iniettiva se ogni elemento $y\in Y$ ha al più una controimmagine ovvero $\forall x_1, x_2\in X, f(x_1)=f(x_2)\Rightarrow x_1=x_2$
Una funzione $f:X\rightarrow Y$ è detta suriettiva se ogni elemento del codominio ha almeno una controimmagine ovvero $\forall y\in Y\ \exists\ x\in X:f(x)=y$
Una funzione $f:X\rightarrow Y$ è detta biettiva se è sia iniettiva che suriettiva

### Definizione (inversa)
Data una funzione $f:X\rightarrow Y$ iniettiva, definiamo la sua immagine come quella funzione $f^{-1}$ !-! che ad ogni elemento $y\in\text{ im}(f)$ associa l'unico $x\in X$ t.c. $f(x)=y$
Se la funzione non è iniettiva non ha l'inverso

### Osservazione
(facile)
$y\in \text{ Im } f$    $f(f^{-1}(y))=y$
$x\in X$    $f^{-1}*f(x))=x

### Definizione (restrizione)
Data $f:X\rightarrow Y$ e $A\subseteq X$, definisco la *restrizione* di $f$ ad $A$ ($f\restriction_A:A\rightarrow Y$ che ad ogni $x\in A$ associa $f\restriction_A:=f(x)$)

### Esempi
$f:\mathbb{R}\rightarrow\mathbb{R}, x\mapsto x^2$
non è iniettiva
non è suriettiva

$f\restriction_{[0,+\infty)}$    $f:[0,+\infty)\rightarrow\mathbb{R}, x\mapsto x^2$
è iniettiva
non è suriettiva

$g:[0,+\infty)\rightarrow[0,+\infty), x\mapsto x^2$
è iniettiva
è suriettiva

$f\restriction_{(-\infty,0]}:(-\infty,0]\rightarrow\mathbb{R}, x\mapsto x^2$
è iniettiva
non è suriettiva

### Definizione (monotòna)
$f:\text{dom}(f)\le\mathbb{R}\rightarrow\mathbb{R}$ è detta:
- monotona crescente (non decrescente): $\forall x_1,x_2\in\text{dom}(f), x_1<x_2\Rightarrow f(x_1)\le f(x_2)$
- monotona strettamente crescente: $\forall x_1,x_2\in\text{dom}(f), x_1<x_2\Rightarrow f(x_1)<f(x_2)$
Analogamente, nel caso decrescente si ha $f(x_1)\ge f(x_2)$ / $f(x_1)>f(x_2)$

### Osservazione
Se $f$ è monotona in senso **stretto**, allora $f$ è iniettiva
N.B.: **non** è $\iff$, esistono funzioni iniettive non monotone
#### Esempio
$f:\mathbb{R}\rightarrow\mathbb{R}, x\mapsto \begin{cases} 0\text{, se }x=0 \\ \frac{1}{x}\text{, se }x\ne0\end{cases}$

### Osservazione
$f, g$ strettamente crescenti $\Rightarrow f+g$ str crescente
$f$ strettamente crescente, $a < 0,\Rightarrow af$ str decrescente

#### Esempio
$x^5+x^3+x$ str crescente (tutte le funzioni sono str crescenti)

### Definizioni (composizione)
Date $f:X\rightarrow Y$ e $g:Y\rightarrow Z$ definisco la composizione $g\circ f:X\rightarrow Z, x\mapsto g(f(x))$
Nel caso in cui:
$f:\text{dom}(f)\subseteq X\rightarrow Y$
$g:\text{dom}(g)\subseteq Y\rightarrow Z$
$g\circ f:\text{dom}(g, f)\subseteq X\rightarrow Z$

$\text{dom}(f\circ g)=f^{-1}(dom(g))=x\in X : x\in\text{dom}(f); f(x)\in\text{dom}(g)$

#### Esempio
$f:[0,+\infty)\subseteq\mathbb{R}\rightarrow\mathbb{R}, x\mapsto\sqrt[4]{x}$
$g:\mathbb{R}\rightarrow\mathbb{R}, x\mapsto x^2$
$g\circ f:[0, +\infty)\subseteq\mathbb{R}\rightarrow\mathbb{R}, x\mapsto(\sqrt[4]{x})^2=\sqrt{x}$
$f\circ g:\mathbb{R}\rightarrow\mathbb{R},x\mapsto\sqrt[4]{x^2}=\sqrt{|x|}$

## Esempi di funzioni elementari
### Elevamento a potenza $(-)^\alpha$
- Esponente $\alpha=0$
	Per convenzione elevare alla 0 coincide con la funzione $\mathbb{R}\rightarrow\mathbb{R},x\mapsto1$
- Esponente $\alpha\in\mathbb{N}_+\ (\alpha=1,2,3,\ldots)$
	$(-)^n:\mathbb{R}\rightarrow\mathbb{R},x\mapsto x\times\ldots\times x \leftarrow n$ volte
- Esponente $\alpha = \frac{1}{n}, n\in\mathbb{R}_+$
	$(-)^n=\sqrt[n]{-}$
- Esponente $\alpha=\frac{n}{m}, m,n\in\mathbb{N}_+$
	$(-)^{\frac{m}{n}}:=\sqrt[n]{(-)}\circ (-)^m$
- Esponente $\alpha>0$ irrazionale
	$(-)^\alpha:[0,+\infty)\rightarrow\mathbb{R}$
	$X\mapsto\begin{cases}\text{inf}\{x^{\frac{m}{n}}\cdot m, n\in\mathbb{N}_+\text{ senza fattori comuni}\},x\in[0,1) \\ \text{sup}\{\backslash\backslash\},x\in[1,+\infty)\end{cases}$

```functionplot
---
title: Grafici di (-)^α > 0
xLabel: x
yLabel: y
bounds: [0,3,-1,2]
disableZoom: true
grid: true
---
f(x) = x
g(x) = x^0.25
h(x) = x^4
```
```functionplot
---
title: Grafici di (-)^α < 0
xLabel: x
yLabel: y
bounds: [0,3,-1,2]
disableZoom: true
grid: true
---
f(x) = x^-1
g(x) = x^-4
h(x) = x^-64
```

# Polinomi
- $P:\mathbb{R}\rightarrow\mathbb{R},x\mapsto P(x)=\alpha_0+\alpha_1x^1+\ldots+\alpha_nx^n$
- $\frac{P}{Q}:=P\cdot((-)^{-1}\circ Q)$
	P e Q senza fattori comuni

$x^2-2x-3=0 \rightarrow x^2=2x+3\rightarrow x^2-2x+\frac{2}{2}^2-\frac{2}{2}^2+3=0\rightarrow(x-1)^2-4=0$
$y=\sqrt3\sin x-\cos x\rightarrow y=a\sin x+b\cos x$
$\cos\alpha=\frac a r\ \ \ \ \sin\alpha=\frac b r\ \ \ \ r=\sqrt{a^2+b^2}$
$y=r\sin(x\pm\alpha)$
$A=\sqrt 3\ \ \ \ b=1\ \ \ \ r=\sqrt{3+1}$
$\cos\alpha=\frac{\sqrt3} 2\ \ \ \ \sin\alpha=\frac1 2$
