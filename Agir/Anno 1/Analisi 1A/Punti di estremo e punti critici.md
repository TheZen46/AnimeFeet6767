# Definizione
Sia $f$ una funzione e $x_0\in\text{dom}(f)$
Si che che $x_0$ è
- **Punto di massimo/minimo relativo** o **locale** se esiste $\delta>0$ tale che $\begin{array}{c}x\in\text{dom}(f)\\0<|x-x_0|<\delta\end{array}\Rightarrow \underbrace{f(x)\le f(x_0)}_{(<)}/\underbrace{f(x)\ge f(x_0)}_{(>)}$
- **Punto di massimo/minimo assoluto** o **globale** se $x\in\text{dom}(f)\backslash\{x_0\}\Rightarrow\underbrace{f(x)\le f(x_0)}_{(<)}/\underbrace{f(x)\ge f(x_0)}_{(>)}$

Sia $f$ una funzione e $x_0\in\text{dom}(f)$
Diremo che $x_0$ è un **punto critico** di $f$ se valgono entrambe le condizioni:
- $f$ è derivabile in $x_0$
- $f'(x_0)=0$

# Teorema di Fermat
Sia $f$ definita in un intorno di $x_0$ e derivabile in $x_0$
Se $x_0$ è un punto di estremo per $f$, allora $x$ è un punto critico, ovvero $f'(x_0)=0$

## Dimostrazione
Supponiamo che $x_0$ sia punto di massimo locale
$\exists\ \delta >0:\begin{array}{c}x\in\text{dom}(f)\\0<|x-x_0|<\delta\end{array}\Rightarrow f(x)\le f(x_0)$
'Per ipotesi, $f$ è derivabile in $x_0$:
$f'(x_0)=\lim\limits_{x\rightarrow x_0^+}\frac{f(x)-f(x_0)}{\underbrace{x-x_0}_{<0}}\le0$ (da destra)    $\lim\limits_{x\rightarrow x_0^-}\frac{f(x)-f(x_0)}{\underbrace{x-x_0}_{>0}}\ge0$ (da sinistra)

## Esempio
$f:[-1,1]\rightarrow\mathbb R,\ x\mapsto x^2$


# Teorema di Rolle
Sia $f$ continua su $[a,b]$ e derivabile su $(a,b)$
Allora $f(a)=f(b)\Rightarrow\exists\ x\in(a,b):f(x_0)=0$

## Dimostrazione (Weierstrass)
$f([a,b])=[m,M]$
$m=\text{min}\{f(x):x\in[a,b]\}$,  $M=\text{max}\{f(x):x\in[a,b]\}$

Caso 1: $m=M\Rightarrow\text{ f è costante }\Rightarrow f'\equiv 0$

Caso 2: $m<M$
$f(a)=f(b)\Rightarrow\text{ almeno uno tra }m\text{ e }M\text{ è raggiunto in }x_0\in(a,b)$

Abbiamo scoperto che $x_0\in (a,b)$, punto interno al dominio $[a,b]$, è punto di estremo $\overset{\text{Fermat}}\Rightarrow f'(x_0)=0$

# Teorema di Cauchy
$f,g$ continue su $[a,b]$ e derivabili su $(a,b)$
Allora $\exists\ x_0\in(a,b)$ tale che $f'(x_0)\big(\normalsize g(b)-g(a)\big)\normalsize=\big(\normalsize f(b)-f(a)\big)\normalsize g'(x_0)$

## Dimostrazione
$h:[a,b]\rightarrow\mathbb{R}, x\mapsto(f(x)-f(a))(g(b)-g(a))+(f(b)-f(a))(g(b)-g(x))$ è continua su $[a,b]$ e derivabile su $(a,b)$ perché lo sono $f,g$
$h(a)=(f(b)-f(a))(g(b)-g(a))=h(b)$
$\overset{\text{Fermat}}\Longrightarrow \exists x_0\in(a,b):h'(x_0)=0=f'(x_0)(g(b)-g(a))+(f(b)-f(a))(-g'(x_0))$

# Teorema di Lagrange
$f$ continua su $[a,b]$ e derivabile su $(a,b)$
Allora $\exists\ x_0\in(a,b)$ tale che $f'(x_0)=\frac{f(b)-f(a)}{b-a}$

# Osservazione (formule di incremento finito)
Caso 1 (prima formula dell'incremento finito): $f$ derivabile in $x_0$
$f(x_0)=\lim\limits_{x\rightarrow x_0}\frac{f(x)-f(x_0)}{x-x_0}\in\mathbb R\ \ \iff\ \ f(x)-f(x_0)-f'(x_0)(x-x_0)=o(x-x_0),\ x\rightarrow x_0$
$f(x)=f(x_0)+f'(x_0)(x-x_0)+o(x-x_0),\ x\rightarrow x_0$

Caso 2 (seconda formula dell'incremento finito): $f$ continua su $[a,b]$ e derivabile su $(a,b)$
Fisso $a\le x_1\le x_2\le b$
$\underset{[x_1,x_2]}{\overset{\text{Lagrange}}\Longrightarrow}\ \exists\ \overline x\in(x_1,x_2):f'(\overline x)=\frac{f(x_2)-f(x_1)}{x_2-x_1}$ ovvero $f(x_2)=f(x_1)+f'(\overline x)(x_2-x_1)$

# Intervalli di monotonia ed estremi locali

## Teorema
$f$ continua su intervallo $I$ e derivabile nei punti interni di $I$
Allora vale quanto segue:
- (i) $f$ è crescente su $I$ se e solo se $f'(x)\ge 0\ \ \forall\ x\in I$
- (i) $f$ è decrescente su $I$ se e solo se $f'(x)\le 0\ \ \forall\ x\in I$
- (ii) Se $f'(x)>0\ \ \forall\ x\in I$, allora $f$ è strettamente crescente su I
- (ii) Se $f'(x)<0\ \ \forall\ x\in I$, allora $f$ è strettamente decrescente su I
Osservazione (ii) non è $\iff$; eg. $f(x)=x^3$ è strettamente crescente eppure $f'(0)=0$

### Dimostrazione
(i) "$\Rightarrow$"
Suppongo $f$ crescente
Fisso $x$ interno ad $I$ e considero $y\in I\backslash\{x\}$
$\left.\begin{array}{c}x<y\Rightarrow f(x)\le f(y)\\x>y\Rightarrow f(x)\ge f(y)\end{array}\right\}\Rightarrow\frac{f(y)-f(x)}{y-x}\ge0\Rightarrow\lim\limits_{y\rightarrow_x}\frac{f(y)-f(x)}{y-x}\ge0$

(i) "$\Leftarrow$"
Per ipotesi $f'(x)\ge0$ per ogni $x$ intorno ad $I$
Prendo $x_1<x_2$ in $I$
Considero $[x_1,x_2]$
Per ipotesi $f$ è continua su $I$ e derivabile sui punti interni
$\Rightarrow f$ è continua su $[x_1,x_2]$ e derivabili su $(x_1,x_2)$
$\overset{\text{Lagrange}}\Rightarrow \exists\ \overline x\in(x_1,x_2):f'(x)=\frac{f(x_2)-f(x_1)}{\underbrace{x_2-x_1}_{>0}}\Rightarrow f(x_2)-f(x_1)\ge0$