Generalizziamo a
1) funzioni illimitate
2) intervalli illimitati

# Intervalli illimitati
Data $f:[a,\infty)\to\mathbb R$ limitata e integrabile (in senso definito) su $[a,b]\quad\forall\ b>a$ definiamo l'**integrale improprio** di $f$ su $[a,\infty]$ come $\int_a^\infty f:=\lim\limits_{b\to\infty}\int_a^b f$. Se esiste diciamo che è **integrale** (impropriamente) su $[a,\infty)$ se tale limite esiste finito. Diciamo che l'integrale è **divergente** se tale limite è $\pm\infty$. Diciamo che l'integrale è **oscillante** se il limite non esiste.
## Nota
Se $f(x)\ge0$ per $x>x_0$, allora l'integrale può essere convergente o divergente a $+\infty$


Nel caso $f:[-\infty,b)$, poniamo $\int_{-\infty}^b f:=\lim\limits_{a\to\infty}\int_a^b f$
Nel caso $f:\mathbb R\overset{(-\infty,\infty)}\longrightarrow\mathbb R$, poniamo $\int_{-\infty}^\infty f:=\int_{-\infty}^0 f+\int_{0}^\infty f$ (devono entrambi dare un numero finito, uno finito e uno $\infty$, oppure entrambi $\infty$ con lo stesso segno)

L'integrale $\int_{-\infty}^\infty xdx$ non converge anche se $\lim_{T\to\infty}\int_{-T}^Tf(x)dx$ esiste (ed è $=0$)

## Esempi
Vediamo se $f(x)=\frac1{1+x^2}$ è integrabile su $[0,\infty)$
$\int_0^{\infty}\frac1{1+x^2}dx=\lim\limits_{b\to\infty}\int_0^b\frac1{1+x^2}dx=\lim\limits_{b\to\infty}\left[\arctan x\right]_a^b$

$\lim\limits_{b\to\infty}(\arctan b-\arctan 0)=\frac\pi2$

Quindi $\frac1{1+x^2}$ è integrabile su $[0,\infty)]$ e $\int_0^\infty\frac1{1+x^2}dx=\frac\pi2$



Vediamo se $f(x)=1$ è integrabile su $[0,\infty)$
$\int_0^{\infty}dx=\lim\limits_{b\to\infty}\int_0^bdx=\lim\limits_{b\to\infty}b=+\infty$

Quindi $1$ è integrabile su $[0,\infty)]$ e $\int_0^\infty dx$ diverge a $+\infty$



Vediamo se $f(x)=\sin x$ è integrabile su $[0,\infty)$
$\int_0^\infty\sin xdx=\lim_{b\to\infty}\int_0^b\sin xdx=\lim_{b\to\infty}\left[-\cos x\right]_0^b=\lim\limits_{b\to\infty}(-\cos b+1)$ che non esiste $\Rightarrow\ \sin x$ non è integrabile su $[0,\infty)$ e il suo integrale è oscillante



Vediamo quando $f(x)=\frac1{x^a} x$ è integrabile su $[0,\infty)$, con $\alpha\in\mathbb R$

$\int_1^\infty\frac1{x^\alpha}dx=\lim\limits_{b\to\infty}\int_1^b\frac1{x^\alpha}dx=\lim_{b\to\infty}\left[\frac{x^{1-\alpha}}{1-\alpha}\right]_a^b=\lim_{b\to\infty}\left(\frac{b^{1-\alpha}}{1-\alpha}-\frac1{1-\alpha}\right)=\begin{cases}\frac{-1}{1-\alpha}&\text{se }\alpha>1\\+\alpha&\text{se }\alpha<1\end{cases}$
Mentre se $\alpha=1$:
$\int_1^\infty\frac1{x}dx=\lim\limits_{b\to\infty}\int_1^b\frac1{x}dx=\lim_{b\to\infty}\left[\ln b-0\right]_a^b=+\infty$
Quindi $\frac1{x^\alpha}$ è integrabile in $[1,\infty)\iff\alpha>1$ (nel resto dei casi, ossia $\alpha\le1$, diverge a $+\infty$)



$\frac1{x(\ln x)^\alpha}$ su $[e,\infty)$

