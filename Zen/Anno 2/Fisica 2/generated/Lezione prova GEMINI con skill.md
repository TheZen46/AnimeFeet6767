# Lezione 5 — Il teorema di Gauss

La lezione completa il discorso sul flusso con un esempio in cui il campo non è uniforme, poi introduce il risultato centrale dell'elettrostatica: il **teorema di Gauss**, che lega il flusso del campo elettrico attraverso una superficie chiusa alle cariche contenute al suo interno. Il teorema non viene dimostrato in generale per via degli strumenti matematici avanzati richiesti. Il docente mostra tuttavia che esso è rigorosamente valido per superfici sferiche attorno a una carica puntiforme, introducendo il concetto di **angolo solido**. Da tale risultato ricava la legge di Coulomb per inversione logica e applica il teorema a un esercizio prototipico su un guscio sferico concentrico. Infine, il teorema viene impiegato «all'incontrario» per determinare la distribuzione spaziale delle cariche elettriche nei conduttori all'equilibrio elettrostatico.

  

> [!tip] Legenda delle figure
> 
> In tutte le figure del corso le cariche positive sono indicate in **blu** e quelle negative in **rosso**. Il campo elettrico è tracciato in **verde petrolio**, le superfici gaussiane in **giallo tratteggiato**, i versori normali in **viola** e i vettori forza in **verde**. I file grafici vettoriali `.svg` richiamati nel testo vanno inseriti nella cartella `Allegati` del vault di Obsidian.
> 
>   

## Riepilogo: il flusso del campo elettrico

La trattazione prende avvio richiamando la definizione generale di flusso del campo elettrico introdotta nella [[Lezione 4 - CLAUDE|lezione 4]]. A ogni elemento infinitesimo di superficie si associa un vettore area $d\vec{A} = dA\,\hat{n}$, avente per modulo l'area dell'elemento e per direzione la normale alla superficie, orientata convenzionalmente verso l'esterno nel caso di superfici chiuse. Il flusso infinitesimo corrisponde al prodotto scalare $d\Phi_E = \vec{E} \cdot d\vec{A}$, e il flusso netto attraverso l'intera superficie chiusa si ottiene per integrazione su tutti gli elementi:

  

$$\Phi_E = \oint \vec{E} \cdot d\vec{A}$$

Il docente rimarca che questa formulazione matematica è universale ed esatta, ma in condizioni arbitrarie l'integrale non è risolvibile analiticamente a causa della complessità geometrica della superficie o del campo vettoriale. Tuttavia, in configurazioni dotate di elevata simmetria spaziale (sfere, cilindri, piani), il calcolo si riduce a semplici prodotti algebrici. Dopo aver analizzato il caso del cilindro immerso in un campo uniforme, si esamina ora una situazione più articolata in cui il campo elettrico è spazialmente disomogeneo.

  

## Esempio: flusso di un campo non uniforme attraverso un cubo

> [!example] Testo
> 
> Il campo elettrico assegnato è espresso nella forma normalizzata:
> 
>   
> 
> $$\vec{E} = E_0 \left(3x\,\hat{i} + 4\,\hat{j}\right)$$
> 
> con la coordinata $x$ misurata in metri. Calcolare il flusso totale attraverso la superficie di un cubo con facce parallele ai piani coordinati, i cui spigoli lungo l'asse $x$ sono compresi tra $x = 1\text{ m}$ e $x = 3\text{ m}$.
> 
>   

### La normalizzazione

Il campo elettrico viene riscalato rispetto a una costante $E_0$ avente le dimensioni fisiche del campo ($\text{N/C}$). In questo modo il vettore adimensionale $\vec{E}/E_0 = 3x\,\hat{i} + 4\,\hat{j}$ permette di eseguire i calcoli algebrici senza trascinare le unità di misura, ripristinandole al termine mediante moltiplicazione per $E_0$.

  

### Struttura del campo elettrico

L'andamento spaziale si scompone nelle tre coordinate cartesiane:

  

- **Componente $x$:** Vale $E_x = 3x E_0$; si annulla sull'origine e cresce linearmente allontanandosi lungo l'asse $x$.
    
      
    
- **Componente $y$:** Vale costantemente $E_y = 4 E_0$, priva di qualsiasi dipendenza spaziale dalle coordinate.
    
      
    
- **Componente $z$:** Identicamente nulla ($E_z = 0$).
    
      
    

Il campo giace dunque nel piano $xy$ ed è rappresentato considerando una terna destra con l'asse $z$ rivolto verso chi guarda.

  

