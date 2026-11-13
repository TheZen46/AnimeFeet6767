Una condizione di equilibrio lascia lo stato del sistema inalterato nel tempo

$\dot x=f(x,u)\\y=g(x,u)\\\pmatrix{x_{ep}\\u_{ep}}\\f\bigl(x_{ep},u_{ep}\bigr)=0\\y_{ep}=g\bigl(x_{ep},u_{ep}\bigr)$

Stabilità di punto di equilibrio:

$\dot x=f(x,eq)$

1) $\boxed{1}\text{ Punto di equilibrio stabile: }\forall\epsilon>0\m{12}\exists\deleps>0:\m{12}\norm{x(0)-x_{ep}}\le\deleps\to\norm{x(t)-x_{ep}}\le\epsilon\quad\forall t$
2) $\text{Punto asintoticamente stabile: }\text{Se vale }\boxed{1}\text{ e }\lim\limits_{\Large{t\to\infty}}\norm{x(t)-x_{ep}}=0$
3) $\text{Punto instabile:} \text{Se non vale }\boxed{1}$

$\dot x=Ax+Bu\Rightarrow 0=Ax_{ep}+Bu_{ep}$
$\delta x=x-x_{ep}$
$\delta\dot x=\dot x-0=A_x+\cancel{Bu_{ep}}-Ax_{ep}-\cancel{Bu_{ep}}$
$\delta\dot x=A\delta x$

Un sistema è stabile se il polinomio caratteristico della matrice A ha poli con $\Re<0$ o $\Re=0$ con molteplicità $1$
Un sistema lineare è instabile quando il polinomio minimo della matrice $A$ ha poli con $\Re>0$ e/o poli con $\Re=0$ con molteplicità $>1$
