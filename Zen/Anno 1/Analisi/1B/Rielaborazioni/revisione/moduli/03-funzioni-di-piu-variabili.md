---
corso: Analisi Matematica 1B
modulo: 3
titolo: Funzioni di più variabili
programma: [AM1B-03, AM1B-04, AM1B-05, AM1B-06, AM1B-07]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 3 · Funzioni di più variabili

**In questo modulo.** Si usano i limiti, le derivate, Fermat, Weierstrass e la formula di Taylor del corso di Analisi 1A; per il criterio dell'Hessiana servono anche autovalori e determinanti di una matrice simmetrica, dal corso di Geometria. Si introduce lo spazio $\mathbb{R}^n$ con la sua struttura algebrica e geometrica (norma, distanza, prodotto scalare) e le nozioni topologiche che servono per parlare di limiti: intorni, punti interni e di frontiera, insiemi aperti, chiusi, limitati e compatti. Poi si studiano le funzioni $f : \mathbb{R}^n \to \mathbb{R}$: dominio, grafico, insiemi di livello, limiti e continuità, derivate parziali e direzionali, gradiente, differenziabilità e piano tangente, derivate seconde, Hessiana e teorema di Schwarz. L'ultima parte è la ricerca dei massimi e minimi liberi con il teorema di Fermat e il criterio dell'Hessiana. Alla fine del modulo si sa studiare il dominio e le curve di livello di una funzione di due variabili, decidere se un limite esiste, calcolare gradiente e piano tangente e classificare i punti critici.

## 3.1 Lo spazio euclideo $\mathbb{R}^n$

$\mathbb{R}^n$ è l'insieme delle $n$-uple ordinate di numeri reali, $x = (x_1, \dots, x_n)$; $\mathbb{R}^2$ è il piano cartesiano e $\mathbb{R}^3$ lo spazio. Un elemento di $\mathbb{R}^n$ si può pensare come un **punto** (una posizione) o come un **vettore** applicato nell'origine (uno spostamento). In questo modulo i vettori si scrivono in tondo come i punti, $x$, $v$; negli appunti a mano sono sottolineati.

Con la somma componente per componente e il prodotto per uno scalare, $\mathbb{R}^n$ è uno spazio vettoriale, con la base canonica $e_1 = (1, 0, \dots, 0)$, …, $e_n = (0, \dots, 0, 1)$: ogni vettore si scrive $x = x_1 e_1 + \dots + x_n e_n$.

> [!definizione] Prodotto scalare, norma e distanza
> Il **prodotto scalare** di $x, y \in \mathbb{R}^n$ è $x \cdot y = x_1 y_1 + \dots + x_n y_n$. La **norma** (euclidea) di $x$ è $\lVert x\rVert = \sqrt{x \cdot x} = \sqrt{x_1^2 + \dots + x_n^2}$, la distanza di $x$ dall'origine. La **distanza** fra $x$ e $y$ è $d(x, y) = \lVert x - y\rVert$.

La norma è nulla solo per il vettore nullo, è omogenea, $\lVert \alpha x\rVert = \lvert\alpha\rvert\, \lVert x\rVert$, e soddisfa la **disuguaglianza triangolare** $\lVert x + y\rVert \le \lVert x\rVert + \lVert y\rVert$. Vale la **disuguaglianza di Cauchy-Schwarz** $\lvert x \cdot y\rvert \le \lVert x\rVert\, \lVert y\rVert$, che permette di definire l'angolo $\theta \in [0, \pi]$ fra due vettori non nulli con $\cos\theta = \frac{x \cdot y}{\lVert x\rVert\, \lVert y\rVert}$; in particolare $x \cdot y = 0$ vuol dire che $x$ e $y$ sono **ortogonali**.

## 3.2 Nozioni di topologia

> [!definizione] Intorno sferico
> L'**intorno sferico** (palla aperta) di centro $x_0$ e raggio $r > 0$ è $B_r(x_0) = \{x \in \mathbb{R}^n : \lVert x - x_0\rVert < r\}$. In $\mathbb{R}^2$ è il disco senza la circonferenza, in $\mathbb{R}$ l'intervallo $(x_0 - r, x_0 + r)$.

Sia $\Omega \subseteq \mathbb{R}^n$. Un punto $x$ è **interno** a $\Omega$ se qualche $B_r(x)$ è contenuto in $\Omega$; **esterno** se qualche $B_r(x)$ è contenuto nel complementare; **di frontiera** se non è né interno né esterno, cioè se ogni intorno di $x$ contiene punti di $\Omega$ e punti del complementare. L'insieme dei punti interni è l'**interno** $\mathring{\Omega}$, quello dei punti di frontiera è la **frontiera** $\partial\Omega$, e $\bar{\Omega} = \Omega \cup \partial\Omega$ è la **chiusura**. Vale $\mathring{\Omega} \subseteq \Omega \subseteq \bar{\Omega}$.

> [!definizione] Aperti, chiusi, limitati, compatti
> $\Omega$ è **aperto** se ogni suo punto è interno ($\Omega = \mathring{\Omega}$), **chiuso** se contiene la sua frontiera ($\Omega = \bar{\Omega}$), equivalentemente se il complementare è aperto. È **limitato** se è contenuto in qualche palla $B_R(0)$. È **compatto** se è chiuso e limitato.

