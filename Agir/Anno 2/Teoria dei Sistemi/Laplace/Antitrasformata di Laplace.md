$\displaystyle\frac{2s+1}{(s-2)(s+3)}=\frac{1}{(s-2)}+\frac{1}{(s+3)}$
$\displaystyle\frac{3s+4}{(s-2)(s+3)}=A\frac{1}{(s-2)}+B\frac{1}{(s+3)}$
	$\displaystyle \frac{As+3A+Bs-2B}{(s-2)(s+3)}=\frac{(A+B)s+3A-2B}{(s-2)(s+3)}\cases{A+B=3\\3A-2B=4}=\cases{A=3-B\\3(3-B)-2B=4}=\cases{A=3-B\\5B=5}=\cases{A=2\\B=1}$
$\displaystyle 2\frac{1}{(s-2)}+\frac{1}{(s+3)}$

$\displaystyle F(s)=\frac{1+3e^{-2s}}{(s+2)}=\underbrace{\frac{1}{s+2}}_{\overset{\mathcal L^{-1}}{e^{-2t}}}+\frac{3}{(s+2)}e^{-2s}=e^{-2t}+3\frac{1}{s+2}e^{-2s}=e^{-2t}+3e^{-2(t-2)}1(t-2)$
$\displaystyle \mathcal L^{-1}\Bigl\{\frac{1}{(s+\alpha)}e^{-\tau s}\Bigr\}=e^{-\alpha(t-\tau)}u(t-\tau)$

$\displaystyle F(s)=\frac{s^2}{s+1}=s-1+\frac{1}{s+1}=\delta_1(t)-\delta(t)+e^{-t}$

$\displaystyle F(s)=\frac{s^3+^2e^{3s}+1}{s^2+1}$
$\displaystyle f(t)=\mathcal L^{-1}\biggl\{\frac{s^3}{s^2+1}+\frac{s^2e^{-3s}}{s^2+1}+\frac1{s^2+1}\biggr\}=\mathcal L^{-1}\biggl\{s-\frac{s}{s^2+1}+e^{-3s}\Bigl(1-\frac{1}{s^2+1}\Bigr)+\frac{1}{s^2+1}\biggr\}=\delta_1(t)-\cos(t)+\delta(t-3)-\sin(t-3)u(t-3)+\sin(t)$


$\displaystyle F(s)=\frac{}{(s+1)(s+2)\ldots(s+100)}$
$\displaystyle F(s)=\frac{N}{D}=\frac{}{(s-p_1)^{k_1}(s-p_2)^{k_2}\ldots(s-p_{nd})^{k_{nd}}}=\sum\limits_{i=1}^{nd}\sum\limits_{k=1}^{k_i}\frac{C_{ik}}{(s-p_i)^k}=\frac{C_{11}}{(s-p_1)}+\ldots+\frac{C_{1k_1}}{(s-p_1)^{k_1}}+\sum\limits_{i=1}^{nd}\sum\limits_{k=2}^{k_i}\frac{C_{ik}}{(s-p_i)^k}$
$nd=\text{poli distinti}$
$k_i\text{ moltiplicità di }P_i\mskip{30mu}P_i\in\mathbb C$

$\displaystyle (s-p_1)^{k_1}F(s)=\cancel{C_{11}(s-p_1)^{k_{i-1}}}+\ldots+C_{1k_1}+\cancel{(s-p_1)^{k_i}\sum\sum}$


$\displaystyle F(s)=\frac{1}{(s+1)(s+2)(s+3)(s+4)}$
$\displaystyle C_1=\lim\limits_{s\to -p_1}(s-p_1)\ F(s)$

$\displaystyle \frac{A}{s+1}+\frac{B}{s+2}+\frac{C}{s+3}+\frac{D}{s+4}$
$\displaystyle A=\lim\limits_{s\to -1}(s-p_1)\ F(s)=\lim\limits_{s\to -1}\frac{1}{(s+2)(s+3)(s+4)}=\frac{1}{(1)(2)(3)}=\frac16$
$\displaystyle B=\lim\limits_{s\to -2}(s-p_1)\ F(s)=\lim\limits_{s\to -1}\frac{1}{(s+1)(s+3)(s+4)}=\frac{1}{(-1)(1)(2)}=-\frac12$
$\displaystyle C=\lim\limits_{s\to -3}(s-p_1)\ F(s)=\lim\limits_{s\to -1}\frac{1}{(s+1)(s+2)(s+4)}=\frac{1}{(-2)(-1)(1))}=\frac12$
$\displaystyle D=\lim\limits_{s\to -4}(s-p_1)\ F(s)=\lim\limits_{s\to -1}\frac{1}{(s+1)(s+2)(s+4)}=\frac{1}{(-3)(-2)(-1))}=-\frac16$


$\displaystyle F(s)=\frac{1}{(s+1)(s+2)(s^2+4)}$
$\displaystyle \frac{A}{s+1}+\frac{B}{s+2}+\frac{2C}{s^2+4}+\frac{sD}{s^2+4}$

