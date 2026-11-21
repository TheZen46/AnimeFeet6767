---
lezione: 3
data: 2026-10-14
argomenti: [posa nel piano, gradi di libertà, trasformazioni rigide, coordinate omogenee, matrice di trasformazione omogenea, composizione di trasformazioni, trasformazione inversa, SE(2), terne mondo-base-sensore, simulatore EDR, Git, Python]
---

# Lezione 3 — Pose nel piano, coordinate omogenee e gruppo SE(2)

## 1. Struttura della lezione e strumenti

La lezione ha due parti. Nella prima si completa la descrizione delle trasformazioni nel piano: alla rotazione, vista nella [[Robotica MOD1 - Lezione 02|lezione 2]], si aggiunge la traslazione, e le due vengono riunite in un'unica matrice grazie alle coordinate omogenee. Nella seconda parte il docente presenta il simulatore del corso e il primo esercizio da svolgere in codice.

Gli esercizi accompagnano la parte teorica e sono scritti principalmente in **Python**. La versione minima richiesta è la 3.12. Il simulatore è un ambiente 3D volutamente semplice: mostra delle terne (*frame*), cioè sistemi di coordinate, e chiede di implementare le formule viste a lezione. Una volta implementata una funzione, si vede subito se il risultato coincide con quello atteso. Il docente ha precisato che in un'altra parte del corso si usa un simulatore diverso, più completo. Questo serve soprattutto a visualizzare i concetti sui riferimenti.

---

## 2. Riepilogo: SO(2) e il ruolo del determinante

La lezione precedente si era chiusa con il gruppo **SO(2)** delle matrici di rotazione piane: matrici $2\times 2$ con colonne ortonormali ($R^TR = I$) e determinante $+1$.

