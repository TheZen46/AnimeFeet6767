---

## lezione: 1 data: 2026-09-23 argomenti: [presentazione del corso, modalità d'esame, algoritmi e programmi, sintassi e semantica, limiti della computazione, ingegneria del software, interprete]

---
# Lezione 1 — Presentazione del corso e motivazioni

La prima lezione non introduce ancora contenuti tecnici in senso stretto. Serve a inquadrare il corso, a chiarirne l'organizzazione e le modalità d'esame e, soprattutto, a spiegare _perché_ un ingegnere informatico debba studiare la teoria della computazione. Il filo conduttore che emerge, e che verrà ripreso per tutto l'anno, è il problema di costruire un **interprete** corretto per un linguaggio di programmazione: viene posto alla fine di questa lezione e sviluppato nella [[Zen/Anno 2/Algoritmi e Computazione/generated/Lezione 2 - CLAUDE|lezione successiva]].

## Il corso in sintesi

### Organizzazione

Algoritmi e Computazione è un corso annuale da 12 CFU del secondo anno di Ingegneria Informatica, tenuto da Armando Tacchella (DIBRIS). Le lezioni coprono entrambi i semestri, da settembre a maggio, con la pausa didattica di gennaio e febbraio. Formalmente il corso è diviso in due moduli: uno porta lo stesso nome del corso, l'altro è il _Laboratorio di algoritmi_. Ciascun modulo ha un proprio codice e una propria pagina su AulaWeb, ma il docente aggiorna solo la pagina del corso principale. È a quella che bisogna iscriversi per ricevere le notifiche e scaricare il materiale: slide, dispense e i PDF dei tre libri di testo, forniti per uso personale e da non diffondere. Dal punto di vista dello studente la divisione in moduli è quindi un dettaglio amministrativo, e il corso va vissuto come un'unica entità.

Il docente è raggiungibile a lezione e per email. Di norma risponde entro 24 ore nei giorni lavorativi; in assenza di risposta entro 48 ore è legittimo inviare un sollecito. Il ricevimento si concorda per appuntamento, in presenza o su Teams. Per il progetto sarà disponibile anche un dottorando del docente.

I contenuti si distribuiscono sui due semestri come segue (lo schema a colori nelle slide della prima lezione riporta la stessa suddivisione):

|Semestre|Area (colore nelle slide)|Contenuti|Natura|
|---|---|---|---|
|Primo|Informatica teorica (blu, circa 4 CFU)|linguaggi formali, automi, macchine di Turing, limiti della calcolabilità|teorica|
|Primo|Programmazione in C++ (arancione)|prosecuzione di Fondamenti di Informatica, tecniche per il progetto|pratica|
|Secondo|Complessità computazionale (blu)|problemi risolvibili ma che richiedono risorse proibitive|teorica|
|Secondo|Algoritmi e strutture dati (verde)|progettazione e analisi di algoritmi e strutture dati|intermedia|

La parte blu corrisponde a ciò che nei corsi internazionali si chiama _Introduction to Theoretical Computer Science_ o _Formal Languages and Complexity_. Il suo scopo è capire che cosa c'è dietro la programmazione: quali modelli concettuali descrivono un calcolatore, e in che senso un portatile, un tablet e uno smartphone sono, per la teoria, la stessa cosa e possono essere rappresentati da un modello matematico molto più semplice su cui ragionare. La parte arancione prosegue il lavoro di Fondamenti di Informatica e prepara al progetto. La parte verde è intermedia: è teorica, ma i suoi contenuti hanno un legame molto più immediato con la programmazione quotidiana.

### Origine del corso

