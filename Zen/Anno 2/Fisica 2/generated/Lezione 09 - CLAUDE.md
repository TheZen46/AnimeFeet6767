---
corso: Fisica 2
lezione: 9
data: 2026-10-20
argomenti: [cariche e tensioni in un circuito di condensatori, condensatore carico collegato a uno scarico, conservazione della carica, energia immagazzinata in un condensatore, densità di energia del campo elettrico, dielettrici, molecole polari, polarizzazione, carica di polarizzazione, costante dielettrica, teorema di Gauss nei dielettrici, spostamento elettrico, condensatore con lastra dielettrica]
bibliography: fisica2.bib
tags: [fisica2]
---

# Lezione 9 — Energia dei condensatori e dielettrici

Questa lezione si è svolta online. Comincia con due esercizi sui circuiti di condensatori: il primo completa quello della [[Fisica 2 - Lezione 08 - Potenziale del disco e condensatori|lezione 8]], il secondo introduce un'idea che tornerà spesso, cioè che la carica si conserva quando si chiude un interruttore. Poi si calcola l'**energia** immagazzinata in un condensatore e si studia che cosa succede quando tra le armature si mette un materiale isolante, un **dielettrico**. Il dielettrico abbassa il campo e aumenta la capacità; per descriverlo si scrive il teorema di Gauss in una forma che contiene solo le cariche libere. Un esercizio su un condensatore con una lastra dielettrica chiude la lezione e prosegue nella [[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]].

> [!warning] Sezione ricostruita — inizio
> Per questa lezione non c'è una trascrizione: l'unica fonte sono i tuoi **appunti a mano** (tre pagine). L'intera nota è quindi ricostruita. Formule, figure ed esercizi vengono dagli appunti; le spiegazioni che li collegano sono mie, scritte con lo stesso approccio del docente nelle altre lezioni, e i calcoli li ho verificati uno per uno. Dove gli appunti contengono un errore lo segnalo nel punto in cui compare.

## Esercizio 1 — Cariche e tensioni nel circuito misto

> [!example] Testo (dagli appunti)
> Ai capi di una porzione di circuito c'è una differenza di potenziale $V$. Due condensatori $C_1$ e $C_2$ in parallelo sono in serie con un terzo condensatore $C_3$. Oltre alla capacità equivalente, trovare la tensione ai capi di ciascun condensatore e la carica $q_1$ su $C_1$.

È il circuito della lezione 8, di cui avevamo già trovato la capacità equivalente:

$$
C_{12} = C_1 + C_2, \qquad
C_{\text{eq}} = \frac{C_{12}\,C_3}{C_{12} + C_3} = \frac{(C_1 + C_2)\,C_3}{C_1 + C_2 + C_3}.
$$

![[F2-L08-circuito-misto.svg]]

Ora si vuole sapere come la tensione $V$ si divide tra i condensatori. Servono due relazioni. La prima viene dalla serie: $C_{12}$ e $C_3$ sono uno dopo l'altro, quindi le loro differenze di potenziale si sommano,

$$
V = V_{12} + V_3 .
$$

La seconda è che $C_{12}$ e $C_3$ hanno la **stessa carica**, $q_{12} = q_3$. Il motivo è lo stesso visto per la serie nella lezione 8. Il tratto di filo tra $C_{12}$ e $C_3$, con le armature che vi sono collegate, è un conduttore isolato: le cariche possono spostarsi al suo interno ma non entrare né uscire. Era neutro prima che si applicasse la tensione, quindi resta neutro: la carica $-q_{12}$ di un'armatura e la carica $+q_3$ dell'altra si compensano.

Si mettono insieme le due relazioni. Da $q_{12} = C_{12}V_{12}$ e $q_3 = C_3V_3$ segue

$$
V_3 = \frac{q_3}{C_3} = \frac{q_{12}}{C_3} = \frac{C_1 + C_2}{C_3}\,V_{12} .
$$

