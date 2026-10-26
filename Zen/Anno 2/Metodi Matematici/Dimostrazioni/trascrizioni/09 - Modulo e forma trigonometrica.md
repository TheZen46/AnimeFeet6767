# Modulo di un numero complesso $|z|$

$z = \sqrt{a + ib}$ [?] $\qquad z \in \mathbb{R} \Rightarrow |z| = |a|$

> [!warning] Prima riga
> Si intende $z = a + ib$. Il modulo è definito dalla riga successiva.

$$|z| = \sqrt{a^2 + b^2} = \sqrt{N(z)}$$

### Proprietà $|z|$

$$|z_1\cdot z_2| = |z_1|\cdot|z_2|$$

$$|z_1 + z_2| \neq |z_1| + |z_2| \qquad \neq \text{ in generale}$$

$$|z_1 + z_2| \le |z_1| + |z_2| \qquad \text{disuguaglianza triangolare}$$

### Forma geometrica

$$a + ib \leftrightarrow (a, b)$$

Legenda dei colori nel disegno: verde $\theta$, rosso $|z|$, viola $b$, blu $a$.

> [!info] Figura
> Piano di Gauss con assi $\operatorname{Re}(z)$ e $\operatorname{Im}(z)$. Il punto $z = (a,b)$ è collegato all'origine da un segmento di lunghezza $|z|$ (rosso); le proiezioni tratteggiate sugli assi individuano $a$ (blu) e $b$ (viola); l'angolo tra l'asse reale e il segmento è $\theta$ (verde).
> ```tikz
> \begin{document}
> \begin{tikzpicture}[scale=1.3]
> \draw[->] (-1,0) -- (3,0) node[right] {$\mathrm{Re}(z)$};
> \draw[->] (0,-1) -- (0,2.3) node[above] {$\mathrm{Im}(z)$};
> \draw[thick,red] (0,0) -- (2,1.5);
> \draw[dashed,blue] (2,1.5) -- (2,0);
> \draw[dashed,violet] (2,1.5) -- (0,1.5);
> \fill (2,1.5) circle (1.5pt) node[above right] {$z$};
> \draw[green!50!black] (0.5,0) arc (0:36.87:0.5);
> \node[green!50!black] at (0.75,0.2) {$\theta$};
> \node[red] at (0.9,0.95) {$|z|$};
> \node[blue] at (1,-0.25) {$a$};
> \node[violet] at (-0.25,0.75) {$b$};
> \end{tikzpicture}
> \end{document}
> ```

$$|z| = \sqrt{a^2 + b^2} = \rho$$

$$a = \rho\cos\theta \qquad b = \rho\sin\theta$$

$$\theta = \operatorname{Arg}(z) \qquad 0 \le \theta < 2\pi \qquad \theta \bmod (2\pi)$$

### Forma trigonometrica

$$z = \rho(\cos\theta + i\sin\theta)$$

$z = 1 + i$, $\quad a = 1,\; b = 1,\; \rho = \sqrt 2$

$$\cos\theta = \frac{a}{\rho} = \frac{1}{\sqrt 2} \qquad \sin\theta = \frac{b}{\rho} = \frac{\sqrt 2}{2} \qquad \theta = \frac{\pi}{4}$$

osservazione:

$$\bar z = \rho\big(\cos(-\theta) + i\sin(-\theta)\big) = \rho\big(\cos(2\pi - \theta) + i\sin(2\pi - \theta)\big)$$

$$N(z) = \rho^2 \qquad z^{-1} = \frac{\bar z}{N(z)} = \frac{1}{\rho}\big(\cos(-\theta) + i\sin(-\theta)\big) \qquad z \neq 0$$

proprietà:

$$z_1 = \rho_1(\cos\theta_1 + i\sin\theta_1) \qquad z_2 = \rho_2(\cos\theta_2 + i\sin\theta_2)$$

$$z_1 z_2 = \rho_1\rho_2\big(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\big)$$

$$= \rho_1\rho_2\big[(\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2) + i(\cos\theta_1\sin\theta_2 + \sin\theta_1\cos\theta_2)\big]$$

> [!note] Interpretazione
> Nel prodotto i moduli si moltiplicano e gli argomenti si sommano. L'ultima riga è lo sviluppo diretto del prodotto, ricondotto alla prima tramite le formule di addizione di seno e coseno.

### Potenza

$$z = \rho(\cos\theta + i\sin\theta)$$

$$z^2 = \rho^2(\cos 2\theta + i\sin 2\theta)$$

$$z^n = \rho^n(\cos n\theta + i\sin n\theta) \qquad \cancel{n \ge 1}\;\; \forall n \in \mathbb{Z}$$

> [!note] Formula di De Moivre
> È la formula di De Moivre: discende dal prodotto applicato $n$ volte. Vale anche per $n$ negativo, usando l'espressione di $z^{-1}$ data sopra.

### Divisione

$$\frac{z_1}{z_2} = z_1\cdot\frac{1}{z_2} = \frac{\rho_1}{\rho_2}\big(\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)\big) \qquad z_2 \neq 0$$

### Radici

cerco i numeri complessi $x = c(\cos\varphi + i\sin\varphi)$ che verificano $x^n = z$

quindi

$$x^n = c^n(\cos n\varphi + i\sin n\varphi) = \rho(\cos\theta + i\sin\theta)$$

$$\Rightarrow \begin{cases} c^n = \rho & (c, \rho \in \mathbb{R}_{>0}) \\ n\varphi \equiv \theta & \bmod (2\pi) \end{cases} = \begin{cases} c = \sqrt[n]{\rho} \\ n\varphi = \theta + 2k\pi & k \in \mathbb{Z} \end{cases}$$

$$\begin{cases} c = \sqrt[n]{\rho} \\[1mm] \varphi = \dfrac{\theta + 2k\pi}{n} & k \in \mathbb{Z} \end{cases} \qquad \begin{aligned} k = 0 &\quad \varphi = \theta/n \\ k = 1 &\quad \varphi = \theta/n + 2\pi/n \\ &\;\;\vdots \end{aligned}$$

le soluzioni

$$x_k = \sqrt[n]{\rho}\left(\cos\frac{\theta + 2k\pi}{n} + i\sin\frac{\theta + 2k\pi}{n}\right) \qquad k \in \mathbb{Z}$$

si trovano per i $k$ fino a $n - 1$ (poi si ripetono): $k = nq + r$, $0 \le r \le n - 1$, $\varphi = \theta/n + 2\pi r/n$ [?] [illeggibile]

> [!note] Perché $n$ radici
> Scrivendo $k = nq + r$ si ha $\varphi = \frac{\theta}{n} + \frac{2\pi r}{n} + 2\pi q$: il termine $2\pi q$ non cambia il punto. Le radici distinte sono quindi esattamente $n$, per $k = 0, \dots, n-1$, e sono i vertici di un poligono regolare inscritto nella circonferenza di raggio $\sqrt[n]{\rho}$.
