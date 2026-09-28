## Eigenvalue
Definizione
$f\in\text{End}(V)$
$\lambda\in\mathbb K$ è un **autovalore** di $f$ se $\exists\ v\in V\ \ v\ne0$ tale che $f(v)=\lambda\cdot v$    **eigenvalue**

$v\in V\ \ v\ne0$ è un **autovettore** di $f$ se $\exists\ \lambda\in\mathbb K$ tale che $f(v)=\lambda v$    **eigenvector**

$\mathbb K^n\overset A\longrightarrow \mathbb K^n\ \ \ \ A\in\text{Mat}_n(\mathbb K)$
Fissato $\lambda$, esiste un vettore che moltiplicato per $A$ diventa il suo coefficiente?

Eg. $Av=5v$
5 è un autovalore?

5 è un autovalore se $\exists v\in V\ \ v\ne0\ \ \ \ Av=5v$

$f\in\text{End}(v)$
$\text{Spec}(f)=\{\lambda\in\mathbb K|\lambda\text{ è un autovalore di }f\}$   **spettro** di $f$

$\begin{array}{l}\exists v\in V&v\ne0&Av=5v\\&&Av-5v=0\\&&(A-5I_n)v=0\end{array}$

$\lambda$ è un autovalore $\iff\ \text{rk}(A-\lambda I_n)<n\ \iff\ \det(A-\lambda I_n)=0$

### Applicato
$A=\left(\begin{array}{c}5&2\\2&2\end{array}\right)$
$\det(A-I_2)=0$
$\det\left|\left(\begin{array}{c}5&2\\2&2\end{array}\right)-\left(\begin{array}{c}\lambda&0\\0&\lambda\end{array}\right)\right|=\left|\left(\begin{array}{c}5-\lambda&2\\2&2\lambda\end{array}\right)\right|=(5-\lambda)(2-\lambda)-4=\lambda^2-7\lambda+10-4=\lambda^2-7\lambda+6=(\lambda-1)(\lambda-6)$
$P_f$

Definizione
$f\in\text{End}(V)$
$\underbrace{P_f(\lambda)=\det(\lambda I-n-A)}_{\text{polinomio caratteristico di }f(\text{e di }A)}$ dove A è una matrice che rappresenta l'applicazione 



$f=\text{End}(v)$
$\mathcal B=v_1,\ldots,v_n$

$M_\mathcal B(f)=\left(\begin{array}{c}d_1&&0\\&\diagdown&\\0&&d_n\end{array}\right)$

$f(v_1)=$

$\forall\ v\in V$
$M_\mathcal B(f)=\left(\begin{array}{c}d_1&&0\\&\diagdown&\\0&&d_n\end{array}\right)C_\mathcal B(v)=C_\mathcal B(f(v))$
$M_\mathcal B(f)=\left(\begin{array}{c}d_1&&0\\&\diagdown&\\0&&d_n\end{array}\right)\underbrace{C_\mathcal B(v_1)}_{\left(\begin{array}{c}1\\0\\\vdots\\0\end{array}\right)=\left(\begin{array}{c}d_1\\0\\\vdots\\0\end{array}\right)}=C_\mathcal B(f(v_1))$
$v_1=\underset1{a_1v_1}+\underset0{a_2v_2}+\ldots+\underset0{a_nv_n}$

Quindi $v_1,\ldots,v_n$ sono autovettori e $d_1,\ldots,d_n$ sono autovalori


Sia $\lambda\in\text{Spec}(f)$
$V_\lambda=\{v\in V\ |\ f(v)=\lambda v\}$
$V_\lambda$ è un sottospazio vettoriale di $V$

$V_\lambda=\ker(f-\lambda\ \text{id})$
$0\in V_\lambda$ Siano $r_1,r_2\in\mathbb K$ e $v_1,v_2\in V_\lambda$

$r_1 v_1+r_2v_2\overset?\in V_\lambda$
$f(r_1 v_1+r_2v_2)=r_1f(v_1)+r_2f(v_2)=r_1\lambda v_1+r_2\lambda v_2=\lambda(r_1 v_1+r_2v_2)$

**autospazio** relativo a $\lambda$ (eigenspace)



Siano $\lambda,\mu\in\text{Spec}(f)\ \ \lambda\ne\mu$
Allora $V_\lambda\cap V_\mu=\{0\}$

$f$ è diagonalizzabile $\iff\ \exists\ \mathcal B$ base di autovettori $\iff\ V=V_{\lambda_1}\oplus\ldots\oplus V_{\lambda_r}$



