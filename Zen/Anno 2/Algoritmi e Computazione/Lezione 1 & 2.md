Il corso di Algoritmi e Computazione, tenuto dal docente Armando Tacchella, si pone l'obiettivo di fornire i fondamenti teorici dell'informatica e della programmazione, elevando lo studente dal ruolo di mero programmatore a quello di ingegnere del software consapevole dei limiti strutturali e matematici delle architetture di calcolo. L'insegnamento annuale è strutturato in due semestri: il primo focalizzato sull'informatica teorica e la programmazione in C++, e il secondo dedicato alla complessità computazionale, agli algoritmi e alle strutture dati. L'esame prevede un progetto obbligatorio, che consiste nello sviluppo di un interprete valutato tramite discussione per accertarne la reale comprensione da parte dello studente, e prove scritte "closed book" da svolgere rigorosamente senza ausili esterni. Il corso sottolinea con forza l'importanza dell'ingegneria informatica citando disastri storici causati da difetti del software, come il razzo europeo Ariane 5 o l'analogo ingegneristico del ponte di Tacoma, dimostrando che gli errori di programmazione hanno un impatto cinetico, economico e di spreco di risorse nel mondo reale. Tale enfasi giustifica lo studio formale e rigoroso: la verifica della correttezza del software non può essere interamente delegata o automatizzata alle macchine o alle moderne intelligenze artificiali, richiedendo l'intervento e l'ingegno di un progettista umano qualificato.

  

**Fondamenti Teorici e Struttura di un Interprete** La teoria della computazione definisce le caratteristiche formali che devono avere gli algoritmi e i linguaggi in cui essi sono espressi, fornendo la base tecnologica e concettuale per la costruzione di traduttori, compilatori e interpreti. Il processo di interpretazione di un programma sorgente, ad esempio scritto in un sottoinsieme del linguaggio C++, viene suddiviso in tre macro-fasi sequenziali per dominare la complessità del problema e scomporlo in componenti computazionalmente trattabili.

  

- **Analisi Lessicale (Lexer):**
    
      
    - L'analizzatore lessicale prende in input il codice sorgente grezzo sotto forma di file di testo e lo converte in una sequenza lineare di elementi strutturati chiamati "token".
        
          
        
    - Ogni token estratto è un'entità logica composta da un lessema, ovvero l'effettiva stringa di testo individuata, e da un tag (etichetta) che ne specifica la natura semantica, classificandolo ad esempio come un tipo di dato (int), un identificatore di variabile o funzione, un operatore matematico o un segno di interpunzione.
        
          
        
    - Durante l'elaborazione lessicale, il lexer si occupa di scartare deliberatamente lo spazio bianco (whitespace), le indentazioni, le tabulazioni e i ritorni a capo, poiché tali artefatti visivi servono unicamente a migliorare la leggibilità del codice per l'essere umano, ma non veicolano informazioni rilevanti per la logica di compilazione.
        
          
        
    - Il risultato finale di questa operazione è una lista sequenziale di token, generata solitamente in memoria, che rappresenta l'input epurato e categorizzato per lo stadio successivo.
        
          
        
- **Analisi Sintattica (Parser):**
    
      
    - L'analizzatore sintattico prende in consegna la lista lineare generata dal lexer e verifica rigorosamente se la disposizione dei token rispetta la grammatica formale prestabilita del linguaggio di programmazione utilizzato.
        
          
        
    - La struttura dei linguaggi di programmazione non è lineare ma gerarchica: un intero programma è composto da funzioni, che delimitano blocchi logici, i quali a loro volta aggregano sequenze di istruzioni semplici o composte.
        
          
        
    - Il compito del parser è trasformare la lista lineare dei token in una struttura ramificata e multidimensionale, definita tecnicamente albero sintattico (o grafo), in cui i singoli nodi astraggono e incapsulano le relazioni gerarchiche tra i costrutti del codice sorgente.
        
          
        
    - Questa fase di verifica è fondamentale e irrinunciabile, in quanto un insieme di token validi e sintatticamente corretti a livello lessicale potrebbe essere stato disposto in un ordine che non costituisce in alcun modo un programma logicamente sensato per le regole del C++.
        
          
        