Il corso nasce dalla fusione di due insegnamenti precedenti, entrambi ritenuti impegnativi dagli studenti. Il primo era _Informatica e Computazione_ (6 CFU, secondo anno), che comprendeva informatica teorica e C++. Il secondo era il corso del terzo anno dedicato alla progettazione e analisi di algoritmi (9 CFU), che prevedeva un progetto di sviluppo di videogiochi. Dei 15 CFU complessivi, 12 sono confluiti in questo corso. I 3 rimanenti sono stati trasferiti al corso del terzo anno sugli strumenti per lo sviluppo software (insieme a data mining e intelligenza artificiale), oggi orientato all'ingegneria del software pratica.

Il docente osserva che si tratta di un ritorno all'antico. Nell'anno accademico 1992–93 seguiva, nella stessa aula, _Fondamenti di Informatica 2_, che trattava argomenti simili; parte dell'informatica teorica si faceva addirittura in _Fondamenti di Informatica 1_. Al termine di Fondamenti 1 e di questo corso si raggiunge quindi una preparazione paragonabile a quella che si aveva allora dopo i due corsi di Fondamenti.

### Prerequisiti e materiale di supporto

Il corso presuppone le nozioni di Fondamenti di Informatica e di Architetture (reti logiche) e, in parte, di Analisi e Algebra. Del C++ ci si aspetta una conoscenza operativa, sufficiente a partire subito con argomenti più complessi. Sul sito del corso è disponibile un compendio di nozioni matematiche di base: alcune verranno riprese, altre saranno date per scontate. Il docente consiglia di scorrerlo subito, soffermandosi sulle parti meno familiari e chiedendo chiarimenti, e di tenerlo poi come riferimento. Il contenuto del compendio è sviluppato nella nota $Nozioni \ di \ base \ (compendio)$.

## Modalità d'esame

### Le tre prove

L'esame si compone di un progetto e di due prove scritte, con punteggi che sommano a 50:

|Prova|Momento|Modalità|Punti|Peso sul modulo|Peso sul voto finale|
|---|---|---|--:|---|--:|
|Progetto|consegna a fine febbraio|individuale, svolto a casa, con discussione|10|100% del Laboratorio di algoritmi|20%|
|Primo scritto (informatica teorica)|fine del primo semestre|a libro chiuso, 2 ore|20|50% di Algoritmi e Computazione|40%|
|Secondo scritto (argomenti del secondo semestre)|fine del secondo semestre|a libro chiuso, 2 ore|20|50% di Algoritmi e Computazione|40%|

Il punteggio complessivo in cinquantesimi viene poi riportato in trentesimi. A registro compaiono tre voti, uno per ciascun modulo e uno per il corso, ma conta solo quest'ultimo, che pesa per 12 CFU. Ciascuno scritto si considera superato con almeno 12 punti su 20.

Il **progetto** è obbligatorio e individuale, e consiste nella realizzazione in C++ di un interprete per un sottoinsieme di un linguaggio di programmazione, usando le tecniche viste a lezione. L'anno scorso il linguaggio era un sottoinsieme del LISP; quest'anno potrà essere un sottoinsieme di C++, Python, Java o di un altro linguaggio, e la scelta verrà comunicata entro Natale. Dopo la consegna c'è una discussione, il cui scopo dichiarato è capire se il progetto è frutto del lavoro dello studente. L'uso di strumenti di intelligenza artificiale non è vietato, ma chi lo usa deve aver capito ciò che consegna: chi presenta un lavoro che non comprende viene rimandato finché non lo ha studiato.

Gli **scritti** sono a libro chiuso nel senso più stretto. Non sono ammessi cellulare, tablet o appunti; il foglio viene fornito dai docenti e lo studente porta solo penna, matita e gomma. La motivazione è la stessa del controllo sul progetto: con l'IA a disposizione, qualunque materiale aggiuntivo rischierebbe di sostituirsi alla comprensione. Il docente chiede inoltre elaborati leggibili e ordinati, con il codice indentato correttamente, e suggerisce di esercitarsi a scrivere a mano se necessario.

> [!important] Struttura dell'esame 
> Progetto (10 punti, individuale, con discussione) + scritto di informatica teorica (20 punti) + scritto del secondo semestre (20 punti) = 50 punti, riportati in trentesimi. Gli scritti sono a libro chiuso, durano 2 ore ciascuno e si superano con almeno 12/20.

