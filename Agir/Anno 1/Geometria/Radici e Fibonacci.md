# Radici
$P(x)$ un polinomio $\in\mathbb K[x]$
$x_0\in\mathbb K$
$x_0$ è radice di $P\ \iff\ (x-x_0)|P$
$x_0$ è una radice di molteplicità $m$ se $(x-x_0)^m|P$

# Fibonacci

$F_n=\#\text{ coppie al mese }n$

$F_{n+2}=F_{n+1}+F_n$

$a_n=\#\text{coppie adulte al mese n}$

$b_n=\#\text{coppie neonate al mese n}$

$\begin{cases}a_{n+1}=a_n+b_n\\b_{n+1}=a_n\end{cases}=\left(\begin{array}{c}1&1\\1&0\end{array}\right)\left(\begin{array}{c}a_n\\b_n\end{array}\right)$

$F_n=a_n+b_n$

$A=\left(\begin{array}{c}1&1\\1&0\end{array}\right)$

$v_n=\left(\begin{array}{c}a_n\\b_n\end{array}\right)$

$v_1=\left(\begin{array}{c}a_1\\b_1\end{array}\right)=\left(\begin{array}{c}0\\1\end{array}\right)$

$v_{n+1}=Av_n\ v_n=a^{n-1}v_1$
$\begin{array}{l}v_2=Av_1\\v_3=AAv_1=A^2v_1\\V_4=A\cdot A^2v_1=A^3v_1\end{array}$

$A=\left(\begin{array}{c}1&1\\1&0\end{array}\right)$

$b_1=\left(\begin{array}{c}1\\0\end{array}\right)$
$b_2=\left(\begin{array}{c}0\\1\end{array}\right)$
Non sono le basi migliori

Basi migliori:
$\begin{array}{l}w_1=\left(\begin{array}{c}\frac{1+sqrt5}{2}\\1\end{array}\right)\\w_2=\left(\begin{array}{c}\frac{1-sqrt5}{2}\\1\end{array}\right)\end{array}\ \ \mathcal B$



$M_\mathcal B(f_A)=P^{-1}AP$

$\begin{array}{c}\mathbb R^2 & \overset A \longrightarrow & \mathbb R^2 \\ \text{id}=C_K\uparrow && \uparrow C_K=\text{id}\\ \mathbb R^2 & \overset {f_A} \longrightarrow & \mathbb R^2 \\ C_\mathcal{B}\downarrow && \downarrow C_\mathcal{B}\\ \mathbb R^2 & \overset{M_\mathcal B(f_A)}\rightarrow & \mathbb R^2\end{array}$




$P=M_\mathcal {BK}(\text{id})=\left(\begin{array}{c}\frac{1+\sqrt5}2&\frac{1-\sqrt5}2\\1&1\end{array}\right)=\left(\begin{array}{c}\varphi_+&\varphi_-\\1&1\end{array}\right)$

$\varphi_+=\frac{1+\sqrt5}2\ \ \ \ \ \ \ \ \varphi_-=\frac{1-\sqrt5}2$

$P^{-1}=\frac1{\sqrt5}\left(\begin{array}{c}1&-\varphi_-\\-1&\varphi_+\end{array}\right)$

$D=\frac1{\sqrt5}\left(\begin{array}{c}1&-\varphi_-\\-1&\varphi_+\end{array}\right)\left(\begin{array}{c}1&1\\1&0\end{array}\right)\left(\begin{array}{c}\varphi_+&\varphi_-\\1&1\end{array}\right)=\frac1{\sqrt5}\left(\begin{array}{c}1&-\varphi_-\\-1&\varphi_+\end{array}\right)\left(\begin{array}{c}\varphi_++1&\varphi_-+1\\\varphi_+&\varphi_-\end{array}\right)=\frac1{\sqrt5}\left(\begin{array}{c}\varphi_++1-\varphi_+\varphi_-&\varphi_-+1-\varphi_-^2\\\varphi_+-1+\varphi_+^2&\varphi_--1+\varphi_+\varphi_-\end{array}\right)$