- **Analisi Semantica e Valutazione (Evaluator):**
    
      
    - L'evaluator costituisce il cuore dell'esecuzione, procedendo a visitare sistematicamente l'albero sintattico nodo per nodo per associare a ciascun blocco la sua definizione semantica ed eseguirne le istruzioni computazionali.
        
          
        
    - Per mantenere la coerenza dello stato del programma, l'evaluator si appoggia a una struttura dati dinamica denominata "symbol table" (tabella dei simboli) per registrare in memoria lo stato e la visibilità degli elementi logici, tenendo traccia delle firme delle funzioni (includendo parametri e tipo di ritorno) e delle allocazioni e assegnazioni delle variabili locali o globali.
        
          
        
    - Valutando le espressioni aritmetiche, manipolando i blocchi di memoria e calcolando le chiamate a funzione incontrate nell'albero, l'interprete risolve i procedimenti logici e determina l'output o il comportamento finale atteso dal software.
        
          
        

**Alfabeti, Stringhe e Linguaggi** Ogni componente pratica che forma un interprete affonda le proprie basi nell'informatica teorica e nella matematica discreta, materie deputate alla modellazione e alla definizione rigorosa dei linguaggi formali.

  

- **Alfabeti:** Un alfabeto, rappresentato formalmente in matematica discreta tramite la lettera greca maiuscola $\Sigma$, è rigorosamente definito come un insieme finito e non vuoto composto da simboli atomici indivisibili. Esempi pratici e ricorrenti di tali alfabeti includono l'alfabeto binario costituito dai soli elementi $\Sigma = \{0, 1\}$, l'elenco sequenziale di tutte le singole lettere dell'alfabeto minuscolo o l'esteso set comprensivo di tutti i caratteri della codifica ASCII.
    
      
    
- **Stringhe:** Sulla base degli alfabeti è possibile generare le stringhe, definite come sequenze finite di simboli ordinati selezionati dall'alfabeto $\Sigma$ di riferimento.
    
      
    - Un elemento fondamentale dell'informatica teorica è la stringa vuota, che si differenzia per l'assenza totale di simboli al suo interno e viene denotata storicamente con la lettera greca $\epsilon$.
        
          
        
    - La proprietà dimensionale di una stringa $w$, indicata con la notazione di cardinalità $\vert{}w\vert{}$, si calcola determinando il numero di posizioni occupate dai caratteri, il che implica che la lunghezza della stringa vuota $\epsilon$ sia costantemente pari a 0.
        
          
        
    - La manipolazione delle stringhe avviene tramite l'operazione di concatenazione insiemistica, che fonde due elementi testuali posizionando la totalità della seconda stringa al termine della prima; in tale operazione, la stringa $\epsilon$ si comporta da elemento neutro o identità, per cui concatenarla a destra o a sinistra di una stringa $x$ restituisce il valore inalterato $x$.
        
          
        
    - Esiste l'operazione di potenza applicata a un alfabeto, trascritta come $\Sigma^k$, che identifica univocamente l'insieme di cardinalità finita contenente tutte e sole le possibili permutazioni di stringhe aventi l'esatta lunghezza $k$ generate tramite i simboli di $\Sigma$.
        
          
        
    - L'aggregazione esaustiva di tutte le possibili stringhe generabili a partire da un alfabeto $\Sigma$, includendo di base anche la stringa vuota, viene raggruppata sotto l'operatore matematico asterisco, originando l'insieme infinito $\Sigma^*$ noto come chiusura di Kleene.
        
          
        
