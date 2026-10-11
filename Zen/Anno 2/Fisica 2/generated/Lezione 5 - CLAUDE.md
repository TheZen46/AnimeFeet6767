---

## corso: Fisica 2 lezione: 5 data: 2026-10-06 argomenti: [flusso di un campo non uniforme, teorema di Gauss, superficie gaussiana, angolo solido, legge di Coulomb dal teorema di Gauss, guscio sferico carico, cariche nei conduttori] bibliography: fisica2.bib tags: [fisica2]
---
# Lezione 5 — Il teorema di Gauss

La lezione completa il discorso sul flusso con un esempio in cui il campo non è uniforme, poi introduce il risultato centrale dell'elettrostatica: il **teorema di Gauss**, che lega il flusso del campo elettrico attraverso una superficie chiusa alle cariche contenute al suo interno. Il teorema non viene dimostrato in generale. Il docente mostra però che vale per superfici sferiche attorno a una carica puntiforme, introducendo l'angolo solido. Ne ricava la legge di Coulomb e lo applica a un primo esercizio tipico. Infine lo usa "al contrario", per capire come si distribuiscono le cariche in un conduttore.

> [!tip] Legenda delle figure In tutte le figure del corso le cariche positive sono in **blu** e quelle negative in **rosso**, come nei tuoi appunti. Il campo elettrico è in **verde petrolio**, le superfici gaussiane in **giallo tratteggiato**, i versori normali in **viola** e le forze in **verde**. I file `.svg` vanno nella cartella `Allegati` del vault, ma Obsidian li trova anche in qualsiasi altra cartella, purché il nome resti invariato.

## Riepilogo: il flusso del campo elettrico

La registrazione comincia mentre il docente riprende la definizione di flusso vista nella [[Fisica 2 - Lezione 04 - Dipolo in campo elettrico e flusso|lezione 4]]. A ogni elemento infinitesimo di superficie si associa il vettore $d\vec A = dA,\hat n$, che ha per modulo l'area dell'elemento e per direzione la normale alla superficie. Il flusso infinitesimo è il prodotto scalare $d\Phi_E = \vec E\cdot d\vec A$, e il flusso attraverso tutta la superficie chiusa si ottiene sommando i contributi di tutti gli elementi:

$$ \Phi_E = \oint \vec E\cdot d\vec A . $$

Il docente precisa che questa definizione matematica vale sempre, ma in generale l'integrale non si sa calcolare, perché diventa troppo complesso. In alcuni casi speciali, però, le cose si semplificano. Sono quelli che capiteranno anche a noi: superfici particolari, come sfere o cilindri, su cui la simmetria rende semplice il campo elettrico. L'esempio del cilindro in un campo uniforme è già stato fatto. Il prossimo è un po' più ricco, perché il campo non è uniforme.

## Esempio: flusso di un campo non uniforme attraverso un cubo

> [!example] Testo Il campo elettrico è $$ \vec E = E_0\left(3x,\hat\imath + 4,\hat\jmath\right), $$ con $x$ misurato in metri. Calcolare il flusso attraverso la superficie di un cubo con le facce parallele ai piani coordinati, i cui lati lungo $x$ vanno da $x = 1\ \mathrm m$ a $x = 3\ \mathrm m$.

**La normalizzazione.** Il campo è scritto in unità di una costante $E_0$, che porta con sé le dimensioni di un campo elettrico ($\mathrm{N/C}$). In questo modo $\vec E/E_0 = 3x,\hat\imath + 4,\hat\jmath$ si può trattare come un vettore di numeri puri, e nei conti "le unità ce le dimentichiamo". Le si recupera alla fine, moltiplicando per $E_0$.

**Com'è fatto il campo.** Le tre componenti si leggono separatamente.

- **Componente $x$.** Vale $3x,E_0$: è nulla nell'origine e cresce linearmente spostandosi lungo l'asse $x$.
- **Componente $y$.** Vale sempre $4E_0$: non dipende da alcuna coordinata.
- **Componente $z$.** Non c'è.

