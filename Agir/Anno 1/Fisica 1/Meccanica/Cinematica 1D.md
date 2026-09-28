# Traiettoria di un punto materiale
Se $t\in(t_0,t_1)\ \ \begin{cases}x(t)=f_x\\y(t)=f_y\\z(t)=f_z\end{cases}$
Al variare del tempo il punto si muove su una curva $\gamma$ (traiettoria)

## Distanza percorsa tra t₀ e t₁
È la lunghezza della curva percorsa dal punto materiale tra $t_0$ e $t_1$
**Scalare**

## Spostamento
Differenza tra il vettore posizione all'instante finale e il vettore posizione all'istante iniziale

$\vec{\Delta s}=(x_1,y_1,z_1)-(x_0,y_0,z_0)=(x_1-x_0,y_1-y_0,z_1-z_0)$

### Esempio
Una persona cammina dall'origine al punto $(1,2)$ in linea retta, poi di sposta di $3$ lungo $x$, e ancora di $4$ lungo $y$.
Distanza percorsa? Spostamento?

#### Distanza percorsa
$d=\sqrt{1^2+2^2}+3+4=\sqrt5+3+4=7+\sqrt5$

#### Spostamento
$\vec{\Delta s}=(4,6)-(0,0)=(4,6)$

## Velocità
Punto materiale vincolato a muoversi lungo l'asse $X$

### Velocità scalare media <vₛ>
$<v_s>=\frac{\text{distanza percorsa}}{\text{tempo impiegato}}=\frac{2x_1}{t_1}$

### Velocità vettoriale media <vᵥ>
$<v_v>=\frac{\text{spostameno}}{\text{tempo impiegato}}$

### Velocità vettoriale istantanea
In un generico istante $t$, la velocità vettoriale istantanea coincide con la velocità vettoriale media nell'intervallo $(t,t+\Delta t)$, con $\Delta t$ "molto piccolo"

$<v_v>=\frac{x(t+\Delta t)-x(t)}{\Delta t}=\frac{dx(t)}{dt}$


#### Esercizio
$x(t)=At^2+B$
$A=2.1\frac m{s^2}$
$B=2.1 m$

Spostamento tra $t_0=3.00s$ e $t_1=5.00 s$
$<v_s>$ nell'intervallo
$<v_v> \forall t$ nell'intervallo

$\vec{\Delta s}=x(5)-x(3)=(A5^2+B)-(A3^2+B)=33.6m$
$<v_v>=\frac{33.6m}{2s}$
$<v_v>=\frac{dx(t)}{dt}=2At$


## Accelerazione media
$[t_0,t_1]$
$<a_v>=\frac{v(t_1)-v(t_0)}{t_1-t_0}$

## Accelerazione istantanea
$a_v(t)=\frac{v(t+\Delta t)-v(t)}{\Delta t}=\frac{dv(t)}{dt}=\frac{d^2x(t)}{dt^2}$
$a=\frac{d}{dt}(v)=\frac{d}{dt}(\frac{dx}{dt})=\frac{d^2t}{dt^2}$


$x(t)\rightarrow v(t)=\frac{dx}{dt}\rightarrow a=\frac{dv}{dt}=\frac{d^2x}{dt^2}$


# Moto rettilineo uniforme
Rettilineo = $1D$
Uniforme = Velocità costante $v_0$

$x(t)?$
$\displaystyle\frac{dx}{dt}=v_0$

$x(t)=v_0t+x_0$

# Moto rettilineo uniformemente accelerato
$\displaystyle\frac{d^2x}{dt^2}=a_0$
$x(t)=\frac12 a_0t^2+v_0t+x_0$
