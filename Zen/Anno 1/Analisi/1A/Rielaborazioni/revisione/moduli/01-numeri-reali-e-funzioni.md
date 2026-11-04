---
corso: Analisi Matematica 1A
modulo: 1
titolo: Numeri reali e funzioni
programma: [AM1A-01, AM1A-02, AM1A-03, AM1A-04, AM1A-05, AM1A-06, AM1A-07, AM1A-18]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-03
---

# 1 · Numeri reali e funzioni

**In questo modulo.** Non servono prerequisiti oltre all'algebra delle superiori. Si costruisce il linguaggio su cui poggia tutto il corso: gli insiemi numerici e le proprietà che distinguono $\mathbb{R}$ da $\mathbb{Q}$, in particolare la completezza; il valore assoluto e gli intervalli; estremo superiore e inferiore. Poi si passa alle funzioni: dominio, immagine, grafico, iniettività, inversa, composizione e monotonia, e alle funzioni elementari con i loro grafici. Alla fine del modulo si sanno leggere e scrivere con precisione definizioni ed enunciati, si riconoscono le proprietà di una funzione dal suo grafico e si determinano dominio e immagine delle funzioni elementari e delle loro composizioni.

## 1.1 Insiemi numerici

I **numeri naturali** sono $\mathbb{N} = \{0, 1, 2, 3, \dots\}$; con $\mathbb{N}_0 = \mathbb{N} \setminus \{0\}$ si indicano i naturali positivi. In $\mathbb{N}$ la somma e il prodotto di due elementi restano in $\mathbb{N}$, la differenza no: $2 - 5$ non è un numero naturale. Per poter sempre sottrarre si passa ai **numeri interi** $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$, nei quali però non si può sempre dividere.

I **numeri razionali** sono le frazioni $\frac{n}{m}$ con $n \in \mathbb{Z}$ e $m \in \mathbb{N}_0$, dove due frazioni rappresentano lo stesso numero quando $\frac{n}{m} = \frac{n'}{m'} \iff n m' = n' m$. In $\mathbb{Q}$ si può dividere per ogni numero diverso da zero.

Ogni razionale ha una scrittura decimale

$$q = c_k c_{k-1} \dots c_1 c_0 , d_1 d_2 d_3 \dots = c_k \cdot 10^k + \dots + c_1 \cdot 10 + c_0 + \frac{d_1}{10} + \frac{d_2}{10^2} + \dots$$

e si presentano solo due casi: la sequenza delle cifre decimali termina, come in $0{,}15 = \frac{15}{100} = \frac{3}{20}$, oppure non termina ma da un certo punto in poi si ripete con un periodo, come in $0{,}\overline{3} = \frac{1}{3}$. Viceversa, ogni scrittura decimale finita o periodica rappresenta un razionale.

> [!nota]
> La scrittura decimale non è sempre unica: $0{,}\overline{9} = 1$. Infatti, posto $x = 0{,}\overline{9}$, si ha $10x - x = 9{,}\overline{9} - 0{,}\overline{9} = 9$, quindi $x = 1$.

Le scritture decimali infinite e non periodiche corrispondono ai **numeri irrazionali**, come $\sqrt{2}$ o $\pi$ (il rapporto fra la lunghezza di una circonferenza e il suo diametro). Razionali e irrazionali insieme formano i **numeri reali** $\mathbb{R}$. In $\mathbb{R}$ un'equazione come $x^2 = 2$ ha esattamente due soluzioni, $x = \sqrt{2}$ e $x = -\sqrt{2}$, mentre in $\mathbb{Q}$ non ne ha nessuna.

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 1*, cap. 1 (AM1A-01)
> **$\sqrt{2}$ non è razionale.** Se fosse $\sqrt{2} = \frac{n}{m}$ con la frazione ridotta ai minimi termini, si avrebbe $n^2 = 2m^2$: allora $n^2$ è pari, quindi anche $n$ è pari, $n = 2h$. Sostituendo, $4h^2 = 2m^2$, cioè $m^2 = 2h^2$, e anche $m$ è pari. Ma $n$ e $m$ non possono essere entrambi pari in una frazione ridotta: l'ipotesi è assurda.
>
> **La retta orientata.** Fissati su una retta un punto $O$, un verso di percorrenza e un'unità di misura, a ogni numero reale $x$ corrisponde uno e un solo punto, a distanza $|x|$ da $O$, dalla parte positiva se $x > 0$ e da quella negativa se $x < 0$; e viceversa ogni punto corrisponde a un reale. Per questo si parla indifferentemente di "numeri" e di "punti" della retta reale. I razionali non bastano a riempirla: il punto a distanza $\sqrt{2}$ da $O$ non corrisponde a nessun razionale. Eppure i razionali sono **densi**: fra due reali distinti $a < b$ c'è sempre un razionale, e quindi infiniti.

