# Teorema della funzione inversa

$f : D \subset \mathbb{R}^n \to \mathbb{R}^n$, $f \in C^1_{(D)}$ e per $\hat x \in D$, $\det|J_{\hat x}| \neq 0$

Allora $\exists N$ un intorno di $\hat x$ t.c. $f : N \to f(N)$ è invertibile.

> [!note] Notazione
> $J_{\hat x}$ è la matrice jacobiana di $f$ in $\hat x$. La condizione $\det J_{\hat x} \neq 0$ significa che il differenziale di $f$ in $\hat x$ è una mappa lineare invertibile.

### Dimostrazione

Provo che $\exists B(\hat x, \delta)$ con $\delta > 0$ t.c. $f$ è iniettiva su $B(\hat x, \delta) = N$

cioè $\forall x,y \in B(\hat x, \delta)$ per $x \neq y \Rightarrow f(x) - f(y) \neq 0 \quad \leftarrow f$ iniettiva

da $f(x) - f(y) \neq 0 \Rightarrow |f(x) - f(y)| > 0$

con $\tau > 0$ [?]

$$\|J_{\hat x}^{-1}\| = \frac{1}{\tau} \qquad \tau = \frac{1}{\|J_{\hat x}^{-1}\|}$$

Scrivo $g(x) = f(x) - J_{\hat x}\cdot x \;\to\; f(x) = g(x) + J_{\hat x}\cdot x$

$$|f(x) - f(y)| \ge |\underbrace{J_{\hat x}\cdot(x-y)}_{\text{lineare}} + \underbrace{(g(x) - g(y))}_{\text{non lineare}}|$$

> [!warning] Passaggio
> In questo punto vale l'uguaglianza: $|f(x) - f(y)| = |J_{\hat x}(x-y) + (g(x) - g(y))|$. La disuguaglianza utile, usata nella conclusione, è la triangolare inversa: $|f(x) - f(y)| \ge |J_{\hat x}(x-y)| - |g(x) - g(y)|$.

So che

$$|x - y| = |J_{\hat x}^{-1}\cdot J_{\hat x}\cdot(x-y)| \le \|J_{\hat x}^{-1}\|\cdot|J_{\hat x}\cdot(x-y)|$$

quindi: $|x - y|\cdot\tau \le |J_{\hat x}\cdot(x-y)|$

Calcolo $J_g(x) = J_f(x) - J_{\hat x}$

in $\hat x$: $J_g(\hat x) = J_{\hat x} - J_{\hat x} = 0$. Continuità: per $\varepsilon > 0 \;\exists\; \|J_g(x)\| < \varepsilon$

Per il teorema della stima $|g(x) - g(y)| \le \varepsilon\cdot|x - y|$

> [!note] Continuità e teorema della stima
> Poiché $J_g$ è continua e vale $0$ in $\hat x$, per ogni $\varepsilon > 0$ esiste $\delta > 0$ tale che $\|J_g(x)\| < \varepsilon$ per $x \in B(\hat x, \delta)$. Il "teorema della stima" è la disuguaglianza del valor medio su un convesso: $|g(x) - g(y)| \le \sup_B \|J_g\|\cdot|x - y|$.

Quindi

$$|f(x) - f(y)| \ge \tau\cdot|x-y| - \varepsilon\cdot|x-y| \ge (\tau - \varepsilon)\cdot|x-y| > 0 \qquad \tau > \varepsilon$$

$$|f(x) - f(y)| > 0$$

$f$ è iniettiva quindi invertibile $\square$

> [!note] Portata della dimostrazione
> L'argomento prova l'iniettività locale, quindi l'invertibilità di $f : N \to f(N)$. L'enunciato completo del teorema aggiunge che $f(N)$ è aperto e che l'inversa è di classe $C^1$, con $J_{f^{-1}}(f(x)) = J_f(x)^{-1}$.
