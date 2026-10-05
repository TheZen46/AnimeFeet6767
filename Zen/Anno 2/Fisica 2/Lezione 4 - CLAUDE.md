---

## corso: Fisica 2 lezione: 4 data: 2026-10-02 argomenti: [dipolo elettrico, molecole polari, momento torcente su un dipolo, energia potenziale di un dipolo, forno a microonde, flusso del campo elettrico, esercizi su distribuzioni continue, moto di una carica in campo uniforme] bibliography: fisica2.bib tags: [fisica2]

---
# Lezione 4 — Dipolo in un campo elettrico e flusso del campo elettrico

La lezione riprende il dipolo elettrico da un altro punto di vista. Finora il dipolo era una **sorgente** di campo; qui diventa un oggetto **immerso** in un campo esterno. Si studia come reagisce a un campo uniforme: compare un momento torcente che tende ad allinearlo al campo, e gli si associa un'energia potenziale che dipende dal suo orientamento. Come applicazione si discute il funzionamento del forno a microonde. Nella seconda parte si introduce il **flusso del campo elettrico**, lo strumento matematico che serve per il teorema di Gauss, previsto per la lezione successiva.

## Riepilogo della lezione precedente

In apertura il docente ricorda che nella [[Zen/Anno 2/Fisica 2/Lezione 3 - CLAUDE|Lezione 3 - CLAUDE]] è stato calcolato il campo elettrico generato da distribuzioni continue di carica: un anello e un disco carichi, sul loro asse. Annuncia poi lo schema della lezione: prima la teoria, poi gli esercizi sui campi elettrici.

## Il dipolo come sistema rigido

Si richiama la definizione: un dipolo è formato da due cariche uguali in modulo e di segno opposto, $+q$ e $-q$, a distanza $d$ l'una dall'altra. A questa definizione si aggiunge ora un elemento: le due cariche sono **legate**. Non possono muoversi liberamente l'una rispetto all'altra, perché un'interazione le tiene unite e il collegamento è rigido. Per cariche macroscopiche lo si può immaginare come una sbarretta rigida che unisce le due cariche. Il caso più importante, però, è microscopico: esistono molecole che si comportano come dipoli.

### La molecola d'acqua: un dipolo permanente

La molecola d'acqua, $\mathrm{H_2O}$, è formata da un atomo di ossigeno e da due atomi di idrogeno. Nel complesso è **neutra**: non ha carica in eccesso. L'ossigeno, però, è un atomo grande con molti elettroni e tende a sbilanciare la distribuzione delle cariche all'interno della molecola. Ne risulta una regione con un eccesso di carica negativa e una con un eccesso di carica positiva. Vista da fuori, la molecola si comporta come una carica positiva legata a una carica negativa uguale e opposta, cioè come un dipolo, pur essendo complessivamente neutra. Per questo la molecola d'acqua si dice **polare**. Moltissime altre molecole sono polari: pur essendo neutre, sono formate da atomi diversi e presentano uno sbilanciamento di carica. Di conseguenza reagiscono ai campi elettrici.

Anche nel caso delle molecole la distanza $d$ tra i "poli" si può considerare fissa. Le distanze tra gli atomi di idrogeno e di ossigeno possono variare un poco, perché gli atomi oscillano attorno alle posizioni di equilibrio, ma in media restano costanti. La schematizzazione con due cariche a distanza fissa ha quindi un interesse pratico: molte molecole, e non solo, si possono approssimare con un dipolo.

> [!warning] Discrepanza sul segno delle cariche nella molecola d'acqua 
> Nella trascrizione si sente che "la regione in cui ci sono gli atomi di idrogeno è mediamente più carica negativamente, mentre quella con l'atomo di ossigeno è carica positivamente". Anche negli appunti a mano gli idrogeni sono segnati "$-$" e l'ossigeno "$+$". È il contrario. L'ossigeno è molto più **elettronegativo** dell'idrogeno, cioè attira più fortemente gli elettroni di legame: attorno all'ossigeno si accumula una **parziale carica negativa** ($\delta^-$), mentre gli idrogeni restano con una **parziale carica positiva** ($\delta^+$). Il momento di dipolo della molecola, diretto per convenzione dalla carica negativa a quella positiva, punta quindi dall'ossigeno verso il punto medio tra i due idrogeni. Il ragionamento fisico della lezione non cambia: la molecola è neutra ma polare.

## Dipolo in un campo elettrico uniforme

### Le forze sulle due cariche

Si immerge il dipolo in un campo elettrico **uniforme**, diretto ad esempio da sinistra verso destra. Uniforme significa costante nel tempo e omogeneo nello spazio, cioè uguale in ogni punto. Il campo agisce quindi allo stesso modo su entrambe le cariche, e la forza su ciascuna è data dalla relazione $\vec F = q\vec E$.

- Sulla carica positiva agisce $\vec F_+ = q\vec E$, diretta come il campo.
- Sulla carica negativa agisce $\vec F_- = (-q)\vec E = -q\vec E$, uguale in modulo e opposta in verso. Il verso opposto è già contenuto nel segno meno della carica.

