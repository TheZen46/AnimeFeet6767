---
corso: Teoria dei Sistemi
lezione: 12
data: 2026-11-05
argomenti: [esercitazione, equazione differenziale con derivata dell'ingresso, ingresso a tratti, due metodi di soluzione, equazioni di stato con ingresso impulsivo, condizioni iniziali che annullano lo stato, matrici diagonali a blocchi, polinomi di controllo per singolo ingresso]
fonti: [trascrizione parte 1, appunti manuali]
tags: [teoria-dei-sistemi, lezione, esercitazione]
---

# Lezione 12 — Esercizi sulle equazioni di stato e polinomi di controllo

Questa nota ricostruisce la dodicesima lezione, interamente dedicata agli esercizi. Le fonti sono la trascrizione della registrazione (parte 1) e gli appunti a mano «Lezione 12» (PDF, due pagine), che riportano testi e passaggi dei tre esercizi.

Gran parte della registrazione coincide con il tempo lasciato agli studenti per risolvere da soli e contiene solo rumore o conversazioni estranee, escluse da questi appunti. I testi degli esercizi provengono dagli appunti a mano, che in questo caso sono la fonte più completa. Tutti i risultati sono stati verificati con il calcolo simbolico.

Il docente apre la lezione accennando ai «tre argomenti fondamentali» che intende affrontare; alla fine della lezione ne nomina due, la **stabilità** e la **controllabilità**. Gli esercizi servono a prendere confidenza con gli strumenti, a partire dalla [[Lezione 08 - Equazioni differenziali, funzione di trasferimento e risposte|lezione 8]] fino alla [[Lezione 11 - Polinomio caratteristico e polinomio minimo|lezione 11]].

## 1. Esercizio: un'equazione con la derivata dell'ingresso

### 1.1 Testo

> [!example] Testo
> $$\dot y + 2y = \dot u, \qquad y(0^-) = 0,$$
> con l'ingresso $u(t)$ che vale $0$ per $t<0$, scende linearmente da $2$ a $1$ tra $t=0$ e $t=1$, e vale $1$ da $t=1$ in poi.
>
> Risolvere in due modi:
> 1. con la trasformata di Laplace, tramite la funzione di trasferimento e $U(s)$;
> 2. calcolando prima $\dot u(t)$, sostituendola nell'equazione e risolvendo di nuovo con la trasformata, applicando la sovrapposizione degli effetti.

```chart
type: line
labels: [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
series:
  - title: "ingresso u(t)"
    data: [2, 1.75, 1.5, 1.25, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  - title: "uscita y(t)"
    data: [2.0, 1.016, 0.42, 0.058, -0.162, -0.098, -0.059, -0.036, -0.022, -0.013, -0.008, -0.005, -0.003]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: false
```

Il grafico mostra la soluzione trovata nel §1.4. Il punto in $t=0$ è il valore in $0^+$: in $0^-$ sia l'ingresso sia l'uscita valgono zero.

### 1.2 La funzione di trasferimento

Con condizioni iniziali nulle, della soluzione generale resta solo la risposta nello stato zero, $Y(s) = T(s)\,U(s)$. Il docente ricorda come si legge la funzione di trasferimento direttamente dall'equazione: ogni punto (ogni derivata) diventa una potenza di $s$, con lo stesso coefficiente. A denominatore c'è il polinomio caratteristico della parte in $y$, a numeratore il polinomio della parte in $u$:

$$T(s) = \frac{s}{s+2} .$$

È **propria** e non strettamente propria: numeratore e denominatore hanno lo stesso grado.

> [!warning] Una giustificazione negli appunti a mano
> Negli appunti si scrive «$y(0^-) = 0 \Rightarrow u(0^-) = 0$». Il valore $u(0^-) = 0$ è corretto, ma la ragione è un'altra: $u$ è nullo prima dell'istante iniziale, perché l'ingresso viene applicato da $0$ in avanti. Le condizioni iniziali dell'ingresso non dipendono da quelle dell'uscita.

### 1.3 L'ingresso con le finestre

Ci sono due tratti, quindi due «finestrelle»: una tra $0$ e $1$, lunga $1$, e una da $1$ a $+\infty$. Il docente insiste che la finestra non dipende dalla funzione che inquadra: la finestra vale $1$ nel suo intervallo, e in quell'intervallo la funzione è quella che si moltiplica.

- Tra $0$ e $1$ c'è una retta con coefficiente angolare $-1$ che parte da $2$: $2 - t$.
- Da $1$ in poi c'è la costante $1$. A rigore la finestra sarebbe $1(t-1) - 1(t-\infty)$, ma $1(t-\infty)$ è sempre zero (il suo argomento non diventa mai positivo), quindi resta $1(t-1)$.

$$u(t) = (2-t)\big[1(t) - 1(t-1)\big] + 1(t-1) = 2\cdot1(t) - 2\cdot1(t-1) - t\cdot1(t) + t\cdot1(t-1) + 1(t-1) .$$

Per trasformare, ogni pezzo deve avere una forma a cui si applicano le proprietà. Il termine $t\cdot1(t-1)$ non va bene: il tempo compare come $t$ e non come $t-1$. Si aggiunge e si toglie $1$, come nella [[Lezione 03 - Trasformate notevoli, poli e andamento nel tempo|lezione 3]]: $t\cdot1(t-1) = (t-1)\,1(t-1) + 1(t-1)$. Raccogliendo i gradini traslati, $-2 + 1 + 1 = 0$, e resta

$$u(t) = 2\cdot1(t) - t\cdot1(t) + (t-1)\,1(t-1) .$$

È formata da un gradino di ampiezza $2$, una rampa con segno meno e una rampa traslata in $1$:

$$U(s) = \frac{2}{s} - \frac{1}{s^2} + \frac{e^{-s}}{s^2} .$$

### 1.4 Primo metodo

$$Y(s) = \frac{s}{s+2}\,U(s) = \frac{2}{s+2} - \frac{1}{s(s+2)} + \frac{1}{s(s+2)}\,e^{-s} .$$

Il primo termine è già un fratto semplice. Il secondo e il terzo hanno la stessa frazione, e il terzo è solo traslato: basta antitrasformare una volta. $\frac{1}{s(s+2)}$ ha due poli semplici, quindi i coefficienti si trovano con i limiti, senza impostare il sistema:

$$\frac{1}{s(s+2)} = \frac{1/2}{s} - \frac{1/2}{s+2} \qquad\Longrightarrow\qquad \mathcal{L}^{-1}\left\{\frac{1}{s(s+2)}\right\} = \frac{1}{2} - \frac{1}{2}\,e^{-2t} .$$

Quindi

$$y(t) = 2e^{-2t} - \frac{1}{2}\,1(t) + \frac{1}{2}\,e^{-2t} + \Big[\frac{1}{2} - \frac{1}{2}\,e^{-2(t-1)}\Big]1(t-1) .$$

Per intervalli:

- per $0 < t < 1$: $y(t) = \frac{5}{2}\,e^{-2t} - \frac{1}{2}$;
- per $t \ge 1$: $y(t) = \frac{5}{2}\,e^{-2t} - \frac{1}{2}\,e^{-2(t-1)} = \frac{5 - e^2}{2}\,e^{-2t}$.

I due tratti si raccordano con continuità in $t=1$, entrambi a $\frac{5}{2}e^{-2} - \frac{1}{2} \approx -0{,}162$, perché l'ingresso in $t=1$ non salta.

> [!tip] Osservazione (non svolta a lezione): il salto iniziale
> L'uscita parte da $y(0^-) = 0$ ma vale $y(0^+) = \frac{5}{2} - \frac{1}{2} = 2$: salta. È coerente con il fatto che $T(s)$ è propria. Dividendo, $\frac{s}{s+2} = 1 - \frac{2}{s+2}$, quindi l'uscita contiene una copia istantanea dell'ingresso, che in $t=0$ salta da $0$ a $2$. Il teorema del valore iniziale lo conferma: $\lim_{s\to\infty} sY(s) = 2$.

### 1.5 Secondo metodo: prima la derivata

Si calcola $\dot u$ con le regole delle funzioni generalizzate, partendo dalla forma con le finestre:

$$\dot u = 2\delta(t) - 1(t) - t\,\delta(t) + 1(t-1) + (t-1)\,\delta(t-1) .$$

Per la **regola del campionamento** (estesa), una funzione moltiplicata per un impulso di ordine zero si può sostituire con la funzione calcolata nel punto in cui l'impulso esiste. Quindi $t\,\delta(t) = 0\cdot\delta(t) = 0$: un impulso «di area nulla», che non c'è. Allo stesso modo $(t-1)\,\delta(t-1) = 0$. Resta

$$\dot u(t) = 2\,\delta(t) - \big[1(t) - 1(t-1)\big] .$$

Il docente invita a controllare il risultato guardando il grafico di $u$.

- In $t=0$ la funzione salta da $0$ a $2$. L'unico modo per far fare un salto a una funzione è che la sua derivata contenga un impulso: la variazione è l'integrale della derivata, e su un intervallo nullo l'integrale può dare un valore finito solo se c'è un impulso. Qui c'è un impulso di area $2$ con la punta verso l'alto.
- Tra $0$ e $1$ la retta scende con coefficiente $-1$: la derivata vale $-1$, cioè una finestra di ampiezza $1$ con coefficiente $-1$.
- Da $1$ in poi la funzione è costante e la derivata è nulla.

Chiamando $v = \dot u$ il nuovo ingresso, l'equazione diventa $\dot y + 2y = v$, con funzione di trasferimento $\frac{1}{s+2}$ e

$$V(s) = 2 - \frac{1}{s} + \frac{e^{-s}}{s} \qquad\Longrightarrow\qquad Y(s) = \frac{2}{s+2} - \frac{1}{s(s+2)} + \frac{1}{s(s+2)}\,e^{-s},$$

lo stesso risultato del primo metodo, come deve essere. Il motivo è che $\mathcal{L}\{\dot u\} = sU(s) - u(0^-) = sU(s)$, perché $u(0^-) = 0$.

> [!warning] Appunti a mano
> La soluzione e la derivata $\dot u$ riportate negli appunti sono corrette e coincidono con quelle qui sopra.

## 2. Esercizio: equazioni di stato con un ingresso impulsivo

### 2.1 Testo

> [!example] Testo
> $$\dot x = \begin{bmatrix} 0 & 2\\ -2 & 0\end{bmatrix}x + \begin{bmatrix} 1\\ 0\end{bmatrix}u, \qquad y = \begin{bmatrix} 0 & 1\end{bmatrix}x .$$
> 1. Con $u(t) = \delta(t)$ e $x(0^-) = 0$, calcolare $x(t)$ e $y(t)$.
> 2. Se esiste, calcolare uno stato iniziale $x(0^-)$ tale che, con $u(t) = \delta(t)$, sia $x(t) = 0$ per ogni $t>0$.

### 2.2 Primo punto

$$sI - A = \begin{bmatrix} s & -2\\ 2 & s\end{bmatrix}, \qquad \det(sI-A) = s^2 + 4 .$$

Con il trucco per le $2\times2$ (si scambiano gli elementi della diagonale principale, che qui sono uguali, si cambiano di segno gli altri due e si divide per il determinante):

$$(sI-A)^{-1} = \begin{bmatrix} \dfrac{s}{s^2+4} & \dfrac{2}{s^2+4}\\[8pt] -\dfrac{2}{s^2+4} & \dfrac{s}{s^2+4}\end{bmatrix}.$$

Lo stato iniziale è nullo, quindi della soluzione generale resta solo $(sI-A)^{-1}B\,U(s)$. $B = [1\ \ 0]^\top$ seleziona la prima colonna, e $U(s) = 1$:

$$X(s) = \begin{bmatrix} \dfrac{s}{s^2+4}\\[8pt] -\dfrac{2}{s^2+4}\end{bmatrix} \qquad\Longrightarrow\qquad x(t) = \begin{bmatrix} \cos 2t\\ -\sin 2t\end{bmatrix}1(t) .$$

Il docente si era dimenticato l'uscita, e lo ha ricordato più tardi («scusate, non ho calcolato la $y$»). $C = [0\ \ 1]$ seleziona la seconda componente dello stato:

$$Y(s) = C\,(sI-A)^{-1}B\,U(s) = -\frac{2}{s^2+4} \qquad\Longrightarrow\qquad y(t) = -\sin(2t)\,1(t) .$$

I poli del sistema sono $\pm2j$: lo stato oscilla per sempre senza smorzarsi.

### 2.3 Secondo punto

Il docente distingue il «metodo lungo», di chi non sa come vanno le cose e fa tutti i conti fino in fondo, dal «metodo corto», di chi conosce un po' la trasformata. Con il metodo corto si raccoglie $(sI-A)^{-1}$ a sinistra, sempre rispettando l'ordine dei prodotti:

$$X(s) = (sI-A)^{-1}x(0^-) + (sI-A)^{-1}B\,U(s) = (sI-A)^{-1}\big[\,x(0^-) + B\,U(s)\,\big] .$$

Perché $x(t)$ sia identicamente nullo per $t>0$ deve essere nulla la sua trasformata. $(sI-A)^{-1}$ non è la matrice nulla, ed è invertibile per quasi ogni $s$, quindi deve annullarsi il vettore tra parentesi:

$$x(0^-) = -B\,U(s) .$$

> [!important] Le condizioni iniziali sono numeri
> $x(0^-)$ è un vettore di **numeri**: non può dipendere da $s$. La condizione $x(0^-) = -B\,U(s)$ si può soddisfare solo se $U(s)$ **non contiene $s$**, cioè solo se l'ingresso è un impulso (di ordine zero). Con qualunque altro ingresso il problema non ha soluzione.
>
> Il docente insiste perché capita di arrivare a problemi simili per altre strade e di trovare qualcuno che fa dipendere le condizioni iniziali da $s$. Le funzioni hanno una trasformata che dipende dalla variabile complessa; i numeri hanno per trasformata numeri.

Qui $U(s) = 1$, quindi

$$x(0^-) = -B = \begin{bmatrix} -1\\ 0\end{bmatrix} .$$

Con questo stato iniziale l'impulso «azzera» lo stato: sostituendo, tutto si cancella.

> [!warning] Segno negli appunti a mano
> Negli appunti è scritto «$x(0^-) = B = \begin{bmatrix} -1\\ 0\end{bmatrix}$». Il vettore è giusto, ma va scritto $x(0^-) = -B$: con $B = [1\ \ 0]^\top$, $-B = [-1\ \ 0]^\top$. La nota a margine sull'uscita dimenticata è corretta: l'uscita è stata calcolata al §2.2.

> [!tip] Interpretazione (non svolta a lezione)
> Integrando l'equazione di stato su un intervallo infinitesimo attorno a $0$, l'impulso $B\,\delta(t)$ fa **saltare** lo stato: $x(0^+) = x(0^-) + B$. Scegliendo $x(0^-) = -B$, l'impulso porta lo stato esattamente nell'origine, $x(0^+) = 0$. Da lì, con ingresso nullo, il sistema resta fermo, perché l'origine è un equilibrio di $\dot x = Ax$. È lo stesso meccanismo del salto di una funzione e dell'impulso nella sua derivata ([[Lezione 02 - Funzioni generalizzate e trasformata di Laplace|lezione 2]]), applicato a un vettore.

## 3. Esercizio: polinomi di controllo con uno o due ingressi

### 3.1 Testo

> [!example] Testo
> $$\dot x = \begin{bmatrix} -1 & 1 & 0\\ 0 & -2 & 0\\ 0 & 0 & -3\end{bmatrix}x + \begin{bmatrix} 0 & 0\\ 1 & 0\\ 0 & 1\end{bmatrix}u .$$
> Calcolare $\varphi(s)$, $m(s)$, $\varphi_c(s)$, $m_c(s)$ e poi i polinomi di controllo che si avrebbero con **un solo ingresso alla volta**: $\varphi_c^1(s)$, $m_c^1(s)$ (solo il primo) e $\varphi_c^2(s)$, $m_c^2(s)$ (solo il secondo).
>
> Il docente motiva la seconda parte con un'immagine. Il controllo ha due componenti, quindi servirebbero due attuatori. Se il budget ne permette uno solo, quale scegliere? «Adesso non sapete perché vi faccio fare questa cosa, ma fra un mese e mezzo o due lo saprete.»

### 3.2 L'inversa: matrici diagonali a blocchi

Il docente raccomanda di «guardare bene la matrice negli occhi» prima di invertire. $A$ è **diagonale a blocchi**: un blocco $2\times2$ in alto a sinistra e un blocco $1\times1$ in basso a destra, con zeri fuori dai blocchi. Allora anche $sI-A$ è diagonale a blocchi.

> [!important] Inversa di una matrice diagonale a blocchi
> L'inversa di una matrice diagonale a blocchi è diagonale a blocchi, con sulla diagonale **le inverse dei blocchi**. Non si inverte una $3\times3$: si invertono una $2\times2$ e una $1\times1$.

$$sI - A = \begin{bmatrix} s+1 & -1 & 0\\ 0 & s+2 & 0\\ 0 & 0 & s+3\end{bmatrix}.$$

Il blocco $2\times2$ si inverte con il trucco (si scambiano gli elementi diagonali, si cambia segno agli altri, si divide per il determinante $(s+1)(s+2)$); il blocco $1\times1$ si inverte direttamente:

$$(sI-A)^{-1} = \begin{bmatrix} \dfrac{1}{s+1} & \dfrac{1}{(s+1)(s+2)} & 0\\[8pt] 0 & \dfrac{1}{s+2} & 0\\[4pt] 0 & 0 & \dfrac{1}{s+3}\end{bmatrix}.$$

### 3.3 Sistema e controllo con entrambi gli ingressi

**Polinomi del sistema.** $A$ è triangolare superiore, quindi $\varphi(s) = (s+1)(s+2)(s+3)$, prodotto degli elementi diagonali. Il polinomio minimo, minimo comune multiplo dei denominatori non nulli di $(sI-A)^{-1}$, è $(s+1)(s+2)(s+3)$. Coincide con $\varphi$, e non può essere altrimenti: $m$ ha le stesse radici di $\varphi$, e qui le radici di $\varphi$ sono semplici.

**Polinomi di controllo.** $(sI-A)^{-1}B$ ha tante righe quante $(sI-A)^{-1}$ e tante colonne quante $B$. Le colonne di $B$ selezionano la seconda e la terza colonna di $(sI-A)^{-1}$:

$$(sI-A)^{-1}B = \begin{bmatrix} \dfrac{1}{(s+1)(s+2)} & 0\\[8pt] \dfrac{1}{s+2} & 0\\[4pt] 0 & \dfrac{1}{s+3}\end{bmatrix}.$$

- $m_c(s)$: minimo comune multiplo dei denominatori non nulli, $(s+1)(s+2)(s+3)$.
- $\varphi_c(s)$: oltre agli elementi servono le tre sottomatrici $2\times2$. Righe 1 e 2: determinante nullo (la seconda colonna è nulla). Righe 1 e 3: $\frac{1}{(s+1)(s+2)(s+3)}$. Righe 2 e 3: $\frac{1}{(s+2)(s+3)}$. Quindi $\varphi_c(s) = (s+1)(s+2)(s+3)$.

Con entrambi gli ingressi, tutti i polinomi coincidono con quello del sistema.

### 3.4 Un ingresso alla volta

Avere solo il primo ingresso significa considerare solo la prima colonna di $B$, quindi solo la prima colonna di $(sI-A)^{-1}B$; lo stesso per il secondo. Sono matrici colonna, quindi caratteristico e minimo coincidono.

$$\text{solo } u_1:\quad \begin{bmatrix} \frac{1}{(s+1)(s+2)}\\ \frac{1}{s+2}\\ 0\end{bmatrix} \ \Rightarrow\ \varphi_c^1(s) = m_c^1(s) = (s+1)(s+2),$$

$$\text{solo } u_2:\quad \begin{bmatrix} 0\\ 0\\ \frac{1}{s+3}\end{bmatrix} \ \Rightarrow\ \varphi_c^2(s) = m_c^2(s) = s+3 .$$

Entrambi sono fattori di $\varphi_c$, come previsto dai contenimenti della lezione 11. Ciascuno dei due ingressi da solo «vede» solo una parte del sistema:

- il primo ingresso agisce sulla seconda variabile di stato e, attraverso il termine $1$ in $A$, sulla prima, ma non raggiunge mai la terza: il polo $-3$ manca;
- il secondo agisce solo sulla terza variabile, e mancano i poli $-1$ e $-2$.

Messi insieme, i due ingressi ricostruiscono il polinomio completo: «un pezzo alla volta vi devono dare quello di prima».

> [!tip] Collegamento con il seguito del corso
> Il docente chiude dicendo che questi calcoli sono intrinsecamente legati a una delle proprietà fondamentali: dopo la stabilità, la **controllabilità**. È la domanda «avete un sistema, volete fargli fare qualcosa con i controlli che avete a disposizione: che cosa riuscite a fargli fare?». La prossima lezione riprenderà la stabilità.

> [!warning] Appunti a mano
> I calcoli degli appunti sono corretti. Due piccole note:
> - manca il polinomio $\varphi_c(s)$, che vale anch'esso $(s+1)(s+2)(s+3)$;
> - nella riga di $m_c^1$ l'apice di $\varphi_c$ è scritto come un apostrofo ($\varphi_c'$), che può confondersi con una derivata: va letto $\varphi_c^1$.

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. *Come si legge la funzione di trasferimento da $\dot y + 2y = \dot u$?* Ogni derivata diventa una potenza di $s$ con lo stesso coefficiente: $(s+2)Y = sU$, quindi $T(s) = \frac{s}{s+2}$.
2. *Perché $t\cdot1(t-1)$ va riscritto prima di trasformarlo?* La proprietà di traslazione richiede che il tempo compaia ovunque come $t-1$: $t\cdot1(t-1) = (t-1)1(t-1) + 1(t-1)$.
3. *Perché $t\,\delta(t)$ si può eliminare?* Per il campionamento vale $0\cdot\delta(t)$, cioè nulla.
4. *Perché i due metodi del primo esercizio danno lo stesso risultato?* $\mathcal{L}\{\dot u\} = sU(s) - u(0^-)$ e $u(0^-) = 0$: sostituire $\dot u$ o moltiplicare $U$ per $s$ è la stessa cosa.
5. *Perché lo stato si può azzerare con un impulso ma non con un gradino?* Bisogna avere $x(0^-) = -BU(s)$, e le condizioni iniziali sono numeri: serve un $U(s)$ costante, cioè un impulso.
6. *Come si inverte una matrice diagonale a blocchi?* Invertendo i blocchi uno per uno e lasciandoli al loro posto.
7. *Perché con il solo secondo ingresso il polinomio di controllo è $s+3$?* Quell'ingresso agisce solo sulla terza variabile di stato, che non interagisce con le altre: il controllo «vede» solo il polo $-3$.
