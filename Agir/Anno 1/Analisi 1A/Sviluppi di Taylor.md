# Formule di Taylor
## Definizione (polinomio di Taylor)
$n\in\mathbb N$, $f$ derivabile $n$ volte in $x_0$
Si dice polinomio di Taylor di $f$ in $x_0$ all'ordine $n$ il polinomio $Tf_{n,x_0}(x):=\frac1{0!}f(x_0)+\frac1{1!}f'(x_0)(x-x_0)+\dots+\frac1{n!}f^{(n)}(x_0)(x-x^0)^n=\sum\limits_{K=0}^n\frac1{K!}f^{(K)}(x_0)\cdot(x-x_0)^K$
Quando $x_0=0$, si usa anche il nome **polinomio di Maclaurin**
### Osservazione
$Tf_{0,x_0}(x)=f(x_0)$
$Tf_{1,x_0}(x)=f(x_0)+f'(x_0)(x-x_0)$

## Teorema (formula di Taylor con resto di Peano)
Sia $f$ derivabile $n$ volte in $x_0$
Allora vale $f(x)=Tf_{n,x_0}(x)+0((x-x_0)^n)_{x\rightarrow x_0}$

### Dimostrazione
Volgiamo usare il teorema di de l'Hôpital per verificare che $\lim\limits_{x\rightarrow x_0}\frac{f(x)-Tf_{n,x_0}(x)}{(x-x_0)^n}=0$
Per prima cosa confronto le derivate in $x_0$ di $f$ e di $Tf_{n,x_0}$
$Tf^{(0)}_{n,x_0}(x_0)=f(x_0)=f^{(0)}(x_0)$
$Tf^{(1)}_{n,x_0}(x_0)=\Big(f(x_0)+f'(x_0)(x-x_0)+\dots\Big)^{(1)}(x_0)=0+f'(x_0)+0=f^{(1)}(x_0)$
$Tf^{(2)}_{n,x_0}(x_0)=\Big(f(x_0)+f'(x_0)(x-x_0)+\frac12f''(x_0)(x-x_0)^2+\dots\Big)^{(2)}(x_0)=0+0+f''(x_0)+0=f^{(2)}(x_0)$

$Tf^{(n)}_{n,x_0}(x_0)=\Big(\dots+\frac1{n!}f^{(n)}(x_0)(x-x_0)^n\Big)^{(n)}(x_0)=0+\dots+0+\frac1{n!}f^{(n)}(x_0)\cdot n!=f^{(n)}(x_0)$

$\lim\limits_{x\rightarrow x_0}(f-Tf_{n,x_0})^{(K)}(x)=\lim\limits_{x\rightarrow x_0}f^{(K)}(x)-\lim\limits_{x\rightarrow x_0}Tf_{x,x_0}^{(K)}(x)=f^{(K)}(x_0)-Tf^{(K)}_{n,x_0}(x_0)=0$


$\lim\limits_{x\rightarrow x_0}\frac{(f-Tf_{n,x_0})(x)}{(x-x_0)^n}\overset H =\lim\limits_{x\rightarrow x_0}\frac{(f-Tf_{n,x_0})^{(1)}(x)}{n(x-x_0)^{n-1}}\overset H =\lim\limits_{x\rightarrow x_0}\\frac{(f-Tf_{n,x_0})^{(2)}(x)}{n(n-1)(x-x_0)^{n-2}}\overset H=\dots\overset H =\lim\limits_{x\rightarrow x_0}\frac{(f-Tf_{n,x_0})^{(n-1)}(x)}{n(n01)\dots2(x-x_0)^{1}}\overset H =\lim\limits_{x\rightarrow x_0}\frac{f^{(n-1)}(x)-f^{(n-1)}(x_0)0f^{(n)}(x-x_0)}{n!(x-x_0)}=\frac1{n!}(\underbrace{\lim\limits_{x\rightarrow x_0}\frac{f^{(n-1)}(x)-f^{(n-1)}(x_0)}{x-x_0}}_{f^{(n)}(x_0)}-f^{(n)}(x_0)=0$

## Teorema (formula di Taylor con resto di Lagrange)
Sia $f$ derivabile $n$ volte in un intorno $I$ di $x_0$, con derivata $n$-esima $f^{(n)}$ continua su $I$ ($f\in C^n(I)$)
Inoltre, sia $f$ derivabile $n+1$ volte su $I\backslash\{x_0\}.$ Allora, per ogni $x\in I\backslash\{x_0\}$ esiste $\overline x$ compreso tra $x_0$ e $x$ tale che $f(x)=Tf^{(x)}_{n,x_0}+\underbrace{\frac1{(n+1)!}f^{(x+1)}(\overline x)(x-x_0)^{n+1}}_{\text{Resto di Lagrange}}$
### Esempi (sviluppi di Taylor di funzioni notevoli)
$e^x$ all'ordine $n$ in $0=x_0$
$e^x=Te^x_{n,0}(x)+0(x^n)$
$Te^x_{n_0}\sum\limits_{K=0}^n\frac1{K!}(e^x)^Ko(x)^K$
$(e^x)^{(0)}=e^x$
$(e^x)^{(1)}=e^x$
$(e^x)^{(2)}=e^x$
$(e^x)^{(n)}=e^x$
$\sum\limits_{K=0}^n\frac1{K!}x^K=1+x+\frac12x^2+\frac1{3!}x^3+\dots+\frac1{n!}x^n$


$\ln(1+x)$ all'ordine $n$ in $0$
$\ln(1+x)=T\ln(1+x)_{n,0}(x)+0(x^n)$
$\ln(1+x)^{(0)}(0)=0$
$\ln(1+x)^{(1)}(0)=(\frac1{1+x})(0)=1$
$\ln(1+x)^{(2)}(0)=(\frac{-1}{(1+x)^2})(0)=-1$

$T\ln(1+x)_{n,0}(x)=\sum\limits_{K=1}^n\frac{(-1)^{K-1}}Kx^K=x-\frac12x^2+\frac13x^3+\dots+\frac{(-1)^{n-1}}nx^n$
$\ln(1+x)=x-\frac12x^2+\frac13x^3+\dots+\frac{(-1)^{n-1}}nx^n+o\underset{x\rightarrow0}{(x^n)}$


$\sin(x)$ all'ordine $n$ in $0$
$\sin^{(1)}=\cos$
$\sin^{(2)}=-\sin$
$\sin^{(3)}=-\cos$
$\sin^{(4)}=\sin=sin^{(0)}$

$\sin^{(K)}(0)=\begin{cases}0&\text{se }K\text{ pari}\\(-1)ê&\text{se }K=2l+1\text{ è dispari}\end{cases}$
$T\sin_{2n,0}(x)=\sum\limits_{K=0}^{2n}\frac1{K!}\sin^{(K)}(0)x^K=\sum\limits_{l=0}^{n-1}\frac1{(2l+1)!}(-1)^lx^{2l+1}$

$\sin(x)=\sum\limits_{l=0}^{n-1}\frac{(-1)^l}{(2l+1)!}x^{2l+1}+0(x^{2n})=x-\frac16x^3+\frac1{120}x^5+\dots+\frac{(-1)^{n-1}}{(2n-1)!}x^{2n-1}+o(x^{2n})$
$T\sin_{2n-1,0}=T\sin_{2n,0}$


$\cos(x)$ all'ordine $2n$ in $0$
$T\cos_{2n,0}(x)=\sum\limits_{l=0}^{n}\frac{(-1)^e}{(2e)!}x^{2e}=T\cos_{2n+1,0}(x)$
$\cos(x)=1-\frac12x^2+\frac1{24}x^4+\dots+\frac{(-1)^n}{(2n)!}x^{2n}+o(x^{2n})$


$(1+x)^\alpha,\ \alpha\in\mathbb R$, all'ordine n in 0
$\begin{array}{l}\big((1+x)^\alpha\big)'=\alpha(1+x)^{\alpha-1}\\\big((1+x)^\alpha\big)''=\alpha(\alpha-1)(1+x)^{\alpha-2}\\\big((1+x)^\alpha\big)'''=\alpha(\alpha-1)(\alpha-2)(1+x)^{\alpha-3}\\\vdots\\\big((1+x)^\alpha\big)=\alpha(\alpha-1)(\alpha-2)\dots(\alpha-n-1)(1+x)^{\alpha-n}\end{array}$

$(1+x)^\alpha=1+\alpha x+\frac12\alpha(\alpha-1)x^2+\frac1{3!}\alpha(\alpha-1)(\alpha-2)x^3+\dots+\frac1{n!}\cdot\alpha(\alpha-1)(\alpha-2)\dots(\alpha-n+1)x^n+o(x^n)$

## Proposizione (unicità del polinomio di Taylor)
Sia $f$ derivabile in $x_0$ e sia $P$ un polinomio di grado $\le n$
Se vale $f(x)=P(x)+o((x-x_0)^n),x\rightarrow x_0$ allora $P=Tf_{n,x_0}$ è il polinomio di Taylor di $f$ in $x_0$ all'ordine $n$

Utilizziamo questa proposizione per costruire sviluppi di Taylor di funzioni complicate (somma, prodotto, quoziente, composta, inversa)

### Somma
$f,g$ derivabili $n$ volte in $x_0$
Vorremmo sviluppare $f+g$ all'ordine $n$ in $x_0$

$f(x)=Tf_{n,x_0}(x)+o\big((x-x_0)^n\big),\ x\rightarrow x_0$
$g(x)=Tg_{n,x_0}(x)+o\big((x-x_0)^n\big),\ x\rightarrow x_0$

$f(x)+g(x)=\underbrace{Tf_{n,x_0}(x)+Tg_{n,x_0}(x)}_{\text{grado }\le n=P(x)'}+o\big((x-x_0)^n\big),\ x\rightarrow x_0$
Deduciamo dalla proposizione che $T(f+g)_{n,x_0}=Tf_{n,x_0}+Tg_{n,x_0}$

### Prodotto
$f,g$ derivabili $n$ volte in $x_0$
Allora $f\cdot g$ è derivabile $n$ volte in $x_0$

$f(x)=Tf_{n,x_0}(x)+o\big((x-x_0)^n\big),\ x\rightarrow x_0$
$g(x)=Tg_{n,x_0}(x)+o\big((x-x_0)^n\big),\ x\rightarrow x_0$

$f(x)\cdot g(x)=Tf_{n,x_0}(x)\cdot Tg_{n,x_0}(x)+o\big((x-x_0)^n\big),\ x\rightarrow x_0$

$\underbrace{Tf_{n,x_0}(x)\cdot Tg_{n,x_0}(x)}_{\text{ha grado }\le 2n}+P(x)+R(x)\Rightarrow f(x)\cdot g(x)=P(x)+R(x)+o\big((x-x_0)^n\big)\overset {\text{prop.}} \Rightarrow T(f\cdot g)_{n,x_0}=P$
$P(x)$: parte di grado $\le n\ \begin{array}{c}(x-x_0)^0\\(x-x_0)^1\\\vdots\\(x-x_0)^n\end{array}$
R(x): resto di grado $\ge n+1\ \begin{array}{c}(x-x_0)^{n+1}\\(x-x_0)^{n+2}\\\vdots\\(x-x_0)^{2}\\=\\o\big((x-x_0)^n\big)\end{array}$


Ad esempio: $e^x\ln(1+x)$ all'ordine $3$ in $0$
$e^x=1+x+\frac12x^2+\frac16x^3+o(x^3),\ x\rightarrow0$
$\ln(1+x)=0+x-\frac12x^2+\frac13x^3(x^3),\ x\rightarrow0$
$e^x\ln(1+x)=(1\cdot0)+x^0+(1\cdot1+1\cdot0)x^1+(1\cdot(-\frac12)+1+\frac12\cdot0)x^2+(1\cdot\frac13+1\cdot(-\frac12)+\frac12\cdot1+\frac16\cdot0)x^3$
$e^x\ln(1+x)=x+\frac12x^2+\frac13x^3+o(x^3),\ x\rightarrow0$

### Quoziente
$f,g$ derivabili $n$ volte in $x_0$, $g(x_0)\ne0$
Allora $\frac fg$ è derivabile $n$ volte in $x_0$
$\frac{f(x)}{g(x)}=T(\frac fg)_{n,x_0}(x)-o\big((x-x_0)^n\big),\ x\rightarrow x_0$
$f(x)=\frac{f(x)}{g(x)}g(x)=P(x)g(x)+\underbrace{o\big((x-x_0)^n\big)\cdot g(x)}_{=0\big((x-x_0)^n\big)}$
Sostituisco sviluppi di $f$ e di $g$
$Tf_{n,x_0}(x)+o\big((x-x_0)^n\big)=P(x)\Big(Tg_{n,x_0}(x)+o\big((x-x_0)^n\big)\Big)$

Quindi cerco un polinomio $P$ di grado $\le n$ che soddisfi $Tf_{n,x_0}(x)=P(x)\cdot Tg_{n,x_0}(x)+\big((x-x_0)^n\big),\ x\rightarrow x_0$

Ad esempio, $\tan(x)=\frac{\sin(x)}{\cos(x)}$ all'ordine $3$ in $0$
Cerco l'unico polinomio $P$ di grado $\le n$ tale che $T\sin_{3,0}(x)=P(x)\cdot T\cos_{3,0}+o(x^2),\ x\rightarrow x_0$
$T\sin_{3,0}(x)=x-\frac16x^3$
$T\sin_{3,0}(x)=1-\frac12x^2$

$P(x)=a_0+a_1\overbrace{(x)}^{x_0=0}+a_2(x)^2+a_3(x)^3$
Determinare $a_0,a_1,a_2,a_3$

$x-\frac16 x^3=(a_0\cdot1)x^0+(a_0\cdot0+a_1\cdot1)x^1+(a_0\cdot(-\frac12)+a_1\cdot0+a_2\cdot1)x^2+(a_0\cdot0+a_1\cdot(-\frac12)+a_2\cdot0+a_3\cdot1)x^3+o(x^3),\ x\rightarrow 0=$
$a_0+a_1x+(-\frac12a_0+a_2)x^2+(-\frac12a_1+a_3)x^3+o(x^3),\ x\rightarrow 0\Rightarrow\begin{array}{l}\text{ordine }x^0:0=a_0\\\text{ordine }x^1:1=a_1\\\text{ordine }x^2:0=a_-\frac12a_0+a_2\\\text{ordine }x^3:-\frac16=-\frac12a_1+a_3\end{array}$

$a_0=0,a_1=1,a_2=0,a_3=\frac13$
$P(x)=x+\frac13x^3$
$\tan(x)=x+\frac13x^3+o(x^3),\ x\rightarrow0$

### Composizione
$f$ derivabile $n$ volte in $x_0$
$g$ derivabile $n$ volte in $f(x_0)$
Allora $g\circ f$ è derivabile $n$ volte in $x_0$
Cerchiamo l'unico polinomio $P$ di grado $\le n$ tale che$g(f(x))=P(x)+o(\small(x-x_0\small)^n\normalsize),\ x\rightarrow x_0$
Sappiamo che
	$f(x)=Tf_{n,x_0}(x)+o(\small(x-x_0\small)^n\normalsize),\ x\rightarrow x_0$
	$g(x)=Tf_{n,f(x_0)}(y)+o(\small(y-f\tiny(x_0)\small)^n\normalsize),\ y\rightarrow f(x_0)$
Sostituendo questi sviluppi e scartando i contributi di grado superiore ad $n$, determiniamo $P$.
#### Esempio
$\sin(e^x-1)$ all'ordine $3$ in $0$
$sin(y)=y-\frac16y^3+o(y^3),\ y\rightarrow0$
$e^x-1=x+\frac12x^2+\frac16x^3+0(x^3),\ x\rightarrow0$
$a_0+a_1x+a_2x^2+a_3x^3+o(x^3)=\underbrace{\sin(e^x-1)}_{g(f\small(x\small)\normalsize)}=(e^x-1)-\frac16(e^x-1)+o(\small(e^x-1\small)^3\normalsize)=\big(\normalsize x+\frac12x^2+\frac16x^3+o(x^3)\big)\normalsize-\frac16\big(\normalsize x+\frac12x^2+16x^3+o(x^3)\big)^3\normalsize+o\big(\normalsize x+\frac12x^3+\frac16x^3+o(x^3)^3\big)=0\cdot x^0+1\cdot x^1+\frac12 x^2+(\frac16-\frac16)x^3+o(x^3)\ x\rightarrow 0=0+x+\frac12 x^2+o(x^3)$
$a_0=0,a_1=1,a_0=\frac12,a_3=0$

Concludiamo che $\sin(e^x-1)=x-\frac12x^2+o(x^3),\ x\rightarrow0$
### Inversa
$f$ derivabile $n$ volte in $x_0$ e invertibile in un intorno di $x_0$
Allora ha senso considerare $f^{-1}$, che risulta essere derivabile $n$ volte in $f(x_0)$
Cerchiamo $P$ di grado $\le n$ tale che $f^{-1}(y)=P(y)+o(\small(y-y_0)^n\normalsize),\ y\rightarrow y_0$
Cerchiamo lo sviluppo di $f$ in $x_0$
	$f(x)=Tf_{n,x_0}(x)+o(\small(x-x_0)^n\normalsize),\ x\rightarrow x_0$
	$x_0+(x-x_0)=x=\overline f^{\ -1}(f\small(x)\normalsize)$
Sostituendo ottengo una equazione che determina univocamente i coefficienti di $P(y)=a_0+a_1(y-y_0)+\dots+a_n(y-y_0)^n$
### Esempio
$\arcsin(y)$ all'ordine 3 in $\underbrace{0}_{\sin(0)}$
$\sin(x)=x-\frac16x^3+0(x^3),\ x\rightarrow0$
$\arcsin(y)=a_0+a_1y+a_2y^2+a_3y^3+o(y^3),\ y\rightarrow0$
$x=\arcsin\small(\sin(x)\normalsize)=\arcsin\small(x-\frac16x^3+0\tiny(x^3)\small)\normalsize)=a_0+a_1(x-\frac16x^3+o\small(x^3)\normalsize)+a_2(x-\frac16x^3+o\small(x^3)\normalsize)^2+a_3(x-\frac16x^3+o\small(x^3)\normalsize)^3+o(\small(x-\frac16x^3+o\tiny(x^3)\small)^3\normalsize)$
$x^1=a_0\cdot x^0+a_1\cdot x^1+a_2\cdot x^2+(-\frac12a_1+a_3)x^3+o(x^3),\ x\rightarrow0$
$a_0=0,a_1=1,a_2=0,-\frac16a_1+a_3=0$
	$a_3=\frac16a_1=\frac16$



Concludiamo che $\arcsin(x)=u+\frac16y^3+o(y^3)$