### Geometria del cubo

L'intervallo dello spigolo lungo l'asse $x$ va da $1\text{ m}$ a $3\text{ m}$, determinando una lunghezza di lato pari a $L = 3 - 1 = 2\text{ m}$. Trattandosi di un cubo regolare con le facce disposte parallelamente ai piani coordinati, ogni singola faccia possiede un'area pari ad $A = L^2 = (2\text{ m})^2 = 4\text{ m}^2$.

  

![[F2-L05-cubo-normali.svg]]

  

### Calcolo del flusso faccia per faccia

Il flusso complessivo sulla superficie chiusa si calcola sommando i contributi integrali delle sei facce poliedriche. Su ogni faccia piana il versore normale uscente $\hat{n}$ è costante, permettendo di scrivere direttamente $\vec{A} = A\,\hat{n}$:

  

1. **Facce perpendicolari all'asse $z$ (anteriore e posteriore):**
    
    I versori normali uscenti sono rispettivamente $+\hat{k}$ e $-\hat{k}$. Poiché il campo elettrico non ha alcuna componente diretta lungo l'asse $z$, i prodotti scalari $\hat{i} \cdot \hat{k}$ e $\hat{j} \cdot \hat{k}$ si annullano per ortogonalità. Il flusso attraverso entrambe le facce lungo $z$ è identicamente nullo:
    
      
    
    $$\Phi_z = 0$$
    
2. **Facce perpendicolari all'asse $y$ (superiore e inferiore):**
    
    Sulla faccia superiore il versore uscente è $+\hat{j}$, mentre su quella inferiore è $-\hat{j}$. Eseguendo i prodotti scalari:
    
      
    
    $$\frac{\vec{E}}{E_0} \cdot A\,\hat{j} = \left(3x\,\hat{i} + 4\,\hat{j}\right) \cdot A\,\hat{j} = 4A \implies \Phi_{sup} = +4A E_0$$
    
    $$\frac{\vec{E}}{E_0} \cdot \left(-A\,\hat{j}\right) = \left(3x\,\hat{i} + 4\,\hat{j}\right) \cdot \left(-A\,\hat{j}\right) = -4A \implies \Phi_{inf} = -4A E_0$$
    
    Su ciascuna faccia isolata il flusso è non nullo, ma i due contributi risultano uguali in modulo e di segno opposto poiché la componente $E_y$ è uniforme. Sommando i due termini, il flusso netto attraverso le facce lungo $y$ si annulla:
    
      
    
    $$\Phi_y = \Phi_{sup} + \Phi_{inf} = 4A E_0 - 4A E_0 = 0$$
    
3. **Facce perpendicolari all'asse $x$ (sinistra e destra):**
    
    Sulla faccia di destra ($x_{dx} = 3\text{ m}$) il versore normale è $+\hat{i}$, mentre sulla faccia di sinistra ($x_{sx} = 1\text{ m}$) il versore è $-\hat{i}$. Il prodotto scalare seleziona la sola componente $E_x$, la quale varia lungo l'asse ma si mantiene costante su tutti i punti appartenenti alla medesima faccia ortogonale:
    
      
    
    $$\Phi_{x=3} = +3\,x_{dx}\,A\,E_0 = +3(3)(4)\,E_0 = +36\,E_0$$
    
    $$\Phi_{x=1} = -3\,x_{sx}\,A\,E_0 = -3(1)(4)\,E_0 = -12\,E_0$$
    
    In questo caso i due flussi non si compensano poiché il campo elettrico uscente sulla faccia destra è più intenso di quello entrante sulla faccia sinistra.
    
      
    

### Flusso totale

Sommando i contributi residui lungo l'asse $x$:

  

$$\Phi_{tot} = 3A\left(x_{dx} - x_{sx}\right)E_0 = 3(4\text{ m}^2)(3\text{ m} - 1\text{ m})E_0 = 24 E_0\text{ N}\cdot\text{m}^2/\text{C}$$

![[F2-L05-cubo-flussi.svg]]

  

Il docente evidenzia come la relazione $\Phi_{tot} = 3A(x_{dx} - x_{sx})E_0$ sia valida per qualunque coppia di coordinate $x_{sx}$ e $x_{dx}$, purché le facce restino parallele agli assi. Inoltre, esprimendo l'area della faccia come $A = (x_{dx} - x_{sx})^2$, il flusso totale diviene $3E_0 (x_{dx} - x_{sx})^3$, risultando direttamente proporzionale al volume del cubo.

  

