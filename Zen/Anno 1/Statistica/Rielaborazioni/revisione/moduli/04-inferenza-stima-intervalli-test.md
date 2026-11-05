---
corso: Statistica
modulo: 4
titolo: "Inferenza: stima, intervalli e test"
programma: [STA-12, STA-13, STA-14, STA-15, STA-16, STA-17]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 4 · Inferenza: stima, intervalli e test

**In questo modulo.** Servono le leggi notevoli, la normale con quantili e valori critici, la legge dei grandi numeri e il teorema del limite centrale del modulo 3. Fin qui la legge delle variabili era nota e se ne calcolavano le probabilità; nell'inferenza si fa il percorso inverso: da un campione di dati si ricavano informazioni sui parametri ignoti della popolazione. Si definiscono stimatori corretti e consistenti, si costruiscono intervalli di confidenza per la media (con varianza nota e ignota), per la varianza, per una proporzione e per la differenza di due medie, e si sceglie la numerosità del campione. Si introducono le leggi chi-quadro e t di Student. Le ultime sezioni trattano i test di ipotesi (errori, livello di significatività, p-value, potenza), i test per medie, varianze e tabelle di contingenza, e l'analisi della varianza a una via.

## 4.1 Campioni, stime e stimatori

Una variabile aleatoria $X$ descrive una grandezza in una **popolazione** (il peso dei pesci di un allevamento, l'esito del lancio di una moneta). La sua legge dipende da un **parametro** $\theta$ ignoto, per esempio $p$ se $X \sim B(p)$, oppure in generale $\theta = \mathbb{E}[X]$.

> [!definizione] Campione, stima, stimatore
> Un **campione** di dimensione $n$ è una famiglia $X_1, \dots, X_n$ di variabili aleatorie indipendenti e con la stessa legge di $X$. I numeri $x_1, \dots, x_n$ effettivamente osservati sono una **realizzazione** del campione. Una funzione $T$ dei dati dà la **stima** $T(x_1, \dots, x_n)$ del parametro, un numero; la stessa funzione applicata al campione dà lo **stimatore** $\hat\theta = T(X_1, \dots, X_n)$, una variabile aleatoria.

Per esempio, $n$ lanci della stessa moneta sono un campione di $X \sim B(p)$; una realizzazione è una sequenza di 0 e 1 come $(1, 0, 1, \dots, 0)$; la frequenza relativa delle teste $\frac{x_1 + \dots + x_n}{n}$ è una stima di $p$, e $\hat p = \frac{X_1 + \dots + X_n}{n}$ è lo stimatore corrispondente. La distinzione è essenziale: la stima cambia da un campione all'altro, e le proprietà di uno stimatore descrivono come si comporta "in media" su tutti i campioni possibili.

> [!definizione] Stimatore corretto e consistente
> Una successione di stimatori $\hat\theta_n = T_n(X_1, \dots, X_n)$ è
>
> - **corretta** (non distorta) se $\mathbb{E}[\hat\theta_n] = \theta$ per ogni $n$; la differenza $\mathbb{E}[\hat\theta_n] - \theta$ si chiama **distorsione**;
> - **consistente** (in media quadratica) se l'**errore quadratico medio** tende a zero: $\lim_{n \to \infty} \mathbb{E}\big[(\hat\theta_n - \theta)^2\big] = 0$.

L'errore quadratico medio si scompone in varianza più quadrato della distorsione:
$$\mathbb{E}\big[(\hat\theta - \theta)^2\big] = \mathrm{Var}[\hat\theta] + \big(\mathbb{E}[\hat\theta] - \theta\big)^2.$$
Per uno stimatore corretto è la sola varianza, quindi uno stimatore corretto è consistente se $\mathrm{Var}[\hat\theta_n] \to 0$.

Fra due stimatori corretti dello stesso parametro è più **efficiente** quello con varianza minore: a parità di campione, le sue stime si disperdono meno attorno al valore vero. Per esempio, per la media di una popolazione sia $X_1$ (la prima osservazione) sia $\bar X$ sono corretti, ma $\mathrm{Var}[\bar X] = \frac{\sigma^2}{n}$ è $n$ volte più piccola di $\mathrm{Var}[X_1] = \sigma^2$.

Gli stimatori più usati sono la **media campionaria** e la **varianza campionaria**:
$$\bar X = \frac{1}{n}\sum_{i=1}^n X_i, \qquad S^2 = \frac{1}{n - 1}\sum_{i=1}^n (X_i - \bar X)^2.$$

> [!teorema] Proprietà di media e varianza campionaria
> Se $\mu = \mathbb{E}[X]$ e $\sigma^2 = \mathrm{Var}[X]$: $\bar X$ è uno stimatore corretto e consistente di $\mu$, e $S^2$ è uno stimatore corretto di $\sigma^2$.

*Dimostrazione.* Per la linearità $\mathbb{E}[\bar X] = \frac1n \cdot n\mu = \mu$, e per l'indipendenza $\mathrm{Var}[\bar X] = \frac{1}{n^2} \cdot n\sigma^2 = \frac{\sigma^2}{n} \to 0$. Per $S^2$, si osserva che $X_i - \bar X$ ha speranza nulla, quindi $\mathbb{E}[(X_i - \bar X)^2] = \mathrm{Var}[X_i - \bar X]$. Scrivendo $X_i - \bar X = \left(1 - \frac1n\right)X_i - \frac1n\sum_{j \neq i} X_j$, somma di variabili indipendenti,
$$\mathrm{Var}[X_i - \bar X] = \left(1 - \frac1n\right)^2\sigma^2 + \frac{n-1}{n^2}\sigma^2 = \frac{(n-1)^2 + (n-1)}{n^2}\sigma^2 = \frac{n-1}{n}\sigma^2.$$
Sommando sugli $n$ indici e dividendo per $n - 1$ si ottiene $\mathbb{E}[S^2] = \sigma^2$. $\square$

Con $\frac{1}{n}$ al posto di $\frac{1}{n-1}$ lo stimatore sarebbe distorto: sottostimerebbe la varianza di un fattore $\frac{n-1}{n}$. È il motivo del denominatore $n - 1$ già incontrato nel modulo 1.

## 4.2 Intervallo di confidenza per la media con varianza nota

Una stima puntuale non dice quanto ci si può fidare. Un **intervallo di confidenza** è un intervallo calcolato dai dati che contiene il parametro con una probabilità fissata in anticipo.

Si supponga $X \sim N(\mu, \sigma^2)$ con $\mu$ ignoto e $\sigma^2$ noto. Allora $\bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$ e, standardizzando, $\frac{\bar X - \mu}{\sigma/\sqrt n} \sim N(0, 1)$. Fissato $\alpha \in (0, 1)$,
$$P\left[\left\lvert \frac{\bar X - \mu}{\sigma/\sqrt n}\right\rvert \le z_{\alpha/2}\right] = 1 - \alpha,$$
e risolvendo la disuguaglianza rispetto a $\mu$: con probabilità $1 - \alpha$,
$$\bar X - \frac{\sigma}{\sqrt n} z_{\alpha/2} \le \mu \le \bar X + \frac{\sigma}{\sqrt n} z_{\alpha/2}.$$

> [!definizione] Intervallo di confidenza per la media (varianza nota)
> Data una realizzazione con media $\bar x$, l'intervallo
> $$\left[\bar x - \delta,\ \bar x + \delta\right], \qquad \delta = z_{\alpha/2}\frac{\sigma}{\sqrt n},$$
> è l'**intervallo di confidenza** bilatero per $\mu$ al **livello di confidenza** $1 - \alpha$.

> [!attenzione] Che cosa vuol dire "al 95%"
> Una volta calcolato sui dati, l'intervallo è fisso, e $\mu$ è un numero: o ci sta dentro o no. Non si può dire che "$\mu$ sta nell'intervallo con probabilità 95%". Il 95% si riferisce alla procedura: se si ripetesse l'esperimento con molti campioni, circa il 95% degli intervalli così costruiti conterrebbe $\mu$ (figura 4.1). Per questo si parla di confidenza e non di probabilità.

![Figura 4.1 · Venti intervalli al 90% calcolati da campioni simulati di 100 pesci con $\mu = 500$ g e $\sigma = 100$ g: tre non contengono $\mu$.](../figure/4-1.svg)

Se $X$ non è normale ma $n$ è grande, per il teorema del limite centrale $\bar X$ è approssimativamente $N(\mu, \sigma^2/n)$ e lo stesso intervallo ha livello approssimativamente $1 - \alpha$. Senza alcuna ipotesi sulla legge e per ogni $n$, la disuguaglianza di Chebyshev dà invece l'intervallo $\bar x \pm \frac{1}{\sqrt\alpha}\frac{\sigma}{\sqrt n}$, con livello almeno $1 - \alpha$, molto più largo:

| $1 - \alpha$ | 75% | 90% | 95% | 99% |
|---|---|---|---|---|
| $\frac{1}{\sqrt\alpha}$ (Chebyshev) | 2 | 3,16 | 4,47 | 10 |
| $z_{\alpha/2}$ (normale) | 1,15 | 1,645 | 1,96 | 2,576 |

> [!esempio] Il peso dei pesci
> In un allevamento il peso dei pesci è normale con media ignota e deviazione standard $\sigma = 100$ g. Un campione di 100 pesci ha peso medio 500 g.
>
> - Al 90%: $\alpha = 0{,}1$, $z_{0,05} = 1{,}645$, $\delta = 1{,}645 \cdot \frac{100}{10} = 16{,}45$, quindi $484 \le \mu \le 516$ g.
> - Al 99%: $z_{0,005} = 2{,}576$, $\delta = 25{,}76$, quindi $474 \le \mu \le 526$ g. Più confidenza costa un intervallo più largo.
> - Quanto deve essere grande il campione perché l'intervallo al 99% sia largo come quello al 90% con 100 pesci? Deve essere $\frac{2{,}576}{\sqrt{n'}} = \frac{1{,}645}{\sqrt{100}}$, cioè $n' = \left(\frac{2{,}576}{1{,}645}\right)^2 \cdot 100 \approx 245{,}2$: servono 246 pesci.