$\int_e^\infty\frac1{x(\ln x)^\alpha}dx=\lim\limits_{b\to\infty}\int_e^b\frac1{x(\ln x)^\alpha}dx$
$\ln x=y\iff x=e^y$
$\frac{dx}x=dy$

$\lim\limits_{b\to\infty}\int_1^{\ln b}\frac 1{y^a}dy=\int_e^{\int}\frac 1{y^a}dy$ e quindi converge se $\alpha>1$ e diverge se $\alpha\le1$
Quindi $\frac1{x(\ln x)^\alpha}$ è integrabile su $[e,\infty)\iff\alpha>1$

In generale $\displaystyle\frac1{x\ln x\cdot\ln(\ln x)\cdot\ln(\ln(\ln x)))\cdot\ln(\ln(\ln(\ln x))))^\alpha}$ è integrabile su $[\overbrace{x}^\text{grande},\infty)\iff a>1$

# Criteri di convergenza

## Criterio del confronto
Siano $f,g:[a,\infty)\to\mathbb R$ limitate e integrabili su $[a,\infty)\quad\forall\ b>a$
Supponiamo $0\le f(x)\le g(x)\quad\forall x\ge x_0$ per qualche $x_0>a$
Allora se $\int_a^\infty g$ converge, allora $\int_a^\infty f$ converge

Se $\int_a^\infty f$ diverge a $+\infty$, allora $\int_a^\infty g$ diverge a $+\infty$

### Esempio
$\frac1{x^\alpha(\ln x)^\beta}$ su $[e,\infty)$ con $\overbrace{a\ne1}^\text{già visto}$

Se $a<1$, allora $\frac1{x^\alpha(\ln x)^\beta}=\frac1x\frac{x^{1-\alpha}}{(\ln x)^\beta}$ quindi in particolare $>1$ per $x\ge x_0$ per un qualche $x_0\Rightarrow\frac1{x^\alpha(\ln x)^\beta}\ge\frac1x$ per$x\ge x_0$ e quindi dato che $\int_e^\infty\frac1xdx$ diverge allora, per confronto, anche $\int_e^\infty\frac1{x^\alpha(\ln x)^\beta}dx$ diverge

Se $\alpha>1\quad \displaystyle\frac1{x^\alpha(\ln x)^\beta}=\frac1{x^{\frac{\alpha-1}2}}\underbrace{\frac{x^{\overbrace{\frac12-\frac\alpha2}^{<0}}}{(\ln x)^\beta}}_{=0\rightarrow\le1\text{ per } x\ge x_0\ \ \exists\ x_0}$
$\frac1{x^{1+\frac{(\alpha)}2}}$ e dato che $\int_e^\infty\frac1{x^{1+\frac{(\alpha)}2}}dx$ converge (perché $1+\frac{a-1}2>1$), allora per confronto anche $\int_e^\infty\frac1{x^\alpha(\ln x)^\beta}dx$ converge

## Criterio del confronto asintotico
Sia $f:[a,\infty)\to\mathbb R$ limitata e integrabile su $[a,\infty)\quad\forall\ b>a$
Per $x\ge x_0$, per qualche $x_0$, si supponga che $f$ abbia ordine d'infinitesimo $\alpha$ rispetto al campione $\frac1x$ per $x\to\infty$
Allora $\int_a^\infty f$ converge se $\alpha>1$ e diverge a $+\infty$ se $\alpha\le 1$

# Criterio di convergenza assoluta
Sia $f:[a,\infty)\to\mathbb R$ limitata e integrabile su $[a,\infty)\quad\forall\ b>a$
Si supponga che $\int_a^\infty|f|$ converga. Allora anche $\int_a^\infty f$ converge e vale $|\int_a^\infty f|\le\int_a^\infty |f|$

### Esempio
$\frac{\cos x}{x^2}$ su $[1,\infty)$
Abbiamo che $\frac{|\cos x|}{x^2}\le\frac1{x^2}\quad\forall\ x>0$ e $\int_1^\infty\frac{\cos x}{x^2}dx$ converge $\Rightarrow$ per confronto $\int_1^\infty\frac{|\cos x|}{x^2}dx$ converge $\Rightarrow$ Per convergenza assoluta anche $\int_1^\infty\frac{\cos x}{x^2}dx$ converge



