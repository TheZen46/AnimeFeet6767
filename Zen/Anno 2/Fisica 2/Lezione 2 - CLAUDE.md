---

## corso: Fisica 2 lezione: 2 data: 2026-09-25 argomenti: [campo elettrico, carica di prova, linee di campo, campo di una carica puntiforme, principio di sovrapposizione, dipolo elettrico, momento di dipolo, esercizi legge di Coulomb] bibliography: fisica2.bib tags: [fisica2]

---
# Lezione 2 — Campo elettrico, dipolo elettrico ed esercizi sulla legge di Coulomb

La lezione si divide in due parti. Nella prima si introduce il **campo elettrico**, un modo più efficiente di descrivere l'elettrostatica rispetto al calcolo diretto delle forze tra coppie di cariche. Lo si applica alla carica puntiforme, a sistemi di più cariche e al **dipolo elettrico**, di cui si ricava il campo in forma quantitativa. Nella seconda parte si svolgono esercizi sulla legge di Coulomb, che servono anche da ripasso della scomposizione dei vettori. In apertura il docente ricorda che il teorema di Gauss verrà trattato "in maniera un po' sportiva": gli strumenti matematici necessari si sviluppano in parallelo nel corso di Metodi Matematici e non si possono dare per acquisiti.

## Riepilogo della lezione precedente

Il docente richiama i risultati della [[Fisica 2 - Lezione 01 - Carica elettrica e legge di Coulomb|lezione 1]]. Due cariche si attraggono o si respingono con una forza descritta quantitativamente dalla legge di Coulomb. La forza è direttamente proporzionale al valore assoluto delle cariche, quindi aumentando le cariche l'interazione si intensifica. Diminuisce invece allontanando le cariche (con l'inverso del quadrato della distanza). È sempre diretta lungo la congiungente: è repulsiva per cariche dello stesso segno e attrattiva per cariche di segno opposto. La legge soddisfa il principio di sovrapposizione: la forza netta su una carica è la somma delle forze che le altre cariche esercitano su di essa,

$$ \vec F_{1,\text{netta}} = \sum_{j=2}^{n} \vec F_{1,j}. $$

Il docente sottolinea subito il punto critico: essendo vettori, queste forze vanno sommate **vettorialmente**, tenendo conto di tutte le direzioni, ed è lì che si commettono più errori.

## Dal concetto di forza al concetto di campo

La descrizione tramite forza di Coulomb e sovrapposizione funziona perfettamente per l'elettrostatica, ma può essere laboriosa. Per calcolare la forza tra due cariche serve conoscere entrambe le cariche e la loro distanza. In un sistema complesso bisogna conoscere tutto: ogni carica e ogni posizione. Si è scoperto che esiste un modo più efficace di descrivere l'elettrostatica, attraverso i **campi**.

L'idea è descrivere che cosa succede nello spazio senza dover sapere come quella situazione è stata generata. Si prende una **carica di prova** $q_0$, la si colloca in un punto dello spazio e si osserva come si muove. Dal suo moto si ricava la forza che agisce su di essa. Rispetto alla descrizione basata su Coulomb, si "cancella" l'informazione sulle sorgenti: non interessa, o non si conosce, come sia stato prodotto il campo. Basta sapere che una carica di prova posta in quel punto risente di una certa forza. La base resta sempre la legge di Coulomb, ma la descrizione diventa molto più agile. Vedremo che si applica anche a distribuzioni continue di carica, come fili o piani carichi, che non si possono trattare come un elenco finito di cariche puntiformi.

> [!important] Definizione di campo elettrico Il campo elettrico in un punto dello spazio è la forza che agirebbe su una carica di prova $q_0$ posta in quel punto, divisa per la carica di prova stessa: $$ \vec E = \frac{\vec F}{q_0} \qquad\Longleftrightarrow\qquad \vec F = q_0,\vec E $$ Dalla definizione segue che il campo elettrico si misura in $\mathrm{N/C}$.

Il campo elettrico è quindi un altro modo di rappresentare la stessa fisica. È definito in ogni punto dello spazio, e la relazione $\vec F = q_0\vec E$ lega in modo diretto, si potrebbe dire sperimentale, la forza sulla carica di prova al campo presente in quel punto.

> [!tip] Approfondimento — Perché la carica di prova deve essere "piccola" #approfondimento Nelle trattazioni standard si precisa che la carica di prova deve essere abbastanza piccola da non perturbare la distribuzione delle cariche che generano il campo. In un conduttore, ad esempio, avvicinare una carica fa ridistribuire le cariche mobili, come nel fenomeno della carica indotta. Con questa cautela il campo $\vec E$ è una proprietà dello spazio creata dalle sorgenti e non dipende da $q_0$, che serve solo a misurarlo.

## Le linee di campo

Per visualizzare un campo si usano le **linee di campo**, una rappresentazione introdotta da Faraday. Per convenzione le linee di campo elettrico **escono dalle cariche positive** ed **entrano nelle cariche negative**. Danno un'idea immediata di come si comporterebbe una carica di prova positiva immersa nel campo. Vicino a una carica negativa la carica di prova viene attratta, e infatti le linee puntano verso la carica negativa. Vicino a una carica positiva viene respinta, e le linee puntano in verso uscente. Per una carica puntiforme isolata, per simmetria, le linee sono **radiali**: semirette uscenti dalla carica se positiva, entranti se negativa.

