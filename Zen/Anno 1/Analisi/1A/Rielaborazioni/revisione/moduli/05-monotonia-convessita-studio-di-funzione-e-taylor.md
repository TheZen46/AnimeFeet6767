---
corso: Analisi Matematica 1A
modulo: 5
titolo: Monotonia, convessità, studio di funzione e Taylor
programma: [AM1A-14, AM1A-15, AM1A-17]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-03
---

# 5 · Monotonia, convessità, studio di funzione e Taylor

**In questo modulo.** Prerequisiti: il modulo 4 (Derivate e teoremi del valor medio) e, per gli sviluppi, i simboli di Landau del modulo 3. Il segno della derivata prima dice dove una funzione cresce e dove ha i suoi estremi; il segno della derivata seconda dice dove è convessa o concava. Con questi strumenti, insieme a limiti e asintoti, si disegna il grafico di una funzione. La seconda parte del modulo è dedicata alla formula di Taylor, che approssima una funzione con un polinomio vicino a un punto. Gli sviluppi notevoli e le regole per combinarli permettono di calcolare limiti e ordini di infinitesimo che con i soli limiti notevoli restano fuori portata. Alla fine del modulo si sa svolgere uno studio di funzione completo e usare gli sviluppi di Taylor negli esercizi d'esame.

## 5.1 Monotonia e segno della derivata

> [!teorema] Criterio di monotonia
> Sia $f$ continua su un intervallo $I$ e derivabile nei punti interni di $I$.
>
> 1. $f$ è crescente su $I$ se e solo se $f'(x) \ge 0$ in ogni punto interno $x$ di $I$; è decrescente se e solo se $f'(x) \le 0$.
> 2. Se $f'(x) > 0$ in ogni punto interno di $I$, allora $f$ è strettamente crescente su $I$; se $f'(x) < 0$, strettamente decrescente.

*Dimostrazione.* (1, $\Rightarrow$) Sia $f$ crescente e $x$ interno a $I$. Per ogni $y \in I$, $y \ne x$, il rapporto incrementale $\frac{f(y) - f(x)}{y - x}$ è $\ge 0$: se $y > x$ numeratore e denominatore sono entrambi $\ge 0$ e $> 0$, se $y < x$ sono entrambi $\le 0$ e $< 0$. Per la permanenza del segno il limite per $y \to x$, cioè $f'(x)$, è $\ge 0$.

(1, $\Leftarrow$) Siano $x_1 < x_2$ in $I$. Per il teorema di Lagrange su $[x_1, x_2]$ esiste $\bar{x} \in (x_1, x_2)$, interno a $I$, con
$$f(x_2) - f(x_1) = f'(\bar{x})\,(x_2 - x_1) \ge 0,$$
quindi $f(x_1) \le f(x_2)$. (2) Con lo stesso argomento, se $f' > 0$ la differenza è strettamente positiva.

> [!attenzione]
> Il punto 2 non si inverte: $f(x) = x^3$ è strettamente crescente su $\mathbb{R}$, ma $f'(0) = 0$. E serve che il dominio sia un intervallo: $-\frac{1}{x}$ ha derivata $\frac{1}{x^2} > 0$ su $\mathbb{R} \setminus \{0\}$, ma non è crescente, perché $-\frac{1}{-1} = 1 > -1 = -\frac{1}{1}$.

## 5.2 Ricerca degli estremi

Dal criterio di monotonia segue il modo standard di classificare i punti critici.

> [!teorema] Test della derivata prima
> Sia $f$ continua su un intervallo $I$ e derivabile nei punti interni, e sia $x_0$ un punto interno con $f'(x_0) = 0$. Se $f'(x) \ge 0$ in un intorno sinistro di $x_0$ e $f'(x) \le 0$ in un intorno destro (escluso $x_0$), allora $x_0$ è un punto di massimo relativo; con i segni opposti è di minimo relativo. Se le disuguaglianze sono strette, l'estremo è stretto.

Gli estremi di una funzione vanno cercati fra i punti critici interni (per Fermat), i punti in cui la funzione non è derivabile e gli estremi del dominio; il segno di $f'$ dice poi quali di questi sono massimi o minimi.

> [!esempio] Gli estremi di $x \arctan x$
> $f(x) = x \arctan x$ è derivabile su $\mathbb{R}$, con
> $$f'(x) = \arctan x + \frac{x}{1 + x^2}.$$
> Per $x > 0$ entrambi gli addendi sono positivi, per $x < 0$ entrambi negativi: $f'(x) > 0$ per $x > 0$, $f'(x) < 0$ per $x < 0$ e $f'(0) = 0$. L'unico punto critico è 0. La funzione decresce strettamente su $(-\infty, 0]$ e cresce strettamente su $[0, +\infty)$: 0 è un punto di minimo stretto, anzi assoluto, con $f(0) = 0$.

## 5.3 Derivate successive

Se $f$ è derivabile in un intorno $I$ di $x_0$, la derivata è a sua volta una funzione $f' : I \to \mathbb{R}$, che si può provare a derivare.

