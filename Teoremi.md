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

# Teorema del valore iniziale
$\displaystyle F=\frac ND$
$\displaystyle{\text{poli }D(s)=\begin{cases}\text{tutti }\displaystyle \Re<0&\exists\lim\limits_{t\to\infty}f(t)=0&\lim\limits_{s\to0}s\frac ND&\end{cases}}$