Le due forze sono uguali e opposte, quindi la **forza risultante è nulla**: in un campo uniforme il dipolo non trasla. Le due forze sono però applicate in punti diversi, alle due estremità della sbarretta rigida. Se il dipolo non è allineato con il campo, le loro rette d'azione non coincidono e le due forze formano una **coppia**: il dipolo inizia a **ruotare**. Il dipolo "sente" il campo e tende a portarsi dalla configurazione inclinata a quella di minima energia, allineata con il campo. Una forza che fa ruotare un corpo rigido è descritta, come visto in Fisica 1, dal **momento torcente**.

### Calcolo del momento torcente

Il momento torcente di una forza $\vec F$ applicata in un punto individuato dal vettore $\vec r$ è

$$ \vec\tau = \vec r \times \vec F . $$

Per scriverlo bisogna scegliere un **polo** $\Omega$, il punto rispetto al quale si misurano i vettori posizione e quindi i momenti. La scelta è arbitraria, ma per un'asta su cui agiscono due forze che la fanno ruotare la scelta migliore, per simmetria, è il centro dell'asta. Altre scelte darebbero calcoli più complicati. Con il polo nel centro del dipolo, il vettore $\vec r$ va dal centro a ciascuna carica e ha modulo $r = d/2$. Si indica con $\theta$ l'angolo tra l'asse del dipolo e il campo elettrico.

> [!tip] Richiamo — Il prodotto vettoriale 
> Il prodotto vettoriale $\vec A\times\vec B$ è un vettore. Il suo **modulo** è $$ |\vec A\times\vec B| = |\vec A|,|\vec B|\sin\theta , $$ con $\theta$ angolo compreso tra i due vettori. La sua **direzione** è perpendicolare al piano dei due vettori, e il **verso** è dato dalla regola della mano destra. In particolare il prodotto vettoriale di due vettori paralleli è nullo, perché $\sin0 = 0$, mentre per due vettori perpendicolari il modulo è semplicemente il prodotto dei moduli.

**Carica positiva.** Si scompone la forza $\vec F_+$ in una componente parallela al vettore posizione $\vec r$ e una perpendicolare:

$$ \vec F_+ = \vec F_\parallel + \vec F_\perp . $$

La componente parallela non contribuisce al momento: $\vec r\times\vec F_\parallel = 0$, perché l'angolo tra i due vettori è nullo. Fisicamente, tira l'asta lungo la sua direzione senza farla ruotare. Contribuisce solo la componente perpendicolare. Poiché $\vec r$ ed $\vec F_\perp$ sono perpendicolari, il modulo del loro prodotto vettoriale è il prodotto dei moduli, $|\vec r\times\vec F_\perp| = r,F_\perp$. Dalla geometria della figura, la componente perpendicolare vale $F_\perp = |\vec F|\sin\theta$. Quindi

$$ |\vec\tau_+| = r,|\vec F_+|\sin\theta = q,E,\frac d2,\sin\theta . $$

**Carica negativa.** La situazione è identica. La forza $\vec F_-$ ha verso opposto, ma anche il vettore $\vec r$ che va dal polo alla carica negativa ha verso opposto. Gli angoli sono gli stessi, e scomponendo di nuovo la forza in componente parallela e perpendicolare a $\vec r$ si ottiene lo stesso modulo:

$$ |\vec\tau_-| = q,E,\frac d2,\sin\theta . $$

**Verso dei due momenti.** Entrambi i momenti, essendo prodotti vettoriali di vettori nel piano della lavagna, sono perpendicolari alla lavagna: entranti o uscenti. Per sommarli si sceglie un asse perpendicolare alla lavagna e si attribuisce un segno a ciascun momento secondo il suo verso rispetto all'asse. La scelta del verso dell'asse è arbitraria. Ad esempio, se lo si prende uscente, un momento che fa ruotare il dipolo in senso orario, cioè verso l'allineamento con il campo, è entrante e quindi negativo. Indipendentemente dalla convenzione, c'è un fatto da notare: **$\vec\tau_+$ e $\vec\tau_-$ fanno ruotare il dipolo nello stesso verso**, pur essendo generati da forze opposte. Hanno quindi lo stesso segno e si sommano:

$$ |\vec\tau| = |\vec\tau_+| + |\vec\tau_-| = 2,q,E,\frac d2,\sin\theta = q,d,E,\sin\theta . $$

### Forma vettoriale: $\vec\tau = \vec p\times\vec E$

Nella [[Zen/Anno 2/Fisica 2/Lezione 2 - CLAUDE|Lezione 2 - CLAUDE]] è stato introdotto il **momento di dipolo** $p = qd$. Il dipolo è caratterizzato da due grandezze, la carica e la distanza tra le cariche. Poiché le due cariche sono uguali in modulo, lo si può descrivere in modo efficace senza pensare alle singole particelle, attraverso un unico vettore: il **vettore momento di dipolo** $\vec p$, di modulo $qd$ e diretto lungo l'asse del dipolo dalla carica negativa a quella positiva. Con questa grandezza il risultato si condensa in una forma compatta.

> [!important] Momento torcente su un dipolo in un campo uniforme $$ |\vec\tau| = p,E,\sin\theta, \qquad \vec\tau = \vec p\times\vec E $$ dove $\theta$ è l'angolo tra $\vec p$ ed $\vec E$. Il momento tende a ruotare $\vec p$ verso la direzione di $\vec E$.