$v_1\ldots,v_n$ base
$f(v_i)=\lambda_i v_i$
allora
$M_\mathcal B(f)=\left(\begin{array}{c}\lambda_1&&0\\&\diagdown&\\0&&\lambda_n\end{array}\right)$

$W_J=<v_{i_1},\ldots,v_{i_j}>\ \ \longleftarrow$ elementi di $\mathcal B$ autovettori relativi
$W_J\subseteq V_{\lambda_j}$



$\mathcal B$ genera $V\Rightarrow W_i+\ldots+W_J=V$

$W_i+\ldots+W_J\subseteq V$
$W_1\oplus\ldots\oplus W_r=V$
- $W_1+\ldots+W_r=V$
- $\forall\ i=1,\ r\ \ \ \ W_i\cap(W_1+\ldots+W_{i-1}+W_{i+1}+\ldots+W_r)=\{0\}$

$W_1\oplus\ldots\oplus W_r=V$
$\forall\ v\in V\ \exists!\ v_i\in W_i$ tali che $v=v_1+\ldots+v_r$
Equivalentemente $\forall\ \mathcal B_1,\ldots,\mathcal B_r$ base di $W_1,\ldots,W_r$
l'unione $\bigcup\limits_{i=1}^r \mathcal B_i$ è una base di $V$


Verifichiamo che un autospazio ha intersezione 0 con un altro
$V_{\lambda_1},\ldots,V_{\lambda_r}$ autospazi
Mostriamo per induzione che
$(V_{\lambda_1},\ldots,V_{\lambda_K})\cap V_{\lambda_{K+1}}=\{0\}$

$K=1\ \ \ \ V_{\lambda_1}\cap V_{\lambda_2}=\{0\}$

Passo induttivo, assumiamo che $V_{\lambda_1}+\ldots+V_{\lambda_K}=V_{\lambda_1}\oplus\ldots\oplus V_{\lambda_K}$
Devo mostrare che $(V_{\lambda_1}+\ldots+V_{\lambda_K})\cap V_{\lambda_{K+1}}=\{0\}$
Sia $v\in(V_{\lambda_1}+\ldots+V_{\lambda_K})\cap V_{\lambda_{K+1}}$

$f(v)=\lambda_{K+1}v$
$v=W_1+\ldots+W_K$
$W_i\in V_{\lambda_i}$

$f(v)=\lambda_{K+1}v = f(\sum\limits_{i=1}^K f(W_i)=\sum\limits_{i=1}^K \lambda_i W_i$

$\lambda_{K+1}v=\sum\limits_{i=1}^K \lambda_{K+1}v$
$\forall\  i=1,k\Rightarrow \lambda_iW_i=\lambda_{K+1}W_i\Rightarrow W_i=0$


$\left(\begin{array}{c}2&-1\\0&2\end{array}\right)$ non è diagonalizzabile
Esistono 2 autovettori indipendenti?
Per trovare gli autovettori prima cerchiamo gli autovalori
$P_i=\left|\begin{array}{c}\lambda-2&-1\\0&\lambda-2\end{array}\right|=(\lambda-2)^2$
$\text{Spec}(A)\{2\}$
$\left(\begin{array}{c}1\\0\end{array}\right)\in V_{\lambda=2}$

$\left(\begin{array}{c}2&-1\\0&2\end{array}\right)\left(\begin{array}{c}x\\y\end{array}\right)=\left(\begin{array}{c}2x\\2y\end{array}\right)$

$\left(\begin{array}{c}0&-1\\0&0\end{array}\right)\left(\begin{array}{c}x\\y\end{array}\right)=\left(\begin{array}{c}0\\0\end{array}\right)$

$\dim\ker\left(\begin{array}{c}0&-1\\0&0\end{array}\right)=1\Rightarrow V_\lambda=2=<\left(\begin{array}{c}1\\0\end{array}\right)>$



Matrice per rotazione $90\deg$ in senso antiorario su $R^2$
$\left(\begin{array}{c}0&-1\\1&0\end{array}\right)$
$P(\lambda)=\left|\begin{array}{c}\lambda&1\\-1&\lambda\end{array}\right|=\lambda^2+1$

$\mathbb C^2\overset f \rightarrow \mathbb C^2$   $\mathbb K=\mathbb C$

$\begin{pmatrix}i&1\\-1&i\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}\ \ \ \ <\begin{pmatrix}-1\\i\end{pmatrix}>$

