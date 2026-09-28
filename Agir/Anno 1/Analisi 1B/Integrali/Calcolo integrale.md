# Primitive (integrali indefiniti)
Operazioni inverse della derivata

## Definizione
Sia $I\subseteq\mathbb R$ e sia $f:I\rightarrow\mathbb R$
Diciamo che $F$ è una **primitiva** di $f$ su $I$ se $F'(x)=f(x)\ \forall x\in I$
(in particolare $F$ deve essere derivabile)

### Esempi
1) $\frac{x^2}2$ è primitiva di X su $\mathbb R$. Infatti $\frac d {dx}(\frac{x^2}2)=\frac{2x}2=x$  \[Anche $\frac{x^2}2+1$ lo è\]
2) $-\cos x$ è primitiva di $\sin x$ su $\mathbb R$. Infatti $\frac{d}{dx}(-\cos x)=\sin x$

**Nota**
Se $F$ è primitiva di $f$ su un intervallo $I$, allora anche $F+c$ lo è $\forall c \in \mathbb R$
Viceversa se $F$ e $G$ sono due primitive di $F$, allora $\exists c \in\mathbb R$ t.c. $G=F+c$
Infatti, posto $H=G-F$ si ha che $H'(x)=G'(x)-F'(x)=f(x)-f(x)=0$


Segue dal teorema di Lagrange che $H$ è costante $\Rightarrow\ \exists c\in\mathbb R$ t.c. $H(x)=c\Rightarrow G(x)-F(x)=c\Rightarrow G-F+c$


# Definizione
L'insieme dei tutte le primitive di una funzione $f$ su un intervallo $I$ si dice **integrale indefinito** di $f$ su $I$ e si indica con $\int f(x)dx$
Se $F$ è una primitiva di $f$ scriviamo $\int f(x)dx=F(x)+c$ su $I$

**Nota**
Come vedremo, non tutte le funzioni ammettono primitiva (però tutte le funzioni continue ammettono primitiva)

# Primitive fondamentali
| $f(x)$                   | $F(x)$                            |               | Per                              |
| ------------------------ | --------------------------------- | ------------- | -------------------------------- |
| $x^\alpha$               | $\frac{x^{\alpha+1}}{\alpha+1}+c$ | $\alpha\ne-1$ | $I\subseteq\text{dom}(x^\alpha)$ |
| $\sin x$                 | $-\cos x+c$                       |               | $I=\mathbb R$                    |
| $\cos x$                 | $\sin x+c$                        |               | $I=\mathbb R$                    |
| $\frac1x$                | $\ln(\lvert x\rvert)+c$           |               | $I=(\infty,0),(0,+\infty)$       |
| $e^x$                    | $e^x+c$                           |               | $I=\mathbb R$                    |
| $\frac1{1+x}$            | $\arctan x+c$                     |               | $I=\mathbb R$                    |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x+c$                     |               | $I=(-1,1)$                       |

# Proprietà di linearità
Se $f$ e $g$ hanno primitive $F,G$ su un intervallo $I$ e $\alpha,\beta\in\mathbb R$, allora $\alpha f+\beta g$ ha primitiva usuale a $\alpha F+\beta G$.
Equivalentemente $\int(\alpha f(x)+\beta g(x))dx=\alpha\int(f(x))dx+\beta\int(g(x))dx$
Infatti $\frac d{dx}(\alpha F(x)+\beta G(x)=\alpha F'(x)+\beta G'(x)=\alpha f(x)+\beta g(x))$
Quindi $\alpha F+\beta G$ è primitiva di $\alpha f+\beta g$


## Esempi
1) $\int(5x^2+e^x)dx=5\int x^2dx+\int e^xdx=5\frac{x^3}3+e^x+c$
2) $\int(\sin|x|)dx\ \ \begin{cases}\sin x&\text{ se }x\ge0\\-\sin x&\text{ se }x<0\end{cases}$
	Quindi se una primitiva $F$ esiste deve valere
	$F(X)=\begin{cases}-\cos x+c_1&\text{ se }x\ge0\\\cos x+c_2&\text{ se }x<0\end{cases}$