Questa rappresentazione è qualitativa: la descrizione quantitativa resta $\vec E = \vec F/q_0$, e per avere i valori bisogna calcolare esplicitamente il campo. Le linee contengono però un'altra informazione, anche questa riconducibile a un dato quantitativo. Le linee si disegnano per convenzione in modo che la loro **densità** rispecchi l'intensità del campo: dove sono più fitte il campo è più intenso. Si prenda una piccola superficie vicino a una carica puntiforme e la si attraversi con le linee: vicino alla carica ne passano, ad esempio, due; la stessa superficie posta più lontano ne intercetta una sola. Il campo è più intenso vicino alla carica, coerentemente con la legge di Coulomb. L'idea di contare le linee che attraversano una superficie anticipa il concetto di **flusso**, alla base del teorema di Gauss.

> [!tip] Approfondimento — Linee di campo e traiettorie #approfondimento In ogni punto la linea di campo è tangente al vettore $\vec E$, quindi indica la direzione e il verso della forza su una carica di prova positiva. In generale, però, non coincide con la traiettoria della carica. La forza determina l'accelerazione, non la velocità, quindi una carica che ha già una velocità può discostarsi dalla linea. Le due cose coincidono in casi semplici, come una carica che parte da ferma in un campo con linee rettilinee.

### Il piano carico infinito: un campo uniforme

Un caso molto meno banale della carica puntiforme è quello di un **piano infinito carico** in modo uniforme. Si può dimostrare che le linee di campo sono **ortogonali al piano**: uscenti se il piano è carico positivamente, entranti se è carico negativamente. Soprattutto, il campo è **uniforme**: non dipende dalla distanza dal piano ed è costante nello spazio.

Questo risultato non si ricava immediatamente dalla legge di Coulomb. Si ottiene suddividendo il piano in elementi piccoli, trattando ciascuno come una carica puntiforme e sommando i contributi con un integrale. Il calcolo è svolto nella [[Fisica 2 - Lezione 03 - Distribuzioni continue di carica|lezione 3]], come limite del disco carico, e dà $E = 2\pi k\sigma = \sigma/(2\varepsilon_0)$. In alternativa lo si ottiene con il teorema di Gauss, che vedremo. In entrambi i casi è decisivo un argomento di simmetria: le componenti del campo parallele al piano si compensano, e resta solo quella ortogonale.

Il risultato ha un'importanza pratica. Il campo di una carica puntiforme decresce rapidamente allontanandosi, come l'inverso del quadrato della distanza. Se si vuole un campo **costante**, il modo è caricare un piano. Un piano reale non è infinito, ma se è abbastanza grande e ci si trova vicino a esso, lontano dai bordi, lo si "vede" come infinito e il campo generato è praticamente uniforme. Questi risultati permettono, come dice il docente, di "bypassare" in parte la legge di Coulomb e ragionare più velocemente: se serve un campo costante, si costruisce un piano carico.

> [!warning] Discrepanza negli appunti a mano Accanto al disegno dei piani carichi, negli appunti a mano compare la dicitura "campo elettrico infinito". Secondo la trascrizione è **infinito il piano**, mentre il campo che genera è **uniforme**: costante in modulo, direzione e verso, e finito.

## Il campo di una carica puntiforme

Il caso più semplice si ricava subito dalla definizione. Si consideri una carica $q_1$ e una carica di prova $q_0$ posta a distanza $r$. La forza su $q_0$ è data dalla legge di Coulomb; dividendo per $q_0$:

$$ \vec E = \frac{\vec F}{q_0} = k,\frac{q_0, q_1}{r^2},\hat r \cdot \frac{1}{q_0} = k,\frac{q_1}{r^2},\hat r . $$

> [!important] Campo elettrico di una carica puntiforme $$ \vec E = k,\frac{q}{r^2},\hat r, \qquad |\vec E| = k,\frac{|q|}{r^2} $$ dove $\hat r$ è il versore diretto dalla carica sorgente verso il punto in cui si calcola il campo. Per $q>0$ il campo è uscente, per $q<0$ entrante.

La carica di prova si semplifica, e il campo dipende solo dalla carica che lo genera. Il campo eredita le proprietà della forza di Coulomb. Decresce come $1/r^2$, quindi più ci si allontana più si indebolisce. È **radiale**: dipende solo dalla distanza dalla carica e, a distanza fissata, la sua intensità non dipende dall'angolo. È una conseguenza diretta della struttura della legge di Coulomb, che dipende solo dalla distanza tra le due cariche.

### Coordinate radiali e angolari

Per descrivere situazioni come questa conviene usare coordinate adatte alla simmetria del problema. Nel piano, al posto delle coordinate cartesiane $(x,y)$, un punto si può individuare con una **coordinata radiale**, la distanza dall'origine, e una **coordinata angolare**: sono le **coordinate polari**. Nello spazio servono una coordinata radiale e due angolari: sono le **coordinate sferiche**. Con questo linguaggio, il campo di una carica puntiforme posta nell'origine dipende solo dalla coordinata radiale $r$ e non dalle coordinate angolari. Questa descrizione servirà più avanti.

> [!tip] Approfondimento — Richiamo sulle trasformazioni di coordinate #approfondimento Coordinate polari: $x = r\cos\theta$, $y = r\sin\theta$, con $r \ge 0$ e $\theta \in [0, 2\pi)$. Coordinate sferiche (convenzione più diffusa in fisica): $x = r\sin\theta\cos\varphi$, $y = r\sin\theta\sin\varphi$, $z = r\cos\theta$, con $\theta \in [0,\pi]$ angolo dall'asse $z$ e $\varphi \in [0,2\pi)$ angolo nel piano $xy$.

## Il principio di sovrapposizione per il campo elettrico

