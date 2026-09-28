# Definizione
Sia $f:\Omega\subseteq\mathbb R^n\to\mathbb R$ e sia $x_0$ un punto di accumulazione per $\Omega$.

$\lim_{\vec x\to\vec{x_0}}f(\vec x)=L\in\mathbb R$
se $\forall\ \varepsilon>0,\ \exists\ \delta>0$ tale che $|f(\vec x)-L|<\varepsilon$
$\forall\ \vec x\in\Omega$ tale che $\delta<||\vec x-\vec{x_0}||<\varepsilon$ ($\forall\ \vec x\in\Omega\cap(B_\delta(\vec{x_0})\setminus\{\vec{x_0}\})$)

## Proprietà
Valgono le usuali proprietà del limite su somma, prodotto e quoziente, sull'unicità del limite e sul confronto


# Definizione
Sia $f:\Omega\subseteq\mathbb R^n\to\mathbb R$, sia $\vec{x_0}\in\Omega$. Diciamo che $f$ è continuo in $\vec{x_0}$ se
- $x_0$ non è punto di accumulazione per $\Omega$
oppure se
- $\lim_{\vec x\to\vec{x_0}}f(\vec x)=f(x_0)$

Dato $A\subseteq\Omega$. Diciamo che $f$ è continua in $A$ se è continua in ogni punto di $A$

## Proprietà
Valgono le usuali proprietà delle funzioni continue. In particolare somma, prodotto, quoziente, composizione di funzioni continue sono continue sul loro dominio. In particolare, sono continue sul loro dominio le funzioni costruite (non a tratti) a partire da polinomi, funzioni razionali, radici, esponenziali, logaritmo, funzioni goniometriche

### Esempio
$f(x,y)=\ln(2+x^2+y^2+\sin(\frac xy)+\frac1{x-1}$
$\text{Dom}(f)=\{(x,y)\ |\ y\ne0,x\ne1\}$

$f$ è continua su $\text{Dom}(f)$



$f(x,y)=\frac{x^2}{x^2+y^2}$
Calcolare $\lim\limits_{(x,y)\to(0,0)}f(x,y)$

$\text{Dom}(f)=\mathbb R^2\setminus\{0,0\}$

$|f(x,y)|=\frac{|x^3|}{x^2+y^2}$

Se $a,b\ge0,\ (a,b)\ne(0,0)$
$\frac1{a+b}\le\frac1a$

se $x^2>0\iff x\ne0$
	$|f(x,y)|=\frac{|x^3|}{x^2+y^2}\le\frac{|x^3|}x^2=|x|$

E la disuguaglianza $|f(x,y)|\le x$ vale in modo banale anche se $x=0\ \left((x,y)\in\text{Dom}(f)\right)$

**Equivalentemente** $-|x|\le f(x,y)\le|x|$

Quindi, per confronto $f(x,y)\to0$, ossia $\lim\limits_{(x,y)\to(0,0)}f(x,y)=0$



$f(x,y)=\frac{x+y}{x-y}\qquad\lim\limits_{(x,y)\to(0,0)}f(x,y)=?$

$\text{Dom}(f)=\{(x,y)\ |\ x\ne y\}$
Dobbiamo capire come si comporta $f$ per $(x,y)\to(0,0)$
 Perché il limite esiste ,deve essere lo stesso lingo ogni \[curva?] per $(x_0,y_0)$
Proviamo a calcolare il limite di $f$ quando $(x,y)$ è ristretto alla retta $x=0$ (che passa per $(0,0)$)

$\lim\limits_{\underset{x=0}{(x,y)\to(0,0)}}f(x,y)=\lim\limits_{y\to0}f(0,y)=\lim\limits_{y\to0}\frac y{-y}=-1$

Restringiamo ora a $y=0$

$\lim\limits_{\underset{y=0}{(x,y)\to(0,0)}}f(x,y)=\lim\limits_{x\to0}f(x,0)=\lim\limits_{x\to0}\frac xx=1$

Dato che i limiti ristretti alle due rette sono diversi, allora $\lim\limits_{(x,y)\to(0,0)}f(x,y)$ non esiste



$f(x,y)=\frac{x^2y}{x^4+y^2}$
$\text{Dom}(f)=\mathbb R^2\setminus\{(0,0)\}$

\[Primi?] tentativi:
$\left|\frac{x^2y}{x^4+y^2}\right|\le\frac{x^2|y|}{x^4}=\frac{|y|}{x^2}$
$\left|\frac{x^2y}{x^4+y^2}\right|\le\frac{x^2|y|}{y^2}=\frac{x^4}{|y|}$
Non sono utili


Su $x=0:$
$\lim\limits_{y=0}f(0,y)=\lim\limits_{y\to0}\frac0{y^2}=0$

Su $y=0:$
$\lim\limits_{x=0}f(x,0)=\lim\limits_{x\to0}\frac0{x^4}=0$

Su $y=mx$ (con $m\ne0,\ y=0$ già fatto)
$\lim\limits_{x\to0}f(x,mx)=\lim\limits_{x\to0}\frac{mx^3}{x^4+m^2x^2}=\lim\limits_{x\to0}\frac{mx}{\underbrace{x^2+m^2}_{m^2\ne0}}=0$
Quindi $f(x,y)\to0$ lungo qualunque retta passante per $(0,0)$
Questo non basta a concludere che il limite esiste ed è zero (in effetti è falso)

Restringendo alla parabola $y=x^2$ (passante per $(0,0)$) abbiamo infatti $\lim\limits_{\underset{y=x^2}{(x,y)\to(0,0)}}f(x,y)=\lim\limits_{x\to0}(x,x^2)=\lim\limits_{x\to0}\frac{x^2\cdot x^2}{x^4+x^4}=\lim\limits_{x\to0}\frac{x^4}{2x^4}=\frac12\ne0$
Quindi il limite non esiste