I calcoli sono esattamente gli stessi di prima: si è solo riassunta l'informazione microscopica sulle due cariche nel vettore di dipolo. Il momento torcente dipende dalla carica e dalla distanza, attraverso $p$, dal modulo del campo e dall'orientamento del dipolo rispetto al campo.

### Configurazioni notevoli

**Momento nullo.** Il modulo del momento è minimo, cioè nullo, quando $\sin\theta = 0$, cioè per $\theta = 0$: il dipolo è **parallelo al campo**. Le forze ci sono ancora, ma sono uguali e contrarie e agiscono lungo la stessa retta, l'asse del dipolo. Si cancellano a vicenda e soprattutto non fanno ruotare il dipolo. È la configurazione verso cui il dipolo tende.

**Momento massimo.** Il modulo è massimo quando $\sin\theta = 1$, cioè per $\theta = \pi/2$: l'asse del dipolo è **perpendicolare al campo**. Le due forze hanno allora il massimo braccio, e il momento vale $|\vec\tau|_{\max} = pE$.

Tra questi due limiti il dipolo ruota con un momento che dipende dall'angolo come $\sin\theta$.

> [!tip] Approfondimento — Anche l'antiparallelo ha momento nullo #approfondimento 
> $\sin\theta$ si annulla anche per $\theta = \pi$, quando il dipolo è allineato al campo ma con verso **opposto**. Anche lì il momento è nullo, ma l'equilibrio è **instabile**: basta una piccola rotazione perché compaia un momento che allontana ulteriormente il dipolo da quella posizione, fino a portarlo verso $\theta = 0$. L'analisi energetica più avanti rende questa differenza evidente.

> [!warning] Discrepanze negli appunti (.md e a mano) sul momento torcente
> 
> - Nel file "Dipolo in campo elettrico.md" si legge "$r$ = distanza tra i poli, $d$ = distanza di un polo dal centro". Le definizioni sono invertite rispetto alla lezione: $d$ è la distanza tra le due cariche, $r = d/2$ la distanza di ciascuna carica dal polo. Le formule successive, ad esempio $qEr\sin\theta = \frac{qEd}{2}\sin\theta$, usano infatti la convenzione corretta.
> - Negli appunti a mano compare "$\tau_+ = q,\vec r\times\vec F_+$". La carica è già contenuta nella forza: $\vec\tau_+ = \vec r\times\vec F_+$, con $\vec F_+ = q\vec E$.

## Un'applicazione: il forno a microonde

Il docente sottolinea che il comportamento dei dipoli in un campo elettrico non è solo materia da esercizi. La polarità delle molecole d'acqua è il motivo per cui funziona il **forno a microonde**. Il forno genera un campo elettrico in una direzione e poi lo inverte, periodicamente: è un campo che oscilla avanti e indietro. Una molecola d'acqua immersa in questo campo sente un momento torcente che tende ad allinearla. Mentre ruota, però, il campo si inverte, e la molecola tende a ruotare dall'altra parte. Poiché il campo cambia continuamente verso a frequenze opportune, i dipoli non riescono mai a stabilizzarsi e la molecola resta in una condizione di continua oscillazione.

Nel vuoto queste oscillazioni non produrrebbero alcun effetto. Le molecole, però, sono immerse in un mezzo e interagiscono con quelle vicine. Si genera una sorta di attrito, c'è **dissipazione di energia** e il materiale si riscalda. Per questo il forno a microonde scalda i cibi, che sono fondamentalmente a base d'acqua, mentre un alimento secco in genere si scalda poco. Alla base di tutto c'è il fatto che la molecola d'acqua ha un **dipolo intrinseco**, che si può manipolare con i campi elettrici.

> [!tip] Approfondimento — Non è una "frequenza di risonanza" dell'acqua #approfondimento 
> I forni a microonde domestici lavorano a circa $2{,}45\ \mathrm{GHz}$. Un'idea molto diffusa è che questa sia una frequenza di risonanza della molecola d'acqua, ma non è così. Le risonanze di assorbimento dell'acqua si trovano a frequenze molto più alte, oltre $1\ \mathrm{THz}$, verso l'infrarosso. Il valore di $2{,}45\ \mathrm{GHz}$ deriva dall'assegnazione di quella banda di frequenze, da parte delle autorità di regolamentazione, all'uso nei forni. Il meccanismo è quello descritto a lezione, detto **riscaldamento dielettrico**: il campo fa ruotare le molecole polari, e le collisioni con le molecole vicine trasformano questo moto ordinato in agitazione termica, cioè calore [@baird2014].

## Lavoro ed energia potenziale del dipolo

### Impostazione

L'altra grandezza che interessa quando si parla di un dipolo in un campo elettrico è il **lavoro** necessario per ruotarlo, cioè per spostarlo da un orientamento a un altro. L'energia è per definizione legata a un lavoro. Per sapere quanta energia è immagazzinata in un dipolo immerso in un campo, si calcola il lavoro compiuto dalle forze del campo quando il dipolo ruota da una configurazione iniziale a una finale. Si ricorda che il lavoro è l'integrale del prodotto scalare tra la forza e lo spostamento:

$$ L = \int_{\text{iniziale}}^{\text{finale}} \vec F\cdot d\vec s . $$

