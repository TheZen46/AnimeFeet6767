# Teorema della funzione implicita

Sia $f : A \subset \mathbb{R}^2 \to \mathbb{R}$ con $f \in C^2_{(A)}$ a tratti e $\nabla f(x_0, y_0) \neq 0$

con $(x_0, y_0) \in A$ t.c. $f(x_0, y_0) = a$

Allora $\exists B$, un intorno di $(x_0, y_0)$ t.c. $\{(x,y) \in B \mid f(x,y) = a\}$ che coincide con $f(x)$ o con $\tilde g(y)$.

> [!warning] Notazione
> Si intende che l'insieme di livello coincide, in $B$, con il **grafico** di $g(x)$ oppure con quello di $\tilde g(y)$, come precisato subito dopo.

Più precisamente se $\partial_y f(x_0, y_0) \neq 0 \Rightarrow \exists g : I \subset \mathbb{R} \to \mathbb{R}$ t.c.

$$\{(x,y) \in B \mid f(x,y) = a\} = \{(x, g(x)) \mid x \in I\}$$

e se $\partial_x f(x_0, y_0) \neq 0 \Rightarrow \exists \tilde g : \tilde I \subset \mathbb{R} \to \mathbb{R}$ t.c.

$$\{(x,y) \in B \mid f(x,y) = a\} = \{(\tilde g(y), y) \mid y \in \tilde I\}$$

con $\tilde g \in C^2_{(\tilde I)}$ a tratti.

### Dimostrazione per $\partial_y f(x_0, y_0) \neq 0$

Per il teorema di permanenza del segno: $\exists r > 0$ t.c. $B((x_0, y_0), r) \in D$ e la $\partial_y f \neq 0$ su $B$.

Cerco $g : I \subset \mathbb{R} \to \mathbb{R}$ con $I$ un intorno aperto di $\mathbb{R}$ che contiene $x_0$ t.c. $f(x, g(x)) = a$

$$\forall x \in I \quad \text{vale} \quad \partial_x f(x, g(x)) + \partial_y f(x, g(x))\cdot g'(x) = 0$$

So che dentro $B$ $\partial_y f \neq 0$, quindi scrivo la relazione con il vincolo:

$$\begin{cases} g'(x) = -\dfrac{\partial_x f(x, g(x))}{\partial_y f(x, g(x))} \\[2mm] g(x_0) = y_0 \end{cases} \qquad \text{un problema di Cauchy}$$

$g'(x) \in C^1_{(B)}$: il problema ammette una sola soluzione definita su $I = (x_0 - \delta, x_0 + \delta)$, $\delta > 0$.

La soluzione è di classe $C^2$.

> [!note] Struttura dell'argomento
> La relazione $\partial_x f + \partial_y f\cdot g' = 0$ si ottiene derivando $f(x, g(x)) = a$ con la regola della catena. Il secondo membro dell'equazione differenziale è $C^1$, quindi localmente lipschitziano: il teorema di Cauchy-Lipschitz (esistenza e unicità locale) fornisce $g$. Poiché $g'$ è composizione di funzioni $C^1$, $g$ risulta di classe $C^2$.