Per essere una primitiva, $F$ deve essere derivabile e quindi continua
Dobbiamo verificare/imporre la continuità in $0$, ossia che $\underbrace{F(0)}_{-1+c_1}=\underbrace{\lim\limits_{x\rightarrow 0^+}F(x)}_{-1+c_1}=\underbrace{\lim\limits_{x\rightarrow 0^+}F(X)}_{1+c_2}$
Quindi per la continuità si deve avere $-1+c_1=1+c_2\Rightarrow c_2=-1+c_1\Rightarrow F(x)=\begin{cases}-\cos x&\text{ se }x\ge0\\\cos x-2&\text{ se }x<0\end{cases}$
Si verifica che $F$ è derivabile e vale $F'=f$ su $\mathbb R$.

3) $f(x)=\begin{cases}0&\text{ se }x<0\\1&\text{ se }x\ge0\end{cases}$
Se una primitiva $F$ di $f$ su $\mathbb R$ esiste è $f(x)=\begin{cases}c_1&\text{ se }x<0\\x+c_2&\text{ se }x\ge0\end{cases}$
Imponendo la continuità in $0$ otteniamo $c_1=c_2\Rightarrow F(x)=\begin{cases}0&\text{ se }x<0\\x+x&\text{ se }x\ge0\end{cases}$
Ma $F$ non è derivabile in $0$ (punto angoloso) e quindi $f$ non ha primitiva su $\mathbb R$

## Teorema (integrazione per parti)
Siano $f,g$ derivabili su un intervallo $I$. Si supponga che $f'\cdot g$ abbia primitiva su $I$. Allora anche $f\cdot g'$ ha primitiva su $I$ e vale $\int (f(x)g'(x))dx=f(x)g(x)-\int(f'(x)g(x))dx$

### Dimostrazione
Sia $H$ una primitiva di $f'\cdot g$
Allora $\frac d{dx}(f(x)g(x)-H(x))=f'(x)g(x)+f(x)g'(x)-\underbrace{f'(x)g(x)}_{H(x)}=f(x)g'(x)$
Quindi $f\cdot g-H$ è una primitiva di $f\cdot g'$ che è equivalente, per definizione a $\int (f(x)g'(x))dx=f(x)g(x)-\int(f'(x)g(x))dx$

### Esempio
$\int(\ln x)dx$ su $(0,+\infty)$
$\int(\underbrace{1}_{\frac{d}{dx}(x)}\cdot \ln x)dx\Rightarrow\int(\frac d{dx}(x)\ln x) dx= x\ln x-\int(x\frac{d}{dx}(\ln x))dx=x\ln x-\int(x\cdot\frac1x)dx=x\ln x-x+c$


## Teorema (integrazione per sostituzione)
Sia $f$ integrabile su un intervallo $J$ con primitiva $F$. Sia $\varphi$ derivabile su un intervallo $I$ e a valori in $J$. Allora anche $(f \circ f) \cdot \varphi'$ ha primitiva su $I$ e si ha $\int(f(f(x))q'(x))dx=F(\varphi(x))+c$
Equivalentemente $\int(f(f(x))\varphi'(x))dx=\left[\int(f(y))dy\right]_{y=\varphi(x)}$
Se $\varphi$ è invertibile abbiamo anche $\int(f(y))sy=\left[\int(f(f(t)\varphi'(t)))dt\right]_{t=\varphi^{-1}(y)}$

### Dimostrazione
Verifichiamo
$\frac d{dx}(F(\varphi(x)))=F'(\varphi(x))\cdot\varphi'(x)=f(\varphi(x))\cdot\varphi'(x)$

### Esempi
1) $\int (x e^x)dx=\frac12\int(2xe^x)dx$
	$\varphi(x)=x^2\rightarrow \varphi'(x)=2x$
	$\frac12\int(\varphi'(x)e^{\varphi(x)})dx=\frac12\left[e^y\right]_{y=x^2}=\frac12\left[e^y+c\right]_{y=x^2}=\frac12 e^{x^2}+c$
2) $\int(\frac1{x+1})dx=\left[\int(1{y})dy\right]_{y=x+1}=\ln|x+1|+c$
3) $\int(\tan x)dx=\int(\frac{\sin x}{\cos x})dx=\int(\frac{-\varphi'(x)}{\varphi(x)})dx$
	$[y=\varphi(x)=\cos x\rightarrow \varphi'(x)=-\sin x]$
	$\left[\int(\frac{-1}y)dy\right]_ {y=\cos x}=-\ln|\cos x|+c$ su $(-\frac\pi2,\frac\pi2)$
4) $\int(\frac{e^x}{1+e^{2x}})dx$
	$[y=e^x\rightarrow \overbrace{x=\ln y}^{y>0}\rightarrow dx=\frac{dy}y]$
	$\int(\frac{y}{1+y^2})\frac{dy}y=\int(\frac{1}{1+y^2})dy=\arctan(y)+c=\arctan(e^x)+c$

# Integrazioni di funzioni razionali
$\int(\frac{P(x)}{Q(x)})dx$ con $P,Q$ polinomi
1) $\displaystyle\int(\frac{Ax+B}{Cx+D})dx=\frac1c\int(\frac{Ax+B}{x+\frac D C})dx=\frac1c\int(\frac{A(X+\frac D C)-\frac{DA}C+B}{x+\frac B C})dx=\frac1c\int(A+\frac{B-\frac{DA}C}{x+\frac DC})dx=\frac1c(Ax+(B-\frac{DA}C)\ln|X+\frac DC|)+\overbrace{K}^{\text{cost}}$
	\[dopo sostituzione $y=x+\frac DC$\] come in 2 (esempi precedenti)
2) $\int(\frac D{Ax^2+Bx+c})dx$
$D, A \ne 0\rightarrow$ raccogliendo ci riduciamo a $\int(\frac1{x^2+bx+c})dx$
3 casi
$\Delta=B^2-4C$
a) $\Delta>0$
b)$\Delta=0$
c) $\Delta<0$


