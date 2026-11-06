---
corso: Robotica MOD2
lezione: 7
data: 2026-11-03
docente: Antonio Sgorbissa
tipo: laboratorio
argomenti: [visita al laboratorio, interazione uomo-robot, pianificazione PDDL, modelli linguistici, robotica sociale, emozioni, droni, visual servoing, pianificazione di percorsi, robot quadrupedi, poligono di supporto, stima dello stato, IMU, LIDAR, camera di profondità, pianificazione globale e locale, Spot]
fonti: [trascrizione L7 (laboratorio)]
tags: [robotica-mod2, lezione, laboratorio]
---

# Lezione 7 — Visita al laboratorio RICE

Questa lezione si è svolta nel laboratorio del docente, il **RICE Lab** del DIBRIS (*Robots and Intelligent systems for Citizens and the Environment*). Non è stata una lezione frontale: gli studenti, divisi in sette gruppi, hanno ruotato fra stazioni in cui dottorandi e assegnisti presentavano i propri robot e progetti. Molti concetti visti a lezione (odometria, stima dello stato, pianificazione globale e locale, sensori) sono comparsi in contesti applicativi reali. Queste note riportano il contenuto delle stazioni registrate e lo collegano agli argomenti del corso.

---

## 1. Organizzazione della visita

Le stazioni erano sette, numerate in senso antiorario a partire da quella subito a destra dell'ingresso. Ogni gruppo partiva dalla stazione con il proprio numero e, ogni 12 minuti circa, passava alla successiva. Ogni studente avrebbe visto tre stazioni.

La visita era anche un gioco a squadre con due componenti.

- **Le domande.** Chi presentava assegnava un punteggio alle domande del gruppo, in base a quanto erano numerose e pertinenti.
- **Le parole chiave.** Ogni presentatore pronunciava fino a **dieci parole chiave** legate alla robotica, le stesse per tutte le stazioni. Ascoltando e facendo "l'intersezione" fra ciò che dicevano tutti, ogni gruppo doveva individuarle. Alcune erano legate agli argomenti del corso, altre più avanzate. L'elenco andava inviato per email entro la sera.

La squadra vincitrice avrebbe ricevuto le magliette del laboratorio. La trascrizione non riporta l'elenco ufficiale delle parole chiave.

> [!tip] Un esercizio per il ripasso
> Ricostruire l'elenco delle parole chiave è un buon esercizio anche a posteriori. Fra i termini che ricorrono in più stazioni compaiono, per esempio, *pianificazione*, *percezione*, *navigazione autonoma*, *localizzazione*, *stima dello stato*, *architettura*, *sensori*, *modello cinematico/dinamico*, *autonomia*. Si tratta però di una ricostruzione dalla trascrizione, non dell'elenco ufficiale.

---

## 2. Robotica sociale e interazione uomo-robot

Tre stazioni riguardavano l'**interazione uomo-robot** (HRI, *Human-Robot Interaction*): robot progettati non per spostare oggetti o ispezionare impianti, ma per interagire con le persone, come anticipato nella [[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]] (§4.15).

### 2.1 Pepper: pianificazione e modelli linguistici

**Pepper** è un umanoide su base mobile. L'obiettivo del progetto presentato è un robot **adattivo**, capace di interagire autonomamente con le persone, per ora soprattutto bambini, e di adattare il proprio comportamento a ciò che fanno.

L'architettura combina due strumenti, con una divisione dei compiti precisa:

> [!important] Cosa, quando, come
> - **Che cosa** fare lo decidono i ricercatori insieme a psicologi ed educatori.
> - **Quando** farlo lo decide un **pianificatore automatico** basato su **PDDL**.
> - **Come** farlo, cioè le frasi concrete, lo genera un **modello linguistico di grandi dimensioni** (LLM).

La **pianificazione**, in questo contesto, è definita così: dati dei **predicati**, cioè "aggettivi" che descrivono lo stato del mondo, e l'insieme delle **azioni** possibili, il pianificatore produce la lista di azioni da eseguire per raggiungere un obiettivo. È lo stesso tipo di pianificazione simbolica nato con Shakey e il linguaggio STRIPS ([[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]], §4.3), ben diverso dalla pianificazione di percorsi geometrici delle lezioni 3 e 4. In PDDL ogni azione è definita da **precondizioni** ed **effetti**.