I numeri reali hanno tre gruppi di proprietà. Le **proprietà algebriche** sono quelle di somma e prodotto, con sottrazione e divisione per numeri non nulli. L'**ordinamento** è **totale**: dati due reali $x$ e $y$ vale sempre $x \le y$ oppure $y \le x$, e l'ordine è compatibile con le operazioni (se $x \le y$ allora $x + z \le y + z$ e, per $z > 0$, $xz \le yz$). La terza è la **completezza**, che distingue $\mathbb{R}$ da $\mathbb{Q}$ e si vede nel paragrafo 1.3.

## 1.2 Valore assoluto e intervalli

> [!definizione] Valore assoluto
> Dato $x \in \mathbb{R}$, il suo **valore assoluto** (o modulo) è
> $$|x| = \begin{cases} x & \text{se } x \ge 0 \\ -x & \text{se } x < 0. \end{cases}$$

Sulla retta orientata $|x|$ è la distanza di $x$ dall'origine, e $|x - y|$ la distanza fra $x$ e $y$. Per ogni $x, y \in \mathbb{R}$ valgono $|xy| = |x|\,|y|$ e la **disuguaglianza triangolare**

$$|x + y| \le |x| + |y|.$$

Da questa segue una disuguaglianza che si usa spesso nelle stime:

$$\big|\, |x| - |y| \,\big| \le |x - y|.$$

Per dimostrarla si scrive $x = (x - y) + y$ e si applica la disuguaglianza triangolare: $|x| \le |x - y| + |y|$, cioè $|x| - |y| \le |x - y|$. Scambiando i ruoli, $|y| = |(y - x) + x| \le |y - x| + |x|$; poiché $|y - x| = |x - y|$, si ottiene $|y| - |x| \le |x - y|$, ossia $-|x - y| \le |x| - |y|$. Le due stime insieme dicono che $|x| - |y|$ sta fra $-|x - y|$ e $|x - y|$, che è la tesi.

> [!definizione] Intervalli
> Dati $a, b \in \mathbb{R}$ con $a < b$:
>
> - intervallo **chiuso** $[a, b] := \{x \in \mathbb{R} : a \le x \le b\}$;
> - intervallo **aperto** $(a, b) := \{x \in \mathbb{R} : a < x < b\}$;
> - intervalli **semiaperti** $[a, b) := \{x : a \le x < b\}$ e $(a, b] := \{x : a < x \le b\}$;
> - intervalli **illimitati** $[a, +\infty) := \{x : x \ge a\}$, $(a, +\infty)$, $(-\infty, b]$, $(-\infty, b)$, e $(-\infty, +\infty) = \mathbb{R}$.

I simboli $+\infty$ e $-\infty$ non sono numeri reali: servono solo a scrivere in breve gli intervalli illimitati, e per questo dalla loro parte la parentesi è sempre tonda.

## 1.3 Estremo superiore e inferiore

> [!definizione] Maggioranti, minoranti, insiemi limitati
> Sia $A \subseteq \mathbb{R}$ non vuoto. Un numero $b \in \mathbb{R}$ è un **maggiorante** di $A$ se $x \le b$ per ogni $x \in A$; un numero $a \in \mathbb{R}$ è un **minorante** di $A$ se $a \le x$ per ogni $x \in A$. L'insieme $A$ è **limitato superiormente** se ha almeno un maggiorante, **limitato inferiormente** se ha almeno un minorante, **limitato** se è entrambe le cose.

> [!definizione] Massimo e minimo
> Un numero $x_0$ è il **massimo** di $A$, e si scrive $x_0 = \max A$, se $x_0 \in A$ e $x \le x_0$ per ogni $x \in A$: è un maggiorante che appartiene ad $A$. Analogamente il **minimo** $\min A$ è un minorante che appartiene ad $A$.

Un insieme limitato può non avere massimo: $A = [0, 1)$ ha come maggioranti tutti i numeri $\ge 1$, ma nessuno di essi sta in $A$. Il numero 1 resta comunque speciale: è il più piccolo dei maggioranti.

> [!definizione] Estremo superiore e inferiore
> Sia $A \subseteq \mathbb{R}$ non vuoto e limitato superiormente. L'**estremo superiore** di $A$ è il più piccolo dei suoi maggioranti:
> $$\sup A := \min\{b \in \mathbb{R} : b \text{ è maggiorante di } A\}.$$
> Se $A$ è limitato inferiormente, l'**estremo inferiore** è il più grande dei minoranti: $\inf A := \max\{a \in \mathbb{R} : a \text{ è minorante di } A\}$. Se $A$ non è limitato superiormente (inferiormente) si pone $\sup A = +\infty$ ($\inf A = -\infty$).