### Calendario e validità del progetto

Il progetto, come dice il docente, «scade come il latte»: la sua validità è legata alla scadenza del progetto dell'anno successivo. La sequenza prevista è la seguente:

| Periodo               | Evento                                                                                  |
| --------------------- | --------------------------------------------------------------------------------------- |
| Settembre 2026        | Inizio del corso                                                                        |
| Metà dicembre 2026    | Assegnazione del progetto                                                               |
| Gennaio–febbraio 2027 | Primi appelli: si può sostenere lo scritto di informatica teorica                       |
| Fine febbraio 2027    | Consegna del progetto, valutazione e discussione                                        |
| Giugno–luglio 2027    | Chi ha superato la prima metà sostiene la seconda; gli altri possono sostenere entrambe |
| Settembre 2027        | Ulteriore appello, parziale o completo                                                  |
| Gennaio–febbraio 2028 | Ultimi appelli validi con il progetto di quest'anno                                     |
| Dopo                  | Il progetto scade e va rifatto quello dell'anno successivo                              |

Chi deve ancora sostenere il vecchio esame di Informatica e Computazione consegna il progetto e svolge lo scritto corrispondente al vecchio programma.

Il consiglio del docente è di sostenere l'esame per parti. I contenuti sono corposi, e affrontare quattro ore di scritto su informatica teorica e algoritmi in un'unica sessione è molto gravoso. Le due parti sono in gran parte indipendenti, con un'eccezione: la complessità computazionale del secondo semestre si appoggia sulla macchina di Turing del primo, e il secondo scritto contiene anche una domanda su quella parte. Gli algoritmi e le strutture dati sono invece del tutto indipendenti. L'ordine naturale di studio è dall'alto verso il basso. Chi non supera il primo parziale può comunque tentare il secondo e recuperare il primo in seguito, e chi non è soddisfatto del voto di una parte può ripeterla. Le situazioni eccezionali vanno discusse direttamente con il docente.

### Indicazioni del docente sul metodo (INFO INUTILI MA FANNO RIDERE)

La frequenza è libera: non si raccolgono firme, e tutto il materiale necessario è sul sito. Per chi frequenta il docente chiede puntualità (le lezioni iniziano alle 16:15 e terminano entro le 18), cellulari almeno silenziati e partecipazione attiva. In particolare invita a evitare due comportamenti: distogliere lo sguardo quando viene posta una domanda, e la «mano di piombo», cioè la reticenza ad alzare la mano quando qualcosa non è chiaro. Anche il docente e le slide possono sbagliare, e segnalare ciò che non torna è utile a tutti. Chi decide di fare qualcosa o di chiedere aiuto lo faccia per tempo: non il giorno prima della scadenza del progetto, mostrando ciò che ha provato e dove si è bloccato.

Sul metodo di studio il docente distingue livelli crescenti. _Leggere_ non è studiare. _Studiare_ significa trattenere ciò che si è letto. _Comprendere_ significa capire che cosa c'è dietro. L'obiettivo è **interiorizzare**: saper spiegare l'argomento a un compagno che non l'ha capito. A questo scopo suggerisce, a chi studia in gruppo, di dividersi gli argomenti e spiegarseli a vicenda. Sconsiglia infine la concentrazione di tutto lo studio nei pochi giorni prima dell'esame. Gli argomenti del corso si costruiscono gli uni sugli altri, come nel C++ non si capiscono le classi senza aver capito i cicli, né i template senza le classi, e un carico distribuito durante l'anno produce un apprendimento migliore.

## Algoritmi, programmi e linguaggi

### Algoritmo e programma