Il campo ha quindi due componenti, una costante lungo $y$ e una che cresce con $x$. Nel disegno il docente usa una terna con l'asse $z$ rivolto verso chi guarda.

**Il cubo.** Il lato lungo $x$ va da $1$ a $3$, quindi misura $2\ \mathrm m$. Poiché si tratta di un cubo con le facce parallele agli assi, la superficie è completamente determinata: ogni faccia ha area $A = 4\ \mathrm{m^2}$.

![[F2-L05-cubo-normali.svg]]

**Il metodo.** Il flusso attraverso la superficie chiusa si spezza nella somma dei flussi attraverso le sei facce, calcolati separatamente. Su ogni faccia il versore normale uscente $\hat n$ è sempre lo stesso, quindi il vettore area è semplicemente $\vec A = A,\hat n$.

**Facce perpendicolari all'asse $z$.** Il versore normale è $\pm\hat k$. Il campo non ha componente lungo $z$, e i prodotti scalari $\hat\imath\cdot\hat k$ e $\hat\jmath\cdot\hat k$ sono nulli, perché i versori sono ortonormali. Su queste due facce il flusso è **nullo**.

**Facce perpendicolari all'asse $y$.** Sulla faccia superiore il versore normale uscente è $\hat\jmath$, su quella inferiore $-\hat\jmath$:

$$ \frac{\vec E}{E_0}\cdot A,\hat\jmath = \left(3x,\hat\imath + 4,\hat\jmath\right)\cdot A,\hat\jmath = 4A, \qquad \frac{\vec E}{E_0}\cdot\left(-A,\hat\jmath\right) = -4A . $$

Il calcolo è identico, salvo il segno. Su ciascuna delle due facce il flusso è diverso da zero, ma i due flussi sono **uguali e opposti** e si compensano. Il motivo è che la componente $y$ del campo è la stessa su entrambe le facce.

**Facce perpendicolari all'asse $x$.** Sulla faccia di destra ($x = 3$) il versore normale è $\hat\imath$, su quella di sinistra ($x = 1$) è $-\hat\imath$. Ora il prodotto scalare seleziona la componente $x$ del campo, che dipende da $x$. Su ciascuna faccia, però, $x$ è fissata: il campo varia lungo $x$, ma è costante su tutta la faccia. Basta quindi specificare la $x$ di ciascuna faccia:

$$ \Phi_{x=3} = 3,x_{\text{dx}},A,E_0, \qquad \Phi_{x=1} = -3,x_{\text{sx}},A,E_0, $$

con $x_{\text{dx}} = 3\ \mathrm m$ e $x_{\text{sx}} = 1\ \mathrm m$. Questa volta i due flussi **non** si compensano: il campo sulla faccia di destra è più intenso di quello sulla faccia di sinistra, e la differenza è un flusso finito.

**Flusso totale.** Restano solo i contributi delle due facce perpendicolari a $x$:

$$ \Phi_{\text{tot}} = 3A\left(x_{\text{dx}} - x_{\text{sx}}\right)E_0 = 3\cdot 4\ \mathrm{m^2}\cdot 2\cdot E_0 = 24\ \mathrm{m^2},E_0 . $$

Con $E_0$ in $\mathrm{N/C}$, il flusso risulta in $\mathrm{N,m^2/C}$, come deve essere.

![[F2-L05-cubo-flussi.svg]]

Il docente osserva che il calcolo vale in generale, per qualsiasi $x_{\text{sx}}$ e $x_{\text{dx}}$: l'unica scelta fatta è che le facce siano parallele agli assi. Per un cubo, inoltre, l'area di una faccia è $A = (x_{\text{dx}} - x_{\text{sx}})^2$. Il flusso diventa quindi $3E_0,(x_{\text{dx}} - x_{\text{sx}})^3$, cioè **proporzionale al volume del cubo**.

