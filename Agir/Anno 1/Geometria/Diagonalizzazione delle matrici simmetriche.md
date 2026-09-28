$\mathbb K=\mathbb R$ oppure $\mathbb K=\mathbb C$ (esempi)

# Forma bilineare
## Reali
$(\cdot,\cdot):\ V\times V\rightarrow\mathbb R$
$\begin{array}{r}\forall\ v_1,v_2,v_3\in V\\\forall\ \lambda,\mu\in\mathbb R\end{array}\ \ \ \ (v_1,\lambda v_2+\mu v_3)=\lambda(v_1,v_2)+\mu(v_1,v_3)$
$(\lambda v_1+\mu v_2,v_3)=\lambda(v_1,v_3)+\mu(v_2,v_3)$

### Simmetria
$\forall\  v_1,v_2\in V$
$(v_1,v_2)=(v_2,v_1)$

## Complessi
Nel caso di $\mathbb K=\mathbb C$
$(\cdot,\cdot):\ V\times V\rightarrow\mathbb C$
$\begin{array}{r}\forall\ v_1,v_2,v_3\in V\\\forall\ \lambda,\mu\in\mathbb R\end{array}\ \ \ \ (v_1,\lambda v_2+\mu v_3)=\lambda(v_1,v_2)+\mu(v_1,v_3)$

### Simmetria
$\forall\ v_1,v_2\in V$
$(v_1,v_2)=\overline{(v_2,v_1)}$


# Definizioni
$\mathbb R$ un prodotto scalare è **definito positivo** se $\forall\ v\in V\ \ v\ne 0\ \ (v,v)>0$
$\mathbb R$ un prodotto scalare è **definito positivo** se $\forall\ v\in V\ \ v\ne 0\ \ (v,v)<0$
$\mathbb R$ un prodotto scalare è **semidefinito positivo** se $\forall\ v\in V\ \ v\ne 0\ \ (v,v)\ge0$ ed $\exists\ v\ne0$ con $(v,v)=0$
$\mathbb R$ un prodotto scalare è **semidefinito negativo** se $\forall\ v\in V\ \ v\ne 0\ \ (v,v)\le0$ ed $\exists\ v\ne0$ con $(v,v)=0$


Su $\mathbb C$ se vale anche $\forall\ v\in V\ \ v\ne0\ \ (v,v)\in\mathbb R$ ed è 0, allora $(\cdot,\cdot)$ è un **prodotto hermitiano**

${v_1}^T,v_2$
$\begin{pmatrix}x_1&y_1&z_1\end{pmatrix}\begin{pmatrix}x_2\\y_2\\z_2\end{pmatrix}=x_1x_2+y_1y_2+z_1z_2$
$M\in\text{Mat}_n$
$n$ spazio vettoriale di dimensione $n$
${v_1}^T Mv_2\in\mathbb K$
$({v_1}^T Mv_2)^T={v_2}^T M^T v_1$

Fissata $M\in\text{Mat}_n(\mathbb R)$ simmetrica
$(v_1,v_2)_M:={v_1}^T M v_2$ è un prodotto scalare
Se $M=I_M$ ottenuto il prodotto scalare standard


# Matrici ortogonali
Sia $\mathbb B$ una base di V
$\mathbb B$ è una base **ortonormale** se $\forall\ v_1\ne v_2$ (rispetto ad un prodotto scalare definito positivo) $(v_1,v_2)=0$ e $\forall\ v$ nella base $(v,v)=1$
In $\mathbb R^n$ (col prodotto standard)
$v_1,\ldots,v_n$ è una base ortonormale se e solo se $Q=\begin{pmatrix}\vert&\vert&&\vert\\v_1&v_2&\dots&v_n\\\vert&\vert&&\vert\end{pmatrix}$
$Q^T Q=I_n$

$O(n)=\{Q\in\text{Mat}_n(\mathbb R)|Q^TQ=I_n\}$

## Isometria
$\begin{array}\forall\ Q\in O(n)\\\forall\ v_1,v_2\in\mathbb R^n\end{array}\ \ \ \ (Qv_1,Qv_2)=(v_1,v_2)={v_1}^Tv_2={v_1}^T\underbrace{Q^TQ}_Iv_2=(Qv_1)^TQv_2$

$f\in\text{End}(v)$
Se $\forall\ v,w\in V\ \ \ \ (f(v),f(w))=(v,w)$
$f$ è un'**isometria** (rispetto a $\small(\cdot,\cdot\small)$)


$\begin{pmatrix} -\sin\theta & \cos\theta \end{pmatrix}$

$\begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}$

$\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\ \ \ \ \begin{pmatrix}0&-1\\1&0\end{pmatrix}$

$\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}\ \ \ \ \begin{pmatrix}0&1\\1&0\end{pmatrix}$

$\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$

$\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$

$O(n)$

$\forall\ Q\in O(n)$
$\text{det}\ Q=\pm1$

$SO(n)=\{Q\in O(n)|\text{det}\ Q=1\}$

$S$ = speciale

# Ortogonalizzazione di Gram-Schmidt
Sia $V$ spazio vettoriale su $\mathbb R$
$\mathbb B=v_1,\ldots,v_n$ base di $V$
$(\cdot,\cdot)$ prodotto scalate determinato positivo

$\overbrace{W_1}^{u_1}=\frac{v_1}{||v_1||}$
$||W_1||=||\frac{v_1}{||v_1||}||=\frac1{||v_1||}||v_1||=1$

