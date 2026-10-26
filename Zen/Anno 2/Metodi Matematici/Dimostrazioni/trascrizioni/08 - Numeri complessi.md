# Numeri complessi

$x^2 + 1 = 0 \qquad \nexists$ soluzioni in $\mathbb{R}$

Si introduce $i$, l'**unità immaginaria**, un numero t.c. $i^2 = -1$

$$\mathbb{C} := \{a + ib \;\text{ t.c. }\; a, b \in \mathbb{R}\}$$

- $a$ = parte reale $= \operatorname{Re}(z)$
- $b$ = parte immaginaria $= \operatorname{Im}(z)$

$\mathbb{R}$ è un campo ordinato: dati due qualunque numeri riesco a stabilire il maggiore.
$\mathbb{C}$ non è un campo ordinato.

### Operazioni tra numeri complessi

dati: $z_1 = a + ib$, $z_2 = c + id$ con $a,b,c,d \in \mathbb{R}$

#### Somma

$$z_1 + z_2 = a + c + i(b + d) = \operatorname{Re}(z_1 + z_2) + i\operatorname{Im}(z_1 + z_2)$$

es. $(1 + i) + (-2 + 3i) = -1 + 4i$

#### Prodotto

$$z_1\cdot z_2 = (a + ib)(c + id) = ac - bd + i(bc + ad)$$

### Complesso coniugato $\bar z$ (def.)

dato $z \in \mathbb{C}$, $\bar z = a - ib$ (con $z = a + ib$)

osservazione:

$$z = \bar z \iff z \in \mathbb{R}$$

$$z + \bar z = 2\operatorname{Re}(z)$$

$$z\cdot\bar z = (a + ib)(a - ib) = a^2 - i^2 b^2 = a^2 + b^2$$

### Norma di un numero complesso $N(z)$

$$N(z) = a^2 + b^2 \in \mathbb{R}$$

$$N(z) = 0 \iff z = 0 \qquad (a = b = 0)$$

### Inverso di un numero complesso

se $z \neq 0 \Rightarrow N(z) \neq 0$: l'inverso di $z$ sarà questo numero $\dfrac{1}{a^2 + b^2}\,\bar z \in \mathbb{C}$

per definizione di inverso: $z\cdot\dfrac{1}{a^2 + b^2}\,\bar z = 1$

$$\frac{1}{a^2 + b^2}\cdot\bar z \Rightarrow \left(\frac{a}{a^2 + b^2} - i\,\frac{b}{a^2 + b^2}\right)\bar z = z^{-1}$$

> [!warning] Fattore in eccesso
> Il $\bar z$ finale è di troppo: $z^{-1} = \dfrac{\bar z}{a^2 + b^2} = \dfrac{a}{a^2 + b^2} - i\,\dfrac{b}{a^2 + b^2}$.

$$\forall z \in \mathbb{C}^* \;\; \exists!\, z^{-1}$$

> [!note] Notazione
> $\mathbb{C}^* = \mathbb{C}\setminus\{0\}$.

### Forma algebrica

$a + ib$ con $a, b \in \mathbb{R}$

osservazioni:

$$a + ib = c + id \iff a = c,\; b = d$$

$z = a + ib$, l'opposto $-z = -a - ib = -a + i(-b)$

$$z + (-z) = 0$$

$\forall z \in \mathbb{C}^*$, $z$ è invertibile rispetto al prodotto, cioè $\exists z^{-1} \in \mathbb{C}$ t.c. $z^{-1}\cdot z = 1$

$$z^{-1} = \frac{\bar z}{N(z)} = \frac{\bar z}{a^2 + b^2} = \frac{a}{N(z)} + i\,\frac{b}{N(z)}$$

> [!warning] Segno
> Il segno della parte immaginaria è sbagliato: $z^{-1} = \dfrac{a}{N(z)} - i\,\dfrac{b}{N(z)}$. La verifica successiva usa correttamente $-\dfrac{b}{N(z)}$.

verifica:

$$z\cdot z^{-1} = 1 \Rightarrow (a + ib)\left(\frac{a}{N(z)} + i\cdot\left(-\frac{b}{N(z)}\right)\right) = 1$$

$$\frac{a^2}{N(z)} + \frac{b^2}{N(z)} + i\left(\frac{ab}{N(z)} - \frac{ab}{N(z)}\right) = \frac{a^2 + b^2}{N(z)} = \frac{N(z)}{N(z)} = 1$$

verifica: $z\cdot\bar z = N(z)$, $z = -3 + 2i$, $\dfrac{1}{z} = \dfrac{1}{-3 + 2i}$

$$\frac{1}{-3 + 2i}\cdot\frac{-3 - 2i}{-3 - 2i} = \frac{-3 - 2i}{13} = -\frac{3}{13} - \frac{2}{13}\,i$$