$i(-1)+1\cdot i=0$

$\begin{pmatrix}-i&1\\-1&-i\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}\ \ \ \ <\begin{pmatrix}1\\i\end{pmatrix}>$



$f:V\rightarrow V$ lineare
- (i) $f$ è diagonalizzabile
- (ii) $\exists$ una base $\mathcal B$ di $V$ di autovettori
- (iii) $\bigoplus\limits_{\lambda\in\text{Spec}(f)}V_\lambda$

Se $P_f(\lambda)$ ha $n$ radici distinte in $\mathbb K$ allora $f$ è diagonalizzabile
$n=\dim V$

$\begin{array}{c}\lambda_1&\ldots&\lambda_n\\\updownarrow&&\updownarrow\\v_1&&v_n\end{array}$

$v_1,\ldots,v_n$ sono indipendenti
$v_1,\ldots,v_n$ sono una base
("diagonalizzabile" = "semplice")

### Osservazione
Se $\lambda$ è una radice multipla di un polinomio $P$, allora $\lambda$ è una radice di $P'$

$\lambda\in\text{Spec}(f)$
$m_a(\lambda)$ "Molteplicità algebrica"
molteplicità di $\lambda$ come radice di $P_f$

$m_a(\lambda)$ "Molteplicità geometrica" = $\dim V_\lambda$
$\sum\limits_{\lambda\in\text{Spec}(f)}m_a(\lambda)\ \le n\ \ (=n\text{ se }\mathbb K=\mathbb C)$
$P_f(x)=(x-\lambda_1)^{m_a(\lambda_1)}\dots(x-\lambda_r)^{m_a(\lambda_r)}(\ \ P_1\ \ )^{e_1}(\ \ P_2\ \ )^{e_2}\dots$


$1\le m_g(\lambda)\le m_a(\lambda)$


Siano $v_1,\ldots,v_r$ degli autovettori indipendenti e relativi ad uno stesso autovettore $\lambda$

Completiamo $v_1,\ldots,v_r$ di una base di $V$

$A=M_\mathcal B(f)$

### Polinomio caratteristico
$P_f(x)=\det(XI_n-A)$

$\overset{i=1,\ldots,r}{f(v_i)=\lambda v_i}$

\[Foto 4/12/25]

$C_\mathcal B(f(v))=AC_\mathcal B(v)$

$C_\mathcal B(\lambda v_i)=AC_\mathcal B(v_i)$

$v_i=0\cdot v_1+0\cdot v_2+\ldots+1\cdot v_i+0\cdot v_{i+1}+\ldots+0\cdot v_r$

$\det(XI_n-A)=\left|\begin{array}{c|c}  {\begin{array}{c}x-\lambda&&0\\&\diagdown&\\0&&x-\lambda\end{array}}  &-\ast\\\hline\\0&XI_{n-r}-B\vphantom{MMMM}\end{array}\right|=(X-\lambda)^r\overbrace{P_B(x)}^{\det(XI_{n=r}=B)}$

$f$ è diagonalizzabile se e solo se
- 1) $\sum\limits_{\lambda\in\text{Spec}(f)}m_a(\lambda)=n$ (sempre vera su $\mathbb C$)
- 2) $\forall\ \lambda\in\text{Spec}(f)\ \ m_g(\lambda)=m_a(\lambda)$

$f$ diagonalizzabile $\iff\ V=\bigoplus\limits_{\lambda\in\text{Spec}(f)}V_\lambda\iff\sum\limits_{\lambda\in\text{Spec}(f)}m_g(\lambda)=n$
$\sum m_g(\lambda)\le \sum m_a(\lambda) \le n$

$f$ diagonalizzabile se e solo se valgono entrambi gli "$=$" e $\sum\limits_\lambda m_g(\lambda)=\sum\limits_\lambda m_a(\lambda)\ \ \iff\ \ \forall\ \lambda\ \ m_g(\lambda)=m_a(\lambda)$ perché $m_g(\lambda)\le m_a(\lambda)$


$f:\mathbb R^3\rightarrow \mathbb R^3$
$f(x,y,z)\rightarrow(x,y,-2y-z)$

$M_{\text{Canonica}}(f)=\begin{pmatrix}1&0&0\\0&1&0\\0&-2&1\end{pmatrix}$
$P_f(\lambda)=\det(\lambda\underbrace{I_3}_{\tiny\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\normalsize}-A)=\left|\begin{array}{c}\lambda-1&0&0\\0&\lambda-1&0\\0&2&\lambda+1\end{array}\right|=(\lambda-1)^2(\lambda+1)$

