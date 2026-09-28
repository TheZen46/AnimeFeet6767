$f(x)=\frac{a\ln x}{x}+b$
$A(1,2)$
$\tan A\parallel$ bisettrice 1o e 3o quadrante ($y=x$)

$\begin{cases}f(1)=2\\f'(1)=1\end{cases}$

$\begin{cases}2=\frac{a\ln 1}{1}+b\end{cases}$

$\begin{cases}a+b=2\end{cases}$

$y=a\frac{\ln x}{x}+1$

$y'=a\frac{\frac1x\cdot x-\ln x}{x^2}=a\frac{1-\ln 1}{1}=1$


- $\tan'(x)=\frac{\sin(x)}{\cos(x)}-\frac{\sin(x)\cos'(x)}{(\cos(x))^2}=\frac{\sin(x)}{\cos(x)}-\frac{\sin(x)\sin(x)}{(\cos(x))^2}=\frac 1 {(\cos(x))^2}=1+(\tan(x))^2$
- $\cot'(x)=-1-(\cot(x))^2=\frac{-1}{(\sin(x))^2}$
- $\ln'(x),\ \ x>0$
- $\ln'(x)=\ln'(e^{\ln(x)})=\frac 1 {e^{\ln(x)}}=\frac1x$
- $\arcsin(x)=\frac1{\sqrt{1-x^2}}\ \ \ \ x\in(-1,1)$
- $\arccos(x)=\frac{-1}{\sqrt{1-x^2}}\ \ \ \ x\in(-1,1)$
- $\arctan(x)=\frac1{1+x^2}\ \ \ \ x\in(-1,1)$
- $\text{arccot}(x)=\frac{-1}{1+x^2}$

## Definizione (derivata destra/sinistra)
Sia $f$ una funzione definita in un interno destro di $x_0\in\text{dom}(f)$
Diremo che $f$ è **derivabile da destra** se esiste il limite destro $f'_+(x_0):=\lim\limits_{x\rightarrow {x_0}^+}\frac{f(x)-f(x_0)}{x-x_0}$

Sia $f$ una funzione definita in un interno sinistro di $x_0\in\text{dom}(f)$
Diremo che $f$ è **derivabile da sinistra** se esiste il limite sinistro $f'_-(x_0):=\lim\limits_{x\rightarrow {x_0}^-}\frac{f(x)-f(x_0)}{x-x_0}$

### Esempio
- $f:\mathbb R\rightarrow\mathbb R,\ x\mapsto|x|$
$f'_+(0)=\lim\limits_{x\rightarrow0^+}\frac{f(x)-f(0)}{x-0}=\lim\limits_{x\rightarrow0^+}\frac{\overbrace{|x|}^{=x}}{x}=1$
$f'_-(0)=\lim\limits_{x\rightarrow0^-}\frac{f(x)-f(0)}{x-0}=\lim\limits_{x\rightarrow0^+}\frac{\overbrace{|x|}^{=-x}}{x}=-1$

#### Punto angoloso
- $f:\mathbb R\rightarrow\mathbb R,\ x\mapsto\begin{cases}\sqrt x,\  x>0\\x,\ x\le0\end{cases}$
$\lim\limits_{x\rightarrow0^+}\frac{\sqrt x-0}{x-0}=\lim\limits_{x\rightarrow0^+}x^{-\frac12}=+\infty$
$\lim\limits_{x\rightarrow0^-}\frac{x-0}{x-0}=1$

#### Cuspide
- $f:\mathbb R\rightarrow\mathbb R,\ x\mapsto\sqrt{|x|}$
$\lim\limits_{x\rightarrow0^+}\frac{\sqrt{|x|}-0}{x-0}=\lim\limits_{x\rightarrow0^+}x^{-\frac12}=+\infty$
$\lim\limits_{x\rightarrow0^-}\frac{\sqrt{|x|}-0}{x-0}=\lim\limits_{x\rightarrow0^-}\frac{\sqrt{-x}}x=-\lim\limits_{x\rightarrow0^-}\frac{\sqrt{-x}}{-x}=-\lim\limits_{x\rightarrow0^-}(-x)^{-\frac12}=\lim\limits_{y\rightarrow0^-}y^{-\frac12}=-\infty$