Nella dimostrazione il bambino svolge un compito **visuo-spaziale**, cioè un compito di ragionamento su forme e posizioni. Compiti di questo tipo si usano nella valutazione cognitiva, anche per diagnosi come l'ADHD o l'autismo. Il gruppo lo usa perché non richiede di saper leggere ed è adatto a bambini di età diverse, non per assegnare un punteggio di intelligenza. Lo scopo è capire se il robot riesce a sostenere la **motivazione** del bambino. Durante il compito il robot ascolta ciò che il bambino dice e stima il suo stato tramite i predicati mostrati su una griglia. Nei primi esperimenti molti bambini si concentravano sul compito e ignoravano il robot: per questo un comportamento **proattivo**, che richiama l'attenzione, aiuta l'interazione.

Alcuni dettagli tecnici emersi dalle domande:

- sul robot gira solo il *client*; le chiamate all'LLM avvengono tramite una **REST API** verso un server del laboratorio, con una chiamata per generare la frase e una per ciascun predicato, eseguite in parallelo. I movimenti sono invece gestiti in locale;
- i movimenti "umani", come la gesticolazione, sono quelli di fabbrica (*autonomous life*);
- Pepper ha **bumper** solo alla base, sulle tre ruote. Non ha sensori sulle braccia: i sensori sono sulla testa e sulle mani;
- le telecamere negli occhi servono anche alla navigazione e al **riconoscimento dei volti**: il robot riconosce che c'è una faccia ("un ovale con due cerchietti") e la guarda mentre parla, ma non sa ancora distinguere *chi* è chi.

L'idea per il futuro è integrare altri canali sensoriali (tatto, vista, dinamica del robot) oltre al solo dialogo.

### 2.2 Emozioni nella pianificazione

Una seconda stazione riguardava l'integrazione delle **emozioni** nella pianificazione del robot. La motivazione è che noi esseri umani decidiamo che cosa fare anche in base alle nostre emozioni e a quelle dell'interlocutore. Per rendere l'interazione più naturale si vuole che il robot faccia lo stesso.

Il sistema ha tre parti.

1. **Percezione.** La telecamera osserva le espressioni facciali e il parlato viene analizzato; da entrambi si stima un'emozione. L'analisi del testo (*sentiment analysis*) è affidata a un LLM con prompt rigidi, in modo da ottenere sempre etichette di un insieme prefissato.
2. **Decisione con una funzione di costo.** L'emozione non è facile da definire, ma "siamo ingegneri e ci piacciono i numeri": a ogni emozione si associano delle **coordinate**, così che le distanze fra stati emotivi siano ben definite. Una **funzione di costo** sceglie poi che cosa fare, per esempio consolare il bambino.
3. **Ripianificazione incrementale.** Normalmente, quando un piano fallisce, si ripianifica da zero. Qui invece il sistema aggiorna lo stato e **ripianifica dal punto esatto** in cui si trova, così l'interazione continua senza ricominciare.

Il codice è in Python, la pianificazione in PDDL. Nell'applicazione dimostrativa il robot, con un volto su schermo e un microfono direzionale, fa domande e dà consigli a bambini delle elementari. Lo schermo non è *touch* per scelta progettuale: un robot sociale non dovrebbe insegnare ai bambini che toccare la faccia di qualcuno va bene.

### 2.3 Navel: un robot per l'assistenza domiciliare

La terza stazione riguardava **Navel**, un robot sociale di un'azienda tedesca, usato in un progetto di dottorato sulla generazione di **risposte emotive coerenti** tramite **architetture cognitive**. In letteratura, robot capaci di esprimere emozioni migliorano l'interazione: il legame con l'utente, la fiducia, la prevedibilità e la comprensibilità del comportamento.

Il punto di partenza è un modello psicologico delle emozioni umane, adattato a un'architettura cognitiva. Il modello citato sostiene che le emozioni nascono dall'interazione. Il primo passo è quindi **percepire**:

- l'**emozione** dell'utente, dalle espressioni (telecamera) e dal contenuto del dialogo (microfono), perché spesso le emozioni passano più per ciò che si dice che per il volto. Le due fonti vanno **fuse**;
- la sua **distanza** dal robot;
- il suo livello di **attenzione**, cioè se sta guardando il robot oppure no.

> [!warning] Nome del modello incerto
> La trascrizione riporta "Fat Control Theory". Si tratta quasi certamente della **Affect Control Theory**, una teoria sociologica delle emozioni nell'interazione sviluppata da D. R. Heise e collaboratori. Il nome va verificato.

L'applicazione è l'assistenza in casa a persone con **malattie neurodegenerative**, per alleggerire il carico dei *caregiver*. Il robot può ripetere le cose molte volte senza stancarsi, ricordare informazioni, mostrare risposte empatiche e stimolare la conversazione quando la persona è sola. Dagli incontri con caregiver e medici sono emerse due richieste.

- **Memoria e promemoria.** Il robot conserva informazioni e le richiama in modo **proattivo**, propone argomenti scelti dai caregiver tramite un'interfaccia e pronuncia frasi prestabilite in certi momenti della giornata.
- **Muoversi in casa.** È un limite tipico dei robot sociali: non hanno buone capacità di navigazione e localizzazione.

> [!example] Il collegamento con il corso: un robot senza localizzazione
> Questi robot si muovono con comandi del tipo "vai avanti di tanti metri, gira di tanti gradi". Non hanno algoritmi di localizzazione, e l'esecuzione è inaffidabile: comandato di girare di 90°, il robot può girare di 20°, e non c'è modo di sapere quanto ha girato davvero. È l'odometria ad **anello aperto** della [[Lezione 02 - Cinematica inversa e odometria|Lezione 2]] (§6.2) nella sua forma peggiore. L'unico rimedio citato è mettere dei **marker** in casa, con cui il robot capisce di essere arrivato in un certo posto: è la localizzazione assoluta con marker della [[Lezione 06 - Localizzazione, riferimenti esterni e filtro di Kalman|Lezione 6]]. Anche questa soluzione però è stata giudicata poco robusta per un robot lasciato da solo in casa di una persona fragile.

Un dettaglio pratico mostra quanto conti l'ingegneria dell'interazione. Il robot ha sette microfoni attorno al volto, ma il gruppo ne usa uno **esterno con un pulsante**. Il robot capisce che la persona ha finito di parlare quando rileva un **silenzio** di qualche secondo. In un ambiente rumoroso il silenzio non arriva mai, e il robot continuerebbe ad ascoltare e trascrivere. Il pulsante permette di "staccare" l'ascolto in modo intuitivo, e soddisfa anche la richiesta di poter far smettere di ascoltare il robot. Il sistema è stato usato anche con bambini nello spettro autistico e in classe, per attività di comprensione socio-emotiva.

Un altro episodio del primo studio pilota: un parametro del modello di dialogo era rimasto a valori vecchi, e il robot rispondeva in modo "scontroso". È un esempio di come, con persone fragili, anche un errore di configurazione abbia conseguenze reali.

---

## 3. Droni per l'ispezione di impianti fotovoltaici

Questa stazione presentava il lavoro su un progetto europeo per il monitoraggio e l'ispezione di **pannelli solari** (il nome del progetto, in trascrizione, è "Solaris"). Il compito del gruppo è **pianificare il percorso** ottimo del drone e **controllarlo** dentro l'impianto.

### 3.1 Dalla mappa alla navigazione

1. Si acquisisce un'immagine satellitare dell'impianto (da Google Earth).
2. La si **georeferenzia**: a ogni pixel si associa una coordinata nel mondo reale.
3. Si naviga in **due fasi**:
   - fra una fila di pannelli e la successiva, il drone raggiunge una coordinata nota usando il **GPS**;
   - **sopra una fila**, il GPS non si usa più, perché ha un errore che fluttua nel tempo. Si usa invece il **visual servoing**.

> [!important] Visual servoing
> Il **visual servoing** consiste nel basare il controllo del moto direttamente sul **feedback visivo** della telecamera. Qui l'immagine viene **segmentata** per ottenere una maschera del pannello rispetto al terreno, se ne calcola la **linea di mezzeria**, e il drone viene controllato per mantenere quella linea **al centro** dell'immagine e il più possibile **orizzontale**, controllando quindi anche l'orientamento. Il riferimento non è una coordinata assoluta incerta, ma l'oggetto stesso da seguire.