Il prodotto scalare va calcolato punto per punto e poi integrato dalla configurazione iniziale a quella finale, che quindi vanno specificate.

### Forza e spostamento

Si consideri la carica positiva. Mentre il dipolo ruota attorno al suo centro, la carica si muove lungo una circonferenza, e il suo spostamento istantaneo $d\vec s$ è **tangente** alla circonferenza, quindi perpendicolare all'asse del dipolo. La forza $\vec F_+ = q\vec E$ è invece diretta come il campo. Se il dipolo ruota nel verso in cui lo spinge il campo, cioè verso l'allineamento, l'angolo tra $\vec F$ e $d\vec s$ vale $90^\circ - \theta$. Lo si vede dalla figura: l'asse del dipolo forma l'angolo $\theta$ con il campo, e lo spostamento è perpendicolare all'asse. Poiché $\cos(90^\circ-\theta) = \sin\theta$,

$$ \vec F\cdot d\vec s = F,ds,\cos(90^\circ-\theta) = F,ds,\sin\theta = q,E,\sin\theta,ds . $$

### Dallo spostamento all'angolo

Per integrare sull'angolo bisogna esprimere $ds$ in funzione di $d\theta$. È lo stesso "giochino" con gli angoli usato per l'arco nella lezione 3: un arco di circonferenza di raggio $\rho$ e angolo $d\theta$ ha lunghezza $\rho,d\theta$. Il docente lo ricava di nuovo con il triangolo rettangolo e l'approssimazione $\sin\theta\simeq\theta$ per angoli piccoli. Ogni carica si trova a distanza $\rho = d/2$ dal centro. Quando il dipolo ruota verso il campo l'angolo $\theta$ **diminuisce**, quindi $d\theta<0$ e la lunghezza dello spostamento è $ds = -\tfrac d2,d\theta$. Per una carica:

$$ \vec F_+\cdot d\vec s = -,q,E,\frac d2,\sin\theta,d\theta . $$

La carica negativa dà un contributo identico, perché si muove in verso opposto ma è soggetta a una forza opposta. Sommando i due contributi si riconosce il modulo del momento torcente, $\tau = qdE\sin\theta = pE\sin\theta$:

$$ dL = -,q,d,E,\sin\theta,d\theta = -,\tau,d\theta \qquad\Longrightarrow\qquad L = -\int_{\theta_i}^{\theta_f}\tau,d\theta . $$

Il lavoro diventa così un integrale sugli angoli. La formula vale in generale: se un esercizio chiede il lavoro per portare un dipolo da un angolo $\theta_i$ a un angolo $\theta_f$, basta calcolare questo integrale.

> [!tip] Collegamento con Fisica 1 Il risultato è un caso particolare di una relazione generale della dinamica del corpo rigido: il lavoro compiuto da un momento torcente durante una rotazione è $L = \int\tau,d\theta$, con $\tau$ preso con il segno. Qui il segno meno compare perché il momento del campo tende a far diminuire $\theta$.

> [!warning] Una precisazione sui passaggi alla lavagna e negli appunti Alla lavagna, e quindi negli appunti a mano e nel file .md, il passaggio è scritto in forma compatta come "$\vec F\cdot d\vec s = -\frac{\tau}{d},ds = -\tau,d\theta$, con $\frac{ds}{d} = d\theta$". Usa $d$ come raggio della circonferenza descritta dalla carica, e mescola il momento proiettato, negativo con la convenzione dell'asse uscente, con il suo modulo. Più precisamente, ogni carica ruota su una circonferenza di raggio $d/2$, e il fattore $d$ nel momento totale si ritrova sommando i contributi delle due cariche, come mostrato sopra. Il risultato finale, $L = -\int\tau,d\theta$ con $\tau = pE\sin\theta$, è lo stesso.

### Integrazione e convenzione sull'angolo iniziale

Se gli angoli non sono fissati dal problema, per convenzione si prende come angolo iniziale $\theta_i = \pi/2$, con il dipolo perpendicolare al campo, e si lascia generico l'angolo finale $\theta$. In altre parole, l'energia si misura rispetto alla configurazione con $\theta = \pi/2$. Sostituendo $\tau = pE\sin\theta$, con $p$ ed $E$ costanti perché il dipolo è rigido e il campo uniforme:

