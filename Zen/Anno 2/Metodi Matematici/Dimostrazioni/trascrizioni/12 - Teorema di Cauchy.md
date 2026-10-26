# Teorema di Cauchy

Siano: $f : D \subset \mathbb{C} \to \mathbb{C}$ **olomorfa** e $C$ una curva chiusa.

Se il bordo di $C$ e $A_C$ la sua regione interna $A_C$ sono contenuti in $D$ $\Rightarrow$

$$\oint_C f(z)\,dz = 0$$

> [!note] Olomorfa
> Una funzione è **olomorfa** su un aperto se è derivabile in senso complesso in ogni suo punto.

### Dimostrazione

Sia $\gamma : [a,b] \to D \subset \mathbb{C}$ una parametrizzazione di $C$, una curva chiusa.

$$\int_C f(z)\,dz = \int_a^b (f\circ\gamma)(\eta)\cdot\gamma'(\eta)\,d\eta \qquad f(z) = u(x,y) + i\,v(x,y) \qquad \gamma(\eta) = x(\eta) + i\cdot y(\eta)$$

$$= \int_a^b [u(x(\eta), y(\eta)) + i\cdot v(x(\eta), y(\eta))]\cdot(x'(\eta) + i\cdot y'(\eta))\,d\eta =$$

$$= \int_a^b u(x(\eta),y(\eta))\cdot x'(\eta) - v(x(\eta),y(\eta))\cdot y'(\eta)\,d\eta + i\int_a^b u(x(\eta),y(\eta))\cdot y'(\eta) + v(x(\eta),y(\eta))\cdot x'(\eta)\,d\eta =$$

$$\int_a^b u(x(\eta),y(\eta))\cdot x'(\eta)\,d\eta = \int_C u(x,y)\,dx \qquad \int_a^b u(x(\eta),y(\eta))\cdot y'(\eta)\,d\eta = \int_C u(x,y)\,dy$$

$$= \int_C u(x,y)\,dx - \int_C v(x,y)\,dy + i\int_C u(x,y)\,dy + i\int_C v(x,y)\,dx = \qquad \text{ora Gauss-Green}$$

$$= -\iint_{A_C} u_y(x,y)\,dx\,dy - \iint_{A_C} v_x(x,y)\,dx\,dy + i\iint_{A_C} u_x(x,y)\,dx\,dy - i\iint_{A_C} v_y(x,y)\,dx\,dy =$$

$$= -\iint_{A_C} u_y(x,y) + v_x(x,y)\,dx\,dy + i\iint_{A_C} u_x(x,y) - v_y(x,y)\,dx\,dy = \qquad \text{applico le C.R.}$$

$$= -\iint_{A_C} u_y(x,y) - u_y(x,y)\,dx\,dy + i\iint_{A_C} u_x(x,y) - u_x(x,y)\,dx\,dy = 0$$

$$\oint_C f(z)\,dz = 0 \qquad \square$$

$f$ è olomorfa, $A_C \subset D \Rightarrow \forall z \in A_C$ valgono le condizioni di Cauchy-Riemann.

> [!note] Applicazione di Gauss-Green
> Con $\int_C P\,dx + Q\,dy = \iint (Q_x - P_y)$: per la parte reale $P = u$, $Q = -v$; per la parte immaginaria $P = v$, $Q = u$. Questa dimostrazione richiede che $u, v$ siano di classe $C^1$, ipotesi necessaria per applicare Gauss-Green.
