---
corso: Teoria dei Sistemi
lezione: 9
data: 2026-10-28
argomenti: [cancellazioni nella funzione di trasferimento, cancellazioni nella risposta libera, la funzione di trasferimento non è il sistema, proprietà strutturali, stabilità BIBO, teorema sui poli della funzione di trasferimento, ingresso che rende limitata l'uscita di un sistema instabile, risposta a regime a un ingresso sinusoidale, risposta in frequenza, criterio di Routh]
fonti: [trascrizione parte 1, dispensa del docente (inglese), dispensa del docente (italiano)]
tags: [teoria-dei-sistemi, lezione]
---

# Lezione 9 — Stabilità BIBO e criterio di Routh

Questa nota ricostruisce la nona lezione. Le fonti sono:

- la trascrizione della registrazione (parte 1);
- la dispensa in inglese del docente (cap. 3: introduzione, §3.1 *BIBO Stability for SISO systems*, criterio di Routh, pp. 25–30);
- la dispensa italiana (cap. 1, «Metodo di Routh-Hurwitz», pp. 26–27).

Per questa lezione non sono stati forniti appunti personali. La registrazione è di qualità inferiore alle precedenti: in molti tratti le formule dettate non si ricostruiscono parola per parola. Dove è stato necessario, gli esempi sono stati ricostruiti dai passaggi udibili e dalla dispensa, e i completamenti sono segnalati.

La lezione introduce la prima **proprietà strutturale** di un sistema, la **stabilità BIBO**. La lega ai poli della funzione di trasferimento, ne ricava il significato della risposta a un ingresso sinusoidale e presenta il **criterio di Routh**, per verificarla senza calcolare le radici.

## 1. Riepilogo e cancellazioni

### 1.1 La soluzione nel dominio di $s$

Nella [[Lezione 08 - Equazioni differenziali, funzione di trasferimento e risposte|lezione 8]] si è trovato che la soluzione di un'equazione differenziale lineare a coefficienti costanti, nel dominio di $s$, è

$$Y(s) = \underbrace{\frac{N_u(s)}{D_y(s)}\,U(s)}_{\text{risposta nello stato zero}} + \underbrace{\frac{Z(s)}{D_y(s)}}_{\text{risposta a ingresso nullo}} .$$

- $D_y(s)$ è il **polinomio caratteristico** dell'equazione differenziale, cioè il polinomio dei coefficienti dell'uscita.
- $N_u(s)$ è il polinomio dei coefficienti dell'ingresso.
- $Z(s)$ è un polinomio omogeneo nelle condizioni iniziali di $y$ e di $u$: è nullo se tutte le condizioni iniziali sono nulle.

Per linearità i due addendi sono contributi distinti, ciascuno generato da un tipo di causa.

### 1.2 Due tipi di semplificazione

I rapporti di polinomi vanno sempre ridotti ai minimi termini: se numeratore e denominatore hanno radici comuni, si semplificano. Il docente fa notare che le semplificazioni nei due addendi hanno natura diversa.

- Nella **funzione di trasferimento** $\frac{N_u(s)}{D_y(s)}$ entrambi i polinomi dipendono soltanto dai coefficienti dell'equazione. Se c'è una semplificazione, c'è **sempre**, qualunque siano le condizioni iniziali: è una proprietà dell'equazione.
- Nella **risposta a ingresso nullo** $\frac{Z(s)}{D_y(s)}$ il numeratore dipende dalle condizioni iniziali. Una semplificazione può esserci o no a seconda di come sono scelte: non è una proprietà dell'equazione, ma del caso particolare.

> [!example] $\ddot y + 2\dot y + y = \dot u + u$
> Rispetto alla forma generale: $n = 2$, $m = 1$, $a_1 = 2$, $a_0 = 1$, $b_1 = 1$, $b_0 = 1$.
>
> **Funzione di trasferimento.** Il polinomio caratteristico è $s^2 + 2s + 1 = (s+1)^2$ e il numeratore è $s+1$. La semplificazione c'è sempre:
> $$T(s) = \frac{s+1}{(s+1)^2} = \frac{1}{s+1} .$$
>
> **Risposta a ingresso nullo.** Trasformando entrambi i membri con le condizioni iniziali:
> $$s^2Y - s\,y(0^-) - \dot y(0^-) + 2\big(sY - y(0^-)\big) + Y = sU - u(0^-) + U,$$
> $$(s+1)^2\,Y(s) = (s+1)\,U(s) + \underbrace{s\,y(0^-) + \dot y(0^-) + 2y(0^-) - u(0^-)}_{Z(s)} .$$
> Il polinomio $Z(s)$ si può riscrivere come $Z(s) = y(0^-)\,(s+1) + \big[\,y(0^-) + \dot y(0^-) - u(0^-)\,\big]$. Si semplifica con un fattore $(s+1)$ del denominatore se e solo se $Z(-1) = 0$, cioè
> $$y(0^-) + \dot y(0^-) - u(0^-) = 0 .$$
> Con condizioni iniziali generiche non c'è nessuna semplificazione; con condizioni scelte in modo particolare sì.
>
> Nella registrazione il docente mostra un caso in cui la semplificazione avviene e uno in cui non avviene, ma i valori numerici non si sentono. La condizione generale riportata qui è stata ricavata dal calcolo.

### 1.3 La funzione di trasferimento non è il sistema

Il docente insiste su un punto che tornerà spesso, perché anche lui, avverte, a volte dirà frasi come «il sistema $T(s)$», e più avanti spiegherà quando lo si può dire. La funzione di trasferimento **non descrive** il sistema. Fa il suo mestiere: è un operatore che mette in relazione la trasformata dell'ingresso con quella dell'uscita, a partire da condizioni iniziali nulle. È un pezzo del sistema, una sua particolare «fotografia».

La dimostrazione è che esistono equazioni differenziali diverse, quindi sistemi diversi, con la stessa funzione di trasferimento.

> [!example] Stessa funzione di trasferimento, sistemi diversi
> L'esempio dettato a lezione non è ricostruibile dalla registrazione. Quello del §1.2 basta a illustrare il concetto:
> $$\ddot y + 2\dot y + y = \dot u + u \qquad\text{e}\qquad \dot y + y = u$$
> hanno entrambe $T(s) = \frac{1}{s+1}$. Sono però equazioni diverse: la prima è del secondo ordine, richiede due condizioni iniziali sull'uscita e ha risposte libere del tipo $(c_1 + c_2t)e^{-t}$; la seconda è del primo ordine e ha solo $c\,e^{-t}$.

Ci sono condizioni sotto le quali una funzione di trasferimento, o una matrice di trasferimento, rappresenta davvero tutto il sistema. Per capire quando, però, serve la teoria che verrà sviluppata nel resto del corso.

## 2. La stabilità BIBO

### 2.1 Definizione

La prima **proprietà strutturale**, cioè una proprietà che dipende dalla struttura del sistema e non da un particolare esperimento, è la stabilità **BIBO** (*Bounded Input, Bounded Output*: ingresso limitato, uscita limitata).

> [!important] Stabilità BIBO (dispensa inglese, D/3.1/1)
> Un sistema è **stabile BIBO** se, partendo da condizioni iniziali nulle, **qualunque** ingresso limitato produce un'uscita limitata.

Anche qui il docente raccomanda attenzione alla logica, come per il teorema del valore finale. La negazione della definizione **non** è «ogni ingresso limitato produce un'uscita illimitata». È: **esiste almeno un** ingresso limitato che produce un'uscita illimitata. Come in teoria degli insiemi, negare un «per ogni» dà un «esiste almeno uno».

> [!example] Il caso banale: un sistema algebrico
> Si consideri $y(t) = k\,u(t)$. Non è un'equazione differenziale ma una relazione algebrica: un moltiplicatore, che, come detto nella prima lezione, non ricorda quante moltiplicazioni abbia fatto nella vita. Se $u$ è limitata, $|u(t)|\le M$, allora $|y(t)| \le |k|\,M$: il sistema è stabile BIBO.
>
> Trasformando: $Y(s) = k\,U(s)$, quindi $T(s) = k$. Una funzione di trasferimento costante, senza poli né zeri, rappresenta un sistema stabile BIBO.

### 2.2 Il teorema: stabilità BIBO e poli della funzione di trasferimento

> [!important] Teorema (dispensa inglese, T/3.1/2)
> Un sistema con funzione di trasferimento $T(s) = \dfrac{N(s)}{D(s)}$ propria o strettamente propria, con $N$ e $D$ primi tra loro, è **stabile BIBO se e solo se** tutti i poli di $T(s)$ hanno **parte reale negativa**.
>
> Equivalentemente: se e solo se $T(s)$ non ha **né poli a parte reale positiva né poli a parte reale nulla**, di nessuna molteplicità, anche semplici.

Il docente sottolinea l'ultima precisazione: per la stabilità BIBO non si cita la molteplicità. Non ci devono essere poli sull'asse immaginario, nemmeno uno, nemmeno semplice.

**Ragionamento.** Si parte da condizioni iniziali nulle, quindi $Y(s) = T(s)\,U(s)$. Gli ingressi considerati hanno trasformata razionale, $U(s) = \frac{N_u(s)}{D_u(s)}$.

1. **Ingresso limitato.** Per l'ipotesi che $u(t)$ sia limitata, le radici di $D_u$ hanno parte reale negativa, quante se ne vogliono e di qualunque molteplicità, oppure parte reale nulla, ma solo semplici ([[Lezione 05 - Fratti semplici, interpretazione e metodo dei residui#2.2 La regola riassuntiva|lezione 5]]).
2. **Poli dell'uscita.** In generale non ci sono semplificazioni tra le due frazioni: non «in verticale», perché $T$ e $U$ sono già ridotte, e non «in diagonale», tra il numeratore di una e il denominatore dell'altra. I poli di $Y$ sono allora le radici di $D(s)\,D_u(s)$. Il prodotto di due polinomi si annulla dove si annulla almeno uno dei due, quindi i poli di $Y$ sono l'**unione** dei poli di $T$ e di $U$, e la molteplicità di un polo comune è la somma delle molteplicità.
3. **Condizione su $T$.** Perché $Y$ rappresenti una funzione limitata **per qualunque** $U$ ammissibile, i suoi poli devono avere parte reale negativa oppure parte reale nulla con molteplicità $1$. Aggiungere a $D_u$ poli a parte reale negativa non crea problemi: si ottengono altri poli a parte reale negativa. Se però $D$ avesse anche un solo polo a parte reale nulla, si potrebbe scegliere un ingresso limitato con **lo stesso** polo semplice: nell'uscita quel polo diventerebbe **doppio**, e l'uscita non sarebbe limitata. Se $D$ avesse un polo a parte reale positiva, l'uscita non sarebbe limitata già con un ingresso qualsiasi.

L'unico modo per essere sicuri che l'unione dei poli rispetti le condizioni di limitatezza, qualunque sia l'ingresso limitato, è che $T$ abbia **solo** poli a parte reale negativa.

> [!example] Un sistema non stabile BIBO e l'ingresso che lo dimostra
> Si consideri $T(s) = \dfrac{1}{s(s+1)}$, con poli $0$ e $-1$. Il polo $s=0$ ha parte reale nulla: per il teorema il sistema **non** è stabile BIBO. Deve quindi esistere almeno un ingresso limitato che produce un'uscita illimitata. Basta mettere in $U(s)$ un polo coincidente con quello a parte reale nulla di $T$, ad esempio il gradino $U(s) = \frac{1}{s}$:
> $$Y(s) = \frac{1}{s^2(s+1)} = \frac{A}{s} + \frac{B}{s^2} + \frac{C}{s+1}.$$
> Quante e quali funzioni ci sono nell'antitrasformata, senza fare conti? Tante quanto il grado del denominatore, cioè tre, legate ai poli: $s=-1$ dà $e^{-t}$; il polo doppio in $0$ dà un gradino e una **rampa**:
> $$y(t) = A\cdot1(t) + B\,t\cdot1(t) + C\,e^{-t} .$$
> Il docente chiede: «Può, signori della corte, $B$ essere zero?» No. Se fosse $B = 0$, rimettendo insieme le frazioni non comparirebbe mai il fattore $s^2$ al denominatore. Quindi $B\neq0$, nell'uscita c'è una rampa e l'uscita non è limitata. Con i residui, $B = \lim_{s\to0}\frac{1}{s+1} = 1$, $C = 1$, $A = -1$, quindi $y(t) = -1 + t + e^{-t}$.

> [!tip] Un altro esempio dalla dispensa
> La dispensa in inglese dimostra la necessità con $T(s) = \frac{1}{s^2+1}$, poli $\pm j$ semplici, e l'ingresso limitato $u(t) = \cos t$, cioè $U(s) = \frac{s}{s^2+1}$. L'uscita è $y(t) = \frac{1}{2}\,t\sin t$, che oscilla in un inviluppo crescente: è la **risonanza** della [[Lezione 08 - Equazioni differenziali, funzione di trasferimento e risposte|lezione 8]], letta come mancanza di stabilità BIBO.

### 2.3 Esercizio: un ingresso che «salva» un sistema instabile

Il docente ribadisce che un sistema non stabile BIBO non produce uscite illimitate con **qualunque** ingresso. Propone quindi un esercizio.

> [!example] Testo
> Dato il sistema con $T(s) = \dfrac{1}{s-1}$, trovare un ingresso **limitato** e **fisicamente realizzabile** tale che l'uscita, a partire da condizioni iniziali nulle, non solo sia limitata ma **tenda a zero**.
>
> Il docente chiama **fisicamente realizzabile** un segnale che non contiene impulsi di alcun ordine. La sua trasformata deve quindi essere **strettamente propria**: numeratore di grado inferiore al denominatore.

**Soluzione.** Il sistema ha un polo a parte reale positiva in $s=1$. Scrivendo $Y(s) = \frac{1}{s-1}\cdot\frac{N_u(s)}{D_u(s)}$, l'unico modo per eliminare quel polo è **cancellarlo**: $N_u(s)$ deve contenere il fattore $(s-1)$. Per il denominatore di $U$:

- deve avere grado almeno $2$, perché $U$ sia strettamente propria con un numeratore di primo grado;
- le sue radici devono avere parte reale **negativa**. Poli a parte reale nulla renderebbero $u$ limitata, ma resterebbero nell'uscita, che allora non tenderebbe a zero.

Ad esempio:

$$U(s) = \frac{s-1}{(s+1)(s+2)} \qquad\Longrightarrow\qquad Y(s) = \frac{1}{s-1}\cdot\frac{s-1}{(s+1)(s+2)} = \frac{1}{(s+1)(s+2)} .$$

L'uscita contiene $e^{-t}$ ed $e^{-2t}$, quindi è limitata e tende a zero: $y(t) = e^{-t} - e^{-2t}$. L'ingresso, con i residui, è

$$u(t) = -2\,e^{-t} + 3\,e^{-2t},$$

limitato, senza impulsi, e contiene le stesse funzioni dell'uscita con coefficienti diversi.

> [!warning] Osservazione (non svolta a lezione)
> La cancellazione funziona solo se lo zero di $U$ coincide **esattamente** con il polo instabile. Un ingresso reale non è mai realizzato con precisione infinita. Con $U(s) = \frac{s - 1 - \varepsilon}{(s+1)(s+2)}$ il polo $s=1$ non si cancella, e nell'uscita compare un termine proporzionale a $\varepsilon\,e^{t}$, che diverge per quanto piccolo sia $\varepsilon$. L'esercizio mostra un fatto logico, l'esistenza di ingressi limitati con uscita limitata. Non è un modo pratico di «stabilizzare» un sistema.

## 3. La risposta a regime a un ingresso sinusoidale

### 3.1 Esempio

Il docente propone un'altra prova: si prenda un sistema stabile BIBO e lo si piloti con un segnale limitato. Per definizione l'uscita, da condizioni iniziali nulle, deve essere limitata. Com'è fatta?

> [!example] $T(s) = \dfrac{1}{s+1}$ con $u(t) = \sin t$
> Il sistema ha un solo polo, in $-1$: è stabile BIBO.
> $$Y(s) = \frac{1}{s+1}\cdot\frac{1}{s^2+1} .$$
> Nell'antitrasformata ci sono tre funzioni: $e^{-t}$, dovuta al polo di $T$, e $\sin t$, $\cos t$, dovute ai poli $\pm j$ dell'ingresso. Per la parte oscillante si usa il metodo della [[Lezione 06 - Residui e poli immaginari semplici|lezione 6]]. Qui $Y = G(s)\,\frac{\omega_0}{s^2+\omega_0^2}$ con $\omega_0 = 1$ e $G(s) = T(s)$:
> $$|T(j)| = \frac{1}{|1+j|} = \frac{1}{\sqrt2}, \qquad \angle T(j) = 0 - \angle(1+j) = -\frac{\pi}{4} .$$
> Con il residuo del polo $-1$, $\lim_{s\to-1}\frac{1}{s^2+1} = \frac{1}{2}$:
> $$y(t) = \frac{1}{2}\,e^{-t} + \frac{1}{\sqrt2}\,\sin\!\Big(t - \frac{\pi}{4}\Big) .$$
> Dopo un po' il termine esponenziale si è esaurito e resta una sinusoide. Si è mandato $\sin t$ e si ottiene ancora una sinusoide della **stessa pulsazione**, moltiplicata per $\frac{1}{\sqrt2} < 1$ e sfasata di $-\frac{\pi}{4}$.

### 3.2 Il caso generale

Il risultato non è un caso. Sia $T(s) = \frac{N(s)}{D(s)}$ stabile BIBO e $u(t) = \sin\omega_0 t$:

$$Y(s) = T(s)\,\frac{\omega_0}{s^2+\omega_0^2} .$$

Si «immagini» di fare l'espansione in fratti semplici e di rimettere insieme separatamente i fratti relativi alle radici di $D$ e quelli relativi a $\pm j\omega_0$ (dispensa inglese, P/3.1/1):

$$Y(s) = \frac{N'(s)}{D(s)} + \frac{N'_u(s)}{s^2+\omega_0^2} .$$

Il sistema è stabile BIBO, quindi tutte le radici di $D$ hanno parte reale negativa e il primo pezzo, nel tempo, tende a zero. È il **transitorio**. Sopravvive solo il secondo pezzo, la **risposta a regime**. Per la lezione 6, con $G = T$:

> [!important] Risposta a regime a un ingresso sinusoidale
> Se il sistema è stabile BIBO e $u(t) = \sin\omega_0 t$, per $t$ grande
> $$y(t) \;\to\; y_{\text{reg}}(t) = |T(j\omega_0)|\,\sin\big(\omega_0 t + \angle T(j\omega_0)\big) .$$
> Il sistema restituisce una sinusoide della stessa pulsazione, con l'ampiezza moltiplicata per $|T(j\omega_0)|$ e sfasata di $\angle T(j\omega_0)$.

Questi due numeri descrivono il modo in cui il sistema **filtra** le sinusoidi: le amplifica o le attenua e le sfasa. Al variare di $\omega$, il modulo $|T(j\omega)|$ e la fase $\angle T(j\omega)$ formano la **risposta in frequenza** del sistema, che si rappresenta con i diagrammi di Bode (dispensa inglese, §3.2 e appendice C). Se, per un certo intervallo di pulsazioni, $|T(j\omega)| = 1$, una sinusoide di ampiezza $1$ esce con ampiezza $1$. Se la fase fosse sempre $-\frac{\pi}{3}$, l'uscita sarebbe sempre in ritardo di quella quantità.

> [!example] Stesso sistema, $u(t) = \sin 2t$
> Con $\omega_0 = 2$: $|T(2j)| = \frac{1}{|1+2j|} = \frac{1}{\sqrt5}$ e $\angle T(2j) = -\arctan 2$, quindi
> $$y_{\text{reg}}(t) = \frac{1}{\sqrt5}\,\sin(2t - \arctan 2) .$$
> Rispetto a $\omega_0 = 1$ l'attenuazione è maggiore ($\frac{1}{\sqrt5} < \frac{1}{\sqrt2}$) e lo sfasamento più grande ($\arctan 2 \approx 1{,}11$ rad $> \frac{\pi}{4}$). Questo sistema attenua di più le sinusoidi più veloci: si comporta come un filtro **passa-basso**.

> [!warning] Ipotesi indispensabile
> Se il sistema **non** è stabile BIBO, il primo pezzo non si esaurisce e non esiste una risposta a regime di questo tipo. Inoltre, se $T$ avesse poli proprio in $\pm j\omega_0$, si cadrebbe nella risonanza.

## 4. Il criterio di Routh

### 4.1 Perché serve

Per decidere se un sistema è stabile BIBO basta sapere se tutti i poli della funzione di trasferimento hanno parte reale negativa. Con un denominatore di secondo grado basta la regola dei segni della [[Lezione 07 - Teoremi del valore finale e del valore iniziale|lezione 7]]: tutti i coefficienti diversi da zero e dello stesso segno. Dal terzo grado in su le radici non si sanno calcolare in generale. Serve un metodo che dica se si è nella condizione di avere solo radici a parte reale negativa, senza calcolarle.

È il **criterio di Routh** (o di Routh-Hurwitz). Il docente avverte che il metodo è molto più vasto di come lo presenta: nel corso lo si usa soltanto per sapere se il sistema è stabile o no.

### 4.2 La tabella

Dato il polinomio

$$a_n s^n + a_{n-1}s^{n-1} + \dots + a_1 s + a_0 ,$$

si costruisce una tabella con una riga per ogni potenza di $s$, da $s^n$ a $s^0$.

- **Prima riga** ($s^n$): i coefficienti a partire dal più grande, **uno sì e uno no**: $a_n, a_{n-2}, a_{n-4}, \dots$
- **Seconda riga** ($s^{n-1}$): i coefficienti rimasti, sempre uno sì e uno no: $a_{n-1}, a_{n-3}, a_{n-5}, \dots$
- Dove manca un elemento si mette **zero**.

| | | | |
| :---: | :---: | :---: | :---: |
| $s^n$ | $a_n$ | $a_{n-2}$ | $a_{n-4}$ … |
| $s^{n-1}$ | $a_{n-1}$ | $a_{n-3}$ | $a_{n-5}$ … |
| $s^{n-2}$ | $b_1$ | $b_2$ | … |
| $s^{n-3}$ | $c_1$ | $c_2$ | … |
| ⋮ | ⋮ | | |
| $s^0$ | … | | |

Le righe successive si calcolano tutte con lo stesso meccanismo. Per ogni elemento si prende la matrice $2\times2$ formata dai **primi due elementi della prima colonna** delle due righe precedenti e dai due elementi **della colonna subito a destra** di quello che si sta calcolando. Si cambia di segno il determinante e lo si divide per il primo elemento della riga immediatamente precedente:

$$b_1 = -\frac{1}{a_{n-1}}\det\begin{bmatrix} a_n & a_{n-2}\\ a_{n-1} & a_{n-3}\end{bmatrix} = \frac{a_{n-1}a_{n-2} - a_n a_{n-3}}{a_{n-1}}, \qquad b_2 = \frac{a_{n-1}a_{n-4} - a_n a_{n-5}}{a_{n-1}},$$

$$c_1 = -\frac{1}{b_1}\det\begin{bmatrix} a_{n-1} & a_{n-3}\\ b_1 & b_2\end{bmatrix} = \frac{b_1 a_{n-3} - a_{n-1}b_2}{b_1}, \qquad \dots$$

e così via, finché si può. La tabella risulta triangolare.

> [!important] Criterio di Routh
> Il polinomio ha **tutte le radici a parte reale negativa se e solo se** tutti gli elementi della **prima colonna** della tabella sono diversi da zero e hanno **lo stesso segno**.
>
> In pratica: se durante il calcolo un elemento della prima colonna risulta **nullo** o **cambia segno**, ci si può fermare, perché il sistema non è stabile. Per essere sicuri che lo sia, invece, bisogna arrivare in fondo e verificare tutti gli elementi.

> [!tip] Oltre la stabilità (dispensa inglese, pp. 29–30)
> Il criterio dice di più: se nessun elemento della prima colonna è nullo, il **numero di variazioni di segno** nella prima colonna è uguale al **numero di radici a parte reale positiva**. Se un elemento della prima colonna è nullo, lo si può sostituire con un $\varepsilon$ piccolo a piacere per proseguire il conteggio. In ogni caso, un elemento nullo esclude che tutte le radici abbiano parte reale negativa.

### 4.3 Il caso del secondo ordine

Il docente verifica che, per un polinomio di secondo grado, il criterio coincide con la regola dei segni. Per $a_2 s^2 + a_1 s + a_0$:

| | | |
| :---: | :---: | :---: |
| $s^2$ | $a_2$ | $a_0$ |
| $s^1$ | $a_1$ | $0$ |
| $s^0$ | $a_0$ | |

L'ultimo elemento è $-\frac{1}{a_1}\det\begin{bmatrix} a_2 & a_0\\ a_1 & 0\end{bmatrix} = -\frac{0 - a_1a_0}{a_1} = a_0$. La prima colonna contiene esattamente i tre coefficienti $a_2$, $a_1$, $a_0$: tutte le radici hanno parte reale negativa se e solo se i tre coefficienti hanno lo stesso segno.

### 4.4 Necessaria, ma non sufficiente

> [!important] La permanenza dei segni dal terzo grado in su
> - Per un polinomio di **secondo** grado, coefficienti tutti diversi da zero e dello stesso segno sono condizione **necessaria e sufficiente** perché tutte le radici abbiano parte reale negativa.
> - Dal **terzo** grado in su è soltanto condizione **necessaria**. Se manca un coefficiente, o due coefficienti hanno segno diverso, è sicuro che non tutte le radici hanno parte reale negativa. Se invece i coefficienti sono tutti presenti e dello stesso segno, **non** si può concludere nulla: serve il criterio di Routh.

> [!example] Coefficienti tutti positivi, ma sistema instabile (esempio non svolto a lezione)
> $$s^3 + s^2 + 2s + 8$$
>
> | | | |
> | :---: | :---: | :---: |
> | $s^3$ | $1$ | $2$ |
> | $s^2$ | $1$ | $8$ |
> | $s^1$ | $\frac{1\cdot2 - 1\cdot8}{1} = -6$ | $0$ |
> | $s^0$ | $8$ | |
>
> La prima colonna è $1, 1, -6, 8$: due variazioni di segno, quindi due radici a parte reale positiva, nonostante i coefficienti siano tutti positivi. Infatti $s^3 + s^2 + 2s + 8 = (s+2)(s^2 - s + 4)$, con radici $-2$ e $\frac{1}{2}\pm j\frac{\sqrt{15}}{2}$.

### 4.5 Esempi

> [!example] Dispensa italiana, Esempio PM 11: $(s+1)(s+2)(s+3)(s+4) = s^4 + 10s^3 + 35s^2 + 50s + 24$
>
> | | | | |
> | :---: | :---: | :---: | :---: |
> | $s^4$ | $1$ | $35$ | $24$ |
> | $s^3$ | $10$ | $50$ | $0$ |
> | $s^2$ | $\frac{10\cdot35 - 1\cdot50}{10} = 30$ | $\frac{10\cdot24 - 1\cdot0}{10} = 24$ | |
> | $s^1$ | $\frac{30\cdot50 - 10\cdot24}{30} = 42$ | $0$ | |
> | $s^0$ | $24$ | | |
>
> La prima colonna è tutta positiva: tutte le radici hanno parte reale negativa, come si sapeva.

> [!example] Dispensa italiana, Esempio PM 12: $s^4 + s^3 - s - 1$
> Manca il termine in $s^2$ e ci sono coefficienti negativi: la condizione necessaria è violata, e non c'è bisogno della tabella. Applicando comunque il metodo, nella prima colonna compare un elemento nullo (da sostituire con $\varepsilon$) e poi uno negativo.

> [!example] Un polinomio con un parametro (esempio non svolto a lezione)
> Il docente ha chiuso la lezione con un polinomio contenente un parametro $K$, ma l'esempio non si ricostruisce dalla registrazione. Questo mostra lo stesso tipo di ragionamento:
> $$s^3 + 2s^2 + s + K$$
>
> | | | |
> | :---: | :---: | :---: |
> | $s^3$ | $1$ | $1$ |
> | $s^2$ | $2$ | $K$ |
> | $s^1$ | $\frac{2\cdot1 - 1\cdot K}{2} = 1 - \frac{K}{2}$ | $0$ |
> | $s^0$ | $K$ | |
>
> Perché la prima colonna sia tutta positiva servono $1 - \frac{K}{2} > 0$ e $K > 0$, cioè $0 < K < 2$. Per $K = 2$ il polinomio diventa $(s+2)(s^2+1)$, con due radici sull'asse immaginario: proprio il caso limite, in cui l'elemento della riga $s^1$ si annulla.

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. *Perché una semplificazione nella funzione di trasferimento c'è sempre, mentre una nella risposta libera dipende dal caso?* Numeratore e denominatore di $T$ dipendono solo dai coefficienti dell'equazione; il numeratore della risposta libera dipende dalle condizioni iniziali.
2. *Che cosa significa che un sistema non è stabile BIBO?* Che esiste almeno un ingresso limitato che, da condizioni iniziali nulle, produce un'uscita illimitata; non che tutti gli ingressi limitati lo facciano.
3. *Perché un polo semplice sull'asse immaginario basta a rendere un sistema non stabile BIBO?* Si può scegliere un ingresso limitato con lo stesso polo semplice: nell'uscita il polo diventa doppio e compare un termine non limitato.
4. *Come si può ottenere un'uscita limitata da un sistema con un polo in $s=1$?* Usando un ingresso il cui numeratore contiene il fattore $(s-1)$, che cancella il polo. È una cancellazione esatta, fragile nella pratica.
5. *Che cosa resta dell'uscita di un sistema stabile BIBO sollecitato da $\sin\omega_0 t$, dopo molto tempo?* $|T(j\omega_0)|\sin(\omega_0 t + \angle T(j\omega_0))$: i termini dovuti ai poli di $T$ si sono esauriti.
6. *Perché per un polinomio di terzo grado non bastano coefficienti tutti positivi?* La condizione è solo necessaria: ad esempio $s^3+s^2+2s+8$ ha due radici a parte reale positiva.
7. *Che cosa si conclude se nella prima colonna della tabella di Routh compare uno zero?* Che non tutte le radici hanno parte reale negativa, e quindi il sistema non è stabile BIBO.