## 4.3 Leggi chi-quadro e t di Student

Quando la varianza non è nota la si stima con $S^2$, e servono le leggi delle quantità che ne risultano.

> [!definizione] Leggi chi-quadro e t di Student
> Siano $Z_1, \dots, Z_n$, $Z$ normali standard indipendenti.
>
> - La legge di $W_n = Z_1^2 + \dots + Z_n^2$ è la **chi-quadro con $n$ gradi di libertà**, $\chi^2_n$. Ha valori positivi, $\mathbb{E}[W_n] = n$, $\mathrm{Var}[W_n] = 2n$, ed è asimmetrica (con moda in $\max\{n - 2, 0\}$).
> - Se $W_n \sim \chi^2_n$ è indipendente da $Z$, la legge di $T_n = \dfrac{Z}{\sqrt{W_n / n}}$ è la **t di Student con $n$ gradi di libertà**, $t_n$. È simmetrica, con $\mathbb{E}[T_n] = 0$ per $n \ge 2$ e $\mathrm{Var}[T_n] = \frac{n}{n-2}$ per $n \ge 3$.

La t di Student somiglia alla normale standard ma ha code più spesse, perché al denominatore c'è una quantità aleatoria; al crescere di $n$ si avvicina alla normale, e per $n$ grande $t_{\alpha, n} \approx z_\alpha$ (figura 4.2). Per $n$ grande anche la chi-quadro è quasi normale, $N(n, 2n)$, per il teorema del limite centrale.

![Figura 4.2 · A sinistra la normale standard e le t di Student con 1 e 3 gradi di libertà; a destra le densità chi-quadro con 2, 4, 8 gradi di libertà.](../figure/4-2.svg)

I **valori critici** si definiscono come per la normale, con la coda destra: $P[T_n > t_{\alpha, n}] = \alpha$ e $P[W_n > \chi^2_{\alpha, n}] = \alpha$, e si leggono sulle tavole. Per simmetria $P[-t_{\alpha/2, n} \le T_n \le t_{\alpha/2, n}] = 1 - \alpha$; per la chi-quadro, che non è simmetrica, servono due valori: $P[\chi^2_{1-\alpha/2, n} \le W_n \le \chi^2_{\alpha/2, n}] = 1 - \alpha$.

> [!teorema] Campioni normali
> Se $X_1, \dots, X_n$ è un campione di $N(\mu, \sigma^2)$, allora
>
> 1. $\dfrac{\bar X - \mu}{S/\sqrt n} \sim t_{n-1}$;
> 2. $\dfrac{(n - 1)S^2}{\sigma^2} \sim \chi^2_{n-1}$;
> 3. $\bar X$ e $S^2$ sono indipendenti.

Si perde un grado di libertà perché gli scarti $X_i - \bar X$ hanno somma nulla. Dal teorema, come nel paragrafo 4.2, si ricavano gli intervalli.

> [!definizione] Intervalli per media e varianza di una popolazione normale
> Con $\bar x$ e $s^2$ calcolate sui dati, al livello $1 - \alpha$:
> $$\bar x - t_{\alpha/2, n-1}\frac{s}{\sqrt n} \le \mu \le \bar x + t_{\alpha/2, n-1}\frac{s}{\sqrt n}, \qquad \frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}.$$