Quando il massimo esiste coincide con l'estremo superiore. Nella pratica si usa quasi sempre la caratterizzazione seguente.

> [!teorema] Caratterizzazione dell'estremo superiore
> Sia $A \subseteq \mathbb{R}$ non vuoto e limitato superiormente. Un numero $S \in \mathbb{R}$ è l'estremo superiore di $A$ se e solo se
>
> 1. $x \le S$ per ogni $x \in A$, cioè $S$ è un maggiorante;
> 2. per ogni $\varepsilon > 0$ esiste $x \in A$ con $x > S - \varepsilon$, cioè nessun numero più piccolo di $S$ è un maggiorante.

La seconda condizione è la traduzione di "è il più piccolo dei maggioranti": se $z < S$, allora $z$ non è un maggiorante, quindi esiste $x \in A$ con $x > z$. Basta prendere $z = S - \varepsilon$.

L'esistenza dell'estremo superiore non è un fatto ovvio, ed è proprio ciò che rende $\mathbb{R}$ diverso da $\mathbb{Q}$.

> [!teorema] Assioma di completezza
> Ogni sottoinsieme di $\mathbb{R}$ non vuoto e limitato superiormente ammette estremo superiore in $\mathbb{R}$. (Allo stesso modo, ogni sottoinsieme non vuoto e limitato inferiormente ammette estremo inferiore.)

> [!esempio] La completezza e $\sqrt{2}$
> L'insieme $A = \{q \in \mathbb{Q} : q > 0,\ q^2 < 2\}$ è non vuoto (contiene 1) e limitato superiormente (2 è un maggiorante, perché se $q \ge 2$ allora $q^2 \ge 4$). In $\mathbb{R}$ il suo estremo superiore esiste e vale $\sqrt{2}$. In $\mathbb{Q}$, invece, $A$ non ha estremo superiore: per ogni razionale positivo $r$ con $r^2 < 2$ si trova un razionale di $A$ più grande, e per ogni $r$ con $r^2 > 2$ si trova un maggiorante razionale più piccolo, mentre $r^2 = 2$ è impossibile. È così che la completezza "riempie i buchi" della retta razionale.

> [!esempio]
> Per $A = \left\{1 - \frac{1}{n} : n \in \mathbb{N}_0\right\} = \left\{0, \frac{1}{2}, \frac{2}{3}, \dots\right\}$ si ha $\min A = \inf A = 0$ e $\sup A = 1$, ma 1 non è un massimo, perché $1 - \frac{1}{n} < 1$ per ogni $n$. La condizione 2 della caratterizzazione si verifica così: dato $\varepsilon > 0$, basta scegliere $n > \frac{1}{\varepsilon}$ per avere $1 - \frac{1}{n} > 1 - \varepsilon$.

## 1.4 Induzione e coefficienti binomiali

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 1*, cap. 1 (AM1A-18)
> **Principio di induzione.** Sia $P(n)$ un'affermazione che dipende da $n \in \mathbb{N}$. Se $P(n_0)$ è vera (*passo base*) e, per ogni $n \ge n_0$, dalla verità di $P(n)$ segue quella di $P(n + 1)$ (*passo induttivo*), allora $P(n)$ è vera per ogni $n \ge n_0$.
>
> Ad esempio, la **disuguaglianza di Bernoulli** $(1 + x)^n \ge 1 + nx$, per $x \ge -1$ e $n \in \mathbb{N}$, si dimostra così. Per $n = 0$ si ha $1 \ge 1$. Se vale per $n$, moltiplicando per $1 + x \ge 0$ si ottiene $(1 + x)^{n+1} \ge (1 + nx)(1 + x) = 1 + (n + 1)x + nx^2 \ge 1 + (n + 1)x$, che è la tesi per $n + 1$. La disuguaglianza servirà nel modulo 2 per il numero $e$.

Il **fattoriale** di $n \in \mathbb{N}$ è $n! = 1 \cdot 2 \cdots n$, con la convenzione $0! = 1$. Per $0 \le k \le n$ il **coefficiente binomiale** è

$$\binom{n}{k} = \frac{n!}{k!\,(n - k)!}$$

e conta i modi di scegliere $k$ oggetti fra $n$. Dalla definizione segue subito la simmetria $\binom{n}{k} = \binom{n}{n - k}$, perché scambiare $k$ e $n - k$ lascia invariato il denominatore.

