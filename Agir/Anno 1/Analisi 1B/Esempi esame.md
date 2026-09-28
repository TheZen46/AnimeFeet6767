1) $\displaystyle\int_2^3\frac{x+3}{x^2-2x+1}dx$
	$\Delta = 2^2-4(1)(1) = 0$
	$\frac{x+3}{(x-1)^2}\underset?=\frac{A}{x-1}+\frac{B}{(x-1)^2)}=\frac{Ax-A+B}{(x-1)^2}\qquad\array{A=1\\-A+B=3}\rightarrow\array{A=1\\B=4}$  ($A$ deve essere uguale al coefficiente di $x$, mentre $-A+B$ il $+3$)
$\displaystyle\int_2^3\frac{1}{x-1}dx+4\int_2^3\frac{1}{(x-1)^2)}dx=\left[\ln|x-1|\right]_2^3-4\left[\frac{1}{x-1}\right]_2^3=\ln2-\cancel{\ln1}-4(\frac12-1)=\ln2+2$

2) $\displaystyle\int_{\sqrt7}^{\sqrt{11}}2x^3\sqrt{x^2-7}dx$
	$x^2-7=t\qquad x^2=t+7\qquad 2xdx=dt$
$\displaystyle\int_{\sqrt7}^{\sqrt{11}}x^2\sqrt{x^2-7}\cdot2xdx$
	$x=\sqrt{7}\Rightarrow t=0, x=\sqrt{11}\Rightarrow t=4$
$\displaystyle\int_0^4(t+7)\sqrt tdt=\int_0^4 t^\frac32dt +7\int_0^4 t^\frac12 dt=\frac25\left[t^\frac32\right]_0^4+7\frac23\left[t^\frac32\right]_0^4=\frac25 4^\frac32+\frac{14}{3}4^\frac32=\frac{64}5+\frac{112}3=\frac{752}{15}$

3) $\displaystyle f(x)=\frac1z\int_0^2 g(t)dt\qquad g(t)=\begin{cases}\frac{e^t-1}{t}&t\ne0\\1&t=0\end{cases}$
	Dominio e limite agli estremi della funzione
		$g$ è continua su $\mathbb R$, infatti, per $t\ne0$ ok; se $t=0\quad\lim\limits_{t\to0}g(t)=\lim\limits_{t\to0}\frac{e^t-1}t=1=g(0)$
		Allora la funzione integrale $\int_0^xg(t)dt$ è definita su $\mathbb R$
	Quindi $\operatorname{dom}(f)=\mathbb R\setminus\{0\}$
$\displaystyle\lim\limits_{x\to-\infty}f(x)=\lim\limits_{x\to-\infty}\frac{\int_0^xg(t)dt}{x}$
		Per $t\to-\infty$, $g(t)\sim\frac{-1}t\rightarrow0\text{ di ordine }1\Rightarrow\operatorname{FI}\ \frac\infty\infty$
	$\overset{\operatorname{Hosp}}{\longrightarrow}\lim\limits_{x\to-\infty}\frac{g(x)}1=0$
$\displaystyle\lim\limits_{x\to+\infty}f(x)=\operatorname{FI}\ \frac\infty\infty\overset{\operatorname{Hosp}}{\longrightarrow}\lim\limits_{x\to+\infty}\frac{g(x)}1=+\infty$
$\displaystyle\lim\limits_{x\to-\infty}f(x)=\operatorname{FI}\ \frac00\overset{\operatorname{Hosp}}{\longrightarrow}\lim\limits_{x\to0}g(x)=1$

4) $\displaystyle\int_1^\infty\frac{x^2-1}{(x-1)e^x}dx$
	Converge? Se sì, calcola
$\frac{x^2}{(x+1)e^x}\text{ è continua su }[+1,\infty)$. Devo solo controllare la convergenza a $+\infty$
$\text{Per }x\to+\infty,\ f(x)\to0\text{ esponenzialmente }(\text{ordine }>\mskip{-6mu}A\mskip{6mu} \forall A)$
Per calcolarlo: $\displaystyle\int_1^\infty\frac{(x+1)(x-1)}{(x+1)e^x}=\int_1^\infty(x-1)e^{-x}dx\Rightarrow-\left[-e^{-x}(x-1)\right]_1^\infty+\int_1^\infty e^{-x}dx=0-\left[e^{-x}\right]_1^\infty=-(0-e^{-1})=\frac1e$

5) $\lim\limits_{(x,y)\to(0,0)}\frac{\sin(-x^3y)}{(x^2+y^2)^2}$
$f(x,mx)=\frac{\sin(-mx^4)}{(1+m^2)^2 x^4}\sim\frac{-mx^4}{(1+m^2)^2 x^4}=-\frac{m}{(1+m^2)^2}$  Limite non esiste (non fermarsi, cercare restrizioni)
$f(x,0)=0$
$f(x,x)=\frac{\sin(-x^4)}{4x^4}\sim-\frac14$

6) Derivata parziali e differenziabilità in $(1,1)$ di $f(x,y)=x\ln(1+x^2+y^2)-\arctan\sqrt{x^2+y^2}$
$\frac{\partial f}{\partial x}(x,y)=\ln(1+x^2+y^2)+\frac{2x^2}{1+x^2+y^2}-\frac{1}{1+x^2+y^2}\frac{x}{\sqrt{x^2+y^2}}$
$\frac{\partial f}{\partial y}(x,y)=x\frac{2y}{1+x^2+y^2}-\frac{1}{1+x^2+y^2}\frac{2y}{2\sqrt{x^2+y^2}}$
Noto che $f$ è continua in $(1,1)$ e le sue derivate parziali sono continue in $(1,1)\to f$ è differenziabile in $(1,1)$

7) $\lim\limits_{(x,y)\to(0,0)}\frac{x^2|y|}{e^{x^2+y^2}-1}$
$f(x,mx)=\frac{|m||x|^3}{e^{x^2+m^2}-1}\sim\frac{|m||x|^3}{(1+m^2)x^2}\sim\frac{|m||x|}{1+m^2}\overset{x\to0}\rightarrow 0\ \forall m$
$|\varphi(\varphi\cos\theta,\varphi\sin\theta)|=\left|\frac{\rho^3\cos^2\theta\cdot|\sin\theta|}{e^{\rho^2}-1}\right|\le\underset{\text{conforme in }\theta}{\left|\frac{\rho^3}{e^{\rho^2}-1}\right|}\overset{\rho\to0}{\sim}\frac{\rho^3}{\rho^2}=\rho\overset{\rho\to0}\longrightarrow0$
$\Rightarrow\lim\limits_{(x,y)\to(0,0)}f(x,y)=0$