$W_2:=v_2-(v_2,u_1)u_1$
$(v_2,u_1)=(v_2,u_1)-(v_2u_1)\overbrace{(u_1,u_1)}^1=0$

$\begin{array}{c}u_1\\\dots\\u_k\end{array}$   ortogonale e di norma 1
$W_{K+1}=v_{K+1}-\sum\limits_{i=1}^K(v_{K+1},u_i)u_n$
$(W_{K+1},u_J)=(W_{K+1},u_J)-\sum\limits_{i=1}^K(v_{K+1},u_i)(u_i,u_J)$



$u_1,\ldots,u_n$ tale che $(u_i,\ldots,u_n)=0\ \ \ \ \forall\ i\ne j$
$||u_i||\ne0\ \ \ \ \forall\ i$
allora $u_i,\ldots,u_n$ sono linearmente indipendenti

$\sum a_iu_i=0$
$\underbrace{(\sum\limits_j a_iu_i,u_i)}_{\sum\limits_j a_j(u_j,u_i)}=(0,u_i)=0$
$\sum\limits_j a_j(u_j,u_i)=a_i\underbrace{||u_i||^2}_{\ne0}\Rightarrow a_i=0$



$v_1,\ldots,v_n\rightsquigarrow i_w\rightsquigarrow u_i$
$\begin{array}{c}w_i\\u_i\end{array}\in<v_1,\ldots,v_i>$
Quali sono i vettori $C_\mathcal B(u_i)$?
$\begin{pmatrix}\ast\\\ast\\1\\0\\\vert\\0\end{pmatrix}\begin{array}{l}\leftarrow i\\\leftarrow i+1\end{array}$

$w_i=(1)v_i-\sum\limits_{j-1}^{i-1}(v_i,u_j)u_j$

$\begin{pmatrix}1&\ast&\ast\\0&\diagdown&\ast\\0&0&1\end{pmatrix}$



$w\subseteq V$ sottospazio  $(,)$ definito positivo
$W^\perp=\{v\in V|\ \forall\ w\in W\ \ (v,w)=0\}$
Se $(,)$ è definito positivo, allora lo spazio vettoriale $V=W\oplus W^\perp$

$\text{dim}V=\text{dim}W+\text{dim}W^\perp$
$v_1,\ldots,v_k$ base di $W\rightsquigarrow v_1,\ldots,v_k,v_{k+1},\ldots,v_n$ base di $V$  $\overset{\text{Gram-Schmidt}}\rightsquigarrow u_1,\ldots,u_n\ \ \begin{array}{l}u_1,\ldots,u_k\text{ è base autonormale di }W\\u_{k+1},\ldots,u_n\text{ è base ortonormale di }W^\perp\end{array}$



## Esempio in R³
$\underset{v_1}{\begin{pmatrix}1\\1\\-1\end{pmatrix}}\underset{v_2}{\begin{pmatrix}2\\0\\1\end{pmatrix}}\underset{v_3}{\begin{pmatrix}1\\-1\\2\end{pmatrix}}$ $\text{det}=2\ne0\rightarrow$ basi

$u_1=\frac{v_1}{||v_1||}=\frac1{\sqrt3}v_1=\begin{pmatrix}\frac{\sqrt3}3\\\frac{\sqrt3}3\\-\frac{\sqrt3}3\end{pmatrix}$

$w_2=v_2-(v_2,u_1)u_1=\begin{pmatrix}2\\0\\1\end{pmatrix}-(\frac{2\sqrt3}3+0+(-\frac{\sqrt3}3))\begin{pmatrix}\frac{\sqrt3}3\\\frac{\sqrt3}3\\-\frac{\sqrt3}3\end{pmatrix}=\begin{pmatrix}2\\0\\1\end{pmatrix}-\begin{pmatrix}\frac13\\\frac13\\-\frac13\end{pmatrix}=\begin{pmatrix}\frac53\\-\frac13\\\frac43\end{pmatrix}$
$||w_2||=\frac13\sqrt{25+1+16}=\frac13\sqrt42$

$u_2=\frac1{\sqrt42}\begin{pmatrix}5\\-1\\4\end{pmatrix}$

$w_3=v_3-(v_3,u_1)u_1-(v_3,u_2)u_2=\begin{pmatrix}1\\-1\\2\end{pmatrix}-\frac1{\sqrt3}(1-1+2)\begin{pmatrix}\frac{\sqrt3}3\\\frac{\sqrt3}3\\-\frac{\sqrt3}3\end{pmatrix}-\frac1{\sqrt42}(5+1+8)\begin{pmatrix}5\\-1\\4\end{pmatrix}=\begin{pmatrix}1\\-1\\2\end{pmatrix}-2\begin{pmatrix}\frac13\\\frac13\\-\frac13\end{pmatrix}+\frac2{42}\begin{pmatrix}1-\frac23+\frac5{21}\\-1-\frac23-\frac1{21}\\-2+\frac23+\frac4{21}\end{pmatrix}=\begin{pmatrix}\frac{21-14+5}{21}\\\frac{-21-14-1}{21}\\\frac{-42+14+4}{21}\end{pmatrix}=\begin{pmatrix}\frac47\\\frac{-12}7\\\frac{-8}7\end{pmatrix}$
$||w_3||=\frac47||\begin{pmatrix}1\\-3\\-2\end{pmatrix}||=\frac47\sqrt{1+9+4}=\frac{4\sqrt{14}}7$