$$ L = -\int_{\pi/2}^{\theta} pE,\sin\theta',d\theta' = -pE\int_{\pi/2}^{\theta}\sin\theta',d\theta' = pE\Big[\cos\theta'\Big]_{\pi/2}^{\theta} = pE\cos\theta . $$

La primitiva di $-\sin\theta'$ è $\cos\theta'$. All'estremo inferiore si dovrebbe sottrarre $\cos(\pi/2)$, ma vale zero, quindi resta solo $pE\cos\theta$, che in forma vettoriale è il prodotto scalare $\vec p\cdot\vec E$.

Uno studente ha chiesto perché l'integrale parta proprio da $\pi/2$. Il docente ha risposto che è una **convenzione**. Se il problema fornisce un angolo iniziale e uno finale, si calcola l'integrale tra quei due angoli e si ottengono il lavoro compiuto e l'energia immagazzinata. Fissando per convenzione $\theta_i = \pi/2$, l'energia del dipolo dipende da un solo angolo invece che da due, e tutta l'informazione si condensa in una sola variabile, il che è più comodo.

### Energia potenziale

La variazione di energia potenziale è, per definizione, l'opposto del lavoro compiuto dalle forze del campo: $\Delta U = -L$. Con la convenzione $U(\pi/2) = 0$ si ottiene l'energia potenziale del dipolo in funzione del suo orientamento.

> [!important] Energia potenziale di un dipolo in un campo uniforme $$ U(\theta) = -,p,E\cos\theta = -,\vec p\cdot\vec E $$ con lo zero fissato nella configurazione perpendicolare, $\theta = \pi/2$. Tra due orientamenti generici il lavoro del campo è $L = pE\left(\cos\theta_f - \cos\theta_i\right)$ e $\Delta U = -L$.

Questi risultati descrivono il comportamento del dipolo in un campo uniforme: tende a ruotare, e in una configurazione inclinata immagazzina una certa energia. L'energia è **minima**, $U = -pE$, per $\theta = 0$, con il dipolo allineato al campo: è la configurazione di equilibrio stabile verso cui il momento torcente spinge il dipolo. È **massima**, $U = +pE$, per $\theta = \pi$, con il dipolo antiparallelo, dove l'equilibrio è instabile. Il grafico mostra entrambe le grandezze in funzione di $\theta$, normalizzate a $pE$: il momento si annulla proprio dove l'energia ha il minimo e il massimo.

```chart
type: line
labels: [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
series:
  - title: Modulo del momento torcente, τ/(pE) = sin θ
    data: [0, 0.259, 0.5, 0.707, 0.866, 0.966, 1, 0.966, 0.866, 0.707, 0.5, 0.259, 0]
  - title: Energia potenziale, U/(pE) = −cos θ
    data: [-1, -0.966, -0.866, -0.707, -0.5, -0.259, 0, 0.259, 0.5, 0.707, 0.866, 0.966, 1]
tension: 0.3
width: 80%
labelColors: false
fill: false
beginAtZero: false
```

> [!tip] Approfondimento — Lavoro del campo e lavoro dell'operatore #approfondimento All'inizio del ragionamento si parla del "lavoro necessario per spostare il dipolo", nel calcolo del lavoro compiuto dalle forze del campo. Le due grandezze sono opposte. Se un operatore ruota il dipolo lentamente, senza dargli energia cinetica, il lavoro che compie è $L_{\text{est}} = -L = \Delta U$. Ad esempio, per portare un dipolo dalla posizione allineata ($\theta = 0$) a quella antiparallela ($\theta = \pi$) l'operatore deve compiere il lavoro $\Delta U = pE - (-pE) = 2pE$.

> [!tip] Approfondimento — Dipolo in un campo non uniforme #approfondimento In un campo **non uniforme** le due cariche sentono campi diversi, e la forza risultante non è più nulla. Un dipolo allineato con il campo viene attratto verso la regione in cui il campo è più intenso. È la spiegazione completa della carica indotta vista nella [[Fisica 2 - Lezione 01 - Carica elettrica e legge di Coulomb|lezione 1]]. La bacchetta conduttrice neutra, polarizzata dalla bacchetta carica, si comporta come un dipolo allineato con il campo di quest'ultima. Quel campo è più intenso vicino alla bacchetta carica, quindi la risultante è attrattiva, qualunque sia il segno della carica inducente.

## Il flusso del campo elettrico

Il concetto di flusso non è stato introdotto in Fisica 1 e verrà trattato in modo completo nel corso di Metodi Matematici, ma solo alla fine dell'anno. Il docente lo introduce quindi qui in forma semplice, perché serve per il **teorema di Gauss**, previsto per la lezione successiva.

### Superficie piana

Si consideri una superficie **piana** di area $A$, ad esempio un rettangolo o un quadrato, attraversata da un campo vettoriale, che per noi sarà il campo elettrico $\vec E$. A una superficie piana si può sempre associare un **versore normale** $\hat n$, cioè un vettore di modulo unitario perpendicolare alla superficie. Il ragionamento è questo: la superficie è un oggetto bidimensionale, ma la sua orientazione nello spazio è determinata completamente dalla direzione perpendicolare, cioè da un solo vettore. Si definisce allora il **vettore area** $\vec A$, che ha come modulo l'area $A$ e come direzione quella di $\hat n$:

$$ \vec A = A,\hat n . $$

Con questo vettore il prodotto scalare con il campo è ben definito e dà il flusso.

> [!important] Flusso del campo elettrico attraverso una superficie piana $$ \Phi_E = \vec E\cdot\vec A = E,A\cos\theta $$ dove $\theta$ è l'angolo tra il campo $\vec E$ e il versore normale $\hat n$ alla superficie. Il flusso è uno **scalare** e si misura in $\mathrm{N,m^2/C}$.

Il passaggio logico è: si prende una superficie piana, le si associa il vettore normale, unico per una superficie piana, si costruisce il vettore area di modulo $A$ e direzione $\hat n$, e si definisce il flusso come prodotto scalare tra $\vec E$ e $\vec A$. Il flusso è massimo quando il campo è perpendicolare alla superficie, cioè parallelo a $\hat n$, ed è nullo quando il campo è parallelo alla superficie, cioè la "sfiora" senza attraversarla. Nella [[Fisica 2 - Lezione 02 - Campo elettrico e dipolo|lezione 2]] si era detto che la densità delle linee di campo rappresenta l'intensità del campo. Con quell'immagine, il flusso misura quante linee di campo attraversano la superficie.

### Superficie qualsiasi

Il procedimento funziona se esiste un unico vettore normale, cioè se la superficie è piana. Per una superficie qualsiasi bisogna generalizzarlo, e si fa come fanno sempre i fisici, e prima di loro i matematici che hanno definito il flusso. Qualsiasi superficie, se si considera una regione abbastanza piccola, è ben approssimata da un piano. Si suddivide quindi la superficie in elementi di area infinitesima $dA$, ciascuno praticamente piano. A ogni elemento si associa il suo versore normale $\hat n$, che cambia da elemento a elemento, e il vettore area infinitesimo

$$ d\vec A = dA,\hat n , $$

il cui modulo è l'area infinitesima e la cui direzione è perpendicolare all'elemento. Il flusso infinitesimo attraverso l'elemento si definisce esattamente come nel caso piano, con il campo $\vec E$ calcolato nel punto in cui si trova l'elemento:

$$ d\Phi_E = \vec E\cdot d\vec A . $$

Il campo, infatti, può cambiare da un punto all'altro della superficie, in direzione e anche in modulo. Nel caso discreto si sommerebbero i contributi di tutti i "quadratini"; nel caso continuo si passa all'integrale di superficie.

> [!important] Flusso attraverso una superficie qualsiasi $$ \Phi_E = \int_S \vec E\cdot d\vec A, \qquad\text{e per una superficie chiusa}\qquad \Phi_E = \oint_S \vec E\cdot d\vec A . $$

Il docente fa notare che è fondamentalmente il solito discorso, lo stesso seguito per i campi dell'anello e del disco: le grandezze si definiscono bene per elementi infinitesimi, lì cariche $dq$ e qui aree $dA$, e poi si integrano tutti i contributi per ottenere il risultato totale.

> [!warning] Precisazione: il flusso si definisce anche per superfici aperte A lezione si dice che "per poter definire il flusso devo avere una superficie chiusa". In realtà il flusso è definito per **qualsiasi** superficie orientata, aperta o chiusa: lo mostra già il primo esempio della lezione, il rettangolo piano, che è una superficie aperta. Le superfici chiuse, come una sfera, un cubo o un cilindro con le basi, sono quelle che interessano per il **teorema di Gauss**, e per esse si usa il simbolo $\oint$. Per lo stesso motivo, quando si calcola il flusso attraverso una singola faccia di una superficie, ad esempio una base di un cilindro, la notazione corretta è $\int$ e non $\oint$, che negli appunti a mano compare anche per le singole basi.

> [!warning] Sezione ricostruita — inizio La trascrizione (Parte 1) si interrompe mentre il docente inizia a discutere il segno del flusso. Il seguito, cioè la convenzione sul segno, l'esempio del cilindro e i tre esercizi, è ricostruito dai tuoi **appunti a mano**, l'unica fonte disponibile per questa parte. Le spiegazioni sono mie e i calcoli li ho verificati; dove gli appunti contengono errori, lo segnalo.

### Il segno del flusso

Il segno del flusso dipende dalla relazione tra il campo elettrico e il vettore area, cioè dal segno di $\cos\theta$:

- se l'angolo tra $\vec E$ e $\hat n$ è minore di $90^\circ$, il campo attraversa la superficie nel verso di $\hat n$ e il flusso è **positivo**;
- se l'angolo è maggiore di $90^\circ$, il campo attraversa la superficie nel verso opposto a $\hat n$ e il flusso è **negativo**;
- se il campo è parallelo alla superficie ($\theta = 90^\circ$), il flusso è **nullo**.

Il segno dipende quindi da come si sceglie $\hat n$: per una superficie ci sono sempre due versi possibili della normale. Come annotato negli appunti, per una superficie chiusa la convenzione è prendere la normale **perpendicolare e uscente** dalla superficie, in ogni suo punto. Con questa scelta le linee di campo che **escono** dalla superficie danno un contributo positivo al flusso, quelle che **entrano** un contributo negativo.

### Esempio: flusso attraverso un cilindro in un campo uniforme

> [!example] Cilindro con l'asse parallelo a un campo uniforme Un cilindro chiuso è immerso in un campo elettrico uniforme $\vec E$ parallelo al suo asse. Calcolare il flusso totale attraverso la sua superficie.
> 
> La superficie chiusa si divide in tre parti: la base 1, da cui il campo entra; la base 2, da cui il campo esce; la superficie laterale 3. Il flusso totale è la somma dei tre contributi, $\Phi_{\text{tot}} = \Phi_1 + \Phi_2 + \Phi_3$.
> 
> **Base 1.** La normale uscente punta in verso opposto al campo: $\vec E$ e $\hat n$ sono **antiparalleli** e $\cos\theta = -1$. Il campo è uniforme ed esce dall'integrale: $$ \Phi_1 = \int_1 \vec E\cdot d\vec A = -\int_1 E,dA = -E\int_1 dA = -E,A_1 . $$ **Base 2.** La normale uscente è parallela al campo e $\cos\theta = +1$: $$ \Phi_2 = \int_2 \vec E\cdot d\vec A = E\int_2 dA = E,A_2 . $$ **Superficie laterale.** In ogni punto la normale è perpendicolare al campo, $\cos(\pi/2) = 0$, quindi $\Phi_3 = 0$.
> 
> **Totale.** Le due basi hanno la stessa area, $A_1 = A_2$: $$ \Phi_{\text{tot}} = -E A_1 + E A_2 + 0 = 0 . $$

Il risultato ha una lettura immediata in termini di linee di campo: ogni linea che entra nel cilindro dalla base 1 ne esce dalla base 2, e il bilancio tra linee entranti e uscenti è nullo.

> [!tip] Anticipazione — Verso il teorema di Gauss Il risultato dell'esempio non dipende dal cilindro. Il teorema di Gauss, oggetto della prossima lezione, lega il flusso attraverso una superficie chiusa alla carica contenuta al suo interno. Un flusso totale nullo, come qui, è coerente con l'assenza di cariche dentro il cilindro.

## Esercizi

### Esercizio 1 — Due anelli concentrici

> [!example] Testo (dagli appunti) Due anelli concentrici e complanari, carichi uniformemente: il primo ha raggio $R$ e carica $Q>0$, il secondo raggio $R' = 3R$ e carica $Q'$. Il punto $P$ si trova sull'asse comune, a distanza $D = 2R$ dal centro. Quanto deve valere $Q'$ perché il campo elettrico in $P$ sia nullo?
> 
> **Ragionamento.** Entrambi gli anelli generano in $P$ un campo diretto lungo l'asse, dato dalla formula ricavata nella lezione 3: $$ E = \frac{k,Q,D}{\left(R^2+D^2\right)^{3/2}}, \qquad E' = \frac{k,Q',D}{\left(R'^2+D^2\right)^{3/2}} . $$ Il primo campo è uscente dall'anello, verso l'alto nella figura. Perché i due campi si annullino, quello del secondo anello deve avere lo stesso modulo e verso opposto, quindi $Q'$ deve avere **segno opposto** a $Q$. Uguagliando i moduli, $E = E'$, $k$ e $D$ si semplificano: $$ \frac{Q}{\left(R^2+D^2\right)^{3/2}} = \frac{|Q'|}{\left(R'^2+D^2\right)^{3/2}} \quad\Longrightarrow\quad |Q'| = Q\left(\frac{R'^2+D^2}{R^2+D^2}\right)^{3/2} = Q\left(\frac{9R^2+4R^2}{R^2+4R^2}\right)^{3/2} = \left(\frac{13}{5}\right)^{3/2} Q . $$ **Risultato.** $$ Q' \simeq -4{,}19,Q . $$ Il secondo anello è più lontano da $P$, quindi per produrre lo stesso campo deve portare una carica più grande in modulo.