L'intervallo per $\sigma^2$ non è simmetrico attorno a $s^2$. Per $n$ grande $t_{\alpha/2, n-1} \approx z_{\alpha/2}$ e l'intervallo per la media è quasi quello con varianza nota, con $s$ al posto di $\sigma$.

> [!esempio] Pezzi venduti in un'ora
> Il numero di pezzi venduti in una certa ora del giorno è normale. In 9 giorni si osservano media $\bar x = 200$ e deviazione standard campionaria $s = 13$. Intervalli al 98% ($\alpha = 0{,}02$, $\frac\alpha2 = 0{,}01$, 8 gradi di libertà):
>
> - per $\mu$: $t_{0,01; 8} = 2{,}896$, $\delta = 2{,}896 \cdot \frac{13}{3} \approx 12{,}6$, quindi $187{,}4 \le \mu \le 212{,}6$. Usando per errore la normale ($z_{0,01} = 2{,}326$) si troverebbe $\delta \approx 10$: con soli 9 dati la differenza conta;
> - per $\sigma^2$: $\chi^2_{0,99; 8} = 1{,}646$ e $\chi^2_{0,01; 8} = 20{,}090$, quindi $\frac{8 \cdot 169}{20{,}090} \le \sigma^2 \le \frac{8 \cdot 169}{1{,}646}$, cioè $67{,}3 \le \sigma^2 \le 821{,}1$ e $8{,}2 \le \sigma \le 28{,}7$. Con pochi dati la varianza è stimata male.

## 4.4 Intervalli per una proporzione e numerosità del campione

Sia $X \sim B(p)$ con $p$ ignoto (la frazione di pezzi difettosi, di elettori di un partito) e $\hat p = \frac{X_1 + \dots + X_n}{n}$ la frequenza relativa dei successi. Per il teorema del limite centrale $\hat p \approx N\left(p, \frac{p(1-p)}{n}\right)$, ma la varianza dipende da $p$, che è ignoto. Ci sono due modi di aggirare il problema:

> [!definizione] Intervalli per una proporzione
> Al livello approssimato $1 - \alpha$:
> $$J_1 = \left[\hat p - \delta_1,\ \hat p + \delta_1\right], \quad \delta_1 = \frac{z_{\alpha/2}}{2\sqrt n}; \qquad J_2 = \left[\hat p - \delta_2,\ \hat p + \delta_2\right], \quad \delta_2 = z_{\alpha/2}\frac{\sqrt{\hat p(1 - \hat p)}}{\sqrt n}.$$

$J_1$ usa la maggiorazione $p(1 - p) \le \frac14$, quindi è prudente (più largo); $J_2$ sostituisce $p$ con la stima $\hat p$.

> [!esempio] Una moneta sospetta
> Una moneta lanciata 100 volte dà 60 teste: $\hat p = 0{,}6$ e $\sqrt{\hat p(1 - \hat p)} \approx 0{,}490$.
>
> - Al 90% ($\alpha = 0{,}1$, $z_{0,05} = 1{,}645$): $\delta_2 \approx 0{,}081$, $J_2 = [0{,}519;\ 0{,}681]$; $\delta_1 \approx 0{,}082$, $J_1 = [0{,}518;\ 0{,}682]$.
> - Al 99% ($z_{0,005} = 2{,}576$): $\delta_2 \approx 0{,}126$, $J_2 = [0{,}474;\ 0{,}726]$; $\delta_1 \approx 0{,}129$, $J_1 = [0{,}471;\ 0{,}729]$.
>
> Al 90% l'intervallo esclude $\frac12$, al 99% no: i dati sono un indizio, non una prova, che la moneta sia truccata. Se le teste fossero 90, al 99% si avrebbe $J_2 = [0{,}823;\ 0{,}977]$ e $J_1 = [0{,}771;\ 1{,}029]$: quando $\hat p$ è vicino a 0 o a 1, $J_1$ è troppo prudente ed esce perfino da $[0, 1]$.

**Numerosità del campione.** Spesso si fissa in anticipo la precisione voluta: si vuole che la stima differisca dal valore vero meno di $\varepsilon$ con probabilità almeno $1 - \alpha$. Basta che sia $\delta = z_{\alpha/2}\frac{\sigma}{\sqrt n} \le \varepsilon$, cioè
$$n \ge \frac{z_{\alpha/2}^2\, \sigma^2}{\varepsilon^2},$$
da arrotondare all'intero superiore. Per una proporzione, se non si sa nulla di $p$, si usa $\sigma^2 = \frac14$. Con Chebyshev, invece, $n \ge \frac{\sigma^2}{\alpha\varepsilon^2}$.

> [!esempio] Quanti lanci?
> Quanti lanci di una moneta equilibrata servono perché la frequenza relativa delle teste differisca da $\frac12$ meno di $\frac{1}{100}$ con probabilità almeno del 90%? Con Chebyshev, $n \ge \frac{1/4}{0{,}1 \cdot 10^{-4}} = 25\,000$. Con il teorema del limite centrale, $n \ge \frac{1{,}645^2 \cdot \frac14}{10^{-4}} \approx 6765$.

## 4.5 Differenza di due medie

Spesso si confrontano due popolazioni (due macchine, due terapie, due classi) con medie $\mu_1$ e $\mu_2$, e interessa $\mu_1 - \mu_2$.

**Campioni indipendenti, varianze note o campioni grandi.** Con campioni di dimensioni $n_1$, $n_2$ e medie $\bar x_1$, $\bar x_2$, la differenza $\bar X_1 - \bar X_2$ è (approssimativamente) normale con varianza $\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$, e l'intervallo al livello $1 - \alpha$ è
$$\bar x_1 - \bar x_2 \pm z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}},$$
dove per campioni grandi le varianze ignote si sostituiscono con $s_1^2$, $s_2^2$.

**Campioni indipendenti normali, varianze ignote ma uguali.** Si stima la varianza comune con la **varianza combinata** $s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$, e si usa la t di Student con $n_1 + n_2 - 2$ gradi di libertà:
$$\bar x_1 - \bar x_2 \pm t_{\alpha/2,\, n_1 + n_2 - 2}\; s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}.$$

**Campioni appaiati.** Se i dati sono coppie misurate sulla stessa unità (prima e dopo un trattamento, due strumenti sullo stesso pezzo), non sono indipendenti. Si calcolano le differenze $d_i = x_i - y_i$ e si tratta $d_1, \dots, d_n$ come un solo campione: l'intervallo per $\mu_1 - \mu_2$ è $\bar d \pm t_{\alpha/2, n-1}\frac{s_d}{\sqrt n}$.