La nozione di **algoritmo** è più generale di quella di programma. Un algoritmo è una procedura costituita da una sequenza finita di passi ben definiti. Ogni programma scritto durante Fondamenti di Informatica è un algoritmo, ma non ogni algoritmo è un programma, anche se può in genere essere tradotto in uno. Sono algoritmi la regola di Cramer per i sistemi lineari, la regola di Ruffini per la divisione di polinomi, il calcolo del polinomio di Taylor, il metodo di bisezione per la ricerca degli zeri di una funzione; in senso lato lo sono anche una ricetta di cucina o le istruzioni di montaggio di un mobile.

Il corso non si occupa degli algoritmi in generale, ma del loro **aspetto computazionale**: interessano le procedure completamente specificate, che possono essere tradotte in programmi per _un qualche tipo di calcolatore_. Quale calcolatore sia, e che cosa esso possa o non possa fare, è precisamente uno dei temi centrali del corso.

### Sintassi e semantica

Scrivere un programma in C++ significa **formalizzare** un algoritmo, cioè esprimerlo in un linguaggio dotato di una sintassi e di una semantica definite con precisione.

La **sintassi** stabilisce come si scrivono le cose. Se manca un punto e virgola dove è richiesto, il compilatore rifiuta il programma; una sequenza come `i + - ;` non rispetta la sintassi del linguaggio. La **semantica** stabilisce il significato di ciò che è scritto: l'istruzione `i = i + 1` significa «leggi il valore corrente della variabile `i`, sommagli 1 e memorizza il risultato in `i`».

Sintassi diverse possono avere la stessa semantica, ma la coincidenza dipende dal contesto, come mostra l'esempio dell'incremento:

```cpp
int i = 3;
i = i + 1;    // i vale 4: si legge il valore, si somma 1, si memorizza
i++;          // i vale 5: usata da sola, stessa semantica della riga precedente
++i;          // i vale 6: idem

int a = i++;  // post-incremento: a riceve il valore corrente (6), poi i diventa 7
int b = ++i;  // pre-incremento: i diventa 8, poi b riceve 8
```

Come istruzioni isolate, `i++` e `++i` sono equivalenti a `i = i + 1`. All'interno di un'espressione, invece, il post-incremento restituisce il valore _precedente_ e il pre-incremento quello _successivo_. Scrivere l'uno al posto dell'altro non produce un errore di sintassi: il programma compila, ma può comportarsi diversamente da quanto voluto, e questo è un errore di semantica.

### Livelli di astrazione dell'esecuzione

Un programma è un numero finito di operazioni elementari. «Elementare», però, è un concetto relativo al livello di astrazione. Un programma C++ viene compilato in linguaggio macchina, le cui istruzioni sono più elementari di quelle del C++. Alcune istruzioni macchina, come certe operazioni in virgola mobile, sono a loro volta realizzate all'interno della CPU come sequenze di operazioni ancora più semplici (microprogrammazione). Per il momento il corso si ferma al livello del linguaggio di programmazione.

La **teoria della computazione** si colloca a monte di tutti questi livelli: definisce le caratteristiche che devono avere gli algoritmi e i linguaggi in cui essi sono espressi. Può sembrare filosofia, ma è ciò che permette di ragionare con rigore su che cosa un calcolatore può fare.

## Perché studiare la teoria: i limiti del calcolo

### Un unico modello per tutti i calcolatori

In un percorso ideale questa teoria verrebbe insegnata prima della programmazione, come accade per Analisi e Geometria al primo anno. Per ragioni storiche e didattiche l'ordine è invertito: prima si impara a programmare, poi si scopre che cosa c'è dietro. Il docente avverte che la parte formale non è lontana, nello stile, da quella dei corsi di Analisi e Geometria, ma resta un corso di informatica: la formalizzazione si fa «con le modalità da informatici», e ogni concetto teorico sarà accompagnato da un'intuizione pratica.

Il motivo per cui la teoria è indispensabile è che vogliamo conoscere i **limiti strutturali** delle nostre architetture di calcolo. Tutti i calcolatori noti, compresi quelli meno convenzionali come i calcolatori quantistici o biologici, sono riconducibili a un unico modello, che sarà studiato nel corso. Questa affermazione non è dimostrabile, ma nessun controesempio è mai stato trovato.