> [!teorema] Formula di Stifel
> Per $1 \le k \le n - 1$ vale $\displaystyle \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

*Dimostrazione.* Si sommano le due frazioni mettendo in evidenza il fattore comune $\frac{(n-1)!}{(k-1)!\,(n-k-1)!}$:

$$\frac{(n-1)!}{(k-1)!\,(n-k)!} + \frac{(n-1)!}{k!\,(n-k-1)!} = \frac{(n-1)!}{(k-1)!\,(n-k-1)!} \left(\frac{1}{n-k} + \frac{1}{k}\right) = \frac{(n-1)!}{(k-1)!\,(n-k-1)!} \cdot \frac{n}{k\,(n-k)} = \frac{n!}{k!\,(n-k)!}.$$

La formula è la regola con cui si costruisce il triangolo di Tartaglia, e con essa si dimostra per induzione lo **sviluppo del binomio**

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k.$$

## 1.5 Funzioni

> [!definizione] Funzione
> Dati due insiemi $X$ e $Y$, una **funzione** $f : X \to Y$ è una legge che associa a ogni elemento $x \in X$ uno e un solo elemento $f(x) \in Y$. L'insieme $X$ è il **dominio**, $Y$ il **codominio**; si scrive anche $x \mapsto f(x)$.

In analisi capita spesso di assegnare solo un'espressione, come $f(x) = \sqrt{x - 1}$, senza dire su quali $x$ ha senso. Si parla allora di funzione **definita in** $X$: una legge che a ogni $x \in X$ associa *al più* un elemento di $Y$. L'insieme degli $x$ a cui associa effettivamente un valore è il suo dominio, $\operatorname{dom}(f) \subseteq X$, e si scrive $f : \operatorname{dom}(f) \subseteq X \to Y$. Determinare il dominio significa trovare il più grande insieme su cui l'espressione ha senso.

> [!definizione] Immagine, controimmagine, grafico
> Sia $f : X \to Y$.
>
> - L'**immagine** di $f$ è $\operatorname{im}(f) := \{y \in Y : \exists\, x \in X \text{ con } f(x) = y\}$; più in generale, per $A \subseteq X$, l'immagine di $A$ è $f(A) := \{f(x) : x \in A\}$.
> - Per $B \subseteq Y$, la **controimmagine** di $B$ è $f^{-1}(B) := \{x \in X : f(x) \in B\}$; per un solo punto si scrive $f^{-1}(y)$ invece di $f^{-1}(\{y\})$.
> - Il **grafico** di $f$ è $\Gamma(f) := \{(x, f(x)) : x \in X\} \subseteq X \times Y$.

> [!attenzione]
> Il simbolo $f^{-1}(B)$ indica la controimmagine e ha senso per ogni funzione. La funzione inversa $f^{-1}$ del paragrafo 1.6 esiste solo per le funzioni iniettive. Quando l'inversa esiste, i due significati sono compatibili.

Dalla definizione seguono due relazioni utili: $A \subseteq f^{-1}(f(A))$, con l'uguaglianza se $f$ è iniettiva, e $f(f^{-1}(B)) = B \cap \operatorname{im}(f)$.

> [!esempio] Una funzione fra insiemi finiti
> Sia $f : \{1, 2, 3, 5\} \to \{a, b, c, d, \dots\}$ definita da $1 \mapsto b$, $2 \mapsto c$, $3 \mapsto d$, $5 \mapsto b$. Allora $\operatorname{im}(f) = \{b, c, d\}$ e $\Gamma(f) = \{(1, b), (2, c), (3, d), (5, b)\}$. La controimmagine di $b$ è $f^{-1}(b) = \{1, 5\}$, quella di $a$ è vuota.

![Figura 1.1](../figure/1-1.svg)

*Figura 1.1. Diagramma a frecce fra $\{1, 2, 3, 5\}$ e l'alfabeto per l'esempio precedente.*

> [!esempio] Il valore assoluto e il quadrato
> Per $f : \mathbb{R} \to \mathbb{R}$, $f(x) = |x|$, si ha $\operatorname{im}(f) = [0, +\infty)$ e $\Gamma(f) = \{(x, |x|) : x \in \mathbb{R}\}$: il grafico è formato dalle bisettrici del primo e del secondo quadrante.
>
> Per $g(x) = x^2$ si calcolano immagini e controimmagini di alcuni intervalli. Poiché $x^2$ è crescente per $x \ge 0$: $g((0, 1)) = (0, 1)$, $g([0, 1)) = [0, 1)$, $g([0, 1]) = [0, 1]$. Per le controimmagini bisogna considerare anche le $x$ negative: $g^{-1}((0, 1)) = (-1, 0) \cup (0, 1)$, $g^{-1}([0, 1)) = (-1, 1)$, $g^{-1}([0, 1]) = [-1, 1]$, e $g^{-1}((1, +\infty)) = (-\infty, -1) \cup (1, +\infty)$.

