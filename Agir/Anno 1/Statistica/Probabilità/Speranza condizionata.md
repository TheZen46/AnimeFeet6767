# Formula della torre
$\mathbb E[X]=\mathbb E[X|Y=y_1]\mathbb E[Y=y_1]+\ldots+\mathbb E[X|Y=y_m]\mathbb E[Y=y_m]=\sum\limits_{i=1}^m\mathbb E[X|Y=y_i]\mathbb E[Y=y_i]$

# Varianza di una variabile aleatoria
$\operatorname{Var}[X]=\mathbb R\left[(X-\mathbb E[X])^2\right]=\sigma^2\ge0$

$\sigma=\sqrt{\operatorname{Var}[X]}\quad\text{Deviazione standard}$

$X\in\{x_1,\ldots,x_n\}\quad x\text{ finita}\quad x_i\ne x_j\quad i\ne j$

| $x$      | $\mathbb P[X=x]$       |
| -------- | ---------------------- |
| $x_1$    | $\mathbb P[X=x_1]=p_1$ |
| $x_2$    | $\mathbb P[X=x_2]=p_2$ |
| $\vdots$ |                        |
| $x_n$    | $\mathbb P[X=x_n]=p_n$ |
$\mathbb E[X]=x_1 p_1+x_2 p_2+\ldots+x_n p_n\quad\text{valora medio}$

$(X-\mathbb E[X])^2=(\text{Distanza dei valori dalla media})^2$

$\operatorname{Var}[X]=\text{Media delle}(\text{Distanze di }x\text{ dalla sua media})^2$


# Disuguaglianza di Cheryshev

$\forall\varepsilon>0$
$\mathbb P[|X-\mathbb R[X]|\ge\varepsilon]\le\frac{\operatorname{Var}[X]}{\varepsilon^2}$