> [!warning] Segno di $Q'$ Negli appunti il risultato è scritto $Q' = 4{,}19,Q$, cioè il solo modulo. Dal disegno, dove il campo $\vec E'$ è opposto a $\vec E$, e dalla condizione di campo nullo, la carica del secondo anello deve avere segno opposto a quella del primo: $Q' \simeq -4{,}19,Q$.

### Esercizio 2 — Disco con un foro centrale

> [!example] Testo (dagli appunti) Un disco di raggio $R$, carico uniformemente con densità $\sigma>0$, ha un foro circolare concentrico di raggio $R' = R/2$. Determinare il campo sull'asse nel punto $P$ a distanza $z = 2R$ dal centro, e confrontarlo con quello del disco senza foro.
> 
> **Il "trucchetto".** La formula del disco della lezione 3 vale per un disco pieno. Per il principio di sovrapposizione, un disco forato equivale a un disco pieno di densità $+\sigma$ sovrapposto a un disco più piccolo, grande quanto il foro, di densità $-\sigma$: nella regione del foro le due densità si annullano. Il campo totale è la somma dei due campi.
> 
> **Disco pieno ($+\sigma$, raggio $R$).** $$ E_+ = 2\pi k\sigma\left(1 - \frac{z}{\sqrt{z^2+R^2}}\right) = 2\pi k\sigma\left(1 - \frac{2}{\sqrt5}\right) \simeq 0{,}1056\cdot 2\pi k\sigma . $$ **Disco del foro ($-\sigma$, raggio $R/2$).** Con $z = 2R$ e $R' = R/2$, $\dfrac{z}{\sqrt{z^2+R'^2}} = \dfrac{2R}{\sqrt{4R^2+R^2/4}} = \dfrac{4}{\sqrt{17}}$: $$ E_- = -2\pi k\sigma\left(1 - \frac{4}{\sqrt{17}}\right) \simeq -0{,}0299\cdot 2\pi k\sigma . $$ **Totale.** $$ E_{\text{tot}} = E_+ + E_- = 2\pi k\sigma\left(\frac{4}{\sqrt{17}} - \frac{2}{\sqrt5}\right) \simeq 0{,}0757\cdot 2\pi k\sigma, \qquad \frac{E_{\text{tot}}}{E_+} \simeq 0{,}717 . $$ Togliere la parte centrale del disco riduce il campo in $P$ di circa il **28%**.
> 
> **Verifica.** Lo stesso risultato si ottiene integrando direttamente sulle corone circolari da $r = R'$ a $r = R$ invece che da $0$ a $R$: $$ E = 2\pi k\sigma z\left(\frac{1}{\sqrt{z^2+R'^2}} - \frac{1}{\sqrt{z^2+R^2}}\right) = 2\pi k\sigma\left(\frac{4}{\sqrt{17}} - \frac{2}{\sqrt5}\right). $$