![Figura 1.2](../figure/1-2.svg)

*Figura 1.2. Parabola $y = x^2$ con evidenziati l'intervallo $(0, 1)$ sull'asse $y$ e la sua controimmagine $(-1, 0) \cup (0, 1)$ sull'asse $x$.*

## 1.6 Iniettività, inversa, restrizione e composizione

> [!definizione] Iniettiva, suriettiva, biettiva
> Una funzione $f : X \to Y$ è
>
> - **iniettiva** se ogni $y \in Y$ ha al più una controimmagine, cioè se $x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$ (equivalentemente, $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$);
> - **suriettiva** se ogni $y \in Y$ ha almeno una controimmagine, cioè se $\operatorname{im}(f) = Y$;
> - **biettiva** se è iniettiva e suriettiva.

Sul grafico, l'iniettività si riconosce perché ogni retta orizzontale lo interseca al più una volta, la suriettività perché ogni retta orizzontale di quota $y \in Y$ lo interseca almeno una volta.

> [!definizione] Funzione inversa
> Sia $f : X \to Y$ iniettiva. La sua **inversa** è la funzione $f^{-1} : \operatorname{im}(f) \to X$ che a ogni $y \in \operatorname{im}(f)$ associa l'unico $x \in X$ tale che $f(x) = y$. Se $f$ è biettiva, $f^{-1}$ è definita su tutto $Y$.

Per costruzione $f(f^{-1}(y)) = y$ per ogni $y \in \operatorname{im}(f)$ e $f^{-1}(f(x)) = x$ per ogni $x \in X$. Il grafico di $f^{-1}$ si ottiene da quello di $f$ per simmetria rispetto alla bisettrice $y = x$, perché $(x, y) \in \Gamma(f)$ se e solo se $(y, x) \in \Gamma(f^{-1})$.

> [!definizione] Restrizione
> Data $f : X \to Y$ e $A \subseteq X$, la **restrizione** di $f$ ad $A$ è la funzione $f|_A : A \to Y$ definita da $f|_A(x) := f(x)$.

Restringere il dominio è il modo standard per rendere invertibile una funzione che non è iniettiva.

> [!esempio] Quando $x^2$ è invertibile
> $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$, non è iniettiva ($f(-1) = f(1)$) né suriettiva (i negativi non sono immagini). Le restrizioni $f|_{(-\infty, 0]}$ e $f|_{[0, +\infty)}$ sono iniettive ma, con codominio $\mathbb{R}$, ancora non suriettive. La funzione $g : [0, +\infty) \to [0, +\infty)$, $g(x) = x^2$, è biettiva, e la sua inversa è la radice quadrata $g^{-1}(y) = \sqrt{y}$.

> [!definizione] Composizione
> Date $f : X \to Y$ e $g : Y \to Z$, la **composizione** $g \circ f : X \to Z$ è $(g \circ f)(x) := g(f(x))$. Se $f$ e $g$ sono definite solo su parte dei rispettivi insiemi, il dominio della composta è
> $$\operatorname{dom}(g \circ f) = \{x \in \operatorname{dom}(f) : f(x) \in \operatorname{dom}(g)\} = f^{-1}(\operatorname{dom}(g)).$$

Ad esempio, per $h(x) = \sqrt{x - 1}$ si ha $h = g \circ f$ con $f(x) = x - 1$ e $g(y) = \sqrt{y}$: il dominio è $\{x : x - 1 \ge 0\} = [1, +\infty)$. In generale $g \circ f \ne f \circ g$: con le stesse funzioni, $(f \circ g)(y) = \sqrt{y} - 1$.

## 1.7 Funzioni monotone

> [!definizione] Funzioni monotone
> Sia $f : \operatorname{dom}(f) \subseteq \mathbb{R} \to \mathbb{R}$. La funzione è
>
> - **crescente** se $x_1 < x_2 \Rightarrow f(x_1) \le f(x_2)$ per ogni $x_1, x_2 \in \operatorname{dom}(f)$;
> - **strettamente crescente** se $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$;
> - **decrescente** e **strettamente decrescente** se valgono le disuguaglianze opposte, $f(x_1) \ge f(x_2)$ e $f(x_1) > f(x_2)$.
>
> Si dice **monotona** una funzione crescente o decrescente.

