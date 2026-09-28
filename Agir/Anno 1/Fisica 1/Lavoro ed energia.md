Capacità di fare lavoro
# Prodotto scalare
$V\cdot V\to\mathbb R$

$\vec{v_1}\cdot \vec{v_2}=|\vec{v_1}|\cdot|\vec{v_2}|\cdot\cos{\theta}=v_{1x}\ v_{2x}+v_{1y}\ v_{2y}+v_{1z}\ v_{2z}$

# Integrale
$A(x_1, x_2)=\int_{x_1}^{x_2}f(x)dx=F(x_2)-F(x_1)$
$\frac{dF(x)}{dx}=f(x)$

# Lavoro
Un punto materiale si muove lungo una curva $\gamma$. Questa curva può essere approssimata con tanti "segmentini" $\Delta\vec{l_i}$
Il punto materiale è soggetto a una forza $\vec F$. In particolare possiamo dire che quando il punto materiale si trova a metà del segmento $\Delta\vec{l_i}$ la forza vale $\vec{F_i}$
Il lavoro della forza $\vec F$ lungo $\gamma$ è dato da $\mathcal L_{\gamma}(\vec F)$

$\mathcal L_{\gamma}(\vec F)=\sum\limits_{i=1}^N\vec F_i\cdot\Delta\vec l_i$


Diciamo $\vec{F_i}=\vec F(\vec r_i)$
$\vec r_i$ punto medio di $\Delta\vec l_i$

$\mathcal L_\gamma(\vec F)=\sum\limits_{i=1}^N \vec F(\vec r_i)\cdot\Delta\vec l_i\overset{\Delta l\to0}\longrightarrow\int_\gamma \vec F\cdot d\vec l$

($\vec F\small(\vec r_i)$ è la forza esercitata quando il punto materiale si trova in $\vec r_i$)


## Teorema lavoro-energia
Consideriamo come forza $\vec F$ la risultante delle forze (quella di $\vec F=m\vec a$)
$\mathcal L_{\gamma}(\vec F)=\sum\limits_{i=1}^N\vec F(\vec r_i)\cdot\Delta\vec l_i=\sum\limits_{i=1}^Nm\vec a(\vec r_i)\cdot\Delta \vec l_i=\sum\limits_{i=1}^N\overset{{\color{#F44}=\Delta\vec v(\vec r_i)}}{m{\color{#F44}\vec a(\vec r_i)}\cdot\vec v(\vec r_i){\color{#F44}\Delta t_i}}=\sum\limits_{i=1}^Nm\ \overset{t_0}{\vec v(\vec r_i)}\cdot\Delta\overset{t_1}{\vec v(\vec r_i)}$
$\vec v(t_0)\cdot\Delta(t_1)=\vec v(t_0)\cdot{\big(}\vec v(t_0+\Delta t)\cdot\vec v(t_0){\big)}$
$\Delta(\vec v^2(t_0))=\Delta(\vec v(t_0)\cdot\vec v())$
yadayadayada
$\mathcal L_\gamma(\vec F)=\frac12m\sum\limits_{i=1}^N(\Delta v_i)^2=\frac12m({v_1}^2-{v_2}^2):T_F-T_I$

$T=\text{energia cinetica}$
$T=\frac12mv^2$


### Definizione formale
$\mathcal L_\gamma(\vec F)=\int_\gamma\vec F\cdot d\vec l=\int_\gamma m\frac{d\vec v}{dt}\cdot d\vec l=\int_\gamma m\frac{d\vec v}{\cancel{dt}}\vec v\cdot \cancel{dt}=\int_\gamma m\vec v\cdot dv=\frac12\int v\cdot dv=\frac12 m\cdot v^2$



In un sistema conservativo, $\vec F=-(\frac{\partial U}{\partial x},\frac{\partial U}{\partial y},\frac{\partial U}{\partial z})=-\vec\nabla U\qquad\nabla=(\partial_x,\partial_y,\partial_z)$
$\displaystyle\frac d{dt}(T+U)=0\Rightarrow\frac d{dt}(\frac12mv^2+U)=\frac d{dt}(\frac12 m\vec v\cdot\vec v+U)=\cancel{\frac12} m{\small\cancel2}v\cdot\frac{d\vec v}{dt}+\frac{dU}{dt}=m\vec v\cdot\frac{d\vec v}{dt}+\frac{dU}{dx}\frac{dx}{dt}+\frac{dU}{dy}\frac{dy}{dt}+\frac{dU}{dz}\frac{dz}{dt}=\vec v\cdot\left(m\cdot\frac{d\vec v}{dt}+(\frac{\partial U}{\partial x},\frac{\partial U}{\partial y},\frac{\partial U}{\partial z})\right)=m\vec v\cdot\frac{d\vec v}{dt}+(\frac{\partial U}{\partial x},\frac{\partial U}{\partial y},\frac{\partial U}{\partial z})=0$
$m\vec a=-(\frac{\partial U}{\partial x},\frac{\partial U}{\partial y},\frac{\partial U}{\partial z})=\vec F_{\text{ris}}$





$U=\frac12 K\Delta x^2=\frac12 Kx^2$
$\vec F=(-kx,0,0)$


$T+U+\Delta=\text{Costante}$

Il teorema energia-lavoro per i sistemi non conservativi
$\vec F_c, \vec F_o$

$T_F-T_I=\mathcal L_C+\mathcal L_O$
$T_F+U_F-T_I-U_I=\Delta E_\text{Meccanica}=\mathcal L_O$


# Potenza
Una forza $F$ da su un punto materiale un lavoro $\mathcal L_\gamma(\vec F)$ in un certo intervallo di tempo $\Delta t$. Si dice potenza media $\vec P=\frac{\mathcal L_\gamma(\vec F)}{\Delta t}\Rightarrow P_{\text{istantanea}}=\frac{d\mathcal L}{dt}$


# Conservazione della quantità di moto
$\vec P=\text{Quantità di moto}$

$\vec P=m\vec v,\ \frac{d\vec P}{dt}=m\frac{d\vec v}{dt}=m\vec a=\vec F$

Sistema isolato: solo forze interne
$\displaystyle\begin{cases}\frac{d\vec P_1}{dt}=F_{2,1}\\\frac{d\vec P_2}{dt}=F_{1,2}=-F_{1,2}\end{cases}\Rightarrow\frac{d}{dt}(P_1+P_2)=\frac{d\vec P_\text{tot}}{dt}=\vec0$

$\displaystyle\begin{cases}\frac{d\vec P_1}{dt}=F_{2,1}+F_{3,1}+\ldots+F_{n,1}\\\frac{d\vec P_2}{dt}=F_{1,2}+F_{3,2}+\ldots+F_{n,2}\\\vdots\\\frac{d\vec P_n}{dt}=F_{1,n}+F_{3,n}+\ldots+F_{n-1,n}\end{cases}\Rightarrow\frac{d}{dt}(P_1+P_2+\ldots+P_n)=\frac{d\vec P_\text{tot}}{dt}=\vec0$

$\frac{d\vec P_1}{dt}=\sum\limits_{j=1}\vec F_{ji}\rightarrow\sum\limits_i\sum\limits_{j\ne i}\vec F_{ji}=\sum\left(\sum\limits_{j>i}\vec F_{ji}+\sum\limits_{j<i}\vec F_{ji}\right)$

$\frac d{dt}(\vec P_1+\vec P_2+\ldots+\vec P_n)=?$


In un sistema isolato la quantità di moto si conserva
$\vec P=\sum_i\vec P_i$

# Processi di urto
Se la forza dell'urto è molto maggiore delle altre (attrito...) allora la si trascura