> [!warning] Numerazione delle facce
> 
> Nella trascrizione della lezione il docente cambia la numerazione delle facce durante la spiegazione, indicando inizialmente con 1 e 2 le facce lungo $z$ e successivamente quelle lungo $y$. Negli appunti manoscritti la faccia a coordinata $x = 3$ è denominata $\Phi_5$. Nello schema visuale normalizzato le facce sono catalogate in base ai versori normali associati.
> 
>   

> [!tip] Approfondimento — Che cosa c'è dentro il cubo? #approfondimento
> 
> Applicando il teorema di Gauss, il cubo contiene una carica netta $q_{in} = \varepsilon_0 \Phi = 24\varepsilon_0 E_0\text{ C}$. Poiché il flusso cresce proporzionalmente al volume racchiuso per qualunque cubo scelto, la carica deve trovarsi distribuita uniformemente nello spazio con una densità volumica costante $\rho = 3\varepsilon_0 E_0$. Tale risultato anticipa la formulazione differenziale locale del teorema di Gauss, governata dall'operatore divergenza:
> 
> $$\nabla \cdot \vec{E} = \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z} = \frac{\partial (3x E_0)}{\partial x} + 0 + 0 = 3E_0 = \frac{\rho}{\varepsilon_0}$$


## Il teorema di Gauss

### Enunciato

Una volta chiarito che cos'è il flusso di un campo vettoriale attraverso una superficie, si può enunciare il teorema di Gauss. Si considera una superficie chiusa, detta **superficie gaussiana**, con alcune cariche al suo interno. Il teorema lega il flusso del campo elettrico attraverso la superficie alle cariche interne.

  

> [!important] Teorema di Gauss Data una superficie chiusa orientata $S$ (denominata **superficie gaussiana**), il flusso del campo elettrico attraverso $S$ moltiplicato per la permittività dielettrica del vuoto $\varepsilon_0$ equivale alla somma algebrica $q_{\text{in}}$ delle cariche racchiuse all'interno del volume delimitato dalla superficie:
> 
>   
> 
> $$\varepsilon_0\,\Phi_E = \varepsilon_0\oint_S \vec{E}\cdot d\vec{A} = q_{\text{in}}$$
> 
>   

La costante $\varepsilon_0 \approx 8{,}854 \times 10^{-12}\ \mathrm{C^2/(N\cdot m^2)}$ è la stessa che compare nella legge di Coulomb, scritta nella forma con $k = 1/(4\pi\varepsilon_0)$: la **costante dielettrica del vuoto**, o permittività elettrica del vuoto. Usare $k$ o $\varepsilon_0$ è del tutto equivalente.

  

"Somma algebrica" significa che ogni carica si conta con il proprio segno. Con tre cariche $q_1, q_2, q_3$ all'interno, $q_{\text{in}} = q_1 + q_2 + q_3$. Se ad esempio due cariche sono positive e una negativa, la carica totale interna può anche essere nulla, pur essendoci cariche dentro la superficie.

  

### Le cariche esterne non contribuiscono

Il teorema contiene un'affermazione implicita che non è affatto banale: le cariche **esterne** alla superficie non contribuiscono al flusso totale. Il risultato non è ovvio, perché anche le cariche esterne generano un campo elettrico, e quel campo attraversa la superficie: localmente un flusso c'è. Il teorema di Gauss assicura però che il loro contributo complessivo è nullo. Il campo di una carica esterna entra nella superficie da una parte ed esce dall'altra, e i due contributi, negativo ed entrante da un lato, positivo e uscente dall'altro, si bilanciano esattamente nell'integrale complessivo.

  

In pratica: si sceglie la superficie, si contano le cariche interne, e si ottiene immediatamente il flusso.

  

![[F2-L05-superfici-gaussiane.svg]]

  

### Perché è utile: la libertà di scegliere la superficie

Il teorema serve, ad esempio, quando l'integrale del flusso è troppo complicato da calcolare. Basta conoscere le cariche interne alla superficie per conoscere il flusso, senza fare l'integrale. Ma la proprietà che lo rende davvero potente è che **la superficie gaussiana è arbitraria**. Con le tre cariche della figura si può scegliere la superficie $S_1$, $S_2$ o $S_3$, o qualsiasi altra che le racchiuda: il flusso è sempre legato alla stessa somma algebrica delle cariche. Questa libertà permette di sfruttare le simmetrie. Se il problema ne ha una, si sceglie una superficie semplice adatta a quella simmetria: una sfera, un cilindro, a volte un cubo. Su una superficie del genere il campo ha un andamento così semplice che il flusso si lega direttamente alle cariche, senza dover conoscere in dettaglio la distribuzione di carica all'interno.

  