> [!warning] Numerazione delle facce Alla lavagna, e quindi nella trascrizione, i numeri delle facce cambiano durante il calcolo: "1" e "2" indicano prima le facce lungo $z$, poi quelle lungo $y$. Negli appunti a mano il flusso della faccia $x = 3$ è chiamato $\Phi_5$. Qui le facce sono numerate come nella seconda figura.

> [!tip] Approfondimento — Che cosa c'è dentro il cubo? #approfondimento Applicando il teorema di Gauss, introdotto subito dopo, il cubo contiene una carica $q_{\text{in}} = \varepsilon_0\Phi = 24\ \mathrm{m^2},\varepsilon_0 E_0$. Poiché il flusso è proporzionale al volume per qualsiasi cubo, la carica deve essere distribuita **uniformemente** nello spazio, con densità volumica $\rho = 3\varepsilon_0E_0$ costante: $\rho\cdot V = 3\varepsilon_0 E_0\cdot 8\ \mathrm{m^3}$ dà lo stesso risultato. È un'anticipazione della forma locale del teorema, $\nabla\cdot\vec E = \rho/\varepsilon_0$. Qui la divergenza vale $\partial E_x/\partial x + \partial E_y/\partial y = 3E_0$. La divergenza si studia in Metodi Matematici.

## Il teorema di Gauss

### Enunciato

Una volta chiarito che cos'è il flusso di un campo vettoriale attraverso una superficie, si può enunciare il teorema di Gauss. Si considera una superficie chiusa, detta **superficie gaussiana**, con alcune cariche al suo interno. Il teorema lega il flusso del campo elettrico attraverso la superficie alle cariche interne.

> [!important] Teorema di Gauss $$ \varepsilon_0,\Phi_E = \varepsilon_0\oint_S \vec E\cdot d\vec A = q_{\text{in}} $$ Il flusso del campo elettrico attraverso una superficie chiusa $S$, moltiplicato per $\varepsilon_0$, è uguale alla **somma algebrica** $q_{\text{in}}$ delle cariche contenute all'interno di $S$.

La costante $\varepsilon_0$ è la stessa che compare nella legge di Coulomb, scritta nella forma con $k = 1/(4\pi\varepsilon_0)$: la **costante dielettrica del vuoto**, o permittività elettrica del vuoto. Usare $k$ o $\varepsilon_0$ è del tutto equivalente.

"Somma algebrica" significa che ogni carica si conta con il proprio segno. Con tre cariche $q_1$, $q_2$, $q_3$ all'interno, $q_{\text{in}} = q_1 + q_2 + q_3$. Se ad esempio due cariche sono positive e una negativa, la carica totale interna può anche essere nulla, pur essendoci cariche dentro la superficie.

### Le cariche esterne non contribuiscono

Il teorema contiene un'affermazione implicita che, sottolinea il docente, non è affatto banale: le cariche **esterne** alla superficie non contribuiscono al flusso totale. Il risultato non è ovvio, perché anche le cariche esterne generano un campo elettrico, e quel campo attraversa la superficie: localmente un flusso c'è. Il teorema di Gauss, che non dimostriamo, assicura però che il loro contributo complessivo è nullo. Il campo di una carica esterna entra nella superficie da una parte ed esce dall'altra, e i due contributi, negativo e positivo, si bilanciano esattamente.

In pratica: si sceglie la superficie, si contano le cariche interne, e si ottiene immediatamente il flusso.

![[F2-L05-superfici-gaussiane.svg]]

### Perché è utile: la libertà di scegliere la superficie