#### Punto di flesso a tangente verticale
- $f:\mathbb R\rightarrow\mathbb R,\ x\mapsto\sqrt[3]{x}$
$\lim\limits_{x\rightarrow0^+}\frac{\sqrt[3]x-0}{x-0}=\lim\limits_{x\rightarrow0^+}x^{-\frac23}=\lim\limits_{x\rightarrow0^+}\frac1{\sqrt[3]{x^2}}=+\infty$
$\lim\limits_{x\rightarrow0^i}\frac{\sqrt[3]x-0}{x-0}=\lim\limits_{x\rightarrow0^+}\frac1{\sqrt[3]{x^2}}=+\infty$

## Proposizione
Sia $f$ definita su un intorno di $x_0$
Allora $f$ è derivabile in $x_0$ se e solo se $f$ è derivabile in $x_0$ sia da destra che da sinistra e $f'_+(x_0)=f'_-(x_0)$

## Teorema (limite della derivata)
Sia $f$ continua in un intorno $I$ di $x_0$ e derivabile in $I\backslash\{x_0\}$
(i) Se esiste finito $\lim\limits_{x\rightarrow x_0}f'(x)$, allora $f$ è derivabile in $x_0$ e $f'(x_0)=\lim\limits_{x\rightarrow x_0}f'(x)$
(ii) Se almeno uno tra $\lim\limits_{x\rightarrow x_0^+}f'(x)$ e $\lim\limits_{x\rightarrow x_0^-}f'(x)$ esiste, ma è $\pm\infty$, oppure entrambi esistono finiti, ma diversi, $f$ **non** è derivabile in $x_0$

