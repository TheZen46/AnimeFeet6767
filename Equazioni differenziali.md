$y^{(n)}+a_{n-1}\ y^{(n-1)}+\ldots+a_0\ y=b_m\ u^{(m)}+b_{m-1}\ u^{(m-1)}+\ldots+b_0\ u\m{40}n\ge m$
$\lt{y^{(n)}}+a_{n-1}\ \lt{y^{(n-1)}}+\ldots+a_o\ Y(s)=b_m\ \lt{u^{(m)}}+\ldots+b_0\ U(s)$
	$\lt{\dot y}=sY(s)-y(0^-)$
	$\lt{\ddot y}=s\lt{\dot y}-\dot y(0^-)=s^2Y(s)-sy(0^-)-\dot y(0^-)$
	$\displaystyle \lt{y^{(n)}}=s\lt{y^{(n-1)}}-y^{(n-1)}(0^-)=s^nY(s)-\sum\limits_{k=1}^n s^{n-k}y^{(k-1)}(0^-)$

$m\le n\begin{cases}m<n&\text{strettamente proprio}\\m=n&\text{proprio}\end{cases}$

$\displaystyle Y(s)=\frac{b_m\ s^m+\ldots+b_0}{s^n+a_{n-1}\ s^{n-1}+\ldots+a_0}U(s)+\frac{Z\Bigl(\left.s^x{n-1},y^{(k)}(-^0)\right|_{k=0}^{n-1},\ \left.u^{(k)}(-^0)\right|_{k=0}^{n-1}\Bigr)}{s^n+a_{n-1}\ s^{n-1}+\ldots+a_0}$

# Esempio
Molla-massa
$M\ddot y=-Ky+f$
$\displaystyle \ddot y+\frac KMy=\frac fM$
$f=U$
$\displaystyle \frac KM=a_0\frac1M=b_0$

$\lt{f}=F$
$\displaystyle s^2Y(s)+sy(0^-)-\dot y(o^-)+\frac KM Y(s)=\frac1M F(s)$
$\displaystyle \bigl(s^2+\frac KM\bigr)Y(s)=\frac 1M F(s)+sy(0^-)+\dot y(0^-)$
$\displaystyle Y(s)=\frac{1/M}{s^2+\frac KM}F(x)+\frac{sY(0^-)+y(0^-)}{s^2+\frac KM}$

## Condizioni iniziali
$\cases{y^(0^-)=\dot y(0^-)\\f=\delta(t)}$
$\displaystyle Y(s)=\frac{1/M}{s^2+\frac KM}=\frac1M\ \frac{\sqrt{K/M}\sqrt{M/K}}{s^2+\frac KM}=\sqrt{\frac1{MK}}\ \frac{\sqrt{K/M}}{s^2+\frac KM}$
$\displaystyle y(t)=\sqrt{\frac{1}{MK}}\ \sin\Bigl(\sqrt{\frac KM}t\Bigr)$



$\cases{f=0\\y(0^-)=\overline y\\\dot y(0^-)=0}$
$\displaystyle Y(s)=\frac{s\overline y}{s^2+\frac KM}$
$\displaystyle \ilt{Y(s)}=\overline y\cos\Bigl(\sqrt{\frac KM}t\Bigr)$



$\cases{y(0^-)=\dot y(0^-)=0\\f=\sin\Bigl(\sqrt{\frac KM}t\Bigr)}$
$\displaystyle Y(s)=\frac{1/M\ \sqrt\frac KM}{\bigl(s^2+\frac KM\bigr)^2}$
$4$ poli immaginari, molteplicita $2$