Le palle aperte sono aperte, le palle chiuse $\{\lVert x - x_0\rVert \le r\}$ sono chiuse; $\mathbb{R}^n$ e $\emptyset$ sono gli unici insiemi aperti e chiusi insieme. Un insieme può non essere né aperto né chiuso: la corona $\{2 < \lVert x\rVert \le 3\}$ non è aperta, perché i punti di norma 3 le appartengono ma non sono interni, e non è chiusa, perché i punti di norma 2 sono di frontiera ma non le appartengono. Le unioni di aperti e le intersezioni finite di aperti sono aperte; le intersezioni di chiusi e le unioni finite di chiusi sono chiuse.

Un punto $x_0$ è **di accumulazione** per $\Omega$ se ogni suo intorno contiene punti di $\Omega$ diversi da $x_0$; un punto di $\Omega$ che non è di accumulazione è **isolato**. Un insieme è **connesso** se, intuitivamente, è fatto di un solo pezzo: non si può scrivere come unione di due aperti disgiunti e non vuoti (relativamente a $\Omega$).

## 3.3 Funzioni di più variabili, grafici e insiemi di livello

Una funzione di più variabili reali è $f : \operatorname{dom}(f) \subseteq \mathbb{R}^n \to \mathbb{R}$. L'**immagine** è $\operatorname{im}(f) = \{f(x) : x \in \operatorname{dom}(f)\}$ e il **grafico** è il sottoinsieme di $\mathbb{R}^{n+1}$
$$G(f) = \{(x, z) \in \mathbb{R}^{n+1} : x \in \operatorname{dom}(f),\ z = f(x)\}.$$
Per $n = 2$ il grafico è una superficie nello spazio.

> [!esempio] Domini
>
> - $f(x, y) = \frac{x^2 + y^2}{x^2 - y^2}$: serve $x^2 \neq y^2$, cioè $y \neq \pm x$. Il dominio è il piano senza le due bisettrici.
> - $f(x, y, z) = \ln(1 - x^2 - y^2 - z^2)$: serve $x^2 + y^2 + z^2 < 1$. Il dominio è la palla aperta $B_1(0) \subseteq \mathbb{R}^3$.
> - $f(x, y) = \ln(xy - x^2)$: serve $x(y - x) > 0$, cioè $x > 0$ e $y > x$, oppure $x < 0$ e $y < x$. Il dominio è l'unione di due regioni angolari aperte del piano, delimitate dall'asse $y$ e dalla bisettrice.

> [!definizione] Insieme di livello
> Per $k \in \mathbb{R}$, l'**insieme di livello** $k$ di $f$ è $L(f, k) = \{x \in \operatorname{dom}(f) : f(x) = k\}$. Per $n = 2$ si chiama di solito **curva di livello**: è la proiezione sul piano $xy$ della sezione del grafico all'altezza $z = k$.

> [!esempio] Paraboloide e cono
> Per $f(x, y) = x^2 + y^2$ l'immagine è $[0, +\infty)$. Per $k > 0$ l'insieme di livello è la circonferenza di centro l'origine e raggio $\sqrt{k}$; per $k = 0$ è il solo punto $(0, 0)$; per $k < 0$ è vuoto. Il grafico è un **paraboloide**. Per $f(x, y) = \sqrt{x^2 + y^2}$ le curve di livello sono ancora circonferenze, di raggio $k$, e il grafico è un **cono** con vertice nell'origine. Le due famiglie si distinguono dalla spaziatura: per il cono, a livelli equispaziati corrispondono circonferenze equispaziate; per il paraboloide le circonferenze si infittiscono allontanandosi dall'origine (figura 3.1).

![Figura 3.1](../figure/3-1.svg)

## 3.4 Limiti e continuità

> [!definizione] Limite
> Sia $f : \Omega \subseteq \mathbb{R}^n \to \mathbb{R}$ e $x_0$ di accumulazione per $\Omega$. Si dice che $\lim_{x \to x_0} f(x) = L \in \mathbb{R}$ se per ogni $\varepsilon > 0$ esiste $\delta > 0$ tale che $\lvert f(x) - L\rvert < \varepsilon$ per ogni $x \in \Omega$ con $0 < \lVert x - x_0\rVert < \delta$.

Valgono, come in una variabile, l'unicità del limite, l'algebra dei limiti e il teorema del confronto. $f$ è **continua** in $x_0 \in \Omega$ se $x_0$ è isolato oppure se $\lim_{x \to x_0} f(x) = f(x_0)$. Somme, prodotti, quozienti e composizioni di funzioni elementari sono continui dove sono definiti.

La differenza con una variabile è che ci si può avvicinare a $x_0$ lungo infinite curve diverse, e il limite deve esistere indipendentemente dal percorso. Ne viene un modo per dimostrare che un limite **non** esiste: trovare due curve lungo le quali si ottengono limiti diversi.

> [!esempio] Tre limiti nell'origine
>
> - $\lim_{(x,y) \to (0,0)} \frac{x^3}{x^2 + y^2}$. Poiché $x^2 + y^2 \ge x^2$, si ha $\left\lvert\frac{x^3}{x^2 + y^2}\right\rvert \le \frac{\lvert x\rvert^3}{x^2} = \lvert x\rvert \to 0$: il limite è 0 per confronto.
> - $\lim_{(x,y) \to (0,0)} \frac{x + y}{x - y}$. Lungo l'asse $x$ ($y = 0$) la funzione vale 1, lungo l'asse $y$ ($x = 0$) vale $-1$: il limite non esiste.
> - $\lim_{(x,y) \to (0,0)} \frac{x^2 y}{x^4 + y^2}$. Lungo ogni retta $y = mx$ si ottiene $\frac{m x^3}{x^4 + m^2 x^2} = \frac{m x}{x^2 + m^2} \to 0$. Ma lungo la parabola $y = x^2$ la funzione vale $\frac{x^4}{2x^4} = \frac{1}{2}$: il limite non esiste. Provare tutte le rette non basta.