Sostituendo in $V = V_{12} + V_3$:

$$
V = V_{12}\left(1 + \frac{C_1 + C_2}{C_3}\right) = V_{12}\,\frac{C_1 + C_2 + C_3}{C_3}
\quad\Longrightarrow\quad
V_{12} = \frac{C_3}{C_1 + C_2 + C_3}\,V,
\qquad
V_3 = \frac{C_1 + C_2}{C_1 + C_2 + C_3}\,V .
$$

$C_1$ e $C_2$ sono in parallelo, quindi hanno entrambi la tensione $V_{12}$, e le loro cariche sono

$$
q_1 = C_1V_{12} = \frac{C_1C_3}{C_1 + C_2 + C_3}\,V,
\qquad
q_2 = C_2V_{12} = \frac{C_2C_3}{C_1 + C_2 + C_3}\,V .
$$

Due osservazioni servono da controllo. Il condensatore più piccolo prende la tensione più grande: in serie la carica è la stessa, e con $V = q/C$ una capacità piccola significa una tensione grande. Inoltre $q_1 + q_2 = \dfrac{(C_1 + C_2)C_3}{C_1 + C_2 + C_3}V = C_{\text{eq}}V = q_3$. La carica che il parallelo accumula in totale è uguale a quella di $C_3$ e del condensatore equivalente, come richiede la neutralità del conduttore isolato.

> [!warning] Dati ancora mancanti
> Negli appunti il risultato è $q_1 = 3{,}1\ \mu\mathrm C$ (con $C_{\text{eq}} = 3{,}5\ \mu\mathrm F$), ma i valori di $C_1$, $C_2$, $C_3$ e $V$ non sono riportati né qui né nella lezione 8. Le formule sono corrette e dimensionalmente coerenti ($\mathrm F\cdot\mathrm F\cdot\mathrm V/\mathrm F = \mathrm C$), ma il numero non lo posso verificare.

## Esercizio 2 — Un condensatore carico collegato a uno scarico

> [!example] Testo (dagli appunti)
> Un condensatore $C_1 = 3{,}45\ \mu\mathrm F$ viene caricato con una batteria fino a una tensione $V_0 = 6{,}30\ \mathrm V$. Poi la batteria viene staccata e $C_1$ viene collegato, chiudendo un interruttore, a un condensatore scarico $C_2 = 8{,}95\ \mu\mathrm F$. Quali sono alla fine le cariche $q_1$ e $q_2$ sui due condensatori?

![[F2-L09-due-condensatori.svg]]

Prima della chiusura, solo $C_1$ è carico, con

$$
q_0 = C_1V_0 = (3{,}45\cdot10^{-6})(6{,}30)\ \mathrm C = 21{,}7\ \mu\mathrm C .
$$

Quando si chiude l'interruttore, le armature superiori dei due condensatori diventano un unico conduttore, e lo stesso vale per quelle inferiori. Le cariche si ridistribuiscono finché le due armature collegate tra loro non sono allo stesso potenziale: alla fine i condensatori sono **in parallelo**, con la stessa tensione $V_f$.

L'idea che risolve l'esercizio è la **conservazione della carica**. La batteria è stata staccata, quindi nessuna carica può entrare nel sistema o uscirne. La carica che stava su $C_1$ si divide tra i due condensatori:

$$
q_0 = q_1 + q_2, \qquad q_1 = C_1V_f, \qquad q_2 = C_2V_f .
$$

Sostituendo:

$$
C_1V_0 = (C_1 + C_2)\,V_f
\quad\Longrightarrow\quad
V_f = \frac{C_1}{C_1 + C_2}\,V_0 = \frac{3{,}45}{12{,}40}\,(6{,}30\ \mathrm V) = 1{,}75\ \mathrm V .
$$

Al denominatore compare $C_1 + C_2$, la capacità equivalente del parallelo. Le cariche finali sono

