# Statistica · registro delle correzioni e delle aggiunte

Ogni esempio ripreso nei moduli è stato ricalcolato con `strumenti/verifica.py`. Qui sono elencate le correzioni di sostanza e le aggiunte; le correzioni di forma (refusi, notazione, ordine) non sono registrate una per una.

## Correzioni di sostanza

| # | Modulo | Dove negli appunti | Prima | Dopo | Motivo | Fonte |
|---|---|---|---|---|---|---|
| 1 | 2 · 2.2 | L05 | Dado: $E \cup F = \Omega$ ("evento certo"), $P[E \cup F] = 1$ con $E$ = pari, $F$ = primo | $E \cup F = \{2, 3, 4, 5, 6\}$, $P = \frac12 + \frac23 - \frac16 = \frac56$ | L'1 non è né pari né primo | Calcolo diretto |
| 2 | 3 · 3.2 | L14 | $\mathbb{E}[X] = \frac{9 + 4}{10} = \frac{13}{20}$ | $\frac{13}{10}$ | Errore nella somma delle frazioni | `verifica.py` |
| 3 | 3 · 3.6 | L17 | Funzione di ripartizione dell'uniforme: $\frac{x - a}{b - a}$ su $[a, b]$, 0 altrove | 0 per $x < a$, 1 per $x > b$ | Una funzione di ripartizione tende a 1 | Proprietà 2 del paragrafo 2.9 |
| 4 | 3 · es. 7 | L19 | $\delta = \sigma\varphi_{0,75} = 5{,}46$ | $\delta = 8 \cdot 0{,}6745 \approx 5{,}40$ cm | Errore numerico | Tavole, `verifica.py` |
| 5 | 4 · 4.2 | L21 | Numerosità $n = 245$ | $n = 246$ | $245{,}2$ va arrotondato per eccesso, altrimenti l'ampiezza non basta | Definizione |
| 6 | 4 · 4.4 | L22 | Livello del 90% con "$\alpha = 5\%$, $\alpha/2 = 0{,}025$" | $\alpha = 10\%$, $\alpha/2 = 0{,}05$ | Il valore $z = 1{,}645$ usato è quello giusto per il 90% | Definizione di livello |
| 7 | 3 · es. 2 | L15 | Domanda b) "sapendo che sono uscite 3 teste" con calcolo per 2 teste | Domanda con 2 teste | Coerenza fra domanda e calcolo | – |
| 8 | 2 · 2.10 | L12 | Densità uguale a 1 fuori dall'intervallo (in $f_X$ e in $f_Y$) | 0 | Con valore 1 l'integrale non converge | Definizione di densità |
| 9 | 3 · 3.5 | L16 | Somma di Poisson scritta "$\mathrm{Pascal}(\lambda)$" | $\mathrm{Poisson}(\lambda + \mu)$ | Refuso | – |
| 10 | 1 · es. 3 | L04 | Mediana scritta "58" | 8 | Confusione con la cumulata 58% | Definizione di quantile |
| 11 | 3 · 3.7 | L18 | Stima della coda per $z = 1$ (≈ 30%, lettura incerta) | 24% | Ricalcolata: $e^{-1/2}/\sqrt{2\pi} \approx 0{,}242$ | `verifica.py` |
| 12 | 4 · 4.2 | L20 | $z_{0,005} = 2{,}56$ | $2{,}576$ | Valore delle tavole | `verifica.py` |
| 13 | 2 · es. 3 | L07 | Probabilità delle cabine "$1{,}5 \cdot 10^{-?}$" (esponente illeggibile) | $\approx 1{,}5 \cdot 10^{-9}$ | Ricalcolata | `verifica.py` |
| 14 | 3 · 3.5 | L17 | Tabella ipergeometrica, $k = 1$: 38,3% [lettura] | 38,9% | Ricalcolata | `verifica.py` |
| 15 | 4 · 4.3 | L22 | Estremo superiore di $\sigma^2$: 821,39 | 821,1 | Con $\chi^2_{0,99; 8} = 1{,}6465$ | `verifica.py` |

Altre piccole correzioni di notazione: $\sigma^2$ al posto di "$\sigma = \mathrm{VAR}[X]$" (L14), $P[\lvert Z\rvert > 1{,}25]$ al posto di "$> -1{,}25$" (L19), $\varphi_p$ per il quantile invece di $\phi_p$ (si confonde con la densità).

## Aggiunte

| # | Modulo · sezione | ID | Contenuto | Fonte | Parole |
|---|---|---|---|---|---|
| A1 | 1 · 1.2 | STA-07 | Moda e diagramma di Pareto | Ross | ~110 |
| A2 | 1 · 1.6 | STA-09 | Coefficiente di variazione | Ross | ~60 |
| A3 | 1 · 1.7 | STA-11 | Coefficiente $R^2$ e analisi dei residui | Ross; Devore, *Probability and Statistics for Engineering and the Sciences* | ~150 |
| A4 | 1 · 1.7 | STA-10 | Paradosso di Simpson, con un esempio costruito per il modulo | Newbold, Carlson, Thorne, *Statistica* | ~140 |
| A5 | 2 · 2.1 | STA-01 | Definizioni classica, a posteriori, assiomatica | Ross | ~90 |
| A6 | 3 · 3.4 | STA-06 | Indipendenza di variabili aleatorie | Ross; Devore, *Probability and Statistics for Engineering and the Sciences* | ~110 |
| A7 | 4 · 4.1 | STA-12 | Efficienza di uno stimatore | Ross | ~80 |
| A8 | 4 · 4.5 | STA-13 | Intervalli per la differenza di medie: indipendenti (varianze note, combinata), appaiati; esempio | Ross; Devore, *Probability and Statistics for Engineering and the Sciences* | ~330 |
| A9 | 4 · 4.6 | STA-14 | Test di ipotesi: ipotesi, errori, livello, potenza, p-value, test z; esempio di potenza | Ross; Newbold, Carlson, Thorne, *Statistica* | ~440 |
| A10 | 4 · 4.7 | STA-15 | Tabella dei test, test t, proporzione, varianza, chi-quadro di indipendenza; quattro esempi | Ross; Devore, *Probability and Statistics for Engineering and the Sciences* | ~480 |
| A11 | 4 · 4.8 | STA-16 | ANOVA a una via con un esempio | Ross; Devore, *Probability and Statistics for Engineering and the Sciences* | ~300 |

Gli esempi delle aggiunte usano, dove possibile, i dati degli esempi degli appunti (moneta con 60 teste, pezzi venduti, ore di straordinario, tabella genere × colore degli occhi); quelli della differenza di medie, del paradosso di Simpson e dell'ANOVA sono costruiti per il modulo.

Le aggiunte valgono circa il 12% del modulo 1, meno del 3% dei moduli 2 e 3 e circa il 37% del modulo 4 (domanda 1 di `01-copertura.md`).