La logica è la stessa della [[Lezione 06 - Localizzazione, riferimenti esterni e filtro di Kalman|Lezione 6]]: quando un riferimento esterno affidabile è disponibile, ci si aggancia a quello invece che a una stima che deriva.

Durante l'ispezione si cercano due tipi di difetti delle celle: le **crepe** (*crack*), vere scheggiature del vetro, e gli **hotspot**, celle che non convertono più energia e si **surriscaldano**. Gli hotspot si individuano con una **telecamera termica**. Secondo i partner del progetto, un buon compromesso fra velocità e qualità delle immagini è un volo a circa 3 m/s.

### 3.2 Pianificare il percorso con una matrice dei costi

A ciascuna estremità di ogni fila di pannelli si associa un **waypoint**. Si costruisce una **matrice dei costi** fra tutte le coppie di waypoint, per esempio le distanze. Un ottimizzatore cerca poi l'ordine di visita più economico.

> [!example] Il trucco del costo nullo
> Se i costi fossero solo distanze, l'ottimizzatore potrebbe preferire saltare da una fila alla vicina invece di percorrere la fila intera, perché le file adiacenti sono più vicine dei due estremi della stessa fila. Ma l'obiettivo è **ispezionare** i pannelli, quindi ogni fila va percorsa da un estremo all'altro. La soluzione è assegnare **costo zero** all'arco fra i due waypoint della **stessa** fila. Così l'ottimizzatore percorre sempre la fila e poi passa alla successiva.

È un esempio istruttivo di come la scelta del **costo** degli archi di un grafo determini il comportamento del pianificatore, come visto per A\* nella [[Lezione 04 - Garanzie, RRT, algoritmi Bug e campi di potenziale|Lezione 4]]: "ottimo" significa sempre ottimo rispetto al costo dichiarato. La pianificazione si fa una volta per impianto.

### 3.3 Vincoli pratici e flotte

- **Normative.** Per non richiedere autorizzazioni aggiuntive, il drone deve volare in modalità **VLOS** (*Visual Line Of Sight*): l'operatore deve sempre vederlo. Esistono categorie e patentini diversi a seconda del peso.
- **Batteria.** È il limite più grosso: circa **20 minuti** di autonomia. Per questo il gruppo lavora al coordinamento di una **flotta multi-drone**. Il percorso ottimo viene suddiviso in *cluster* (sotto-percorsi), uno per drone. Con due droni il tempo si riduce circa della metà, anche se non in modo esattamente lineare.
- **Precedenze.** Quando due droni devono incrociarsi, uno mantiene la quota e l'altro si alza, lascia passare e poi riscende. La priorità dipende dal rapporto fra **batteria residua e percorso ancora da fare**: ha priorità il drone con il rapporto più basso, cioè quello con meno batteria rispetto a ciò che gli resta da volare. A parità di rapporto decide l'identificativo del drone.
- **Software.** Il drone è commerciale e il produttore fornisce un SDK (Android) che permette di ricevere immagini, posizioni e velocità e di dare comandi ad alto livello. Non permette di modificare il **controllo di basso livello** (quanto far girare ciascuna elica), ma per un lavoro di pianificazione e controllo ad alto livello non serve. Il calcolo per ora gira su un computer a terra.

---

## 4. Robot quadrupedi: controllo basato su modello

### 4.1 Perché le gambe

I quadrupedi hanno le gambe perché sono **agili**: affrontano scale, gradini, buchi nel terreno, persone ferite a terra. Le gambe permettono anche di **interagire** con il mondo, come fa un cane che apre una porta con la zampa o sposta un oggetto. È la ricerca sulla *loco-manipolazione*. Nella navigazione autonoma classica una porta chiusa è percepita come un muro, e il robot non va oltre. Ma in una missione di ricerca e soccorso, dietro quella porta potrebbe esserci qualcuno.

### 4.2 Gradi di libertà e controllo gerarchico

Il robot presentato ha **18 gradi di libertà**:

