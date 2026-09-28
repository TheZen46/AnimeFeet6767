1) $\begin{cases}y'(x)=\frac1x y(x)+x^2\ln(1+|x|)\\y(-1)=\alpha&\alpha\in\mathbb R\end{cases}$
a) Esistenza e unicità soluzione al variare di $\alpha$ specificando il dominio
Eq diff $1$ lineare
$y'(x)=a(x)y(x)+b(x)$

$a(x)=\frac1x\in\mathcal C^0()$ ?
	Continua su $(-\infty,0)\cup(0,+\infty)$
	ma $-1\in(-\infty,0)$
$a(x)=\frac1x\in\mathcal C^0({\small(-\infty,0)})$
$b(x)=x^2\ln(1+|x|)\in\mathcal C^0({\small(-\infty,0)})\Rightarrow\forall\alpha\in\mathbb R\quad\exists!\text{ soluzione su }(-\infty,0)$

b) Risolvere per $\alpha=0$
$\begin{cases}y'(x)=\frac1x y(x)+x^2\ln(1+|x|)\\y(-1)=\underbrace{0}_{\alpha}&\alpha\in\mathbb R\end{cases}$

Troviamo $y(x)=e^{A(x)}(c+K(x))\quad x\in\mathbb R,\ A\text{ primitiva di }a,\ K\text{ primitiva di }e^{-A}b$

$A(x)=\int_{x_0}^{x}a(t)dt$
$c=y_0$
$\displaystyle A(x)=\int_{-1}^x\frac1tdt=\ln|x|\overbrace{=}^{x\in(-\infty,0)}\ln(-x)$
$\displaystyle y(x)=e^{\ln|x|}(0+\int_{-1}^x e^{-\ln(t)}t^2\ln(1+t)dt)$
$\displaystyle y(x)=x\int_{-1}^x -\frac{t^2}t\ln(1+t)dt=x\left[\frac{t^2}t\ln(1-t)\right]_{-1}^x-x\int_{-1}^x\frac{t^2}2\frac{1}{t-1}=\frac{x^3}2\ln(1-x)-\frac x2\ln(2)-\frac x2\int_{-1}^x\frac{t^2}{t-1}dt$
$\displaystyle \int\frac{t^2}{t-1}dt=\int\frac{t^2-t+t}{t-1}dt=\int\frac{t^2-t}{t-1}dt+\frac{t-1+1}{t-1}dt=\int\frac tdt+\int 1dt+\int\frac{1}{t-1}dt=\frac{t^2}2+t+\ln|t-1|+c$
$\displaystyle \int_{-1}^x\frac{t^2}{t-1}dt=\frac{x^2}2+x+\ln(1-x)-\frac12+1-\ln(2)$
$\displaystyle y(x)=\frac{x^3}2\ln(1-x)+\cancel{\frac x2\ln(2)}-\frac{x^3}4-\frac{x^3}2-\frac x2\ln(1-x)-\frac x4+\cancel{\frac x2\ln(2)}$

2) $y''(x)-4ay(x)=0\quad a\in\mathbb R$
a) Determinare l'integrale lineare
EQ di ordine $2$ a coefficienti costanti

Polinomio caratteristico
$\lambda^2-4a$
Radici
$\lambda^2=4a$
Se $\Delta>0\text{ cioè } a>0$
	$\lambda^2=4a\quad \lambda_1=2\sqrt a\quad\lambda_2=-2\sqrt a$
	$y(x)=c_1e^{2\sqrt a x}+c_2 e^{-2\sqrt a x}$
Se $\Delta=0\text{ cioè } a=0$
	$\lambda^2=0\quad\lambda_1=\lambda_2=0$
	$y(x)=c_1 e^{0x}+c_2 x e^{0x}=c_1+c_2x$
Se $\Delta<0\text{ cioè }a<0$
	$\lambda^2=4a\quad \lambda_\pm=\pm2i\sqrt{-a}$
	$y(x)=c_1 e^{\overbrace{0x}^{ix}}\cos(\underbrace{2\sqrt {-a}}_\beta x)+c_2\sin(\underbrace{2\sqrt{-a}}_\beta x)$
	$0\pm i\cdot 2\sqrt{-a}$
	$\alpha\pm i\beta$

b) Stabilire se $\exists$ soluzioni che tendono a $0$ per $x\to+\infty$
$\alpha>0$
	$y(x)= c_1\ \underbrace{e^{2\sqrt a x}}_{\to\infty}+c_2\ \underbrace{e^{-2\sqrt a x}}_{\to 0}$
	Scelgo $c_1=0$
	$y(x)=c_2 e^{-2\sqrt a x}\quad\forall c_2\in \mathbb R$
