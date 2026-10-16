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
Sia $\large t>0\Rightarrow x_N\ge0$ è $\large x_B=B^{-1}b-B^{-1}N\Small\left[\begin{array}{c}0\\\vdots\\t\\\vdots\\0\end{array}\right]\large=B^{-1}b-\underbrace{\bigl[B^{-1}N\bigr]_h}_{\text{colonna }h\text{-esima}}\cdot\ t\Rightarrow x_B\ge0$