Il docente ha chiesto perché il determinante debba valere esattamente $+1$. Anche una matrice ortogonale con determinante $-1$ è invertibile e conserva le lunghezze, ma opera una **riflessione**: ribalta la terna a cui viene applicata. Una terna con assi $x, y$ disposti secondo la convenzione abituale (con $y$ ruotato di $90^\circ$ in senso antiorario rispetto a $x$, e quindi con l'asse $z$ che «esce» dal piano) diventerebbe una terna con l'ordine degli assi invertito. La terna non sarebbe più **destrorsa** e tutte le formule costruite su quella convenzione smetterebbero di funzionare. Il vincolo $\det R = +1$ serve proprio a escludere questi casi.

Le altre proprietà (inversa uguale alla trasposta, chiusura rispetto al prodotto) discendono dalla definizione. Nel piano le rotazioni **commutano**, perché c'è un solo grado di libertà rotazionale e ogni rotazione si limita a sommare un angolo. Il docente ha ricordato che nello spazio non sarà più così: lì l'ordine delle rotazioni conta (lo si vedrà nella lezione 4).

---

## 3. La posa di una terna nel piano

### 3.1 Rotazione più traslazione

Per descrivere completamente dove si trova un robot non basta la sola rotazione: serve anche la posizione. Si considerino due terne nel piano.

- La terna $\{a\}$, con origine $O_a$ e assi $x_a, y_a$.
- La terna $\{b\}$, con origine $O_b$ e assi $x_b, y_b$, traslata e leggermente ruotata rispetto ad $\{a\}$.

Sia $P$ un punto del piano di cui si conoscono le coordinate ${}^{b}P$ nella terna $\{b\}$. Si vogliono le sue coordinate ${}^{a}P$ nella terna $\{a\}$.

Il ragionamento parte dai **vettori geometrici**, cioè dalle frecce nel piano, prima di proiettarle su una qualsiasi terna. Per andare da $O_a$ a $P$ si può passare per $O_b$:

$$\overrightarrow{O_aP} = \overrightarrow{O_aO_b} + \overrightarrow{O_bP}.$$

Questa uguaglianza vale per le frecce. Per trasformarla in un'uguaglianza tra numeri bisogna proiettare tutti i termini **nella stessa terna**, quella di arrivo $\{a\}$.

- $\overrightarrow{O_aP}$ espresso in $\{a\}$ ha come componenti le coordinate di $P$ in $\{a\}$, cioè ${}^{a}P$.
- $\overrightarrow{O_aO_b}$ espresso in $\{a\}$ è la posizione dell'origine di $\{b\}$ vista da $\{a\}$, cioè ${}^{a}O_b$.
- $\overrightarrow{O_bP}$ è noto in $\{b\}$, dove le sue componenti sono ${}^{b}P$. Per esprimerlo in $\{a\}$ serve la matrice di rotazione ${}^{a}_{b}R$: le sue componenti in $\{a\}$ sono ${}^{a}_{b}R\,{}^{b}P$.

Mettendo insieme i tre pezzi:

> [!important] Cambio di coordinate di un punto tra due terne
> $${}^{a}P = {}^{a}O_b + {}^{a}_{b}R\;{}^{b}P .$$
> Si percorre prima il tratto da $O_a$ a $O_b$, già espresso in $\{a\}$. Poi si «cambia riferimento»: il tratto da $O_b$ a $P$, noto in $\{b\}$, viene riportato in $\{a\}$ con la rotazione. Solo a quel punto i due addendi sono nella stessa base e si possono sommare.

Il docente ha insistito su questo passaggio perché sarà implicito in moltissime operazioni future. È il caso base: con catene di più terne il ragionamento si ripete uguale, ma le rotazioni si accumulano. Ricordiamo la regola della lezione 2: l'apice in alto a sinistra indica in quale terna è espressa una grandezza, e si possono sommare solo grandezze con lo stesso apice.

### 3.2 Gradi di libertà della posa piana

La coppia $\big({}^{a}_{b}R,\ {}^{a}O_b\big)$ descrive completamente la **posa** della terna $\{b\}$ rispetto ad $\{a\}$. Nel piano la posa ha **tre gradi di libertà**: due per la posizione ($x$, $y$) e uno per l'orientamento (l'angolo $\theta$ di rotazione attorno all'asse $z$, perpendicolare al piano). Nella letteratura e nel software si usa spesso la sigla inglese **DOF** (*Degrees Of Freedom*) invece dell'italiano GdL.

### 3.3 Trasformazioni rigide

La trasformazione appena scritta è una **trasformazione rigida** e appartiene alla famiglia delle **trasformazioni affini** (trasformazioni lineari seguite da una traslazione). La sua caratteristica fondamentale è che **conserva le lunghezze e gli angoli**. È indispensabile: quando si descrive un robot o un oggetto in terne diverse, il cambio di riferimento non deve deformare la struttura che si sta descrivendo.

---

## 4. Coordinate omogenee

### 4.1 Perché servono

Si consideri un manipolatore articolato: una terna sulla base, una su ciascun giunto (giunto 1, 2, 3, …) e una sull'utensile. Per sapere dove si trova l'utensile bisogna applicare in sequenza tutte le trasformazioni da una terna alla successiva, ognuna fatta di una rotazione e di una traslazione. Il calcolo va ripetuto a ogni ciclo del controllo, quindi molte volte al secondo e in tempi brevissimi.

Scritto come catena di rotazioni e somme, questo calcolo è laborioso. La strategia usata in robotica, come in altri campi del calcolo scientifico, è ricondurre tutto a **prodotti tra matrici**: sono operazioni molto regolari, che i processori eseguono in modo estremamente efficiente. Il problema è che la traslazione non è un'operazione lineare e quindi non si può scrivere come prodotto per una matrice delle coordinate ordinarie. Le **coordinate omogenee** risolvono il problema: con un elemento in più, la trasformazione affine diventa un semplice prodotto matrice-vettore.

### 4.2 Punti in coordinate omogenee e matrice di trasformazione

Un punto del piano, che in coordinate ordinarie ha due componenti, in coordinate omogenee ne ha tre: le due componenti ordinarie e un $1$ in fondo. Per distinguere le due rappresentazioni il docente ha usato per ora una barra, anche se più avanti potrà restare implicita:

$${}^{a}P = \begin{bmatrix} x_{P,a} \\ y_{P,a} \end{bmatrix} \qquad\longrightarrow\qquad {}^{a}\bar P = \begin{bmatrix} x_{P,a} \\ y_{P,a} \\ 1 \end{bmatrix}.$$

La rotazione e la posizione dell'origine, che descrivono la posa, vengono raccolte in un'unica matrice.

> [!important] Matrice di trasformazione omogenea nel piano
> $${}^{a}_{b}T = \begin{bmatrix} {}^{a}_{b}R & {}^{a}O_b \\ \mathbf{0}_{1\times 2} & 1 \end{bmatrix} \in \mathbb{R}^{3\times 3}, \qquad {}^{a}\bar P = {}^{a}_{b}T\;{}^{b}\bar P .$$
> In alto a sinistra c'è la matrice di rotazione $2\times 2$ da $\{b\}$ ad $\{a\}$. In alto a destra c'è l'origine di $\{b\}$ espressa in $\{a\}$ (una colonna $2\times 1$). L'ultima riga è $(0,\ 0,\ 1)$. La regola di lettura degli indici è la stessa delle rotazioni: il pedice della matrice deve coincidere con l'apice del punto a cui si applica.

Il docente ha raccomandato attenzione a questa distinzione anche nel codice. Se si moltiplica una matrice $3\times 3$ per un punto rappresentato con due sole componenti, il programma si interrompe con un errore di dimensioni incompatibili. Errori di questo tipo sono utili, perché segnalano un'incoerenza nella rappresentazione dei dati.

### 4.3 Sviluppo esplicito

Per vedere che la matrice realizza davvero una rotazione seguita da una traslazione, conviene sviluppare il prodotto. Sia $\{b\}$ ruotata di $\theta$ rispetto ad $\{a\}$, con origine ${}^{a}O_b = (x_O,\ y_O)^T$:

$$
{}^{a}\bar P =
\begin{bmatrix} \cos\theta & -\sin\theta & x_O \\ \sin\theta & \cos\theta & y_O \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} x_{P,b} \\ y_{P,b} \\ 1 \end{bmatrix}
=
\begin{bmatrix} \cos\theta\, x_{P,b} - \sin\theta\, y_{P,b} + x_O \\ \sin\theta\, x_{P,b} + \cos\theta\, y_{P,b} + y_O \\ 1 \end{bmatrix}.
$$