- **6** della **base**, cioè la posizione $(x, y, z)$ e l'orientamento attorno ai tre assi. Questi gradi di libertà **non sono attuati** direttamente: la base si muove solo grazie alle forze che le gambe scambiano con il terreno. Per questo si parla di robot **sottoattuato** (*underactuated*);
- **12** dei **giunti**, tre per gamba, tutti attuati da motori elettrici. Il comando finale inviato ai motori è una **coppia**.

L'approccio è **basato su modello**: un modello **cinematico** (posizioni e velocità) e un modello **dinamico** (forze). I piedi sono sfere, quindi i contatti con il terreno sono puntiformi: in ciascun punto la forza di reazione del terreno compensa la gravità e permette di muoversi. Nell'interazione con gli oggetti il problema diventa *dove* toccare l'oggetto e con quale forza.

Il controllo è organizzato su **tre livelli**:

1. **Predizione e ottimizzazione.** Con un modello semplificato, abbastanza veloce da risolvere il problema in tempo, si predice la dinamica del robot nell'arco di circa **un secondo**, ottimizzando una funzione di costo con dei vincoli. Gli obiettivi sono camminare, stare in equilibrio, interagire con un oggetto. È lo schema del *controllo predittivo*.
2. **Inseguimento dei task.** La soluzione ottima viene inseguita da una serie di *task* (stare in una certa posizione, bilanciare una certa forza) definiti sulla dinamica completa. Il risultato sono le **forze di reazione desiderate** e le **posizioni e velocità desiderate dei giunti**.
3. **Controllo dei giunti a 1 kHz.** Un controllo **proporzionale-derivativo** (PD) sull'errore di posizione dei giunti, più una **coppia in anticipo** (*feedforward*) calcolata dal livello superiore. L'alta frequenza serve a reagire e a compensare ciò che il modello non considera: attriti dei giunti, disturbi, differenze rispetto al modello.

La struttura ricorda l'architettura ibrida della [[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]] (§4.6): livelli diversi lavorano a scale di tempo diverse, dal secondo al millisecondo.

### 4.3 Stabilità: il poligono di supporto

Uno studente chiede come fa il robot a non cadere mentre cammina, visto che il busto oscilla. La risposta richiama il criterio del **poligono di supporto**.

> [!important] Poligono di supporto
> I punti di contatto dei piedi con il terreno definiscono un **poligono**. Se la **proiezione del centro di massa** sul terreno cade **dentro** il poligono, le forze di reazione riescono a bilanciare il robot. Se esce dal poligono, la gravità genera una coppia che fa ruotare il robot, e il robot cade.

> [!tip] Approfondimento #approfondimento
> Il criterio, nella sua forma statica, risale agli studi sull'andatura dei quadrupedi di R. B. McGhee e A. A. Frank, *On the stability properties of quadruped creeping gaits* (Mathematical Biosciences, 1968) [@mcghee1968]. Vale per moti lenti, in cui le forze d'inerzia sono trascurabili. Per andature dinamiche, come il trotto o la corsa, il centro di massa può uscire temporaneamente dal poligono, e servono criteri più generali basati sulle forze di contatto, come quelli usati dal controllo predittivo descritto sopra.

### 4.4 Sensori e stima dello stato

Il controllo ha bisogno di un **feedback**, cioè di una misura. Se una grandezza non si può misurare, la si deve **stimare**. I sensori principali sono:

- l'**IMU** (*Inertial Measurement Unit*), "senza la quale non si va da nessuna parte". È un pacchetto di sensori che restituisce l'**accelerazione lineare** (compresa quella di gravità), la **velocità angolare** e l'**orientamento**. Di solito è posta molto vicino al centro della base;
- gli **encoder dei giunti**, che danno posizione e velocità di ciascun giunto;
- le **stereocamere**, che come i nostri due occhi forniscono due immagini con una **disparità**, da cui si ricava la **profondità**. Servono a sapere *dove* si trova un ostacolo per evitarlo, ma anche alla localizzazione: riconoscendo punti di riferimento nell'immagine e osservando come si spostano, si stima lo spostamento del robot (**odometria visiva**);
- **sensori a ultrasuoni**, come i sensori di parcheggio delle auto. Non riconoscono l'ostacolo, ma misurano la distanza: se il robot va a 3 m/s e il muro è a un centimetro, si ferma in tempo.