*Esempio.* Due linee producono pezzi; su 40 pezzi della prima la media di una misura è 52 (con $\sigma_1^2 = 36$), su 50 della seconda è 48 ($\sigma_2^2 = 25$). L'errore standard della differenza è $\sqrt{\frac{36}{40} + \frac{25}{50}} = \sqrt{1{,}4} \approx 1{,}18$ e l'intervallo al 95% è $4 \pm 1{,}96 \cdot 1{,}18$, cioè $[1{,}7;\ 6{,}3]$: non contiene 0, quindi le due linee differiscono.

## 4.6 Test di ipotesi

Un **test di ipotesi** decide, sulla base di un campione, fra due affermazioni sul parametro: l'**ipotesi nulla** $H_0$ (per esempio $\mu = \mu_0$, "la media dichiarata è vera") e l'**ipotesi alternativa** $H_1$, bilatera ($\mu \neq \mu_0$) o unilatera ($\mu > \mu_0$ oppure $\mu < \mu_0$). Si calcola una **statistica test**, una funzione del campione di cui si conosce la legge quando $H_0$ è vera, e si rifiuta $H_0$ se il suo valore cade nella **regione di rifiuto**, cioè è troppo improbabile sotto $H_0$.

Le decisioni possibili hanno due tipi di errore:

| | $H_0$ vera | $H_0$ falsa |
|---|---|---|
| Si accetta $H_0$ | corretto | errore di II tipo (probabilità $\beta$) |
| Si rifiuta $H_0$ | errore di I tipo (probabilità $\alpha$) | corretto (probabilità $1 - \beta$) |

Il **livello di significatività** $\alpha$ è la probabilità massima di errore di I tipo che si accetta, fissata prima di guardare i dati (tipicamente 5% o 1%). La **potenza** $1 - \beta$ è la probabilità di rifiutare $H_0$ quando è falsa, e dipende dal vero valore del parametro: cresce quando questo si allontana da $\mu_0$ e quando cresce $n$. Le due ipotesi non sono simmetriche: si rifiuta $H_0$ solo con evidenza forte, e "accettare" $H_0$ vuol dire solo che i dati non bastano a rifiutarla.

Il **p-value** è la probabilità, calcolata sotto $H_0$, di osservare un valore della statistica almeno altrettanto estremo di quello osservato. Si rifiuta $H_0$ al livello $\alpha$ se e solo se il p-value è minore di $\alpha$; il p-value dice quindi, in un solo numero, per quali livelli i dati portano a rifiutare.

**Test sulla media, varianza nota.** Per $H_0: \mu = \mu_0$ la statistica è $Z = \frac{\bar X - \mu_0}{\sigma/\sqrt n}$, normale standard sotto $H_0$. Al livello $\alpha$ si rifiuta se $\lvert z\rvert > z_{\alpha/2}$ (alternativa bilatera), se $z > z_\alpha$ (alternativa $\mu > \mu_0$), se $z < -z_\alpha$ (alternativa $\mu < \mu_0$). Il test bilatero al livello $\alpha$ rifiuta esattamente quando $\mu_0$ non sta nell'intervallo di confidenza al livello $1 - \alpha$.

*Esempio (potenza).* Per i pesci del paragrafo 4.2 ($\sigma = 100$, $n = 100$) si sottopone a test $H_0: \mu = 500$ contro $H_1: \mu > 500$ al 5%. Si rifiuta se $\bar x > 500 + 1{,}645 \cdot 10 = 516{,}45$. Se in realtà $\mu = 520$, la probabilità di rifiutare è $P\left[Z > \frac{516{,}45 - 520}{10}\right] = \Phi(0{,}355) \approx 64\%$: con questo campione una differenza di 20 g sfugge in più di un caso su tre.

## 4.7 Test per medie, proporzioni, varianze e tabelle

Tutti i test seguono lo schema del paragrafo 4.6; cambiano la statistica e la sua legge sotto $H_0$.