Le prime due righe sono esattamente ${}^{a}_{b}R\,{}^{b}P + {}^{a}O_b$, cioè la formula del paragrafo 3.1. Si vede che le componenti del punto vengono **prima ruotate** e solo dopo vi si somma la traslazione. L'ultima riga si limita a riprodurre l'$1$ finale.

> [!warning] Lapsus durante lo sviluppo alla lavagna
> Sviluppando l'esempio il docente ha iniziato a scrivere una matrice $4\times 4$ con una rotazione attorno a un asse dello spazio, poi si è corretto: l'esempio riguarda il piano e la matrice corretta è quella $3\times 3$ riportata sopra.

### 4.4 Vettori in coordinate omogenee

Per i **vettori** (direzioni, spostamenti) la rappresentazione omogenea è diversa: l'ultima componente vale $0$ invece di $1$. Il motivo è semplice: un vettore è una differenza di punti, e la differenza tra due punti omogenei ha ultima componente $1 - 1 = 0$:

$${}^{b}\bar P - {}^{b}\bar Q = \begin{bmatrix} {}^{b}P - {}^{b}Q \\ 0 \end{bmatrix}, \qquad {}^{b}\bar v = \begin{bmatrix} v_{x,b} \\ v_{y,b} \\ 0 \end{bmatrix}.$$

Applicando la trasformazione omogenea a un vettore, la parte traslazionale non agisce, perché viene moltiplicata per $0$:

$${}^{a}_{b}T\;{}^{b}\bar v = \begin{bmatrix} {}^{a}_{b}R & {}^{a}O_b \\ \mathbf{0} & 1 \end{bmatrix}\begin{bmatrix} {}^{b}v \\ 0 \end{bmatrix} = \begin{bmatrix} {}^{a}_{b}R\;{}^{b}v \\ 0 \end{bmatrix}.$$

È coerente con quanto visto nella lezione 2: un vettore non dipende dall'origine della terna, ma solo dal suo orientamento. Una direzione cambia quando si ruotano gli assi, non quando li si trasla.

---

## 5. Composizione di trasformazioni

Lo scopo di tutto questo formalismo è descrivere un mondo virtuale con robot, sensori, ostacoli e punti osservati, e passare agevolmente dall'uno all'altro. Si aggiunga allora una terza terna $\{c\}$, con origine $O_c$ e assi $x_c, y_c$. Sia noto un punto in $\{c\}$ e lo si voglia esprimere in $\{a\}$.

Si procede a ritroso, partendo dalla terna più «interna». Prima si porta il punto da $\{c\}$ a $\{b\}$, poi da $\{b\}$ ad $\{a\}$:

$$
{}^{a}P = {}^{a}O_b + {}^{a}_{b}R\Big({}^{b}O_c + {}^{b}_{c}R\;{}^{c}P\Big)
= \underbrace{\Big({}^{a}O_b + {}^{a}_{b}R\;{}^{b}O_c\Big)}_{{}^{a}O_c} + \underbrace{{}^{a}_{b}R\;{}^{b}_{c}R}_{{}^{a}_{c}R}\;{}^{c}P .
$$

Il risultato ha di nuovo la forma «origine più rotazione per punto», quindi corrisponde a una matrice omogenea ${}^{a}_{c}T$. La si ottiene direttamente come prodotto delle due matrici:

> [!important] Composizione di trasformazioni omogenee
> $${}^{a}_{c}T = {}^{a}_{b}T\;{}^{b}_{c}T = \begin{bmatrix} {}^{a}_{b}R\;{}^{b}_{c}R & {}^{a}O_b + {}^{a}_{b}R\;{}^{b}O_c \\ \mathbf{0}_{1\times 2} & 1 \end{bmatrix}.$$
> - La parte rotazionale è la composizione delle rotazioni.
> - La parte traslazionale è l'origine di $\{b\}$ in $\{a\}$ più l'origine di $\{c\}$ in $\{b\}$, **ruotata** in $\{a\}$.

Basta eseguire il prodotto a blocchi per verificarlo. Il docente ha sottolineato che, capito il significato, la composizione non è affatto misteriosa.

**Le trasformazioni operano da destra verso sinistra.** In ${}^{a}_{c}T\,{}^{c}\bar P = {}^{a}_{b}T\,{}^{b}_{c}T\,{}^{c}\bar P$ si parte dal punto espresso in $\{c\}$. La matrice più vicina, ${}^{b}_{c}T$, lo porta in $\{b\}$, e poi ${}^{a}_{b}T$ lo porta in $\{a\}$. Gli indici interni si «semplificano» a catena, come per le rotazioni.

**Le trasformazioni omogenee non commutano**, nemmeno nel piano. Le rotazioni piane commutano, ma nel prodotto ${}^{a}_{b}T\,{}^{b}_{c}T$ la traslazione ${}^{b}O_c$ viene ruotata da ${}^{a}_{b}R$. Invertendo l'ordine si ruota la traslazione sbagliata e si ottiene una trasformazione diversa, con un significato fisico diverso. Un esempio numerico è nel paragrafo 8.5.