Caso 3: $\Delta<0$
$x^2+bx+c=(x+\frac b2)^2+\overbrace{c-\frac{b^2}4}^{-\Delta}$
$\int(\frac1{(x+\frac b2)^2+|\Delta|})dx=\frac1{|\Delta|}\int\frac{dx}{1+(x+{\frac b 2})^2}$

$\int\frac1{x^2+Bx+C}dx\rightarrow\Delta=B^2-4C$

Caso 2: $\Delta=0$
$x^2+Bx+C=(x+\frac B2)^2$
$\int\frac1{x^2+Bx+C}dx=\int\frac1{(x+\frac B2)^2}dx$
$\int\frac1{y^2}dy=\left[-y^{-1}\right]_{y=x+\frac B2}=(-x+\frac{B}2)^{-1}+K$

Caso 1: $\Delta > 0$
$x^2+Bx+C=(x-x_1)(x-x_2)$
$\frac1{x^2+Bx+C}=\frac{\alpha}{x-x_1}+\frac{\beta}{x-x_2}$
$\frac1{x^2+Bx+C}=\frac{\alpha(x-x_1)+\beta(x-x_2)}{x^2+Bx+C}\Rightarrow\frac1{x^2+Bx+C}=\frac{\alpha(x-x_1)+\beta(x-x_2)}{x^2+Bx+C}\Rightarrow\begin{cases}\alpha+\beta=0\\-(\alpha x_2+\beta x_1)=1\end{cases}\Rightarrow\text{risolvo trovando }\alpha, \beta$

$\int\frac1{x^2+Bx+C}dx=\int\frac\alpha{x-x_1}dx+\int\frac\beta{x-x_2}dx=\alpha\ln{|x-x_1|}+\beta\ln{|x-x_2|}+k$

$\int\frac{Dx+E}{x^2+Bx+C}dx=\int\frac{\frac D2(2x+B)+E-\frac{BD}2}{x^2+Bx+C}dx=\frac D2\underbrace{\int\frac{2x+B}{x^2+Bx+C}dx}_{y=x^2+Bx+C}+(E-\frac{BD}2)\underbrace{\int\frac{dx}{x^2+Bx+C}}_{\text{come prima}}=\frac D2\ln|x^2+Bx+C|+(E-\frac{BD}2)\int\frac{dx}{x^2+Bx+C}+C_0$