Il principio di sovrapposizione, valido per le forze di Coulomb, vale anche per il campo elettrico, come conseguenza diretta del primo. Si consideri una carica di prova $q_0$ e un insieme di $n$ cariche $q_1, q_2, \dots, q_n$. La forza totale su $q_0$ è la somma delle forze dovute alle singole cariche:

$$ \vec F_0 = \sum_{i=1}^{n} \vec F_{0,i}. $$

Dividendo entrambi i membri per $q_0$, a sinistra compare per definizione il campo elettrico nel punto in cui si trova $q_0$. A destra compare la somma dei campi generati dalle singole cariche:

$$ \frac{\vec F_0}{q_0} = \sum_{i=1}^{n}\frac{\vec F_{0,i}}{q_0} \qquad\Longrightarrow\qquad \vec E = \sum_{i=1}^{n} \vec E_i . $$

> [!important] Principio di sovrapposizione per il campo elettrico Il campo elettrico generato da un insieme di cariche in un punto è la **somma vettoriale** dei campi generati in quel punto dalle singole cariche: $$ \vec E = \vec E_1 + \vec E_2 + \dots + \vec E_n = \sum_{i=1}^{n} \vec E_i . $$

Operativamente, per calcolare il campo in un punto si immagina di collocarvi una carica di prova e si calcola, carica per carica, il campo generato. Ognuno è radiale rispetto alla propria carica sorgente, con modulo $k|q_i|/r_i^2$. Poi si sommano i vettori. Nell'esempio della lezione ci sono tre cariche, con la carica 2 negativa. Il campo dovuto alla carica 1 punta in verso uscente rispetto a essa; quello dovuto alla carica 2 punta verso la carica 2, perché entra nelle cariche negative; quello dovuto alla carica 3 è di nuovo radiale rispetto alla 3. Il campo totale si ottiene sommando i primi due con la regola del parallelogramma e poi la risultante con il terzo.

## Il campo di due cariche: analisi qualitativa

Prima del calcolo quantitativo, conviene capire qualitativamente come si combinano i campi di due cariche puntiformi. Si ragiona punto per punto: in ogni punto si sommano vettorialmente $\vec E_1$ ed $\vec E_2$.

### Due cariche positive uguali

Sulla congiungente, nel tratto tra le due cariche, i due campi hanno verso opposto: ciascuno punta via dalla propria carica sorgente. Se le cariche sono uguali, nel punto medio i due campi hanno anche lo stesso modulo e si annullano: il campo totale è **nullo**. Se le cariche sono diverse, la cancellazione non avviene più nel punto medio. Il punto di campo nullo si sposta verso la carica di modulo minore, perché per compensare una carica più piccola bisogna esserle più vicini. Sulla congiungente ma all'esterno del segmento, invece, i due campi hanno lo stesso verso e si **sommano**.

Le linee di campo, vicino a ciascuna carica, sono quasi radiali, come per una carica isolata. Allontanandosi si incurvano, come se si respingessero a vicenda. Nella zona centrale il campo è più debole: le linee sono meno fitte, cioè, per quanto detto sulla densità, meno linee attraversano la stessa superficie.

### Una carica positiva e una carica negativa

Se le cariche hanno segno opposto, le linee **escono dalla carica positiva ed entrano nella carica negativa**: collegano direttamente le due cariche. Nel tratto intermedio della congiungente i due campi hanno ora lo stesso verso, perché entrambi puntano dalla carica positiva verso quella negativa, e quindi si **sommano**. È la configurazione più generale di una coppia di cariche di segno opposto. Il caso particolare in cui le due cariche hanno lo stesso modulo è il dipolo elettrico, che ora si tratta in modo quantitativo.

> [!tip] Schema consigliato L'andamento delle linee di campo per due cariche uguali e per due cariche opposte è difficile da rendere a parole. Uno schizzo in Excalidraw dei due casi affiancati è utile; un primo abbozzo è nella seconda pagina dei tuoi appunti a mano. Va bene anche la figura corrispondente di un qualsiasi testo di Fisica 2.

## Il dipolo elettrico

> [!important] Definizione di dipolo elettrico Un **dipolo elettrico** è un sistema di due cariche puntiformi di uguale modulo e segno opposto, $|q_+| = |q_-| = q$, poste a distanza $d$ l'una dall'altra.

### Impostazione del calcolo

Il calcolo del campo in un punto generico è complicato, ma diventa semplice in un punto dell'**asse del dipolo**, cioè della retta che congiunge le due cariche. Si orienta l'asse $z$ dalla carica negativa verso quella positiva e si pone l'origine nel centro del dipolo. La carica positiva si trova quindi in $z = +d/2$ e quella negativa in $z = -d/2$. Si calcola il campo nel punto $P$ dell'asse a distanza $z$ dal centro, dalla parte della carica positiva, con $z > d/2$.

La carica positiva genera in $P$ un campo uscente, diretto lungo $+z$. La carica negativa genera un campo entrante, diretto verso di essa, cioè lungo $-z$. I due campi hanno la stessa direzione e versi opposti. Il punto $P$ è più vicino alla carica positiva; a parità di carica e con il campo che scala come $1/r^2$, il campo della carica positiva prevale. Il campo risultante è quindi diretto lungo $+z$.

### Una nota di metodo: proiettare sugli assi