---

## 6. La trasformazione inversa

Nelle applicazioni capita spesso di dover fare il passaggio opposto: noto ${}^{a}P$, ricavare ${}^{b}P$. Si parte dalla relazione del paragrafo 3.1 e la si risolve rispetto a ${}^{b}P$:

$${}^{a}P - {}^{a}O_b = {}^{a}_{b}R\;{}^{b}P .$$

Si moltiplicano entrambi i membri per l'inversa di ${}^{a}_{b}R$. Per la proprietà delle matrici di rotazione l'inversa coincide con la trasposta, quindi

$${}^{b}P = {}^{a}_{b}R^{T}\big({}^{a}P - {}^{a}O_b\big) = {}^{a}_{b}R^{T}\;{}^{a}P \;-\; {}^{a}_{b}R^{T}\;{}^{a}O_b .$$

Anche questa è una relazione «rotazione più traslazione», quindi si scrive come matrice omogenea. Si noti che gli indici sono scambiati: è la trasformazione da $\{a\}$ a $\{b\}$.

> [!important] Inversa di una trasformazione omogenea
> $${}^{b}_{a}T = \big({}^{a}_{b}T\big)^{-1} = \begin{bmatrix} {}^{a}_{b}R^{T} & -\,{}^{a}_{b}R^{T}\;{}^{a}O_b \\ \mathbf{0}_{1\times 2} & 1 \end{bmatrix}, \qquad {}^{a}_{b}T\;{}^{b}_{a}T = I .$$

Il termine $-\,{}^{a}_{b}R^{T}\,{}^{a}O_b$ ha un significato preciso: è la posizione dell'origine $O_a$ espressa in $\{b\}$, cioè ${}^{b}O_a$. Il segno meno compare perché il vettore che va da $O_b$ a $O_a$ è opposto a quello che va da $O_a$ a $O_b$; la trasposta lo riporta nelle componenti di $\{b\}$.

Il docente ha sottolineato il **vantaggio computazionale**. Invertire una matrice generica è un'operazione lunga: bisogna calcolare determinante e matrice aggiunta (dei complementi algebrici), con molti passaggi. Qui basta una trasposizione e un prodotto matrice-vettore. Quando si eseguono centinaia di migliaia di queste operazioni al secondo, il risparmio è notevole.

> [!warning] L'inversa di $T$ non è la sua trasposta
> Per le rotazioni vale $R^{-1} = R^T$, ma per le trasformazioni omogenee in generale ${}^{a}_{b}T^{-1} \neq {}^{a}_{b}T^{T}$. Trasponendo $T$ la colonna di traslazione finirebbe nell'ultima riga, che non avrebbe alcun significato. Non vanno confuse le due proprietà.

---

## 7. Posizione, posa e il gruppo SE(2)

### 7.1 Posizione e posa

Il docente ha raccomandato attenzione alla terminologia, anche consultando materiale online.

- La **posizione** è data dalle sole coordinate del punto: $(x, y)$ nel piano, $(x, y, z)$ nello spazio.
- La **posa** comprende posizione e orientamento: $(x, y, \theta)$ nel piano. Nello spazio, come si vedrà, servono tre coordinate di posizione e tre angoli.

### 7.2 Il gruppo speciale euclideo

Come le rotazioni formano il gruppo SO(2), le trasformazioni omogenee piane formano un gruppo. Le rototraslazioni non sono più matrici ortogonali, perché contengono anche la traslazione, e il gruppo prende un nome diverso: **gruppo speciale euclideo**.

> [!important] Definizione di SE(2)
> $$SE(2) = \left\{\, T = \begin{bmatrix} R & p \\ \mathbf{0}_{1\times 2} & 1 \end{bmatrix} \;:\; R \in SO(2),\ p \in \mathbb{R}^{2} \right\}.$$

Le proprietà di gruppo si verificano con quanto visto.

- **Chiusura**: il prodotto di due elementi di SE(2) ha ancora la stessa forma (paragrafo 5), quindi è ancora una rototraslazione.
- **Elemento neutro**: l'identità $I_3$, cioè rotazione nulla e traslazione nulla («tutto fermo»).
- **Inverso**: ogni elemento ha l'inversa del paragrafo 6, che appartiene ancora a SE(2).

SE(2) è il **gruppo delle trasformazioni rigide e proprie** del piano.

- **Rigide** perché conservano le distanze: non deformano gli oggetti.
- **Proprie** perché non ribaltano l'ordine degli assi: la parte rotazionale ha determinante $+1$.

> [!tip] Approfondimento — SE(2), SE(3) e la notazione «da… a…»
> #approfondimento
> Nel testo di Lynch e Park la posa di un corpo rigido è trattata sistematicamente come elemento dei gruppi SE(2) e SE(3), rappresentati con matrici omogenee; i gruppi SO(n) e SE(n) sono esempi di gruppi di Lie matriciali [@lynch2017]. La stessa notazione a due indici (da quale terna, verso quale terna) è quella di Craig, già citata nella lezione 2 [@craig2005].

---

