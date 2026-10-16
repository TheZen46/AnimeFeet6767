Supponiamo $\overline x=\Small\left[\array{1\\1\\0\\0}\right]$ sia una **SBA**; $I_b=\{1,2\}\m{20}\bigl(\overline x_B=\left[\array{1\\1}\right],\ \ \overline x_N=\left[\array{0\\0}\right]\bigr)$
Supponiamo $\gamma^T=\bigl[-1,0\bigr]$
Supponiamo che $f(\overline x)=12$
Quanto vale la funzione obiettivo in $\Small\left[\array{1\\1\\3\\0}\right]$?

Si ha: $f(x)={C_B}^T B^{-1}b+\gamma^T(3,0)$

Criterio ottimalità: $\gamma\ge0\Rightarrow\overline x$ è soluzione ottima
Osservazione: Se $\gamma>0\Rightarrow\overline x$ è l'unica soluzione ottima

Sia $x\ne\overline x,\ x\in\mc{P}$
$f(x)=C^Tx={C_B}^TB{^-1}b+\gamma^T x_N>{C_B}^T B^{-1}b=C^T\overline x=f(\overline x)$

Test di illimitatezza:
Supponiamo che $\exists\ h$ radice tale che $\gamma_h<0$
Se la colonna $h$-esima di $B^{-1}N$ ha tutte entrate negative (o nulle) allora il problema è illimitato


$\gamma=\bigl(\gamma_1,\ldots,\gamma_{n-m}\bigr)$ si ha $\gamma_h<0$
Considero $x_N=t e_h=\bigl[0,\ldots,1,0\ldots,0\bigr]^T\cdot t$
Se definisco $x_B=B^{-1}b-B^{-1}Nx_N$, il vettore $\left[\array{x_B\\x_N}\right]$ verifica $Ax=b$
Sia $\large t>0\Rightarrow x_N\ge0$ è $\large x_B=B^{-1}b-B^{-1}N\Small\left[\begin{array}{c}0\\\vdots\\t\\\vdots\\0\end{array}\right]\large=\underbrace{B^{-1}b}_{\ge0}-\underbrace{\bigl[B^{-1}N\bigr]_h}_{\text{colonna }\\h\text{-esima}}\cdot\ t\Rightarrow x_B\ge0$

$f(x)={C_B}^TB^{-1}b+\gamma^T\cdot\ te_h={C_B}^TB^{-1}b+t\gamma_h\underset{t\to+\infty}{\longrightarrow}-\infty$


# Esercizio
$\cases{\min -x_1-x_2\\x_1-x_2=x_3=1\\-x_1+x_2+x_4=1\\x_1\ge0,\ x_2\ge0,\ x_3\ge0,\ x_4\ge0}$

$A=\sqmatrix{1&-1&1&0\\-1&1&0&1}\m{30}b=\sqmatrix{1\\1}\m{30}B=\sqmatrix{1&0\\-1&1}\Leftarrow\text{è una matrice di base}$
$B^{-1}=\sqmatrix{1&0\\1&1}\Rightarrow B^{-1}b=\sqmatrix{1\\2}\Rightarrow\overline x=\sqmatrix{1\\0\\0\\2}\text{è SBA}$
$\overline x_B=\sqmatrix{1\\2},\quad \overline x_N=\sqmatrix{0\\0}$
${C_B}^T=\sqmatrix{-1,0}\quad {C_N}^T=\sqmatrix{-1,0}\qquad N=\sqmatrix{-1&1\\1&0}\qquad B^{-1}N=\sqmatrix{-1&1\\0&1}$
$\gamma^T=\sqmatrix{-1,0}-\sqmatrix{-1,0}\sqmatrix{-1&1\\0&1}=\sqmatrix{-1,0}-\sqmatrix{1,-1}=\sqmatrix{-2,1}\leftarrow\text{vettore costi ridotti}$
$\gamma_1=-2<0$
$\bigl[B^{-1}N\bigr]_1=\sqmatrix{-1\\0}\Rightarrow\text{il pb è illimitato}$

$\cases{\min\ -x_1-x_2\\x_1=1+x_2-x_3\\x_4=1+x_1-x_2=2-x_3\\x\ge0}\m{30}\cases{\min\ -1-2x_2+x_3\\x_1=1+x_2-x_3\\x_4=2-x_3\\x\ge0}$

$B^{-1}N=\sqmatrix{-1&1\\0&1}$

$\overline x_B=\sqmatrix{1\\2}\quad\overline x_N=\sqmatrix{0\\0}$

### Osservazione
Test ottimalità non superato $\Rightarrow\exists\ \gamma_h<0$
Test illimitatezza non superato $\Rightarrow$ in corrispondenza di tutte le entrate negative (streattamente) di $\gamma$ esiste un elemento strettamente positivo nella colonna corrispondente di $B^{-1}N$

Fisso $h$ indice tale che $\gamma_h<0$ e quindi esiste un elemento $B^{-1}N_{ih}>0$

Come si aggiorna le SBA??
$\array{\overline x_B=B^{-1}b\\\overline x_N=\tiny{\sqmatrix{0\\\vdots\\0}}}\longrightarrow \array{x_B=B^{-1}b-B^{-1}Nte_k\\\\x_N=te_k}$

Come scegliere $k$? Come scegliere $t$?
1) Scegliamo $k=h$, perche $\gamma_h<0$
$x_B=B^{-1}b-B^{-1}Nx_N=B^{-1}b-\bigl[B^{-1}N\bigr]_h\ t$
Affinché il vettore sia ammissibilie:
	$B^{-1}b_j-\bigl[B^{-1}N\bigr]_{jh}\ t\ge0\qquad\forall\ j$
Se $\bigl[B^{-1}N\bigr]_{jh}\le0\Rightarrow(x_B)_j\ge0\qquad\forall\ t\ge0$
Se $\displaystyle \bigl[B^{-1}N\bigr]_{jh}\qquad t\le\frac{\bigl(B^{-1}b\bigr)_j}{\bigl[B^{-1}N\bigr]_{jh}}$

Per garantire $\sqmatrix{x_B\\x_N}$ ammissibile devo scegliere: $\ds t\le\min\limits_{j:B^{-1}N_{jh}>0}\frac{B^{-1}b_j}{\bigl[B^{-1}N\bigr]_{jh}}$

Criterio del rapporto minimo: $\ds\large t\le\min\limits_{j:[B^{-1}N]_{jh}>0}\frac{B^{-1}b_j}{\bigl[B^{-1}N\bigr]_{jh}}$
Sia $k=$indice su cui si ottiene il minimo
Allora la nuova SBA si ottiene:
	$\to$ facendo entrare $(x_N)_h\qquad(\gamma_h<0)$
	$\to$ facendo uscire $(x_B)_h\qquad(\text{corrispondente al rapporto min})$