$\text{Spec}(f)=\{1,-1\}$  $\begin{array}{c}m_a(1)=2\\m_a(-1)=1\end{array}$

$m_g(-1)=1$

$f(v)=v\begin{pmatrix}1&0&0\\0&1&0\\0&-2&1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}x\\y\\z\end{pmatrix}$

$\begin{pmatrix}0&0&0\\0&0&0\\0&2&2\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}x\\y\\z\end{pmatrix}$

$m_g(\lambda)=n-\text{rk}(\lambda I_n-A)$
$m_g(1)=2$

$A\sim\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix}\sim\begin{pmatrix}-1&0&0\\0&1&0\\0&0&1\end{pmatrix}\sim\begin{pmatrix}1&0&0\\0&-1&0\\0&0&1\end{pmatrix}$

$V_{\lambda=-1}=\ker\begin{pmatrix}-2&0&0\\0&-2&0\\0&-2&0\end{pmatrix}=<\begin{pmatrix}0\\0\\1\end{pmatrix}>0$
$V_{\lambda=1}=\ker\begin{pmatrix}0&0&0\\0&0&0\\0&2&2\end{pmatrix}=<\begin{pmatrix}-1\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\-1\end{pmatrix}>$

$f(v)=v$     $(Id-f)(v)=0$
$Av=v$       $(I_3-A)v=0$

$M_\mathcal B(f)=\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix}$

$C_\mathcal B(f(v))=M_\mathcal B(f)\cdot C_\mathcal B(v)$

$\underbrace{C_\mathcal B(f\begin{pmatrix}1\\0\\0\end{pmatrix})}_{C_\mathcal B\begin{pmatrix}1\\0\\0\end{pmatrix}}=MC_\mathcal B\Bigg(\begin{pmatrix}1\\0\\0\end{pmatrix}\Bigg)$

$C_\mathcal B\begin{pmatrix}1\\0\\0\end{pmatrix}=\begin{pmatrix}1\\0\\0\end{pmatrix}$



$A=\begin{pmatrix}1&0&1\\0&2&1\\-1&0&3\end{pmatrix}$

$P_A=\left|\begin{array}{c}x-1&0&-1\\0&x-2&-1\\-1&0&x-3\end{array}\right|=(x-1)(x-2)(x-3)+x-2=(x-2)(x^2-4x+3+1)=(x-2)(x^2-4x+4)=(x-2)^3$
$\text{Spac}(A)=\{2\}$  $m_a(2)=3$

$\begin{pmatrix}1&0&-1\\0&0&1\\1&0&-1\end{pmatrix}$  $m_g(2)=1$

$A$ non è diagonalizzabile

Blocco di Jordan



Sia $A$ una matrice simmetrica a coefficienti $\mathbb R$  $A^T=A$

$P_A$ ha solo radici reali

$\mathbb C^n\mapsto \mathbb C^n$
$v\mapsto Av$
Sia $\lambda\in\text{Spec}_\mathbb C(A)$

$P_A(x)=(x-\lambda_1)\ldots(x-\lambda_n)$
$\lambda_i\in\mathbb C$
$\exists\ \underset{\ne0}v\in\mathbb C^n$ tale che $Av=\lambda v$

$v^TA^T=v^TA=\lambda v^T$

$\overline{v^TA}=\overline v^T \overline A=\overline v^T A\overline\lambda \overline v^T$

$\overline vTÂv=\overline v^t(Av)=\lambda\overline v^Tv=(\overline v^TA)v=\overline\lambda\overline v^Tv$
$(\lambda-\overline\lambda)\overline v^Tv=0\Rightarrow\lambda=\overline\lambda$
$\overline v^Tv=$

$v=\begin{pmatrix}Z_1\\dots\\Z_n\end{pmatrix}\ \ \ \ \ \ \ \ \overline v^T=\begin{pmatrix}\overline{Z_1}&\ldots&\overline{Z_N}\end{pmatrix}$
$\overline v^Tv=\sum\limits_{i=1}^n\overline{Z_i}Z_i=\sum\limits_{i=1}^n|Z_i|^2$

Se tutti i vettori $z_1=0$, allora vettore $v=0$

quindi $\sum\limits_{\lambda\in\text{Spec}_\mathbb R(A)}m_a(\lambda)=m$
$P_A(x)=\prod\limits_{i=1}^r(x-\lambda_i)^{m_a(\lambda_i)}$