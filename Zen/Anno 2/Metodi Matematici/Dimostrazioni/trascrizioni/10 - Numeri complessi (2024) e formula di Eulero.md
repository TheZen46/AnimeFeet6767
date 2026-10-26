# Numeri complessi (2024)

prop. sia $z$ un numero t.c. $z \in \mathbb{C}$

| | |
|---|---|
| $\overline{(\bar z)} = z$ | $\overline{(z + w)} = \bar z + \bar w$ |
| $\lvert\bar z\rvert = z$ | $\overline{(z\cdot w)} = \bar z\cdot\bar w$ |
| $\lvert z\rvert = 0 \iff z = 0$ | $z\cdot\bar z = a^2 + b^2 = \lvert z\rvert^2$ |
| $\forall z \neq 0 \quad \overline{z^{-1}} = (\bar z)^{-1}$ | $z + \bar z = 2a$ |

> [!warning] Modulo del coniugato
> La proprietà corretta è $|\bar z| = |z|$.

**def.** Si definisce **argomento** di un numero complesso l'angolo che si forma tra l'asse reale e la semiretta che collega $z$ con l'origine.

$$\sin(\operatorname{Arg}(z)) = \frac{b}{|z|} \qquad b = |z|\cdot\sin(\operatorname{Arg}(z))$$

$$\cos(\operatorname{Arg}(z)) = \frac{a}{|z|} \qquad a = |z|\cdot\cos(\operatorname{Arg}(z))$$

$$z = a + ib = |z|\cdot\cos(\operatorname{Arg}(z)) + |z|\,i\sin(\operatorname{Arg}(z)) =$$

$$= |z|\cdot\big(\cos(\arg(z)) + i\sin(\arg(z))\big)$$

$$\tan(\arg(z)) = \frac{\sin(\arg(z))}{\cos(\arg(z))} = \frac{b/|z|}{a/|z|} = \frac{b}{a} \qquad \text{con } a \neq 0$$

### Ricavare l'opposto

$z\cdot w$ t.c. $z\cdot w = 1$, $w = z^{-1}$

> [!warning] Terminologia
> Si sta ricavando l'**inverso** (rispetto al prodotto), non l'opposto.

$$z^{-1} = \frac{\bar z}{|z|^2} \qquad \cos(-\alpha) = \cos\alpha, \quad \sin(-\alpha) = -\sin\alpha$$

$$z = |z|(\cos\alpha + i\sin\alpha), \qquad z^{-1} = \frac{1}{|z|}(\cos\beta + i\sin\beta)$$

$$\Rightarrow z\cdot z^{-1} = \frac{|z|}{|z|}\big(\cos\alpha\cos\beta + i\cos\alpha\sin\beta + i\sin\alpha\cos\beta + i^2\sin\alpha\sin\beta\big) = 1$$

$$= \underbrace{\cos\alpha\cos\beta - \sin\alpha\sin\beta}_{=1} + \underbrace{i(\cos\alpha\sin\beta + \cos\beta\sin\alpha)}_{=0} = 1$$

$\beta = -\alpha \;\to$

$$= \cos\alpha\cdot\cos(-\alpha) - \sin\alpha\sin(-\alpha) + i\big(\cos(\alpha)\sin(-\alpha) + \cos(-\alpha)\sin\alpha\big) = 1$$

$\cos\alpha = \cos(-\alpha)$, $-\sin\alpha = \sin(-\alpha) \;\to$

$$= \cos\alpha\cos\alpha - \sin\alpha(-\sin\alpha) + i\big(\cos\alpha\cdot(-\sin\alpha) + \cos\alpha\sin\alpha\big) = 1$$

$\cos^2 x + \sin^2 x = 1 \;\to$

$$= \cos^2\alpha + \sin^2\alpha + i\cdot 0 = 1 \Rightarrow 1 = 1$$

> [!note] Conclusione
> La scelta $\beta = -\alpha$ soddisfa le due condizioni (parte reale $= 1$, parte immaginaria $= 0$). Quindi l'inverso ha modulo $1/|z|$ e argomento $-\alpha$.

### Formula di Eulero

sia $z = \alpha + i\beta \in \mathbb{C}$

$$e^z = e^\alpha\underbrace{(\cos\beta + i\sin\beta)}_{e^{i\beta}} = e^a\cdot e^{ib} = e^{a + ib}$$

$$z = |z|(\cos\alpha + i\sin\alpha) = |z|\,e^{i\alpha} \qquad \textit{forma esponenziale}$$

proprietà:

- $z\cdot w = |z|\cdot|w|\cdot e^{i(\arg(z) + \arg(w))}$
- $z^{-1} = \dfrac{1}{|z|}\cdot e^{-i\alpha}$

### Equazioni di forma $x^n = w$

con $w \in \mathbb{C}$, $\theta = \arg w$

$$w = |w|\cdot e^{i\theta}$$

$$x^n = |w|\cdot e^{i\theta}$$

$$x = \sqrt[n]{|w|}\cdot\left(e^{i\theta}\right)^{1/n} = \sqrt[n]{|w|}\cdot e^{i\theta/n}$$

$$n\cdot\arg(x) = \theta + 2k\pi \qquad k \in \mathbb{N},\; 0 \le k \le n-1$$

esempio: $x^3 = 1 \;\to\; |w| = 1$, $\theta = 0$

$$|x| = \sqrt[3]{1} = 1$$

$$3\arg(x) = \theta + 2k\pi \qquad k \in \mathbb{N},\; 0 \le k \le 2$$

$$3\arg(x) = 2k\pi$$

$$\arg(x) = \frac{2\pi}{3}\cdot k$$

$$x_1 = 1\cdot e^{i0}, \qquad x_2 = 1\cdot e^{i\frac{2}{3}\pi}, \qquad x_3 = e^{i\frac{4}{3}\pi}$$