## Dimostrazione (conseguenza del teorema di de l'Hôpital)
$\lim\limits_{x\rightarrow {x_0}^\pm}\frac{f(x)-f(x_0)}{x-x_0}\overset H =\lim\limits_{x\rightarrow {x_0}^\pm}\frac{f'(x)}{1}$

(i) Esistono finiti coincidenti $\Rightarrow\ f$ è derivabile in $x_0$ e $f'(x_0)=\lim\limits_{x\rightarrow x_0}f'(x)$
(ii) $f$ non è derivabile

### Esempio
Cercare valori di $\alpha,\beta\in\mathbb R$ per cui la funzione $f:\mathbb R\rightarrow\mathbb R,x\mapsto\begin{cases}\alpha(e^x-1)+\beta\cos(x),\ x\ge0\\1+x,\ x<0\end{cases}$  è derivabile in 0.

Continua in 0?
$\lim\limits_{x\rightarrow0^-}f(x)=\lim\limits_{x\rightarrow0^-}(1+x)=1$
$\lim\limits_{x\rightarrow0^+}f(x)=\lim\limits_{x\rightarrow0^+}(\alpha(e^x-1)+\beta\cos(x))=\beta$

$f$ è continua in 0 se e sono le $\beta=1$
$f$ è derivabile in 0?

$f'(x)=\begin{cases}\alpha e^x-\sin(x),\ x>0\\1,\ x<0\end{cases}$
$\lim\limits_{x\rightarrow0^-}f'(x)=0$
$\lim\limits_{x\rightarrow0^-}f'(x)=\lim\limits_{x\rightarrow0^+}(\alpha e^x-\sin\small(x)\normalsize)=\alpha$

$f$ è derivabile in 0 se e solo se $\alpha=1$

## Proposizione
Sia $f$ continua su $[a,b]$ e derivabile su $(a,b)$
Se $f'(x)=0\ \ \forall\ x\in(a,b)$ allora $f$ è costante su $[a,b]$

### Dimostrazione
Fisso $x\in[a,b)$ e applico il teorema di Lagrange a $f$ su $[x,b]$: trovo $\overline x\in(x,b)$ tale che $0\overset{\text{IP}}=f'(\overline x)=\frac{f(b)-f(x)}{\underbrace{b-x}_{>0}}\Rightarrow f(b)-f(x)=0\Rightarrow f(x)=f(b)$
Abbiamo verificato che $\forall\ x\in[a,b)\ \ f(x)=f(b)$ ovvero $f$ è costante su $[a,b]$


## Corollario
**Massimo**
$f$ continua su intervallo $I$ e derivabile nei punti interni di $I$. Sia $x_0$ un punto interno di $I$ che è critico per $f$, ovvero $f'(x_0)=0$.
Se sono verificate entrambe le condizioni seguenti:
- (i) $f'(x)\ge 0$ in un intorno sinistro di $x_0$, $x_0$ escluso
- (ii) $f''(x)\le 0$ in un intorno destro di $x_0$, $x_0$ escluso
Allora $x_0$ è un punto di massimo relativo

**Minimo**
$f$ continua su intervallo $I$ e derivabile nei punti interni di $I$. Sia $x_0$ un punto interno di $I$ che è critico per $f$, ovvero $f'(x_0)=0$.
Se sono verificate entrambe le condizioni seguenti:
- (i) $f'(x)\le 0$ in un intorno sinistro di $x_0$, $x_0$ escluso
- (ii) $f''(x)\ge 0$ in un intorno destro di $x_0$, $x_0$ escluso
Allora $x_0$ è un punto di minimo relativo


Inoltre, se le diseguaglianze sono strette, allora $x_0$ è punto di estremo locale stretto.

### Esempio
Ricerca degli estremi di $f:\mathbb R\rightarrow \mathbb R,\ x\mapsto x\arctan(x)$

Per teorema di Fermat, gli estremi di $f$ sono necessariamente punti critici.
Pertanto cerco tutte le soluzioni $x\in\mathbb R$ dell'equazione $f'(x)=0$ e successivamente mi chiedo quali di queste soluzioni sono punti di estremo.

$f'(x)=1\cdot \arctan(x)+x\cdot\frac1{1+x^2}=\arctan(x)\frac x{\underbrace{1+x^2}_{>0}}$
$f'(0)=0\Rightarrow 0$ è punto critico
$x>q\Rightarrow f'(x)>0\Rightarrow$ **no** punti critici per $x>0$
$x<q\Rightarrow f'(x)<0\Rightarrow$ **no** punti critici per $x<0$

Allora $0$ è l'unico punto critico

```functionplot
---
title: 
xLabel: x
yLabel: x
bounds: [-3,3,-2,2]
disableZoom: false
grid: true
---
f(x)=atan(x)*(x/(1+x^2))
```


# Derivate di ordine superiore e convessità
$f$ derivabile in un intorno $I$ di $x_0$
Ha senso considerare $f':I\rightarrow\mathbb R,\ x\mapsto f'(x)$

## Definizione (derivata seconda)
Se f' è derivabile in $x_0$, diremo che $f$ è **derivabile 2 volte** in $x_0$ e chiameremo **derivata seconda** di $f$ in $x_0$ il numero $f''(x_0)=\lim\limits_{x\rightarrow x_0}\frac{f['(x)-f'(x_0)}{x-x_0}$
Iterando questo procedimento definiamo le derivate successive $f'''=f^{(3)},f^{(4)},f^{(5)},\ldots$

### Esempio
$(x^n)^{(k)}=((x^n)')^{(k-1)}=(nx^{n-1})^{(k-1)}=((nx^{n-1})')^{(k-2)}=(n(n-1)x^{n-2})^{(k-2)}=\ldots=n(n+1)(n+2)\ldots(n-k+1)x^{n-k}$

$(x^n)^(k)=\left\{\begin{array}{l}n(n-1)\ldots(n-k+1)x^{n-k}& \text{se }k\le n\\0&\text{se }k>n\end{array}\right.$

## Definizione
(Classe $C^k,C^\infty$)  $k\in \mathbb N$
Una funzione si dice di classe $C^k$ su un intervallo $I$ se è derivabile $k$ volte su $I$ e $f^{(k)}:I\rightarrow\mathbb R$ è continua
Si dice di classe $C^\infty$ se è di classe $C^k\ \ \ \ \forall\ k\in\mathbb N$

## Definizione
**Convessa**
$f$ derivabile su intervallo $I$.
Diciamo che $f$ è **convessa** su $I$ se $\underset{x_1\ne x_2}{x_1,x_2}\in I\Rightarrow f(x_2)\ge f(x_1)+f'(x_1)(x_2-x_1)$
Se le disuguaglianze sono strette, $f$ si dice **strettamente convessa**

**Concava**
$f$ derivabile su intervallo $I$.
Diciamo che $f$ è **convessa** su $I$ se $\underset{x_1\ne x_2}{x_1,x_2}\in I\Rightarrow f(x_2)\le f(x_1)+f'(x_1)(x_2-x_1)$
Se le disuguaglianze sono strette, $f$ si dice **strettamente concava**

### Osservazione (Interpretazione geometrica della convessità)
\[Grafico\]
Significa che il tratto del grafico di $f$ relativo all'intervallo $I$ giace al di sopra di ogni retta tangente

#### Esempio
Verifichiamo che $x^2$ è strettamente convessa su tutto $\mathbb R$
$\underset{x_1\ne x_2}{x_1,x_2}\in\mathbb R\overset?\Rightarrow \underbrace{f(x_2)}_{{x_2}^2}>\underbrace{f(x_1)}_{{x_1}^2}+\underbrace{f'(x_1)}_{2x_1}(x_2-x_1)$
Da verificare: ${x_2}^2>{x_1}^2+2x_1(x_2-x_1)$

${x_2}^2>{x_1}^2+2x_1(x_2-x_1)\overset?>0$
${x_2}^2>{x_1}-2x_1x_2=(x_1-x_2)^2$
## Definizione (flesso)
Sia $f$ derivabile in $x_0$
Si dice che $x_0$ è **punto di flesso** per $f$ se esiste un intorno $I$ di $x_0$ in cui è verificata una delle condizioni seguenti:
($\uparrow$) $\forall\ x\in I$ vale $\begin{cases}f(x)\le f(x_0)+f'(x_0)(x-x_0)&x<x_0\\f(x)\ge f(x_0)+f'(x_0)(x-x_0)&x>x_0\end{cases}$

($\downarrow$) $\forall\ x\in I$ vale $\begin{cases}f(x)\ge f(x_0)+f'(x_0)(x-x_0)&x<x_0\\f(x)\le f(x_0)+f'(x_0)(x-x_0)&x>x_0\end{cases}$


## Teorema
**Convessa**
Sia $f$ derivabile su intervallo $I$
Allora valgono le seguenti affermazioni
- (i) $f$ è convessa si $I\ \iff\ f$ è crescente su $I$
- (ii) Se $f$ è strettamente crescente su $I$, allora $f$ è strettamente convessa su I

Sia $f$ derivabile su intervallo $I$
Allora valgono le seguenti affermazioni
- (i) $f$ è concava si $I\ \iff\ f$ è decrescente su $I$
- (ii) Se $f$ è strettamente decrescente su $I$, allora $f$ è strettamente concava su I
### Osservazione
(ii) **non** è un $\iff$
Ad esempio, $x^4$ è strettamente convessa su $\mathbb R$
Tuttavia $(x^4)''=12x^2$ si annulla in $0$

## Dimostrazione (i)
"$\Rightarrow$"
Suppongo $f$ convessa
$x_1,x_2\in I,x_1\ne x_2\Rightarrow\begin{array}{l}f(x_2)\ge f(x_1)+f'(x_1)(x_2-x_1)\\f(x_1)\ge f(x_2)+f'(x_2)(x_1-x_2)\end{array}$

Sommando membro a membro:
$f(x_2)+f(x_1)\ge f(x_1)+f'(x_1)(x_2-x_1)+f(x_2)+f'(x_2)(x_1-x_2)\Rightarrow(x_2-x_1)(f'(x_1)-f'(x_2))\le 0$
Se $x_2>x_1$, allora $f'(x_1)-f'(x_2)\le 0$
Se $x_2<x_1$, allora $f'(x_1)-f'(x_2)\ge 0$

$\Rightarrow x<y$ allora $f'(x)\le f'(y)\text{ in }I\ \checkmark$



"$\Leftarrow$"
Suppongo $f'$ crescente in $I$
Da seconda formula incremento finito punti $x<y$ in $I$, trovo $\overline x\in(x,y)$ tale che $f(y)=f(x)+f'(\overline x)(y-x)$
Da ipotesi segue che $\underbrace{f'(x)\le f'(\overline x)\le f'(y)}_{(x<\overline x<y)}$
Deduco che $f(y)=f(x)+\underbrace{f'(\overline x)}_{\ge f'(x)}\underbrace{(y-x)}_{>0}\le f(x)+f'(x)(y-x)\ \ \(*)$
$f(y)=f(x)+\underbrace{f'(\overline x)}_{\le f'(x)}\underbrace{(y-x)}_{>0}\le {l}f(x)+f'(x)(y-x)\Rightarrow f(x)\ge f(y)+f'(y)(x-y)\ \ (**)$

Devo dimostrare che
$x_1,x_2\in I,\ x_1\ne x_2\overset \checkmark \Rightarrow f(x_2)\underset{\underset{(ii)}{(>)}}\ge \underset{(*)}{f(x_1)}+\underset{(**)}{f'(x_1)}(x_1-x_1)$

$x_1\ne x_2\Rightarrow$ dice così:
- $x_1<x_2:$ scelgo $x=x_1,y=x_2$ in $(*)$
- $x_1>x_2:$ scelgo $x=x_2,y=x_1$ in $(**)$

## Corollario
**Convessa**
Sia $f$ derivabile 2 volte su un intervallo $I$. Allora:
- (i) $f$ è convessa su $I\ \iff\ f'(x)\ge0\ \ \forall\ x\in I$
- (ii) Se $f''(x)>0\ \ \forall\ x\in I$, allora $f$ è strettamente convessa su $I$

**Concava**
Sia $f$ derivabile 2 volte su un intervallo $I$. Allora:
- (i) $f$ concava su $I\ \iff\ f'(x)\le0\ \ \forall\ x\in I$
- (ii) Se $f''(x)<0\ \ \forall\ x\in I$, allora $f$ è strettamente concava su $I$
### Dimostrazione
Combino il teorema precendente e caratterizzazione della monotonia di $f'$ mediante segno $f''$,

### Osservazione
(ii) **non** è $\iff$
$f(x)=x^4$ è strettamente convessa, tuttavia $f''(x)=12x^2$ si annulla in $x=0$

#### Esempio
$f:\mathbb R\rightarrow\mathbb R,\ x\mapsto x\arctan(x)$
Studio convessità
$f'(x)=\arctan(x)+\frac x{1+x^2}$
$f''(x)=\frac 1 {1+x^2}+\frac 1 {1+x^2}+x(-\frac{2x}{(1+x^2)^2})=\frac{2(1+x^2)-2x^2}{(1+x^2)^2}=\frac{2}{(1+x^2)^2}>0\leftarrow$ è strettamente convessa

### Proposizione
$f$ derivabile 2 volte in un intorno di $x_0$
- (i) Se $x_0$ è punto di flesso per $f$, allora $f''(x_0)=0$
- (ii) Se $f''(x_0)=0$ e vale una delle condizioni seguenti, allora $x_0$ è punto di flesso
	- $(\uparrow)$ esistono intorno sinistro di $x_0$ in cui $f''\le 0$ e intorno destro di $x_0$ in cui $f''\ge 0$    (flesso ascendente)
	- $(\downarrow)$ esistono intorno sinistro di $x_0$ in cui $f''\ge 0$ e intorno destro di $x_0$ in cui $f''\le0$    (flesso discendente)

# Studio di funzione
- dominio, simmetrie, periodicità, punti di discontinuità o non-derivabilità
- andamento al limite agli estremi del dominio, andamento asintotico
- punti critici, intervalli di monotonia, punti di estremo locali o globali
- zeri della derivata seconda, intervalli di convessità

# Teorema di de l'Hôpital
Siano $f,g$ definite in un interno di $c (=x_0,\pm\infty,x_0^\pm)$, eventualmente c escluso
Si supponga che i limiti $\lim\limits_{x\rightarrow c}f(x)=\lim\limits_{x\rightarrow c}g(x)=0,\pm\infty$ siano entrambi nulli o entrambi infinity

Se $f$ e $g$ sono derivabili in un intorno di $c$, eventualmente $c$ escluso, e in questo intorno $g'\ne0$, e se esiste (finito oppure $\pm\infty$) il limite $\lim\limits_{x\rightarrow c}\frac{f'(x)}{g'(x)}$, allora esiste il limite $\lim\limits_{x\rightarrow c}\frac{f(x)}{g(x)}=\lim\limits_{x\rightarrow c}\frac{f'(x)}{g'(x)}$

## Dimostrazione
Dimostriamo solo il caso $c={x_0}^+$ e $\lim\limits_{x\rightarrow {x_0}^+}f(x)=\lim\limits_{x\rightarrow {x_0}^+}g(x)=0$
$x>x_0$  Applico Cauchy all'intervallo $[x_0,x]$ e alle funzioni $f,g$: trovo $\overline x\in(x_0,x)$ tale che $f'(\overline x)(g(x)-g(x_0))=(f(x)-f(x_0))\underbrace{g'(\overline x)}_{\ne0}\Rightarrow\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(\overline x)}{g'(\overline x)}$
$\lim\limits_{x\rightarrow {x_0}^+}f(x)=\lim\limits_{x\rightarrow {x_0}^+}g(x)=0$
$f(x_0)=0=g(x_0)$

Passo al limite per $x\rightarrow {x_0}^+$
Per confronto, $\overline x\rightarrow {x_0}^+$

$\lim\limits_{x\rightarrow {x_0}^+}\frac{f(x)}{g(x)}=\lim\limits_{x\rightarrow {x_0}^+}\frac{f'(\overline x)}{g'(\overline x)}$   Il secondo esiste per ipotesi

## Esempi
$\lim\limits_{x\rightarrow+\infty}\frac{e^x}{x}\overset H =\lim\limits_{x\rightarrow+\infty}\frac{e^x}1=+\infty$

$\lim\limits_{x\rightarrow+\infty}\frac{\ln(x)}{x}\overset H =\lim\limits_{x\rightarrow+\infty}\frac{\frac1x}{1}=0$