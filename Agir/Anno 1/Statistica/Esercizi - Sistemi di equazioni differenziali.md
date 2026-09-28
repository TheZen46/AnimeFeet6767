1) $\cases{y'_1=2y_1+3y_2\\y'_2=2y_1+y_2}\qquad A=\pmatrix{2&3\\2&1}$
$P(\lambda)=\operatorname{det}(A-\lambda I)=\operatorname{det}\pmatrix{2-\lambda&3\\2&1-\lambda}=(2-\lambda)(1-\lambda)-6=\lambda^2-3\lambda-4=(\lambda+1)(\lambda-4)\Rightarrow\array{\lambda=-1\\\lambda=4}$

$\lambda=4\qquad Av=4v$

$\cases{2v_1+3v_2=4v_1\\2v_1+v_2=4v_2}\Rightarrow \cases{2v_1=3v_2\\\cancel{2v_1=3v_2}}\qquad v=(3,2)$

$\lambda=-1\qquad Av=-v$

$\cases{2v_1+3v_2=-v_1\\2v_1+v_2=-v_2}\Rightarrow \cases{v_1=-v_2\\\cancel{v_1=-v_2}}\qquad v=(1,-1)$

$\vec y=c_1e^{4x}\pmatrix{3\\2}+c_2 e^{-x}\pmatrix{1\\-1}$
$\array{y_1(x)=3c_1 e^{4x}+c_2 e^{-x}\\y_2(x)=2c_1 e^{4x}-c_2 e^{-x}}\qquad c_1,c_2\in\mathbb R$

2) $\vec y'=A\vec y\qquad A=\pmatrix{3&1&1\\1&3&1\\1&1&3}$    (La scrittura $A$ è equivalente a $y'_1=3y_1+2_2+y_3\ldots$)
$\displaystyle P(\lambda)=\operatorname{det}\pmatrix{3-\lambda&1&1\\1&3-\lambda&1\\1&1&3-\lambda}=(3-\lambda)((3-\lambda)^2-1)+((3-\lambda)-1)+(1-(3\lambda))=$
$=(3-\lambda)(8-6\lambda+\lambda^2)-2+\lambda-2+\lambda=-\lambda^3+6\lambda^2+3\lambda^2-8\lambda-18\lambda+24-4+2\lambda=-\lambda^2+9\lambda^2-24\lambda+20$
	Ruffini
$-(\lambda-2)^2(\lambda-5)$
$\begin{array}{l}\lambda=2\Leftarrow\text{Doppio}\\\lambda=5\end{array}$

$\lambda=5\qquad\cases{3v_1+v_2+v_3=5v_1\\v_1+3v_2+v_3=5v_2\\v_1+v_2+3v_3=5v_3}\qquad v=(1,1,1)$
$\lambda=2\qquad\cases{3v_1+v_2+v_3=2v_1\\v_1+3v_2+v_3=2v_2\\v_1+v_2+3v_3=2v_3}\qquad v=(1,-1,0)\ \text{e}\ (1,0,-1)$
$\vec y= c_1 e^{3x}\pmatrix{1\\1\\1}+c_2 e^{2x}\pmatrix{1\\-1\\0}+c_3 e^{2x}\pmatrix{1\\0\\-1}$

$\left(\begin{array}{ccc|c}3&1&1&5\\1&3&1&5\\1&1&3&5\end{array}\right)$

3) $\vec y'=Ay\qquad\pmatrix{1&1&0\\0&1&1\\0&0&2}$
$\displaystyle P(\lambda)=\operatorname{det}\pmatrix{1-\lambda&1&0\\0&1-\lambda&1\\0&0&3-\lambda}=(1-\lambda)\operatorname{det}\pmatrix{1-\lambda&1\\0&2-\lambda}=(1-\lambda)(1-\lambda)(2-\lambda)$
$\begin{array}{l}\lambda=1\Leftarrow\text{Doppio}\\\lambda=2\end{array}$

