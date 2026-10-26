# Teorema dei residui

Sia $D \subset \mathbb{C}$ un sottoinsieme semplicemente connesso.

Siano $z_1, \dots, z_n \in D$ i punti singolari isolati di $f(z)$ olomorfa, $f : D\setminus\{z_1, \dots, z_n\} \subset \mathbb{C} \to \mathbb{C}$.

Presa una curva chiusa semplice supportata in $D$ che contiene $z_1, \dots, z_n$

vale la formula

$$\oint_C f(z)\,dz = 2\pi i\cdot\sum_{k=1}^{n}\operatorname{Res}(f, z_k)$$

> [!note] Residuo
> Il **residuo** di $f$ in una singolarità isolata $z_k$ è il coefficiente $c_{-1}$ dello sviluppo di Laurent di $f$ attorno a $z_k$. Equivalentemente, $\operatorname{Res}(f, z_k) = \frac{1}{2\pi i}\oint_{C_k} f(z)\,dz$, con $C_k$ una piccola circonferenza attorno a $z_k$ percorsa in verso antiorario. È questa identità a giustificare il penultimo passaggio della dimostrazione.

### Dimostrazione

> [!info] Figura
> Curva chiusa $C$ (rossa, verso antiorario; nell'originale ha forma a "boomerang") che racchiude tre singolarità $z_1, z_2, z_3$. Attorno a ciascuna è tracciata una piccola circonferenza $C_k$ (verde). I segmenti $T_k$ collegano $C$ a ciascuna $C_k$.
> ```tikz
> \begin{document}
> \begin{tikzpicture}[scale=1.0]
> \draw[thick,red] (3,1.5) ellipse (3 and 1.5);
> \draw[->,thick,red] (6,1.4) -- (6,1.6);
> \node[red] at (6.3,2.3) {$C$};
> \draw[thick,green!50!black] (1.5,1.5) circle (0.35);
> \draw[thick,green!50!black] (3,2.0) circle (0.35);
> \draw[thick,green!50!black] (4.5,1.2) circle (0.35);
> \fill (1.5,1.5) circle (1.2pt) node[right] {$z_1$};
> \fill (3,2.0) circle (1.2pt) node[right] {$z_2$};
> \fill (4.5,1.2) circle (1.2pt) node[right] {$z_3$};
> \node[green!50!black] at (1.5,2.1) {$C_1$};
> \node[green!50!black] at (3,2.6) {$C_2$};
> \node[green!50!black] at (4.5,1.8) {$C_3$};
> \draw[thick] (1.5,0.2) -- (1.5,1.15) node[midway,left] {$T_1$};
> \draw[thick] (3,0) -- (3,1.65) node[midway,left] {$T_2$};
> \draw[thick] (4.5,0.2) -- (4.5,0.85) node[midway,left] {$T_3$};
> \end{tikzpicture}
> \end{document}
> ```

Dal cammino scelto sulla curva $C$ e sui segmenti $T$, escludo i punti interni di $C_1, C_2, C_3$.

Il cammino si chiama $\tilde C$.

Per il teorema di Cauchy $\displaystyle\oint_{\tilde C} f(z)\,dz = 0$

$$\int_C f(z)\,dz = \sum_{k=1}^{n}\int_{C_k} f(z)\,dz + \int_{T_k} f(z)\,dz - \int_{T_k} f(z)\,dz =$$

$$= \sum_{k=1}^{n}\int_{C_k} f(z)\,dz =$$

$$= \sum_{k=1}^{n} 2\pi i\cdot\operatorname{Res}(f, z_k) =$$

$$\oint_C f(z)\,dz = 2\pi i\cdot\sum_{k=1}^{n}\operatorname{Res}(f, z_k) \qquad$$
