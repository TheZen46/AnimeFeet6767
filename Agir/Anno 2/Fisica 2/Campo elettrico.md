Il campo elettrico è definito da $\displaystyle\vec E=\frac{\vec F}{q_0}\begin{array}{ll}\leftarrow\text{forza di Coulomb risentita}\\\leftarrow\text{carica di prova}\end{array}$
Linee di campo $E$
Positivo:    Escono cariche
Negativo: Entrano cariche

$\boxed{\array{+&&+\\&+&\\+&&+}}\ \ \array{\rightarrow\\\rightarrow\\\rightarrow}\mskip{60mu}\boxed{\array{-&&-\\&-&\\-&&-}}\ \ \array{\leftarrow\\\leftarrow\\\leftarrow}$

$\displaystyle\vec E=\frac{\vec F}{q_0}=K\frac{q_0 q_1}{r^2}\hat r\cdot\frac{1}{q_0}=K\frac{q_1}{r^2}\hat r$

$\displaystyle\frac{\vec F_0}{q_0}=\sum\limits_{i=1}^n\frac{\vec F_{0,i}}{q_0}$
$\displaystyle\mskip{6.5mu}\vec E\mskip{6.5mu}=\sum\limits_{i=1}^n\vec E_{0,i}$

Punto per punto
$\hat E=\hat E_1+\hat E_2$

## Dipolo elettrico
$\vert q_+\vert=\vert q_-\vert\text{ distanti }d$

$\oplus\ \textemdash\ \ominus\leftarrow\text{monodimensionale}$
$Z=\text{distanza dal centro del dipolo}$

$E=E_+-E_-$
$E_+=K\frac{q}{(Z-\frac d2)^2}$
$E_+=K\frac{q}{(Z+\frac d2)^2}$

$\displaystyle E=\underbrace{K\frac{q}{(Z-\frac d2)^2}}_{E_+}-\underbrace{K\frac{q}{(Z+\frac d2)^2}}_{E_-}=Kq\frac{(Z+\frac d2)^2-(Z-\frac d2)^2}{(Z-\frac d2)^2(Z+\frac d2)^2}=Kq\frac{\cancel{Z^2}+\cancel{\frac{d^2}4}+dZ-\cancel{Z^2}-\cancel{\frac{d^2}4}+dZ}{\left(Z^2-\frac{d^2}4\right)^2}=\frac{2Kq\ dZ}{\left(Z^2-\frac{d^2}4\right)^2}=\frac{2Kq\ dZ}{Z^4\left(1-\frac{d^2}{4Z}\right)^2}=\frac{2Kq\ d \bcancel Z}{Z^{\bcancel 4^3} \left(1-\frac{d^2}{4Z}\right)^2}=\frac{2Kqd}{Z^3 \left(1-\frac{d^2}{4Z}\right)^2}\approx\frac{2Kqd}{Z^3}\leftarrow\frac dz \ll 1$

$z\gg d$
$p=qd\leftarrow\text{momento di dipolo elettrico}$


# Anello
$\text{raggio }R\text{ in centro }C$
$\text{densità di carica }\lambda$
$\displaystyle \lambda=\bigr[\frac QL\bigr]$

Particella $P$ in $C$, elevata di $Z$

