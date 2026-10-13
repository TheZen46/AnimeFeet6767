# Teorema del valore finale
Se $\exists$ finito $\lim\limits_{t\to\infty}f(t)=L$ allora $\lim\limits_{s\to0}sF(s)=L$
## Esempio
### Errato
$\displaystyle F(s)=\frac{1}{s-2}\Rightarrow f(t)=e^{2t}$
$\displaystyle \lim\limits_{s\to0}s\frac{1}{s-2}=0\cancel\Rightarrow \lim\limits_{t\to\infty}=0$

### Corretto
$\displaystyle F(s)=\frac{1}{s+2}\Rightarrow f(t)=e^{-2t}$
$\lim\limits_{t\to\infty}=e^{-2t}=e^{-\infty}=0\Rightarrow\lim\limits_{s\to0}sF(s)=0$

$\displaystyle F(s)=\frac3s\Rightarrow f(t)=3\cdot u(t)$
$\lim\limits_{t\to\infty}f(t)=3\Rightarrow\lim\limits_{s\to0}sF(s)=3$



$\displaystyle F=\frac ND$
$\displaystyle \operatorname{roots}\bigl(D(s)\bigr)=\begin{cases}\text{tutti }\displaystyle \Re<0&\exists\lim\limits_{t\to\infty}f(t)=0&\m{30}&\lim\limits_{s\to0}s\frac ND=0\\\exists\ \Re>0\text{ e/o }\Re=0\ \mu>1&\nexists\text{ finito }\lim\limits_{t\to\infty}f(t)\\\Re<0\text{ e }\Re=0\ \mu=1\ \boxed\star\end{cases}$

$\boxed\star: \begin{cases}\exists\text{ poli }\omega\ne0\\\exists!\text{ polo in }s=0\ \boxed{\boxed\star}\end{cases}$

$\boxed{\boxed\star}:\ \begin{cases}F(s)=\frac{N}{sD}&\lim\limits_{s\to0}\cancel s\frac{N}{\cancel s D}=L\\\operatorname{roots}(D)\Re<0\end{cases}$
Aggiustare $\boxed{\boxed\star}$, non sono condizioni separate


$\displaystyle F(s)=\frac{1}{(s+a)(s^2+2bs+c)}\m{40}a,b,c\in\R$
$\operatorname{roots}\bigl(D(s)\bigr)=\bigl(-a,-b-\sqrt{b^2-4c},-b+\sqrt{b^2-4c}\bigr)$
$a<0\m{20}\cancel{\lim\limits_{t\to\infty}f(t)}$

$\displaystyle a>0:\ \begin{cases}b\ \&\ c<0&\exists\ \lim\\b\ \&\ c>0&\exists\ \lim_{t\to\infty}f(t)=0&\text{perche 3 radici }\Re<0\\b=0,\ c>0&f(t)\text{ limitata, }\nexists\ \lim\limits_{t\to\infty}\\b>0,\ c=0&\exists\ \lim=\frac{1}{2ab}\end{cases}$

$a=0:\ \begin{cases}b\ \&\ c<0&\exists\ \lim=\frac1c\\b=0,\ c>0&\lim\limits_{s\to0}sF(s)=\frac1c\ne\lim\limits_{t\to\infty}f(t)\\b>0,\ c=0&\nexists\ \lim\end{cases}$
# Teorema del valore iniziale
Se $\exists$ finito $\lim\limits_{s\to\infty}sF(s)=L$ allora $f(0^+)=L$
$\N=b_ms^m+\ldots+b_0$
$D=s^n+a_{n-1}s^{n-1}+\ldots+a_0$
$n>m$

$\displaystyle F(s)=\suml_{i=1}^\infty c_i s^{-i}=\suml_{i=1}^\infty\frac{c_i}{s^i}$
$\displaystyle \mathcal L^{-1}=\suml_{i=1}^\infty c_i\frac{t^{i-1}}{(i-1)!}\Leftarrow\text{ McLaurin di }f(t)$
$c_i=f^{i-1}(o^+)$

$\displaystyle F(s)=\frac{1}{s(s+1)}=\frac1{s^2+s}$
$$