Scrivere $E = E_+ - E_-$ contiene già un passaggio mentale importante, che il docente invita a rendere esplicito, perché è proprio qui che si sbaglia negli esercizi. Il campo è un vettore, quindi in principio la somma è vettoriale. Il problema però è unidimensionale, e si può proiettare tutto su un asse. Una volta fissato l'asse $z$, si attribuisce a ogni campo un segno secondo il suo verso rispetto all'asse: $E_+$ con il segno più, perché concorde con $z$, ed $E_-$ con il segno meno, perché discorde. Da quel momento $E_+$ ed $E_-$ indicano **moduli**, e non bisogna più preoccuparsi del segno delle cariche, perché il verso è già stato incorporato nel segno della proiezione. Per i moduli si usa quindi

$$ |\vec E| = k,\frac{|q|}{r^2}. $$

### Calcolo

Le distanze di $P$ dalle due cariche sono $z - \tfrac d2$ dalla positiva e $z + \tfrac d2$ dalla negativa. Quindi

$$ E_+ = k,\frac{q}{\left(z-\frac d2\right)^2}, \qquad E_- = k,\frac{q}{\left(z+\frac d2\right)^2}. $$

Raccogliendo $kq$ e portando le frazioni a denominatore comune:

$$ \begin{aligned} E = E_+ - E_- &= \frac{kq}{\left(z-\frac d2\right)^2} - \frac{kq}{\left(z+\frac d2\right)^2} = kq,\frac{\left(z+\frac d2\right)^2 - \left(z-\frac d2\right)^2}{\left(z-\frac d2\right)^2\left(z+\frac d2\right)^2} \[4pt] &= kq,\frac{\left(z^2 + zd + \frac{d^2}{4}\right) - \left(z^2 - zd + \frac{d^2}{4}\right)}{\left(z^2-\frac{d^2}{4}\right)^2} = \frac{2kq,d,z}{\left(z^2-\frac{d^2}{4}\right)^2}. \end{aligned} $$

Al numeratore si sviluppano i quadrati: i termini $z^2$ e $d^2/4$ si elidono, mentre i doppi prodotti $\pm zd$ diventano entrambi positivi, perché il segno meno davanti alla seconda parentesi cambia $-zd$ in $+zd$. Al denominatore si usa il prodotto notevole $(a-b)(a+b) = a^2 - b^2$: il prodotto dei due quadrati è il quadrato del prodotto, $\left(z-\frac d2\right)^2\left(z+\frac d2\right)^2 = \left[\left(z-\frac d2\right)\left(z+\frac d2\right)\right]^2 = \left(z^2 - \frac{d^2}{4}\right)^2$.

> [!important] Campo del dipolo sull'asse (espressione esatta) $$ E = \frac{2kq,d,z}{\left(z^2-\dfrac{d^2}{4}\right)^2}, \qquad z > \frac d2 $$ Il campo è diretto lungo l'asse, dalla carica negativa verso quella positiva.

Questa è la versione quantitativa del campo, a differenza della rappresentazione con le linee: fornisce il valore esatto in ogni punto dell'asse. Il docente lo sottolinea: fisica e ingegneria sono scienze quantitative, non qualitative.

### Approssimazione a grande distanza e momento di dipolo

Esiste un'espressione semplificata, ottenuta con un'approssimazione analoga a quelle viste negli sviluppi di Taylor. Ci si mette nel caso in cui la distanza $z$ sia molto maggiore della distanza $d$ tra le cariche: il dipolo è piccolo e lo si osserva da lontano, così che le due cariche appaiono vicinissime.

Prima si riscrive l'espressione esatta in modo equivalente, **senza ancora approssimare**. Si raccoglie $z^2$ dentro la parentesi del denominatore; essendo la parentesi al quadrato, ne esce $z^4$:

$$ E = \frac{2kq,d,z}{z^4\left(1-\dfrac{d^2}{4z^2}\right)^2} = \frac{2kq,d}{z^3\left(1-\dfrac{d^2}{4z^2}\right)^2}. $$

Ora si usa l'ipotesi $z \gg d$. Allora $d/z$ è molto minore di 1, e a maggior ragione lo è $d^2/z^2$, perché un numero minore di 1 elevato al quadrato diventa ancora più piccolo. Il termine $d^2/(4z^2)$ è trascurabile rispetto a 1, e la parentesi al denominatore vale praticamente 1:

$$ E \simeq \frac{2kq,d}{z^3} \qquad (z \gg d). $$

In questa approssimazione il dipolo entra nel campo solo attraverso il prodotto $qd$. È naturale quindi introdurre una grandezza che lo caratterizza da sola.

> [!important] Momento di dipolo elettrico e campo a grande distanza Il **momento di dipolo elettrico** è $$ p = q,d \qquad [\mathrm{C\cdot m}] $$ e, a grande distanza sull'asse del dipolo, $$ E \simeq \frac{2k,p}{z^3} \qquad (z \gg d). $$

Il campo del dipolo a grande distanza decresce come $1/z^3$, più rapidamente del campo di una singola carica, che va come $1/z^2$. Il motivo è fisico: visto da lontano il dipolo è complessivamente neutro, i campi delle due cariche sono quasi uguali e opposti, e ne resta solo la piccola differenza dovuta alla diversa distanza. Il momento di dipolo contiene tutta l'informazione necessaria a descrivere il campo a grandi distanze. Per questo negli esercizi il dipolo è spesso caratterizzato direttamente dal valore di $p$, invece che da $q$ e $d$ separatamente.

Il primo grafico mostra quanto è buona l'approssimazione. Riporta il rapporto tra campo esatto e campo approssimato in funzione di $z/d$: a $z = d$ il campo esatto supera di quasi l'80% quello approssimato, a $z = 3d$ la differenza scende sotto il 6%, a $z = 10d$ è dello 0,5%.