> [!example] Il collegamento con il corso: odometria con le gambe
> La **stima dello stato** del quadrupede è una versione più ricca di ciò che si è visto per i robot su ruote ([[Lezione 06 - Localizzazione, riferimenti esterni e filtro di Kalman|Lezione 6]]). Se un piede è a contatto con il terreno, quel punto è **fermo**. Se i giunti si muovono, tramite il modello cinematico si calcola come si è spostata la base: è l'equivalente dell'odometria con gli encoder delle ruote. Questo spostamento viene **fuso** con l'accelerazione dell'IMU integrata (velocità, poi posizione) e con l'odometria visiva, per ottenere una stima del tipo "il robot è in $x = 1$, $y = 0$". Senza questa stima non si potrebbe nemmeno controllare la velocità: per comandare al robot di andare a una certa velocità serve sapere a che velocità sta andando.

**Applicazioni.** Robot come **Spot** di Boston Dynamics vengono venduti alle aziende per l'ispezione autonoma di impianti, per esempio un impianto siderurgico: il robot fa il giro con telecamere ad alta risoluzione e, con algoritmi di apprendimento automatico, legge i manometri e segnala le anomalie. Nel laboratorio si lavora anche a missioni di **ricerca e soccorso** con Spot: navigazione autonoma per esplorare un edificio, costruire una mappa e trovare persone.

---

## 5. Un robot su ruote: sensori, mappe e navigazione

Questa stazione, presentata in inglese e tradotta in modo frammentario dalla trascrizione, riprendeva molti concetti del corso su un piccolo robot a quattro ruote (in trascrizione "robot rosso"/"Rosebolt", probabilmente un **ROSbot**).

### 5.1 Modelli cinematici

Per un'automobile il modello semplificato è quello a **bicicletta** ([[Lezione 02 - Cinematica inversa e odometria|Lezione 2]], §7). Il robot presentato ha invece quattro ruote e gira usando la **differenza di velocità** fra i due lati, quindi si può approssimare con il modello **uniciclo** della guida differenziale ([[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]], §5.4).

### 5.2 Sensori: LIDAR 2D e camera di profondità

- Il **LIDAR** (in trascrizione "radar") misura la distanza punto per punto. Ruotando, scandisce tutto attorno al robot e fornisce le distanze in un piano. Con queste informazioni il robot può costruire una **mappa 2D** e localizzarsi su di essa.
- La **camera di profondità** (RGB-D) fornisce per ogni pixel di un'immagine la distanza del punto corrispondente: non più un punto per direzione, ma un'intera immagine di distanze. Permette di costruire un **modello 3D** dell'ambiente e di localizzarsi in 3D.

> [!warning] Il limite del LIDAR planare
> Un LIDAR 2D vede solo ciò che interseca il **suo piano** di scansione. Un oggetto più basso, per esempio una borsa a terra, o più alto, come il piano di un tavolo, non compare nella mappa. Per questo si affiancano sensori 3D, come le camere di profondità, o LIDAR con più piani di scansione, presenti sui robot più costosi. È un limite da aggiungere a quello già visto per i vetri ([[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]], §4.10).

### 5.3 Pianificazione globale e locale

La domanda posta ai gruppi era: il robot ha una mappa e un obiettivo, la traiettoria pianificata è una linea retta; che cosa succede se si mette un ostacolo in mezzo? Cambia la mappa? La risposta è **sì**: la mappa si aggiorna in tempo reale con ciò che i sensori percepiscono.

Il presentatore ha poi riassunto la distinzione delle lezioni 3 e 4. Il **pianificatore globale** genera la traiettoria verso l'obiettivo. Durante il moto però possono capitare molti imprevisti: errori dei sensori, ostacoli nuovi, una traiettoria che non va più bene. La strategia è spezzare la traiettoria lunga in **segmenti molto corti**, seguiti uno alla volta dal **pianificatore locale**. I due livelli si combinano sempre per portare il robot alla meta in sicurezza ([[Lezione 04 - Garanzie, RRT, algoritmi Bug e campi di potenziale|Lezione 4]], §9.3).

### 5.4 Riconoscimento di attività con modelli visione-linguaggio

