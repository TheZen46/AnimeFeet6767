1) $f:\mathbb R^3\to\mathbb R\qquad f(x,y,z)=\sin\left(\frac{xy^2}{1+z^2}\right)$
	Calcolare le derivate direzionali e il gradiente nel punto $(0,1,1)$
$\frac{\partial f}{\partial x}(x,y,z)=\cos\left(\frac{xy^2}{1+z^2}\right)\frac{y^2}{1+z^2}$
$\frac{\partial f}{\partial y}(x,y,z)=\cos\left(\frac{xy^2}{1+z^2}\right)\frac{2xy}{1+z^2}$
$\frac{\partial f}{\partial z}(x,y,z)=\cos\left(\frac{xy^2}{1+z^2}\right)\frac{-2xy^2z}{(1+z^2)^2}$
$\nabla_{\!f}\ (0,1,1)=(\frac12,0,0)$

2) $f:\mathbb R^2\to\mathbb R\qquad f(x,y)=x^3+y^3+xy$
	1) Piano tangente a $f$ nel punto $\left(1,1, f(1,1)\right)$
	2) Versore normale al grafico di $f$ nel punto $\left(0,1, f(0,1)\right)$

1)
$z=f(1,1)+\frac{\partial f}{\partial x}(1,1)(x-1)+\frac{\partial f}{\partial y}(1,1)(y-1)$
$z=f(x_0,y_0)+\nabla_{\!f}\ (x_0,y_0)\cdot(x-x_0,y-y_0)$
$\nabla_{\!f}\ (x,y)=(3x^2+y,3y^2+x)$
$z=3+4(x-1)+4(x-1)=4x+4y-5$

2)
Versore normale
- $\perp$ al punto tangente
- di lunghezza $1$

$\left(0,1,f(0,1)\right)$
$z=1+(x-0)+3(y-1)\Rightarrow x+3y-z-2=0$
$\vec\ \perp\text{ a piano }\tan\to(1,3,-1)$
$\frac{(1,3,1)}{\sqrt{1+9+1}}=\pm\left(\frac1{\sqrt11},\frac3{\sqrt11},\frac{-1}{\sqrt11}\right)$


3) $f(x,y)=\arctan(x^2+y^2)$
	Calcolare (se $\exists$) la derivata direzionale di $f$ rispetto a $v=(\frac{\sqrt2}2,\frac{\sqrt2}2)$ in $(1,-1)$

Derivata direzionale
$f'(x_0)=\lim_{(h\to0)}\frac{f(x_0+h)-f(x_0)}h$
$\displaystyle\frac{\partial f}{\partial v}(x_0,y_0)=\lim_{(h\to0)}\frac{f\left(x_0+v_1h,y_0+v_2h\right)-f(x_0,y_0)}h$

$\displaystyle\frac{\partial f}{\partial v}(1,-1)\overset{\text{se }\exists}{=}\lim_{(h\to0)}\frac{\arctan\left((1+\frac{\sqrt2}2 h)^2+(-1+\frac{\sqrt2}2 h)^2\right)-\arctan h}h=\lim_{(h\to0)}\frac1h\left(\arctan(2+h^2)-\arctan2\right)$

	$\array{g(h)=\arctan(2+h^2)&g(0)=\arctan2\\g'(h)=\frac{2h}{1+(2+h^2)^2}&g'(0)=0}$
	$g(h)=g(0)+g'(0)h+o(h^2)=\arctan2+o(h^2)$

$\displaystyle\lim_{(h\to0)}\frac1h\left(\arctan(2+h^2)-\arctan2\right)=\lim_{(h\to0)}\frac{o(h^2)}h=\lim_{(h\to0)}0(h)=0$


Altra formula
$\frac{\partial f}{\partial v}(x_0,y_0)\overset{\text{sotto ipotesi}}{=}\nabla_{\!f}\ (x_0,y_0)\bullet v$
$f$ costante
$\frac{\partial f}{\partial v}\quad\frac{\partial f}{\partial v}\quad$ costante in un intorno del punto $(1,-1)$
	$\nabla_{\!f}\ (x,y)=\left(\frac{2x}{1+(x^2+y^2)^2},\frac{2y}{1+(x^2+y^2)^2}\right)$
$\frac{\partial f}{\partial v}(1,-1)=\left(\frac25,-\frac25\right)\cdot\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)=0$
Se la formula desse $\infty$ in $\nabla$, allora bisogna usare il metodo 1

4) Caso senza formula 2$\quad f(x,y)=\sqrt x\sin^2(x)y$
$\frac{\partial f}{\partial x}(x,y)=\frac y{2\sqrt x}\sin^2 x+\sqrt{x}y\cdot2\sin x\cos x$
$\frac{\partial f}{\partial x}(0,0)$ problema

5) $f(x,y)=\begin{cases}(x^2+y^2)^\alpha&(x,y)\ne(0,0)\\0&(x,y)=(0,0)\end{cases}$
- Studiare la differenziabilità in $(0,0)$ nei casi:
	1) $\alpha=-\frac25$
	2) $\alpha=\frac47$