```chart
type: line
labels: [1, 1.5, 2, 3, 4, 5, 6, 8, 10]
series:
  - title: E esatto / E approssimato (in funzione di z/d)
    data: [1.778, 1.266, 1.138, 1.058, 1.032, 1.020, 1.014, 1.008, 1.005]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: false
```

Il secondo grafico confronta, in unità di $kq/d^2$, il campo di una carica isolata $q$ ($1/u^2$, con $u = z/d$) con il campo esatto del dipolo sull'asse. Vicino al dipolo il campo del dipolo è più intenso, perché il punto è prossimo alla carica positiva. Allontanandosi, però, decresce molto più rapidamente.

```chart
type: line
labels: [2, 3, 4, 5, 6, 8, 10]
series:
  - title: Carica isolata (1/u^2)
    data: [0.2500, 0.1111, 0.0625, 0.0400, 0.0278, 0.0156, 0.0100]
  - title: Dipolo, campo esatto sull'asse
    data: [0.2844, 0.0784, 0.0322, 0.0163, 0.0094, 0.0039, 0.0020]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: true
```

> [!tip] Approfondimento — Il momento di dipolo come vettore e la prima correzione #approfondimento Nei testi standard il momento di dipolo è definito come vettore, $\vec p = q,\vec d$, con $\vec d$ diretto dalla carica negativa a quella positiva. Con questa convenzione, sull'asse e dalla parte della carica positiva il campo ha lo stesso verso di $\vec p$, come trovato sopra. Il termine trascurato si può anche stimare. Con lo sviluppo $(1-x)^{-2} \simeq 1 + 2x$ per $x \ll 1$, ponendo $x = d^2/(4z^2)$, si ottiene $$ E \simeq \frac{2kp}{z^3}\left(1 + \frac{d^2}{2z^2}\right), $$ che mostra esplicitamente come la correzione relativa vada a zero come $(d/z)^2$.

> [!warning] Discrepanze negli appunti (.md) sul dipolo Nel file "Campo elettrico.md" ci sono alcuni refusi, assenti invece negli appunti a mano:
> 
> - la seconda riga delle definizioni riporta $E_+ = Kq/(Z+\frac d2)^2$, ma quella espressione è $E_-$;
> - nel raccoglimento compare $\left(1-\frac{d^2}{4Z}\right)^2$ invece di $\left(1-\frac{d^2}{4Z^2}\right)^2$: raccogliendo $z^2$ il termine diventa $d^2/(4z^2)$;
> - la riga "Punto per punto $\hat E = \hat E_1 + \hat E_2$" usa i versori, ma la somma riguarda i vettori campo, $\vec E = \vec E_1 + \vec E_2$, non i versori.

## Esercizi sulla legge di Coulomb

La seconda parte della lezione è dedicata agli esercizi. Il docente avverte che sono prima di tutto un ripasso di come si trattano i vettori: scelta degli assi, proiezioni e segni.

### Due regole di metodo

**Scelta degli assi e proiezioni.** Gli assi di riferimento sono arbitrari, e ciascuno può scegliere quelli che preferisce. Una volta scelti, però, si è vincolati a quella convenzione: ogni forza va proiettata su quegli assi, con il segno corretto rispetto al loro orientamento. Con una sola forza un errore di segno ha conseguenze limitate. Con due o tre forze, dimenticare un segno significa sottrarre forze che andavano sommate, o viceversa, e il risultato è sbagliato. Scegliere assi poco adatti al problema non è un errore, ma complica i conti, perché bisogna proiettare su più componenti del necessario. Infine, se si chiede una forza, va data come vettore: in componenti, oppure con modulo, direzione e verso. Il solo modulo non basta.

**Analisi dimensionale.** È un controllo "alla cieca" da fare sempre. Se a sinistra c'è una forza, a destra devono comparire newton; una carica va in coulomb, una corrente in ampere, una tensione in volt. Non si possono sommare newton e ampere. Se semplificando le unità non si ottiene quella attesa, è un segnale sicuro di errore, ad esempio un termine dimenticato o aggiunto. È un controllo semplice, ma secondo il docente distingue spesso un esercizio giusto da uno sbagliato.

### Esercizio 1 — Forza tra due cariche positive

> [!example] Esercizio 1a Due cariche positive $q_1 = 1{,}6\times10^{-19}\ \mathrm C$ e $q_2 = 3{,}2\times10^{-19}\ \mathrm C$ si trovano a distanza $r = 0{,}2\ \mathrm m$. Determinare la forza $\vec F_{1,2}$ che agisce sulla carica 1 per effetto della carica 2.
> 
> **Ragionamento.** La forza è diretta lungo la congiungente. Le cariche sono entrambe positive, quindi la forza è repulsiva: sulla carica 1 punta in verso opposto alla carica 2. Il problema è unidimensionale e basta un asse. Si sceglie l'asse $x$ orientato dalla carica 1 verso la carica 2. Con questa scelta la forza sulla carica 1 è diretta contro l'asse e la sua componente è negativa: $$ \vec F_{1,2} = -k,\frac{q_1,q_2}{r^2},\hat\imath . $$ **Calcolo.** $$ F_{1,2} = 8{,}99\times10^{9}\ \frac{\mathrm{N,m^2}}{\mathrm{C^2}}\cdot\frac{(1{,}6\times10^{-19}\ \mathrm C)(3{,}2\times10^{-19}\ \mathrm C)}{(0{,}2\ \mathrm m)^2} $$ Il prodotto delle cariche vale $5{,}12\times10^{-38}\ \mathrm{C^2}$; diviso per $0{,}04\ \mathrm{m^2}$ dà $1{,}28\times10^{-36}\ \mathrm{C^2/m^2}$; moltiplicato per $k$ dà $$ \vec F_{1,2} = -1{,}15\times10^{-26}\ \mathrm N\ \hat\imath . $$ **Controllo dimensionale.** $\dfrac{\mathrm{N,m^2}}{\mathrm{C^2}}\cdot\dfrac{\mathrm C\cdot\mathrm C}{\mathrm{m^2}} = \mathrm N$: le unità si semplificano e resta il newton, come deve essere.

