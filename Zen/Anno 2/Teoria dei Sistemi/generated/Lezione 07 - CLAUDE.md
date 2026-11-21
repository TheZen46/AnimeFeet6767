---
corso: Teoria dei Sistemi
lezione: 7
data: 2026-10-14
argomenti: [poli e limite dell'antitrasformata, teorema del valore finale, interpretazione con i residui, regola dei segni per polinomi di secondo grado, studio parametrico, teorema del valore iniziale, divisione lunga e serie di Maclaurin, grado relativo]
fonti: [trascrizione parte 1, appunti manuali, dispensa del docente (italiano), dispensa del docente (inglese)]
tags: [teoria-dei-sistemi, lezione]
---

# Lezione 7 — Teoremi del valore finale e del valore iniziale

Questa nota ricostruisce la settima lezione. Le fonti sono:

- la trascrizione della registrazione (parte 1);
- le note personali «Teoremi» e «Lezione 7 - handwritten»;
- la dispensa italiana del docente (cap. 1, pp. 21–26: teoremi del valore iniziale e finale, considerazioni sul loro uso, regola di Cartesio);
- la dispensa in inglese (§2.2.3, pp. 22–24: *Final value theorem*, *Initial value theorem*, Theorem T/2.2/4).

Con questa lezione si chiude, nelle parole del docente, la fase degli «strumenti» sulla trasformata di Laplace. I due teoremi rispondono alla stessa domanda vista finora, ma agli estremi dell'asse dei tempi. Il **teorema del valore finale** dice come si comporta la funzione dopo moltissimo tempo; il **teorema del valore iniziale** dice come parte, subito dopo l'istante zero. In entrambi i casi la risposta si ottiene senza antitrasformare: se si dovesse antitrasformare, osserva il docente, non si risparmierebbe nulla.

Come nelle lezioni precedenti, un tratto lungo della registrazione coincide con il tempo dato agli studenti per l'esercizio del §3 ed è stato escluso.

## 1. Riepilogo, con una precisazione sul terzo caso

Il docente riprende la regola che lega i poli di una trasformata razionale al comportamento della sua antitrasformata ([[Lezione 05 - Fratti semplici, interpretazione e metodo dei residui#2.2 La regola riassuntiva|lezione 5]]) e ne raffina il terzo caso.

1. **Tutti i poli a parte reale negativa**: la funzione è limitata e tende a zero.
2. **Almeno un polo a parte reale positiva, e/o un polo a parte reale nulla con molteplicità maggiore di 1**: la funzione non è limitata.
3. **Poli a parte reale negativa e poli a parte reale nulla di molteplicità 1**: la funzione è limitata. Qui si distinguono due sottocasi.
   - Se tra i poli a parte reale nulla ci sono poli **sull'asse immaginario con $\omega \neq 0$**, cioè coppie $\pm j\omega$, la funzione contiene seni e coseni: è limitata ma **non ha limite**.
   - Se l'unico polo a parte reale nulla è **un solo polo in $s=0$**, senza parte immaginaria, la funzione non solo è limitata ma **ha un limite**, in generale diverso da zero.

Il docente ribadisce che queste corrispondenze vanno conosciute in modo automatico: poli reali negativi ↔ esponenziali che decrescono, poli puramente immaginari ↔ seni e coseni, polo nell'origine ↔ gradino. Senza questa associazione tutto il resto «è una stupidaggine».

## 2. Il teorema del valore finale

### 2.1 Enunciato, e il verso dell'implicazione

Il docente chiede di scrivere il teorema facendo molta attenzione **al verso delle frecce**. Spesso all'esame viene citato senza sapere se una cosa implica l'altra, se vale il viceversa, se è un «se e solo se».

> [!important] Teorema del valore finale
> Sia $F(s)$ la trasformata di Laplace di $f(t)$.
> $$\text{Se esiste finito}\ \lim_{t\to\infty} f(t) = L, \quad\text{allora}\quad \lim_{s\to0} s\,F(s) = L .$$

L'implicazione va **in un solo verso**. Se si calcola $\lim_{s\to0}sF(s)$ e viene $27$, non si può concludere che $27$ sia il limite della funzione. Si può solo dire che, **se** il limite di $f$ esiste ed è finito, **allora** vale $27$.

> [!example] L'uso sbagliato
> $F(s) = \dfrac{1}{s-2}$ ha antitrasformata $f(t) = e^{2t}$, che tende a $+\infty$: il limite finito non esiste. Eppure
> $$\lim_{s\to0} s\,\frac{1}{s-2} = 0 .$$
> Calcolare prima il limite in $s$ e pretendere che sia il limite nel tempo, senza aver verificato che il teorema si possa applicare, è il modo sbagliato di usarlo.

> [!example] Due usi corretti
> - $F(s) = \dfrac{1}{s+2}$: $f(t) = e^{-2t}$ tende a $0$. Infatti $\lim_{s\to0}\frac{s}{s+2} = 0$.
> - $F(s) = \dfrac{3}{s}$: $f(t) = 3\cdot1(t)$ tende a $3$. Infatti $\lim_{s\to0}s\,\frac{3}{s} = 3$.

### 2.2 Perché funziona: l'interpretazione con i poli

La dispensa riporta una dimostrazione basata sulla proprietà della derivata e sul passaggio al limite sotto il segno di integrale. Il docente la considera valida ma poco istruttiva: «vale quello che vale», e non fa capire il risultato. Preferisce spiegarlo con il legame tra poli e andamento nel tempo. Per noi una trasformata è sempre un rapporto di polinomi $F(s) = N(s)/D(s)$, con $N$ e $D$ primi tra loro; si esaminano i tre casi della regola.

**Tutti i poli a parte reale negativa.** Tutti i fratti dell'espansione corrispondono a funzioni con davanti un esponenziale decrescente. Nella tabella la parte reale del polo, reale o complesso che sia, è sempre il coefficiente di un esponenziale che premoltiplica una potenza del tempo, eventualmente con seno o coseno. Ogni pezzo tende a zero, e la somma di funzioni che tendono a zero tende a zero, che siano due o «un miliardo». Dal lato di $s$: se $D$ ha solo radici a parte reale negativa, $D(0)\neq0$ e quindi $N(0)/D(0)$ è un numero finito. Moltiplicato per $s\to0$, dà $0$. I due limiti coincidono.

**Almeno un polo a parte reale positiva, o un polo a parte reale nulla multiplo.** In questo caso il limite finito di $f(t)$ **non esiste**. L'ipotesi del teorema è falsa e il teorema non dice nulla, qualunque numero dia il limite in $s$. È il caso di $\frac{1}{s-2}$.

**Poli a parte reale negativa e poli a parte reale nulla semplici.** Qui servono i due sottocasi del §1.

- **Un solo polo in $s=0$, gli altri a parte reale negativa.** Si scrive $F(s) = \dfrac{N(s)}{s\,\bar D(s)}$, dove $\bar D$ ha solo radici a parte reale negativa. Espandendo in fratti semplici c'è un fratto $\frac{A}{s}$, che diventa un **gradino** di ampiezza $A$. Tutti gli altri fratti, relativi alle radici di $\bar D$, danno funzioni che tendono a zero. Dopo un po' resta solo il gradino: se la funzione è «$3$ più una marea di esponenziali decrescenti», alla fine arriva a $3$. Il valore di regime è quindi il coefficiente $A$. Ma $A$ si calcola con il metodo dei residui ([[Lezione 05 - Fratti semplici, interpretazione e metodo dei residui#4. Il metodo dei residui|lezione 5]]):
$$A = \lim_{s\to0} s\,F(s) = \frac{N(0)}{\bar D(0)} .$$
Il limite del teorema **è** il residuo del polo nell'origine. Poiché $N$ e $D$ sono primi tra loro, $N(0)\neq0$ e il limite è un numero finito, non nullo.
- **Poli immaginari $\pm j\omega$ semplici, eventualmente anche un polo semplice in $0$.** Il limite $\lim_{s\to0}sF(s)$ si può calcolare e dà un numero. Ma nell'antitrasformata ci sono seni e coseni, e il limite di $f(t)$ non esiste. Il numero trovato è ancora il coefficiente del gradino, cioè il **valore medio** attorno al quale la funzione oscilla. Non è il limite, perché il limite non c'è.

> [!important] Che cosa calcola davvero $\lim_{s\to0}sF(s)$
> Per una trasformata razionale con al più un polo semplice nell'origine, $\lim_{s\to0}sF(s)$ è il **coefficiente del gradino** nell'antitrasformata, cioè il residuo del polo $s=0$; vale zero se il polo nell'origine non c'è. Che questo numero sia anche il limite di $f(t)$ per $t\to\infty$ **dipende da tutti gli altri poli**.
> $$\lim_{s\to0}sF(s) = \lim_{t\to\infty}f(t) \iff \begin{cases}\text{tutti i poli hanno parte reale negativa (e i due limiti valgono } 0\text{), oppure}\\ \text{c'è un solo polo semplice in } s=0 \text{ e tutti gli altri hanno parte reale negativa.}\end{cases}$$
> In questa forma, con il «se e solo se», il risultato è riportato nella dispensa in inglese come corollario C/2.2/1.

> [!warning] Nota personale «Teoremi»
> Lo schema dei casi nella nota è corretto nella sostanza; la nota stessa segnala che il caso ★★ va sistemato («non sono condizioni separate»). La sistemazione è quella sopra. Il caso ★ (poli a parte reale negativa più poli a parte reale nulla semplici) si divide in:
> - **almeno una coppia $\pm j\omega$ con $\omega\neq0$** (con o senza polo in $0$): limitata, nessun limite;
> - **un solo polo in $s=0$** e gli altri a parte reale negativa: limite finito, pari a $N(0)/\bar D(0)$.
>
> Le due condizioni di ★★ («un solo polo in $0$» e «radici di $\bar D$ a parte reale negativa») non sono due casi diversi ma due parti della **stessa** condizione.

> [!tip] Un caso particolare dalla dispensa
> La dispensa italiana (p. 25) osserva che il discorso vale per trasformate senza fattori $e^{-sT}$. Con una traslazione si possono avere sorprese «positive». Ad esempio $F(s) = F_1(s) - F_1(s)e^{-sT}$ può corrispondere a una $f(t) - f(t-T)$ limitata anche se $f$ da sola non lo è, e allora il teorema si può applicare. Un caso concreto è l'esercizio della [[Lezione 08 - Equazioni differenziali, funzione di trasferimento e risposte#6. Esercizio — risposta a un impulso rettangolare|lezione 8]].

## 3. Esercizio: studio parametrico senza antitrasformare

### 3.1 Il testo

Il docente propone un esercizio «relativamente noioso» ma utile, perché costringe a esplorare tutti i casi possibili. Data

$$F(s) = \frac{1}{(s+a)\,(s^2+bs+c)}, \qquad a,b,c\in\mathbb{R},$$

bisogna:

1. al variare di $a$, $b$, $c$, stabilire la limitatezza dell'antitrasformata **senza antitrasformare**;
2. nei casi in cui ha senso, stabilire se esiste il limite per $t\to\infty$ e verificare che coincida con quello dato dal teorema del valore finale.

> [!warning] Il denominatore nella nota personale
> Nella nota il fattore è scritto $s^2+2bs+c$, mentre nella trascrizione il docente dice «$s^2 + bs + c$». Qui si usa la seconda forma. Con $s^2+2bs+c$ cambiano solo le formule esplicite delle radici e il valore $\frac{1}{2ab}$ del §3.3, che diventa $\frac{1}{ab}$. La formula delle radici nella nota, $-b\pm\sqrt{b^2-4c}$, non è corretta in nessuna delle due versioni: per $s^2+bs+c$ è $\frac{-b\pm\sqrt{b^2-4c}}{2}$, per $s^2+2bs+c$ è $-b\pm\sqrt{b^2-c}$.

### 3.2 Uno strumento: i segni dei coefficienti di un polinomio di secondo grado

Per non calcolare le radici di $s^2+bs+c$ il docente richiama un criterio sui segni dei coefficienti. Avverte che in rete lo si trova spesso formulato solo per le radici **reali**, accompagnato dalla condizione che il discriminante sia positivo. Per i polinomi di secondo grado, però, vale per la **parte reale** delle radici, qualunque sia il discriminante.

> [!important] Regola dei segni per $s^2+bs+c$ (dispensa italiana, «Regola di Cartesio», p. 26)
> Per un polinomio di secondo grado con primo coefficiente positivo e **tutti i coefficienti diversi da zero**, il numero di radici a parte reale positiva è uguale al numero di **variazioni di segno** nella sequenza dei coefficienti $(1, b, c)$.
> In particolare, **condizione necessaria e sufficiente** perché entrambe le radici abbiano parte reale negativa è che i coefficienti abbiano tutti lo stesso segno: $b>0$ e $c>0$.

Esempi: con $b<0$ e $c<0$ la sequenza è $+,-,-$, una variazione e quindi una radice a parte reale positiva. Con $b<0$ e $c>0$ è $+,-,+$, due variazioni e due radici a parte reale positiva. Con $b>0$ e $c<0$ è $+,+,-$, una variazione.

Se un coefficiente è **nullo** la regola non si applica così com'è, ma i casi si studiano a mano. Con $c=0$ si ha $s(s+b)$, cioè una radice nulla e l'altra in $-b$. Con $b=0$ si ha $s^2 + c$: radici $\pm j\sqrt{c}$, immaginarie, se $c>0$; reali opposte $\pm\sqrt{-c}$ se $c<0$.

> [!tip] Verifica della condizione (non svolta a lezione)
> Siano $p_1$, $p_2$ le radici di $s^2+bs+c$. Allora $p_1 + p_2 = -b$ e $p_1p_2 = c$.
> - Se le radici sono **complesse coniugate**, $p_{1,2} = \sigma\pm j\omega$, la parte reale comune è $\sigma = -\frac{b}{2}$, negativa se e solo se $b>0$; in questo caso $c = \sigma^2 + \omega^2 > 0$ automaticamente.
> - Se sono **reali**, sono entrambe negative se e solo se il prodotto è positivo (stesso segno) e la somma è negativa: $c>0$ e $b>0$.
>
> Per gradi superiori al secondo la sola assenza di variazioni di segno è necessaria ma **non** sufficiente. Serve un criterio più completo, il criterio di Routh-Hurwitz, che la dispensa italiana presenta subito dopo (pp. 26–27).

### 3.3 La soluzione caso per caso

I poli di $F$ sono $s=-a$ e le due radici di $s^2+bs+c$.

**Caso $a<0$.** Il polo $-a$ è reale positivo. Qualunque siano $b$ e $c$, l'antitrasformata contiene un esponenziale crescente: **non limitata**, nessun limite.

**Caso $a\ge0$ con $b<0$ oppure $c<0$.** Per la regola dei segni il fattore di secondo grado ha almeno una radice a parte reale positiva, oppure (se $c<0$ e $b=0$) una radice reale positiva: **non limitata**. Restano i casi $a\ge0$, $b\ge0$, $c\ge0$.

**Caso $a>0$** (polo $-a$ negativo):

| $b$, $c$ | Poli del fattore quadratico | Antitrasformata | Valore finale |
| :--- | :--- | :--- | :--- |
| $b>0$, $c>0$ | due poli a parte reale negativa | limitata, $\to 0$ | $\lim sF = 0 = \lim f$ |
| $b=0$, $c>0$ | $\pm j\sqrt c$ semplici | limitata, oscilla, **nessun limite** | $\lim sF = 0$ ma non è il limite |
| $b>0$, $c=0$ | $0$ semplice e $-b$ | limitata, ha limite | $\lim f = \lim_{s\to0}\frac{1}{(s+a)(s+b)} = \frac{1}{ab}$ |
| $b=0$, $c=0$ | $0$ doppio | **non limitata** (rampa) | il teorema non si applica |

**Caso $a=0$** (polo in $0$ dovuto al primo fattore):

| $b$, $c$ | Poli | Antitrasformata | Valore finale |
| :--- | :--- | :--- | :--- |
| $b>0$, $c>0$ | $0$ semplice, due a parte reale negativa | limitata, ha limite | $\lim f = \lim_{s\to0}\frac{1}{s^2+bs+c} = \frac{1}{c}$ |
| $b=0$, $c>0$ | $0$ semplice e $\pm j\sqrt c$ semplici | limitata, **nessun limite** | $\lim sF = \frac{1}{c}$ è il **valore medio** dell'oscillazione |
| $b>0$, $c=0$ | $0$ doppio e $-b$ | **non limitata** | il teorema non si applica |
| $b=0$, $c=0$ | $0$ triplo | **non limitata** | il teorema non si applica |

Il docente si sofferma su due righe.

- **$a=0$, $b=0$, $c>0$.** C'è un polo nell'origine e una coppia di poli immaginari, quindi una parte costante più seni e coseni. La funzione è limitata ma non ha limite. Questo non significa che la parte costante non ci sia: le oscillazioni avvengono non attorno a zero ma attorno alla parte costante. Il numero $\lim_{s\to0}sF(s) = \frac{1}{c}$ è proprio quella costante, il coefficiente del gradino.
- **$a=0$, $b>0$, $c=0$.** Il polo nell'origine è doppio, quindi non c'è nemmeno un limite finito e non c'è niente da calcolare. Anche se, in combinazioni come questa, il calcolo può dare l'impressione che «le cose tornino», non lo si può fare.

> [!warning] Nota personale «Teoremi»: alcuni casi
> - Per $a>0$ la nota indica «$b$ & $c<0$: $\exists$ lim», e per $a=0$ «$b$ & $c<0$: $\exists$ lim $=\frac{1}{c}$». Con $b$ o $c$ negativi c'è almeno una variazione di segno e quindi una radice a parte reale positiva: il limite **non** esiste. Con ogni probabilità si intendeva $b,c>0$, come nella riga successiva.
> - Il valore $\frac{1}{2ab}$ per $a>0$, $b>0$, $c=0$ corrisponde al denominatore $s^2+2bs+c$; con $s^2+bs+c$ è $\frac{1}{ab}$.
> - Per $a>0$, $b=c=0$ la riga manca: il polo doppio nell'origine rende la funzione non limitata.

## 4. Il teorema del valore iniziale

### 4.1 Enunciato

> [!important] Teorema del valore iniziale
> $$\text{Se esiste finito}\ \lim_{s\to\infty} s\,F(s) = L, \quad\text{allora}\quad f(0^+) = L .$$

Qui l'ipotesi riguarda il dominio di $s$ e si verifica direttamente sulla trasformata: se il calcolo dà un numero, si è sicuri che la funzione parte da quel valore. Il valore è in $0^+$, cioè «subito dopo» lo zero, quando eventuali impulsi nell'origine si sono già esauriti.

### 4.2 Quando il limite esiste

Quando l'argomento di un rapporto di funzioni va all'infinito e numeratore e denominatore vanno entrambi all'infinito, comanda quella che ci va più velocemente. Per i polinomi comanda il termine di grado più alto. Per $F = N/D$ con $\deg N = m$ e $\deg D = n$:

- $sF(s)$ ha al numeratore un polinomio di grado $m+1$. Perché il limite sia **finito** deve essere $m+1\le n$, cioè $n \ge m+1$: il denominatore deve avere grado **maggiore** del numeratore. $F$ deve quindi essere strettamente propria;
- se $n = m+1$, i gradi di $sN$ e $D$ coincidono e il limite è il **rapporto dei coefficienti di grado massimo**: $f(0^+) = b_m$ (con $D$ monico). Basta dividere sopra e sotto per la potenza massima;
- se $n > m+1$, il limite è $0$: $f(0^+) = 0$.

### 4.3 L'interpretazione: la divisione «infinita» e la serie di Maclaurin

Anche qui il docente preferisce un'interpretazione alla dimostrazione integrale. L'idea è la **divisione lunga** tra polinomi, condotta a partire dalle potenze più alte. Se il resto non diventa mai zero, la divisione non finisce mai: si può continuare a dividere quanto si vuole. Con $\deg N < \deg D$ il risultato contiene solo potenze negative di $s$:

$$F(s) = \frac{N(s)}{D(s)} = \frac{c_1}{s} + \frac{c_2}{s^2} + \frac{c_3}{s^3} + \dots = \sum_{i=1}^{\infty}\frac{c_i}{s^i} .$$

Ogni termine $\frac{1}{s^i}$ è la trasformata di un impulso di ordine negativo, $\frac{t^{i-1}}{(i-1)!}$ (per $t\ge0$). Per linearità, anche se la somma è infinita,

$$f(t) = \sum_{i=1}^{\infty} c_i\,\frac{t^{i-1}}{(i-1)!} .$$

Questa è esattamente la **serie di Maclaurin** di $f$, cioè la serie di Taylor attorno a zero, $\sum_k f^{(k)}(0^+)\frac{t^k}{k!}$. Confrontando i coefficienti:

$$c_i = f^{(i-1)}(0^+) .$$

> [!important] Valori iniziali di tutte le derivate (dispensa inglese, Theorem T/2.2/4)
> Se $F(s) = N(s)/D(s)$ con $\deg N < \deg D$, i coefficienti della divisione lunga di $N$ per $D$ sono i valori in $0^+$ della funzione e delle sue derivate:
> $$c_1 = f(0^+), \quad c_2 = \dot f(0^+), \quad c_3 = \ddot f(0^+), \quad \dots$$
> Il teorema del valore iniziale è il caso banale in cui si pesca soltanto il primo coefficiente: $\lim_{s\to\infty}sF(s) = c_1$.

Con un pezzo di divisione, fermandosi dove si vuole, si conoscono il valore iniziale e anche la derivata prima, la seconda, la terza, e così via.

### 4.4 Il grado relativo

La differenza $n-m$ tra i gradi di denominatore e numeratore si chiama **grado relativo**. Nella divisione il primo termine è $\frac{b_m}{s^{\,n-m}}$, quindi i coefficienti $c_1,\dots,c_{n-m-1}$ sono nulli e il primo diverso da zero è $c_{n-m}$:

$$f(0^+) = \dot f(0^+) = \dots = f^{(n-m-2)}(0^+) = 0, \qquad f^{(n-m-1)}(0^+) = b_m \neq 0 .$$

Più alto è il grado relativo, più la funzione parte «dolcemente»: ha un numero maggiore di derivate nulle nell'istante iniziale.

### 4.5 Esempio svolto a lezione

> [!example] $F(s) = \dfrac{1}{s(s+1)} = \dfrac{1}{s^2+s}$
> **Divisione lunga.** $1 \div (s^2+s)$: il primo quoziente è $\frac{1}{s^2}$; il resto $1 - \frac{1}{s^2}(s^2+s) = -\frac{1}{s}$ dà il quoziente $-\frac{1}{s^3}$, e così via:
> $$\frac{1}{s^2+s} = \frac{0}{s} + \frac{1}{s^2} - \frac{1}{s^3} + \frac{1}{s^4} - \dots$$
> Quindi $f(0^+) = 0$, $\dot f(0^+) = 1$, $\ddot f(0^+) = -1$. Il grado relativo è $2$: la funzione parte da zero, con derivata prima diversa da zero.
>
> **Valore finale.** I poli sono $0$ (semplice) e $-1$: siamo nel caso in cui il teorema si applica, e $\lim_{t\to\infty}f(t) = \lim_{s\to0}\frac{1}{s+1} = 1$. «L'oracolo degli oracoli» dice quindi che la funzione parte da $0$ e tende a $1$.
>
> **Verifica antitrasformando.** Con i residui, $\frac{1}{s(s+1)} = \frac{A}{s} + \frac{B}{s+1}$ con $A = \lim_{s\to0}\frac{1}{s+1} = 1$ (lo stesso conto del valore finale) e $B = \lim_{s\to-1}\frac{1}{s} = -1$:
> $$f(t) = \big(1 - e^{-t}\big)\,1(t).$$
> Derivando con le funzioni generalizzate:
> $$\dot f(t) = e^{-t}\,1(t) + \big(1-e^{-t}\big)\,\delta(t) = e^{-t}\,1(t),$$
> perché per il campionamento $(1-e^{-t})\delta(t) = (1-1)\,\delta(t) = 0$. Quindi $\dot f(0^+) = 1$. Derivando ancora:
> $$\ddot f(t) = -e^{-t}\,1(t) + e^{-t}\,\delta(t) = -e^{-t}\,1(t) + \delta(t).$$
> In $0^+$ l'impulso «è già bell'e finito», quindi $\ddot f(0^+) = -1$. Tutto coincide con la divisione.

### 4.6 Se la trasformata non è strettamente propria

Se il grado del numeratore è maggiore o uguale a quello del denominatore, $\lim_{s\to\infty}sF(s)$ è infinito e il teorema non dice nulla. In quel caso si fa prima la divisione «normale», fino al primo resto di grado inferiore al divisore. I termini senza denominatore sono impulsi di ordine $\ge0$, concentrati nell'origine, che in $0^+$ sono già esauriti e non danno alcun contributo né alla funzione né alle sue derivate. Si applica il teorema, o la divisione lunga, solo alla parte strettamente propria.

> [!example] Dispensa italiana, Esempio PM 9 (p. 22)
> $$F(s) = \frac{s}{s+1} = 1 - \frac{1}{s+1} \qquad\Longrightarrow\qquad f(t) = \delta(t) - e^{-t}\,1(t).$$
> Il termine $1$ è l'impulso, che in $0^+$ non c'è più. Applicando il teorema al solo resto: $f(0^+) = \lim_{s\to\infty} s\cdot\frac{-1}{s+1} = -1$, in accordo con $-e^{-0}$.

> [!example] Dispensa inglese, Esempio E/2.2/9
> Per $F(s) = \dfrac{s^2+3}{s^3+5s^2+4s}$ (grado relativo $1$) la divisione lunga dà
> $$F(s) = \frac{1}{s} - \frac{5}{s^2} + \frac{24}{s^3} - \dots \quad\Longrightarrow\quad f(0^+) = 1,\ \ \dot f(0^+) = -5,\ \ \ddot f(0^+) = 24 .$$
> Con $F(s) = \dfrac{s^2+3}{s^4+5s^3+4s^2}$ (grado relativo $2$) si ottengono gli stessi numeri spostati di un posto: $f(0^+) = 0$, $\dot f(0^+) = 1$, $\ddot f(0^+) = -5$, $\dddot f(0^+) = 24$.

> [!warning] Esempi non ricostruibili
> Durante la lezione il docente ha svolto altri esempi di divisione lunga, uno con coefficienti $c_1 = 1$, $c_2 = 3$, $c_3 = 5$, … e uno con una trasformata non strettamente propria. Dalla registrazione non si ricavano le funzioni di partenza, e non sono stati inventati. Gli esempi delle dispense sopra illustrano gli stessi due meccanismi.

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. *Perché $\lim_{s\to0}s\,\frac{1}{s-2} = 0$ non dice che $e^{2t}$ tende a zero?* Il teorema richiede come ipotesi che il limite finito di $f$ esista; con un polo a parte reale positiva non esiste.
2. *Che cosa si calcola con $\lim_{s\to0}sF(s)$ quando c'è un polo semplice nell'origine?* Il residuo di quel polo, cioè il coefficiente del gradino nell'antitrasformata. È il limite di $f$ solo se tutti gli altri poli hanno parte reale negativa.
3. *Perché con poli $\pm j\omega$ semplici il teorema del valore finale non si applica, anche se la funzione è limitata?* L'antitrasformata contiene seni e coseni che non si smorzano: la funzione non ha limite. $\lim sF$ dà solo il valore medio dell'oscillazione.
4. *Quando $s^2+bs+c$ ha entrambe le radici a parte reale negativa?* Se e solo se $b>0$ e $c>0$, anche quando il discriminante è negativo.
5. *Perché il teorema del valore iniziale richiede che il denominatore abbia grado maggiore del numeratore?* Altrimenti $sF(s)$ ha al numeratore un polinomio di grado almeno pari a quello del denominatore, e il limite per $s\to\infty$ è infinito.
6. *Perché i coefficienti della divisione lunga sono le derivate in $0^+$?* Ogni $\frac{1}{s^i}$ antitrasforma in $\frac{t^{i-1}}{(i-1)!}$, quindi la divisione produce la serie di Maclaurin di $f$.
7. *Perché gli impulsi nell'origine non influenzano $f(0^+)$?* Sono concentrati in $t=0$: in $0^+$ sono già esauriti.