| Ipotesi nulla | Statistica | Legge sotto $H_0$ |
|---|---|---|
| $\mu = \mu_0$, varianza ignota, popolazione normale | $T = \dfrac{\bar X - \mu_0}{S/\sqrt n}$ | $t_{n-1}$ |
| $p = p_0$, $n$ grande | $Z = \dfrac{\hat p - p_0}{\sqrt{p_0(1 - p_0)/n}}$ | circa $N(0, 1)$ |
| $\sigma^2 = \sigma_0^2$, popolazione normale | $W = \dfrac{(n-1)S^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ |
| $\mu_1 = \mu_2$, campioni indipendenti | $\dfrac{\bar X_1 - \bar X_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$ oppure con $s_p$ | $N(0, 1)$ oppure $t_{n_1 + n_2 - 2}$ |
| $\mu_1 = \mu_2$, campioni appaiati | $\dfrac{\bar D}{S_D/\sqrt n}$ | $t_{n-1}$ |

*Esempio (media, varianza ignota).* Per le ore di straordinario dell'esercizio 1 in fondo al modulo ($n = 81$, $\bar x = 24$, $s = 6$), l'azienda dichiara una media di 25,5 ore. Con $H_0: \mu = 25{,}5$ contro $\mu \neq 25{,}5$: $t = \frac{24 - 25{,}5}{6/9} = -2{,}25$. Al 5% il valore critico è $t_{0,025; 80} = 1{,}990$ e si rifiuta $H_0$; all'1% è $t_{0,005; 80} = 2{,}639$ e non si rifiuta. Il p-value è circa 2,7%.

*Esempio (proporzione).* Per la moneta con 60 teste su 100, $H_0: p = \frac12$: $z = \frac{0{,}6 - 0{,}5}{0{,}5/10} = 2$, con p-value $2\Phi(-2) \approx 4{,}6\%$. Si rifiuta al 5%, non all'1%, in accordo con gli intervalli del paragrafo 4.4.

*Esempio (varianza).* Per i pezzi venduti del paragrafo 4.3 ($n = 9$, $s^2 = 169$), $H_0: \sigma^2 = 100$ contro $\sigma^2 > 100$: $w = \frac{8 \cdot 169}{100} = 13{,}52$, minore di $\chi^2_{0,05; 8} = 15{,}507$. Al 5% non si rifiuta.

**Test chi-quadro di indipendenza.** Per una tabella a due vie con $m$ righe e $k$ colonne si sottopone a test $H_0$: "le due variabili sono indipendenti". Sotto $H_0$ la frequenza attesa della casella $(i, j)$ è $e_{ij} = \frac{n_{i\cdot}\, n_{\cdot j}}{n}$, e la statistica
$$\chi^2 = \sum_{i,j} \frac{(n_{ij} - e_{ij})^2}{e_{ij}}$$
ha approssimativamente legge $\chi^2_{(m-1)(k-1)}$ se tutte le $e_{ij}$ sono almeno 5. Si rifiuta per valori grandi. Per la tabella genere × colore degli occhi del modulo 1 le frequenze attese sono 3,6, 5,6, 10,8 per le donne e 5,4, 8,4, 16,2 per gli uomini, e $\chi^2 \approx 4{,}85$ con 2 gradi di libertà: minore di $\chi^2_{0,05; 2} = 5{,}991$, quindi al 5% non si rifiuta l'indipendenza (p-value circa 9%). Una frequenza attesa è sotto 5, e l'approssimazione va presa con cautela.

## 4.8 Analisi della varianza a una via

L'**ANOVA** (*analysis of variance*) confronta le medie di $k \ge 2$ gruppi in un solo test, con $H_0: \mu_1 = \dots = \mu_k$ contro "almeno due medie sono diverse". Si suppone che in ogni gruppo i dati siano normali con la stessa varianza $\sigma^2$, e che i gruppi siano indipendenti. Siano $n_i$ e $\bar x_i$ la numerosità e la media del gruppo $i$, $N = n_1 + \dots + n_k$ e $\bar x$ la media generale. La variabilità totale si scompone in quella **fra i gruppi** e quella **entro i gruppi**:
$$\underbrace{\sum_{i,j} (x_{ij} - \bar x)^2}_{SS_T} = \underbrace{\sum_i n_i(\bar x_i - \bar x)^2}_{SS_B} + \underbrace{\sum_{i,j}(x_{ij} - \bar x_i)^2}_{SS_W}.$$
Sotto $H_0$ la statistica
$$F = \frac{SS_B/(k - 1)}{SS_W/(N - k)}$$
ha legge **F di Fisher** con $(k - 1, N - k)$ gradi di libertà, e si rifiuta $H_0$ se $F > F_{\alpha;\, k-1,\, N-k}$ (dalle tavole di Fisher). L'idea: se le medie sono uguali, la dispersione fra le medie dei gruppi deve essere confrontabile con quella dentro i gruppi; se è molto più grande, le medie differiscono.

*Esempio.* Tre gruppi di tre misure: (20, 22, 24), (25, 27, 26), (21, 23, 22), con medie 22, 26, 22 e media generale $\frac{70}{3}$. Si trova $SS_B = 32$ e $SS_W = 8 + 2 + 2 = 12$, quindi $F = \frac{32/2}{12/6} = 8$, maggiore di $F_{0,05; 2, 6} = 5{,}14$: al 5% le medie non sono tutte uguali. Con due soli gruppi l'ANOVA equivale al test t con varianza combinata.

## 4.9 Il funnel plot

**Il problema.** Si vogliono confrontare più strutture (ospedali, scuole, reparti di un'azienda) attraverso una proporzione: la mortalità dopo un intervento, la percentuale di promossi, la frazione di pezzi difettosi. La tentazione è fare una classifica dei tassi osservati $\hat p_i = \frac{x_i}{n_i}$, ma è un errore: una struttura con pochi casi ha un tasso molto variabile per puro caso, e finisce in cima o in fondo alla classifica senza essere né migliore né peggiore delle altre. Il **funnel plot** (grafico a imbuto) tiene conto proprio della numerosità.

**La costruzione.** Si suppone (ipotesi nulla) che tutte le strutture abbiano la stessa probabilità vera $p$, stimata con il tasso complessivo
$$\bar p = \frac{\sum_i x_i}{\sum_i n_i}.$$
Sotto questa ipotesi $\hat p_i$ ha media $\bar p$ e deviazione standard $\sqrt{\bar p(1 - \bar p)/n_i}$, e per $n_i$ grande è circa normale (paragrafo 4.4). Nel piano con $n$ in ascissa e il tasso in ordinata si disegnano la retta $y = \bar p$ e le **curve di controllo**
$$\bar p \pm z\sqrt{\frac{\bar p(1 - \bar p)}{n}},$$
di solito con $z = 1{,}96$ (95%) e $z = 3{,}09$ (99,8%). Le curve si stringono al crescere di $n$, come un imbuto: con più casi il tasso osservato deve stare più vicino a quello medio. Poi si mette un punto $(n_i, \hat p_i)$ per ogni struttura.

**La lettura.** Un punto dentro le curve al 95% è compatibile con la media: la differenza da $\bar p$ si spiega con il caso. Un punto fra le curve al 95% e al 99,8% è un segnale di **allerta**: succederebbe per caso a circa una struttura su venti. Un punto fuori dalle curve al 99,8% è un segnale di **allarme**: per caso succederebbe a circa una struttura su cinquecento, e conviene cercare una causa. Ogni punto, in pratica, è un test dell'ipotesi $p_i = \bar p$ al livello del 5% o dello 0,2%, e le curve sono le regioni di accettazione disegnate tutte insieme.

**Esempio.** Dieci ospedali riportano i decessi dopo un intervento.

| Ospedale | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| Interventi $n_i$ | 50 | 80 | 120 | 150 | 200 | 260 | 300 | 400 | 500 | 640 |
| Decessi $x_i$ | 6 | 4 | 10 | 18 | 14 | 34 | 21 | 30 | 70 | 36 |
| Tasso $\hat p_i$ | 0,120 | 0,050 | 0,083 | 0,120 | 0,070 | 0,131 | 0,070 | 0,075 | 0,140 | 0,056 |

In tutto 243 decessi su 2700 interventi, quindi $\bar p = 0{,}09$. Per l'ospedale I, $\sqrt{0{,}09 \cdot 0{,}91/500} = 0{,}0128$, e le curve superiori valgono $0{,}09 + 1{,}96 \cdot 0{,}0128 = 0{,}115$ e $0{,}09 + 3{,}09 \cdot 0{,}0128 = 0{,}130$: il tasso 0,140 è fuori da entrambe, allarme ($z = \frac{0{,}140 - 0{,}09}{0{,}0128} = 3{,}9$). L'ospedale F ($z = 2{,}3$) è in allerta. A e D hanno lo stesso tasso, 12%, più alto della media, ma sono dentro l'imbuto: con 50 e 150 interventi una differenza così è normale. In basso, J ha $z = -3{,}0$: è in allerta "dalla parte buona", e varrebbe la pena di capire che cosa fa di diverso. Una classifica dei tassi avrebbe messo A e D fra i peggiori, alla pari di I, e B fra i migliori; il funnel plot dice che fra A, B, C, D, E, G, H non c'è nessuna differenza dimostrabile (figura 4.3).

![Figura 4.3](../figure/4-3.svg)

*Figura 4.3. Funnel plot dei dieci ospedali: retta del tasso medio, curve di controllo al 95% (tratteggiate) e al 99,8% (punteggiate).*

> [!attenzione]
> Le curve si calcolano con $\bar p$, il tasso comune sotto l'ipotesi nulla, non con il tasso della singola struttura. E il funnel plot non dice *perché* un punto è fuori: casi più gravi, errori di registrazione o qualità peggiore danno lo stesso segnale. È uno strumento per decidere dove guardare, non un giudizio.

## Esempi ed esercizi svolti

**Esercizio 1 (ore di straordinario).** Le ore mensili di straordinario dei dipendenti di un'azienda sono normali. In un campione di 81 dipendenti si trovano $\bar x = 24$ e $s = 6$. Intervalli al 99% ($\alpha = 0{,}01$, 80 gradi di libertà). Per la media: $t_{0,005; 80} = 2{,}639$, $\varepsilon = 2{,}639 \cdot \frac{6}{9} \approx 1{,}759$, quindi $22{,}24 \le \mu \le 25{,}76$; con la normale, $z_{0,005} = 2{,}576$ e $22{,}28 \le \mu \le 25{,}72$, quasi uguale perché $n$ è grande. Per la varianza: $\chi^2_{0,995; 80} = 51{,}172$ e $\chi^2_{0,005; 80} = 116{,}321$, quindi
$$\frac{80 \cdot 36}{116{,}321} \le \sigma^2 \le \frac{80 \cdot 36}{51{,}172}, \qquad 24{,}76 \le \sigma^2 \le 56{,}28, \qquad 4{,}98 \le \sigma \le 7{,}50.$$

**Esercizio 2 (scegliere l'intervallo giusto).** Lo schema degli intervalli al livello $1 - \alpha$:

| Situazione | Stimatore | Intervallo |
|---|---|---|
| Proporzione, $X \sim B(p)$, $n$ grande | $\hat p$ | $\hat p \pm z_{\alpha/2}\frac{\sqrt{\hat p(1-\hat p)}}{\sqrt n}$ |
| Media, varianza nota $\sigma_0^2$ (normale, o $n$ grande) | $\bar x$ | $\bar x \pm z_{\alpha/2}\frac{\sigma_0}{\sqrt n}$ |
| Media, varianza ignota, popolazione normale | $\bar x$, $s^2$ | $\bar x \pm t_{\alpha/2, n-1}\frac{s}{\sqrt n}$ |
| Varianza, popolazione normale | $s^2$ | $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}},\ \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}\right]$ |

