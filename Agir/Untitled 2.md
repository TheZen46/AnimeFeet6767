$\cases{y'(x)=xe^{-y(x)}\\y(0)=1}$

- $\exists!$ soluzione su un intorno di $x_0=0$
L'equazione differenziale è a variabili separabili $\Rightarrow y'(x)=f(x)\cdot g(y(x))$
$f(x)=x \in c^\infty(\mathbb R)$ quindi in particolare $c^0$
$g(x)=e^{-z}\in c^\infty(\mathbb R)$ quindi in particolare $c^1$
$\Rightarrow\exists!$

- Polinomio di Taylor della soluzione di grado $2$ e centro $0$
$\displaystyle P(x)=\underbrace{y(0)}_{1}+\underbrace{y'(0)}_{0} x+\frac{\overbrace{y''(0)}^{1/e}}{2}x^2=1+\frac1{2e}x^2$
	$y''(x)=e^{-y(x)}-xe^{-y(x)}y'(x)\Rightarrow y''(0)=e^{y(0)}=\frac1e$
La funzione ha un minimo in $0$

- Risolvi e dominio soluzione
$\displaystyle\int_0^x y'(t)e^{y(t)}dt=\int_0^x tdt$
$\displaystyle\int_{y(0)}^{y(x)}e^zdz=\frac{x^2}2$

$e^{y(x)}-e^{y(0)}=\frac{x^2}2\Rightarrow e^{y(x)}=e+\frac{x^2}2$
$y(x)=\ln(e+\frac{x^2}2$ su $\mathbb R$




$\cases{y'(t)=\frac{y^2(t)+y(t)}t\\y(1)=2}$
- Provare l'$\exists!$ soluzione in un intorno di $t_0=1$
L'equazione differenziale è a variabili separabili
$f(t)=\frac1t\in c^\infty\left((0,\infty)\right)$
$g(z)=z^2+z\in c^\infty(\mathbb R)$ in particolare $c^1(\mathbb R)$
$\Rightarrow\exists!$
(Cerchiamo soluzioni al massimo su $(0,\infty)$)

- Soluzioni
$\displaystyle\int_1^t\frac{y'(z)}{y(z)^2+y(z)}dz=\int_1^t\frac{dz}{z}$
$\displaystyle\int_2^{y(t)}\frac{1}{x^2+x}dx=\ln(t)$ poiché $t\in(0,\infty)\quad |t|=t$
$\frac{1}{x^2+x}=\frac Ax+\frac B{x+1}=\frac{Ax+A+Bx}{x^2(x+1)}$
$\cases{A+B=0\\ A=1}\cases{B=-1\\A=1}$
$\displaystyle\int_2^{y(t)}\frac{1}{x^2+x}dx=\int_2^{y(t)}\frac1xdx-\int_2^{y(t)}\frac 1{x+1}dx=\ln(y(t))-\ln(2)-\ln\left(y(t)+1\right)+\ln(3)=\ln(\frac{y(t)}{y(t)+1})-\ln\frac23$
$\ln\frac{y(t)}{y(t)+1}-\ln\frac23=\ln t\Rightarrow\ln\frac{y(t)}{y(t)+1}=\ln\frac{2t}3$
$\frac{y(t)}{y(t)+1}=\frac{2t}3\Rightarrow 3y(t)=2ty(t)+2t\Rightarrow (3-2t)y(t)=2t$
Problema in $t=\frac32$
$(0,\frac32)$ dominio massimale

- Calcola $\displaystyle\lim\limits_{t\to1^=}\frac{y(t)-2}{t-1}$
$\displaystyle\frac{\frac{2t}{3-2t}-2}{t-1}=\frac{2t-4+4t}{(3-2t)(t-1)}=6\frac{\cancel{t-1}}{(3-2t)\cancel{(t-1)}}\overset{t\to1^+}{\Rightarrow}6$
Senza calcolare
	$\displaystyle\lim\limits_{t\to1^+}\frac{y'(t)}1$
	$\displaystyle\lim\limits_{t\to1^+}\frac{y^2(t)+y(t)}{t}=y(1^2)+y(1)=6$



$y'''-3y''+3y'-y=0$
	$\array{y\to y_1\\y'\to y_2\\y''\to y_3\\y'''\to y_3'}$
$\cases{y_1'=y_2\\y_2'=y_3\\y_3'-3y_3+3y_2-y_1=0\\y_3'=y_1-3y_2+3y_3}$

$\underline y'=Ay$
$A=\pmatrix{0&1&0\\0&0&1\\1&-3&3}$
$P(\lambda)=\operatorname{det}(A-\lambda I)=\operatorname{det}\pmatrix{-\lambda&1&0\\0&-\lambda&1\\1&-3&3-\lambda}=-\lambda\operatorname{det}\pmatrix{-\lambda&1\\-3&3-\lambda}\underbrace{-\operatorname{det}\pmatrix{0&1\\1&3-\lambda}}_{+1}=-\lambda(-3\lambda+\lambda^2+3)+1=-\lambda^2+3\lambda^2-3\lambda+1=-(\lambda-1)^3$
$\lambda=1\text{ autovalore triplo}$

$y(x)=e^x(c_1+c_2x+c_3x^2)$

Autovettore
$A\underline v=\underline v\Rightarrow\pmatrix{0&1&0\\0&0&1\\1&-3&3}\pmatrix{v_1\\v_2\\v_3}=\pmatrix{v_1\\v_2\\v_3}\Rightarrow\cases{v_2=v_1\\v_3=v_2\\v_1-3v_2+3v_3=v_3}\quad\cases{v_2=v_1\\v_3=v_2\\\cancel{v_1-3v_1+3v_1-v_1}}\Rightarrow\pmatrix{1\\1\\1}$

Autovettori generalizzati
$(A-I)\underline w=\underline v\Rightarrow\pmatrix{-1&1&0\\0&-1&1\\1&-3&3}\pmatrix{w_1\\w_2\\w_3}=\pmatrix{1\\1\\1}\Rightarrow\cases{-w_1+w_2=1\\-w_2+w_3=1\\w_1-3w_2+2w_3=1}\quad\cases{w_2=w_1+1\\w_3=w_2+2\\\cancel{w_1-3w_1-3+2w_24=1}}\Rightarrow\pmatrix{1\\2\\3}$

Altro autovettore generalizzato
$(A-I)\underline u=\underline w\Rightarrow\pmatrix{-1&1&0\\0&-1&1\\1&-3&3}\pmatrix{w_1\\w_2\\w_3}=\pmatrix{1\\2\\3}\Rightarrow\cases{-u_1+u_2=1\\-u_2+u_3=2\\u_1-uw_2+uw_3=3}\quad\cases{u_2=u_1+1\\u_3=u_2+3}\Rightarrow\pmatrix{1\\2\\4}$

$\underline y=e^x\left(c_1\pmatrix{1\\1\\1}+c_2x\pmatrix{1\\2\\3}+c_3\frac{x^2}{2}\pmatrix{1\\2\\4}\right)$



Verifica se $y(t)=\cos(3t)$ è soluzione di $y'''-3y''+3y'-y=18\sin(3t)+26\cos(3t)$
$\array{y(t)=\cos(3t)\\y'(t)=-3\sin(3t)\\y''(t)=-9\cos(3t)\\y'''(t)=27\sin(3t)}$
$(27\sin(3t))-3(-9\cos(3t))+3(-3\sin(3t))-\cos(3t)=18\sin(3t)+26\cos(3t)\ \checkmark$

$\cases{y_1'=y_1+\alpha y_2\\y_2-=y_1-3y_2}\quad$ Stabilire per quali $\alpha\in\mathbb R$ le soluzioni $\to0$ per $t\to+\infty$

$\pmatrix{1&\alpha\\1&-3}$
$P(\lambda)=\operatorname{det}\pmatrix{1&\alpha\\1&-3}=(1-\lambda)(-3-\lambda)-\alpha=\lambda^2+2\lambda-(3+\alpha)$
$\displaystyle\lambda_{1,2}=\frac{-2\pm\sqrt{4+4(3+\alpha)}}{2}=-1\pm\sqrt{1+3+\alpha}=-1\pm\sqrt{4+\alpha}$

Se $\alpha\ge-4$ allora autovalori $\Re$
$\lambda_{1,2}=-1\pm\sqrt{4+\alpha}$
$-1+\sqrt{4+\alpha}\overset?>0\qquad\alpha>-3$
Per avere autovalori negativi dobbiamo richiedere $\alpha\le-3\Rightarrow -4\le\alpha\le-3$

Se $\alpha<-4$ allora autovalori complessi coniugati
$\lambda_\pm=-1\pm i\sqrt{-\alpha-4}$
$\Re(\lambda_\pm)=-1<0$
Le soluzioni $\overset{t\to+\infty}\rightarrow0\text{ se }\alpha<-3$


Se $\alpha=-3$
$\lambda_{1,2}=-1\pm1\Rightarrow\lambda_{1,2}=-2,0$ autovalori regolari
No asintoticamente stabile, si stabile