## 8. Esempio: robot, sensore e punto osservato

### 8.1 Le terne del problema

Nella maggior parte degli esempi del corso non si useranno terne astratte $a$, $b$, $c$ ma terne con un significato fisico.

- $\{w\}$, il **mondo** (*world*).
- $\{b\}$, la **base**: può essere la base di un robot mobile oppure la base fissa di un manipolatore.
- $\{s\}$, il **sensore**.

Il sensore fornisce le sue rilevazioni (*detection*) nel proprio riferimento, mentre gli obiettivi del robot, per esempio un punto da raggiungere, sono espressi nel riferimento del mondo. Bisogna quindi saper passare da una terna all'altra a seconda di ciò che serve.

Lo scenario è questo.

- Il robot si trova nel punto $(2, 1)$ del mondo ed è orientato in modo che il suo «davanti» punti lungo l'asse $y$ del mondo.
- Sul robot è montato un sensore, allineato con la base, $0{,}5$ m più avanti lungo la direzione di marcia. Può essere un sensore che sporge dalla struttura del robot.
- Il sensore osserva un punto $P$ un metro davanti a sé.

Si vuole la posizione di $P$ nel mondo.

```mermaid
flowchart RL
    P["Punto P<br/>noto in {s}"] -->|"ˢP"| S["Sensore {s}"]
    S -->|"ᵇₛT"| B["Base del robot {b}"]
    B -->|"ʷᵦT"| W["Mondo {w}"]
```

### 8.2 Scegliere le terne

Il primo passo è **definire le terne** sul robot e sul sensore. È una nostra libertà: le terne si possono collocare come si vuole. Conviene però sceglierle in modo che vengano fuori numeri semplici, senza orientamenti arbitrari.

Il docente ha avvertito che proprio qui nasce l'errore più frequente in quasi tutte le applicazioni robotiche. Il robot vede un obiettivo, parte e va da un'altra parte, perché una terna è stata definita male: per esempio quella del sensore rispetto alla base, con destra e sinistra scambiate. Capita quotidianamente. Il rimedio è guardare i numeri e chiedersi se hanno senso («l'obiettivo dovrebbe essere a destra, il robot lo vede a sinistra»), poi togliere una complicazione alla volta finché non si trova l'errore. Le formule si calcolano in automatico, ma bisogna saperne controllare il risultato.

Per i corpi in movimento si segue una convenzione naturale: **l'asse $x$ punta nella direzione di avanzamento**. Se si immagina un punto materiale che va avanti, lo si immagina lungo $x$. L'asse $y$ segue dalla regola della terna destrorsa (ruotato di $90^\circ$ in senso antiorario rispetto a $x$, quindi verso sinistra). Nel disegno della lavagna il robot è rettangolare, con il sensore sul lato anteriore, e la sua $x_b$ punta lungo $y_w$.

Non è solo una convenzione di comodo.

- Per un **manipolatore**, il modello si scrive di solito con il braccio disteso e fermo. In quella configurazione si mette l'asse $x$ di ogni terna nella direzione della terna successiva lungo la catena.
- Molti **sensori** assumono un montaggio preciso. Un accelerometro riferisce le accelerazioni al corpo su cui è montato e si aspetta, per esempio, di misurare un'accelerazione «in avanti» lungo il proprio $x$ quando il corpo avanza. I sensori di fascia più alta hanno la terna $x, y, z$ disegnata direttamente sull'involucro.

> [!tip] Approfondimento — La convenzione di ROS per le terne dei corpi
> #approfondimento
> In ROS, il middleware citato nella lezione 2, la convenzione è fissata dal documento REP 103 [@rep103]. Per le terne solidali a un corpo prescrive l'asse $x$ in avanti, $y$ a sinistra e $z$ verso l'alto, e richiede che tutti i sistemi di coordinate siano destrorsi. È la stessa scelta adottata a lezione.

### 8.3 Costruire le matrici leggendo le colonne

Con le terne fissate si possono scrivere le due trasformazioni. Il docente ha mostrato come costruirle rapidamente con la lettura «per colonne» vista nella lezione 2: le colonne della matrice di rotazione sono gli assi della nuova terna espressi nella vecchia.

**Dalla base al mondo, ${}^{w}_{b}T$.**

- L'asse $x_b$ punta lungo $y_w$: la prima colonna è $(0,\ 1)^T$.
- L'asse $y_b$, ruotato di $90^\circ$ in senso antiorario rispetto a $x_b$, punta lungo $-x_w$: la seconda colonna è $(-1,\ 0)^T$.
- L'origine della base nel mondo è ${}^{w}O_b = (2,\ 1)^T$.

$${}^{w}_{b}T = \begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}.$$

La parte rotazionale è $R(\pi/2)$: si sarebbe ottenuta anche sostituendo $\theta = \pi/2$ nella formula con seni e coseni. La lettura per colonne è più rapida e intuitiva.

**Dal sensore alla base, ${}^{b}_{s}T$.** Il docente ha invitato a ricavarla da soli, perché è più semplice.