c) Soluzioni limitate (convergono)
$\begin{array}{l}a>0&c_1=0&c_2=0\\a=0&\forall\ c_1&c_2=0\\a<0&\forall c_1&\forall c_2&\leftarrow(\cos,\sin\in{\small(-c_x,c_x)})\end{array}$

d) Risolvi Cauchy
$\cases{y''(x)-ay(x)=0\\ y(0)=0\\y'(x)=4a}$

$a>0$
	$y(x)=c_1 e^{2\sqrt a x}+c_2e^{-2\sqrt a x}$
	$y(0)=0\rightarrow c_1+c_2=0$
	$y'(0)=4a$
		$2\sqrt a c_1-2\sqrt a c_2=4a\rightarrow c_1-c_2=2\sqrt a$
	$\begin{cases}c_1+c_2=0&c_1=-c2&c_2=-\sqrt a\\c_1-c_2=2\sqrt a&2c_1=2\sqrt a&c_1=\sqrt a\end{cases}$

3) $\begin{cases}y''(x)-4 y(x)=x\\y''(x)+ay'(x)+by(x)=f(x)\end{cases}$

Soluzioni
$y(x)=y_0(x)+y_p(x)$
$y_0$
	Risolvo l'equazione omogenea $y''(x)-4y(x)=0$
	$\lambda^2-4=0\quad \lambda=\pm2\quad\lambda y_0(x)=c_1 e^{2x}+c_2e^{-2x}\quad c_1,c_2\in\mathbb R$
$y_p$
	Cerco la soluzione particolare nella famiglia seguente

$f(t)=Q_n(t)\cdot e^{\alpha t}$
$y_p(x)=ax+b$
$y_p'(x)=a$
$y_p''(x)=0$
$0-4(ax+b)=x$
$-4ax-4b=x$
$-4a=1$
$a=-\frac14$

$y(x)=-\frac x4+c_1 e^{2x}+c_2 e^{-2x}$

$\cases{y''(x)-4y(x)=x+e^x(e^x+1)\\ y(0)=0\\y'(0)=0}$

Omogenea identica
$y_p\quad f(t)=f_1(t)+f_2(t)+f_3(t)$
$y_p(x)=\underset{x}{y_p^{(1)}(x)}+\underset{e^{2x}}{y_p^{(2)}}+\underset{e^x}{y_p^{(3)}}$
$y_p^{(1)}(x)=-\frac x4$
$y_p^{(2)}(x)$
	Soluzione parti di $y''(x)-4y(x)=e^{2x}$
	$f(t)=e^{2}Q_x(x)$
	$yp(x)=x^\mu \overbrace{\mathcal R_b(x)}^{\text{poly grado 0}} e^{\alpha x}$
		$\mu=\text{molteplicità di }\alpha\text{ come radice del polinomio caratteristico}$
	$yp^{(2)}=cx\ e^{2x}$
	$\text{der 1}=ce^{2x}+2cxe^{2x}$
	$\text{der 2}=2ce^{2x}+2ce^{2x}+4cx e^{2x}$
	$(4ce^{2x}+\cancel{4cxe^{2x}})-\cancel{4(cxe^{2x})}=e^{2x}$
	$4c e^{2x}=0e^{-2x}\quad 4c=1\quad c=\frac14$

$yp^{(3)}\quad y''-4y=e^x$
$yp^{(3)}(x)=ce^x\quad ce^x$
$ce^x-4ce^x=e^x$
$-3ce^x=e^x$
$c=\frac13$

$y(x)=c_1 e^{2x}+c_2 e^{-2x}-\frac x4+\frac x4e^{2x}-\frac13 e^x$

$y(0)=0\quad c_1+c_2-\frac13=0$
$y'(x)=2c_1 e^{2x}-2c_3 e^{-2x}-\frac14+\frac14 e^{2x}+\frac x2 e^{2x}-\frac13 e^x$
$y'(0)=2c_1-2c_2-\cancel{\frac14}+\cancel{\frac14}-\frac13=0$
$\cases{c_1=\frac13-c_2\\\frac23-2c_2-2c_2-\frac13=0}\cases{c_1=\frac13-c_2\\-4c_2=-\frac13}\cases{c_1=\frac14\\c_2=\frac12}$
$y(x)=\frac14 e^{2x}+\frac1{12} e^{-2x}-\frac x4+\frac x4 e^{2x} -\frac13 e^x$