"Crescente" qui significa "non decrescente": una funzione costante è contemporaneamente crescente e decrescente. Altri testi dicono "crescente" solo per il caso stretto; in questi appunti si usa sempre "strettamente" quando la disuguaglianza è stretta.

![Figura 1.3](../figure/1-3.svg)

*Figura 1.3. Quattro grafici: una funzione non monotona, una costante (crescente e decrescente), una strettamente crescente, una strettamente decrescente.*

> [!teorema] Monotonia stretta e iniettività
> Una funzione strettamente monotona è iniettiva.

Infatti, se $x_1 \ne x_2$, ad esempio $x_1 < x_2$, la monotonia stretta dà $f(x_1) < f(x_2)$ oppure $f(x_1) > f(x_2)$, comunque $f(x_1) \ne f(x_2)$. Il viceversa è falso.

> [!esempio] Iniettiva ma non monotona
> Sia $f(x) = \frac{1}{x}$ per $x \ne 0$ e $f(0) = 0$. Su $(-\infty, 0)$ e su $(0, +\infty)$ la funzione è strettamente decrescente, ma globalmente non è monotona: $-1 < 1$ e $f(-1) = -1 < 1 = f(1)$, mentre $1 < 2$ e $f(1) > f(2)$. Eppure è iniettiva: valori diversi da 0 vengono da un solo punto, e il valore 0 solo da $x = 0$.

## 1.8 Funzioni elementari

### Potenze

La funzione potenza $x \mapsto x^\alpha$ si definisce per gradi, ampliando l'esponente.

- **Esponente nullo.** Per convenzione $x^0 = 1$ per ogni $x$.
- **Esponente $n \in \mathbb{N}_0$.** $x^n = x \cdot x \cdots x$ ($n$ fattori), definita su $\mathbb{R}$. Se $n$ è pari la funzione è pari ($(-x)^n = x^n$), strettamente decrescente su $(-\infty, 0]$ e strettamente crescente su $[0, +\infty)$; se $n$ è dispari è dispari ($(-x)^n = -x^n$) e strettamente crescente su $\mathbb{R}$.
- **Esponente $\frac{1}{n}$, $n \in \mathbb{N}_0$.** La radice $n$-esima $\sqrt[n]{x} = x^{1/n}$ è l'inversa della potenza $n$-esima: per $n$ pari l'inversa di $x^n|_{[0, +\infty)}$, quindi definita su $[0, +\infty)$; per $n$ dispari l'inversa di $x^n$ su tutto $\mathbb{R}$.
- **Esponente razionale $\frac{m}{n}$**, con $m, n \in \mathbb{N}_0$ senza fattori comuni: $x^{m/n} = \sqrt[n]{x^m}$, composizione di potenza e radice. Per semplicità la si considera su $[0, +\infty)$.
- **Esponente reale $\alpha > 0$ irrazionale.** Si usa la completezza. Per $x \ge 1$ la potenza $x^q$ cresce con l'esponente razionale $q$, e si pone $x^\alpha := \sup\{x^q : q \in \mathbb{Q},\ 0 < q \le \alpha\}$; per $0 \le x < 1$ la potenza decresce con l'esponente, e si pone $x^\alpha := \inf\{x^q : q \in \mathbb{Q},\ 0 < q \le \alpha\}$.
- **Esponente negativo.** $x^{\alpha} := \frac{1}{x^{-\alpha}}$ per $\alpha < 0$, definita dove è definita $x^{-\alpha}$ tolto lo zero; in altre parole è la composta di $x^{-\alpha}$ con $y \mapsto \frac{1}{y}$.

Su $(0, +\infty)$, per $\alpha > 0$ la potenza è strettamente crescente, per $\alpha < 0$ strettamente decrescente. Tutte le potenze passano per $(1, 1)$. Per $\alpha > 1$ il grafico sta sotto la bisettrice in $(0, 1)$ e sopra per $x > 1$; per $0 < \alpha < 1$ vale il contrario.

![Figura 1.4](../figure/1-4.svg)

*Figura 1.4. Grafici di $x^\alpha$ su $[0, +\infty)$ per $\alpha > 1$, $\alpha = 1$ e $0 < \alpha < 1$, con il punto $(1, 1)$ in comune.*

