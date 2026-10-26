# Condizioni di Cauchy-Riemann

Sia $f = u + i\cdot v$ una funzione $f : D \subset \mathbb{C} \to \mathbb{C}$, $\; z \mapsto f(z)$

$$x + iy \to u(x,y) + i\cdot v(x,y) \qquad z_0 = (x_0, y_0) \in D$$

**1]** Se $\exists f'(z_0)$ con $z_0 \in D \Rightarrow \exists$ le derivate parziali di $u, v$ in $z_0$

$$\begin{cases} u_x(x_0, y_0) = v_y(x_0, y_0) \\ u_y(x_0, y_0) = -v_x(x_0, y_0) \end{cases} \qquad \text{valgono le condizioni di Cauchy-Riemann}$$

### Dimostrazione

Per ipotesi

$$\exists f'(z_0) = \lim_{z\to z_0}\frac{f(z) - f(z_0)}{z - z_0} \in \mathbb{C}$$

considero 2 restrizioni.

> [!note] Idea
> Se il limite esiste in $\mathbb{C}$, deve valere lo stesso lungo qualunque direzione di avvicinamento. Confrontando la direzione reale ($h$) e quella immaginaria ($ih$) si ottengono le due condizioni.

**Restrizione 1:** $z = z_0 + h$, $h \in \mathbb{R}$, $h \to 0$

$$z_0 + h = \begin{cases} x = x_0 + h \\ y = y_0 \end{cases}$$

$$\frac{f(z) - f(z_0)}{z - z_0} = \frac{[u(x,y) + i\cdot v(x,y)] - [u(x_0,y_0) + i\,v(x_0,y_0)]}{h} =$$

$$= \frac{u(x,y) - u(x_0,y_0)}{h} + i\,\frac{v(x,y) - v(x_0,y_0)}{h} =$$

$$= \frac{u(x_0 + h, y_0) - u(x_0,y_0)}{h} + i\,\frac{v(x_0 + h, y_0) - v(x_0,y_0)}{h} =$$

$$\lim_{h\to 0}\frac{f(z) - f(z_0)}{h} = \lim_{h\to 0}\frac{u(x_0 + h, y_0) - u(x_0,y_0)}{h} + i\,\frac{v(x_0 + h, y_0) - v(x_0,y_0)}{h} =$$

$$= u_x(x_0,y_0) + i\,v_x(x_0,y_0) = f'(z_0)$$

**Restrizione 2:** $z = z_0 + ih$

$$z_0 + ih = \begin{cases} x = x_0 \\ y = y_0 + h \end{cases}$$

$$\lim_{h\to 0}\frac{f(z) - f(z_0)}{ih} = \lim_{h\to 0}\frac{u(x,y) - u(x_0,y_0)}{ih} + \cancel{i}\,\frac{v(x,y) - v(x_0,y_0)}{\cancel{i}h} =$$

$$= \lim_{h\to 0} -i\,\frac{u(x_0, y_0 + h) - u(x_0,y_0)}{h} + \frac{v(x_0, y_0 + h) - v(x_0,y_0)}{h} =$$

$$= v_y(x_0,y_0) - i\,u_y(x_0,y_0) = f'(z_0)$$

> [!note] Passaggio
> Si è usato $\frac{1}{i} = -i$.

Quindi $u_x(x_0,y_0) = v_y(x_0,y_0)$ e $v_x(x_0,y_0) = -u_y(x_0,y_0)$ $\square$

**2]** Se $u, v$ sono differenziabili in $(x_0, y_0)$ e valgono le C.R.

allora $\exists f'(z_0) = f'(x_0 + i\,y_0)$, $\quad f'(z_0) = u_x(x_0,y_0) + i\,v_x(x_0,y_0)$

### Dimostrazione

$$\text{differenziabili} \Rightarrow \begin{cases} u(x,y) = u(x_0,y_0) + u_x(x_0,y_0)\cdot(x - x_0) + u_y(x_0,y_0)\cdot(y - y_0) + o(|z - z_0|) \\ v(x,y) = v(x_0,y_0) + \underbrace{v_x(x_0,y_0)}_{-u_y(x_0,y_0)}\cdot(x - x_0) + \underbrace{v_y(x_0,y_0)}_{u_x(x_0,y_0)}\cdot(y - y_0) + o(|z - z_0|) \end{cases} \leftarrow \text{C.R.}$$

$$f(z) - f(z_0) = u(x,y) + i\,v(x,y) - u(x_0,y_0) - i\,v(x_0,y_0) =$$

$$= u(x,y) - u(x_0,y_0) + i\,[v(x,y) - v(x_0,y_0)] =$$

$$= u_x(x_0,y_0)(x - x_0) + u_y(x_0,y_0)(y - y_0) + o(|z - z_0|) + i\,[v_x(x_0,y_0)(x - x_0) + v_y(x_0,y_0)(y - y_0) + o(|z - z_0|)] =$$

$$= u_x(x_0,y_0)(x - x_0) + u_y(x_0,y_0)(y - y_0) + o(|z - z_0|) + i\,[-u_y(x_0,y_0)(x - x_0) + u_x(x_0,y_0)(y - y_0) + o(|z - z_0|)] =$$

$$= [u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot(x - x_0) + [u_y(x_0,y_0) + i\,u_x(x_0,y_0)]\cdot(y - y_0) + o(|z - z_0|) =$$

$$= [u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot(x - x_0) + i\,[u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot(y - y_0) + o(|z - z_0|) =$$

$$= [u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot[(x - x_0) + i(y - y_0)] + o(|z - z_0|) =$$

$$= [u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot(z - z_0) + o(|z - z_0|)$$

$$\frac{f(z) - f(z_0)}{z - z_0} = [u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot\frac{z - z_0}{z - z_0} + \frac{o(|z - z_0|)}{z - z_0} =$$

$$= [u_x(x_0,y_0) - i\,u_y(x_0,y_0)]\cdot 1 + 0 =$$

$$= u_x(x_0,y_0) - i\,u_y(x_0,y_0) = u_x(x_0,y_0) + i\,v_x(x_0,y_0) = f'(z_0) \qquad$$

> [!note] Passaggio al limite
> Le ultime due righe valgono nel limite $z \to z_0$: è il termine $\frac{o(|z - z_0|)}{z - z_0}$ a tendere a $0$.