> [!tip] Approfondimento — La tesi di Church-Turing #approfondimento 
> L'affermazione secondo cui tutti i calcolatori sono riconducibili a un unico modello, senza che lo si possa dimostrare, corrisponde alla **tesi di Church-Turing**. La tesi afferma che la nozione intuitiva di procedura effettiva (algoritmo) coincide con ciò che può essere calcolato da una macchina di Turing. È una _tesi_ e non un teorema perché uno dei due termini del confronto, la nozione intuitiva di algoritmo, non è un oggetto matematico formale. A suo sostegno c'è il fatto che i principali modelli di calcolo proposti (funzioni ricorsive, lambda-calcolo, macchine a registri) si sono rivelati equivalenti alla macchina di Turing. La tesi riguarda _che cosa_ è calcolabile, non _quanto velocemente_. I calcolatori quantistici, per esempio, non ampliano l'insieme delle funzioni calcolabili. Per alcuni problemi, però, sono noti algoritmi quantistici più efficienti dei migliori algoritmi classici conosciuti, come l'algoritmo di Shor per la fattorizzazione degli interi.

### Problemi non calcolabili e problemi intrattabili

Il modello ha dei limiti di due tipi. Esistono problemi che **non possono essere risolti** da alcun calcolatore. Non si tratta di questioni vaghe come il senso della vita, ma di problemi precisi e in apparenza semplici. Esistono poi problemi che **possono essere risolti** ma richiedono un tempo enorme: più lungo della vita di una persona, o persino dell'età dell'universo.

Questo secondo limite ha conseguenze molto concrete. Un committente potrebbe chiedere un programma che funziona bene con tre, quattro o sei variabili, ma che da dieci variabili in su richiede un tempo insensato. Un ingegnere deve saperlo riconoscere e saperlo spiegare, perché il tempo di calcolo si traduce in denaro, risorse ed emissioni di CO₂. Un programma inefficiente scarica la batteria di uno smartphone o rende un sito web lento a rispondere. L'efficienza viene studiata in termini teorici, ma è un problema pratico del mestiere.

### Correttezza del software e intelligenza artificiale

Il risultato a cui il primo semestre vuole arrivare è che un calcolatore come quelli che usiamo, compresi quelli su cui girano i sistemi di intelligenza artificiale, **non può dimostrare in modo algoritmico la correttezza** di ciò che produce, né di ciò che produciamo noi. Le capacità computazionali di un'IA sono limitate da quelle della macchina su cui gira. A meno di un cambiamento radicale di architettura, che oggi non si sa prevedere, nessun sistema di IA può garantire la correttezza delle proprie risposte. Strumenti come ChatGPT o Claude possono scrivere codice, anche parti del progetto del corso, ma non possono garantire che sia corretto.

La dimostrazione formale di correttezza non è immediata nemmeno per un essere umano. In certi casi la si riesce a fare, e in certi casi la si riesce ad automatizzare, ma esistono limiti invalicabili. Il docente usa come analogia il principio di indeterminazione di Heisenberg: un limite strutturale, non una carenza tecnologica destinata a essere superata.

> [!tip] Approfondimento — Perché la correttezza non è verificabile in generale #approfondimento 
> Il risultato anticipato a lezione poggia su due teoremi classici che verranno trattati nel corso. Il primo è l'indecidibilità del **problema della terminazione** (_halting problem_), che risale al lavoro di Turing del 1936: non esiste alcun algoritmo che, dato un programma qualsiasi e un suo input, stabilisca sempre correttamente se l'esecuzione termina [@turing1936]. Il secondo è il **teorema di Rice**, che generalizza il primo: qualunque proprietà non banale del _comportamento_ di un programma è indecidibile [@rice1953; @sipser2013]. «Non banale» significa che la proprietà vale per alcuni programmi e non per altri; «calcola la funzione richiesta dalla specifica» è una proprietà di questo tipo. Ne segue che nessun verificatore automatico può decidere la correttezza di _tutti_ i programmi. Restano possibili verifiche su classi ristrette di programmi o di proprietà, oppure procedure che in alcuni casi non terminano o rispondono «non so». Questo è coerente con quanto detto a lezione: la verifica è possibile in casi specifici, non in generale.

