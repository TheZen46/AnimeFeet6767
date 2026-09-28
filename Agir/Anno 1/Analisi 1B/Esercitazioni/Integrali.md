# Primitive
1) Sia $f(x)=\sqrt{4-x^2}$, provare che:
- $F(x)=\frac x2\sqrt{4-x^2}+2\arcsin(\frac x2)$ è primitiva di $f$ su $(-2,2)$
- $G(x)=\frac x2\sqrt{4-x^2}+2\arcsin(\frac x2)-\frac\pi3$

$F'(x)=\frac12\sqrt{4-x^2}+\frac x2 \frac{-2x}{2\sqrt{4-x^2}}+2\frac{\frac12}{\sqrt{1-(\frac x2)^2}}=\frac{4-x^2-x^2+4}{2\sqrt{4-x^2}}=\frac{8-x^2}{2\sqrt{4-x^2}}=\frac{4-x^2}{\sqrt{4-x^2}}=\sqrt{4-x^2}$

$G\cdot F\Rightarrow G$ primitiva
$G(1)=\frac{\sqrt3}2\iff G\text{ passa per }P(1,\frac{\sqrt3}2)$
$\frac12\sqrt3+\underbrace{2\arcsin\frac12}_{\frac\pi6}-\frac\pi3=\frac{\sqrt3}2$

2) Trovare le primitive di $\overset{(x\mapsto \arctan(\sqrt x))}{\arctan(\sqrt x)} \text{ su } [0,+\infty)$

$\int(\small f(g(x))g'(x)\normalsize)dx=\int(f(t))dt$
$\int(\small f(x)g'(x)\normalsize)dx=f(x)g(x)-\int(\small f'(x)g(x)\normalsize)dx$
$dy=f'(x)dx$


$\int(\arctan\sqrt x)dx$

$\frac d {dx}\arctan x=\frac1{1+x^2}$
$arctan$ trigonometrica con buona derivata

Sostituisco $\sqrt x=y\rightarrow x=y^2\rightarrow dx=2ydy$

$\int(\arctan(y)2y)dy=y^2\cdot\arctan y-\int(y^2\frac{1}{1+y^2})dy=y^2\cdot\arctan y-\int(\frac{y^2+1-1}{1+y^2})dy=y^2\cdot\arctan y-\int\overbrace{(\frac{1+y^2}{1+y^2})}^1dy-\int(\frac{-1}{1+y^2})dy=y^2\cdot\arctan y-y+\arctan y+c=(y^2+1)\arctan y-y+c=(x+1)\arctan\sqrt x-\sqrt x+c$

- Trovare quella $(1,\frac\pi2)$
$2\underbrace{\arctan(1)}_{\frac\pi4}-1+c=\frac\pi2$
$c=\frac\pi2-\frac\pi2+1\rightarrow c=1$

$(x+1)\arctan\sqrt x-\sqrt x+1$


3) Calcolare $\displaystyle\int\frac{e^{-x}}{\sqrt{4e^{-x}-e^{-2x}-3}}dx$

$e^{-x}=y$
$-e^-xdx=dy$

$e^{-2x}=(e^{-2})^2=y^2$

$\displaystyle-\int\frac{-e^{-x}}{\sqrt{4e^{-x}-e^{-2x}-3}}dx=-\int\frac{1}{\sqrt{4y-y^2-3}}dy$

$-y^2+4y-3=1-y^2+4y-4=1-(y^2+4y-4)=1-(y-2)^2$

$\displaystyle-\int\frac1{\sqrt{1-(y-2)^2}}dy=-\arcsin(y-2)+c=-\arcsin(e^{-x}-2)+c$


4) Calcolare $\displaystyle\int\frac1{x\sqrt x+2x+2\sqrt x}dx$
$\sqrt x=y$
$\frac{dx}{2\sqrt x}=dy$

$\displaystyle\int\frac{1}{\frac x2+\sqrt x+1}\frac{dx}{2\sqrt x}$

$x=y^2$

$\displaystyle\int\frac1{\frac{y^2}2+y+1}dy=2\int\frac1{y^2+2y+2}dy=2\int\frac1{1+(y+1)^2}=2\arctan(y+1)+c=2\arctan(\sqrt x+1)+c$


5) $\displaystyle\int(e^x\sin x)dx$

$\displaystyle\int(e^x\sin x)dx=e^x\sin-\int(e^x\sin x)dx=e^x\sin x-e^x\cos x-\int(e^x\sin x)dx\rightarrow 2\int(e^x\sin x)dx=e^x\sin x-e^x\cos x+c$

$\displaystyle\int(e^x\sin x)dx=\frac{e^x}2(\sin x-\cos x)+c$


6) Sia $f_a:\mathbb R\rightarrow \mathbb R$    $f_a(x)=\begin{cases}\frac\pi{4x^2+a^2}&\text{ se }x\ge1\\\arctan x&\text{ se }x<1\end{cases}$
- Trova $a$ per una $f_a$ continua
- Primitive di $f_a$ su $(-\infty,1)$
- Primitive di $f_a$ su $(1,+\infty)$

$x\to 1^+\ \ \ \ f_a(x)\overset{x\to 1^+}{\longrightarrow}\frac{\pi}{4+a^2}=f_a(1)$

$x\to 1^-\ \ \ \ f_a(x)\overset{x\to 1^-}{\longrightarrow}\arctan 1=\frac\pi4$

$f_a\text{ continua }\iff a=0$

$\text{per }x\in(-\infty,1),\ f_a(x)=\arctan x\text{ continua}\Rightarrow\text{ammette primitive su }(-\infty,1)\forall a$

$\displaystyle\int\arctan xdx=x\arctan x-\int x\frac1{1+x^2}dx=x\arctan x-\frac12\int 2x\frac1{1+x^2}dx=\arctan(x)-\frac12\log(1+x^2)+c_1$


$f_a(x)=\frac{\pi}{4x^2+a^2}\ \ \forall\ x\in(1,+\infty)$    continua, ammette primitiva

$\displaystyle\int\frac\pi{4x^2+a^2}dx$

$a\ne 0$

$\frac{f'(x)}{1+f(x)}\to \arctan f(x)$

$\displaystyle\frac\pi{a^2}\displaystyle\int\frac1{\frac{4x^2}{a^2}+1}dx=\frac\pi{a^2}\frac a2\displaystyle\int\frac{\frac2a}{(\frac{2x}{a})^2+1}dx=\frac\pi{2a}\arctan(\frac{2x}a)+c_2$

 $a=0$
 
$\displaystyle\int f_a(x)dx=\int\frac\pi{4x^2}dx=-\frac\pi{4x}+c_3$
