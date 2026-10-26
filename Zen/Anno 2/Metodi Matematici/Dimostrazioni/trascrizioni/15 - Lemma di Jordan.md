# Lemma di Jordan

Sia $g : \mathbb{C}\setminus\{\text{un disco}\} \to \mathbb{C}$ una funzione continua.

Suppongo esista $G$ che domina $g$, cioè $|g(z)| \le G(|z|)$ $\forall z \in \mathbb{C}$, $|z| > R$, ed è infinitesima all'infinito.

Allora:

$$\lim_{\rho\to+\infty}\int_{\Gamma_\rho} e^{iaz}\cdot g(z)\,dz = 0$$

$\Gamma_\rho$ è una semicirconferenza di raggio $= \rho > R$.

Per $a > 0$ si trova nel semipiano positivo, per $a < 0$ in quello negativo.

> [!note] Uso tipico
> Il lemma serve a mostrare che, nel calcolo con i residui di integrali del tipo $\int_{-\infty}^{+\infty} e^{iax}g(x)\,dx$, il contributo della semicirconferenza grande si annulla. Il semipiano va scelto in modo che $|e^{iaz}| = e^{-a\operatorname{Im}(z)}$ decada.

### Dimostrazione

Parametrizzo $\Gamma_\rho$ con $\gamma : [0, \pi] \to \mathbb{C}$, $\; \eta \to \rho\cdot e^{i\eta} = \rho\cdot\cos(\eta) + \rho\cdot i\cdot\sin(\eta)$

$$\int_{\Gamma_\rho} e^{iaz}\cdot g(z)\,dz = \int_0^\pi e^{ia\cos(\eta)}\cdot e^{-a\rho\sin(\eta)}\cdot g(\rho e^{i\eta})\cdot i\rho\,e^{i\eta}\,d\eta \qquad \text{(1)}$$

> [!warning] Esponente
> Il primo fattore è $e^{ia\rho\cos(\eta)}$ (manca $\rho$). Il passaggio successivo non cambia, perché il modulo di tale fattore è comunque $1$.

$$\left|\int_{\Gamma_\rho} e^{iaz}\cdot g(z)\,dz\right| \le \int_0^\pi\left|e^{ia\cos(\eta)}\right|\cdot\left|e^{-a\rho\sin(\eta)}\right|\cdot\underline{\left|g(\rho\cdot e^{i\eta})\right|}\cdot\left|i\rho\,e^{i\eta}\right|d\eta \qquad \text{(2)}$$

$$\le \int_0^\pi 1\cdot e^{-a\rho\sin(\eta)}\cdot\underline{G(|\rho\cdot e^{i\eta}|)}\cdot\rho\,d\eta \le G(\rho)\cdot\rho\cdot\int_0^\pi e^{-a\rho\sin(\eta)}\,d\eta$$

$$\int_0^\pi e^{-a\rho\sin(\eta)}\,d\eta = 2\int_0^{\pi/2} e^{-a\rho\sin(\eta)}\,d\eta \le 2\int_0^{\pi/2} e^{-a\rho\frac{2\eta}{\pi}}\,d\eta \qquad \text{(3)}$$

$$2\int_0^{\pi/2} e^{-a\rho\frac{2\eta}{\pi}}\,d\eta = 2\left[\frac{-\pi}{2a\rho}\cdot e^{-a\rho\frac{2\eta}{\pi}}\right]_0^{\pi/2} = -\frac{\pi}{a\rho}\left[e^{-a\rho} - 1\right] = \frac{\pi}{a\rho}\left(1 - e^{-a\rho}\right)$$

$$\left|\int_{\Gamma_\rho} e^{iaz}\cdot g(z)\,dz\right| \le G(\rho)\cdot\rho\cdot\int_0^\pi e^{-a\rho\sin(\eta)}\,d\eta = G(\rho)\cdot\cancel{\rho}\cdot\frac{\pi}{a\cancel{\rho}}\left(1 - e^{-a\rho}\right)$$

$$\lim_{\rho\to+\infty}\left|\int_{\Gamma_\rho} e^{iaz}\cdot g(z)\,dz\right| \le \lim_{\rho\to+\infty} G(\rho)\cdot\frac{\pi}{a}\left(1 - e^{-a\rho}\right) = 0 \qquad \text{(4)}$$

$$\lim_{\rho\to+\infty}\int_{\Gamma_\rho} e^{iaz}\cdot g(z)\,dz = 0 \qquad$$

**Note ai passaggi**

1. $z(\eta) = \rho\cdot e^{i\eta}$

$$\frac{dz}{d\eta} = \frac{d(\rho\cdot e^{i\eta})}{d\eta} \qquad dz = \rho\cdot\frac{d(e^{i\eta})}{d\eta}\cdot d\eta = \rho\cdot i\cdot e^{i\eta}\cdot d\eta$$

2. Qui si usa che $G$ domina $g$.

3. Tra $[0, \frac{\pi}{2}]$ si ha $\frac{2}{\pi}\eta \le \sin(\eta)$ $\forall \eta \in [0, \frac{\pi}{2}]$

$$\frac{2}{\pi}\eta \le \sin(\eta)$$

$$-a\rho\cdot\frac{2}{\pi}\eta \ge -a\rho\cdot\sin(\eta) \;\to\; e^{-a\rho\cdot\frac{2}{\pi}\eta} \ge e^{-a\rho\cdot\sin(\eta)} \qquad \forall \eta \in [0, \tfrac{\pi}{2}]$$

4. $G(+\infty) = 0$, $G$ infinitesima all'infinito.

> [!note] Dettagli
> Il primo passaggio della (3) usa la simmetria $\sin(\pi - \eta) = \sin\eta$. La disuguaglianza $\frac{2}{\pi}\eta \le \sin\eta$ (disuguaglianza di Jordan) discende dalla concavità del seno su $[0, \pi/2]$: la corda tra $(0,0)$ e $(\pi/2, 1)$ sta sotto il grafico. La dimostrazione è svolta per $a > 0$; il caso $a < 0$ è analogo sul semipiano inferiore.
