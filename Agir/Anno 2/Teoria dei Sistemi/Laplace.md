$\displaystyle f(t)\to\underset{t\to s\in \mathbb{C}}{\mathcal L\left\{f(t)\right\}}\to F(s)$
$\displaystyle\mathcal L\left\{f(t)\right\}=F(s)=\int_{0^-}^\infty f(t)e^{-st}dt$

$\displaystyle s=\sigma+j\omega=\int_{0^-}^{\infty}f(t)e^{-j\omega t}e^{-\sigma t}$

# Proprietà
$\mathcal L\left\{\alpha f+\beta f_2\right\}=\alpha F(s)+\beta F_2(s)$
$\displaystyle\mathcal L\left\{f(t)g(t)\right\}\neq F(s)G(s)$
$\mathcal L\left\{\dot f(t)\right\}=sF(s)-f(0^-)$
$\displaystyle\mathcal L\left\{\int_{0^-}^t f(\tau)d\tau\right\}=\frac1s F(s)$
$\displaystyle\mathcal L\left\{f(t-T)1(t-T)\right\}=e^{-sT}F(s)$
$\displaystyle\mathcal L\left\{e^{at}f(t)\right\}=F(s-a)$
$\displaystyle\mathcal L\left\{tf(t)\right\}=-\frac{d}{ds}F(s)$
$\displaystyle\mathcal L\left\{\delta(t)\right\}=\int_{0^-}^\infty \delta(t)\underbrace{e^{-st}}_{e^0=1}dt=1$
$\displaystyle\mathcal L\left\{1(t)\right\}=\mathcal L\left\{\int_{0^-}^t\delta(\tau)d\tau\right\}=\frac{1}{s}$
$\displaystyle\mathcal L\left\{1\right\}=\frac{1}{s}$
$\displaystyle\mathcal L\left\{t1(t)\right\}=-\frac{d}{dx}\frac1s=\frac1{s^2}$
$\displaystyle\mathcal L\left\{\frac{t^K}{K!}1(t)\right\}=\frac{1}{s^{K+1}}$
$\displaystyle\mathcal L\left\{e^{at}\right\}=\frac1{s-a}$
$\displaystyle\mathcal L\left\{\frac{t^K}{K!}e^{at}\right\}=\frac{1}{(s-a)^{K+1}}$
$\displaystyle\mathcal L\left\{\sin(\omega t)\right\}=\displaystyle\mathcal L\left\{\frac{e^{j\omega t}-e^{-j\omega t}}{2j}\right\}=\frac{1}{2j}\left(\mathcal L\left\{e^{j\omega t}\right\}-\mathcal L\left\{e^{-j\omega t}\right\}\right)=\frac1{2j}\left(\frac{1}{s-j\omega}-\frac{1}{s+j\omega}\right)=\frac{1}{\cancel{2j}}\left(\frac{\cancel s+\cancel j\omega\cancel {-s}+\cancel j\omega}{s^2+\omega^2}\right)=\frac{\omega}{s^2+\omega^2}$
$\displaystyle\mathcal L\left\{\cos(\omega t)\right\}=\frac{s}{s^2+\omega^2}$
$\displaystyle\mathcal L\left\{e^{at}\sin(\omega t)\right\}=\mathcal L\left\{t\left(e^{at}\sin(\omega t)\right)\right\}=-\frac{d}{ds}\mathcal L\left\{e^{at}\sin{\omega t}\right\}=-\frac{d}{ds}\frac{\omega}{(s-a)^2+\omega^2}$
$\displaystyle\mathcal L\left\{e^{at}\cos(\omega t)\right\}=\frac{s-a}{(s-1)^2+\omega^2}$
$\displaystyle \mathcal L\{te^{at}\sin(\omega t)\}=\frac{2(s-a)\omega}{[(s-a)^2+\omega^2]^2}$

$\mathcal L\{\delta_k(t)\}=s^k$
$\mathcal L\{t \}$



$f(t)\to F(s)=\frac ND$
$\displaystyle \mathcal L\{tf(t)\}=-\frac d{ds}\frac ND=-\frac{N'D-D'N}{D^2}$

$f(t)\to F(s)=\frac N{D^\alpha}$
$\displaystyle \mathcal L\{tf(t)\}=-\frac d{ds}\frac N{D^\alpha}=-\frac{N'D^\alpha-\alpha D^{\alpha-1}D'N}{D^{2\alpha}}=-\frac{D^{\alpha-1}(N'D-\alpha D'N)}{D^{2\alpha}}=\frac{\varphi}{D^{\alpha+1}}$
$\mathcal L\{e^{a(t-T)\cos\omega(t-T)1(t-T)}\}=e^{-sT}\frac{s-a}{(s-a)^2+\omega^2}$
$\displaystyle \mathcal L\{1(t-3)+\delta(t)+t1(t)\}=\underbrace{\mathcal L\{1(t-3)\}}_{\ \ 1/s}+\underbrace{\mathcal L\{\delta(t)\}}_{1}+\underbrace{\mathcal L\{t1(t)\}}_{1/s^2}=\frac{se^{-3s}+s^2+1}{s^2}=1+\frac{se^{-3s}+1}{s^2}$
$$\displaystyle \mathcal L\Bigl\{\displaystyle cos(t)\left[1(t)-1(t-\frac\pi2)\right]+\frac{1}{4-\pi}\bigl[1(t-\pi)-1(t-4)\bigr]\Bigl\}=\mathcal L\Bigl\{\displaystyle cos(t)\left[1(t)-1(t-\frac\pi2)\right]\Bigr\}+\frac{1}{4-\pi}\mathcal L\Bigr\{\bigl[1(t-\pi)-1(t-4)\bigr]\Bigl\}=\mathcal L\Bigr\{\cos(t)\Bigl\}-\mathcal L\Bigr\{\cos(t)1(t-\frac\pi2)\Bigl\}+\frac{1}{4-\pi}\mathcal L\Bigr\{1(t-\pi)\Bigl\}-\frac{1}{4-\pi}\mathcal L\Bigr\{1(t-4)\Bigl\}=\frac{s}{\omega^2+s^2}$$