> [!warning] Discrepanza sul rapporto finale Negli appunti si legge $E_{\text{tot}}/E_+ \simeq 0{,}283$. Quel numero è il rapporto $|E_-|/E_+ = (1-4/\sqrt{17})/(1-2/\sqrt5) \simeq 0{,}283$, cioè la **frazione di campo persa** a causa del foro. Il rapporto tra il campo del disco forato e quello del disco pieno è $E_{\text{tot}}/E_+ = 1 - 0{,}283 \simeq 0{,}717$.

### Esercizio 3 — Moto di una carica in un campo uniforme

> [!example] Testo (dagli appunti) Una particella carica viene lanciata con velocità iniziale $v_0 = 2\cdot10^{6}\ \mathrm{m/s}$, inclinata di $\theta = 40^\circ$ rispetto all'asse $x$, in un campo elettrico uniforme $\vec E = 5\ \mathrm{N/C}\ \hat\jmath$. Uno schermo è posto perpendicolarmente all'asse $x$ a distanza $x = 3\ \mathrm m$ dal punto di lancio. La particella raggiunge lo schermo? Con quale velocità?
> 
> **Forza e accelerazione.** La forza è $\vec F = q\vec E$. Negli appunti è disegnata verso il basso, cioè in verso opposto al campo, quindi la carica è **negativa**. Il modulo si ottiene dalla seconda legge della dinamica: $$ |\vec F| = ma, \quad |\vec F| = |q|E \quad\Longrightarrow\quad a = \frac{|q|E}{m}\quad\text{(costante, diretta lungo } -\hat\jmath\text{)} . $$ Accelerazione costante e diretta lungo $y$: è lo stesso problema del **moto di un proiettile** in Fisica 1, con $a$ al posto di $g$. Le equazioni del moto sono $$ \begin{cases} x = v_{0x},t \ y = v_{0y},t - \tfrac12 a t^2 \end{cases} \qquad \begin{cases} v_x = v_{0x} \ v_y = v_{0y} - a t \end{cases} $$ con $v_{0x} = v_0\cos\theta \simeq 1{,}53\cdot10^6\ \mathrm{m/s}$ e $v_{0y} = v_0\sin\theta \simeq 1{,}29\cdot10^6\ \mathrm{m/s}$.
> 
> **Calcolo (con un elettrone).** Con $|q| = e = 1{,}602\cdot10^{-19}\ \mathrm C$ e $m = 9{,}11\cdot10^{-31}\ \mathrm{kg}$: $$ a = \frac{(1{,}602\cdot10^{-19})(5)}{9{,}11\cdot10^{-31}}\ \mathrm{m/s^2} \simeq 8{,}79\cdot10^{11}\ \mathrm{m/s^2} . $$ Il tempo per arrivare allo schermo si ricava dal moto uniforme lungo $x$: $$ t = \frac{x}{v_{0x}} = \frac{3\ \mathrm m}{1{,}53\cdot10^6\ \mathrm{m/s}} \simeq 1{,}96\cdot10^{-6}\ \mathrm s . $$ In quell'istante la quota è $$ y = v_{0y}t - \tfrac12 a t^2 \simeq 2{,}52\ \mathrm m - 1{,}69\ \mathrm m \simeq 0{,}83\ \mathrm m > 0 , $$ quindi l'elettrone **raggiunge lo schermo**, 0,83 m sopra la quota di lancio, prima di ricadere. Senza schermo tornerebbe alla quota iniziale dopo una gittata $2v_{0x}v_{0y}/a \simeq 4{,}5\ \mathrm m > 3\ \mathrm m$. La velocità all'impatto è $$ v_x = v_{0x} \simeq 1{,}53\cdot10^{6}\ \mathrm{m/s}, \qquad v_y = v_{0y} - at \simeq -4{,}4\cdot10^{5}\ \mathrm{m/s}, $$ $$ \vec v \simeq \left(1{,}53\cdot10^{6}\ \hat\imath - 4{,}4\cdot10^{5}\ \hat\jmath\right)\mathrm{m/s} . $$ La componente $y$ negativa indica che l'elettrone ha già superato il punto più alto della traiettoria, a circa 0,94 m, e sta scendendo.
> 
> **Peso trascurabile.** Il rapporto tra forza peso e forza elettrica è $mg/(eE) \sim 10^{-11}$: la gravità si può ignorare del tutto.

> [!warning] Dati mancanti negli appunti Gli appunti non dicono quale sia la particella e si fermano alle equazioni del moto, senza risultati numerici. Dal verso della forza, opposto al campo, la carica è negativa. Il calcolo assume un **elettrone**, che è la versione abituale di questo problema nei testi. Se a lezione la particella era diversa, vanno cambiati $|q|$ e $m$ nell'accelerazione, e di conseguenza i numeri. Il metodo resta identico.

> [!warning] Sezione ricostruita — fine