Il teorema serve, ad esempio, quando l'integrale del flusso è troppo complicato da calcolare. Basta conoscere le cariche interne alla superficie per conoscere il flusso, senza fare l'integrale. Ma la proprietà che lo rende davvero potente è che **la superficie gaussiana è arbitraria**. Con le tre cariche della figura si può scegliere la superficie $S_1$, $S_2$ o $S_3$, o qualsiasi altra che le racchiuda: il flusso è sempre legato alla stessa somma algebrica delle cariche. Questa libertà permette di sfruttare le simmetrie. Se il problema ne ha una, si sceglie una superficie semplice adatta a quella simmetria: una sfera, un cilindro, a volte un cubo. Su una superficie del genere il campo ha un andamento così semplice che il flusso si lega direttamente alle cariche, senza dover conoscere in dettaglio la distribuzione di carica all'interno.

Il docente non dimostra il teorema in generale. Servirebbero integrali in più dimensioni, il gradiente e concetti analoghi, che si sviluppano nel corso di Metodi Matematici. Ne dà una dimostrazione nel caso delle superfici sferiche, le uniche che si trattano in modo semplice.

## Verifica per una carica puntiforme: l'angolo solido

Si vuole mostrare che il flusso generato da una carica puntiforme $q$ attraverso una sfera di raggio $R_1$ è uguale al flusso attraverso una sfera concentrica di raggio $R_2$. È un caso molto particolare: una sola carica, al centro, e superfici sferiche, su cui il campo è noto dalla legge di Coulomb. Fa però intuire che c'è qualcosa che funziona in generale.

### L'angolo solido

Nel piano, un arco di circonferenza è individuato da un angolo. Su una superficie sferica servono due angoli: uno che "spazza" una direzione e uno che spazza la direzione perpendicolare. L'**angolo solido** $d\Omega$ è la generalizzazione dell'angolo piano a questa situazione. Il docente lo descrive come il prodotto dei due angoli $d\omega_1$ e $d\omega_2$ che delimitano un piccolo elemento di sfera.

Per ciascuna delle due direzioni vale la stessa relazione già usata per gli archi di circonferenza: si approssima il tratto di arco con un cateto di un triangolo rettangolo, per angoli piccoli il seno si confonde con l'angolo, e poi si passa agli infinitesimi. Su una sfera di raggio $R$ i due lati dell'elemento valgono quindi

$$ dl_1 = R,d\omega_1, \qquad dl_2 = R,d\omega_2 , $$

e l'area dell'elemento è il loro prodotto:

$$ dA = dl_1,dl_2 = R^2,d\omega_1,d\omega_2 = R^2,d\Omega . $$

La struttura è la stessa della relazione per gli archi: là una lunghezza è il raggio per un angolo, qui un'area è il raggio al quadrato per un angolo solido. Si è semplicemente passati da una a due dimensioni.

![[F2-L05-angolo-solido.svg]]

> [!tip] Approfondimento — L'angolo solido in coordinate sferiche #approfondimento L'unità di misura dell'angolo solido è lo **steradiante** ($\mathrm{sr}$). L'angolo solido sotteso da una superficie è l'area che essa ritaglia sulla sfera di raggio unitario centrata nel vertice, e l'intera sfera corrisponde a $4\pi\ \mathrm{sr}$. In coordinate sferiche, con $\theta$ angolo dall'asse $z$ e $\varphi$ angolo nel piano $xy$, l'elemento di angolo solido è $d\Omega = \sin\theta,d\theta,d\varphi$. L'immagine del "prodotto di due angoli" è corretta per un elemento infinitesimo delimitato da due direzioni perpendicolari. Il fattore $\sin\theta$ tiene conto del fatto che i paralleli si accorciano avvicinandosi ai poli. Integrando, $\int_0^{2\pi}!\int_0^{\pi}\sin\theta,d\theta,d\varphi = 4\pi$.

### Il flusso non dipende dal raggio

La relazione $dA = R^2 d\Omega$ vale per qualsiasi sfera. Si prende allora un unico angolo solido $d\Omega$, con il vertice nella carica. Sulla sfera interna esso ritaglia l'area $dA_1 = R_1^2,d\Omega$, su quella esterna l'area $dA_2 = R_2^2,d\Omega$.