# Integrale improprio per funzioni illimitate su intervalli finiti
Sia $f:[a,\infty)\to\mathbb R$ limitata e integrabile (in senso definito) su $[a,c]\quad\forall\ c\in(a,b)$

L'**integrale improprio** di $f$ su $[a,b)$ è $\int_a^b f=\lim_{c\to b}\int_a^cf$

L'integrale è convergente, divergente a $\pm\infty$ oscillante a seconda che il limite esista finito, sia $\pm\infty$, o non esista

## Nota
Se $f$ è integrabile in senso definito su $[a,b]$ allora lo è anche in senso indefinito e i due integrali coincidono
I criteri di confronto e di convergenza assoluta valgono anche in questo caso (per confronto serve $0\le f(x)\le g(x)\quad\forall\ x\in(x_0,b\ \ \exists x_0$)
Per il confronto asintotico in questo caso c'è convergenza $\iff f(x)$ ha ordine $\alpha<1$ rispetto al campione $\frac1{b+x}$
Questo perché, come prima si vede che $\int_0^1\underbrace{\frac1{x^\alpha}dx}_{\text{problema in }0}\qquad \int_a^b\underbrace{\frac{1}{(x-\alpha)^\alpha}dx}_{\text{problema in }x=\alpha}\qquad \int_a^b\underbrace{\frac1{(b-x)^\alpha}dx}_{\text{problema in }b=x}$ convergono $\iff \alpha<1$

### Esempio
$\displaystyle\int_0^{\frac\pi2}\frac{\sqrt x}{\sin x}dx$
Per $x\to 0$, $\sin x\sim x\Rightarrow\frac{\sqrt x}{\sin x}\sim\underset{x\to0^+}{\frac1{\sqrt x}}$
Quindi l'ordine in $0$ è $\frac12$ rispetto a $\frac1x$ e quindi per confronto asintotico l'integrale converge



$\int_0^1(\ln x) dx$ (problema $x=0$)
$|\ln x|=\underbrace{(|\ln x|\sqrt x)}_{\text{tende a }0\le 1\text{ per }x\in(0,x_0)\exists\ x_0}\frac1{\sqrt x}$
$\le\frac1{\sqrt x}\quad x\in(0,x_0)$
Dato che $\int_0^1\frac1{\sqrt x}dx$ converge, allora per confronto converge anche $\int_0^1(\ln x)dx$



$\int_{-\infty}^{+\infty}f$ con $\displaystyle f(x)=\frac{\sin x}{|x|^\frac32}$
4 problemi: $-\infty, 0^-, 0^+, +\infty$
$\displaystyle\int_{-\infty}^{+\infty}f=\int_{-\infty}^{-1}f+\int_{-1}^{0}f+\int_{0}^{1}f+\int_{1}^{+\infty}f$ (converge)



La funzione integrale $F_{x_0}(x)\int_{x_0}^xf(y)dx$ è definita con dominio gli $x$ tali che $f$ è integrabile in senso improprio tra $x_0$ e $x$
**Esempio**

$f(x)=\begin{cases}0&x\le 0\\1&x>0\end{cases}$

Non è continua in $0$, ma è integrabile (in senso definito) su $[a,b]\quad \forall a<b$
$F_0(x)=\int_0^xf(y)dy==\begin{cases}0&x\le 0\\x&x\ge0\end{cases}$
Nei punti in cui $f$ è continua, per il teorema fondamentale del calcolo, $F_0$ è derivabile e $F_0'=f$, mentre nel punto dove $f$ ha una discontinuità a salto, $F_0$ non è derivabile



$f(x)=\frac1{\sqrt{|x-1|})}$ (problema in $1$, ma è integrabile in 1 \[ha ordine $\frac12$\])
$F_0(x)=\int_0^1f$ ha dominio $\mathbb R$

$F_0'(x)=f(x)$ se $x\ne1$, mentre in $1\ F_0$ ha un punto a tangente verticale.
Inoltre $\lim\limits_{x\to\infty}F_0(x)=\int_0^\infty f=+\infty$ ($f$ non è integrabile in $\infty$)
$\lim\limits_{x\to-\infty}F(x)=-\infty$
$F_0(0)=0$ per definizione

$F_0'>0$ se $x\ne 1\Rightarrow F_0$ crescente