## Dal programmatore all'ingegnere

### Il paragone con l'ingegneria civile

Il docente riassume l'obiettivo del corso con un'analogia: **il programmatore sta all'ingegnere informatico come il muratore sta all'ingegnere civile**. Il lavoro del muratore si può in parte automatizzare, per esempio stampando una casa in 3D. Resta però necessario l'ingegnere che la progetta perché non crolli: sceglie materiali e spessori, la rende resistente ai terremoti, ne contiene i costi e, soprattutto, firma il progetto assumendosene la responsabilità. Allo stesso modo, il programmatore può essere sostituito in parte dall'IA, l'ingegnere informatico no. Per questo la parte di programmazione del corso è relativamente ridotta: non perché sia poco importante (il progetto esiste proprio perché saper costruire applicazioni è fondamentale), ma perché lo scopo è formare ingegneri e non solo programmatori.

Nell'informatica questa distinzione tende a sfumare, perché il software sembra immateriale, gratuito e facile da produrre. Capita che vengano fatte richieste che, tradotte nell'ingegneria civile, suonerebbero come «costruiscimi questo ponte in una settimana, chiavi in mano», magari con l'argomento che «tanto lo fa l'IA». Ma l'IA genera anche molti errori. Un'applicazione che funziona davvero, e su cui un ingegnere mette la propria firma, richiede il tempo necessario a garantirne la correttezza.

La ricerca degli errori (_bug_) non è meccanizzabile in generale. Si possono eseguire test e prove, ma nessuna quantità di prove dà la certezza totale dell'assenza di errori. È per questo che sistemi operativi e applicazioni continuano a ricevere aggiornamenti correttivi, anche dopo decenni di lavoro dei migliori informatici del mondo: gli errori sono molti meno che in passato, ma non sono eliminabili per via automatica.

> [!tip] Approfondimento — Testing e assenza di errori #approfondimento 
> L'osservazione che le prove non bastano a garantire l'assenza di errori ha una formulazione celebre dovuta a Edsger W. Dijkstra, nella conferenza per il premio Turing del 1972. Il testing, osservò, può essere molto efficace nel mostrare la _presenza_ di bug, ma è del tutto inadeguato a dimostrarne l'_assenza_ [@dijkstra1972]. Il motivo è combinatorio prima ancora che teorico: anche una funzione che riceve due interi a 32 bit ammette $2^{64} \approx 1{,}8 \times 10^{19}$ input distinti, un numero che rende impraticabile il collaudo esaustivo.

### Casi storici

Gli errori di progettazione hanno conseguenze materiali, e la lezione ne passa in rassegna alcuni esempi.

Nell'ingegneria civile, il ponte sullo stretto di Tacoma, nello Stato di Washington, entrò in oscillazioni sempre più ampie sotto l'azione del vento fino a crollare, pochi mesi dopo l'apertura nel 1940. Il docente lo paragona a un'altalena: spingendo in fase con il moto si ottengono oscillazioni sempre più ampie. Il fenomeno rientra nello studio dei sistemi oscillanti sottoposti a una forzante, che si affronta in Teoria dei Sistemi. Il progettista era un ingegnere di primo piano, che aveva lavorato al Golden Gate: neppure la competenza mette al riparo dagli errori. Più recente è il crollo del viadotto Polcevera (il «ponte Morandi») a Genova, il 14 agosto 2018, costato la vita a 43 persone. Il docente lo attribuisce a una combinazione di errori progettuali, riconosciuti dallo stesso progettista e rimasti inascoltati, e di carenze di manutenzione.