Su entrambe le sfere il versore normale all'elemento di superficie è **radiale**. Anche il campo di una carica puntiforme è radiale, come la forza di Coulomb da cui deriva. I due vettori sono quindi paralleli, e il prodotto scalare si riduce al prodotto dei moduli. Sostituendo il campo di Coulomb a distanza $R_1$ e a distanza $R_2$:

$$ \begin{aligned} d\Phi_1 &= \vec E\cdot d\vec A_1 = E,dA_1 = \frac{kq}{R_1^2},R_1^2,d\Omega = kq,d\Omega,\[4pt] d\Phi_2 &= \vec E\cdot d\vec A_2 = E,dA_2 = \frac{kq}{R_2^2},R_2^2,d\Omega = kq,d\Omega . \end{aligned} $$

Quindi $d\Phi_1 = d\Phi_2 = kq,d\Omega$. Il flusso attraverso l'elemento **non dipende dal raggio** della sfera: dipende solo dall'angolo solido spazzato e dalla carica $q$. Il "trucchetto", come lo chiama il docente, è che il campo scala come $1/R^2$, mentre l'area dell'elemento scala come $R^2$, e le due dipendenze si cancellano.

Resta da integrare su tutta la sfera. Poiché l'angolo solido totale vale $4\pi$, il flusso complessivo è $\Phi = 4\pi kq = q/\varepsilon_0$, che è proprio il teorema di Gauss per una carica puntiforme.

Non è una dimostrazione completa, perché riguarda una carica puntiforme e superfici sferiche. Il docente assicura che, sviluppando tutta la matematica necessaria, si dimostra che il risultato vale per **qualsiasi** superficie chiusa: il flusso dipende solo dalla carica racchiusa. Intanto questo caso particolare mostra che il flusso non dipende dalla superficie gaussiana, e quindi dà la libertà di sceglierla.

## Dal teorema di Gauss alla legge di Coulomb

Come esempio, il docente calcola il campo di una carica puntiforme senza la legge di Coulomb, partendo dal teorema di Gauss. Le due leggi sono **intercambiabili**: si può assumere la legge di Coulomb e ricavare il teorema di Gauss, oppure assumere il teorema di Gauss e ricavare la legge di Coulomb. Nelle equazioni di Maxwell, le equazioni fondamentali dell'elettromagnetismo, la legge fondamentale è quella di Gauss, non quella di Coulomb.

Si prende una carica puntiforme positiva $q$ e, poiché la superficie gaussiana è arbitraria, una sfera di raggio $r$ concentrica alla carica.

1. **Direzione.** Il campo è radiale, e su ogni elemento della sfera anche il versore normale è radiale. Campo e normale sono paralleli, quindi $\vec E\cdot d\vec A = E,dA$.
2. **Simmetria.** Una carica puntiforme ha simmetria sferica: non c'è alcun motivo per cui il campo sia più intenso in una direzione che in un'altra. Il modulo del campo può dipendere dalla distanza $r$, ma non dagli angoli. Sulla sfera, dove tutti i punti hanno la stessa $r$, il campo ha quindi lo stesso valore ovunque e può uscire dall'integrale.
3. **Integrale.** Resta l'integrale di $dA$ su tutta la sfera, cioè la sua area: $$ \varepsilon_0\oint \vec E\cdot d\vec A = \varepsilon_0 E\oint dA = \varepsilon_0,E,4\pi r^2 . $$
4. **Teorema di Gauss.** Uguagliando alla carica interna: $$ \varepsilon_0,E,4\pi r^2 = q \quad\Longrightarrow\quad E = \frac{1}{4\pi\varepsilon_0},\frac{q}{r^2} = k,\frac{q}{r^2}. $$

È esattamente il campo dato dalla legge di Coulomb.