A fine presentazione è stato mostrato un video, girato con Spot, di un sistema che riconosce le **attività** delle persone (bere, usare un oggetto). Il punto più interessante è che il sistema riconosce anche attività **mai viste in addestramento**, come giocare a basket o aprire la porta d'ingresso, descritte solo con **frasi** in linguaggio naturale. Il modello usato è indicato in trascrizione come "Flip": si tratta quasi certamente di **CLIP**. Il modello trasforma sia le immagini sia le frasi in **vettori** dello stesso spazio, e un'immagine viene associata alla frase il cui vettore è più vicino. È la risposta al problema del **vocabolario chiuso** dei rilevatori tradizionali, discusso nella [[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]] (§4.12): non serve conoscere in anticipo la classe di un oggetto, basta saperlo descrivere.

> [!tip] Approfondimento #approfondimento
> CLIP è stato presentato da A. Radford e collaboratori (OpenAI) in *Learning Transferable Visual Models From Natural Language Supervision* (ICML 2021) [@radford2021]. Il modello è addestrato su centinaia di milioni di coppie immagine-testo raccolte dal web, in modo che le immagini e le rispettive didascalie abbiano vettori vicini. Questo permette la classificazione *zero-shot*: per riconoscere una categoria nuova basta scriverne una descrizione testuale.

---

## 6. Spot

L'ultima stazione presentava da vicino **Spot**, il quadrupede di Boston Dynamics già citato nella [[Lezione 01 - Robot autonomi e cinematica differenziale|Lezione 1]] (§4.13).

- **Comando.** Si guida con un **tablet**, che mostra il feedback visivo delle telecamere. Si può passare dalla posizione in piedi alla camminata e scegliere la vista.
- **Sensori di serie.** **Cinque telecamere** attorno al corpo (davanti, ai lati e dietro), usate anche per evitare gli ostacoli: se lo si guida contro una persona o un oggetto, il robot si ferma.
- **Carichi aggiuntivi.** Sul dorso si montano altri moduli: un **LIDAR**, una camera **RGB-D** di qualità superiore a quelle integrate, una camera termica o un sensore di radioattività, una scheda di calcolo con **GPU** (una Jetson) per applicazioni avanzate, e un modulo **4G** con SIM per controllare il robot da remoto. Il calcolo aggiuntivo va montato all'esterno perché il produttore non permette di modificare il computer interno.
- **Ritorno autonomo.** Il robot può tornare autonomamente alla posizione di partenza ripercorrendo il tragitto fatto.
- **Mappe.** Con il LIDAR si costruisce una mappa densa e precisa. In un ambiente interno basta spesso una mappa **2D**, in cui le pareti appaiono come punti più scuri. All'aperto, su terreni inclinati, conviene una mappa **3D** che registri anche l'altezza di ogni punto.

---

## Riepilogo della lezione

- Il laboratorio RICE lavora su robotica sociale, droni, quadrupedi e navigazione autonoma. La visita ha mostrato in contesti reali molti concetti del corso.
- **Robotica sociale.** Si combinano **pianificazione simbolica** (PDDL: predicati, azioni con precondizioni ed effetti) e **modelli linguistici**: le persone decidono *che cosa*, il pianificatore *quando*, l'LLM *come*. La percezione delle emozioni fonde volto e dialogo. I robot sociali hanno capacità di localizzazione scarse e si muovono di fatto in anello aperto.
- **Droni.** GPS per spostarsi fra le file di pannelli, **visual servoing** sopra di esse. Pianificazione con una matrice dei costi in cui il costo nullo fra gli estremi di una fila impone di percorrerla. Batteria limitata, flotte e regole di precedenza.
- **Quadrupedi.** 18 gradi di libertà, di cui 6 non attuati. Controllo gerarchico: predizione su un secondo, inseguimento dei task, PD a 1 kHz. Stabilità statica con il **poligono di supporto**. **Stima dello stato** dalla fusione di cinematica delle gambe, IMU e odometria visiva.
- **Navigazione.** LIDAR 2D (con i suoi limiti planari) e camere di profondità per mappe 2D e 3D. Pianificazione globale e locale combinate. Modelli visione-linguaggio come CLIP per riconoscere categorie mai viste.
