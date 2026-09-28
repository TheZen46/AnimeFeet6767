$\displaystyle f(x,y)=\begin{cases}\frac{x^2y}{x^2+y^2}&(x,y)\ne(0,0)\\0&(x,y)=(0,0)\end{cases}$
1) Continuità in $(0,0)$
$\lim\limits_{(x,y)\to(0,0)}f(x,y)\overset{?}{=}0$
$\forall\epsilon>0\ \ \overset{?}{\exists}\delta_\epsilon>0\text{ t.c. }0<|(x,y)|<\delta_\epsilon\Rightarrow|f(x,y)|<\epsilon$

$\vec x=(x,y)\mskip{24mu}\vec x\ne(0,0)$
$\vec x=t\vec v$
$\vec v=\frac{\vec x}{\Vert\vec x\Vert}=(\alpha,\beta)$
$t=\Vert\vec x\Vert$
$\Vert\vec v\Vert=1=\sqrt{\alpha^2+\beta^2}$
$\displaystyle f(\vec x)=\frac{t^2(\alpha^2)t\beta}{t^2\alpha^2+t^2\beta^2}=\frac{t^3}{t^2}\frac{\alpha^2\beta}{\underbrace{\alpha^2+\beta^2}_{\Vert\vec v\Vert = 1}}=t(\alpha^2\beta)$
$|f(\vec x)|<t\Rightarrow \vert(\vec x)<\Vert\vec x\Vert$

Fissato $\epsilon$ scelgo $\delta_\epsilon=\epsilon$
Se $\vec x\ne 0\ \Vert\vec x\Vert<\delta_\epsilon$
$|f(\vec x)|<\Vert\vec x\Vert<\delta_\epsilon=\epsilon$
$f(\vec x)=0$
$f$ è continua in $(0,0)$

2) Derivate direzionali in (0,0)
$\vec w=(\alpha,\beta)\mskip{24mu}\vec w\ne(0,0)$
$\displaystyle \frac{\partial f}{\partial \vec w}=\lim\limits_{t\to 0}\frac{f(0+t\vec w)-f(0)}{t}=\frac{\cancel {t^3}}{\cancel {t^3}}\frac{\alpha^2\beta}{\alpha^2+\beta^2}$
	$\vec x=t\vec w=(t\alpha,t\beta)$
	$\displaystyle f(0+t\vec w)=\frac{t^2}{(\alpha^2+\beta^2)}$
$\displaystyle \forall\ \vec w\ne0\ \ \exists \frac{\partial f}{\partial \vec w}\big((0,0)\big)=\frac{\alpha^2\beta}{\alpha^2+\beta^2}$