> [!warning] Discrepanza sull'ordine di grandezza Negli appunti (.md e a mano) il risultato è $-1{,}15\times10^{-24}\ \mathrm N$; nella trascrizione l'esponente non si sente. Il ricalcolo con i dati dell'esercizio dà $1{,}15\times10^{-26}\ \mathrm N$. Gli esponenti valgono $9 - 19 - 19 = -29$, e la divisione per $0{,}04$ moltiplica per $25$: $8{,}99 \cdot 1{,}6 \cdot 3{,}2 \cdot 25 \simeq 1151$, da cui $1151\times10^{-29}\ \mathrm N = 1{,}15\times10^{-26}\ \mathrm N$. Di conseguenza vanno corretti di un fattore 100 anche i risultati numerici dei punti successivi. Nel file "Elettrostatica - Esercizi.md", inoltre, i dati riportano $10^{-13}\ \mathrm C$ invece di $10^{-19}\ \mathrm C$, mentre il calcolo usa correttamente $10^{-19}$.

> [!example] Esercizio 1b — Aggiunta di una carica negativa Si aggiunge una terza carica $q_3 = -q_2$ sulla congiungente, tra le due cariche, a distanza $\tfrac34 r$ dalla carica 1. Determinare la forza netta sulla carica 1.
> 
> **Ragionamento.** Per il principio di sovrapposizione la forza netta è la somma di $\vec F_{1,2}$ e $\vec F_{1,3}$. Il sistema è ancora unidimensionale e si proietta sullo stesso asse $x$. Ora però i segni non sono più indifferenti: con due forze, a seconda del verso, si sommano o si sottraggono. $\vec F_{1,2}$ è repulsiva e diretta lungo $-x$, come prima. $\vec F_{1,3}$ è attrattiva, perché $q_1>0$ e $q_3<0$, quindi è diretta verso la carica 3, cioè lungo $+x$. Si ha allora $$ F_{1,\text{netta}} = F_{1,3} - F_{1,2} = \frac{k,q_1,q_2}{\left(\frac34 r\right)^2} - \frac{k,q_1,q_2}{r^2}. $$ Nel primo termine compare $q_2$ invece di $|q_3|$ perché le due cariche hanno lo stesso modulo.
> 
> **Calcolo.** Poiché $\left(\tfrac34\right)^2 = \tfrac{9}{16}$, invertendo si ottiene $\tfrac{16}{9}$: $$ F_{1,\text{netta}} = \left(\frac{16}{9} - 1\right)\frac{k,q_1,q_2}{r^2} = \frac{7}{9},F_{1,2} = \frac79\cdot 1{,}15\times10^{-26}\ \mathrm N \simeq 8{,}95\times10^{-27}\ \mathrm N, $$ diretta lungo $+x$, cioè $\vec F_{1,\text{netta}} \simeq +8{,}95\times10^{-27}\ \mathrm N\ \hat\imath$.
> 
> **Controllo intuitivo.** Le cariche 2 e 3 hanno lo stesso modulo, ma la 3 è più vicina alla carica 1. L'attrazione verso la 3 deve quindi essere più intensa della repulsione dalla 2, e la forza netta deve puntare verso $+x$. Il risultato lo conferma: $16/9 > 1$.

Durante l'esercizio uno studente ha chiesto perché nella formula compaia $q_2$ anziché $q_3$. La risposta del docente chiarisce un punto di metodo importante. Quando si scrive $F_{1,3} - F_{1,2}$, i segni sono **già stati fissati** dalla proiezione sull'asse: il verso attrattivo di $\vec F_{1,3}$ è contenuto nel segno più davanti al termine. Da quel momento tutte le cariche vanno inserite **in modulo**. Si potrebbe scrivere $q_3$, ma bisognerebbe ricordarsi che $q_3$ è negativa e usarne il modulo, altrimenti si conterebbe il segno due volte e si invertirebbe il verso della forza. Visto che $|q_3| = q_2$, scrivere direttamente $q_2$ evita l'errore.

Il controllo intuitivo non è sempre possibile. Se il valore di $q_3$ fosse diverso da quello di $q_2$, non si potrebbe dire a priori quale forza prevale: la carica 3 è più vicina, ma il risultato dipenderebbe dal suo valore. In questo caso il confronto era immediato.