![[F2-L05-gauss-carica-puntiforme.svg]]

> [!important] Coulomb e Gauss sono equivalenti Per cariche ferme, la legge di Coulomb e il teorema di Gauss contengono la stessa fisica: dall'una si ricava l'altra. Il procedimento appena visto, cioè simmetria, superficie adatta, campo costante sulla superficie e integrale ridotto a un'area, è lo schema che si ripete in tutte le applicazioni del teorema.

> [!tip] Approfondimento — Perché Gauss è "più fondamentale" #approfondimento La legge di Coulomb descrive la forza tra cariche **ferme**. Il teorema di Gauss resta valido anche quando cariche e campi variano nel tempo, ed è per questo che compare tra le equazioni di Maxwell, mentre la legge di Coulomb ne è un caso particolare. I testi di Fisica 2 tornano su questo punto quando presentano le equazioni di Maxwell al completo.

## Esercizio: carica puntiforme al centro di un guscio carico

> [!example] Testo Una carica puntiforme positiva $+q$ si trova al centro di un guscio sferico di raggio $R$, carico uniformemente con carica $-Q$. Calcolare il campo elettrico in un punto interno al guscio, a distanza $r_1 < R$ dal centro, e in un punto esterno, a distanza $r_2 > R$.

Il docente lo presenta come un esercizio facile ma prototipico, perché mostra in quale situazione conviene usare il teorema di Gauss. I valori numerici sono poco importanti.

**Perché non con la legge di Coulomb.** Il campo della carica puntiforme è noto. Nel punto considerato agiscono però anche i campi di tutti i "pezzettini" del guscio, e con la legge di Coulomb bisognerebbe sommare tutti quei contributi. Visti da un punto generico, gli elementi del guscio non si dispongono in modo simmetrico, e diventa molto difficile anche solo impostare l'integrale, figuriamoci risolverlo.

**Con il teorema di Gauss.** Si prende una superficie gaussiana sferica concentrica passante per il punto. Il flusso è determinato solo dalla carica racchiusa. Per la simmetria sferica il campo è radiale e dipende solo da $r$, quindi il calcolo è identico a quello appena svolto per la carica puntiforme.

- **Punto interno ($r_1 < R$).** La sfera di raggio $r_1$ contiene solo la carica $+q$; la carica $-Q$ del guscio è esterna e si trascura: $$ \varepsilon_0,E,4\pi r_1^2 = q \quad\Longrightarrow\quad E(r_1) = \frac{1}{4\pi\varepsilon_0},\frac{q}{r_1^2}. $$ È di nuovo la legge di Coulomb: il guscio non ha alcun effetto all'interno.
- **Punto esterno ($r_2 > R$).** La sfera di raggio $r_2$ contiene sia la carica puntiforme sia il guscio: $q_{\text{in}} = q - Q$. La distribuzione sul guscio è omogenea, quindi la simmetria resta sferica e il calcolo è lo stesso: $$ E(r_2) = \frac{1}{4\pi\varepsilon_0},\frac{q - Q}{r_2^2}. $$

![[F2-L05-guscio-e-carica-centrale.svg]]

Il campo esterno può risultare positivo o negativo, e il segno ne indica il verso, che è sempre radiale. Se $|Q| > q$, la carica del guscio prevale, $E$ è negativo e il campo è diretto **verso l'interno**. Se $|Q| < q$, il campo è positivo e diretto **verso l'esterno**. Il verso è determinato dalla carica netta inglobata nella sfera: se è negativa, il campo entra nella superficie gaussiana invece di uscirne.

> [!important] Scegliere la superficie giusta Il calcolo è semplice perché la simmetria è sferica: il campo dipende solo da $r$, e su una sfera concentrica è costante. Con un cubo come superficie gaussiana il teorema varrebbe ancora, ma la distanza dal centro cambierebbe da punto a punto della superficie, il campo non sarebbe costante e l'integrale non si saprebbe fare. La superficie gaussiana è arbitraria, ma, come dice il docente, "ci sono delle arbitrarietà furbe e delle arbitrarietà non furbe".