Per un campione grande di una popolazione qualsiasi con varianza ignota si usa la seconda riga con $s$ al posto di $\sigma_0$.

### Altri esercizi svolti

Ogni test si imposta con gli stessi cinque passi: (1) ipotesi $H_0$ e $H_1$, bilatera o unilatera; (2) statistica test e sua legge sotto $H_0$; (3) livello $\alpha$ e regione di rifiuto; (4) valore osservato; (5) decisione e, se si può, p-value.

**Esercizio 3. Test sulla media con varianza nota, unilatero.** Un produttore dichiara che le sue lampadine durano in media 1000 ore, con $\sigma = 80$ ore. Un'associazione di consumatori ne prova 64 e trova $\bar x = 980$. C'è evidenza che la durata media sia minore di quella dichiarata?

(1) $H_0: \mu = 1000$ contro $H_1: \mu < 1000$ (l'associazione sospetta una durata *minore*). (2) $Z = \frac{\bar X - 1000}{80/\sqrt{64}} \sim N(0, 1)$ sotto $H_0$. (3) Al 5% si rifiuta se $z < -1{,}645$. (4) $z = \frac{980 - 1000}{10} = -2$. (5) Si rifiuta al 5%. Il p-value è $\Phi(-2) = 0{,}023$: all'1% non si rifiuterebbe.

**Esercizio 4. Test t su un piccolo campione.** Dieci misure di una lunghezza danno $\bar x = 12{,}4$ mm e $s = 0{,}9$ mm. Il valore nominale è 12 mm. Al 5%, le misure sono compatibili con il nominale?

$H_0: \mu = 12$ contro $\mu \ne 12$; varianza ignota e $n$ piccolo, quindi $T = \frac{\bar X - 12}{S/\sqrt{10}} \sim t_9$ (popolazione supposta normale). $t = \frac{0{,}4}{0{,}9/\sqrt{10}} = 1{,}41$, e $t_{0,025; 9} = 2{,}262$. Non si rifiuta: il p-value è circa 0,19. Con la normale al posto della t si userebbe 1,96: per $n = 10$ la differenza fra le due tavole è già sensibile.

**Esercizio 5. Due medie con varianza combinata.** Due metodi di studio: 12 studenti con il metodo 1 ottengono in media 78 punti con $s_1 = 6$, 10 studenti con il metodo 2 ottengono 72 con $s_2 = 5$. Al 5%, i metodi danno risultati diversi? Dare l'intervallo al 95% per la differenza.

Si suppongono popolazioni normali con la stessa varianza. La varianza combinata è
$$s_p^2 = \frac{11 \cdot 36 + 9 \cdot 25}{12 + 10 - 2} = \frac{621}{20} = 31{,}05, \qquad s_p = 5{,}57.$$
L'errore standard della differenza è $s_p\sqrt{\frac{1}{12} + \frac{1}{10}} = 2{,}39$, e $t = \frac{78 - 72}{2{,}39} = 2{,}51$, con 20 gradi di libertà. Poiché $t_{0,025; 20} = 2{,}086$, si rifiuta $H_0: \mu_1 = \mu_2$ (p-value 0,021). L'intervallo è $6 \pm 2{,}086 \cdot 2{,}39 = [1{,}0;\ 11{,}0]$: non contiene lo 0, coerentemente con il test.

**Esercizio 6. Dati appaiati.** Sei pazienti misurano la pressione prima e dopo un farmaco; le differenze "prima meno dopo" sono $3, 5, -1, 4, 2, 5$. Il farmaco abbassa la pressione?

I dati non sono due campioni indipendenti: sono le stesse persone. Si lavora sulle differenze, con $H_0: \mu_D = 0$ contro $\mu_D > 0$. $\bar d = 3$, $s_D^2 = \frac{0 + 4 + 16 + 1 + 1 + 4}{5} = 5{,}2$, $s_D = 2{,}28$. $t = \frac{3}{2{,}28/\sqrt{6}} = 3{,}22$ con 5 gradi di libertà; $t_{0,05; 5} = 2{,}015$: si rifiuta, il farmaco abbassa la pressione (p-value unilatero circa 0,012). Trattare i dati come due campioni indipendenti sarebbe un errore: si perderebbe l'informazione che le misure vengono a coppie, e la variabilità fra persone diverse coprirebbe l'effetto.

**Esercizio 7. Chi-quadro di adattamento: il dado è truccato?** In 120 lanci le facce da 1 a 6 escono $25, 17, 15, 23, 24, 16$ volte.

$H_0$: il dado è equo, quindi ogni faccia è attesa $e_i = 20$ volte. $\chi^2 = \sum \frac{(o_i - e_i)^2}{e_i} = \frac{25 + 9 + 25 + 9 + 16 + 16}{20} = 5{,}0$. I gradi di libertà sono $6 - 1 = 5$ (le frequenze hanno un vincolo, la somma è 120). $\chi^2_{0,05; 5} = 11{,}07$: non si rifiuta, le differenze sono compatibili con il caso (p-value 0,42).

**Esercizio 8. ANOVA con la tabella completa.** Tre macchine producono pezzi; il peso in grammi di quattro pezzi per macchina è: A: 10, 12, 11, 13; B: 14, 15, 13, 16; C: 11, 10, 12, 11. Le macchine producono pezzi dello stesso peso medio?

Medie: $\bar x_A = 11{,}5$, $\bar x_B = 14{,}5$, $\bar x_C = 11$, media generale $\bar x = \frac{148}{12} = 12{,}33$.

| Fonte | $SS$ | gradi di libertà | $MS = SS/\text{gdl}$ |
|---|---|---|---|
| fra i gruppi | $4\big[(11{,}5 - 12{,}33)^2 + (14{,}5 - 12{,}33)^2 + (11 - 12{,}33)^2\big] = 28{,}67$ | $k - 1 = 2$ | 14,33 |
| dentro i gruppi | $5 + 5 + 2 = 12$ | $N - k = 9$ | 1,33 |
| totale | 40,67 | 11 | |

$F = \frac{14{,}33}{1{,}33} = 10{,}75$, e $F_{0,05; 2, 9} = 4{,}26$: si rifiuta l'uguaglianza delle medie (p-value 0,004). L'ANOVA dice solo che *almeno due* medie sono diverse; dalle medie si vede che è la macchina B a produrre pezzi più pesanti.

**Esercizio 9. Quanti dati servono per vedere una differenza?** Nel test $H_0: \mu = 500$ contro $\mu > 500$ con $\sigma = 100$ e $\alpha = 5\%$ (paragrafo 4.6), quanti pesci servono perché la potenza sia del 90% quando $\mu = 520$?

Si rifiuta se $\bar x > 500 + z_\alpha\frac{\sigma}{\sqrt n}$; la potenza in $\mu = 520$ è $P\left[Z > z_\alpha - \frac{20\sqrt n}{100}\right]$, che vale 0,90 quando $z_\alpha - \frac{20\sqrt n}{100} = -z_{0,10} = -1{,}2816$. Quindi
$$\sqrt n = \frac{(1{,}645 + 1{,}2816) \cdot 100}{20} = 14{,}63, \qquad n \ge 214{,}1,$$
cioè servono 215 pesci, più del doppio dei 100 del paragrafo 4.6, dove la potenza era del 64%.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Un sondaggio.** Su 1000 intervistati, 540 sono favorevoli a una proposta. Si può dire, all'1%, che la maggioranza è favorevole?

*Passo 1: le ipotesi.* La domanda è se $p > 0{,}5$: $H_0: p = 0{,}5$ contro $H_1: p > 0{,}5$.

*Passo 2: la statistica.* $Z = \frac{\hat p - 0{,}5}{\sqrt{0{,}5 \cdot 0{,}5/1000}}$, circa normale standard sotto $H_0$. Al denominatore va $p_0$, non $\hat p$: la legge si calcola supponendo vera $H_0$.

*Passo 3: la regione di rifiuto.* All'1%, unilatero: $z > 2{,}326$.

*Passo 4: il valore.* $z = \frac{0{,}04}{0{,}0158} = 2{,}53$.

*Passo 5: decisione.* Si rifiuta $H_0$: p-value $1 - \Phi(2{,}53) = 0{,}006$.

**Guidato 2. Un funnel plot in piccolo.** Tre reparti hanno avuto rispettivamente 3 pezzi difettosi su 40, 12 su 100 e 30 su 400. Che cosa dice il funnel plot al 95%?

*Passo 1: il tasso comune.* $\bar p = \frac{3 + 12 + 30}{40 + 100 + 400} = \frac{45}{540} = 0{,}0833$.

*Passo 2: le deviazioni standard.* $\sqrt{\bar p(1 - \bar p)/n}$ vale 0,0437 per $n = 40$, 0,0276 per $n = 100$, 0,0138 per $n = 400$.

*Passo 3: i valori $z$.* Reparto 1: $\frac{0{,}075 - 0{,}0833}{0{,}0437} = -0{,}19$. Reparto 2: $\frac{0{,}12 - 0{,}0833}{0{,}0276} = 1{,}33$. Reparto 3: $\frac{0{,}075 - 0{,}0833}{0{,}0138} = -0{,}60$.

*Passo 4: conclusione.* Tutti i $|z|$ sono minori di 1,96: i tre reparti sono dentro l'imbuto. Il 12% del secondo reparto sembra alto, ma con 100 pezzi è compatibile con un tasso dell'8%.

**Guidato 3. Chi-quadro di indipendenza su una tabella $2 \times 2$.** Su 200 clienti, 60 dei 100 che hanno ricevuto un'offerta via email hanno comprato, contro 45 dei 100 che non l'hanno ricevuta. Acquisto e offerta sono indipendenti, al 5%?

*Passo 1: la tabella.* Righe: email sì (60 comprano, 40 no), email no (45 comprano, 55 no). Totali di colonna: 105 comprano, 95 no.

*Passo 2: le frequenze attese.* $e_{ij} = \frac{n_{i\cdot}\,n_{\cdot j}}{n}$: per entrambe le righe $\frac{100 \cdot 105}{200} = 52{,}5$ e $\frac{100 \cdot 95}{200} = 47{,}5$.

*Passo 3: la statistica.* $\chi^2 = \frac{7{,}5^2}{52{,}5} + \frac{7{,}5^2}{47{,}5} + \frac{7{,}5^2}{52{,}5} + \frac{7{,}5^2}{47{,}5} = 4{,}51$, con $(2 - 1)(2 - 1) = 1$ grado di libertà.

*Passo 4: decisione.* $\chi^2_{0,05; 1} = 3{,}841$: si rifiuta l'indipendenza. Il p-value è circa 0,034, quindi all'1% non si rifiuterebbe.

## Riepilogo

Un campione è una famiglia di variabili i.i.d. con la legge della popolazione; uno stimatore è una funzione del campione, corretto se ha speranza uguale al parametro, consistente se l'errore quadratico medio (varianza più distorsione al quadrato) tende a zero, più efficiente di un altro se ha varianza minore. La media campionaria e la varianza campionaria con $n - 1$ sono stimatori corretti di $\mu$ e $\sigma^2$. Un intervallo di confidenza al livello $1 - \alpha$ è costruito in modo che la procedura contenga il parametro nella frazione $1 - \alpha$ dei campioni: per la media con varianza nota è $\bar x \pm z_{\alpha/2}\sigma/\sqrt n$ (esatto per popolazioni normali, approssimato per $n$ grande), con varianza ignota $\bar x \pm t_{\alpha/2, n-1}s/\sqrt n$, per la varianza si usano due valori critici della chi-quadro, per una proporzione $\hat p \pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ o la versione prudente con $\frac{1}{2\sqrt n}$. La numerosità per una precisione $\varepsilon$ è $n \ge z_{\alpha/2}^2\sigma^2/\varepsilon^2$. Per due medie si usano le differenze, con la varianza combinata o con i dati appaiati. Un test di ipotesi rifiuta $H_0$ quando la statistica test cade nella regione di rifiuto, con probabilità di errore di I tipo $\alpha$; la potenza è la probabilità di rifiutare quando $H_0$ è falsa, e il p-value è il più piccolo livello a cui i dati portano a rifiutare. Gli stessi schemi danno i test per media, proporzione, varianza, differenza di medie, il test chi-quadro di indipendenza per le tabelle a due vie e l'ANOVA a una via, che confronta più medie con la statistica F.

## Formulario

Stimatori, intervalli, test e valori critici più usati, con i termini per l'orale.

### Stimatori

$$\bar X = \frac{1}{n}\sum X_i, \quad S^2 = \frac{1}{n - 1}\sum (X_i - \bar X)^2, \quad E[\bar X] = \mu, \quad \operatorname{Var}(\bar X) = \frac{\sigma^2}{n}, \quad MSE = \operatorname{Var} + (\text{distorsione})^2.$$

### Intervalli al livello $1 - \alpha$

| Parametro | Intervallo |
|---|---|
| $\mu$, $\sigma$ nota | $\bar x \pm z_{\alpha/2}\,\sigma/\sqrt n$ |
| $\mu$, $\sigma$ ignota, normale | $\bar x \pm t_{\alpha/2, n-1}\,s/\sqrt n$ |
| $p$, $n$ grande | $\hat p \pm z_{\alpha/2}\sqrt{\hat p(1 - \hat p)/n}$ |
| $\sigma^2$, normale | $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}\right]$ |
| $\mu_1 - \mu_2$, varianze uguali | $\bar x_1 - \bar x_2 \pm t_{\alpha/2, n_1+n_2-2}\,s_p\sqrt{1/n_1 + 1/n_2}$ |