> [!example] Esercizio 1c — La terza carica fuori dall'asse La carica $q_3 = -q_2$ viene ruotata attorno alla carica 1 di un angolo $\theta = 60^\circ$, mantenendo la distanza $\tfrac34 r$. Determinare la forza netta sulla carica 1.
> 
> **Ragionamento.** Ora il problema è bidimensionale: servono gli assi $x$ (verso la carica 2) e $y$, con i rispettivi versori $\hat\imath$ e $\hat\jmath$. Il modulo di $\vec F_{1,3}$ non cambia, perché la distanza è la stessa: $$ |\vec F_{1,3}| = \frac{k,|q_1|,|q_3|}{\left(\frac34 r\right)^2} = \frac{16}{9},\frac{k,|q_1|,|q_2|}{r^2} = \frac{16}{9},F_{1,2}. $$ La forza è attrattiva, quindi diretta dalla carica 1 verso la carica 3, a $60^\circ$ dall'asse $x$. Le sue componenti si ricavano dal triangolo rettangolo che ha $\vec F_{1,3}$ come ipotenusa: il cateto adiacente all'angolo è la componente $x$ e quello opposto è la componente $y$: $$ F_{1,3}^{x} = F_{1,3}\cos\theta, \qquad F_{1,3}^{y} = F_{1,3}\sin\theta \quad\Longrightarrow\quad \vec F_{1,3} = F_{1,3}\cos\theta\ \hat\imath + F_{1,3}\sin\theta\ \hat\jmath . $$ Per sommare correttamente anche $\vec F_{1,2}$ va scritta in forma vettoriale. Ha solo componente lungo $x$, negativa: $\vec F_{1,2} = -F_{1,2},\hat\imath$.
> 
> **Somma vettoriale.** Si sommano separatamente le componenti lungo $\hat\imath$ e lungo $\hat\jmath$: $$ \begin{aligned} \vec F_{1,\text{netta}} = \vec F_{1,2} + \vec F_{1,3} &= \left(F_{1,3}\cos\theta - F_{1,2}\right)\hat\imath + F_{1,3}\sin\theta\ \hat\jmath \ &= \left(\frac{16}{9}\cos\theta - 1\right)F_{1,2}\ \hat\imath + \frac{16}{9}\sin\theta, F_{1,2}\ \hat\jmath . \end{aligned} $$ **Calcolo.** Con $\cos 60^\circ = \tfrac12$ e $\sin 60^\circ = \tfrac{\sqrt3}{2}$ i coefficienti valgono $\tfrac{16}{9}\cdot\tfrac12 - 1 = \tfrac89 - 1 = -\tfrac19$ e $\tfrac{16}{9}\cdot\tfrac{\sqrt3}{2} = \tfrac{8\sqrt3}{9} \simeq 1{,}54$: $$ \vec F_{1,\text{netta}} = -\frac{1}{9}F_{1,2}\ \hat\imath + \frac{8\sqrt3}{9}F_{1,2}\ \hat\jmath \simeq \left(-1{,}28\times10^{-27}\ \hat\imath + 1{,}77\times10^{-26}\ \hat\jmath\right)\mathrm N . $$ In modulo, $|\vec F_{1,\text{netta}}| \simeq 1{,}78\times10^{-26}\ \mathrm N$, con un angolo di circa $94^\circ$ rispetto all'asse $+x$: la forza è diretta quasi lungo $+y$, leggermente inclinata verso $-x$.

> [!warning] Discrepanza sul segno della componente $x$ Nella trascrizione il docente afferma che le componenti $x$ e $y$ "sono entrambe positive". Il file "Elettrostatica - Esercizi.md" riporta $+1{,}25\times10^{-25}\ \mathrm N\ \hat\imath + 1{,}78\times10^{-24}\ \mathrm N\ \hat\jmath$. Negli appunti a mano il termine lungo $\hat\jmath$ è scritto $|F_{1,2}|\sin\theta$, senza il fattore $\tfrac{16}{9}$. Con i dati dell'esercizio, invece, il coefficiente della componente $x$ è $\tfrac{16}{9}\cos60^\circ - 1 = -\tfrac19 < 0$. La proiezione orizzontale dell'attrazione verso la carica 3, pari a $\tfrac89 F_{1,2}$, è leggermente minore della repulsione dalla carica 2, $F_{1,2}$. Il termine in $\hat\jmath$ deve contenere $F_{1,3} = \tfrac{16}{9}F_{1,2}$. Gli ordini di grandezza corretti sono quelli indicati sopra, discussi nella discrepanza dell'esercizio 1a. Conviene verificare il testo esatto del problema; se l'angolo fosse diverso da $60^\circ$, il segno potrebbe cambiare.

Il docente sottolinea un'ultima volta che il risultato va dato come vettore. La forma $F_x,\hat\imath + F_y,\hat\jmath$ contiene tutta l'informazione su modulo, direzione e verso. Dare solo il modulo significa perdere l'informazione su dove punta la forza.

### Esercizio 2 — Posizione di equilibrio di una terza carica

> [!example] Esercizio 2 Due cariche $q_1 = 8q$ e $q_2 = -2q$, con $q>0$, si trovano a distanza $L$. La carica 1 è positiva e la carica 2 negativa, con $|q_1/q_2| = 4$. Si aggiunge una terza carica positiva $Q$ sulla retta che congiunge le due. Esiste una posizione in cui $Q$ è in equilibrio, cioè in cui le forze esercitate su di essa da $q_1$ e da $q_2$ sono uguali e opposte?

Esprimere entrambe le cariche in funzione della stessa carica arbitraria $q>0$ serve solo a riscalarle: ciò che conta è il rapporto $|q_1/q_2| = 4$. Il valore di $Q$ non conta, perché entrambe le forze sono proporzionali a $Q$ e nella condizione di equilibrio si semplifica. A lezione il docente pone la carica aggiuntiva uguale a $q$, ma il risultato non cambia. La carica $Q$ può trovarsi in tre regioni: tra le due cariche, a sinistra di $q_1$ o a destra di $q_2$. La distanza è incognita, quindi ogni caso va esaminato con una variabile libera. Si orienta l'asse $x$ da $q_1$ verso $q_2$.

