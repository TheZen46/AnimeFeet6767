# Formulario di Analisi 1A

Trascrizione di `Formulari e riassunti/Formulario Analisi 1A.pdf` (2 pagine, la seconda vuota). Le formule sono riportate per intero; gli esercizi a margine sono riassunti. Segni usati: `[?]` lettura incerta.

## Funzioni

- Funzione monotona: $\forall x_1, x_2 \in I$, $x_1 < x_2 \Rightarrow f(x_1) \le f(x_2)$.
- Funzioni composte: $h(x) = g(f(x))$; $x \in \operatorname{dom}(g \circ f) \iff x \in \operatorname{dom} f$ e $f(x) \in \operatorname{dom} g$.

## Trigonometria

- $\cos^2 x + \sin^2 x = 1\ \ \forall x \in \mathbb{R}$
- $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$
- $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$
- $\sin 2x = 2\sin x\cos x$, $\quad \cos 2x = 2\cos^2 x - 1$
- $\sin x - \sin y = 2\sin\frac{x - y}{2}\cos\frac{x + y}{2}$
- $\cos x - \cos y = -2\sin\frac{x - y}{2}\sin\frac{x + y}{2}$
- $\sin(x + \pi) = -\sin x$, $\cos(x + \pi) = -\cos x$, $\sin\left(x + \frac{\pi}{2}\right) = \cos x$, $\cos\left(x + \frac{\pi}{2}\right) = -\sin x$
- $\tan x = \frac{\sin x}{\cos x}$, $\quad \cot x = \frac{\cos x}{\sin x}$

## Limiti delle funzioni elementari

- $\alpha > 0$: $\lim_{x \to +\infty} x^\alpha = +\infty$, $\lim_{x \to 0^+} x^\alpha = 0$; $\quad \alpha < 0$: $\lim_{x \to +\infty} x^\alpha = 0$, $\lim_{x \to 0^+} x^\alpha = +\infty$.
- $a > 1$: $\lim_{x \to +\infty} a^x = +\infty$, $\lim_{x \to -\infty} a^x = 0$; $\quad a < 1$: $\lim_{x \to +\infty} a^x = 0$, $\lim_{x \to -\infty} a^x = +\infty$.
- $a > 1$: $\lim_{x \to +\infty} \log_a x = +\infty$, $\lim_{x \to 0^+} \log_a x = -\infty$; $\quad a < 1$: $\lim_{x \to +\infty} \log_a x = -\infty$, $\lim_{x \to 0^+} \log_a x = +\infty$.
- $\lim_{x \to \pm\infty} \sin x$, $\cos x$, $\tan x$ non esistono [?].
- $\lim_{x \to (\pi/2 + k\pi)^\pm} \tan x = \mp\infty\ \ \forall k \in \mathbb{Z}$.
- $\lim_{x \to \pm 1} \arcsin x = \pm\frac{\pi}{2} = \arcsin(\pm 1)$; $\lim_{x \to 1} \arccos x = 0 = \arccos 1$, $\lim_{x \to -1} \arccos x = \pi = \arccos(-1)$; $\lim_{x \to +\infty} \arctan x = \frac{\pi}{2}$.

## Limiti notevoli

- $\lim_{x \to 0} \frac{\log(1 + x)}{x} = 1$, $\quad \lim_{x \to 0} \frac{e^x - 1}{x} = 1$
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$, $\quad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$, $\quad \lim_{x \to \pm\infty} \left(1 + \frac{a}{x}\right)^x = e^a$
- $\lim_{x \to 0} (1 + x)^{1/x} = e$, $\quad \lim_{x \to 0} \frac{\log_a(1 + x)}{x} = \frac{1}{\log a}$
- $\lim_{x \to 0} \frac{(1 + x)^\alpha - 1}{x} = \alpha$ $(\alpha \in \mathbb{R})$

## Esercizi a margine (riassunto)

- Domini: (a) sistema $3x + 1 > 0$, $x^2 - x - 6 > 0$; (b) $\frac{\sqrt{x^2 - 3x - 4}}{x + 5}$; (c) $\log(x^2 - x)$; (d) funzione definita a tratti con $\frac{1}{2x + 1}$ ed $e^{\sqrt{x+1}}$.
- Immagini: $f(x) = \frac{1}{x^2 + 1}$ ha immagine $(0, 1]$ (ricavando $x = \sqrt{\frac{1}{y} - 1}$); $f(x) = \sqrt{x + 2} - 1$; $\sqrt{\cos x - 1}$ è definita solo per $x = 2k\pi$.
- $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$; $\lim_{x \to -\infty} \frac{x}{\sqrt{x^2 - 1}} = -1$, razionalizzando.

## Rimandi

"Vedi Landau pag. 184; 190 Rolle, Lagrange e Cauchy; 235-239" (pagine di un testo, probabilmente il libro di riferimento).