$$
q_1 = C_1V_f = \frac{C_1^2}{C_1 + C_2}\,V_0 = 6{,}05\ \mu\mathrm C,
\qquad
q_2 = C_2V_f = \frac{C_1C_2}{C_1 + C_2}\,V_0 = 15{,}7\ \mu\mathrm C .
$$

La somma, $21{,}7\ \mu\mathrm C$, ridà la carica iniziale. La tensione finale è più bassa di quella iniziale perché la stessa carica è distribuita su una capacità più grande.

> [!warning] Errore numerico negli appunti
> Negli appunti c'è $q_1 = 6{,}35\ \mu\mathrm C$. Con i dati del testo si ottiene $q_1 = (3{,}45)^2/12{,}40\cdot 6{,}30\ \mu\mathrm C = 6{,}05\ \mu\mathrm C$. Il controllo con la conservazione della carica lo conferma: $6{,}05 + 15{,}7 = 21{,}7\ \mu\mathrm C = q_0$, mentre con $6{,}35$ la somma darebbe $22{,}0\ \mu\mathrm C$. Il valore $q_2 \simeq 16\ \mu\mathrm C$ degli appunti è corretto.

## Energia immagazzinata in un condensatore

### Il lavoro per caricare un condensatore

Caricare un condensatore costa lavoro. Durante la carica, la batteria toglie elettroni a un'armatura e li porta sull'altra. Già dopo i primi trasferimenti le armature sono cariche e tra loro c'è un campo che si oppone: l'armatura negativa respinge gli elettroni che arrivano. Per aggiungere altra carica bisogna vincere questa repulsione, e più il condensatore è carico più costa.

Per calcolare il lavoro conviene ragionare per piccoli passi, come se si portasse la carica da un'armatura all'altra una porzione alla volta. Nella [[Fisica 2 - Lezione 07 - Potenziale elettrico|lezione 7]] abbiamo visto che il lavoro per spostare una carica $q$ attraverso una differenza di potenziale $V$ è $L = qV$. Qui però $V$ non è costante. Supponiamo che a un certo istante sulle armature ci siano $+q'$ e $-q'$: la differenza di potenziale è $V' = q'/C$, e per spostare un'ulteriore carica $dq'$ serve il lavoro