> [!definizione] Derivata seconda e derivate di ordine superiore
> Se $f'$ è derivabile in $x_0$, si dice che $f$ è derivabile due volte in $x_0$, e la **derivata seconda** è
> $$f''(x_0) = \lim_{x \to x_0} \frac{f'(x) - f'(x_0)}{x - x_0}.$$
> Iterando si definiscono $f''' = f^{(3)}$, $f^{(4)}$, …, $f^{(k)}$, con $f^{(0)} = f$.

> [!esempio]
> Per $k \le n$, $(x^n)^{(k)} = n(n-1) \cdots (n - k + 1)\, x^{n-k}$; in particolare $(x^n)^{(n)} = n!$ e $(x^n)^{(k)} = 0$ per $k > n$. Per l'esponenziale $(e^x)^{(k)} = e^x$ per ogni $k$; per il seno le derivate si ripetono ogni quattro: $\sin$, $\cos$, $-\sin$, $-\cos$, $\sin$, …

> [!definizione] Classi $C^k$
> Una funzione $f : I \to \mathbb{R}$ è **di classe $C^k$** sull'intervallo $I$, e si scrive $f \in C^k(I)$, se è derivabile $k$ volte in $I$ e $f^{(k)}$ è continua su $I$; è **di classe $C^\infty$** se è di classe $C^k$ per ogni $k$. Polinomi, esponenziali, seno e coseno sono di classe $C^\infty$ su $\mathbb{R}$.

## 5.4 Convessità e flessi

> [!definizione] Funzione convessa e concava
> Sia $f$ derivabile su un intervallo $I$. La funzione è **convessa** su $I$ se per ogni $x_1, x_2 \in I$
> $$f(x_2) \ge f(x_1) + f'(x_1)(x_2 - x_1),$$
> cioè se il grafico sta sopra ogni sua retta tangente; è **concava** con la disuguaglianza opposta. È **strettamente** convessa o concava se la disuguaglianza è stretta per $x_1 \ne x_2$.

![Figura 5.1](../figure/5-1.svg)

*Figura 5.1. Grafico di una funzione convessa su $I$ con due rette tangenti, sotto il grafico.*

> [!esempio] $x^2$ è strettamente convessa
> Bisogna verificare che $x_2^2 > x_1^2 + 2x_1(x_2 - x_1)$ per ogni $x_1 \ne x_2$. Portando tutto a sinistra:
> $$x_2^2 - x_1^2 - 2x_1 x_2 + 2x_1^2 = x_2^2 - 2x_1 x_2 + x_1^2 = (x_2 - x_1)^2 > 0.$$

> [!teorema] Convessità e derivate
> Sia $f$ derivabile sull'intervallo $I$.
>
> 1. $f$ è convessa su $I$ se e solo se $f'$ è crescente su $I$ (concava se e solo se $f'$ è decrescente).
> 2. Se $f'$ è strettamente crescente, $f$ è strettamente convessa.
>
> Se $f$ è derivabile due volte su $I$, ne segue che $f$ è convessa se e solo se $f''(x) \ge 0$ per ogni $x \in I$, e che $f'' > 0$ su $I$ implica la convessità stretta.

*Dimostrazione di 1.* ($\Rightarrow$) Siano $x_1 < x_2$ in $I$. La convessità, scritta nei due punti, dà
$$f(x_2) \ge f(x_1) + f'(x_1)(x_2 - x_1), \qquad f(x_1) \ge f(x_2) + f'(x_2)(x_1 - x_2).$$
Sommando membro a membro e semplificando si ottiene $0 \ge (x_2 - x_1)\big(f'(x_1) - f'(x_2)\big)$; poiché $x_2 - x_1 > 0$, è $f'(x_1) \le f'(x_2)$.

($\Leftarrow$) Siano $x_1 \ne x_2$ in $I$; per Lagrange $f(x_2) = f(x_1) + f'(\bar{x})(x_2 - x_1)$ con $\bar{x}$ fra $x_1$ e $x_2$. Se $x_1 < x_2$, allora $\bar{x} > x_1$ e, essendo $f'$ crescente, $f'(\bar{x}) \ge f'(x_1)$; moltiplicando per $x_2 - x_1 > 0$ si ha $f(x_2) \ge f(x_1) + f'(x_1)(x_2 - x_1)$. Se $x_1 > x_2$, allora $\bar{x} < x_1$, quindi $f'(\bar{x}) \le f'(x_1)$; moltiplicando per $x_2 - x_1 < 0$ la disuguaglianza si inverte e si ottiene la stessa conclusione. La parte con $f''$ segue applicando il criterio di monotonia (paragrafo 5.1) alla funzione $f'$.

> [!attenzione]
> Anche qui la condizione sufficiente non si inverte: $x^4$ è strettamente convessa, ma $f''(x) = 12x^2$ si annulla in 0.

> [!definizione] Punto di flesso
> Sia $f$ derivabile in $x_0$. Il punto $x_0$ è di **flesso** se in un intorno di $x_0$ il grafico passa da una parte all'altra della tangente in $x_0$, cioè se, con $t(x) = f(x_0) + f'(x_0)(x - x_0)$, vale $f(x) \le t(x)$ per $x < x_0$ e $f(x) \ge t(x)$ per $x > x_0$ (flesso **ascendente**), oppure il contrario (flesso **discendente**).

> [!teorema] Flessi e derivata seconda
> Sia $f$ derivabile due volte in un intorno di $x_0$.
>
> 1. Se $x_0$ è un punto di flesso, allora $f''(x_0) = 0$.
> 2. Se $f''(x_0) = 0$ e $f''$ cambia segno in $x_0$ (negativa a sinistra e positiva a destra, oppure il contrario), allora $x_0$ è un punto di flesso: ascendente nel primo caso, discendente nel secondo.

![Figura 5.2](../figure/5-2.svg)

*Figura 5.2. Flesso ascendente e discendente, con la retta tangente nel punto di flesso.*

> [!esempio]
> Per $f(x) = x \arctan x$ si ha
> $$f''(x) = \frac{1}{1 + x^2} + \frac{(1 + x^2) - 2x^2}{(1 + x^2)^2} = \frac{2}{(1 + x^2)^2} > 0,$$
> quindi la funzione è strettamente convessa su $\mathbb{R}$ e non ha flessi.

## 5.5 Studio di funzione

Per disegnare il grafico di $f$ si raccolgono, in quest'ordine, le informazioni seguenti.

1. **Dominio**, eventuali simmetrie (funzione pari o dispari) e periodicità; segno e zeri, se si trovano facilmente.
2. **Limiti** agli estremi del dominio e nei punti esclusi; **asintoti** orizzontali, obliqui e verticali.
3. **Derivata prima**: punti di non derivabilità, punti critici, intervalli di monotonia, estremi relativi e assoluti.
4. **Derivata seconda**: intervalli di convessità e concavità, flessi.
5. **Grafico**, coerente con tutte le informazioni raccolte.

**Esempio completo: $f(x) = x\, e^{-x}$.**

*Dominio e segno.* $f$ è definita e di classe $C^\infty$ su $\mathbb{R}$. Non è né pari né dispari. Poiché $e^{-x} > 0$, il segno è quello di $x$: $f < 0$ per $x < 0$, $f(0) = 0$, $f > 0$ per $x > 0$.

*Limiti e asintoti.* Per $x \to -\infty$, $x \to -\infty$ ed $e^{-x} \to +\infty$, quindi $f(x) \to -\infty$; inoltre $\frac{f(x)}{x} = e^{-x} \to +\infty$, e non c'è asintoto obliquo. Per $x \to +\infty$ la forma è $\infty \cdot 0$: $f(x) = \frac{x}{e^x} \to 0$ per la gerarchia degli infiniti (o per de l'Hôpital), e $y = 0$ è asintoto orizzontale a destra.

*Derivata prima.* $f'(x) = e^{-x} - x e^{-x} = (1 - x)\, e^{-x}$, positiva per $x < 1$ e negativa per $x > 1$. La funzione cresce su $(-\infty, 1]$ e decresce su $[1, +\infty)$: $x = 1$ è il punto di massimo assoluto, con $f(1) = \frac{1}{e}$. L'immagine è $\left(-\infty, \frac{1}{e}\right]$.

*Derivata seconda.* $f''(x) = -e^{-x} - (1 - x)\, e^{-x} = (x - 2)\, e^{-x}$: la funzione è concava su $(-\infty, 2]$ e convessa su $[2, +\infty)$, e $x = 2$ è un punto di flesso, con $f(2) = \frac{2}{e^2}$.

*Grafico.* Sale da $-\infty$ passando per l'origine, raggiunge il massimo $\left(1, \frac{1}{e}\right)$, scende, cambia concavità in $\left(2, \frac{2}{e^2}\right)$ e si avvicina all'asse $x$ da sopra.

![Figura 5.3](../figure/5-3.svg)

*Figura 5.3. Grafico di $x e^{-x}$ con il massimo in $(1, 1/e)$, il flesso in $(2, 2/e^2)$ e l'asintoto $y = 0$.*

## 5.6 Formula di Taylor

L'idea è approssimare $f$ vicino a $x_0$ con il polinomio che ha in $x_0$ lo stesso valore e le stesse derivate di $f$, fino a un certo ordine.

> [!definizione] Polinomio di Taylor
> Sia $f$ derivabile $n$ volte in $x_0$. Il **polinomio di Taylor** di $f$ di ordine $n$ e centro $x_0$ è
> $$T_{n,x_0} f(x) := \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}\,(x - x_0)^k = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2}(x - x_0)^2 + \dots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n.$$
> Con $x_0 = 0$ si chiama anche **polinomio di Mac Laurin**.

Per $n = 0$ è la costante $f(x_0)$, per $n = 1$ la retta tangente. Derivando termine a termine e valutando in $x_0$ si verifica che $\left(T_{n,x_0} f\right)^{(k)}(x_0) = f^{(k)}(x_0)$ per $k = 0, 1, \dots, n$: il termine di grado $k$ è l'unico che contribuisce alla derivata $k$-esima in $x_0$, e la sua derivata $k$-esima vale $\frac{f^{(k)}(x_0)}{k!} \cdot k! = f^{(k)}(x_0)$.

> [!teorema] Formula di Taylor con resto di Peano
> Sia $f$ derivabile $n$ volte in $x_0$. Allora
> $$f(x) = T_{n,x_0} f(x) + o\big((x - x_0)^n\big), \qquad x \to x_0.$$

*Dimostrazione.* Si deve mostrare che $\frac{f(x) - T_{n,x_0} f(x)}{(x - x_0)^n} \to 0$. Sia $R = f - T_{n,x_0} f$. Per quanto appena osservato $R^{(k)}(x_0) = 0$ per $k = 0, \dots, n$, e per $k \le n - 1$ la funzione $R^{(k)}$ è derivabile vicino a $x_0$, quindi continua: $R^{(k)}(x) \to 0$ per $x \to x_0$. Numeratore e denominatore sono quindi infinitesimi, e si può applicare de l'Hôpital $n - 1$ volte:
$$\lim_{x \to x_0} \frac{R(x)}{(x - x_0)^n} \overset{H}{=} \lim_{x \to x_0} \frac{R'(x)}{n(x - x_0)^{n-1}} \overset{H}{=} \dots \overset{H}{=} \lim_{x \to x_0} \frac{R^{(n-1)}(x)}{n!\,(x - x_0)}.$$
A questo punto non si deriva più, perché $f^{(n)}$ esiste solo in $x_0$, non in un intorno. Si scrive esplicitamente $R^{(n-1)}(x) = f^{(n-1)}(x) - f^{(n-1)}(x_0) - f^{(n)}(x_0)(x - x_0)$ e si usa la definizione di derivata:
$$\frac{R^{(n-1)}(x)}{n!\,(x - x_0)} = \frac{1}{n!}\left(\frac{f^{(n-1)}(x) - f^{(n-1)}(x_0)}{x - x_0} - f^{(n)}(x_0)\right) \longrightarrow \frac{1}{n!}\big(f^{(n)}(x_0) - f^{(n)}(x_0)\big) = 0.$$

Il resto di Peano dice *come* l'errore tende a zero, ma non quanto vale. Per stimarlo serve un'altra forma del resto.

> [!teorema] Formula di Taylor con resto di Lagrange
> Sia $f$ di classe $C^n$ in un intorno $I$ di $x_0$ e derivabile $n + 1$ volte in $I \setminus \{x_0\}$. Per ogni $x \in I$, $x \ne x_0$, esiste $\bar{x}$ strettamente compreso fra $x_0$ e $x$ tale che
> $$f(x) = T_{n,x_0} f(x) + \frac{f^{(n+1)}(\bar{x})}{(n+1)!}\,(x - x_0)^{n+1}.$$

Per $n = 0$ è il teorema di Lagrange. Ad esempio, per $f(x) = e^x$, $x_0 = 0$ e $x = 1$, con $0 < \bar{x} < 1$:
$$e = \sum_{k=0}^{n} \frac{1}{k!} + \frac{e^{\bar{x}}}{(n+1)!}, \qquad 0 < e - \sum_{k=0}^{n} \frac{1}{k!} < \frac{3}{(n+1)!}.$$
Con $n = 7$ l'errore è minore di $10^{-4}$.

> [!teorema] Unicità del polinomio di Taylor
> Sia $f$ derivabile $n$ volte in $x_0$ e sia $P$ un polinomio di grado $\le n$ tale che $f(x) = P(x) + o\big((x - x_0)^n\big)$ per $x \to x_0$. Allora $P = T_{n,x_0} f$.

È questo risultato a rendere utili gli sviluppi: qualunque procedimento produca un polinomio di grado $\le n$ che approssima $f$ a meno di $o\big((x - x_0)^n\big)$ ha trovato il polinomio di Taylor, anche senza calcolare le derivate.

## 5.7 Sviluppi notevoli e operazioni

Per $x \to 0$ valgono gli sviluppi seguenti. I primi tre si ottengono dalle derivate in 0, come negli appunti.

- **Esponenziale.** $(e^x)^{(k)}(0) = 1$ per ogni $k$, quindi
$$e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \dots + \frac{x^n}{n!} + o(x^n) = \sum_{k=0}^{n} \frac{x^k}{k!} + o(x^n).$$
- **Logaritmo.** Le derivate di $\ln(1 + x)$ sono $\frac{1}{1 + x}$, $-\frac{1}{(1 + x)^2}$, $\frac{2}{(1 + x)^3}$, …, e in generale la $k$-esima vale $(-1)^{k-1}(k-1)!$ in 0. Quindi
$$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n) = \sum_{k=1}^{n} \frac{(-1)^{k-1}}{k} x^k + o(x^n).$$
- **Seno.** Le derivate in 0 si ripetono come $0, 1, 0, -1$: quelle di ordine pari sono nulle, quella di ordine $2l + 1$ vale $(-1)^l$. Quindi
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots + (-1)^{n-1}\frac{x^{2n-1}}{(2n-1)!} + o(x^{2n}).$$
Poiché il coefficiente di $x^{2n}$ è nullo, il polinomio di ordine $2n - 1$ coincide con quello di ordine $2n$, e il resto è $o(x^{2n})$ invece che $o(x^{2n-1})$.

Con lo stesso metodo si ottengono gli altri sviluppi notevoli, per $x \to 0$:
$$\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{4!} - \dots + (-1)^n \frac{x^{2n}}{(2n)!} + o(x^{2n+1}),$$
$$\frac{1}{1 - x} = 1 + x + x^2 + \dots + x^n + o(x^n),$$
$$(1 + x)^\alpha = 1 + \alpha x + \binom{\alpha}{2} x^2 + \dots + \binom{\alpha}{n} x^n + o(x^n), \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha - 1)\cdots(\alpha - k + 1)}{k!},$$
$$\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots + (-1)^n \frac{x^{2n+1}}{2n+1} + o(x^{2n+2}).$$
Ad esempio $\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + o(x^2)$.

Grazie all'unicità, gli sviluppi di funzioni costruite a partire da questi si ottengono con l'algebra, senza calcolare derivate.

**Somma.** Se $f$ e $g$ sono derivabili $n$ volte in $x_0$, sommando i due sviluppi si ottiene un polinomio di grado $\le n$ più $o\big((x - x_0)^n\big)$; per l'unicità, $T_{n,x_0}(f + g) = T_{n,x_0} f + T_{n,x_0} g$.

**Prodotto.** Moltiplicando gli sviluppi,
$$f(x)\, g(x) = T_{n,x_0} f(x) \cdot T_{n,x_0} g(x) + o\big((x - x_0)^n\big).$$
Il prodotto dei due polinomi ha grado fino a $2n$; i termini di grado $> n$ sono anch'essi $o\big((x - x_0)^n\big)$. Quindi $T_{n,x_0}(fg)$ è il prodotto dei polinomi **troncato** al grado $n$.

**Quoziente.** Se $g(x_0) \ne 0$, si cerca $P = T_{n,x_0}\left(\frac{f}{g}\right)$. Da $f = \frac{f}{g} \cdot g$ e dalla regola del prodotto segue che $T_{n,x_0} f$ è il prodotto $P \cdot T_{n,x_0} g$ troncato al grado $n$: i coefficienti di $P$ si trovano uno alla volta, confrontando i coefficienti delle potenze uguali. In pratica, per $x_0 = 0$ e $g(0) = 1$, conviene scrivere $\frac{1}{g} = \frac{1}{1 - t}$ con $t = 1 - g(x) \to 0$ e usare lo sviluppo di $\frac{1}{1 - t}$. Ad esempio
$$\tan x = \frac{\sin x}{\cos x} = \left(x - \frac{x^3}{6}\right)\left(1 + \frac{x^2}{2}\right) + o(x^3) = x + \frac{x^3}{3} + o(x^3),$$
dove $\frac{1}{\cos x} = \frac{1}{1 - \left(\frac{x^2}{2} + o(x^3)\right)} = 1 + \frac{x^2}{2} + o(x^3)$.

**Composizione.** Se $t = g(x) \to 0$ per $x \to 0$, nello sviluppo di $f(t)$ si sostituisce lo sviluppo di $g$ e si tengono solo i termini fino al grado voluto. Ad esempio, con $t = \cos x - 1 = -\frac{x^2}{2} + \frac{x^4}{24} + o(x^4)$:
$$\ln(\cos x) = \ln(1 + t) = t - \frac{t^2}{2} + o(t^2) = -\frac{x^2}{2} + \frac{x^4}{24} - \frac{x^4}{8} + o(x^4) = -\frac{x^2}{2} - \frac{x^4}{12} + o(x^4).$$
Poiché $t \sim -\frac{x^2}{2}$, il termine $t^2$ è di ordine 4 e $o(t^2) = o(x^4)$; il termine $t^3$ sarebbe di ordine 6 e si trascura.

## 5.8 Applicazioni degli sviluppi

**Limiti.** Nelle forme $\frac{0}{0}$ si sviluppano numeratore e denominatore fino al primo termine che non si cancella.
$$\lim_{x \to 0} \frac{\sin x - x \cos x}{x^3} = \lim_{x \to 0} \frac{\left(x - \frac{x^3}{6}\right) - \left(x - \frac{x^3}{2}\right) + o(x^3)}{x^3} = \lim_{x \to 0} \frac{\frac{x^3}{3} + o(x^3)}{x^3} = \frac{1}{3}.$$
Con i soli limiti notevoli questo limite non si calcola: i termini di primo grado si cancellano e serve l'ordine successivo.

**Ordine e parte principale.** Lo stesso calcolo dice che $\sin x - x \cos x$ è, per $x \to 0$, un infinitesimo di ordine 3 con parte principale $\frac{x^3}{3}$. Allo stesso modo $e^x - 1 - x = \frac{x^2}{2} + o(x^2)$ ha ordine 2, e $\cos x - 1 + \frac{x^2}{2} = \frac{x^4}{24} + o(x^4)$ ha ordine 4.

**Natura dei punti critici.** Sia $f'(x_0) = 0$ e sia $f^{(n)}(x_0)$ la prima derivata non nulla in $x_0$, con $n \ge 2$. Dalla formula di Peano,
$$f(x) - f(x_0) = \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n + o\big((x - x_0)^n\big),$$
quindi vicino a $x_0$ la differenza ha il segno di $f^{(n)}(x_0)(x - x_0)^n$. Se $n$ è pari, $x_0$ è un punto di minimo stretto quando $f^{(n)}(x_0) > 0$ e di massimo stretto quando $f^{(n)}(x_0) < 0$. Se $n$ è dispari, non è un estremo ma un flesso a tangente orizzontale. Il caso più usato è $n = 2$: $f'(x_0) = 0$ e $f''(x_0) > 0$ danno un minimo, $f''(x_0) < 0$ un massimo. Per $x^3$ in 0 la prima derivata non nulla è la terza: flesso; per $x^4$ è la quarta, positiva: minimo.

## 5.9 Gli sviluppi negli esercizi, passo per passo

Negli esercizi d'esame gli sviluppi servono quasi sempre in tre situazioni: un limite in forma $\frac{0}{0}$ in cui i limiti notevoli non bastano, l'ordine di infinitesimo di una differenza, e il polinomio di Taylor di una funzione composta. Il procedimento è sempre lo stesso.

1. **Decidere l'ordine.** Si sviluppa il pezzo "più semplice" (di solito il denominatore) e si guarda il suo primo termine: se è $x^n$, numeratore e denominatore vanno sviluppati fino all'ordine $n$. Se dopo le cancellazioni al numeratore resta solo $o(x^n)$, si torna indietro e si sviluppa di un ordine in più.
2. **Sviluppare ogni pezzo** con gli sviluppi notevoli, sempre con il resto: $o(x^n)$ va scritto, perché ricorda fin dove si è arrivati.
3. **Comporre.** Se compare $f(g(x))$ con $g(x) \to 0$, si pone $t = g(x)$, si sviluppa $f(t)$, si sostituisce lo sviluppo di $g$ e si buttano i termini di grado maggiore di $n$. Per sapere quante potenze di $t$ servono si guarda l'ordine di $g$: se $g \sim x^m$, allora $t^k$ ha ordine $km$, e bastano le potenze con $km \le n$.
4. **Sommare e semplificare**, raccogliendo i termini dello stesso grado e tutti i resti in un solo $o(x^n)$.

**Esempio: $e^{\sin x}$ fino all'ordine 3.** Con $t = \sin x = x - \frac{x^3}{6} + o(x^3)$, che ha ordine 1, servono le potenze di $t$ fino alla terza:
$$e^t = 1 + t + \frac{t^2}{2} + \frac{t^3}{6} + o(t^3).$$
Sostituendo: $t^2 = x^2 + o(x^3)$ (il doppio prodotto $-\frac{x^4}{3}$ è di ordine 4) e $t^3 = x^3 + o(x^3)$. Quindi
$$e^{\sin x} = 1 + \left(x - \frac{x^3}{6}\right) + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3) = 1 + x + \frac{x^2}{2} + o(x^3).$$
Il termine di terzo grado si cancella: per conoscere il primo termine dopo $\frac{x^2}{2}$ bisognerebbe sviluppare fino all'ordine 4 (si troverebbe $-\frac{x^4}{8}$).

**Esempio: un limite con un parametro.** Calcolare, al variare di $k \in \mathbb{R}$, $\displaystyle\lim_{x \to 0} \frac{e^{kx} - \sqrt{1 + 2x}}{x^2}$.

Il denominatore è $x^2$: si sviluppa il numeratore fino all'ordine 2. $e^{kx} = 1 + kx + \frac{k^2 x^2}{2} + o(x^2)$ e, con $(1 + y)^{1/2} = 1 + \frac{y}{2} - \frac{y^2}{8} + o(y^2)$ e $y = 2x$, $\sqrt{1 + 2x} = 1 + x - \frac{x^2}{2} + o(x^2)$. La differenza è
$$(k - 1)x + \frac{k^2 + 1}{2}x^2 + o(x^2).$$
Se $k \ne 1$ il termine dominante è $(k - 1)x$, e il rapporto si comporta come $\frac{k - 1}{x}$: il limite destro è $+\infty$ o $-\infty$ secondo il segno di $k - 1$, il sinistro è opposto, e il limite non esiste. Se $k = 1$ il numeratore è $x^2 + o(x^2)$ e il limite vale 1. È la struttura tipica degli esercizi con parametro: il parametro decide quale termine si cancella.

**Esempio: l'esponenziale di una forma $1^\infty$.** Calcolare $\displaystyle\lim_{x \to 0} \frac{(1 + x)^{a/x} - e^a}{x}$.

Si scrive $(1 + x)^{a/x} = e^{\frac{a}{x}\ln(1 + x)}$ e si sviluppa l'esponente: $\frac{a}{x}\left(x - \frac{x^2}{2} + o(x^2)\right) = a - \frac{a}{2}x + o(x)$. Quindi
$$(1 + x)^{a/x} = e^a \cdot e^{-\frac{a}{2}x + o(x)} = e^a\left(1 - \frac{a}{2}x + o(x)\right),$$
e il limite è $-\frac{a\,e^a}{2}$. Per $a = 0$ il numeratore è identicamente nullo e il limite è 0, coerente con la formula.

## Esempi ed esercizi svolti

> [!esempio] Un limite con due sviluppi
> $$\lim_{x \to 0} \frac{e^{x^2} - \cos x}{x^2} = \lim_{x \to 0} \frac{\left(1 + x^2\right) - \left(1 - \frac{x^2}{2}\right) + o(x^2)}{x^2} = \frac{3}{2}.$$

> [!esempio] Studio locale
> Per $f(x) = \cos x + \frac{x^2}{2}$, in 0 si ha $f'(0) = 0$ e $f''(0) = -1 + 1 = 0$. Lo sviluppo $f(x) = 1 + \frac{x^4}{24} + o(x^4)$ mostra che la prima derivata non nulla è la quarta, positiva: 0 è un punto di minimo stretto.

### Altri esercizi svolti

Gli esercizi riprendono la struttura delle prove: studio di funzione completo, numero di soluzioni di un'equazione, estremi globali, sviluppi e ordini di infinitesimo.

**Esercizio 1. Studio completo di $g(x) = x^2 \ln x$.**

*Dominio e segno.* $x > 0$. Il fattore $x^2$ è positivo, quindi $g$ ha il segno di $\ln x$: negativa su $(0, 1)$, nulla in 1, positiva dopo.

*Limiti.* Per $x \to 0^+$, $x^2 \ln x \to 0$ per la gerarchia (paragrafo 2.8): la funzione si può prolungare per continuità con $g(0) = 0$. Per $x \to +\infty$, $g \to +\infty$, e $\frac{g(x)}{x} = x \ln x \to +\infty$: niente asintoto obliquo.

*Derivata prima.* $g'(x) = 2x\ln x + x = x(2\ln x + 1)$. Si annulla per $\ln x = -\frac{1}{2}$, cioè $x = e^{-1/2} = \frac{1}{\sqrt{e}} \approx 0{,}61$. È negativa prima e positiva dopo: $g$ decresce su $\left(0, e^{-1/2}\right]$ e cresce su $\left[e^{-1/2}, +\infty\right)$. Il minimo vale $g\left(e^{-1/2}\right) = e^{-1} \cdot \left(-\frac{1}{2}\right) = -\frac{1}{2e} \approx -0{,}18$, ed è globale. Inoltre $g'(x) \to 0$ per $x \to 0^+$: il grafico parte dall'origine con tangente orizzontale.

*Derivata seconda.* $g''(x) = 2\ln x + 3$, nulla per $x = e^{-3/2} \approx 0{,}22$: $g$ è concava su $\left(0, e^{-3/2}\right]$ e convessa dopo. Il flesso è nel punto $\left(e^{-3/2}, -\frac{3}{2e^3}\right) \approx (0{,}22;\ -0{,}07)$.

*Immagine e numero di soluzioni.* L'immagine è $\left[-\frac{1}{2e}, +\infty\right)$. L'equazione $g(x) = k$ non ha soluzioni per $k < -\frac{1}{2e}$, ne ha una per $k = -\frac{1}{2e}$, due per $-\frac{1}{2e} < k < 0$ (una per tratto di monotonia), e una per $k \ge 0$ (per $k = 0$ è $x = 1$, perché lo 0 non è nel dominio).

**Esercizio 2. Estremi globali su un intervallo chiuso.** Trovare massimo e minimo di $f(x) = x e^{-x}$ su $[0, 3]$.

Per Weierstrass esistono. I candidati sono gli estremi dell'intervallo e i punti critici interni. $f'(x) = (1 - x)e^{-x}$ si annulla solo in 1. I valori sono $f(0) = 0$, $f(1) = e^{-1} \approx 0{,}37$, $f(3) = 3e^{-3} \approx 0{,}15$. Il massimo è $\frac{1}{e}$ in $x = 1$, il minimo 0 in $x = 0$. Il minimo cade in un estremo dell'intervallo, dove la derivata non è nulla ($f'(0) = 1$): il teorema di Fermat vale solo per i punti interni.

**Esercizio 3. Un minimo globale con una disuguaglianza.** Sia $f(x) = e^x - 1 - x + \sin^2 x$. Dire se 0 è un punto di minimo locale e se $f$ ha minimo globale.

$f(0) = 0$, $f'(x) = e^x - 1 + 2\sin x\cos x = e^x - 1 + \sin 2x$, quindi $f'(0) = 0$; $f''(x) = e^x + 2\cos 2x$, quindi $f''(0) = 3 > 0$: minimo locale stretto. Per il minimo globale non serve studiare tutta la funzione: per l'esercizio 6 del modulo 4, $e^x - 1 - x \ge 0$ per ogni $x$, e $\sin^2 x \ge 0$. Quindi $f(x) \ge 0 = f(0)$ ovunque: 0 è anche punto di minimo globale.

**Esercizio 4. Polinomio di McLaurin di una composta e ordine di un prodotto.** Sia $f(x) = \ln(1 + x) - \sqrt{1 + x}$. (a) Scrivere il polinomio di McLaurin di ordine 2 di $g(x) = f(x^2)$. (b) Trovare l'ordine di infinitesimo per $x \to 0$ di $h(x) = \big(g(x) + 1\big)(x - \sin x)$.

(a) Si sviluppa $f$ al primo ordine in $y$ e si pone $y = x^2$: $\ln(1 + y) = y + o(y)$, $\sqrt{1 + y} = 1 + \frac{y}{2} + o(y)$, quindi $f(y) = -1 + \frac{y}{2} + o(y)$ e
$$g(x) = -1 + \frac{x^2}{2} + o(x^2).$$
Il polinomio è $-1 + \frac{x^2}{2}$. Basta l'ordine 1 in $y$, perché $y^2 = x^4$ è già oltre l'ordine 2 in $x$.

(b) $g(x) + 1 = \frac{x^2}{2} + o(x^2) \sim \frac{x^2}{2}$ e $x - \sin x = \frac{x^3}{6} + o(x^3) \sim \frac{x^3}{6}$. Il prodotto è $\sim \frac{x^5}{12}$: ordine 5.

**Esercizio 5. Il polinomio che approssima meglio.** Trovare un polinomio $P$ di grado 2 tale che $f(x) - P(x)$, con $f(x) = x + \sqrt{x^2 + 4}$, sia un infinitesimo di ordine maggiore di 2 per $x \to 0$.

È il polinomio di McLaurin di ordine 2. $\sqrt{x^2 + 4} = 2\sqrt{1 + \frac{x^2}{4}} = 2\left(1 + \frac{x^2}{8} + o(x^2)\right) = 2 + \frac{x^2}{4} + o(x^2)$, quindi $P(x) = 2 + x + \frac{x^2}{4}$. Per l'unicità dello sviluppo è l'unico polinomio di grado al più 2 con questa proprietà.

**Esercizio 6. Un limite con due composizioni.** Calcolare $\displaystyle\lim_{x \to 0} \frac{\ln(1 + \sin x) - x}{1 - \cos x}$.

Il denominatore è $\frac{x^2}{2} + o(x^2)$: serve l'ordine 2. Con $t = \sin x = x + o(x^2)$ (il termine successivo è $-\frac{x^3}{6}$), $\ln(1 + t) = t - \frac{t^2}{2} + o(t^2) = x - \frac{x^2}{2} + o(x^2)$. Il numeratore è $-\frac{x^2}{2} + o(x^2)$ e il limite è $-1$.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Studio di $f(x) = x\,e^{1/x}$.**

*Passo 1: dominio, segno, simmetrie.* $x \ne 0$. L'esponenziale è positivo, quindi $f$ ha il segno di $x$. Non è né pari né dispari.

*Passo 2: limiti in 0.* Per $x \to 0^+$, con $y = \frac{1}{x} \to +\infty$: $f = \frac{e^y}{y} \to +\infty$, asintoto verticale da destra. Per $x \to 0^-$, $\frac{1}{x} \to -\infty$ ed $e^{1/x} \to 0$: $f \to 0 \cdot 0 = 0$. Da sinistra il grafico arriva nell'origine (che non fa parte del grafico).

*Passo 3: limiti all'infinito e asintoti obliqui.* $f \to \pm\infty$ per $x \to \pm\infty$. $m = \lim \frac{f(x)}{x} = \lim e^{1/x} = 1$; $q = \lim \big(f(x) - x\big) = \lim x\left(e^{1/x} - 1\right) = \lim_{y \to 0} \frac{e^y - 1}{y} = 1$. Asintoto $y = x + 1$ da entrambe le parti.

*Passo 4: derivata prima.* $f'(x) = e^{1/x} + x e^{1/x}\left(-\frac{1}{x^2}\right) = e^{1/x}\,\frac{x - 1}{x}$. Il segno è quello di $\frac{x - 1}{x}$: positivo per $x < 0$ e per $x > 1$, negativo su $(0, 1)$. $f$ cresce su $(-\infty, 0)$, decresce su $(0, 1]$, cresce su $[1, +\infty)$. In 1 c'è un minimo locale, $f(1) = e$, che non è globale perché $f \to -\infty$ a $-\infty$. Per $x \to 0^-$, $f'(x) \to 0$: il grafico arriva nell'origine con tangente orizzontale.

*Passo 5: derivata seconda.* Derivando $e^{1/x}\left(1 - \frac{1}{x}\right)$ si ottiene $f''(x) = \frac{e^{1/x}}{x^3}$: convessa per $x > 0$, concava per $x < 0$. Non ci sono flessi, perché il cambio di concavità avviene in un punto fuori dal dominio.

*Passo 6: immagine e numero di soluzioni.* Il ramo sinistro copre $(-\infty, 0)$, il ramo destro $[e, +\infty)$. L'equazione $f(x) = k$ ha una soluzione per $k < 0$, nessuna per $0 \le k < e$, una per $k = e$, due per $k > e$ (una in $(0, 1)$ e una in $(1, +\infty)$).

**Guidato 2. Ordine di infinitesimo con un parametro.** Per quali $a \in \mathbb{R}$ l'infinitesimo $f(x) = \sin x - x\cos(ax)$ ha ordine maggiore di 3 per $x \to 0$? Qual è allora l'ordine?

*Passo 1: sviluppare all'ordine 3.* $\sin x = x - \frac{x^3}{6} + o(x^3)$ e $x\cos(ax) = x\left(1 - \frac{a^2x^2}{2} + o(x^2)\right) = x - \frac{a^2}{2}x^3 + o(x^3)$.

*Passo 2: la differenza.* $f(x) = \left(\frac{a^2}{2} - \frac{1}{6}\right)x^3 + o(x^3)$. Se il coefficiente non è nullo l'ordine è 3.

*Passo 3: annullare il coefficiente.* $\frac{a^2}{2} = \frac{1}{6}$ per $a^2 = \frac{1}{3}$, cioè $a = \pm\frac{1}{\sqrt{3}}$.

*Passo 4: andare all'ordine 5.* Con $a^2 = \frac{1}{3}$ i termini di grado 3 si cancellano e serve l'ordine successivo. $\sin x$ ha il termine $\frac{x^5}{120}$, $x\cos(ax)$ ha $x \cdot \frac{a^4 x^4}{24} = \frac{x^5}{9 \cdot 24} = \frac{x^5}{216}$. Quindi $f(x) = \left(\frac{1}{120} - \frac{1}{216}\right)x^5 + o(x^5) = \frac{x^5}{270} + o(x^5)$: ordine 5.

### Una prova d'esame simulata

Si consideri, al variare di $a \in \mathbb{R}$, la funzione $f_a(x) = \ln(1 + x)$ per $-1 < x \le 0$ e $f_a(x) = x - ax^2$ per $x > 0$.

(a) Studiare continuità e derivabilità di $f_a$ in 0; per quali $a$ esiste anche $f_a''(0)$? [5 punti]
(b) Con $a = 1$, tracciare il grafico di $f_1$, con limiti, asintoti, monotonia, estremi e concavità. [8 punti]
(c) Trovare maggioranti, minoranti, sup, inf, massimo e minimo di $A = \left\{(-1)^n\frac{n}{n + 1} : n \ge 1\right\}$. [5 punti]
(d) Calcolare $\displaystyle\lim_{x \to 0} \frac{\ln(1 + \sin x) - x}{1 - \cos x}$. [4 punti]

*Soluzione (a).* I due tratti valgono 0 in 0: continua per ogni $a$. Le derivate sono $\frac{1}{1 + x} \to 1$ da sinistra e $1 - 2ax \to 1$ da destra: derivabile per ogni $a$, con $f_a'(0) = 1$. Le derivate seconde sono $-\frac{1}{(1 + x)^2} \to -1$ e $-2a$: per il teorema del limite della derivata applicato a $f'$, esiste $f_a''(0)$ se e solo se $a = \frac{1}{2}$.

*Soluzione (b).* Il dominio è $(-1, +\infty)$. Per $x \to -1^+$, $\ln(1 + x) \to -\infty$: asintoto verticale $x = -1$. Per $x \to +\infty$, $x - x^2 \to -\infty$, e $\frac{f(x)}{x} = 1 - x \to -\infty$: niente asintoto obliquo. Sul tratto sinistro $f$ è crescente; su quello destro $f' = 1 - 2x$ è positiva fino a $\frac{1}{2}$ e negativa dopo. Poiché $f$ è derivabile in 0 con $f'(0) = 1 > 0$, è crescente su $\left(-1, \frac{1}{2}\right]$ e decrescente dopo: il massimo globale è $f\left(\frac{1}{2}\right) = \frac{1}{4}$, e non c'è minimo. Zeri: $x = 0$ e $x = 1$. Concavità: $f'' < 0$ su entrambi i tratti, e $f'$ è decrescente su tutto il dominio (in 0 vale 1 da entrambe le parti), quindi $f$ è concava su $(-1, +\infty)$.

*Soluzione (c).* Per $n$ pari i termini sono $\frac{n}{n + 1} = 1 - \frac{1}{n + 1}$, crescenti verso 1; per $n$ dispari sono $-\frac{n}{n + 1}$, decrescenti verso $-1$. Tutti stanno in $(-1, 1)$ e si avvicinano quanto si vuole a entrambi gli estremi: $\sup A = 1$, $\inf A = -1$, senza massimo né minimo. I maggioranti sono $[1, +\infty)$, i minoranti $(-\infty, -1]$.

*Soluzione (d).* È l'esercizio 6: il limite vale $-1$.

## Riepilogo

Su un intervallo, $f' \ge 0$ equivale a $f$ crescente, e $f' > 0$ implica la crescenza stretta (non il viceversa: $x^3$). Gli estremi si cercano fra punti critici, punti di non derivabilità ed estremi del dominio, e si classificano con il segno di $f'$. Su un intervallo $f$ è convessa se e solo se $f'$ è crescente, e se è derivabile due volte se e solo se $f'' \ge 0$; nei flessi $f''$ si annulla e, se cambia segno, il flesso c'è. Lo studio di funzione mette insieme dominio, limiti e asintoti, segno di $f'$ e di $f''$.

La formula di Taylor approssima $f$ con il polinomio $T_{n,x_0} f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$: con il resto di Peano l'errore è $o\big((x - x_0)^n\big)$, con il resto di Lagrange vale $\frac{f^{(n+1)}(\bar{x})}{(n+1)!}(x - x_0)^{n+1}$. Gli sviluppi da sapere, per $x \to 0$, sono
$$e^x = \sum_{k=0}^{n} \frac{x^k}{k!} + o(x^n), \quad \ln(1 + x) = \sum_{k=1}^{n} \frac{(-1)^{k-1}}{k} x^k + o(x^n), \quad \sin x = \sum_{k=0}^{n} \frac{(-1)^k x^{2k+1}}{(2k+1)!} + o(x^{2n+2}),$$
$$\cos x = \sum_{k=0}^{n} \frac{(-1)^k x^{2k}}{(2k)!} + o(x^{2n+1}), \quad (1 + x)^\alpha = \sum_{k=0}^{n} \binom{\alpha}{k} x^k + o(x^n).$$
Per l'unicità del polinomio di Taylor, gli sviluppi di somme, prodotti, quozienti e composte si ottengono con l'algebra, troncando al grado voluto, e servono per calcolare limiti, ordini di infinitesimo e la natura dei punti critici.

## Formulario

Criteri, procedura dello studio di funzione, sviluppi e termini per l'orale.

### Monotonia, estremi, convessità

| Condizione su un intervallo | Conclusione |
|---|---|
| $f' > 0$ ($f' < 0$) | $f$ strettamente crescente (decrescente) |
| $f' = 0$ | $f$ costante |
| $f'(x_0) = 0$, $f'' (x_0) > 0$ | minimo locale stretto |
| $f'(x_0) = 0$, $f''(x_0) < 0$ | massimo locale stretto |
| prima derivata non nulla in $x_0$ di ordine $n$ | $n$ pari: estremo (minimo se positiva); $n$ dispari: flesso |
| $f'' \ge 0$ | $f$ convessa: grafico sopra le tangenti, $f' $ crescente |
| $f''$ cambia segno in $x_0$ | flesso in $x_0$ |

Estremi globali su $[a, b]$: si confrontano i valori agli estremi, nei punti critici interni e nei punti di non derivabilità.

### Studio di funzione: i passi

1. Dominio, simmetrie (pari, dispari, periodica), segno e intersezioni con gli assi.
2. Limiti agli estremi del dominio e asintoti (verticali, orizzontali, obliqui).
3. Continuità e derivabilità; punti angolosi, cuspidi, prolungamenti.
4. Derivata prima: monotonia, estremi locali e globali.
5. Derivata seconda: convessità e flessi (quando richiesto).
6. Grafico, immagine, numero di soluzioni di $f(x) = k$.

### Taylor

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + o\big((x - x_0)^n\big) \quad \text{(Peano)}, \qquad R_n(x) = \frac{f^{(n+1)}(\xi)}{(n + 1)!}(x - x_0)^{n+1} \quad \text{(Lagrange)}.$$

| Funzione ($x \to 0$) | Sviluppo |
|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \dots + \frac{x^n}{n!} + o(x^n)$ |
| $\ln(1 + x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$ |
| $\sin x$ | $x - \frac{x^3}{6} + \frac{x^5}{120} - \dots + o(x^{2n})$ |
| $\cos x$ | $1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots + o(x^{2n+1})$ |
| $(1 + x)^\alpha$ | $1 + \alpha x + \binom{\alpha}{2}x^2 + \dots + o(x^n)$; $\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + o(x^2)$ |
| $\frac{1}{1 - x}$ | $1 + x + x^2 + \dots + x^n + o(x^n)$ |
| $\arctan x$ | $x - \frac{x^3}{3} + \frac{x^5}{5} - \dots + o(x^{2n+2})$ |
| $\tan x$ | $x + \frac{x^3}{3} + o(x^4)$ |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Punto critico | $f'(x_0) = 0$ |
| Estremo locale / globale | massimo o minimo in un intorno / su tutto il dominio |
| Funzione convessa | il segmento fra due punti del grafico sta sopra il grafico |
| Flesso | punto in cui cambia la concavità, con retta tangente |
| Polinomio di Taylor | il polinomio di grado $n$ che ha in $x_0$ le stesse derivate di $f$ fino all'ordine $n$ |
| Polinomio di McLaurin | polinomio di Taylor in $x_0 = 0$ |
| Resto di Peano / di Lagrange | $o((x - x_0)^n)$ / espressione con $f^{(n+1)}(\xi)$ |
| Unicità dello sviluppo | un solo polinomio di grado $n$ approssima $f$ a meno di $o((x - x_0)^n)$ |

### Domande che tornano spesso

- Dimostrare con Lagrange il legame fra segno della derivata e monotonia.
- Condizioni necessarie e sufficienti per un estremo; perché $f'(x_0) = 0$ non basta ($x^3$)?
- Definire la convessità; legame con la derivata seconda e con le tangenti.
- Enunciare la formula di Taylor con i due resti; ricavare lo sviluppo di $e^x$ o di $\sin x$.
- Come si usano gli sviluppi per calcolare un limite e per decidere la natura di un punto critico?
- Descrivere i passi dello studio di funzione.