### Esponenziali e logaritmi

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 1*, cap. 2 (AM1A-02, AM1A-06)
> Fissata una base $a > 0$, $a \ne 1$, la funzione **esponenziale** $x \mapsto a^x$ è definita su tutto $\mathbb{R}$, con lo stesso procedimento delle potenze (prima per $x$ razionale, poi con sup e inf), ed è sempre positiva. Valgono le proprietà
> $$a^{x + y} = a^x a^y, \qquad (a^x)^y = a^{xy}, \qquad a^{-x} = \frac{1}{a^x}.$$
> Per $a > 1$ è strettamente crescente, per $0 < a < 1$ strettamente decrescente; in entrambi i casi l'immagine è $(0, +\infty)$ e il grafico passa per $(0, 1)$.
>
> Essendo strettamente monotona, l'esponenziale è iniettiva, e la sua inversa è il **logaritmo** in base $a$: $\log_a : (0, +\infty) \to \mathbb{R}$, con
> $$y = \log_a x \iff a^y = x.$$
> Dalle proprietà dell'esponenziale seguono quelle del logaritmo: $\log_a(xy) = \log_a x + \log_a y$, $\log_a(x^b) = b \log_a x$, $\log_a 1 = 0$, e il cambiamento di base $\log_a x = \frac{\log_b x}{\log_b a}$. Il logaritmo è strettamente crescente se $a > 1$ e strettamente decrescente se $0 < a < 1$.
>
> La base più usata è il numero $e \approx 2{,}718$, che si definisce nel modulo 2 come limite di $(1 + 1/n)^n$. Si scrive $\ln x = \log_e x$ per il **logaritmo naturale**.

![Figura 1.5](../figure/1-5.svg)

*Figura 1.5. Grafici di $a^x$ e $\log_a x$ per $a > 1$ e per $0 < a < 1$, simmetrici rispetto alla bisettrice.*

### Funzioni trigonometriche

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 1*, cap. 2 (AM1A-02)
> Sulla circonferenza di centro l'origine e raggio 1, a ogni $x \in \mathbb{R}$ corrisponde il punto $P$ che si raggiunge percorrendo un arco di lunghezza $|x|$ a partire da $(1, 0)$, in verso antiorario se $x > 0$ e orario se $x < 0$ (angolo in radianti). Le coordinate di $P$ sono $(\cos x, \sin x)$. Seno e coseno sono definiti su $\mathbb{R}$, hanno immagine $[-1, 1]$ e sono periodiche di periodo $2\pi$; il seno è dispari, il coseno pari. La **tangente** $\tan x = \frac{\sin x}{\cos x}$ è definita per $x \ne \frac{\pi}{2} + k\pi$, $k \in \mathbb{Z}$, ha periodo $\pi$ e immagine $\mathbb{R}$.

Le identità fondamentali, da sapere a memoria, sono:

$$\cos^2 x + \sin^2 x = 1,$$

$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta, \qquad \cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta,$$

$$\sin 2x = 2\sin x\cos x, \qquad \cos 2x = 2\cos^2 x - 1 = 1 - 2\sin^2 x,$$

$$\sin x - \sin y = 2\sin\frac{x - y}{2}\cos\frac{x + y}{2}, \qquad \cos x - \cos y = -2\sin\frac{x - y}{2}\sin\frac{x + y}{2},$$

$$\sin(x + \pi) = -\sin x, \quad \cos(x + \pi) = -\cos x, \quad \sin\left(x + \tfrac{\pi}{2}\right) = \cos x, \quad \cos\left(x + \tfrac{\pi}{2}\right) = -\sin x.$$

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 1*, cap. 2 (AM1A-05, AM1A-06)
> Le funzioni trigonometriche non sono iniettive, ma lo diventano su intervalli opportuni, e lì si invertono:
>
> - $\arcsin : [-1, 1] \to \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ è l'inversa di $\sin$ ristretto a $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, strettamente crescente;
> - $\arccos : [-1, 1] \to [0, \pi]$ è l'inversa di $\cos$ ristretto a $[0, \pi]$, strettamente decrescente;
> - $\arctan : \mathbb{R} \to \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ è l'inversa di $\tan$ ristretta a $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, strettamente crescente.
>
> Attenzione: $\arcsin(\sin x) = x$ solo per $x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$; ad esempio $\arcsin(\sin \pi) = 0$.

![Figura 1.6](../figure/1-6.svg)

*Figura 1.6. Grafici di $\sin$, $\cos$, $\tan$ e delle loro inverse $\arcsin$, $\arccos$, $\arctan$.*

## 1.9 Grafici e operazioni sulle funzioni

