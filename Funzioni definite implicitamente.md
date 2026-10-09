Consideriamo $f:D\subset\mathbb R^2\to\mathbb R$
$\bigl\{(x,y)\in D\ |\ f(x,y)=a\bigr\}\leftarrow\text{Una curva di livello costante }y=g(x)\text{ oppure }\tilde g(y)=x$

# Teorema della funzione implicita
$f:D\subset\mathbb R^2\to\mathbb R\qquad D\text{ aperto}$
$f\in C^1(D)$
$(x_o,y_0)\in D\qquad f(x_0,y_0)=a$
$\underset{\small{(x_0,y_0)}}{\nabla f}\ne0$
$\Rightarrow\exists B\text{ intorno di }(x_0,y_0)\text{ t.c. }\bigl\{(x,y)\in B\ |\ f(x,y)=a\bigr\}\text{ coincide con il grafico di una funzione di classe }C^1\ y=g(x)\text{ o }\tilde g(y)=x$
$\displaystyle \text{Più precisamente: Se }\frac{\partial f}{\partial y}(x_0,y_0)\ne0\Longrightarrow\exists g:I\subset\mathbb R\to\mathbb R\text{ t.c. }(x,y)\in B\ |\ f(x,y)=a\quad x\in I\quad y=g(x)$
$\displaystyle \text{Se}\frac{\partial f}{\partial y}(x_0,y_0)\ne0\Longrightarrow\exists \tilde g:J\subset\mathbb R\to\mathbb R\text{ t.c. }\ \ x=\tilde g(y)\text{ sono tali che }f(\tilde g(y),y)=a$

## Dimostrazione
Consideriamo il caso $\displaystyle \frac{\partial f}{\partial y}(x_0,y_0)\ne0$
Caso $f\in C$
Per il teorema di permanenza del segno, per la continuità di $\displaystyle \frac{\partial f}{\partial y},\quad\exists B\bigl((x_0,y_0),\sigma\bigr)=B'\text{ t.c. in }B'\ \frac{\partial f}{\partial y}\ne0\qquad g:I\subset\mathbb R\to\mathbb R\text{ t.c. }f\bigl(x,g(x)\bigr)=a$
$\displaystyle \frac{df}{dx}\bigl(x,g(x)\bigr)=\frac{\partial f}{\partial x}\bigl(x,g(x)\bigr)+\frac{\partial f}{\partial y}\bigl(x,g(x)\bigr)g'(x)$
$x\to\bigl(x,g(x)\bigr)$

$\partial_x f\bigl(x,g(x)\bigr)+\partial_yf\bigl(x,g(x)\bigr)g'(x)=0\Rightarrow \partial_x f\bigl(x,g(x)\bigr)=-\partial_yf\bigl(x,g(x)\bigr)g'(x)\Rightarrow \cases{g'(x)=-\frac{\partial_x f\bigl(x,g(x)\bigr)}{\partial_y f\bigl(x,g(x)\bigr)}\\g(x_0)=y_0}$
Ipotesi $\exists!$ soluzione
Teorema di Cauchy
$\exists\ I\subset\mathbb R\quad x_0\in I\text{ t.c. }\exists!\ g(x)$ che risolve il problema

### Osservazione
$x\mapsto g(x)$
$f\bigl(x,g(x)\bigr)=a$
