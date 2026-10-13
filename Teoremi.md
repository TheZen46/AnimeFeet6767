# Teorema del valore finale
Se $\exists$ finito $\lim\limits_{t\to\infty}f(t)=L$ allora $\lim\limits_{s\to0}sF(s)=L$
(Non al contrario)
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


$\displaystyle F(s)=\frac{1}{(s+a)(s^2+2bs+c)}$
$\operatorname{roots}\bigl(-a,-b-\sqrt{b^2-4c},-b+\sqrt{b^2-4c}\bigr)$


# Teorema del valore iniziale