- **Linguaggi:** Partendo da questi assunti, la definizione universale di linguaggio $L$ stabilisce che esso corrisponde a un qualunque sottoinsieme, sia esso proprio o improprio, estratto dall'insieme generatore universale $\Sigma^*$, formalizzabile tramite la dicitura matematica $L \subseteq \Sigma^*$.
    
      
    - Le proprietà di cardinalità permettono l'esistenza di linguaggi composti da un numero strettamente finito di elementi, arrivando ai casi estremi del linguaggio vuoto denotato dal simbolo $\emptyset$, che si caratterizza per non avere alcuna stringa al suo interno e una cardinalità di 0, e il linguaggio unitario composto esclusivamente dalla stringa vuota $\{\epsilon\}$, il quale possiede una cardinalità pari a 1.
        
          
        
    - Simmetricamente, la maggior parte dei linguaggi interessanti dal punto di vista informatico presenta un numero totalmente infinito di stringhe, sebbene esse siano circoscritte e generate a partire da un set chiuso e strettamente finito di regole costruttive grammaticali. Fanno parte di tale tipologia insiemi complessi come l'insieme di ogni programma C++ sintatticamente immacolato, o linguaggi descrittivi matematici come l'insieme di stringhe binarie dove occorrono quantità identiche di simboli zero e uno.
        
          
        
    - Sui linguaggi, concepiti matematicamente come insiemi, possono operare logiche e trasformazioni algebriche standard e peculiari, incluse l'unione (la fusione degli elementi di due sottoinsiemi garantendo computatività), la concatenazione (la generazione di nuove stringhe giustapponendo in modo vincolato un prefisso appartenente al primo linguaggio a un suffisso originario del secondo) e la ripetizione indefinita tramite la chiusura di Kleene (l'unione insiemistica di ogni possibile operazione di potenza iterata sul medesimo linguaggio).
        
          
        

**Il Problema della Parola (Word Problem)** Tutte le strutture descritte convergono all'interno dell'assioma del "Word Problem" (il problema dell'appartenenza della parola), la cui risoluzione impone di determinare, in modo algoritmico e in tempi circoscritti, se una specifica stringa arbitraria $w$, facente parte dell'insieme chiusura $\Sigma^*$, sia effettivamente o meno un elemento che compone il linguaggio $L$ in esame. L'intera sovrastruttura applicativa dei software e ogni singola divisione funzionale di un compilatore possono essere matematicamente classificate come risoluzioni in scala di vari "Word Problem" innestati l'uno dentro l'altro:

  

- L'analisi lessicale svolge un "Word Problem" il cui obiettivo è stabilire se stringhe di byte e caratteri ASCII rientrino perfettamente nei limiti del linguaggio delimitante i token corretti, ad esempio discriminando se una combinazione testuale sia un nome ammissibile all'interno del linguaggio isolato degli identificatori di programma.
    
      
    
- L'analisi sintattica si configura a propria volta come la medesima famiglia di problemi logici che, modificando il proprio dominio di base assumendo la lista dei token appena creata come alfabeto generativo primitivo, deve discriminare categoricamente se la catena formata da suddetti blocchi token appartenga al linguaggio di proporzioni infinite inglobante ogni programma formalmente valevole secondo il set di direttive della grammatica del codice.
    
      
    
- Le ultime barriere architettoniche e l'analisi semantica sono preposte a sentenziare su linguaggi aventi un grado di ambiguità e una scala concettuale che impongono calcoli estesi, come l'onere di risolvere il word problem volto a sancire la presenza o meno della stringa raffigurante il nome di una variabile prima che ne sia richiesta la computazione dinamica.
    
      
    
- Lo scibile della computazione artificiale riposa sulla costruzione di meccanismi fisici o matematici (che si estendono dagli automi a stati finiti in possesso di limitatissima memoria per i lexer e i parser, scalando in alto per potenza e capacità descrittiva fino all'apoteosi del modello universale offerto dalla macchina di Turing e dalle architetture dei moderni processori) destinati essenzialmente alla sola mansione di abbattere e calcolare le risposte per i "Word Problem", la cui classificazione stabilisce le basi per la dimostrazione inconfutabile non solo delle enormi facoltà, ma soprattutto dei perentori e invalicabili limiti strutturali presenti in ciascun sistema di calcolo esistente.