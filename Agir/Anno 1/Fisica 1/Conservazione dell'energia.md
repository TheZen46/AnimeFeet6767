# Forza conservativa
$\displaystyle[\mathcal L]=[T]=\frac{Kg\cdot m}{s^2}=J$

Una forza è detta **conservativa** quando il lavoro compiuto dalla forza stessa durante lo spostamento del punto materiale da un punto $A$ a un punto $B$ lungo una curva $\gamma$ **non** dipende da $\gamma$, ma solo da $A,B\quad\forall\ A,B$

Una forza è conservativa$\iff$quando il lavoro lungo ogni curva $\gamma$ è nulla
	Se il lavoro dipende dagli estremi e non dal percorso, se considero una curva $\gamma$ chiusa, individuo $2$ punti $A,B$ che hanno $\gamma_1$ e $\gamma_2$ (entrambe da $A$ a $B$) 
	$1\to2$
		$\displaystyle\oint_\gamma \vec F\cdot d\vec l=\int_{\gamma_1} \vec F\cdot d\vec+\int_{\gamma_2} \vec F\cdot(-d\vec l)=\int_{\gamma_1} \vec F\cdot d\vec l-\int_{\gamma_2} \vec F\cdot d\vec l=0$
	$2\to1$
	$\displaystyle\oint_\gamma\vec F\cdot d\vec l=0\qquad\qquad\mathcal L_{\gamma_1}(\vec F)=\mathcal L_1\quad\mathcal L_{\gamma_2}(\vec F)=?$
		Consideriamo curva $\gamma$ chiusa
		$\displaystyle\mathcal L_{\gamma_1}(\vec F)-\mathcal L_{\gamma 2}(\vec F)=0\Rightarrow\mathcal L_{\gamma_2}(\vec F)=\mathcal L_{\gamma_1}(\vec F)=\mathcal L_\gamma$

## Forza peso
Curva $\gamma$
$\xi$ variabile temporale ($\simeq\Delta t$)

$\cases{x=x(\xi)\\y=y(\xi)\\z=z(\xi)}$

$\vec F=-mg\ \hat{U_z}$
$(dx,dy,dz)=\vec v\quad dt=\frac{dl}{dt}dt$
$\displaystyle\int_\gamma\vec F\cdot d\vec l=\int_{\gamma}-mg\ \overbrace{\hat{U_z}}^{(0,0,1)}\cdot(\frac{dx}{d\xi},\frac{dy}{d\xi},\frac{dz}{d\xi})d\vec\xi=\int_{\xi_0}^{\xi_1}-mg\frac{dx}{d\xi}d\xi=-mg\int_{\xi_0}^{\xi_1}\frac{dz}{d\xi}d\xi=-mg\left(Z(\xi_1)-Z(\xi_0)\right)=mg\left(Z(\xi_0)-Z(\xi_1)\right)=-mg\Delta h$


# Forza d'attrito non conservativa
$\gamma$ da $A$ a $B$
$F_B=-\mu_BN$

+$\mathcal L_\gamma(\vec F_B)=-\mu N\cdot(\text{lunghezza di }\gamma)$
# Energia potenziale (di una forza conservativa)
Per definire l'energia potenziale $U(x,y,z)$ di un punto materiale che si trova in $B=(x,y,z)$ di procede nel seguente modo.
- Si sceglie arbitrariamente un punto $A=(x_0,y_0,z_0)$ detto **riferimento** e si definisce $U(x,y,z)$ come l'opposto del lavoro della forza compiuto nello spostamento del punto materiale da $A$ a $B$

$U(x,y,z)=-\mathcal L_{A\to B}$

Le differenze di energia potenziale **non** dipendono dal riferimento
$U(x_2,y_2,z_2)-U(x_1,y_1,z_1)=-\left(\mathcal L_{\array{(x_0,y_0,z_0)\\\downarrow\\(x_2,y_2,z_2)}}-\mathcal L_{\array{(x_2,y_2,z_2)\\\downarrow\\(x_1,y_1,z_1)}}\right)=-\mathcal L_{\array{(x_1,y_1,z_1)\\\downarrow\\(x_2,y_2,z_2)}}$
## Esempi
$\mathcal L=-mg\ \Delta h$
$U=mg\ \Delta h$
$\text{Forza elsatica}$
$U=\frac12K(\Delta {x_2}^2-\Delta {x_1}^2)$

# Sistema conservativo
La risultante delle forze è conservativa
## Conservazione dell'energia meccanica
$\mathcal L_{A\to B}=\overbrace{T_B}^{\text{cinetica}}-T_A$
$U_A-U_B=T_B-T_A$
$U_A+T_A=U_B+T_B\quad\forall\ A,B$