Il docente non dimostra il teorema in generale: servirebbero integrali in più dimensioni, il gradiente, la divergenza e concetti analoghi sviluppati nel corso di Metodi Matematici. Ne dà una dimostrazione nel caso delle superfici sferiche, le uniche che si trattano in modo elementare.

  

## Verifica per una carica puntiforme: l'angolo solido

Si vuole mostrare che il flusso generato da una carica puntiforme $q$ attraverso una sfera di raggio $R_1$ è uguale al flusso attraverso una sfera concentrica di raggio $R_2$. È un caso particolare (una sola carica posta al centro e superfici sferiche concentriche su cui il campo è noto dalla legge di Coulomb), ma fa intuire perché il meccanismo funzioni in generale.

  

### L'angolo solido

Nel piano, un arco di circonferenza è individuato dal raggio e da un angolo. Su una superficie sferica servono due angoli: uno che "spazza" una direzione e uno che spazza la direzione perpendicolare. L'**angolo solido** $d\Omega$ è la generalizzazione dell'angolo piano allo spazio tridimensionale. Il docente lo descrive intuitivamente come il prodotto dei due angoli $d\omega_1$ e $d\omega_2$ che delimitano un piccolo elemento di sfera.

  

Per ciascuna delle due direzioni vale la stessa relazione già usata per gli archi di circonferenza: si approssima il tratto di arco con un cateto di un triangolo rettangolo, per angoli piccoli il seno si confonde con l'angolo, e poi si passa agli infinitesimi. Su una sfera di raggio $R$ i due lati dell'elemento infinitesimo valgono quindi:

  

$$dl_1 = R\,d\omega_1, \qquad dl_2 = R\,d\omega_2$$

  

e l'area dell'elemento è il loro prodotto:

  

$$dA = dl_1\,dl_2 = R^2\,d\omega_1\,d\omega_2 = R^2\,d\Omega$$

  

La struttura è la stessa della relazione per gli archi: là una lunghezza è il raggio per un angolo ($ds = R\,d\theta$), qui un'area è il raggio al quadrato per un angolo solido ($dA = R^2\,d\Omega$). Si è semplicemente passati da una a due dimensioni.

  

![[F2-L05-angolo-solido.svg]]

  