$f(x,y)=(x^2+y^2)^{-\frac25}$
$\lim\limits_{(x,y)\to(0,0)}f(x,y)=$
	$\displaystyle f(\varphi\cos\theta,\varphi\sin\theta)=\left(\varphi^2(\cos^2\theta+\sin^2\theta)\right)^{-\frac25}=\varphi^{-\frac45}=\frac1{\varphi^{\frac45}}\overset{\varphi\to0}{\longrightarrow}\infty$
$\Rightarrow f$ non è continua in $\vec0$
$\Rightarrow f$ non è differenziabile in $\vec0$


$f(x,y)=(x^2+y^2)^{-\frac47}$
$\nabla_{\!f}\ (x,y)=\left(\frac47(x^2+y^2)^{-\frac37}\cdot2x,\frac47(x^2+y^2)^{-\frac37}\cdot2y\right)$
$\frac{\partial f}{\partial x}(0,0)\overset{\text{se }\exists}{=}\lim\limits_{h\to0}\frac{f(h,0)-f(0,0)}h=\lim\limits_{h\to0}\frac{h^{\frac87}}h=0$
$\frac{\partial f}{\partial y}(0,0)\overset{\text{se }\exists}{=}\lim\limits_{h\to0}\frac{f(0,h)-f(0,0)}h=\lim\limits_{h\to0}\frac{h^{\frac87}}h=0$

$\lim\limits_{(x,y)\to(0,0)}\frac{f(x,y)-f(0,0)-\frac{\partial f}{\partial x}(0,0)\cdot x-\frac{\partial f}{\partial y}(0,0)\cdot y}{\sqrt{x^2+y^2}}$
$\displaystyle\lim\limits_{(x,y)\to(0,0)}\frac{(x^2+y^2)^{\frac47}}{\sqrt{x^2+y^2}}=\lim\limits_{(x,y)\to(0,0)}(x^2+y^2)^{\frac1{14}}=0$

$\frac{\partial f}{\partial x}(x_0,y_0)=\lim\limits_{h\to0}\frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}$

Modo 2
$\lim\limits_{(x,y)\to(0,0)}\frac{\partial f}{\partial x}(x,y)=\lim\limits_{(x,y)\to(0,0)}\frac{8x}7(x^2+y^2)^{\frac37}$
$\left|f(\varphi\cos\theta,\varphi\sin\theta)\right|=\frac87\varphi|\cos\theta|\cdot\varphi^{-\frac67}\le\frac87\varphi^{\frac17}\to0\Rightarrow\frac{\partial f}{\partial x}(x,y)$ è continua in $(0,0)$
Stessa cosa
$\Rightarrow\frac{\partial f}{\partial x}(x,y)$ è continua in $(0,0)$
$\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}$ è continua in $(0,0)\Rightarrow f$ diff in $(0,0)$


5) $f(x,y)=\ln(x^2y)-\frac{xy}2+y$
	1) Dominio
	2) Estremo relativo di $f$ sul suo dominio
	3) $\max/\min$ assoluti di $f$ sia $T=\left\{(x,y)\in\mathbb R^2:\array{\frac12\le x\le 2\\\frac1x\le y\le2}\right\}$
1)
$\operatorname{Dom}(f)=\{(x,y)\in\mathbb R^2:x^2y>0\}\Rightarrow\array{y>0\\x\ne0}$

2)
$\max/\min$ su $\operatorname{Dom}(f)$
Li cerco tra i punti
- Che annullano $\nabla_{\!f}$
- Punti problematici
$\nabla_{\!f}\ (x,y)=\left(\frac{\partial f}{\partial x}(x,y),\frac{\partial f}{\partial y}(x,y)\right)=\left(\frac{2xy}{x^2y}-\frac y2,\frac{x^2}{x^2y}-\frac x2+1\right)=\left(\frac2x-\frac y2,\frac1y-\frac x2+1\right)$
$\nabla_{\!f}\ (x,y)=(0,0)\iff\cases{\frac2x-\frac y2=0\\\frac1y-\frac x2+1=0}$
	$\overset{x,y\ne\vec0}\iff\cases{4-xy=0\\2-xy+2y=0}\iff\cases{xy=4\\2-4+2y=0}\iff\cases{xy=4\\2y=2}\iff\cases{x=4\\y=1}$
Punti critici: $(4,1)$

Studio natura di $(4,1)$
$H_f(x,y)=\pmatrix{-\frac2{x^2}&-\frac12\\-\frac12&-\frac1{y^2}}$
$H_f(4,1)=\pmatrix{-\frac18&-\frac12\\-\frac12&-1}$
$\det(H_f(4,1))=\frac18-\frac14=-\frac18<0$
	$\det<0\Rightarrow\text{autovalori opposti}\Rightarrow(4,1)\text{ punto di sella}$

$\det\left(H_f(4,1)-\pmatrix{\lambda&0\\0&\lambda}\right)=\pmatrix{-\frac18-\lambda&-\frac12\\-\frac12&-1-\lambda}=(-\frac18-\lambda)(-1-\lambda)-\frac14\overset?=0$

3)
$\array{f\text{ continua su }T\\T\text{ compatto}}\overset{\text{Weierstrass}}\Rightarrow\array{f\text{ ammette }\max\\\text{e }\min\text{ assoluti}}$
Li cerco sui bordi