$\lambda=2\qquad\cases{v_1+v_2=2v_1\\v_2+v_3=2v_2\\-2v_3=2v_3}\qquad v=(1,1,1)$
$\lambda=1\qquad\cases{v_1+v_2=v_1\\v_2+v_3=v_2\\-2v_3=v_3}\qquad v=(1,0,0)\qquad\text{autospazio di dimensione }1\Rightarrow\text{cerco autospazio generalizzato}$
Cerco $\vec w$ tale che $\quad\array{\lambda\text{ autovalore}\\v\text{ autovettore}}$
$(A-I\lambda)\vec w=\vec v$
$(A-I)\vec w=\pmatrix{1\\0\\0}$
$\pmatrix{0&1&0\\0&0&1\\0&0&1}\pmatrix{w_1\\w_2\\w_3}=\pmatrix{1\\0\\0}$
$\cases{w_2=1\\w_3=0\\w_3=0}\Rightarrow (1,1,0)\text{ autovettore generalizzato}$

$\vec y=c_1e^{2x}\pmatrix{1\\1\\1}+c_2e^x\pmatrix{1\\0\\0}+c-3 e^x\left(x\cdot\pmatrix{1\\0\\0}+\pmatrix{1\\1\\0}\right)=c_2e^{2x}\pmatrix{1\\1\\1}+c_2e^x\pmatrix{1\\0\\0}+c_3e^x\pmatrix{x+1\\1\\0}$

# Formula
$ce^{\lambda x}(x\cdot\vec v+\vec w)$

4) $3y_1'''+y_1''-2y_1'=0\qquad\array{y_1\to y_1\\y'\to y_2\\y''\to y_3}$
$\cases{y'_1=y_2\\y'_2=y_3\\3y_3'+y_3'+y_3-2y_2=0}\qquad\cases{y'_1=y_2\\y'_2=y_3\\y_3'=\frac23 y_2-\frac13 y_3}$
$\pmatrix{0&1&0\\0&0&1\\0&\frac23&-\frac13}$
$P(\lambda=\operatorname{det}\pmatrix{-\lambda&1&0\\0&-\lambda&1\\0&\frac23&-\frac13-\lambda}=-\lambda\operatorname{det}\pmatrix{-\lambda&-1\\\frac23&-\frac13-\lambda}=\lambda(\lambda^2+\frac13\lambda-\frac23)=\lambda(\lambda+1)(\lambda-\frac23)$
$\begin{array}{l}\lambda=0\\\lambda=-1\\\lambda=\frac23\end{array}$

Volendo trovare solo $y_1$, basta $y(x)=c_1+c_2e^{-x}+c_3e^{\frac23 x}$

Con autovettori invece $y(x)=c_1\pmatrix{1\\0\\0}e^{0x}+c_2\pmatrix{1\\-1\\1}e^{-x}+c_3\pmatrix{9\\6\\4}e^{\frac23 x}$

5) $3y_1'''+y_1''-2y_1'=e^{-x}$
$y(x)=\underbrace{y_o(x)}_{\array{\text{trovata}\\\text{prima}}}+y_p(x)$
Metodo delle costanti
$f(x)=x^{\mu} Q_0(x) e^{-x}=cx e^{-x}$

# Risolvi

$c=\frac15$
$y_p(x)=\frac15 xe^{-x}$


6) $\cases{y_1(x)=2y_1(x)+y_2(x)\\y_2(x)=\alpha y_1(x)+2y_2(x)}\qquad A=\pmatrix{2&1\\\alpha&2}\quad\alpha\in\mathbb R$
$P_\alpha(\lambda)=\operatorname{det}\pmatrix{2-\lambda&1\\\alpha&2-\lambda}=(2-\lambda)^2-\alpha$
$P_\alpha(\lambda)=0\iff \lambda=2\pm\sqrt\alpha$

$4-4\lambda+\lambda^2-\alpha$
$\lambda=\frac{4\pm\sqrt{16-4(4-\alpha)}}2$
$\sqrt{-7}=i\sqrt{7}$