> [!tip] Approfondimento — L'angolo solido in coordinate sferiche #approfondimento L'unità di misura dell'angolo solido è lo **steradiante** ($\mathrm{sr}$). L'angolo solido sotteso da una superficie è l'area che essa ritaglia sulla sfera di raggio unitario centrata nel vertice, e l'intera sfera corrisponde a $4\pi\ \mathrm{sr}$. In coordinate sferiche, con $\theta$ angolo polare (colatitudine dall'asse $z$) e $\varphi$ angolo azimutale nel piano $xy$, l'elemento di angolo solido è $d\Omega = \sin\theta\,d\theta\,d\varphi$. L'immagine del "prodotto di due angoli" è corretta per un elemento infinitesimo delimitato da due direzioni perpendicolari. Il fattore $\sin\theta$ tiene conto del fatto che i paralleli si accorciano avvicinandosi ai poli. Integrando su tutta la sfera:
> 
>   
> 
> $$\oint d\Omega = \int_0^{2\pi} d\varphi \int_0^{\pi} \sin\theta\,d\theta = 2\pi [-\cos\theta]_0^{\pi} = 4\pi\ \mathrm{sr}$$
> 
>   

### Il flusso non dipende dal raggio

La relazione $dA = R^2\,d\Omega$ vale per qualsiasi sfera. Si prende allora un unico angolo solido infinitesimo $d\Omega$, con il vertice nella carica $q$. Sulla sfera interna di raggio $R_1$ esso ritaglia l'area $dA_1 = R_1^2\,d\Omega$, su quella esterna di raggio $R_2$ l'area $dA_2 = R_2^2\,d\Omega$.

  

Su entrambe le sfere il versore normale $\hat{n}$ all'elemento di superficie è **radiale**. Anche il campo generato da una carica puntiforme è radiale, conformemente alla legge di Coulomb da cui deriva. I due vettori sono quindi rigorosamente paralleli ($\vec{E} \parallel \hat{n}$), e il prodotto scalare si riduce al prodotto algebrico dei moduli. Sostituendo il campo di Coulomb a distanza $R_1$ e a distanza $R_2$:

  

$$\begin{aligned} d\Phi_1 &= \vec{E}\cdot d\vec{A}_1 = E(R_1)\,dA_1 = \left(\frac{kq}{R_1^2}\right) \left(R_1^2\,d\Omega\right) = kq\,d\Omega, \\ d\Phi_2 &= \vec{E}\cdot d\vec{A}_2 = E(R_2)\,dA_2 = \left(\frac{kq}{R_2^2}\right) \left(R_2^2\,d\Omega\right) = kq\,d\Omega \end{aligned}$$

  

Risulta quindi $d\Phi_1 = d\Phi_2 = kq\,d\Omega$. Il flusso attraverso l'elemento **non dipende dal raggio** della sfera: dipende unicamente dall'angolo solido spazzato e dalla carica $q$. Il punto chiave è che il modulo del campo scala come $1/R^2$, mentre l'area dell'elemento scala come $R^2$: le due dipendenze geometriche si cancellano reciprocamente.

  

Integrando sull'intera sfera, poiché l'angolo solido totale vale $4\pi\ \mathrm{sr}$, il flusso complessivo è:

  

$$\Phi_E = \oint kq\,d\Omega = kq \oint d\Omega = kq\,(4\pi) = \left(\frac{1}{4\pi\varepsilon_0}\right) 4\pi q = \frac{q}{\varepsilon_0}$$

  

ovvero proprio l'enunciato del teorema di Gauss per una carica puntiforme.

  

Non si tratta di una dimostrazione generale completa, poiché riguarda una carica puntiforme e superfici sferiche concentriche. Tuttavia, sviluppando gli strumenti del calcolo differenziale vettoriale (teorema della divergenza), si dimostra che il risultato è identicamente valido per **qualsiasi** superficie chiusa e per una qualsiasi distribuzione di cariche: il flusso dipende unicamente dalla carica racchiusa. Questo caso mostra con chiarezza geometrica l'invarianza del flusso rispetto alla superficie gaussiana scelta.

  

## Dal teorema di Gauss alla legge di Coulomb

Come applicazione diretta, si calcola il campo generato da una carica puntiforme senza assumere a priori la legge di Coulomb, ma deducendola dal teorema di Gauss. Le due leggi sono infatti **interscambiabili**: assumendo Coulomb si può ricavare Gauss, e assumendo Gauss si ricava Coulomb. Nelle quattro equazioni fondamentali di Maxwell per l'elettromagnetismo, la formulazione assunta come assioma primario è proprio la legge di Gauss, non quella di Coulomb.

  

Si considera una carica puntiforme positiva $q$ posta nell'origine e, sfruttando la libertà di scelta della superficie gaussiana, si traccia una sfera di raggio $r$ concentrica alla carica.

  

1. **Direzione.** Per la simmetria sferica della carica puntiforme, il campo non può che essere radiale. Su ogni punto della sfera anche il versore normale uscente è radiale: campo e normale sono paralleli ovunque ($\vec{E} \parallel \hat{n}$), quindi $\vec{E}\cdot d\vec{A} = E\,dA$.
    
      
    
2. **Simmetria e modulo.** Una carica puntiforme isolata non possiede direzioni spaziali privilegiate: non vi è motivo per cui il campo debba essere più intenso lungo una direzione rispetto a un'altra. Il modulo del campo può dipendere solo dalla distanza $r$ dal centro, non dagli angoli. Su tutti i punti della sfera a raggio fisso $r$, il modulo $E$ è perciò rigorosamente costante e può essere portato fuori dall'integrale di superficie.
    
      
    
3. **Calcolo del flusso.** L'integrale si riduce all'area della sfera:
    
      
    
    $$\varepsilon_0 \oint_S \vec{E}\cdot d\vec{A} = \varepsilon_0 E \oint_S dA = \varepsilon_0\,E\,\left(4\pi r^2\right)$$
    
      
    
4. **Applicazione del teorema di Gauss.** Uguagliando il flusso alla carica interna racchiusa $q$:
    
      
    
    $$\varepsilon_0\,E\,\left(4\pi r^2\right) = q \quad\Longrightarrow\quad E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2} = \frac{kq}{r^2}$$
    
      
    

Si ritrova esattamente la dipendenza radiale e l'espressione analitica della legge di Coulomb.

  

![[F2-L05-gauss-carica-puntiforme.svg]]

  