- Sensore e base sono orientati allo stesso modo, quindi la rotazione è l'**identità**.
- La traslazione va espressa **nella terna della base**: il sensore è $0{,}5$ m più avanti lungo $x_b$, quindi ${}^{b}O_s = (0{,}5,\ 0)^T$. Non va confusa con lo spostamento nel mondo, che sarebbe lungo $y_w$.

$${}^{b}_{s}T = \begin{bmatrix} 1 & 0 & 0{,}5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.$$

Saper costruire queste matrici guardando la scena è il punto di partenza di tutto il resto. Senza di esse non si possono nemmeno scrivere i dati di ingresso di un programma.

### 8.4 Da dove vengono questi dati in un robot reale

Nell'esempio i dati sono assegnati; in un robot reale vanno misurati.

- La **posizione** del robot nel mondo può venire, per esempio, da un **GPS**. Nota la posizione del robot, si ricava quella del sensore con la trasformazione appena scritta.
- L'**orientamento** è più difficile da misurare. Servono punti di riferimento, e l'unico sempre disponibile è la **gravità**: una forza diretta verso il basso, che si assume verticale. La gravità permette di capire se il corpo è inclinato o in piano. Per l'angolo attorno alla verticale si può usare una **bussola**, che fissa la direzione di riferimento ($0$). Le altre grandezze vengono di solito inizializzate a zero in base alla configurazione di partenza.

I dispositivi che misurano l'orientamento, come quelli dei telefoni, vengono **calibrati in fabbrica**: si appoggiano su ciascuna faccia per identificare gli assi $x$, $y$, $z$ del sensore.

### 8.5 Il calcolo

**Il punto in coordinate omogenee.** Il punto è un metro davanti al sensore, cioè lungo $x_s$:

$${}^{s}\bar P = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}.$$

**Dal sensore alla base.** Prima di calcolare conviene chiedersi che cosa ci si aspetta. Il punto è $1$ m davanti al sensore, che è $0{,}5$ m davanti alla base: in $\{b\}$ la coordinata $x$ deve venire $1{,}5$. Se non viene $1{,}5$, la matrice è sbagliata. Sono piccoli controlli intuitivi da fare sempre, altrimenti tutto l'esercizio risulta sbagliato.

$${}^{b}\bar P = {}^{b}_{s}T\;{}^{s}\bar P = \begin{bmatrix} 1 & 0 & 0{,}5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1{,}5 \\ 0 \\ 1 \end{bmatrix}.$$

**Perché portare tutto nel mondo.** Il docente ha sottolineato che, alla fine, si vogliono **confrontare** grandezze tra loro: il sensore ha rilevato qualcosa in un punto e ci si aspetta che lì ci sia un certo oggetto. Se le due informazioni sono espresse in terne diverse, vanno portate in una terna comune. Il **mondo** è la scelta più frequente, perché è comune a tutti gli elementi: più robot, oggetti, sensori esterni. È il caso tipico delle stanze attrezzate con sistemi di *motion capture*, dove l'origine del mondo è spesso al centro dell'area di lavoro. In robotica mobile o marina, quando non si hanno riferimenti globali, si usa invece la base del robot e si esprime tutto «rispetto a sé».

**Dal sensore al mondo.** Si potrebbe moltiplicare ${}^{w}_{b}T$ per ${}^{b}\bar P$. Il docente ha preferito comporre prima le due matrici, per ottenere direttamente la trasformazione dal sensore al mondo:

$${}^{w}_{s}T = {}^{w}_{b}T\;{}^{b}_{s}T = \begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0{,}5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 1{,}5 \\ 0 & 0 & 1 \end{bmatrix}.$$

L'ultima colonna dice che il sensore si trova nel punto $(2,\ 1{,}5)$ del mondo, mezzo metro «sopra» il robot lungo $y_w$, come ci si aspetta. A questo punto

$${}^{w}\bar P = {}^{w}_{s}T\;{}^{s}\bar P = \begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 1{,}5 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 2{,}5 \\ 1 \end{bmatrix}.$$

Il punto è in $(2,\ 2{,}5)$: un metro e mezzo davanti al robot, lungo $y_w$. Il risultato coincide con quello che si ottiene moltiplicando ${}^{w}_{b}T$ per ${}^{b}\bar P$, per la proprietà associativa. Conferma che le matrici sono usate correttamente.

> [!example] Esempio: l'ordine delle trasformazioni conta
> Si inverta per errore l'ordine del prodotto:
> $${}^{b}_{s}T\;{}^{w}_{b}T = \begin{bmatrix} 1 & 0 & 0{,}5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 2{,}5 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}.$$
> La rotazione è la stessa (nel piano le rotazioni commutano), ma il sensore risulterebbe in $(2{,}5,\ 1)$. Lo spostamento di $0{,}5$ m è stato applicato lungo $x_w$ invece che lungo la direzione di marcia del robot: la traslazione non è stata ruotata. Gli indici lo segnalano subito: in ${}^{b}_{s}T\,{}^{w}_{b}T$ il pedice $s$ non coincide con l'apice $w$, quindi il prodotto non ha significato.

