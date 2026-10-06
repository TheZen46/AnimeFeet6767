$\displaystyle F(s)=\frac{s^4}{(s+1)(s+2)(s^2+4)}=1-\frac{3s^3+6s^2+12s+8}{(s+1)(s+2)(s^2+4)}$

$\displaystyle \mathcal L^{-1}\bigl\{F(s)\bigr\}=\delta(t)-\mathcal L^{-1}\biggl\{\frac{3s^3+6s^2+12s+8}{(s+1)(s+2)(s^2+4)}\biggr\}$
	$\displaystyle \frac{A}{s+1}+\frac{B}{s+2}+\frac{2C}{s^2+4}+\frac{sD}{s^2+4}=\frac{A(s+2)(s^2+4)+B(s+1)(s^2+4)+2C(s+1)(s+2)+sD(s+1)(s+2)}{(s+1)(s+2)(s^2+4)}$
		$A(s+2)(s^2+4)+B(s+1)(s^2+4)+2C(s+1)(s+2)+sD(s+1)(s+2)=A(s^3+2s^2+4s+8)+B(s^3+s^2+4s+4)+2C(s^2+3s+2)+D(s^3+3s^2+2s)=$
		$=\underbrace{(A+B+D)}_{3} s^3+\underbrace{(2A+B+2C+3D)}_{6}s^2+\underbrace{(4A+4B+6C+2D)}_{12}s+\underbrace{8A+4B+4C}_{8}$
		