In $\mathbb{R}^2$, per i limiti nell'origine conviene spesso passare alle **coordinate polari** $x = \rho\cos\theta$, $y = \rho\sin\theta$, con $(x, y) \to (0, 0)$ che diventa $\rho \to 0^+$ per ogni $\theta$.

> [!teorema] Criterio in coordinate polari
> Se esistono $L \in \mathbb{R}$ e una funzione $g(\rho)$, che dipende solo da $\rho$, con $\lvert f(\rho\cos\theta, \rho\sin\theta) - L\rvert \le g(\rho)$ per ogni $\theta$ e ogni $\rho$ piccolo, e $g(\rho) \to 0$ per $\rho \to 0^+$, allora $\lim_{(x,y) \to (0,0)} f(x, y) = L$.

Per il primo esempio: $\left\lvert\frac{\rho^3\cos^3\theta}{\rho^2}\right\rvert = \rho\lvert\cos\theta\rvert^3 \le \rho \to 0$. Il punto essenziale è che la maggiorazione deve valere **uniformemente** in $\theta$: per $\frac{x^2 y}{x^4 + y^2}$ in polari si ottiene $\frac{\rho\cos^2\theta\sin\theta}{\rho^2\cos^4\theta + \sin^2\theta}$, che tende a 0 per ogni $\theta$ fissato ma non si maggiora con una $g(\rho)$ indipendente da $\theta$.

## 3.5 Derivate parziali, gradiente, derivate direzionali

> [!definizione] Derivata parziale e gradiente
> Sia $x_0$ interno al dominio di $f$. La **derivata parziale** di $f$ rispetto a $x_i$ in $x_0$ è, se esiste finito,
> $$\frac{\partial f}{\partial x_i}(x_0) = \lim_{h \to 0} \frac{f(x_0 + h e_i) - f(x_0)}{h}.$$
> Se esistono tutte, $f$ si dice **derivabile** in $x_0$ e il vettore $\nabla f(x_0) = \left(\frac{\partial f}{\partial x_1}(x_0), \dots, \frac{\partial f}{\partial x_n}(x_0)\right)$ si chiama **gradiente**.

In pratica la derivata rispetto a $x$ si calcola derivando come in una variabile e trattando le altre variabili come costanti.

> [!esempio] Un gradiente
> $f(x, y, z) = x\ln(x + y - z)$, definita per $x + y - z > 0$:
> $$\frac{\partial f}{\partial x} = \ln(x + y - z) + \frac{x}{x + y - z}, \quad \frac{\partial f}{\partial y} = \frac{x}{x + y - z}, \quad \frac{\partial f}{\partial z} = -\frac{x}{x + y - z}.$$

> [!definizione] Derivata direzionale
> Sia $v \in \mathbb{R}^n$ non nullo (di solito un versore, $\lVert v\rVert = 1$). La **derivata direzionale** di $f$ in $x_0$ lungo $v$ è
> $$D_v f(x_0) = \frac{\partial f}{\partial v}(x_0) = \lim_{h \to 0} \frac{f(x_0 + hv) - f(x_0)}{h}.$$

Le derivate parziali sono le derivate direzionali lungo i vettori della base canonica. Per $f(x, y) = x^2 + y^3$, $x_0 = (0, 1)$ e $v = (1, 1)$:
$$D_v f(0, 1) = \lim_{h \to 0} \frac{h^2 + (1 + h)^3 - 1}{h} = \lim_{h \to 0} (3 + 4h + h^2) = 3.$$

In più variabili la derivabilità **non** implica la continuità, perché le derivate parziali guardano solo lungo gli assi.

**Derivabile ma non continua.** Sia $f(x, y) = \frac{xy}{x^2 + y^2}$ per $(x, y) \neq (0, 0)$ e $f(0, 0) = 0$. Sugli assi $f$ è nulla, quindi $\frac{\partial f}{\partial x}(0, 0) = \frac{\partial f}{\partial y}(0, 0) = 0$: la funzione è derivabile nell'origine. Ma lungo la retta $y = x$ vale $\frac{1}{2}$, quindi non ha limite 0 e non è continua nell'origine.

## 3.6 Differenziabilità e piano tangente

Serve una nozione più forte della derivabilità, che controlli tutte le direzioni insieme.

> [!definizione] Funzione differenziabile
> $f$, derivabile nel punto interno $x_0$, è **differenziabile** in $x_0$ se
> $$f(x) = f(x_0) + \nabla f(x_0) \cdot (x - x_0) + o(\lVert x - x_0\rVert) \quad \text{per } x \to x_0,$$
> cioè se $\displaystyle\lim_{x \to x_0} \frac{f(x) - f(x_0) - \nabla f(x_0) \cdot (x - x_0)}{\lVert x - x_0\rVert} = 0$.

> [!teorema] Conseguenze della differenziabilità
> Se $f$ è differenziabile in $x_0$: $f$ è continua in $x_0$; ha derivata direzionale lungo ogni $v \neq 0$; e vale la **formula del gradiente** $D_v f(x_0) = \nabla f(x_0) \cdot v$.

Per l'esempio del paragrafo 3.5, $\nabla f(0, 1) = (0, 3)$ e $\nabla f(0, 1) \cdot (1, 1) = 3$, come trovato con la definizione.

