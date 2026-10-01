$\displaystyle\frac{2s+1}{(s-2)(s+3)}=\frac{1}{(s-2)}+\frac{1}{(s+3)}$
$\displaystyle\frac{3s+4}{(s-2)(s+3)}=A\frac{1}{(s-2)}+B\frac{1}{(s+3)}$
	$\displaystyle \frac{As+3A+Bs-2B}{(s-2)(s+3)}=\frac{(A+B)s+3A-2B}{(s-2)(s+3)}\cases{A+B=3\\3A-2B=4}=\cases{A=3-B\\3(3-B)-2B=4}=\cases{A=3-B\\5B=5}=\cases{A=2\\B=1}$
$\displaystyle 2\frac{1}{(s-2)}+\frac{1}{(s+3)}$

$\displaystyle F(s)=\frac{1+3e^{-2s}}{(s+2)}=\underbrace{\frac{1}{s+2}}_{\overset{\mathcal L^{-1}}{e^{-2t}}}+\frac{3}{(s+2)}e^{-2s}=e^{-2t}+3\frac{1}{s+2}e^{-2s}=e^{-2t}+3e^{-2(t-2)}1(t-2)$
$\displaystyle \mathcal L^{-1}\{\frac{1}{(s+\alpha)}e^{-\tau s}\}=e^{-\alpha(t-\tau)}u(t-\tau)$

$\displaystyle F(s)=\frac{s^2}{s+1}=s-1+\frac{1}{s+1}=\delta_1(t)-\delta(t)+e^{-t}$

$\displaystyle F(s)=\frac{s^3+^2e^{3s}+1}{s^2+1}$
$\displaystyle f(t)=\mathcal L^{-1}\biggl\{\frac{s^3}{s^2+1}+\frac{s^2e^{-3s}}{s^2+1}+\frac1{s^2+1}\biggr\}=\mathcal L^{-1}\biggl\{s-\frac{s}{s^2+1}+e^{-3s}\Bigl(1-\frac{1}{s^2+1}\Bigr)+\frac{1}{s^2+1}\biggr\}=\delta_1(t)-\cos(t)+\delta(t-3)-\sin(t-3)u(t-3)+\sin(t)$