$$
dL = V'\,dq' = \frac{q'}{C}\,dq' .
$$

Il lavoro totale per portare il condensatore da scarico a carica $q$ si ottiene sommando, cioè integrando:

$$
L = \int_0^q \frac{q'}{C}\,dq' = \frac{1}{C}\int_0^q q'\,dq' = \frac{q^2}{2C} .
$$

![[F2-L09-lavoro-carica.svg]]

Il grafico mostra il significato geometrico del risultato. La tensione cresce linearmente con la carica, $V = q/C$. Il lavoro per un passo $dq'$ è l'area di una striscia sottile sotto la retta, e il lavoro totale è l'area del triangolo, base per altezza diviso due: $\tfrac12 qV$. Il fattore $\tfrac12$ nasce proprio dal fatto che all'inizio la carica si sposta quasi gratis, mentre alla fine bisogna vincere l'intera tensione $V$.

Il campo elettrostatico è conservativo, quindi questo lavoro non va perso: resta immagazzinato come **energia potenziale elettrica** del condensatore. Usando $q = CV$ si ottengono tre forme equivalenti:

> [!important] Energia di un condensatore
> $$
> U = \frac{q^2}{2C} = \frac12\,CV^2 = \frac12\,qV .
> $$
> Si misura in joule. Si usa la forma più comoda secondo la grandezza che resta fissa: $q^2/(2C)$ se il condensatore è isolato (carica costante), $\tfrac12 CV^2$ se è collegato a una batteria (tensione costante).

> [!example] Ordine di grandezza
> Il condensatore dell'esercizio 3 qui sotto ha $C_0 = 8{,}21\ \mathrm{pF}$ e $V_0 = 85{,}5\ \mathrm V$. Immagazzina
> $$
> U_0 = \tfrac12\,C_0V_0^2 = \tfrac12\,(8{,}21\cdot10^{-12})(85{,}5)^2\ \mathrm J = 3{,}0\cdot10^{-8}\ \mathrm J,
> $$
> trenta nanojoule: pochissimo. Poiché $U$ cresce con $C$ e con il quadrato di $V$, un condensatore da $5\ \mu\mathrm F$ caricato a $300\ \mathrm V$ immagazzina già $\tfrac12(5\cdot10^{-6})(300)^2\ \mathrm J \simeq 0{,}2\ \mathrm J$, quasi dieci milioni di volte di più.

> [!tip] Dove sta l'energia: la densità di energia del campo #approfondimento
> Per un condensatore piano si può riscrivere l'energia in termini del campo. Con $C = \varepsilon_0A/d$ e $V = Ed$:
> $$
> U = \frac12\,\frac{\varepsilon_0A}{d}\,(Ed)^2 = \frac12\,\varepsilon_0E^2\,(Ad).
> $$
> $Ad$ è il volume tra le armature, cioè proprio la regione in cui il campo è diverso da zero. L'energia per unità di volume è quindi
> $$
> u = \frac{U}{Ad} = \frac12\,\varepsilon_0E^2 .
> $$
> Il risultato vale in generale, non solo per il condensatore piano: si può pensare che l'energia elettrostatica sia immagazzinata **nel campo**, con densità $\tfrac12\varepsilon_0E^2$ in ogni punto dello spazio. Per il condensatore dell'esempio, $E_0 = 6{,}90\ \mathrm{kV/m}$ dà $u = 2{,}1\cdot10^{-4}\ \mathrm{J/m^3}$, e moltiplicando per il volume $Ad = 1{,}43\cdot10^{-4}\ \mathrm{m^3}$ si ritrovano i $3{,}0\cdot10^{-8}\ \mathrm J$.

> [!tip] Ritorno all'esercizio 2: l'energia non si conserva #approfondimento
> Nell'esercizio 2 la carica si conserva, ma l'energia no. Prima della chiusura $U_i = \tfrac12 C_1V_0^2 = 68{,}5\ \mu\mathrm J$; dopo, $U_f = \tfrac12(C_1 + C_2)V_f^2 = 19{,}0\ \mu\mathrm J$. Il rapporto è $U_f/U_i = C_1/(C_1 + C_2) = 0{,}28$: si perde più del 70% dell'energia iniziale. Non è un errore. Mentre la carica passa da un condensatore all'altro scorre una corrente nei fili, che li scalda (è l'effetto Joule, [[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]]), e una parte dell'energia viene irradiata. La perdita non dipende da quanto sono resistivi i fili: con fili migliori la corrente è più intensa e più breve, ma l'energia dissipata è la stessa.

## Dielettrici

Finora tra le armature dei condensatori c'era il vuoto. In pratica tra le armature si mette quasi sempre un materiale isolante, che in questo contesto si chiama **dielettrico**. Il dielettrico tiene separate meccanicamente le armature e, soprattutto, aumenta la capacità. Per capire perché bisogna guardare che cosa fanno le molecole del materiale in un campo elettrico.

### Molecole polari

Molte molecole sono **polari**: la loro carica, complessivamente nulla, non è distribuita in modo simmetrico, e un'estremità è leggermente positiva e l'altra leggermente negativa. Una molecola polare è quindi un piccolo dipolo elettrico con un momento di dipolo permanente $\vec p$. L'esempio tipico è l'acqua, di cui abbiamo parlato nella [[Fisica 2 - Lezione 01 - Carica elettrica e legge di Coulomb|lezione 1]].

![[F2-L09-molecole-polari.svg]]

In assenza di campo esterno, l'agitazione termica orienta le molecole in tutte le direzioni (pannello a). I momenti di dipolo si cancellano in media e il materiale, visto dall'esterno, non mostra alcun effetto elettrico.

In un campo elettrico esterno le cose cambiano. Nella [[Fisica 2 - Lezione 04 - Dipolo in campo elettrico e flusso|lezione 4]] abbiamo visto che su un dipolo in un campo uniforme agisce il momento torcente $\vec\tau = \vec p\times\vec E$, che tende a ruotare $\vec p$ parallelo a $\vec E$, la posizione di energia minima $U = -\vec p\cdot\vec E$. Le molecole si orientano quindi con l'estremità positiva nel verso del campo (pannello b). L'agitazione termica disturba l'allineamento, che in realtà non è mai perfetto, ma basta un allineamento parziale perché compaia un effetto netto. Si dice che il dielettrico si **polarizza**.

> [!tip] E le molecole non polari? #approfondimento
> Anche un materiale fatto di molecole senza momento di dipolo permanente si polarizza. Il campo esterno spinge i nuclei in un verso e le nuvole elettroniche nel verso opposto, deformando le molecole: compare un momento di dipolo **indotto**, parallelo al campo. Il meccanismo è diverso, ma il risultato è lo stesso: dipoli allineati con il campo, e tutto quello che segue vale anche per questi materiali.

### Un dielettrico nel condensatore

Mettiamo ora il dielettrico tra le armature di un condensatore carico. Il campo $\vec E_0$, che punta dall'armatura positiva a quella negativa, allinea le molecole.

![[F2-L09-dielettrico-condensatore.svg]]

All'interno del materiale l'estremità positiva di ogni molecola è affiancata dall'estremità negativa della molecola successiva, e in media le cariche si compensano. Sulle due facce del dielettrico invece non c'è compensazione. Sulla faccia rivolta verso l'armatura positiva affiorano le estremità negative delle molecole, sulla faccia rivolta verso l'armatura negativa quelle positive. Il dielettrico resta neutro nel complesso, ma sulle sue superfici compaiono due strati di carica opposta, detti **cariche di polarizzazione** (o cariche indotte).

Questi due strati formano a loro volta una specie di condensatore, con il campo diretto dalla faccia positiva a quella negativa: un campo $\vec E'$ **opposto** a $\vec E_0$. Il campo totale nel dielettrico è la somma vettoriale dei due, e il suo modulo è

$$
E = E_0 - E' < E_0 .
$$

Le conseguenze si susseguono una dall'altra. Il campo nel dielettrico è più debole, quindi è più piccola anche la differenza di potenziale tra le armature, che è l'integrale del campo. A parità di carica sulle armature, una tensione più bassa significa, per $C = q/V$, una **capacità più grande**.

> [!warning] Notazione vettoriale negli appunti
> Negli appunti c'è $\vec E_{\text{tot}} = \vec E - \vec E'$. Se $\vec E'$ indica il vettore campo delle cariche di polarizzazione, che è già opposto a $\vec E$, la somma corretta è $\vec E_{\text{tot}} = \vec E + \vec E'$. La relazione $E_{\text{tot}} = E - E'$ vale invece tra i **moduli**, ed è così che va letta.

## Il teorema di Gauss in presenza di un dielettrico

### La carica di polarizzazione

Il discorso qualitativo si rende quantitativo con il teorema di Gauss della [[Fisica 2 - Lezione 05 - Teorema di Gauss|lezione 5]]. Consideriamo un condensatore piano con armature di area $A$ e cariche $\pm q$.

![[F2-L09-gauss-dielettrico.svg]]

**Senza dielettrico** (pannello a). Si prende una superficie gaussiana a scatola che racchiude l'armatura positiva, con una faccia nel vuoto sopra l'armatura e una tra le armature. Come per il piano conduttore della [[Fisica 2 - Lezione 06 - Applicazioni del teorema di Gauss|lezione 6]], il campo fuori dal condensatore è nullo e quello tra le armature è uniforme e perpendicolare: il flusso passa solo dalla faccia interna.

$$
\varepsilon_0\Phi = q \quad\Longrightarrow\quad \varepsilon_0E_0A = q \quad\Longrightarrow\quad E_0 = \frac{q}{\varepsilon_0A}.
$$

**Con il dielettrico** (pannello b). La stessa scatola ora racchiude anche la faccia superiore del dielettrico, su cui c'è la carica di polarizzazione $-q'$. Il teorema di Gauss conta **tutte** le cariche racchiuse, quindi

$$
\varepsilon_0EA = q - q' \quad\Longrightarrow\quad E = \frac{q - q'}{\varepsilon_0A}.
$$

La carica indotta è più piccola di quella sulle armature, $|q'| < q$: il dielettrico indebolisce il campo senza annullarlo (lo annullerebbe solo un conduttore). Sperimentalmente si trova che, per ogni materiale, il campo si riduce di un fattore costante:

> [!important] Costante dielettrica
> In un dielettrico che riempie lo spazio tra le armature,
> $$
> E = \frac{E_0}{\kappa}, \qquad \kappa > 1,
> $$
> dove $\kappa$ (negli appunti $K$) è la **costante dielettrica relativa** del materiale. È un numero puro e dipende solo dal materiale: per il vuoto vale esattamente $1$, per l'aria è appena maggiore di $1$, per i materiali usati nei condensatori va da qualche unità a molto di più. Il prodotto $\varepsilon = \kappa\varepsilon_0$ si chiama **permittività** del materiale.

Confrontando le due espressioni di $E$ si ricava la carica di polarizzazione:

$$
\frac{q - q'}{\varepsilon_0A} = \frac{q}{\kappa\,\varepsilon_0A}
\quad\Longrightarrow\quad
q - q' = \frac{q}{\kappa}
\quad\Longrightarrow\quad
q' = \frac{\kappa - 1}{\kappa}\,q .
$$

I casi limite tornano. Per $\kappa = 1$ (vuoto) $q' = 0$: non c'è polarizzazione. Per $\kappa\to\infty$, $q'\to q$: la carica indotta compensa completamente quella dell'armatura e il campo si annulla, come dentro un conduttore.

### Il teorema di Gauss con le sole cariche libere

L'espressione $\varepsilon_0\oint\vec E\cdot d\vec A = q - q'$ è corretta ma scomoda, perché $q'$ non è nota in anticipo: dipende dal campo che si sta cercando. Conviene riscriverla in modo che compaia solo $q$. Dal risultato precedente $q - q' = q/\kappa$, quindi

$$
\varepsilon_0\oint\vec E\cdot d\vec A = \frac{q}{\kappa}
\quad\Longrightarrow\quad
\varepsilon_0\oint\kappa\,\vec E\cdot d\vec A = q .
$$

> [!important] Teorema di Gauss nei dielettrici
> $$
> \varepsilon_0\oint\kappa\,\vec E\cdot d\vec A = q_{\text{lib}} .
> $$
> A destra compare solo la **carica libera** $q_{\text{lib}}$ racchiusa dalla superficie, cioè la carica che si può spostare e controllare, come quella portata sulle armature dalla batteria. Le cariche di polarizzazione, legate alle molecole del dielettrico, non compaiono più esplicitamente: il loro effetto è tutto contenuto nel fattore $\kappa$ dentro l'integrale.

È la generalizzazione del teorema della lezione 5: nel vuoto $\kappa = 1$ e si ritrova la forma usuale. La distinzione tra i due tipi di carica è importante. Le **cariche libere** sono quelle dei conduttori, che si muovono liberamente. Le **cariche di polarizzazione** (o legate) appartengono alle molecole e possono solo spostarsi di poco attorno alla loro posizione.

### Lo spostamento elettrico

La quantità sotto l'integrale merita un nome. Si definisce il vettore **spostamento elettrico**

$$
\vec D = \varepsilon_0\kappa\,\vec E = \varepsilon\,\vec E,
\qquad
\oint\vec D\cdot d\vec A = q_{\text{lib}} .
$$

Il flusso di $\vec D$ attraverso una superficie chiusa dipende solo dalle cariche libere racchiuse. $\vec D$ si misura in $\mathrm{C/m^2}$, come una densità superficiale di carica: tra le armature del condensatore piano vale proprio $D = \sigma = q/A$, con o senza dielettrico.

> [!warning] Definizione di $\vec D$ negli appunti
> Negli appunti lo spostamento elettrico è definito come $\vec D = K\vec E$, e il teorema è scritto $\varepsilon_0\oint\vec D\cdot d\vec A = q$. L'equazione è la stessa, ma la definizione standard nel Sistema Internazionale include $\varepsilon_0$: $\vec D = \varepsilon_0\kappa\vec E$, così che $\oint\vec D\cdot d\vec A = q_{\text{lib}}$ senza fattori davanti. È questa la forma che troverai sui libri. La differenza conta quando si danno valori numerici di $D$: con la definizione standard $D$ ha le unità di $\mathrm{C/m^2}$, con quella degli appunti di $\mathrm{V/m}$.

### La capacità aumenta di un fattore $\kappa$

Si può ora rendere quantitativa la conclusione qualitativa di prima. Con il dielettrico che riempie tutto lo spazio tra le armature, a parità di carica $q$ il campo è $E = E_0/\kappa$, quindi la tensione è $V = Ed = V_0/\kappa$ e la capacità è

$$
C = \frac{q}{V} = \kappa\,\frac{q}{V_0} = \kappa\,C_0,
\qquad
C = \kappa\,\frac{\varepsilon_0A}{d} \ \ \text{(condensatore piano)}.
$$

La capacità di un condensatore riempito di dielettrico si ottiene da quella nel vuoto sostituendo $\varepsilon_0$ con $\varepsilon = \kappa\varepsilon_0$. Lo stesso vale per i condensatori sferico e cilindrico della lezione 8.

> [!tip] Batteria staccata o collegata #approfondimento
> Il ragionamento sopra vale a **carica costante**, cioè con la batteria staccata prima di inserire il dielettrico: la tensione scende da $V_0$ a $V_0/\kappa$. Se invece la batteria resta collegata, è la **tensione** a restare fissa, e la batteria fornisce altra carica finché $q = CV_0 = \kappa q_0$. In entrambi i casi $C = \kappa C_0$, perché la capacità dipende solo dalla geometria e dal materiale. Cambia l'energia: a carica costante $U = q^2/(2C)$ scende di un fattore $\kappa$, a tensione costante $U = \tfrac12CV^2$ sale di un fattore $\kappa$.

## Esercizio 3 — Condensatore piano con una lastra dielettrica

> [!example] Testo (dagli appunti)
> Un condensatore piano ha armature di area $A = 115\ \mathrm{cm^2}$ a distanza $d = 1{,}24\ \mathrm{cm}$. Viene caricato da una batteria alla tensione $V_0 = 85{,}5\ \mathrm V$. Tra le armature si inserisce poi una lastra di dielettrico di spessore $b = 0{,}78\ \mathrm{cm}$ e costante dielettrica $\kappa = 2{,}61$, parallela alle armature. Calcolare: (1) la capacità $C_0$ prima del dielettrico; (2) la carica $q_0$; (3) il campo $E_0$ tra le armature senza dielettrico; (4) il campo $E_1$ dentro il dielettrico.

![[F2-L09-lastra-dielettrica.svg]]

> [!warning] Ipotesi implicita
> Gli appunti non dicono esplicitamente se la batteria viene staccata prima di inserire la lastra. Il calcolo del punto 4, in cui la carica libera resta $q_0$, presuppone che lo sia: la carica sulle armature resta quella iniziale.

**(1) Capacità senza dielettrico.** È un condensatore piano:

$$
C_0 = \varepsilon_0\,\frac{A}{d} = (8{,}85\cdot10^{-12})\,\frac{115\cdot10^{-4}}{1{,}24\cdot10^{-2}}\ \mathrm F = 8{,}21\cdot10^{-12}\ \mathrm F = 8{,}21\ \mathrm{pF}.
$$

> [!warning] Unità negli appunti
> Negli appunti c'è $C_0 = 8{,}21\ \mu\mathrm F$, ma il valore corretto è $8{,}21\ \mathrm{pF}$ ($10^{-12}$ F, non $10^{-6}$). La carica del punto 2 negli appunti, $702\ \mathrm{pC}$, è coerente con i picofarad: $8{,}21\ \mathrm{pF}\cdot85{,}5\ \mathrm V = 702\ \mathrm{pC}$. Con i microfarad verrebbe $702\ \mu\mathrm C$, un milione di volte di più. È anche un buon ordine di grandezza da ricordare: armature di una decina di centimetri di lato a un centimetro di distanza danno qualche picofarad.

**(2) Carica.**

$$
q_0 = C_0V_0 = (8{,}21\cdot10^{-12})(85{,}5)\ \mathrm C = 7{,}02\cdot10^{-10}\ \mathrm C = 702\ \mathrm{pC}.
$$

**(3) Campo senza dielettrico.** Con il teorema di Gauss su una scatola che racchiude un'armatura, come sopra:

$$
\varepsilon_0E_0A = q_0 \quad\Longrightarrow\quad
E_0 = \frac{q_0}{\varepsilon_0A} = \frac{7{,}02\cdot10^{-10}}{(8{,}85\cdot10^{-12})(115\cdot10^{-4})}\ \mathrm{V/m} = 6{,}90\ \mathrm{kV/m}.
$$

Il controllo è immediato: in un condensatore piano il campo è uniforme, quindi $E_0 = V_0/d = 85{,}5/0{,}0124\ \mathrm{V/m} = 6{,}90\ \mathrm{kV/m}$.

**(4) Campo nel dielettrico.** Si usa il teorema di Gauss nella forma con le sole cariche libere. Negli appunti la superficie gaussiana racchiude l'**armatura negativa** e la faccia inferiore della lastra: una faccia della scatola sta dentro il dielettrico, l'altra sotto l'armatura, dove il campo è nullo. La carica libera racchiusa è quella dell'armatura, $q_{\text{lib}} = -q_0$; la carica di polarizzazione della faccia inferiore della lastra non va contata, perché è già nel fattore $\kappa$. Sulla faccia dentro il dielettrico il vettore $d\vec A$ uscente punta verso l'alto, mentre il campo punta verso il basso, quindi $\vec E\cdot d\vec A = -E\,dA$:

$$
\varepsilon_0\oint\kappa\,\vec E\cdot d\vec A = q_{\text{lib}}
\quad\Longrightarrow\quad
-\varepsilon_0\kappa E_1A = -q_0
\quad\Longrightarrow\quad
E_1 = \frac{q_0}{\kappa\varepsilon_0A} = \frac{E_0}{\kappa} = \frac{6{,}90}{2{,}61}\ \mathrm{kV/m} = 2{,}64\ \mathrm{kV/m}.
$$

I segni si compensano, come devono: il risultato non dipende da quale armatura si sceglie. Negli spazi vuoti tra la lastra e le armature il campo resta $E_0$. La superficie gaussiana che racchiude un'armatura e una faccia del vuoto adiacente contiene la stessa carica libera, e le cariche di polarizzazione della lastra, uguali e opposte, non cambiano il campo fuori dalla lastra.

L'esercizio prosegue nella [[Fisica 2 - Lezione 10 - Corrente elettrica, resistenza e legge di Ohm|lezione 10]] con la differenza di potenziale e la capacità con il dielettrico inserito.

> [!warning] Sezione ricostruita — fine