> [!aggiunta] Aggiunta in revisione · fonte: Canuto-Tabacco, *Analisi Matematica 1*, cap. 2 (AM1A-03)
> Dal grafico di $y = f(x)$ si ottengono quelli di molte funzioni collegate, senza rifare i conti. Con $c > 0$:
>
> - $f(x) + c$ e $f(x) - c$: traslazione verticale, verso l'alto o verso il basso, di $c$;
> - $f(x + c)$ e $f(x - c)$: traslazione orizzontale, verso sinistra o verso destra, di $c$;
> - $c\,f(x)$: dilatazione verticale (contrazione se $c < 1$); $f(cx)$: contrazione orizzontale (dilatazione se $c < 1$);
> - $-f(x)$: simmetria rispetto all'asse $x$; $f(-x)$: simmetria rispetto all'asse $y$;
> - $|f(x)|$: le parti del grafico sotto l'asse $x$ si ribaltano sopra;
> - $f(|x|)$: si tiene la parte con $x \ge 0$ e la si ribalta a sinistra dell'asse $y$.
>
> Ad esempio, il grafico di $y = |x - 2| - 1$ è quello di $|x|$ traslato di 2 a destra e di 1 verso il basso: una "V" con vertice in $(2, -1)$.

![Figura 1.7](../figure/1-7.svg)

*Figura 1.7. Le trasformazioni del grafico di una stessa funzione, ad esempio $\sin x$: $\sin x + 1$, $\sin(x - \pi/4)$, $2\sin x$, $\sin 2x$, $|\sin x|$.*

## Esempi ed esercizi svolti

> [!esempio] Domini
> **a)** $f(x) = \frac{\sqrt{x^2 - 3x - 4}}{x + 5}$. Serve il radicando non negativo, $x^2 - 3x - 4 = (x - 4)(x + 1) \ge 0$, cioè $x \le -1$ oppure $x \ge 4$, e il denominatore non nullo, $x \ne -5$. Il dominio è $(-\infty, -5) \cup (-5, -1] \cup [4, +\infty)$.
>
> **b)** $f(x) = \ln(x^2 - x)$. Serve l'argomento positivo: $x(x - 1) > 0$, cioè $x < 0$ oppure $x > 1$. Il dominio è $(-\infty, 0) \cup (1, +\infty)$.
>
> **c)** $f(x) = \sqrt{\cos x - 1}$. Serve $\cos x - 1 \ge 0$, cioè $\cos x \ge 1$; poiché $\cos x \le 1$ sempre, deve essere $\cos x = 1$, quindi $x = 2k\pi$ con $k \in \mathbb{Z}$. Il dominio è l'insieme di questi punti isolati e l'immagine è $\{0\}$.

> [!esempio] Immagini
> **a)** $f(x) = \frac{1}{x^2 + 1}$. Si cerca per quali $y$ l'equazione $y = \frac{1}{x^2 + 1}$ ha soluzione. Deve essere $y > 0$, e allora $x^2 = \frac{1}{y} - 1$, che ha soluzione se e solo se $\frac{1}{y} - 1 \ge 0$, cioè $y \le 1$. L'immagine è $(0, 1]$: il massimo 1 si raggiunge in $x = 0$, mentre lo 0 non si raggiunge mai.
>
> **b)** $f(x) = \sqrt{x + 2} - 1$. Il dominio è $[-2, +\infty)$; la radice assume tutti i valori di $[0, +\infty)$, quindi l'immagine è $[-1, +\infty)$. Sul grafico, è quello di $\sqrt{x}$ traslato di 2 a sinistra e di 1 verso il basso.

## Riepilogo

I numeri reali estendono i razionali e sono caratterizzati dalle proprietà algebriche, dall'ordinamento totale e dalla completezza: ogni insieme non vuoto e limitato superiormente ha un estremo superiore, cioè un più piccolo maggiorante, che si riconosce dalle due condizioni "$x \le S$ per ogni $x \in A$" e "per ogni $\varepsilon > 0$ c'è un $x \in A$ con $x > S - \varepsilon$". Il valore assoluto misura le distanze e soddisfa $|x + y| \le |x| + |y|$ e $\big||x| - |y|\big| \le |x - y|$.

Una funzione associa a ogni punto del dominio un solo valore; immagine, controimmagine e grafico la descrivono. Una funzione iniettiva ha un'inversa, definita sull'immagine, il cui grafico è il simmetrico rispetto a $y = x$. Restringere il dominio rende invertibili funzioni come $x^2$, seno, coseno e tangente, da cui nascono radici e funzioni trigonometriche inverse. La monotonia stretta implica l'iniettività, non il contrario. Potenze, esponenziali e logaritmi sono strettamente monotone sui loro domini naturali, e $\log_a$ è l'inversa di $a^x$. Infine, traslazioni, dilatazioni, simmetrie e valori assoluti permettono di disegnare molti grafici partendo da quelli elementari.
