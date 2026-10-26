# Condizioni di integrabilità

Siano $f : Q \subset \mathbb{R}^2 \to \mathbb{R}$ e $Q = [a,b]\times[c,d]$ un compatto.

Allora se $f$ è continua è anche integrabile.

### Dimostrazione

$f$ continua su $Q$ compatto $\Rightarrow$ $f$ è uniformemente continua:

$$\forall \varepsilon > 0 \;\; \exists \delta_\varepsilon > 0 \;\; \text{t.c.} \;\; |x - y| < \delta_\varepsilon \Rightarrow |f(x) - f(y)| < \varepsilon$$

Cerco una partizione di $Q$ adattata a $\delta_\varepsilon$:

$$a = x_0 < x_1 < \dots < x_r = b \qquad x_j - x_{j-1} = \Delta x_j < \frac{\delta_\varepsilon}{2} \quad \forall j \in \{1,\dots,r\}$$

$$c = y_0 < y_1 < \dots < y_s = d \qquad y_k - y_{k-1} = \Delta y_k < \frac{\delta_\varepsilon}{2} \quad \forall k \in \{1,\dots,s\}$$

Allora $Q_{jk} = [x_{j-1}, x_j]\times[y_{k-1}, y_k]$

e $z_1, z_2 \in Q_{jk}$ t.c. $|z_1 - z_2| < \left(\frac{\delta_\varepsilon}{2}\right)^2 + \left(\frac{\delta_\varepsilon}{2}\right)^2$

Stimo $|z_1 - z_2| < 2\cdot\frac{1}{4}\cdot\delta_\varepsilon^2 < \delta_\varepsilon^2$

> [!warning] Stima della distanza
> La disuguaglianza riguarda il quadrato della distanza: $|z_1 - z_2|^2 < \left(\frac{\delta_\varepsilon}{2}\right)^2 + \left(\frac{\delta_\varepsilon}{2}\right)^2 = \frac{\delta_\varepsilon^2}{2}$, quindi $|z_1 - z_2| < \frac{\delta_\varepsilon}{\sqrt 2} < \delta_\varepsilon$, che è ciò che serve per applicare l'uniforme continuità.

Uso uniforme continuità $\Rightarrow |f(z_1) - f(z_2)| < \varepsilon$ cioè $M_{jk} - m_{jk} < \varepsilon$

$$M_{jk} = \sup f(z_1), \qquad m_{jk} = \inf f(z_2)$$

$$S_{sup}(D,f) - S_{inf}(D,f) = \sum_{j=1}^{r}\sum_{k=1}^{s} M_{jk}\,\Delta x_j\,\Delta y_k - m_{jk}\,\Delta x_j\,\Delta y_k =$$

$$= \sum_{jk} (M_{jk} - m_{jk})\cdot A(Q_{jk}) <$$

$$< \sum_{jk} \varepsilon\cdot A(Q_{jk}) = \varepsilon\cdot\sum_{jk} A(Q_{jk}) = \varepsilon\cdot A(Q)$$

Il risultato vale $\forall \varepsilon$ $\Rightarrow$ $f$ è integrabile su $Q$ $\square$

Ho dimostrato che: per $\varepsilon > 0 \;\exists D \in \mathcal{P}$ t.c. $S_{sup}(D,f) - S_{inf}(D,f) < \varepsilon\cdot\text{costante}$

> [!note] Criterio di integrabilità
> $D$ indica una partizione di $Q$ e $\mathcal{P}$ l'insieme delle partizioni. Una funzione limitata è integrabile secondo Riemann se e solo se, per ogni $\varepsilon > 0$, esiste una partizione per cui somma superiore e somma inferiore differiscono meno di $\varepsilon$. La costante $A(Q)$ non altera il criterio, perché basta scegliere $\varepsilon / A(Q)$ al posto di $\varepsilon$.
