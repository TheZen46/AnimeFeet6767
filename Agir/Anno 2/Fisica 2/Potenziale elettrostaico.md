### Energia potenziale
$K_i+U_i=K_f+U_f$
$U=-W$
$dW=\vec F\cdot d\vec s$
$U_i=0$
$U=U_f-U_i=U_f$

### Potenziale elettrostatica
$U_i=U_{\infty}=0$
$\displaystyle F=K\frac{q_1 q_0}{r^2}$

$q_0>0$
	$\vec F\cdot d\vec s<0$
	$\displaystyle W=\int_i^f \vec F\cdot d\vec s$
$q_0<0$
	$\vec F\cdot d\vec s>0$

$\displaystyle V=\frac{U}{q_0}=-\frac{W}{q_0}\Leftarrow\text{potenziale}$
$\text{Volt}=\frac{\text{Joule}}{\text{Coulomb}}$

```tikz
\begin{document}
	\begin{tikzpicture}
		\draw[thick] (-2,-1) -- (2,1) node[midway, below]{1};
		\draw[thick] (-2,-1) arc[start angle=206.6, end angle=26.6, radius=2.236] node[midway, above]{2};
		\filldraw[orange] (-2,-1) circle (3pt) node[left]{A};
		\filldraw[green] (2,1) circle (3pt) node[right]{B};
	\end{tikzpicture}
\end{document}
```

1)
$\displaystyle \vec F\cdot d\vec s= F\ dr=k\frac{q\ q_0}{r^2}dr$
$\displaystyle dW=k\frac{q\ q_0}{r^2}dr$
$\displaystyle W=\int_A^B k\frac{q\ q_0}{r^2}dr=kq\ q_0\int_A^B\frac{dr}{r^2}=kq\ q_0\int_{r_A}^{r_B}\frac{dr}{r^2}=-\left.k\frac{q\ q_0}{r}\right|_{r_A}^{r_B}=-kq\ q_0\bigl(\frac1{r_B}-\frac1{r_A}\bigr)$

2)
$\displaystyle \vec F\cdot d\vec r=0\ \ \ \ \vec F\perp d\vec r$
$\displaystyle \int_A^B\vec F\cdot d\vec r=\int_A^B F\cdot dr=-kq\ q_0\bigl(\frac1{r_B}-\frac1{r_A}\bigr)$

$\displaystyle \begin{cases}W=\int\vec F\cdot d\vec S=\int q\vec E\cdot d\vec s=q\int\vec E\cdot d\vec s\\W=-qV\end{cases}$
$\displaystyle -\cancel qV=\cancel q\int\vec E\cdot d\vec s\Rightarrow V=-\int\vec E\cdot d\vec s$



## Superfici equipotenziali
$V=\text{cost}$
$V_A=V_B$
$\Delta V=V_B-V_A=0\Rightarrow W=0$
$\Delta V=V_3-V_1$