> [!important] Coulomb e Gauss sono equivalenti Per cariche elettrostatiche stazionarie, la legge di Coulomb e il teorema di Gauss racchiudono la medesima fisica: dall'una si deduce l'altra. Il procedimento (analisi della simmetria, scelta della superficie adatta su cui il campo è parallelo alla normale e costante in modulo, estrazione del modulo dall'integrale e uguagliamento alla carica interna) costituisce lo schema operativo universale per ogni applicazione di Gauss.
> 
>   

> [!tip] Approfondimento — Perché Gauss è "più fondamentale" #approfondimento La legge di Coulomb descrive l'interazione elettrostatica istantanea tra cariche in quiete. Il teorema di Gauss (prima equazione di Maxwell, $\nabla\cdot\vec{E} = \rho/\varepsilon_0$) mantiene invece la sua piena validità anche nel regime elettrodinamico dipendente dal tempo, con cariche in moto e campi variabili che si propagano a velocità finita $c$, contesto in cui la formulazione originale di Coulomb cessa di essere rigorosa.

## Esercizio: carica puntiforme al centro di un guscio carico

> [!example] Testo Una carica puntiforme positiva $+q$ si trova al centro di un guscio sferico sottile di raggio $R$, carico uniformemente con carica totale $-Q$. Calcolare il campo elettrico in un punto interno al guscio, a distanza $r_1 < R$ dal centro, e in un punto esterno, a distanza $r_2 > R$.
> 
>   

### Perché non con la legge di Coulomb

Il campo della carica puntiforme centrale è noto immediatamente. Nel punto considerato agiscono però anche i campi di tutti gli elementi infinitesimi di superficie del guscio sferico. Con la legge di Coulomb bisognerebbe integrare vettorialmente tutti questi contributi: da una posizione interna eccentrica rispetto ai singoli elementi superficiali, le distanze e gli angoli variano punto per punto, rendendo l'integrale estremamente complicato e privo di una simmetria evidente rispetto al punto di osservazione.

  

### Risoluzione con il teorema di Gauss

Sfruttando la simmetria sferica globale della distribuzione attorno all'origine, il campo deve essere puramente radiale e dipendere esclusivamente dalla distanza $r$ dal centro. Si scelgono superfici gaussiane sferiche concentriche:

  

- **Punto interno ($r_1 < R$):** Si sceglie una superficie gaussiana sferica di raggio $r_1 < R$ concentrica alla carica. L'unica carica racchiusa è la carica centrale $+q$; la carica $-Q$ del guscio si trova all'esterno della superficie gaussiana e non dà alcun contributo al flusso totale:
    
      
    
    $$\varepsilon_0 \oint_{S_1} \vec{E}\cdot d\vec{A} = \varepsilon_0 E(r_1) (4\pi r_1^2) = q \implies E(r_1) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r_1^2} = \frac{kq}{r_1^2}$$
    
      
    
    All'interno della cavità il guscio carico circostante non ha alcun effetto sul campo elettrico: il campo è identico a quello che la carica $+q$ genererebbe se fosse completamente isolata nel vuoto.
    
      
    
- **Punto esterno ($r_2 > R$):** Si traccia una superficie gaussiana sferica di raggio $r_2 > R$ concentrica al sistema. Essa racchiude interamente sia la carica puntiforme centrale sia la carica distribuita sul guscio. La carica totale interna netta è la loro somma algebrica:
    
      
    
    $$q_{\text{in}} = q + (-Q) = q - Q$$
    
      
    
    Applicando il teorema di Gauss:
    
      
    
    $$\varepsilon_0 E(r_2) (4\pi r_2^2) = q - Q \implies E(r_2) = \frac{1}{4\pi\varepsilon_0}\frac{q - Q}{r_2^2}$$
    
      
    

![[F2-L05-guscio-e-carica-centrale.svg]]

  

Il verso del campo all'esterno è determinato dal segno della carica netta racchiusa:

  

- Se $\vert{}Q\vert{} > q$, la carica netta è negativa, $E(r_2) < 0$ e il campo è radiale **entrante**.
    
      
    
- Se $\vert{}Q\vert{} < q$, la carica netta è positiva, $E(r_2) > 0$ e il campo è radiale **uscente**.
    
      
    
- Se $\vert{}Q\vert{} = q$, la carica interna totale è nulla e all'esterno del guscio il campo elettrico svanisce identicamente ($E(r_2) = 0$).
    
      
    

