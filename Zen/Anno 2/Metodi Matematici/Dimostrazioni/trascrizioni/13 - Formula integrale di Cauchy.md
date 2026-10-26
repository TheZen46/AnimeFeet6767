# Formula integrale di Cauchy

Sia $f : D \subset \mathbb{C} \to \mathbb{C}$

con $D$ un insieme semplicemente connesso e $C$ una curva chiusa semplice.

Sia $z_0$ un punto interno a $C$ $\Rightarrow$

$$f(z_0) = \frac{1}{2\pi i}\cdot\oint_C\frac{f(z)}{z - z_0}\,dz$$

> [!warning] Ipotesi
> Manca l'ipotesi che $f$ sia **olomorfa** su $D$, usata nella dimostrazione.

> [!note] Semplicemente connesso
> Un insieme connesso è **semplicemente connesso** se non ha "buchi": ogni curva chiusa in esso può essere deformata con continuità fino a un punto senza uscirne. Una curva **semplice** non ha autointersezioni.

### Dimostrazione

$z_0$ è interno a $C$ che è chiusa e supportata su $D$ semplicemente connesso $\Rightarrow z_0 \in D$

$$C_0 = \gamma_0 : [0, 2\pi] \to \mathbb{C}, \qquad \eta \to z_0 + \delta\cdot e^{i\eta}$$

Introduco $\tilde C = C * T * C_0^- * T^-$

La regione interna di $\tilde C$ è contenuta in $D$ ma non contiene $z_0$

$$D\setminus\{z_0\} \to \mathbb{C}, \qquad z \to \frac{f(z)}{z - z_0} \quad \text{è olomorfa su } D\setminus\{z_0\}$$

> [!info] Figura
> Insieme $D$ (rettangolo) contenente la curva chiusa $C$ (rossa, verso antiorario). Al suo interno la circonferenza $C_0$ (verde) di centro $z_0$ e raggio $\delta$. Il segmento $T$ collega $C$ a $C_0$. La regione tratteggiata compresa tra $C$ e $C_0$ è la regione interna di $\tilde C$, che esclude $z_0$. $\delta$ = raggio di $C_0$.
> ```tikz
> \begin{document}
> \begin{tikzpicture}[scale=1.1]
> \draw (0,0) rectangle (5,4);
> \node at (4.75,3.75) {$D$};
> \draw[thick,red] (2.5,2) ellipse (2 and 1.5);
> \node[red] at (4.65,2.9) {$C$};
> \draw[->,thick,red] (4.5,1.9) -- (4.5,2.1);
> \draw[thick,green!50!black] (2.8,2.2) circle (0.6);
> \node[green!50!black] at (3.6,2.75) {$C_0$};
> \fill (2.8,2.2) circle (1.2pt) node[left] {$z_0$};
> \draw (2.8,2.2) -- (3.4,2.2) node[midway,above] {$\delta$};
> \draw[->,thick] (2.8,0.52) -- (2.8,1.6);
> \node at (3.05,1.0) {$T$};
> \end{tikzpicture}
> \end{document}
> ```

> [!note] Cammino $\tilde C$
> $*$ indica la concatenazione di curve. Si percorre $C$, si entra lungo $T$, si percorre $C_0$ in verso opposto ($C_0^-$) e si torna indietro lungo $T$ ($T^-$). I due passaggi su $T$ si annullano, e $\tilde C$ racchiude una regione su cui $f(z)/(z - z_0)$ è olomorfa.

Uso il teorema di Cauchy:

$$\oint_{\tilde C}\frac{f(z)}{z - z_0}\,dz = 0$$

$$\int_C\frac{f(z)}{z - z_0}\,dz + \int_T\frac{f(z)}{z - z_0}\,dz - \int_{C_0}\frac{f(z)}{z - z_0}\,dz - \int_T\frac{f(z)}{z - z_0}\,dz = 0$$

Si vuole provare che

$$\int_C\frac{f(z)}{z - z_0}\,dz = \int_{C_0}\frac{f(z)}{z - z_0}\,dz$$

$$\int_C\frac{f(z)}{z - z_0}\,dz - 2\pi i\cdot f(z_0) = \int_{C_0}\frac{f(z)}{z - z_0}\,dz - 2\pi i\cdot f(z_0)$$

$$= \int_0^{2\pi}\frac{f(z_0 + \delta\cdot e^{i\eta})}{\delta\cdot e^{i\eta}}\cdot i\,\delta e^{i\eta}\,d\eta - 2\pi i\cdot f(z_0) = i\int_0^{2\pi} f(z_0 + \delta\cdot e^{i\eta}) - f(z_0)\,d\eta$$

$f$ olomorfa $\Rightarrow f$ continua

Posso fissare $\varepsilon > 0$ e trovare $\delta > 0$ t.c. $|z - z_0| \le \delta \Rightarrow |f(z) - f(z_0)| \le \varepsilon$

$$\left|\int_C\frac{f(z)}{z - z_0}\,dz - 2\pi i\cdot f(z_0)\right| = \left|\int_0^{2\pi} f(z_0 + \delta\cdot e^{i\eta}) - f(z_0)\,d\eta\right| \le$$

$$\le \int_0^{2\pi}\left|f(z_0 + \delta\cdot e^{i\eta}) - f(z_0)\right|d\eta \le 2\pi\cdot\varepsilon$$

La disuguaglianza vale $\forall \varepsilon > 0$

Quindi

$$\int_C\frac{f(z)}{z - z_0}\,dz - 2\pi i\cdot f(z_0) = 0 \qquad \square$$

> [!note] Perché si può scegliere $\delta$
> Il primo membro non dipende da $\delta$, grazie all'uguaglianza tra l'integrale su $C$ e quello su $C_0$. Si può quindi prendere il raggio $\delta$ piccolo quanto richiesto dalla continuità di $f$ in $z_0$.