$\displaystyle A=\lim\limits_{s\to -1}(s-p_1)\ F(s)=\lim\limits_{s\to -1}\frac{1}{(s+2)(s^2+4)}=\frac{1}{(1)(5)}=\frac15$
$\displaystyle B=\lim\limits_{s\to -2}(s-p_1)\ F(s)=\lim\limits_{s\to -2}\frac{1}{(s+1)(s^2+4)}=\frac{1}{(-1)(8)}=-\frac18$



$\displaystyle F(s)=\frac{N(s)}{D(s)(s^2+{\omega_0}^2)}=\underbrace{\frac{N}{D\omega_0}}_{G(s)}\frac{\omega_0}{s^2+{\omega_0}^2}=E_G(s)+\overline{C_1}\frac{\omega_0}{s^2+{\omega_0}^2}+\overline{C_2}\frac{s}{s^2+{\omega_0}^2}$
	$\mathcal L{^-1}\Bigl\{E_G(s)\Bigr\}+C_1\sin(\omega_0 t)+C_2\cos(\omega_0 t)$
$\displaystyle F(s)=E_G+C_1\frac{1}{s+j\omega_0}+C_2\frac{1}{s-j\omega_0}$
$\displaystyle C_1=\lim\limits_{s\to-j\omega_0}F(s)=\lim\limits_{s\to-j\omega_0}\cancel{(s+j\omega_0)}\ G(s)\frac{\omega_0}{\cancel{(s+j\omega_0)}(s-j\omega_0)}=\frac{G(-j\omega_0)\cancel{\omega_0}}{-2j\cancel{\omega_0}}=-\frac{G(-j\omega_0)}{2j}$
$\displaystyle C_2=\lim\limits_{s\to j\omega_0}F(s)=\frac{G(j\omega_0)}{2j}$

$G(j\omega_0)=\Re\bigl(G(j\omega_0)\bigr)+j\ \Im\bigl(G(j\omega_0)\bigr)=A+jB$
$\displaystyle \mathcal L^{-1}\Bigl\{F(s)\Bigr\}=\mathcal L^{-1}\Bigl\{E_G\Bigr\}+\left(-\frac{A-jB}{2j}\right)e^{-j\omega_0 t}+\left(-\frac{A-jB}{2j}\right)e^{j\omega_0t}$

$\displaystyle -\frac A{2j}e^{-j\omega_0t}+\frac A{2j}e^{j\omega_0t}+\frac B{2}e^{-j\omega_0t}+\frac B{2}e^{-j\omega_0t}=A\Bigl(\underbrace{\frac{e^{j\omega_0 t}-e^{-j\omega_0 t}}{2j}}_{\sin(\omega_0t)}\Bigr)+B\Bigl(\underbrace{\frac{e^{j\omega_0 t}+e^{-j\omega_0 t}}{2}}_{\cos(\omega_0t)}\Bigr)$
$(s+j\omega_0)(s-j\omega_0)\mathcal L^{-1}\Bigl\{E_G(s)\Bigr\}+\overline {C_1}\sin(\omega_0t)+\overline {C_2}\cos(\omega_0t)\Rightarrow=\mathcal L^{-1}\Bigl\{E_G(s)\Bigr\}+\Re\bigl(G(j\omega_0)\bigr)\sin(\omega_0t)+\Im\bigl(G(j\omega_0)\bigr)\cos(\omega_0t)\Rightarrow$
	$M\sin(\omega_0 t+\varphi)=M\sin(\omega_0t)\cos(\phi)+M\cos(\omega_0t)\sin(\phi)$
		$M\cos\phi=\Re\bigl(G(j\omega_0)\bigr)$
		$M\sin\phi=\Im\bigl(G(j\omega_0)\bigr)$
		$\Re^2+\Im^2=M^2$
	$M=|G(j\omega_0)|$
	$\displaystyle \tan(\phi)=\frac{\Im}{\Re}$
	$\phi=\angle G(j\omega_0)$
$\Rightarrow |G(j\omega_0)|\sin\bigl(\omega_0t+\angle G(j\omega_0)\bigr)$


$\displaystyle F(s)=\frac{1}{(s+1)(s+2)\underset{s=\pm 2j}{(s^2+4)}}=\underbrace{\frac{1}{2(s+1)(s+2)}}_G\frac{2}{s^2+4}$
$\displaystyle G(j\omega_0)=\frac{1}{2(2j+1)(2j+2)}=\frac{1}{2(-4+4j+2j+2)}=\frac{1}{2(-2+6j)}=\frac{1}{-4+12j}\frac{-4-12j}{-4-12j}=\frac{-4-12j}{160}=-\frac{1}{40}-\frac{3}{40}j$
$\displaystyle -\frac{1}{40}\sin(2t)-\frac3{40}\cos(2t)$

$\displaystyle G(2j)=\frac{1}{2(2j+1)(2j+2)}$
	$\displaystyle |G(2j)|=\frac1{2|(2j+1)(2j+2)|}=\frac1{2\sqrt 5\ 2\sqrt 2}=\frac{1}{4\sqrt{10}}$
	$\angle G(2j)=0-\angle\bigl(2(2j+1)(2j+2)\bigr)=\bigl(0+\arctan2+\frac\pi4\bigr)$
$\displaystyle G(2j)=\frac{1}{4\sqrt{10}}\sin(2t-\frac\pi4-\arctan2)$




$\displaystyle F(s)=$