Numerosità per un errore massimo $\varepsilon$: $n \ge \left(\frac{z_{\alpha/2}\sigma}{\varepsilon}\right)^2$ per la media, $n \ge \frac{z_{\alpha/2}^2}{4\varepsilon^2}$ per una proporzione (caso peggiore $p = \frac12$).

### Test

| $H_0$ | Statistica | Legge sotto $H_0$ |
|---|---|---|
| $\mu = \mu_0$, $\sigma$ nota | $\frac{\bar X - \mu_0}{\sigma/\sqrt n}$ | $N(0, 1)$ |
| $\mu = \mu_0$, $\sigma$ ignota | $\frac{\bar X - \mu_0}{S/\sqrt n}$ | $t_{n-1}$ |
| $p = p_0$ | $\frac{\hat p - p_0}{\sqrt{p_0(1 - p_0)/n}}$ | circa $N(0, 1)$ |
| $\sigma^2 = \sigma_0^2$ | $\frac{(n-1)S^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ |
| $\mu_1 = \mu_2$ | $\frac{\bar X_1 - \bar X_2}{S_p\sqrt{1/n_1 + 1/n_2}}$ | $t_{n_1+n_2-2}$ |
| appaiati | $\frac{\bar D}{S_D/\sqrt n}$ | $t_{n-1}$ |
| adattamento, $k$ classi | $\sum \frac{(o_i - e_i)^2}{e_i}$ | $\chi^2_{k-1}$ |
| indipendenza, $m \times k$ | $\sum \frac{(n_{ij} - e_{ij})^2}{e_{ij}}$, $e_{ij} = \frac{n_{i\cdot}n_{\cdot j}}{n}$ | $\chi^2_{(m-1)(k-1)}$ |
| ANOVA, $k$ gruppi | $\frac{SS_B/(k-1)}{SS_W/(N-k)}$ | $F_{k-1, N-k}$ |

Funnel plot: curve $\bar p \pm z\sqrt{\bar p(1 - \bar p)/n}$ con $z = 1{,}96$ e $3{,}09$.

### Valori critici della normale

| $\alpha$ | 0,10 | 0,05 | 0,025 | 0,01 | 0,005 | 0,001 |
|---|---|---|---|---|---|---|
| $z_\alpha$ | 1,282 | 1,645 | 1,960 | 2,326 | 2,576 | 3,090 |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Stimatore corretto, consistente, efficiente | speranza uguale al parametro; MSE che tende a 0; varianza minore |
| Intervallo di confidenza | intervallo casuale che contiene il parametro con probabilità $1 - \alpha$ |
| Ipotesi nulla e alternativa | l'affermazione da mettere alla prova e quella che si accetta se la si rifiuta |
| Errore di I e II tipo | rifiutare $H_0$ vera; accettare $H_0$ falsa |
| Livello di significatività | probabilità massima di errore di I tipo |
| Potenza | probabilità di rifiutare $H_0$ quando è falsa |
| p-value | probabilità, sotto $H_0$, di un risultato almeno così estremo |
| Gradi di libertà | numero di quantità libere dopo i vincoli |
| Funnel plot | confronto di tassi con curve di controllo che dipendono da $n$ |

### Domande che tornano spesso

- Perché $S^2$ si divide per $n - 1$? Dimostrare che è corretto.
- Ricavare l'intervallo per la media con varianza nota; che cosa vuol dire "al 95%"?
- Quando si usa la t di Student e perché le sue code sono più pesanti della normale?
- Definire errori di I e II tipo, potenza e p-value; legame fra test bilatero e intervallo di confidenza.
- Test chi-quadro: come si calcolano le frequenze attese e i gradi di libertà?
- Idea dell'ANOVA: perché si confronta la varianza fra i gruppi con quella dentro i gruppi?
- A che cosa serve un funnel plot, e perché una classifica dei tassi è fuorviante?