$\displaystyle \text{Un segmento }ds\text{ ha carica dq (se omogenea). Se l'elemento è sufficientemente piccolo, }|dE|=k\frac{dq}{r^2}\Rightarrow\text{se uniforme }\frac{Q_{tot}}{S_{tot}}$
$dq=\lambda ds$

$\vec {PR}=\sqrt{\vec{PR}^2+\vec {CR}^2}=\sqrt{Z^2+R^2}$
$\displaystyle |k|=k\frac{ds}{r^2}=k\frac{\lambda ds}{R^2+Z^2}$

$\displaystyle dE_z=|dE|\cos\theta=K\lambda\frac{ds}{R^2+Z^2}\cos\theta=K\lambda\frac{ds}{R^2+Z^2}\frac{Z}{\underbrace{\bigl(R^2+Z^2\bigr)^{1/2}}_{r}}=k\lambda\frac{dsZ}{\bigl(R^2+Z^2\bigr)^{3/2}}$
$\displaystyle F_z=\int dE_z=\int\frac{k\ \lambda\ dsZ}{\bigl(R^2+Z^2\bigr)^{3/2}}=\frac{k\ \lambda\ Z}{\bigl(R^2+Z^2\bigr)^{3/2}}\int_0^{\pi/2} ds=\frac{k\ \lambda Z\ 2\pi R}{\bigl(R^2+Z^2\bigr)^{3/2}}$
$\displaystyle \lambda=\frac{Q_{tot}}{2\pi R}\mskip{24mu}2\pi R\lambda=Q_{tot}$
$\displaystyle E_z=K\frac{Q_{tot}z}{\bigl(R^2+Z^2\bigr)^{3/2}}$

$Z\gg R\Rightarrow Z^2\gg R^2$
$R^2+Z^2\simeq Z^2$
$\displaystyle E_z\simeq k\frac{Q_{tot}Z}{\bigl(Z^{\cancel 2})^{\frac 3{\cancel 2}}}=k\frac{Q_{tot}\cancel Z}{Z^{\cancel 3 2}}=k\frac{Q_{tot}}{Z^2}$




Arco di circonferenza di $120\degree$
$Q_{tot}=-Q$
$r$
$\varphi=60\deg$
Campo elettrico nel centro della circonferenza

$ds\to dq$
$\displaystyle |dE|=K\frac{dq}{r^2}=k\frac{\lambda\ ds}{r^2}$
$dq=\lambda\ ds$

$\displaystyle dE_x=|dE|\cos\theta=k\ \lambda\frac{ds}{r^2}\cos\theta$

$r\sin\theta=s\Rightarrow r\theta=s\mskip{12mu}\sin\theta\simeq\theta$
$r\ d\theta=ds$

$\displaystyle dE_x=k\lambda\frac{\cancel r}{r^{\cancel 2}}\cos\theta\ d\theta=\frac{k\lambda}{r}\cos\theta\ d\theta$
$\displaystyle E_x=\int dE_x=\int_{-60\degree}^{60\degree}\frac{k\lambda}{r}\cos\mskip{-2mu}\theta\ d\theta=\frac{k\lambda}{r}\int_{-60\degree}^{60\degree}\cos\mskip{-2mu}\theta\ d\theta=\frac{k\lambda}{r}\Bigl[\sin\mskip{-2mu}\theta\Bigr]_{-60\degree}^{60\degree}=\frac{k\lambda}{r}\ 2\sin\mskip{-2mu}\theta=\frac{k\lambda}{r}\frac{\cancel 2\sqrt 3}{\cancel 2}=\sqrt3\frac{k\lambda}{r}$



# Cerchio
$\text{raggio }R\text{ in centro }C$
$\text{densità di carica }\sigma$
$\displaystyle \sigma=\bigr[\frac Q{L^2}\bigr]=\frac{Q}{A}$

Particella $P$ in $C$, elevata di $Z$

$\displaystyle d\sigma=\frac{dq}{dA}$
$\displaystyle |dE_z|=k\frac{dq\ Z}{\bigl(Z^2+r^2\bigr)^{3/2}}$

$dq=6dA$

Si prende un anello interno al cerchio, lasciando tra i due $dr$ distanza

$A=\pi r^2$
$dA=2r\ \pi\ dr$

$dq=\sigma\ 2\pi r\ di$

$\displaystyle |dE|=k\frac{\sigma\ Z}{\bigl(Z^2+r^2\bigr)^{3/2}}2\pi r\ dr$

$\displaystyle P=\int dE=\int_0^Rk\sigma Z\frac{2\pi r}{\bigl(Z^2+r^2\bigr)^{3/2}}dr=\pi k \sigma Z\int_0^R \frac{2\pi}{\bigl(Z^2+r^2\bigr)^{3/2}}dr$
	$x=r^2+Z^2\Rightarrow r^2=x-Z^2\Rightarrow 2rdr=dx$
	$\displaystyle \int\frac{2\pi}{\bigl(Z^2+r^2\bigr)^{3/2}}dr\Rightarrow\int \frac{1}{x^{3/2}}dx=\Bigl[x^{-1/2}\Bigr]\Rightarrow$
$\displaystyle \pi k \sigma Z$

$E=2\pi k\sigma z\Bigl(\frac{1}{\sqrt{R^2+Z^2}}-\frac1Z\Bigr)=$