**Significato del gradiente.** Dalla formula del gradiente e da Cauchy-Schwarz, fra le direzioni unitarie $v$ la derivata direzionale $\nabla f(x_0) \cdot v$ è massima per $v = \frac{\nabla f(x_0)}{\lVert\nabla f(x_0)\rVert}$ e nulla per $v$ ortogonale al gradiente. Il gradiente indica quindi la direzione di massima crescita di $f$, ed è ortogonale all'insieme di livello che passa per $x_0$, lungo il quale $f$ non cambia.

Per $n = 2$ la differenziabilità vuol dire che il grafico ha nel punto $(x_0, y_0, f(x_0, y_0))$ un **piano tangente**, di equazione
$$z = f(x_0, y_0) + \frac{\partial f}{\partial x}(x_0, y_0)(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0)(y - y_0).$$

Verificare la differenziabilità con la definizione è laborioso; di solito si usa una condizione sufficiente.

> [!teorema] Teorema del differenziale totale
> Se le derivate parziali di $f$ esistono in un intorno di $x_0$ e sono continue in $x_0$, allora $f$ è differenziabile in $x_0$. In particolare le funzioni di classe $C^1$ su un aperto sono differenziabili in ogni punto.

> [!esempio] Piano tangente
> $f(x, y) = x^3 + y^3 + xy$ è un polinomio, quindi di classe $C^1$. Si ha $\nabla f(x, y) = (3x^2 + y, 3y^2 + x)$, $\nabla f(1, 1) = (4, 4)$ e $f(1, 1) = 3$. Il piano tangente al grafico in $(1, 1, 3)$ è $z = 3 + 4(x - 1) + 4(y - 1)$, cioè $z = 4x + 4y - 5$.

## 3.7 Derivate seconde, Hessiana e teorema di Schwarz

Se le derivate parziali esistono in un intorno, si possono derivare di nuovo: $\frac{\partial^2 f}{\partial x_j \partial x_i} = \frac{\partial}{\partial x_j}\frac{\partial f}{\partial x_i}$. Per $i = j$ si parla di **derivata pura**, per $i \neq j$ di **derivata mista**; si scrive anche $f_{x_i x_j}$.

> [!definizione] Matrice Hessiana
> Se in $x_0$ esistono tutte le derivate seconde, la **matrice Hessiana** è la matrice $n \times n$ $H_f(x_0)$ che ha nella riga $i$ e colonna $j$ la derivata $\frac{\partial^2 f}{\partial x_i \partial x_j}(x_0)$. $f$ è **di classe $C^2$** su un aperto se tutte le derivate seconde esistono e sono continue.

> [!teorema] Teorema di Schwarz
> Se $f$ è di classe $C^2$ sull'aperto $\Omega$, per ogni $x_0 \in \Omega$ e ogni $i$, $j$ le derivate miste coincidono: $\frac{\partial^2 f}{\partial x_i \partial x_j}(x_0) = \frac{\partial^2 f}{\partial x_j \partial x_i}(x_0)$. Quindi l'Hessiana è una matrice simmetrica.

Per $f$ di classe $C^2$ vale la **formula di Taylor del secondo ordine**:
$$f(x) = f(x_0) + \nabla f(x_0) \cdot (x - x_0) + \frac{1}{2}(x - x_0)^T H_f(x_0)(x - x_0) + o(\lVert x - x_0\rVert^2).$$
Il termine quadratico fa la parte della derivata seconda in una variabile: descrive come il grafico si incurva vicino al punto.

## 3.8 Massimi e minimi liberi

> [!definizione] Estremi locali e globali
> $x_0 \in \operatorname{dom}(f)$ è un punto di **minimo locale** se esiste $\varepsilon > 0$ tale che $f(x) \ge f(x_0)$ per ogni $x \in B_\varepsilon(x_0) \cap \operatorname{dom}(f)$; di **massimo locale** se vale $f(x) \le f(x_0)$. È di minimo (massimo) **globale** su $A$ se la disuguaglianza vale per ogni $x \in A$. Massimi e minimi si chiamano **estremi**.

> [!teorema] Teorema di Weierstrass
> Una funzione continua su un insieme compatto (chiuso e limitato) $K$ ha in $K$ almeno un punto di massimo globale e almeno un punto di minimo globale.

> [!definizione] Punto critico
> Un punto $x_0$ in cui $f$ è derivabile si dice **critico** (o stazionario) se $\nabla f(x_0) = 0$.

> [!teorema] Teorema di Fermat
> Se $x_0$ è interno al dominio, $f$ è derivabile in $x_0$ e $x_0$ è un estremo locale, allora $\nabla f(x_0) = 0$.

*Dimostrazione.* Per ogni $i$ la funzione di una variabile $g(t) = f(x_0 + t e_i)$ ha un estremo locale in $t = 0$, ed è derivabile in 0 con $g'(0) = \frac{\partial f}{\partial x_i}(x_0)$. Per il teorema di Fermat in una variabile $g'(0) = 0$. $\square$

Come in una variabile il viceversa è falso: $f(x, y) = xy$ ha gradiente nullo nell'origine, ma ha valori positivi nel primo e terzo quadrante e negativi negli altri due. Un punto critico che non è né di massimo né di minimo si chiama **punto di sella**. Gli estremi di $f$ su un insieme vanno quindi cercati fra i punti critici interni, i punti interni in cui $f$ non è derivabile (come il vertice del cono $\sqrt{x^2 + y^2}$) e i punti della frontiera.