> [!example] Esempio: la trasformazione inversa ${}^{b}_{w}T$
> Con la formula del paragrafo 6:
> $${}^{b}_{w}T = \begin{bmatrix} R(\pi/2)^{T} & -R(\pi/2)^{T}\,{}^{w}O_b \\ \mathbf{0} & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & -1 \\ -1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}.$$
> L'ultima colonna è l'origine del mondo vista dal robot, ${}^{b}O_w = (-1,\ 2)^T$. Verifica intuitiva: l'origine del mondo è $1$ m «indietro» lungo $y_w$ rispetto al robot, cioè $-1$ lungo $x_b$, e $2$ m lungo $-x_w$, cioè alla sinistra del robot, quindi $+2$ lungo $y_b$. Applicando ${}^{b}_{w}T$ a ${}^{w}\bar P = (2,\ 2{,}5,\ 1)^T$ si ritrova ${}^{b}\bar P = (1{,}5,\ 0,\ 1)^T$.

### 8.6 Variante: punto osservato a 30 gradi

Il docente ha poi complicato l'esempio. Tutto resta uguale, ma il punto è osservato con un angolo $\beta = 30^\circ = \pi/6$ rispetto all'asse $x_s$, sempre a un metro di distanza.

Per esprimere il punto conviene la rappresentazione **raggio e angolo** delle **coordinate polari**, tipica dei sensori che misurano una distanza lungo una direzione (come i sensori laser). Con raggio $r$ e angolo $\beta$:

$${}^{s}P = \begin{bmatrix} r\cos\beta \\ r\sin\beta \end{bmatrix} = \begin{bmatrix} \cos\frac{\pi}{6} \\ \sin\frac{\pi}{6} \end{bmatrix} = \begin{bmatrix} \frac{\sqrt 3}{2} \\ \frac12 \end{bmatrix}, \qquad {}^{s}\bar P = \begin{bmatrix} \frac{\sqrt 3}{2} \\ \frac12 \\ 1 \end{bmatrix}.$$

I punti a distanza $1$ dal sensore stanno su una circonferenza di raggio $1$ centrata nel sensore; l'angolo seleziona uno di essi. La trasformazione ${}^{w}_{s}T$ non cambia, perché il robot e il sensore non si sono mossi:

$${}^{w}\bar P = \begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 1{,}5 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} \frac{\sqrt 3}{2} \\ \frac12 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 - \frac12 \\ \frac{\sqrt 3}{2} + 1{,}5 \\ 1 \end{bmatrix} \approx \begin{bmatrix} 1{,}5 \\ 2{,}366 \\ 1 \end{bmatrix}.$$

> [!warning] Valore numerico della seconda coordinata
> Nella trascrizione il valore $2{,}36\ldots$ viene descritto come «periodico». Il valore esatto è $\tfrac32 + \tfrac{\sqrt 3}{2}$, un numero irrazionale, quindi non periodico: $\approx 2{,}3660$.

**Controllo proposto dal docente.** La distanza tra il punto e il sensore deve essere rimasta $1$: le trasformazioni rigide conservano le distanze. Lo si può verificare nel mondo, dove l'origine del sensore è ${}^{w}O_s = (2,\ 1{,}5)$:

$${}^{w}P - {}^{w}O_s = \begin{bmatrix} -\frac12 \\ \frac{\sqrt 3}{2} \end{bmatrix}, \qquad \left\| {}^{w}P - {}^{w}O_s \right\| = \sqrt{\tfrac14 + \tfrac34} = 1 .$$

Si noti che ${}^{w}P - {}^{w}O_s$ è proprio la **direzione** dal sensore al punto espressa nel mondo. La si ottiene anche trasformando il vettore omogeneo ${}^{s}\bar d = (\cos\beta,\ \sin\beta,\ 0)^T$: l'ultima componente nulla elimina la traslazione e rimane solo la rotazione, ${}^{w}d = R(\pi/2)\,{}^{s}d = (-\tfrac12,\ \tfrac{\sqrt3}{2})^T$.