$\varphi_+\varphi_-=\frac{(1+\sqrt5)(1-\sqrt5)}{4}=\frac{1-5}4=1$
$\varphi_+^2=\frac{1+5+2\sqrt5}4=\frac{4+2(1+\sqrt5)}4=\varphi_++1$
$\varphi_-^2=\frac{1+5-2\sqrt5}4=\frac{4+2(1-\sqrt5)}4=\varphi_++1$

$D=\frac1{\sqrt5}\left(\begin{array}{c}\varphi_++2&0\\0&-\varphi_- -2\end{array}\right)=\frac1{\sqrt5}\left(\begin{array}{c}\frac{1+\sqrt5+4}2&0\\0&\frac{-1+\sqrt5-4}2\end{array}\right)=\left(\begin{array}{c}\frac{5+\sqrt5}{2\sqrt5}&0\\0&\frac{-5+\sqrt5}{2\sqrt5}\end{array}\right)=\left(\begin{array}{c}\frac{1+\sqrt5}2&0\\0&\frac{-5+\sqrt5}2\end{array}\right)=\left(\begin{array}{c}\varphi_+&0\\0&\varphi_-\end{array}\right)$

$D=P^{-1}AP$
$A=PDP^{-1}$
$A^n=P\underbrace{D^n}_{\left(\begin{array}{c}\varphi_+&0\\0&\varphi_-\end{array}\right)}P^{-1}$

$F_n=a_n+b_n\left(\begin{array}{c}a_n\\b_n\end{array}\right)=v_n=A^{n-1}\left(\begin{array}{c}0\\1\end{array}\right)$

$F_n=a_n+b_n=\left(\begin{array}{c}1&1\end{array}\right)\left(\begin{array}{c}a_n\\b_n\end{array}\right)=\left(\begin{array}{c}1&1\end{array}\right)A^{n-1}\left(\begin{array}{c}0\\1\end{array}\right)=\left(\begin{array}{c}1&1\end{array}\right)\left(\begin{array}{c}\varphi_+&\varphi_-\\1&1\end{array}\right)\left(\begin{array}{c}\varphi_+^{n-1}&0\\0&\varphi_-^{n-1}\end{array}\right)\frac1{\sqrt5}\left(\begin{array}{c}1&-\varphi_-\\-1&\varphi_+\end{array}\right)\left(\begin{array}{c}0\\1\end{array}\right)=$
$=\frac1{\sqrt5}\left(\begin{array}{c}\varphi_++1&\varphi_-+1\end{array}\right)\left(\begin{array}{c}\varphi_+^{n-1}&0\\0&\varphi_-^{n-1}\end{array}\right)\left(\begin{array}{c}-\varphi_-\\\varphi_+\end{array}\right)=\frac1{\sqrt5}\left(\begin{array}{c}\varphi_++1&\varphi_-+1\end{array}\right)\left(\begin{array}{c}-\varphi_-&\varphi_+^{n-1}\\\varphi_+&\varphi_-^{n-1}\end{array}\right)=\frac1{\sqrt5}(-\varphi_+^2\varphi_-\varphi_+^{n-1}+\varphi_-^2\varphi_+\varphi_-^{n-1})=\frac1{\sqrt5}(\varphi_+^n-\varphi_-^n)$
$F_n\approx \frac{\varphi_+^n}{\sqrt5}$


$A\in\text{Mat}_n(\mathbb K)$
$A$ è **diagonalizzabile** se $\exists\ P\in GL_n(\mathbb K)$ tale che $P^{-1}AP$ è diagonale

$V$ spazio vettoriale
$f\in\text{End}(v)\ \ \ \ (f:V\rightarrow V\text{ lineare})$
Si dice **diagonalizzabile** se esiste una base $\mathcal B$ di $V$ tale che $M_\mathcal B(f)$ è diagonale
($f$ è diagonalizzabile $\iff\ \forall\ \mathcal B$ base di $V$  $M_\mathcal B(f)$ è diagonalizzabile)