> [!teorema] Criterio dell'Hessiana
> Sia $x_0$ un punto critico e $f$ di classe $C^2$ in un suo intorno.
>
> 1. Se $H_f(x_0)$ è definita positiva (tutti gli autovalori positivi), $x_0$ è un minimo locale.
> 2. Se è definita negativa (tutti gli autovalori negativi), $x_0$ è un massimo locale.
> 3. Se è indefinita (autovalori di segno opposto), $x_0$ è un punto di sella.
> 4. Se è semidefinita (qualche autovalore nullo e gli altri dello stesso segno), il criterio non decide.

Per $n = 2$, con $\Delta = \det H_f(x_0) = f_{xx} f_{yy} - f_{xy}^2$:

- $\Delta > 0$ e $f_{xx} > 0$: minimo locale;
- $\Delta > 0$ e $f_{xx} < 0$: massimo locale;
- $\Delta < 0$: punto di sella;
- $\Delta = 0$: caso dubbio.

> [!esempio] Cinque punti critici nell'origine
> In tutti i casi l'unico punto critico è $(0, 0)$.
>
> - $x^2 + y^2$: $H = \operatorname{diag}(2, 2)$, $\Delta = 4 > 0$, $f_{xx} > 0$: minimo (globale).
> - $-x^2 - y^2$: $H = \operatorname{diag}(-2, -2)$, $\Delta = 4$, $f_{xx} < 0$: massimo.
> - $x^2 - y^2$: $H = \operatorname{diag}(2, -2)$, $\Delta = -4 < 0$: sella; la funzione cresce lungo l'asse $x$ e decresce lungo l'asse $y$.
> - $x^2 + y^4$: $H(0, 0) = \operatorname{diag}(2, 0)$, $\Delta = 0$, caso dubbio. Ma $f \ge 0 = f(0, 0)$ ovunque: minimo globale.
> - $(y - x^2)(y - 2x^2) = y^2 - 3x^2 y + 2x^4$: $\nabla f = (8x^3 - 6xy, 2y - 3x^2)$ si annulla in $(0, 0)$, $H(0, 0) = \operatorname{diag}(0, 2)$, caso dubbio. Studiando il segno: $f < 0$ fra le due parabole, cioè per $x^2 < y < 2x^2$, e $f > 0$ fuori. In ogni intorno dell'origine ci sono valori dei due segni: è un punto di sella, anche se lungo ogni retta per l'origine la funzione ha un minimo in 0.

## Esempi ed esercizi svolti

**Esercizio 1.** Gradiente di $f(x, y, z) = \sin\left(\frac{xy^2}{1 + z^2}\right)$ nel punto $(0, 1, 1)$. Con la regola della catena:
$$\frac{\partial f}{\partial x} = \cos\left(\tfrac{xy^2}{1+z^2}\right)\frac{y^2}{1 + z^2}, \quad \frac{\partial f}{\partial y} = \cos\left(\tfrac{xy^2}{1+z^2}\right)\frac{2xy}{1 + z^2}, \quad \frac{\partial f}{\partial z} = -\cos\left(\tfrac{xy^2}{1+z^2}\right)\frac{2xy^2 z}{(1 + z^2)^2}.$$
In $(0, 1, 1)$ l'argomento del coseno è 0, e $\nabla f(0, 1, 1) = \left(\frac{1}{2}, 0, 0\right)$.

**Esercizio 2.** Punti critici di $f(x, y) = x^3 - 3x + y^2$. $\nabla f = (3x^2 - 3, 2y) = 0$ dà $(1, 0)$ e $(-1, 0)$. L'Hessiana è $\begin{pmatrix} 6x & 0 \\ 0 & 2 \end{pmatrix}$. In $(1, 0)$: $\Delta = 12 > 0$, $f_{xx} = 6 > 0$, minimo locale. In $(-1, 0)$: $\Delta = -12 < 0$, sella. Non ci sono estremi globali, perché $f(x, 0) = x^3 - 3x$ è illimitata sopra e sotto.

**Esercizio 3.** Massimo e minimo di $f(x, y) = x^2 + y^2 - 2x$ sul disco chiuso $K = \{x^2 + y^2 \le 4\}$. $K$ è compatto e $f$ continua: per Weierstrass gli estremi esistono. All'interno, $\nabla f = (2x - 2, 2y) = 0$ dà $(1, 0)$, con $f(1, 0) = -1$. Sulla frontiera $x^2 + y^2 = 4$ la funzione vale $4 - 2x$ con $x \in [-2, 2]$: minimo 0 in $(2, 0)$, massimo 8 in $(-2, 0)$. Confrontando: il minimo globale è $-1$ in $(1, 0)$, il massimo globale è 8 in $(-2, 0)$.

### Altri esercizi svolti

Nelle prove si chiede quasi sempre di disegnare un dominio, di calcolare un limite nell'origine, e di trovare e classificare i punti stazionari; a volte una derivata direzionale o la differenziabilità.

**Esercizio 4. Un dominio da disegnare.** Dominio di $f(x, y) = \sqrt{4 - x^2 - y^2} + \ln(y - x^2)$.

La radice vuole $x^2 + y^2 \le 4$: il disco chiuso di centro l'origine e raggio 2, bordo compreso. Il logaritmo vuole $y > x^2$: la parte di piano strettamente sopra la parabola $y = x^2$, che resta esclusa. Il dominio è l'intersezione: la "lente" dentro il cerchio e sopra la parabola. Le due curve si incontrano dove $y + y^2 = 4$, cioè $y = \frac{-1 + \sqrt{17}}{2} \approx 1{,}56$ e $x = \pm\sqrt{y} \approx \pm 1{,}25$. Nel disegno l'arco di circonferenza va tratto pieno (incluso) e l'arco di parabola tratteggiato (escluso); i due punti d'incontro sono esclusi, perché stanno sulla parabola.