> [!tip] Approfondimento — Risonanza o instabilità aeroelastica? #approfondimento 
> Il ponte di Tacoma Narrows, progettato da Leon Moisseiff (che era stato ingegnere consulente per il Golden Gate), fu costruito a partire dal novembre 1938, aperto il 1° luglio 1940 e crollato il 7 novembre dello stesso anno, con un vento di circa 64–68 km/h. La trascrizione colloca l'apertura a novembre, che è invece il mese del crollo. Il paragone con l'altalena è efficace, ma la spiegazione come semplice risonanza forzata, molto diffusa nei manuali, è considerata dagli ingegneri un'eccessiva semplificazione. Billah e Scanlan mostrano che il crollo è descritto meglio come un'**instabilità aeroelastica autoeccitata** (_flutter_ torsionale): è il moto stesso del ponte a modulare le forze del vento, che si comportano in sostanza come uno smorzamento negativo.

Nell'ingegneria informatica, l'esempio più noto è il primo lancio del razzo europeo **Ariane 5** (1996). Meno di un minuto dopo il decollo il razzo prese una traiettoria anomala e si distrusse. La causa fu un errore nel software del sistema di riferimento inerziale, il componente che fornisce assetto e posizione. Un numero in virgola mobile a 64 bit fu convertito in un intero a 16 bit, troppo piccolo per contenerlo. Il controllo che avrebbe intercettato l'errore era stato disattivato per ragioni di efficienza. A questo si aggiungono il caso di una macchina per radioterapia che somministrava ai pazienti dosi letali (il caso noto è quello del Therac-25) e quello del sistema automatico di smistamento bagagli dell'aeroporto di Denver, i cui malfunzionamenti ne bloccarono l'apertura (avvenuta nel 1995, con oltre un anno di ritardo) finché il sistema non fu ripristinato. Tutti questi incidenti risalgono a negligenze nella progettazione e nella produzione del software.

> [!tip] Approfondimento — I casi Ariane 5 e Therac-25 nelle fonti #approfondimento 
> Il volo 501 di Ariane 5 (4 giugno 1996) è documentato nel rapporto della commissione d'inchiesta presieduta da Jacques-Louis Lions [@lions1996]. L'eccezione si verificò nel software del sistema di riferimento inerziale (SRI), durante la conversione da un numero in virgola mobile a 64 bit a un intero con segno a 16 bit di una variabile chiamata BH (_horizontal bias_), legata alla velocità orizzontale. Il software era stato ripreso da Ariane 4, la cui traiettoria iniziale produceva velocità orizzontali molto inferiori. Su Ariane 5 il valore superò il massimo rappresentabile, $2^{15}-1 = 32,767$.
> 
> Non tutte le conversioni erano protette, perché per il calcolatore dello SRI era stato fissato un carico di lavoro massimo dell'80%. Per le variabili lasciate senza protezione si era ragionato che fossero fisicamente limitate, e per BH quel ragionamento si rivelò sbagliato. Le due unità SRI ridondanti eseguivano lo stesso software e si guastarono allo stesso modo. Il calcolatore di bordo interpretò come dati di volo il messaggio diagnostico ricevuto e comandò la deflessione massima degli ugelli. Il modulo che causò l'errore, peraltro, produceva risultati significativi solo _prima_ del decollo.
> 
> Quanto alle cifre, i 7 miliardi di dollari ricordati a lezione corrispondono al costo di circa dieci anni di sviluppo del programma Ariane 5. Il valore del lanciatore e del carico perduti è stimato in circa 500 milioni di dollari [@arnold-ariane].
> 
> Il Therac-25 era un acceleratore lineare per radioterapia. Tra giugno 1985 e gennaio 1987 fu coinvolto in sei incidenti con sovradosaggi massicci, alcuni mortali. L'analisi di riferimento è quella di Leveson e Turner [@leveson1993]. Tra le cause individua difetti di programmazione concorrente e la scelta di affidare al software controlli di sicurezza prima garantiti da interblocchi hardware. Un difetto di programmazione concorrente è, per esempio, una _race condition_: un errore che si manifesta solo per certi ordini temporali in cui processi concorrenti accedono a dati condivisi.