**Caso 1: $Q$ tra le due cariche.** La carica $q_1$, positiva, respinge $Q$ verso destra. La carica $q_2$, negativa, attrae $Q$ verso di sé, cioè ancora verso destra. Le due forze hanno lo stesso verso e non possono bilanciarsi, in qualunque punto del segmento si ponga $Q$. Non c'è equilibrio, e non serve fare conti.

**Caso 2: $Q$ a sinistra di $q_1$.** Sia $x>0$ la distanza di $Q$ da $q_1$; la distanza da $q_2$ è $x+L$. La forza di $q_1$ è repulsiva e spinge $Q$ verso sinistra, $-x$. La forza di $q_2$ è attrattiva e la tira verso destra, $+x$. I versi sono opposti, quindi in linea di principio l'equilibrio è possibile. Non è però evidente, perché le cariche sono diverse: una carica molto intensa, anche se lontana, potrebbe bilanciare una carica più debole ma più vicina. Proiettando sull'asse e usando i moduli delle cariche, perché i segni sono già stati attribuiti:

$$ F = -\frac{k,Q,(8q)}{x^2} + \frac{k,Q,(2q)}{(x+L)^2} = 0 . $$

Si semplificano $k$, $Q$ e $q$, e si divide per 2:

$$ \frac{4}{x^2} = \frac{1}{(x+L)^2} \quad\Longrightarrow\quad (x+L)^2 = \frac{x^2}{4} \quad\Longrightarrow\quad x + L = \frac{x}{2} \quad\Longrightarrow\quad x = -2L . $$

Nell'estrarre la radice si prende il segno positivo, perché $x$ e $x+L$ sono distanze, quindi positive. Il risultato $x = -2L$ è negativo, ma $x$ è per definizione una distanza: è una **contraddizione**, e a sinistra di $q_1$ non esiste posizione di equilibrio. Anche la radice negativa, $x + L = -x/2$, porta a un valore negativo, $x = -\tfrac{2}{3}L$, e va scartata. Il risultato ha una lettura intuitiva: in questa regione la carica più vicina, $q_1$, è anche la più intensa, quindi la sua repulsione prevale sempre.

**Caso 3: $Q$ a destra di $q_2$.** Sia ora $x>0$ la distanza di $Q$ da $q_2$; la distanza da $q_1$ è $x+L$. La forza di $q_1$ è repulsiva e spinge $Q$ verso destra, $+x$. La forza di $q_2$ è attrattiva e la tira verso sinistra, $-x$. Anche qui i versi sono opposti, e ora la carica più vicina, $q_2$, è la più debole. L'equilibrio è quindi plausibile, e la conferma deve venire dal calcolo:

$$ F = \frac{k,Q,(8q)}{(x+L)^2} - \frac{k,Q,(2q)}{x^2} = 0 \quad\Longrightarrow\quad \frac{4}{(x+L)^2} = \frac{1}{x^2} \quad\Longrightarrow\quad 4x^2 = (x+L)^2 . $$

Estraendo la radice, con lo stesso argomento sul segno:

$$ 2x = x + L \quad\Longrightarrow\quad x = L . $$

La soluzione è positiva e quindi accettabile. La radice negativa, $2x = -(x+L)$, darebbe $x = -L/3$ e va scartata.

> [!important] Risultato dell'esercizio 2 L'unica posizione di equilibrio per la carica positiva $Q$ sulla retta delle due cariche si trova **a destra della carica negativa, a distanza $L$ da essa**, cioè a distanza $2L$ dalla carica $q_1$. Il valore $x = L$ esce "pulito" perché il rapporto tra le cariche è 4, un quadrato perfetto, e la radice si estrae esattamente.

> [!warning] "Equilibrio" e "stabilità" non sono la stessa cosa A lezione si dice che in questa posizione la configurazione "è stabile". Più precisamente è una posizione di **equilibrio**, ma di equilibrio **instabile** lungo l'asse. Detta $f(x) \propto \dfrac{8}{(x+L)^2} - \dfrac{2}{x^2}$ la forza netta, positiva se diretta lontano da $q_2$, si ha:
> 
> - se $Q$ si sposta leggermente oltre $x = L$, ad esempio a $x = 2L$, $f = \tfrac{8}{9L^2} - \tfrac{2}{4L^2} > 0$: la forza la spinge ancora più lontano;
> - se si avvicina, ad esempio a $x = L/2$, $f = \tfrac{8}{(9/4)L^2} - \tfrac{8}{L^2} < 0$: la forza la tira verso $q_2$.
> 
> In entrambi i casi la carica si allontana dalla posizione di equilibrio.

> [!tip] Approfondimento — Il teorema di Earnshaw #approfondimento Il risultato precedente non è un caso particolare. Il teorema di Earnshaw (1842) stabilisce che un insieme di cariche puntiformi soggette solo a forze elettrostatiche non può trovarsi in equilibrio stabile: per ogni posizione di equilibrio esiste almeno una direzione lungo cui una piccola perturbazione allontana la carica [@earnshaw1842]. È uno dei motivi per cui le trappole per particelle cariche usano campi variabili nel tempo o campi magnetici.

### Esercizio 3 — Due sfere conduttrici (incompleto)

> [!warning] Trascrizione interrotta L'ultimo esercizio della lezione, che il docente presenta come "concettuale e abbastanza semplice", riguarda due sfere conduttrici A e B separate da una certa distanza, con una condizione iniziale. La trascrizione della Parte 1 si interrompe proprio all'inizio del testo, prima dei dati e della soluzione, e negli appunti non ce n'è traccia. L'esercizio verrà integrato qui se arriva la parte successiva della registrazione o il testo del problema.