> [!tip] Excalidraw
> Uno schizzo della scena (terna del mondo, robot in $(2,1)$ con $x_b$ verso l'alto, sensore $0{,}5$ m più avanti, circonferenza di raggio $1$ attorno al sensore con il punto a $0^\circ$ e a $30^\circ$) aiuta a controllare a colpo d'occhio tutti i risultati numerici.

---

## 9. Il simulatore del corso

### 9.1 Git e GitHub

Il simulatore usato a lezione è pubblicato dal docente su **GitHub**. Il nome nella trascrizione è poco chiaro; la sigla coerente con quella delle slide del corso (*Elementi di Robotica*, EDR) è **EDR Simulator**.

Il docente ha dato qualche nozione di base sugli strumenti.

- **Git** è il software più diffuso per gestire lo sviluppo del codice. È un sistema di **versionamento** (*version control*): il codice sta in un **repository**, un archivio su un server, in un certo stato. Ogni modifica caricata è un ***commit***, che registra le differenze rispetto alla versione precedente. Se si introduce un errore, si può tornare a un commit precedente e riavere una versione funzionante. Il docente ne consiglia l'uso per qualunque progetto personale.
- **GitHub** è uno dei siti più noti che ospitano repository Git, pubblici o privati.

Il repository del simulatore è pubblico e si può ottenere in due modi.

1. **Con Git** (il metodo consigliato): si installa Git su Windows o Linux e si scarica il repository da riga di comando con `git clone`.
2. **Come archivio ZIP**: dal pulsante verde della pagina del repository si sceglie il download.

Esiste anche **GitHub Desktop**, un'applicazione grafica per le stesse operazioni.

### 9.2 Python

Il repository non contiene Python, che va installato a parte scaricandolo da python.org (per Windows, Linux, macOS). Il corso non è un corso di Python, ma alcune caratteristiche del linguaggio vanno conosciute.

- È un linguaggio **interpretato**: non va compilato, quindi dopo una modifica si riesegue direttamente il codice.
- Lo svantaggio è un'efficienza di esecuzione inferiore rispetto a un linguaggio compilato come il C++.
- In Python l'**indentazione** (i rientri delle righe) fa parte della sintassi e determina la struttura del codice. In C++ gli spazi sono invece irrilevanti.

### 9.3 Avvio e interfaccia

Una volta scaricata la cartella del simulatore, lo si avvia con lo script adatto al sistema operativo.

- **Windows**: doppio clic su `start_simulator.cmd`.
- **Linux**: `start_simulator.sh`, da riga di comando.

Da terminale si entra nella cartella con il comando `cd` (*change directory*). Il docente ha ricordato che Windows e Linux usano separatori di percorso opposti (la barra rovesciata `\` su Windows, la barra `/` su Linux), cosa che genera qualche malinteso.

L'ambiente è molto semplice: ogni quadrato della griglia è un metro. Trascinando con il clic del mouse si ruota la vista; tenendo premuto Shift si sposta il punto di vista.

### 9.4 L'esercizio sulle trasformazioni planari

L'esercizio riproduce esattamente l'esempio svolto alla lavagna: il mondo, il robot in $(2,1)$, il sensore $0{,}5$ m più avanti e il punto $P$. Si trova nella cartella degli esercizi, sotto la lezione 2 (modulo 1), nel file `planar.py`. Finché la funzione non è implementata, il simulatore segnala che il modulo non è ancora implementato e non mostra la posizione del punto.

La funzione riceve dall'interfaccia:

- la trasformazione dal robot al mondo (*world from robot*);
- la trasformazione dal sensore al robot (*robot from sensor*);
- il punto e la direzione osservati, espressi nella terna del sensore.

Deve restituire il punto e la direzione **espressi nel mondo**. Il README del repository riporta le equivalenze utili.

- Per passare a coordinate omogenee si aggiunge in coda un $1$ ai punti e uno $0$ alle direzioni (in NumPy, con `np.append`).
- Per tornare in coordinate cartesiane si scarta l'ultima componente.
- Il prodotto tra matrici in Python si scrive con l'operatore `@`.

Il risultato atteso è il punto in $(2,\ 2{,}5)$. Spostando il punto giallo nell'interfaccia si possono cambiare i dati del sensore (punto e direzione, cioè il vettore che va dal sensore al punto) e verificare la funzione su altri casi.

Una possibile implementazione, che segue passo per passo il ragionamento del paragrafo 8, è la seguente.

```python
import numpy as np

def sensor_to_world(world_from_robot, robot_from_sensor,
                    point_in_sensor, direction_in_sensor):
    # Composizione: i nomi "interni" (robot) si semplificano come gli indici
    world_from_sensor = world_from_robot @ robot_from_sensor   # ʷₛT = ʷᵦT ᵇₛT

    # Coordinate omogenee: 1 per i punti, 0 per le direzioni
    point_h = np.append(point_in_sensor, 1.0)
    direction_h = np.append(direction_in_sensor, 0.0)

    # Trasformazione e ritorno in coordinate cartesiane
    point_in_world = (world_from_sensor @ point_h)[:2]
    direction_in_world = (world_from_sensor @ direction_h)[:2]
    return point_in_world, direction_in_world


# Dati dell'esempio alla lavagna
world_from_robot = np.array([[0.0, -1.0, 2.0],
                             [1.0,  0.0, 1.0],
                             [0.0,  0.0, 1.0]])
robot_from_sensor = np.array([[1.0, 0.0, 0.5],
                              [0.0, 1.0, 0.0],
                              [0.0, 0.0, 1.0]])

p, d = sensor_to_world(world_from_robot, robot_from_sensor,
                       np.array([1.0, 0.0]), np.array([1.0, 0.0]))
print(p, d)   # [2.  2.5] [0. 1.]
```

> [!warning] Nomi indicativi
> I nomi della funzione e degli argomenti sono ricostruiti da quanto detto a lezione (*world from robot*, *robot from sensor*, *point/direction in sensor*). La firma effettiva in `planar.py` può essere diversa: fa fede il file del repository.

Il nome *world from robot* corrisponde alla notazione ${}^{w}_{b}T$: si legge «dal robot al mondo». Con questa convenzione di nomi la composizione `world_from_robot @ robot_from_sensor` si controlla come gli indici. Il nome «interno» (*robot*) deve comparire due volte di seguito e scompare dal risultato (*world from sensor*).