Il docente fa notare che questi incidenti sono avvenuti prima dell'era dei generatori automatici di codice. Generare software senza verificare che abbia le proprietà attese, e senza poter delegare questa verifica alle macchine, porta a guasti di questo tipo. Gli errori di un ingegnere informatico hanno quindi un **impatto cinetico**, cioè conseguenze fisiche nel mondo reale. Lo stesso vale, in scala minore, per l'inefficienza: un programma lento consuma batteria, allunga i tempi di attesa e aumenta le emissioni. Lo scopo del corso non è fornire ricette risolutive, ma rendere consapevoli di questi aspetti dal punto di vista teorico.

## Il problema guida del corso: costruire un interprete

La lezione si chiude con il problema che accompagnerà tutto il corso e che sarà anche il tema del progetto. A sinistra c'è un file sorgente con un semplice programma; a destra c'è il risultato che appare sulla console. L'obiettivo non è scrivere quel programma, ma scrivere **un programma che, dato un qualsiasi programma costruito con un insieme di istruzioni ben definito e con una semantica ben definita, ne produca il risultato**. Questo programma è un interprete.

> [!important] Il problema dell'interprete Dato un linguaggio con sintassi e semantica definite con precisione, costruire un programma che riceva in input un qualsiasi programma scritto in quel linguaggio e ne produca il risultato dell'esecuzione. L'interprete deve essere **corretto**: un errore nell'interprete fa fallire programmi che di per sé sono giusti.

La correttezza dell'interprete è cruciale. Quando si svolgono gli esercizi di programmazione si assume implicitamente che il compilatore sia corretto, e che ogni errore sia nostro. Se l'interprete è sbagliato, invece, i programmi falliscono senza colpa di chi li ha scritti.

Il docente invita a riflettere su come si affronterebbe il problema, anche cercando in rete o chiedendo a un assistente IA. Un assistente probabilmente risolverebbe il caso specifico, ma senza far capire _perché_ ha fatto certe scelte, ed è proprio questo il punto del corso. Pur non essendo un corso di compilatori, il corso fornirà alcune nozioni tipiche di quella disciplina. I primi calcolatori, come l'ENIAC, risalgono agli anni Quaranta. Dalla programmazione per cablaggio si è passati all'assembly e poi, dagli anni Cinquanta e Sessanta, ai linguaggi di alto livello, e da allora esiste una vasta letteratura su come costruire traduttori e interpreti. Il corso si limiterà alla parte iniziale della catena di un compilatore, detta _front-end_, sufficiente a costruire un interprete; la traduzione in assembly è esclusa.

Ogni fase dell'interprete si collega a una parte specifica della teoria, e ogni argomento teorico verrà motivato richiamando questo esempio. Gli interpreti sono peraltro ovunque: un browser è un interprete di HTML, un sistema di gestione di basi di dati è un interprete di SQL, la riga di comando di un sistema operativo è un interprete.

## In sintesi

Il corso unisce informatica teorica, programmazione in C++, algoritmi e complessità, con l'obiettivo di formare ingegneri capaci di ragionare sui limiti e sulla correttezza del software, e non semplici programmatori. L'esame combina un progetto individuale (un interprete scritto in C++) con due scritti a libro chiuso, ed è consigliabile sostenerlo per parti. Concettualmente, la lezione distingue algoritmo e programma, introduce la coppia sintassi–semantica e anticipa il risultato teorico centrale del semestre: un calcolatore non può verificare algoritmicamente, in generale, la correttezza dei programmi. Il problema dell'interprete, che sarà scomposto nelle sue fasi nella lezione successiva, è il ponte tra la teoria e la pratica del corso.