> [!important] Scegliere la superficie giusta Il calcolo analitico si risolve in modo elementare solo grazie alla simmetria sferica, che garantisce l'uniformità del modulo del campo sui punti della sfera gaussiana concentrica. Con una superficie di forma diversa (ad esempio un cubo), il teorema di Gauss resterebbe formalmente valido, ma la distanza $r$ dal centro varierebbe lungo le facce, impedendo di estrarre $E$ dall'integrale. Come sottolinea il docente, la superficie gaussiana è del tutto arbitraria, ma «ci sono delle arbitrarietà furbe e delle arbitrarietà non furbe».
> 
>   

## Distribuzione delle cariche in un conduttore

Il teorema di Gauss consente di ricavare le leggi di confinamento spaziale della carica nei materiali conduttori all'equilibrio elettrostatico. Si considera un corpo conduttore isolato (ad esempio sospeso a un filo isolante per impedire dispersione o passaggio di cariche verso l'esterno) a cui viene conferita una carica netta in eccesso, positiva o negativa.

  

L'intuizione suggerisce che le cariche dello stesso segno, respingendosi reciprocamente secondo la legge di Coulomb, tendano ad allontanarsi il più possibile, disponendosi sulla superficie esterna del corpo dove la distanza reciproca è massima. Sebbene intuitivo, questo ragionamento non spiega cosa accada in corpi di geometria irregolare o in presenza di punte. Il teorema di Gauss fornisce una deduzione rigorosa e generale basata su principi fisici fondamentali.

  

### 1. Campo elettrico nullo all'interno del conduttore

In condizioni statiche (assenza di generatori esterni o correnti stazionarie), il campo elettrico macroscopico all'interno della massa di un conduttore è identicamente nullo:

  

$$\vec{E}_{\text{int}} = 0$$

  

La motivazione risiede nella dinamica dei portatori e nella conservazione dell'energia:

  

1. Se all'interno del conduttore esistesse un campo $\vec{E} \neq 0$, le cariche libere subirebbero una forza $\vec{F} = q\vec{E}$, muovendosi all'interno del reticolo cristallino.
    
      
    
2. Il conduttore possiede una resistenza non nulla: il moto ordinato delle cariche genererebbe dissipazione energetica per effetto Joule.
    
      
    
3. In un corpo isolato privo di alimentazione continua, il moto dissipativo non può sostenersi indefinitamente. I moti transitori si estinguono e il sistema raggiunge necessariamente uno stato finale di equilibrio statico caratterizzato dall'assoluta assenza di forze nette interne sui portatori liberi, imponendo $\vec{E} = 0$ in ogni punto del volume massivo.
    
      
    

### 2. Il teorema di Gauss applicato alla massa del conduttore

Si traccia una superficie gaussiana $S$ situata interamente all'interno del materiale conduttore, a una distanza infinitesima al di sotto della sua superficie fisica esterna.

  

- Poiché la superficie $S$ giace nel metallo, in ogni suo punto il campo elettrico è nullo: $\vec{E} = 0$.
    
      
    
- Il flusso attraverso la superficie gaussiana è conseguentemente nullo:
    
      
    
    $$\Phi_E = \oint_S \vec{E}\cdot d\vec{A} = 0$$
    
      
    
- Per il teorema di Gauss, la carica netta contenuta nel volume racchiuso deve essere zero:
    
      
    
    $$q_{\text{in}} = \varepsilon_0 \Phi_E = 0$$
    
      
    

Poiché questa proprietà vale per qualunque superficie interna tracciata a distanza arbitrariamente piccola dal bordo, ne consegue che all'interno del volume del conduttore non può risiedere alcuna densità volumica netta di carica. L'unica localizzazione consentita per la carica in eccesso è la **superficie esterna** del conduttore.

  

### 3. Conduttore con cavità vuota (schermo elettrostatico)

Si consideri un blocco conduttore al cui interno è presente una cavità vuota priva di cariche. Ci si domanda se la carica in eccesso possa distribuirsi anche sulla superficie libera interna che delimita la cavità.

  

Si traccia una superficie gaussiana chiusa che avvolge la cavità, mantenendosi interamente immersa nella massa del conduttore.

  

1. Sulla superficie gaussiana il campo elettrico è ovunque nullo ($\vec{E} = 0$), in quanto interna al conduttore.
    
      
    
2. Il flusso è nullo, imponendo per Gauss che la carica totale racchiusa sia nulla: $q_{\text{in}} = 0$.
    
      
    
3. Poiché all'interno della cavità non vi sono cariche libere inserite, la carica netta depositata sulla parete della cavità deve essere rigorosamente nulla:
    
      
    
    $$q_{\text{parete}} = 0$$
    
      
    

