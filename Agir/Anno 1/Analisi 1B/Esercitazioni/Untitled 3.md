$\displaystyle\int_{-\ln10}^{-\ln2}\frac{e^x}{e^2x}-1dx$
$e^x=y$
$e^xdx=dy$

$x=-\ln10\to y=e^{-\ln10}=e^{\ln10^{-1}}=\frac1{10}$

$\displaystyle\int_{\frac1{10}}^{\frac12}\frac1{y^2-1}dy$

$\displaystyle\frac1{y^2-1}=\frac1{(y+1)(y-1)}$
Cerchiamo $A,B$ tale che: $\frac A{y+1}+\frac B{y-1}$
$\displaystyle\frac{A(y-1)+B(y+1)}{y^2-1}=\frac{(A+B)y+(B-A)}{y^2-1}\begin{cases}A+B=0&2A+1=0&A=-\frac12\\B-A=1&B=A+1&B=\frac12\end{cases}$

$\displaystyle\int_{\frac1{10}}^{\frac12}\frac{-\frac12}{y+1}+\frac{\frac12}{y-1}dy=-\frac12\left[\ln|y+1|\right]_\frac1{10}^\frac12+\frac12\left[\ln|y-1|\right]_\frac1{10}^\frac12=-\frac12(\ln\frac32-\ln\frac{11}{10}-\ln\frac{1}2\ln\frac9{10})=-\frac12(\ln3-\cancel{\ln2}-\ln{11}+\cancel{\ln{10}}+\cancel{\ln{2}}+2\ln3-\cancel{\ln{10}})$





$\displaystyle\int_0^1\frac{x^2+4x+5}{4x^2+4x-1}dx$

$x^2+4x+5=\frac14(4x^2+4x+1)$
$x^2+4x+5-\frac14(4x^2+4x+1)=3x+\frac{19}4$

$\displaystyle\int_0^1\frac14dx+\frac14\int_0^1\frac{12x+19}{4x^2+4x+1}$

$\displaystyle\frac{12x+19}{(2x+1)^2}\overset?=\frac{A}{2x+1}+\frac B{(2x+1)^2}=\frac{A(2x+1)+B}{(2x+1)^2}=\frac{2Ax+(A+B)}{(2x+1)^2}\begin{cases}2A=12&A=6\\A+B=19&B=13\end{cases}$

$\displaystyle\left[\frac x4\right]_0^1+\overbrace{\frac34}^{\frac14\cdot 3}\int_0^1\frac{\overbrace 2^{6\cdot\frac13}}{2x+1}dx+\frac14\int_0^1\frac{13}{(2x+1)^2}dx=\frac14+\frac34\left[\ln|2x+1|\right]_0^1+\frac{13}8\int_0^1\frac2{(2x+1)^2}dx=\frac14+\frac34\ln3+\frac{13}8\left[-\frac1{2x+1}\right]_0^1=\frac14+\frac34\ln3+\frac{13}8(-\frac13+1)=\frac43+\frac34\ln3$





Area di $\displaystyle\left\{(x,y)\in\mathbb R^2;\ x\in\left[\frac34\pi,\frac32\pi\right]\ \ 0\le y\le \cos^2x\right\}$

$\displaystyle\text{Area}(\mathbb R)=\int_{\frac34\pi}^{\frac32\pi}\cos^2(x)dx$

$\cos(2x)=\cos^2x-\sin^2x=2\cos^2x-1$
$\cos^2(x)=\frac{\cos(2x)+1}2$

$\displaystyle\int_{\frac34\pi}^{\frac32\pi}\frac{\cos(2x)+1}2dx=\frac14\int_{\frac34\pi}^{\frac32\pi}\overbrace2^{\text{perché composta}}\cos(2x)dx+\frac12\int_{\frac34\pi}^{\frac32\pi}dx$

$\displaystyle\frac14\left[\sin(2x)\right]_{\frac34\pi}^{\frac32\pi}+\frac12\left[x\right]_{\frac34\pi}^{\frac32\pi}=\frac14(\sin(3\pi)-\sin(\frac32\pi))+\frac12(\frac32\pi-\frac34\pi)=\frac14+\frac38\pi$





Area di $B=\left\{(x,y)\in\mathbb R^2:x^2-1\le y\le \arcsin(1-|x|)\right\}$

$\displaystyle\text{Area}(B)=\int_{-1}^1\left(\arcsin(1-|x|)-(x^2-1)\right)dx=2\int_0^1\left(\arcsin(1-x)-x^2+1\right)dx=2\int_0^1\arcsin(1-x)-2\int_0^1x^2dx+2\int_0^1dx$

$1-x=y$
$-dx=dy$

$\displaystyle-2\int_0^1\arcsin(y)dy-2\left[\frac{x^3}3\right]_0^1+2\left[x\right]_0^1=2\int_0^`\arcsin(y)dy-\frac23+2=2\left[y\arcsin(y)\right]_0^1-2\int_0^1y\frac{1}{\sqrt{1-y^2}}dy+\frac43$

$1-y^2=t$
$-2ydy=dt$

$\displaystyle2\left(\arcsin(1)+\int_1^0\frac1{\sqrt t}dt+\frac43\right)=2\frac\pi2+\left[\frac{t^{\frac12}}{\frac12}\right]_1^0+\frac43-2=\pi-\frac23$





$\displaystyle\int_{-1}^1\sqrt{1-x^2}dx=\text{Area sottesa}f(x)=\sqrt{1-x^2}$

$y=\sqrt{1-x^2}$
$y^2=1-x^2$
$$