## Distribuzione delle cariche in un conduttore

Il teorema di Gauss serve anche a capire come **devono** distribuirsi le cariche, ad esempio in un conduttore. Si consideri un corpo conduttore, in cui le cariche si muovono liberamente, appeso a un filo isolante. Il filo impedisce alla carica di passare, quindi il conduttore resta isolato. Gli si dà un eccesso di carica, ad esempio positiva. Come si distribuisce?

L'intuizione suggerisce che le cariche, respingendosi, vadano sulla superficie, dove la loro distanza reciproca è massima. Il ragionamento funziona per forme regolari, ma se il conduttore ha una punta non è più chiaro che cosa accada. Con il teorema di Gauss lo si può invece stabilire in generale.

**Primo ingrediente: nel conduttore il campo è nullo.** In condizioni statiche il campo elettrico all'interno di un conduttore è zero. È un'evidenza sperimentale, giustificata da un bilancio energetico. Se all'interno ci fosse un campo, le cariche libere sarebbero soggette a una forza e si sposterebbero. Il conduttore ha una resistenza, quindi il moto delle cariche dissiperebbe energia, e prima o poi le cariche dovrebbero fermarsi. Lo stato finale di un conduttore isolato è quindi quello in cui il campo interno è nullo.

**Secondo ingrediente: il teorema di Gauss "al contrario".** Si sceglie una superficie gaussiana vicinissima alla superficie del conduttore, ma interna a esso. In ogni suo punto il campo è nullo, quindi il flusso è nullo, e per il teorema di Gauss la carica racchiusa è nulla. L'unica possibilità è che tutta la carica in eccesso si trovi **sulla superficie** del conduttore.

**Conduttore con una cavità.** Il caso è un po' meno intuitivo. Se il conduttore è "scavato" all'interno, anche la parete della cavità è una superficie libera, e in linea di principio le cariche potrebbero disporsi anche lì. Si ripete lo stesso argomento con una superficie gaussiana che circonda la cavità, restando dentro il conduttore. Il campo è nullo ovunque su di essa, quindi il flusso è nullo, e la carica racchiusa è zero: sulla parete della cavità non c'è carica netta. Anche in questo caso le cariche si dispongono sulla superficie **esterna**.

![[F2-L05-cariche-nei-conduttori.svg]]

> [!important] Cariche in un conduttore in equilibrio In condizioni statiche il campo elettrico all'interno di un conduttore è nullo, e tutta la carica in eccesso si dispone sulla sua superficie esterna. Se il conduttore ha una cavità vuota, sulla parete della cavità non c'è carica netta.

> [!tip] Approfondimento — Due precisazioni #approfondimento
> 
> - **Carica netta e distribuzione.** Il teorema di Gauss garantisce che la carica **totale** sulla parete della cavità è nulla. Da solo non esclude che vi siano zone positive e zone negative che si compensano. Questa possibilità si esclude con il **potenziale elettrico**: linee di campo che andassero da una zona positiva a una negativa attraverso la cavità implicherebbero una differenza di potenziale tra due punti dello stesso conduttore, che invece è tutto allo stesso potenziale. L'argomento si vedrà quando verrà introdotto il potenziale.
> - **Le punte.** Il dubbio del docente sulle punte ha una risposta precisa. Sulla superficie di un conduttore la densità di carica è maggiore dove la curvatura è maggiore, cioè sulle punte. È il principio del parafulmine. Anche questo si spiega con il potenziale.

Il docente anticipa che questo risultato verrà sfruttato nella lezione successiva per calcolare il campo generato da una lamina conduttrice infinita: si veda [[Zen/Anno 2/Fisica 2/generated/Lezione 6 - CLAUDE|Lezione 6 - CLAUDE]].