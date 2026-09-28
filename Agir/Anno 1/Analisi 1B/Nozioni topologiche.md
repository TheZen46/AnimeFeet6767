Intorno sferico (aperto) di $\vec x\in\mathbb R^n$ (o palla centrata in $\vec{x_0}$) di raggio $r>0$ è $B_r(\vec{x_0})=\{x\in\mathbb R^n|\ ||\vec x-\vec{x_0}||<r\}$

Dati $\Omega\subseteq\mathbb R^n,\ \vec{x_0}\in\mathbb R^n$ diciamo che $\vec{x_0}$ è:
- **interno** a $\Omega$ se $\exists\ r>0$ tale che $B_r(\vec{x_0})\subseteq\Omega$
- **esterno** a $\Omega$ se $\exists\ r>0$ tale che $B_r(\vec{x_0})\subseteq\overbrace{\Omega^c}^{\text{complementare di }\Omega}$
- interno/esterno **di frontiera** per $\Omega$ se non è né interno né esterno (equivalentemente $\forall\ r>0\quad B_r(\vec{x_0})$ contiene sia elementi di $\Omega$ che di $\Omega^c$)
- L'**interno** di $\Omega$ è l'insieme dei punti interni di $\Omega$ e si indica con $\mathring{\Omega}$
- La **frontiera** (o **bordo**) do $\Omega$ è l'insieme dei punti di frontiera di $\Omega.$ Si indica con $\partial\Omega$
- La **chiusura** di $\Omega$ è $\bar\Omega=\partial\Omega\cup\mathring\Omega$

$\mathring\Omega\subseteq\Omega\subseteq\bar\Omega$

$\Omega$ si dice **aperto** se $\omega=\mathring\Omega$

## Nota
$\mathring{\Omega}$ è sempre aperta
$B_r(\vec{x}_0)$ è sempre **aperta**$\quad\forall\ r>0,\forall\ x\in\mathbb R^n$

- Un insieme si dice **chiuso** se contiene la sua frontiera o equivalentemente se $\Omega=\bar\Omega$

## Nota
$\bar\Omega$ è sempre chiusa

$\bar{B_r(\vec{x_0})}=\{\vec x\in\mathbb R^n|\ ||\vec x-\vec{x_0}||\le r\}$ è chiusa (palla piena)

$\partial B_r(\vec{x_0})=\{\vec x\in\mathbb R^n|\ ||\vec x-\vec{x_0}||= r\}$ è chiuso (palla non piena)

## Nota
$\{\vec x\in\mathbb R\ |\ 2\le||\vec x||\le3\}$ non è né aperto né chiuso



- $\mathbb R^n$ e $\varnothing$ sono gli unici insiemi di $\mathbb R^n$ che sono sia aperti che chiusi
- L'unione (anche infinita) di aperte è aperta
- L'intersezione (anche infinita) di chiuse è chiusa

# Altre definizioni
- Dato $\vec{x_0}\in\mathbb R^n,\ \Omega\subseteq\mathbb R^n,\ \vec{x_0}$ si dice di **accumulazione** per $\Omega$ se $\forall\ r>0\ \ \Omega\cap\left(B_r(\vec{x_0})\setminus\{x_0\}\right)\ne\varnothing$
- $\vec{x_0}\in\Omega$ si dice **punto isolato** di $\Omega$ se non è di accumulazione per $\Omega$
- $\Omega$ si dice **limitato** se $\exists\ R>0$ tale che $B_R(\vec O)\supset\Omega$
- $\Omega$ si dice **connesso** se non è l'unione di insiemi separati non vuoti,, ossia se $\nexists A,b\subseteq\Omega$ tale che $\Omega=A\cup B,\ A\cap\bar B=\bar A\cap B=\varnothing$


## Esempi
1) 
$D:f(x,y)=x+y,\ \text{Dom}(f)\in\mathbb R^2,\ \text{Im}(f)=\mathbb R$
$G(f)=\{(x,y,z\in\mathbb R^3|z=x+y)\}$

$L(f,k)=\{(x,y)\ |\ f(x,y)=k\}=\{(x,y)\ |\ x+y=k\}$

```functionplot
---
title: Curve di livello
xLabel: x
yLabel: y
bounds: [-5,5,-3,3]
disableZoom: false
grid: true
---
l0(x)=-x
l1(x)=-x+1
l2(x)=-x+2
l-1(x)=-x-1
l-2(x)=-x-2
```
$lasld$

2) 
$f(x,y)=x^2+y^2,\ \text{Dom}(f)=\mathbb R^2,\ \text{Im}(f)=[0,\infty)$

$L(f,k)=\{(x,y)\ |\ x^2+y^x=k\}$ è un cerchio di centro $O$ e segno $\sqrt k$

$L(f,0)=\{0,0\}$
$L(f,1)=\text{cerchio }C=(0,0),\ l=1$
$L(f,2)=\text{cerchio }C=(0,0),\ l=\sqrt2$

$L(f,-1)=\varnothing$

3) 
$f(x,y)=\sqrt{x^2+y^2},\ \text{Dom}(f)=\mathbb R^2,\ \text{Im}(f)=[0,\infty)$

$g(f)=\{(x,y,z)\ |\ \sqrt{x^2+y^2}=z\}=\{(x,y,z)\ |\ x^2+y^=z^2,\ z\ge0\}$

$L(f,k)=\begin{array}{c}\{(x,y)\ |\ x^2+y^2=z^2\}&\text{se }k\ge0\\\varnothing&\text{se }k<0\end{array}$

Se $k\ge0\Rightarrow L(f,k)$ è o; cerchio di $C=(0,0)$ e $r=K$

4) 
$f(x,y)=x^2-y^2,\ \text{Dom}(f)=\mathbb R^2,\ \text{Im}(f)=\mathbb R^2$

$L(f,k)=\{(x,y|x^2-y^2=k\}=\begin{array}{l}\text{iperbole con asisntoti }x=\pm y&\text{se }k\ne0 \\\text{la retta }x=\pm y&\text{se }k=0\end{array}\qquad\begin{array}{l}\text{passante per }(0,\sqrt{-k}&\text{se }x<0)\\\text{passante per }(\sqrt k,0)&\text{se }k>0\end{array}$

5) 
$f(x,y)=\ln(xy-x^2),\ \text{Dom}(f)=\{(x,y)\ |\ xy>x^2\}\rightarrow\begin{array}{l}y>x&\text{se }x>0\\y<x&\text{se }x<0\end{array}\qquad \text{Im}(f)=\mathbb R$

$L(f,k)=\{(c,y)\ |\ \ln(xy-x^2)=k\}=\{(x,y)\ |\ xy-x^2=e^k\}$ (iperbole ruotata con asintoti $x=0,\ x=y$)


6) 
$f(x,y)=\arcsin(\frac{x^2}4+y^2-2),\ \text{Dom}(f)=\{(x,y)\|-1\le\frac{x^2}4+y^2-2\le1\}=\{(x,y)\ |\ 1\le\frac{x^2}4+y^2\le3\},\ \text{Im}(f)=\left[-\frac\pi2,\frac\pi2\right]$

$L(f,k)=\{(x,y)\ |\ \arcsin(\frac{x^2}4+y^2-2)=k\}=\{(x,y)\ |\ \frac{x^2}4+y^2=2+\sin k$ se $k\in\text{Im}(f)$ ossia se $k\in\left[-\frac\pi2,\frac\pi2\right]$