**Esercizio 5. Un dominio con una frazione sotto radice.** Dominio di $f(x, y) = \sqrt{\dfrac{xy - 1}{x^2 + y^2 - 9}}$.

Serve la frazione $\ge 0$ con il denominatore non nullo. Numeratore e denominatore devono avere lo stesso segno: (i) $xy \ge 1$ e $x^2 + y^2 > 9$: le due regioni del primo e del terzo quadrante che stanno al di là dei rami dell'iperbole $xy = 1$ (dalla parte opposta agli assi), limitatamente ai punti fuori dal cerchio di raggio 3; oppure (ii) $xy \le 1$ e $x^2 + y^2 < 9$, cioè l'interno del cerchio tolte le due regioni oltre l'iperbole. L'iperbole fa parte del dominio (numeratore nullo), la circonferenza no (denominatore nullo). Conviene disegnare prima le due curve, che dividono il piano in sei regioni, e poi controllare il segno con un punto per regione: $(0, 0)$ dà $\frac{-1}{-9} > 0$ (sì), $(4, 4)$ dà $\frac{15}{23} > 0$ (sì), $(4, 0)$ dà $\frac{-1}{7} < 0$ (no).

**Esercizio 6. Limiti nell'origine.** (a) $\displaystyle\lim \frac{x^3 y}{x^2 + y^2}$; (b) $\displaystyle\lim \frac{e^{x^2 y} - 1}{x^2 + y^2}$; (c) $\displaystyle\lim \frac{\ln(1 + xy^3)}{(x^2 + y^2)^2}$; (d) $\displaystyle\lim \frac{x\sin(xy)}{x^2 + y^2}$.

(a) In polari $\left|\frac{\rho^4\cos^3\theta\sin\theta}{\rho^2}\right| \le \rho^2 \to 0$ indipendentemente da $\theta$: il limite è 0. (b) $e^u - 1 \sim u$ con $u = x^2 y \to 0$, quindi la funzione si comporta come $\frac{x^2 y}{x^2 + y^2}$, che in modulo è $\le \rho\,|\cos^2\theta\sin\theta| \le \rho$: limite 0. (c) $\ln(1 + u) \sim u$ con $u = xy^3$: si studia $\frac{xy^3}{(x^2 + y^2)^2} = \cos\theta\sin^3\theta$, che non dipende da $\rho$ ma da $\theta$. Lungo l'asse $x$ vale 0, lungo la bisettrice $y = x$ vale $\frac{x^4}{4x^4} = \frac{1}{4}$: il limite non esiste. (d) $\sin(xy) \sim xy$, e $\left|\frac{x^2 y}{x^2 + y^2}\right| \le \rho$: limite 0.

Il punto delicato, in (b) e (d), è che l'equivalenza $\sin u \sim u$ vale perché $u = xy \to 0$; formalmente si scrive $\frac{\sin(xy)}{xy} \to 1$ (con la convenzione che vale 1 dove $xy = 0$) e si moltiplica.

**Esercizio 7. Derivate parziali e direzionali senza continuità.** Sia $g(x, y) = \frac{x^2 y}{x^4 + y^2}$ per $(x, y) \ne (0, 0)$, $g(0, 0) = 0$. Studiare in $(0, 0)$ continuità, derivate parziali e derivate direzionali.

*Derivate parziali*: $g(h, 0) = 0$ e $g(0, h) = 0$ per ogni $h$, quindi i rapporti incrementali sono nulli e $g_x(0, 0) = g_y(0, 0) = 0$. *Derivate direzionali*: per $v = (a, b)$ con $b \ne 0$, $\frac{g(ta, tb)}{t} = \frac{a^2 b}{t^2 a^4 + b^2} \to \frac{a^2}{b}$; per $b = 0$ il rapporto è 0. Esistono tutte. *Continuità*: lungo le rette $y = mx$, $g = \frac{mx}{x^2 + m^2} \to 0$; ma lungo la parabola $y = x^2$, $g = \frac{x^4}{2x^4} = \frac{1}{2}$. Non è continua. In più variabili l'esistenza di tutte le derivate direzionali non implica nemmeno la continuità: serve la differenziabilità.

**Esercizio 8. Punti stazionari.** Classificare i punti stazionari di $f(x, y) = x^2 - 2xy + y^3$.

$\nabla f = (2x - 2y,\ -2x + 3y^2)$. Dalla prima equazione $x = y$, e la seconda diventa $3y^2 - 2y = 0$: $y = 0$ oppure $y = \frac{2}{3}$. Punti $(0, 0)$ e $\left(\frac{2}{3}, \frac{2}{3}\right)$. L'Hessiana è $\begin{pmatrix} 2 & -2 \\ -2 & 6y \end{pmatrix}$, con determinante $12y - 4$. In $(0, 0)$ vale $-4 < 0$: sella. In $\left(\frac{2}{3}, \frac{2}{3}\right)$ vale $4 > 0$ con $f_{xx} = 2 > 0$: minimo locale, $f = \frac{4}{9} - \frac{8}{9} + \frac{8}{27} = -\frac{4}{27}$. Non è globale, perché $f(0, y) = y^3 \to -\infty$.

**Esercizio 9. Tre punti stazionari.** Classificare quelli di $f(x, y) = x^4 + y^4 - 4xy$.