Tutta la carica netta in eccesso si dispone forzatamente sulla sola superficie esterna del corpo conduttore.

  

![[F2-L05-cariche-nei-conduttori.svg]]

  

Snippet di codice

```
graph TD
    Conduttore["Conduttore isolato carico in equilibrio"]
    Conduttore --> CampoNullo["E = 0 all'interno della massa"]
    CampoNullo --> Gauss["Gauss su superficie interna infinitesima"]
    Gauss --> CaricaZero["Carica volumica interna q_in = 0"]
    CaricaZero --> Conclusione["Tutta la carica migra sulla superficie esterna"]
    CampoNullo --> Cavita["Gauss attorno a cavità vuota"]
    Cavita --> Schermo["q_parete = 0 (Schermo elettrostatico)"]
```

> [!important] Cariche in un conduttore in equilibrio In condizioni statiche il campo elettrico all'interno di un conduttore è identicamente nullo, e tutta la carica netta in eccesso si distribuisce esclusivamente sulla superficie esterna. Se il conduttore racchiude una cavità vuota, sulla superficie interna della cavità non è presente alcuna carica netta.
> 
>   

> [!tip] Approfondimento — Due precisazioni #approfondimento
> 
>   
> 
> - **Carica netta vs distribuzione locale:** Il teorema di Gauss assicura che l'integrale della carica sulla parete interna della cavità vuota è nullo ($q_{\text{parete}} = 0$). L'assoluta assenza di cariche locali (escludendo la presenza di zone positive e negative contrapposte) discende dall'analisi del **potenziale elettrostatico**: l'intero conduttore costituisce un volume equipotenziale; se nella cavità vuota vi fossero campi elettrici diretti da regioni positive a negative, si instaurerebbero differenze di potenziale tra punti del medesimo corpo conduttore, violando la condizione di equilibrio.
>     
>       
>     
> - **Effetto delle punte:** Sulla superficie esterna di conduttori con geometria non sferica, la carica non si distribuisce uniformemente: la densità superficiale di carica $\sigma$ si addensa nelle regioni a maggior curvatura locale (raggi di curvatura minimi, ossia le punte), determinando campi elettrici locali molto intensi all'esterno (principio del parafulmine).
>     
>       
>     

## In sintesi

Il flusso del campo elettrico quantifica il numero netto di linee di campo che attraversano una superficie orientata. Nelle configurazioni poliedriche immerse in campi disomogenei, come il cubo orientato lungo gli assi coordinati, il flusso totale corrisponde alla somma dei contributi delle singole facce: componenti di campo ortogonali ai versori normali generano flussi nulli, mentre variazioni spaziali del campo lungo la normale determinano un flusso netto globale non nullo, proporzionale al volume racchiuso e rappresentativo della divergenza delle sorgenti interne.

  

Il teorema di Gauss stabilisce che il flusso totale del campo elettrico attraverso una qualsiasi superficie chiusa, moltiplicato per $\varepsilon_0$, equivale alla somma algebrica delle sole cariche racchiuse all'interno. Le cariche esterne, pur producendo un campo che attraversa localmente la superficie, non contribuiscono al bilancio complessivo in quanto le linee entranti compensano esattamente quelle uscenti. La verifica analitica condotta per una carica puntiforme mediante l'angolo solido dimostra che la validità del teorema è una diretta conseguenza della decrescita con la legge dell'inverso del quadrato della distanza ($1/r^2$), la quale compensa esattamente la crescita quadratica dell'area con il raggio ($r^2$). Invertendo il percorso logico, il teorema di Gauss consente di ricavare direttamente la legge di Coulomb attraverso l'applicazione della simmetria sferica.

  

Applicato ai materiali conduttori, Gauss chiarisce la dinamica dell'equilibrio elettrostatico: poiché la presenza di campi interni provocherebbe moti continui di carica con dissipazione per effetto Joule incompatibili con lo stato statico, il campo elettrico nella massa del conduttore deve annullarsi identicamente. Di conseguenza, il flusso attraverso qualsiasi superficie gaussiana interna è nullo, dimostrando che non possono esistere cariche nette volumetriche: tutte le cariche in eccesso risiedono sulla superficie esterna, lasciando neutre anche le pareti di cavità interne vuote. Questo principio verrà impiegato nella lezione successiva per determinare il campo elettrostatico di lamine conduttrici infinite e configurazioni con distribuzioni spaziali continue.
