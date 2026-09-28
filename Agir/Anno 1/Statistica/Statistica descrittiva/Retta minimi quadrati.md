$x_1,\ldots,x_n\in\mathbb R\quad \text(altezza)$
$y_1,\ldots,y_n\in\mathbb R\quad \text(peso)$

$x_{\text{new}}$
$x\to y=f(x)$
$y_{\text{new}}=f(x_{\text{new}})$

$y=mx+q=f(x)$
$\tan\theta=m$
```chart
type: line
labels: [x1, x2, xnew, xn]
series:
  - title: 
    data: [2, 4, 1, 3]
tension: 0.34
width: 80%
labelColors: false
fill: false
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```


| $x_1$    | $y_1$    | $\hat y_1=mx_1+q$ | $y_1-\hat y_1=r_1$ |
| -------- | -------- | ----------------- | ------------------ |
| $\vdots$ | $\vdots$ | $\vdots$          | $\vdots$           |
| $x_n$    | $y_n$    | $\hat y_n=mx_q$   | $y_n-\hat y_n=r_n$ |

$\frac{|r_1|+|r_2|+\ldots+|r_n|}n=\text{errore Laplace}\rightarrow(m,q)\text{minimizzano l'errore}$
$\frac{{r_1}^2+{r_2}^2+\ldots+{r_n}^2}n=\text{errore Legendre/Gauss}\rightarrow m,q\text{minimizzo errore}\rightarrow\text{retta minimi quadrati}$

# Definizione
Dati un campione $\begin{array}{l}x_1,\ldots,x_n\\y_1,\ldots,y_n\end{array}$ si chiama **retta dei minimi quadrati** la retta $y=m^\star x+q^\star$ dove $m^\star,q^\star$ sono la soluzione del problema di minimo $\frac1n\left[(y_1-(mx_1+q))^2+\ldots(y_n-(mx_n+q))^2\right]=\frac1n\left[(\underbrace{y_1-\hat y_1}_{r_1})^2+\ldots(\underbrace{y_n-\hat y_n}_{r_1})^2\right]=\text{errore quadratico medio}=MSE$
# Teorema
La retta dei minimi quadrati è data da $y=\frac{\sigma_y}{\sigma_x}\rho_{x,y}(x-\overline x)+\overline y$
$\frac1n\left[(\underbrace{y_1-\hat y_1}_{r_1})^2+\ldots(\underbrace{y_n-\hat y_n}_{r_1})^2\right]={\sigma_y}^2(1-{\rho_{x,y}}^2)$
$\displaystyle\hat y_1=\frac{\sigma_y}{\sigma_x}\rho_{x,y}(x_1-\overline x)+\overline y,\; \ldots,\;\hat y_n=\frac{\sigma_y}{\sigma_x}\rho_{x,y}(x_n-\overline x)+\overline y$

$\tan\theta=\frac{\sigma_y}{\sigma_x}\rho{x_y}$

$\rho{x_y}>0 \nearrow\quad x\text{ e }y\text{ sono positivamente correlate}$
$\rho{x_y}<0 \searrow\quad x\text{ e }y\text{ sono negativamente correlate}$
$\rho{x_y}=0\quad x\text{ e }y\text{ sono scorrelate}$

$\overbrace{\rho_{x,y}}^{-1\le\rho_{x,y}\le1}=\pm1\Rightarrow\text{errore zero}\quad\begin{array}{l}y_1=m^\star x_1+q^\star\\\vdots\\y_n=m^\star x_n+q^\star\end{array}$