$\nabla f = (4x^3 - 4y,\ 4y^3 - 4x) = 0$ dà $y = x^3$ e $x = y^3 = x^9$, cioè $x(x^8 - 1) = 0$: $x = 0, \pm 1$. Punti $(0, 0)$, $(1, 1)$, $(-1, -1)$. Hessiana $\begin{pmatrix} 12x^2 & -4 \\ -4 & 12y^2 \end{pmatrix}$: in $(0, 0)$ il determinante è $-16$, sella; in $(\pm 1, \pm 1)$ è $144 - 16 = 128 > 0$ con $f_{xx} = 12 > 0$, minimi, con $f = -2$. Sono minimi globali: $f \to +\infty$ all'infinito (domina $x^4 + y^4$), quindi il minimo globale esiste ed è uno dei punti stazionari.

**Esercizio 10. Derivata direzionale.** Calcolare la derivata di $f(x, y) = \sqrt{x + y^2 + 1}$ in $P = (0, 1)$ nella direzione $v = \left(\frac{3}{5}, \frac{4}{5}\right)$.

$f$ è differenziabile vicino a $P$ (le derivate parziali sono continue dove il radicando è positivo), quindi $D_v f(P) = \nabla f(P) \cdot v$. $\nabla f = \left(\frac{1}{2\sqrt{x + y^2 + 1}},\ \frac{y}{\sqrt{x + y^2 + 1}}\right)$, in $P$: $\left(\frac{1}{2\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$. Quindi
$$D_v f(P) = \frac{3}{5} \cdot \frac{1}{2\sqrt{2}} + \frac{4}{5} \cdot \frac{1}{\sqrt{2}} = \frac{3 + 8}{10\sqrt{2}} = \frac{11\sqrt{2}}{20}.$$
Il vettore $v$ ha norma 1: se non l'avesse, va prima normalizzato.

**Esercizio 11. Piano tangente.** Scrivere il piano tangente al grafico di $f(x, y) = x e^{xy}$ nel punto $(1, 0)$.

$f(1, 0) = 1$; $f_x = e^{xy}(1 + xy)$ e $f_y = x^2 e^{xy}$, quindi $f_x(1, 0) = 1$ e $f_y(1, 0) = 1$. Il piano è $z = 1 + (x - 1) + y$, cioè $z = x + y$.

**Esercizio 12. Differenziabile qui, non lì.** Sia $f(x, y) = y\ln(1 + x^2 + y^2) + \sqrt{x^2 + y^2}$. È differenziabile vicino a $(1, 1)$? E in $(0, 0)$?

Lontano dall'origine $\sqrt{x^2 + y^2}$ ha derivate parziali $\frac{x}{\sqrt{x^2 + y^2}}$, $\frac{y}{\sqrt{x^2 + y^2}}$, continue; anche il primo addendo è $C^1$. Per il teorema del differenziale totale, $f$ è differenziabile in un intorno di $(1, 1)$. In $(0, 0)$ il primo addendo è differenziabile, ma $\sqrt{x^2 + y^2}$ non ha nemmeno le derivate parziali: $\frac{\sqrt{h^2}}{h} = \frac{|h|}{h}$ non ha limite. Il grafico di $\sqrt{x^2 + y^2}$ è un cono, con la punta nell'origine.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Le rette non bastano.** Studiare $\lim_{(x, y) \to (0, 0)} \frac{xy^2}{x^2 + y^4}$.

*Passo 1: lungo gli assi.* Per $y = 0$ e per $x = 0$ la funzione è nulla: se il limite esiste, vale 0.

*Passo 2: lungo le rette.* Con $y = mx$: $\frac{m^2 x^3}{x^2 + m^4 x^4} = \frac{m^2 x}{1 + m^4 x^2} \to 0$ per ogni $m$.

*Passo 3: le polari non chiudono.* $\frac{\rho^3\cos\theta\sin^2\theta}{\rho^2\cos^2\theta + \rho^4\sin^4\theta}$: per $\theta$ vicino a $\frac{\pi}{2}$ il denominatore può essere piccolo quanto il numeratore, e non si trova una stima uniforme in $\theta$. È il segnale di cercare un'altra curva.

*Passo 4: la curva giusta.* I due termini del denominatore hanno lo stesso ordine se $x = y^2$: lungo questa parabola la funzione vale $\frac{y^4}{2y^4} = \frac{1}{2}$. Il limite non esiste.

**Guidato 2. Classificare con l'Hessiana.** Punti stazionari di $f(x, y) = x^3 + y^3 - 3xy$.

*Passo 1: il gradiente.* $\nabla f = (3x^2 - 3y,\ 3y^2 - 3x)$.

*Passo 2: il sistema.* $y = x^2$ e $x = y^2 = x^4$, quindi $x(x^3 - 1) = 0$: $x = 0$ o $x = 1$. Punti $(0, 0)$ e $(1, 1)$.

*Passo 3: l'Hessiana.* $H = \begin{pmatrix} 6x & -3 \\ -3 & 6y \end{pmatrix}$, $\det H = 36xy - 9$.

*Passo 4: classificazione.* In $(0, 0)$: $\det H = -9 < 0$, sella. In $(1, 1)$: $\det H = 27 > 0$, $f_{xx} = 6 > 0$, minimo locale con $f(1, 1) = -1$. Non globale: $f(x, 0) = x^3 \to -\infty$.

**Guidato 3. Estremi su un quadrato.** Massimo e minimo di $f(x, y) = x^2 + y^2 - x - y$ su $Q = [0, 1] \times [0, 1]$.

*Passo 1: esistenza.* $f$ è continua e $Q$ è chiuso e limitato: per Weierstrass massimo e minimo esistono.

*Passo 2: interno.* $\nabla f = (2x - 1, 2y - 1) = 0$ in $\left(\frac{1}{2}, \frac{1}{2}\right)$, dove $f = -\frac{1}{2}$.

*Passo 3: bordo.* Sul lato $x = 0$: $f = y^2 - y$, con minimo $-\frac{1}{4}$ in $y = \frac{1}{2}$ e massimo 0 agli estremi. Gli altri tre lati, per simmetria, danno gli stessi valori. Nei vertici $f = 0$.

*Passo 4: confronto.* I candidati valgono $-\frac{1}{2}$, $-\frac{1}{4}$ e 0: il minimo è $-\frac{1}{2}$ nel centro, il massimo 0 nei quattro vertici.

## Riepilogo

$\mathbb{R}^n$ è uno spazio vettoriale con prodotto scalare, norma e distanza, e la disuguaglianza di Cauchy-Schwarz. Con le palle aperte si definiscono punti interni, esterni e di frontiera, insiemi aperti, chiusi, limitati e compatti. Una funzione di più variabili ha un dominio, un grafico e insiemi di livello, che per due variabili sono le curve di livello. Il limite deve essere lo stesso lungo ogni percorso: due percorsi con limiti diversi provano che non esiste, una maggiorazione uniforme (in coordinate polari) prova che esiste. Le derivate parziali formano il gradiente; la derivabilità non dà la continuità, la differenziabilità sì, e con essa la formula del gradiente per le derivate direzionali e il piano tangente; una funzione $C^1$ è differenziabile. Per le funzioni $C^2$ l'Hessiana è simmetrica (Schwarz) e compare nella formula di Taylor del secondo ordine. Gli estremi interni sono punti critici (Fermat); il segno degli autovalori dell'Hessiana, o in due variabili il segno del determinante e di $f_{xx}$, li classifica in minimi, massimi e selle, tranne nel caso semidefinito, in cui si studia direttamente il segno di $f - f(x_0)$. Su un compatto gli estremi globali esistono (Weierstrass) e si cercano fra i punti critici interni e la frontiera.

## Formulario

Definizioni, teoremi e procedure del calcolo differenziale in più variabili, con i termini per l'orale.

### Limiti in due variabili

- Per mostrare che un limite **non esiste**: due curve per il punto lungo cui la funzione ha limiti diversi (rette $y = mx$, parabole $x = y^2$, …).
- Per mostrare che **esiste** e vale $l$: in polari, $|f(\rho\cos\theta, \rho\sin\theta) - l| \le g(\rho)$ con $g(\rho) \to 0$ indipendente da $\theta$.
- Le equivalenze di una variabile valgono con l'argomento che tende a 0: $\sin(xy) \sim xy$, $e^{u} - 1 \sim u$, $\ln(1 + u) \sim u$.

### Derivate

$$\frac{\partial f}{\partial x}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}, \qquad \nabla f = \left(f_x, f_y\right), \qquad D_v f = \nabla f \cdot v \ \text{(se differenziabile, } \lVert v\rVert = 1).$$

Differenziabilità in $x_0$: $f(x_0 + h) = f(x_0) + \nabla f(x_0) \cdot h + o(\lVert h\rVert)$. Piano tangente: $z = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$.

| Implicazioni | |
|---|---|
| $C^1$ in un intorno (derivate parziali continue) | $\Rightarrow$ differenziabile (differenziale totale) |
| differenziabile | $\Rightarrow$ continua, derivabile in ogni direzione, $D_v f = \nabla f \cdot v$ |
| derivate parziali (o direzionali) esistenti | $\not\Rightarrow$ continua |

Il gradiente indica la direzione di massima crescita, con $\lVert\nabla f\rVert$ come pendenza massima, ed è perpendicolare agli insiemi di livello.

### Estremi liberi

Condizione necessaria (Fermat): $\nabla f(x_0) = 0$ nei punti interni. Hessiana $H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}$, simmetrica se $f \in C^2$ (Schwarz). Con $\Delta = \det H(x_0)$:

