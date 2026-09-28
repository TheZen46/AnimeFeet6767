Trovare un polinomio $p(x)$ di grado $\le n-1$ tale che $\underset{i=1,\ldots,n}{p(x)=y_i}$
$P(x)=a_0+a_1x+\dots+a_{n-1}x^{n-1}$
$P(x_i)=y_i=a_0+a_1x+\dots+a_{n-1}x^{n-1}$

$\begin{pmatrix}1&x_1&x_1^2&&x_1^{n-1}\\1&x_2&x_2^2&&x_2^{n-1}\\\\1&x_n&x_n^2&&x_n^{n-1}\end{pmatrix}\begin{pmatrix}a_0\\a_1\\\vert\\a_{n-1}\end{pmatrix}=\begin{pmatrix}y_1\\y_2\\\vert\\y_n\end{pmatrix}$  matrice di **Vandermonde**

$\text{det}V(x_1,\dots,x_n)=\prod\limits_{1\le i<j\le n}(x_j-x_i)$
per induzione su N
\[Foto 2025/12/11]

$Q(x)=(x-x_1)(x-x_2)\dots(x-x_{n-1})=b_0+b_1x+b_2x^2\dots b_{n-2}x^{x^2}+x^{n-1}$
$C_n\rightarrow C_n+b_{n-2}C_{n-1}+\dots+b_1C_2+b_0C_1$