Se $\alpha>0$
$2\pm\sqrt\alpha$ autovalori di molteplicità $1$
$Av=(2\pm\sqrt\alpha)v\qquad\cases{\cancel{2v_1}+v_2=(\cancel 2+\sqrt\alpha)v_1\\\alpha v_1+\cancel{2v_2}=(\cancel 2 +\sqrt\alpha)v_2}$
$\vec y(x)=c_1\pmatrix{1\\\sqrt\alpha}e^{(2+\sqrt\alpha)x}+c_2\pmatrix{1\\-\sqrt\alpha}e^{(2-\sqrt\alpha)x}$

Se $\alpha=0$
$2$ autovalore doppio
$Av=2v\qquad\cases{2v_1+v_2=2v_1\\\cancel{2v_2=v_2}}\qquad v=(1,0)$
$(A-2I)w=\pmatrix{1\\0}\qquad\pmatrix{0&1\\0&0}\pmatrix{w_1\\w_2}=\pmatrix{1\\0}\qquad\cases{w_2=1\\\cancel{0=0}}\qquad v=(0,1)$
$\vec y(x)=c_1 e^{2x}\pmatrix{1\\0}+c_2 e^{2x}\left(x\pmatrix{1\\0}+\pmatrix{0\\1}\right)$

Se $\alpha<0$
$\lambda\pm=2\pm i\sqrt{-\alpha}$ autovalori complessi
$Av=\lambda_+ v\qquad\cases{\cancel{2v_1}+v_2=(\cancel 2+i\sqrt{-\alpha})v_1\\\alpha v_1+\cancel{2v_2}=(\cancel 2+i\sqrt{-\alpha})v_2}$
$Av=\lambda v\Rightarrow\pmatrix{1\\-i\sqrt{-\alpha}}$
$\lambda=a\pm ib$
$\vec v=\vec u+i\vec w$
$y=c_1 e^{\alpha}\left(\vec u\cos(bx)-\vec w\sin(bx)\right)+c_2 e^{\alpha}\left(\vec u\sin(bx)+\vec w\cos(bx)\right)$
$y(x)=c_1 e^{2x}\left(\pmatrix{1\\0}\cos(\sqrt{-\alpha}x)-\pmatrix{0\\\sqrt{-\alpha}}\sin(\sqrt{-\alpha}x)\right)+c_2e^{2x}\left(\pmatrix{1\\0}\sin(\sqrt{-\alpha}x)+\pmatrix{0\\\sqrt{-\alpha}}\cos(\sqrt{-\alpha}x)\right)$
$\vec y(x)=c_2 e^{2x}\pmatrix{\cos(\sqrt{-\alpha}x)\\-\sqrt{-\alpha}\sin(\sqrt{-\alpha}x)}+c_2 e^{2x}\pmatrix{\sin(\sqrt{-\alpha}x)\\\sqrt{-\alpha}\cos(\sqrt{-\alpha}x)}$

$\underline y'=A_\mu y\quad\mu\in\mathbb R$
$A_\mu=\pmatrix{-1&2\\-2&-3}+\mu\pmatrix{1&0\\0&1}$
$A_\mu=\pmatrix{\mu-1&2\\-2&\mu-3}$
$P_\mu(\lambda)=\operatorname{det}\pmatrix{\mu-1-\lambda&2\\-2&\mu-3-\lambda}=\lambda^2+\lambda(-\mu+3-\mu^2+1)+(\mu^2-4\mu+3+4)=\lambda^2+\lambda(4-2\mu)+(\mu^2-4\mu+7)$
$\lambda_{1,2}=\frac{4-2\mu\pm\sqrt{16+\cancel{4\mu^2}+\cancel{6\mu}-\cancel{4\mu^2}+\cancel{16\mu}-28}}2=2-\mu\pm\sqrt{-\frac{12}4}=2-\mu \pm i\sqrt3$

$\Re(\text{autovalori})=2-\mu$
Se $\mu>2$ allora $\Re(\text{autovalori})<0$
Quindi $\vec 0$ è asintoticamente stabile
Se $\mu<2$ allora $\Re(\text{autovalori})>0\Rightarrow\text{No stabile}$
(Perché questo? $e^{c x}$ deve avere $c<0$ per essere stabile, non tende a $\infty$)

Se $\mu=2$ caso critico
$\vec 0$ non è asintoticamente stabile
È stabile? Dipende delle regolarità degli autovettori



Autovalori regolari