| $\Delta$ | $f_{xx}$ | Punto |
|---|---|---|
| $> 0$ | $> 0$ | minimo locale |
| $> 0$ | $< 0$ | massimo locale |
| $< 0$ | – | sella |
| $= 0$ | – | caso dubbio: si studia il segno di $f - f(x_0)$ |

Estremi su un compatto: si confrontano i punti stazionari interni e il massimo e il minimo sul bordo.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Insieme aperto, chiuso, limitato, compatto | ogni punto interno; contiene il bordo; sta in una palla; chiuso e limitato |
| Punto interno, di frontiera | ha un intorno nell'insieme; ogni intorno ha punti dentro e fuori |
| Insieme di livello | $\{f = c\}$: curve di livello in $\mathbb{R}^2$ |
| Derivata direzionale | derivata lungo la retta per $x_0$ di direzione $v$ |
| Differenziabilità | approssimazione lineare con errore $o(\lVert h\rVert)$ |
| Punto di sella | punto stazionario che non è né massimo né minimo |
| Matrice Hessiana | matrice delle derivate seconde |

### Domande che tornano spesso

- Definire la differenziabilità; dimostrare che differenziabile implica continua e che $D_v f = \nabla f \cdot v$.
- Un esempio di funzione con derivate parziali ma non continua.
- Enunciare il teorema del differenziale totale.
- Perché il gradiente è la direzione di massima crescita? Perché è perpendicolare alle curve di livello?
- Enunciare Fermat in più variabili e il criterio dell'Hessiana; che cosa fare nel caso dubbio.
- Enunciare il teorema di Schwarz.
