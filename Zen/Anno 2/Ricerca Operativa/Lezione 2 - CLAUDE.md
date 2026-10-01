---

## corso: Ricerca Operativa lezione: 2 data: 2026-09-25 docente: Silvia Villa argomenti: [allocazione ottima di risorse scarse, programmazione lineare continua, programmazione non lineare, problemi di minimo e di massimo, soluzione ammissibile, soluzione ottima, vincoli di disuguaglianza, vincolo attivo, vincolo ridondante, risorse concorrenti, risorse alternative, forma matriciale, problemi di miscelazione] fonti: [trascrizione, appunti manuali, dispense] tags: [ricerca-operativa, lezione]

---

# Lezione 2 — Primi modelli di programmazione matematica


Nella lezione precedente si è arrivati alla forma generale di un problema di ottimizzazione,

$$ \min_{x \in S} f(x) \qquad \text{oppure} \qquad \max_{x \in S} f(x), $$

con variabili $x$, funzione obiettivo $f$ e insieme $S$ definito dai vincoli (si veda [[Zen/Anno 2/Ricerca Operativa/Lezione 1 - CLAUDE|Lezione 1 - CLAUDE]]). L'obiettivo di questa lezione è esercitarsi a portare problemi concreti in questa forma, determinando ogni volta, nell'ordine, **variabili**, **funzione obiettivo** e **insieme ammissibile**, e introdurre la nomenclatura di base.

## Esempio: un'industria chimica

Un'industria chimica produce **quattro tipi di fertilizzanti** $T_1, \dots, T_4$. Per essere pronto alla vendita, ogni tipo deve essere lavorato in **due reparti**, che le dispense chiamano reparto produzione e reparto confezionamento. La tabella riporta le ore di lavorazione necessarie in ciascun reparto per una tonnellata di fertilizzante, insieme al profitto netto per tonnellata (in euro):


|                   | $T_1$ | $T_2$  | $T_3$  | $T_4$ |
| ----------------- | ----- | ------ | ------ | ----- |
| $R_1$             | $2$   | $1.5$  | $0.5$  | $2.5$ |
| $R_2$             | $0.5$ | $0.25$ | $0.25$ | $1$   |
|                   |       |        |        |       |
| $\text{Profitto}$ | $250$ | $230$  | $110$  | $350$ |

Ogni settimana il reparto $R_1$ può essere utilizzato al massimo per **100 ore** e il reparto $R_2$ al massimo per **50 ore**. Si vuole determinare la **produzione settimanale** che massimizza il profitto complessivo. Si potrebbe, per esempio, produrre solo fertilizzante di tipo 1, ma occorre capire come diversificare la produzione.

> [!warning] Discrepanza tra fonti — disponibilità del reparto 2 In un passaggio della trascrizione la docente dice "reparto 2, 80 ore", ma poco dopo usa 50 ore per scrivere il vincolo. Gli appunti manuali e le dispense riportano 50 ore. La nota Obsidian _Esempi_ scrive "$R_1 \leftarrow 50$ ore": è un refuso per $R_2$. Il valore corretto è **50 ore per il reparto 2**.

### Variabili

Bisogna mettersi nei panni del direttore della produzione e chiedersi che cosa può scegliere. Non c'è un unico modo di affrontare un problema, ma qui la scelta più naturale è evidente: si decide **quanto produrre di ciascun tipo**. Una decisione possibile, ancora da verificare rispetto ai vincoli, sarebbe "questa settimana 5 tonnellate di tipo 1, 4 di tipo 2, nessuna di tipo 3 e 2 di tipo 4". Si pone quindi

$$ x_i = \text{tonnellate di fertilizzante di tipo } T_i \text{ prodotte in una settimana}, \qquad i = 1, \dots, 4. $$

È ragionevole poter produrre anche frazioni di tonnellata, quindi le variabili sono **continue** e l'insieme ammissibile sarà un sottoinsieme $S \subseteq \mathbb{R}^4$. Un problema con variabili continue si dice di **programmazione matematica continua**.

### Funzione obiettivo

Se si producono $x_1, x_2, x_3, x_4$ tonnellate, il profitto settimanale è

$$ f(x_1, x_2, x_3, x_4) = 250,x_1 + 230,x_2 + 110,x_3 + 350,x_4, $$

da **massimizzare**. Dietro questa espressione c'è un'ipotesi poco realistica, ma accettabile per il modello: si **vende tutto ciò che si produce**.

### Vincoli

Non tutte le produzioni sono ammissibili, perché le ore disponibili nei reparti sono limitate. Ogni tonnellata di tipo 1 richiede 2 ore del reparto 1, quindi producendone $x_1$ si usano $2x_1$ ore. Ogni tonnellata di tipo 2 richiede un'ora e mezza, quindi $1.5x_2$ ore, e così via. Il tempo totale di utilizzo del reparto 1 non deve superare 100 ore; lo stesso ragionamento vale per il reparto 2:

$$ \begin{aligned} 2x_1 + 1.5x_2 + 0.5x_3 + 2.5x_4 &\le 100, \ 0.5x_1 + 0.25x_2 + 0.25x_3 + x_4 &\le 50. \end{aligned} $$

Le quantità prodotte non possono essere negative. Si aggiungono quindi i **vincoli di non negatività** $x_1 \ge 0$, $x_2 \ge 0$, $x_3 \ge 0$, $x_4 \ge 0$. La docente sottolinea che è sempre comodo averli espliciti: saranno molto utili quando si applicherà il metodo del simplesso.

### Il modello

> [!important] Modello dell'industria chimica $$ \begin{aligned} \max \quad & 250x_1 + 230x_2 + 110x_3 + 350x_4 \ \text{s.t.} \quad & x = (x_1, x_2, x_3, x_4) \in S, \end{aligned} $$ $$ S = \left{ x \in \mathbb{R}^4 ;\middle|; \begin{aligned} & 2x_1 + 1.5x_2 + 0.5x_3 + 2.5x_4 \le 100 \ & 0.5x_1 + 0.25x_2 + 0.25x_3 + x_4 \le 50 \ & x_1 \ge 0,\ x_2 \ge 0,\ x_3 \ge 0,\ x_4 \ge 0 \end{aligned} \right}. $$ $S$ è l'**insieme ammissibile**; ogni suo elemento è una **soluzione ammissibile**.

La funzione obiettivo è **lineare** (le incognite compaiono al primo grado), i vincoli sono **lineari** (in questo caso vincoli di disuguaglianza, sia "$\le$" sia "$\ge$") e le variabili sono **continue**. Il problema è quindi di **programmazione lineare continua**. Il nome di un problema dipende sia dalla **struttura** della funzione obiettivo e dei vincoli, sia dal **tipo di variabili**.

Problemi come questo si chiamano **problemi di allocazione ottima di risorse scarse**. La risorsa scarsa è il tempo disponibile nei reparti, e bisogna "allocarla", cioè ripartirla, tra i diversi prodotti.

## Esempio non lineare: un'agenzia pubblicitaria

Un'agenzia pubblicitaria deve organizzare una campagna usando solo due mezzi, annunci **radiofonici** e pagine di **giornale**. La docente nota che il libro da cui è tratto l'esempio "si vede che è un po' datato". I dati sono:

- **radio**: il costo _al minuto_ di un annuncio è di $100$ euro meno $2$ euro per ogni minuto di durata dell'annuncio, che può durare al massimo **30 minuti**. Quindi un annuncio più lungo costa meno _al minuto_: un annuncio di un minuto costa $98$ €/min, uno di due minuti $96$ €/min;
- **giornale**: $200$ euro per pagina, con pagine **frazionabili** (mezza pagina costa $100$ euro). La docente ha scelto questo dato apposta, per avere variabili continue come quelle del corso;
- **vincolo contrattuale**: almeno **un terzo della spesa** complessiva deve essere destinato ai giornali. Vincoli di questo tipo, come quelli di mercato, vengono da accordi esterni e non da limiti fisici;
- **pubblico raggiunto**: ogni minuto di annuncio radio raggiunge $100,000$ persone, ogni pagina di giornale $15,000$.

Si vogliono raggiungere almeno **3 milioni di persone** **minimizzando i costi**.

### Variabili, obiettivo e vincoli

L'agenzia deve scegliere quanti minuti di radio e quante pagine di giornale acquistare. Entrambe le grandezze possono essere frazionarie:

$$ x_1 = \text{minuti di annuncio radiofonico}, \qquad x_2 = \text{pagine di giornale}, \qquad S \subseteq \mathbb{R}^2. $$

La parte delicata è il costo della radio. Se l'annuncio dura $x_1$ minuti, il costo al minuto è $100 - 2x_1$, quindi il costo totale della radio è $x_1(100 - 2x_1)$. Il costo del giornale è invece lineare, $200x_2$. La funzione obiettivo da **minimizzare** è

$$ f(x_1, x_2) = x_1(100 - 2x_1) + 200,x_2 . $$

I vincoli sono tre. Il **vincolo contrattuale** impone che la spesa per i giornali sia almeno un terzo della spesa totale; il **vincolo sul pubblico** impone di raggiungere almeno 3 milioni di persone; infine ci sono i vincoli di **non negatività**:

$$ \begin{aligned} 200,x_2 &\ge \tfrac{1}{3}\big( x_1(100 - 2x_1) + 200,x_2 \big), \ 100,000,x_1 + 15,000,x_2 &\ge 3,000,000, \ x_1 \ge 0, \quad x_2 &\ge 0 . \end{aligned} $$

> [!warning] Vincolo mancante nella formulazione della lavagna (integrazione) Nel testo del problema la durata massima dell'annuncio è di 30 minuti, ma né la formulazione scritta a lezione né gli appunti contengono il vincolo corrispondente $$ x_1 \le 30 .$$ Il vincolo va aggiunto, e non solo per completezza. Senza di esso, per $x_1 > 50$ il "costo al minuto" $100 - 2x_1$ diventa negativo. Scegliendo $x_2 = 0$ e $x_1 = t$ con $t \ge 50$, tutti i vincoli sono soddisfatti: il vincolo contrattuale diventa $0 \ge \tfrac13 t(100-2t)$, vero perché $t(100-2t) \le 0$, e il pubblico raggiunto è $100,000,t \ge 3,000,000$. Intanto il costo $t(100 - 2t)$ tende a $-\infty$. Il modello privo del vincolo sarebbe quindi **illimitato inferiormente**: non avrebbe soluzione ottima e non rappresenterebbe il problema reale. È un buon esempio di ciò che la fase di analisi del modello deve intercettare.

### Perché il problema è diverso dal precedente

Il procedimento è stato lo stesso dell'esempio dei fertilizzanti e il risultato sembra simile, ma il problema è **molto diverso**. Svolgendo il prodotto, la funzione obiettivo contiene il termine $-2x_1^2$, quindi **non è lineare**. Lo stesso termine compare nel vincolo contrattuale, che quindi non è lineare nemmeno lui. Un problema di questo tipo si dice di **programmazione non lineare** (in questo caso continua, perché le variabili sono continue). I metodi per risolverlo sono completamente diversi da quelli per il problema precedente, e in generale la programmazione non lineare è più difficile. La divisione del corso riflette questa differenza: **prima parte, problemi lineari; seconda parte, problemi non lineari**.

> [!note] Sul termine "programmazione" "Programmazione" è un'altra traduzione poco felice, dall'inglese _mathematical programming_. In questo contesto _programming_ significa **pianificazione** e non scrittura di codice. Le dispense lo precisano esplicitamente [@roma2023, §1.5].

### Domanda: perché "$\ge$" e non "$>$"?

Uno studente ha chiesto perché scrivere $x_1 \ge 0$ invece di $x_1 > 0$, visto che un annuncio di durata nulla "non ha senso". La risposta ha due parti.

1. Dal punto di vista matematico i vincoli con disuguaglianza **stretta** sono difficili da gestire. Le soluzioni potrebbero avvicinarsi indefinitamente a un valore senza mai raggiungerlo, come accade con un asintoto, e il minimo potrebbe non esistere.
2. In questo problema non si può escludere a priori che la soluzione abbia $x_1 = 0$, cioè che convenga fare solo annunci sul giornale. Il caso opposto, $x_2 = 0$, è invece escluso dal vincolo contrattuale. Se la soluzione può trovarsi su $x_1 = 0$, il vincolo va scritto come $x_1 \ge 0$.

Nel corso si vedranno **solo vincoli di disuguaglianza non stretta** ($\ge$, $\le$) e di uguaglianza, e questo semplifica moltissimo la situazione.

> [!example] Un esempio minimo (aggiunto per chiarire il punto 1) Il problema $\min x$ con il vincolo $x > 0$, $x \in \mathbb{R}$, non ha soluzione. Ogni punto ammissibile $x$ è battuto dal punto ammissibile $x/2$, che ha valore più basso. I valori della funzione obiettivo si avvicinano a $0$ senza mai raggiungerlo, perché $x = 0$ non è ammissibile. Con il vincolo $x \ge 0$ il minimo esiste ed è raggiunto in $x^\star = 0$.

## Nomenclatura

### Minimizzare o massimizzare è lo stesso

Nel corso ci si concentrerà sui problemi di **minimo**. È una scelta di convenienza: chi sa risolvere i problemi di minimo sa risolvere anche quelli di massimo, e viceversa. Il grafico di $-f$ è il grafico di $f$ ribaltato rispetto all'asse delle ascisse, quindi il punto più alto del grafico di $f$ su $S$ diventa il punto più basso del grafico di $-f$. Il **punto** in cui si trova l'ottimo è lo stesso; per ritrovare il **valore** del massimo basta cambiare segno al valore del minimo di $-f$:

$$ \max_{x \in S} f(x) = -\min_{x \in S} \big(-f(x)\big). $$

> [!tip] Schema da disegnare In questo punto la docente ha disegnato il grafico di una funzione $f$ di una variabile su un intervallo $S$ e il grafico di $-f$, simmetrico rispetto all'asse delle ascisse: il massimo di $f$ e il minimo di $-f$ si trovano nello stesso punto. Uno schizzo in Excalidraw rende l'idea a colpo d'occhio.

### Il problema e le sue soluzioni

Si considera d'ora in poi il problema

$$ \min_{x \in S} f(x), \qquad f : \mathbb{R}^n \to \mathbb{R}, \qquad S \subseteq \mathbb{R}^n, $$

dove $S$ si chiama **insieme ammissibile**. In generale $f$ potrebbe anche essere definita solo su un sottoinsieme di $\mathbb{R}^n$, ma tipicamente va da $\mathbb{R}^n$ in $\mathbb{R}$.

> [!important] Definizioni fondamentali
> 
> 1. Se $S = \varnothing$ il problema si dice **inammissibile**: non esiste neppure un punto che rispetti tutti i vincoli.
> 2. Se $S \neq \varnothing$, ogni $x \in S$ si dice **soluzione ammissibile**.
> 3. Se esiste $x^\star \in S$ tale che $$ f(x^\star) \le f(x) \qquad \forall, x \in S, $$ allora $x^\star$ si dice **soluzione ottima**, o **punto di minimo globale** (o **assoluto**), e $f(x^\star)$ si dice **minimo globale** (o **assoluto**), o **valore ottimo**.

Due osservazioni. La prima: può capitare di costruire un modello senza accorgersi che i vincoli sono incompatibili, cioè che non esiste nessuna produzione che li rispetti tutti; in quel caso il problema è inammissibile. La seconda: l'espressione "soluzione ammissibile" è fuorviante, perché una soluzione ammissibile **non è una soluzione del problema**. È soltanto un punto che soddisfa i vincoli. La vera soluzione è la **soluzione ottima**. La docente avverte che nel parlare chiamerà spesso $x^\star$ "minimo globale"; la nomenclatura corretta è quella riportata sopra.

> [!warning] Discrepanza tra fonti — verso della disuguaglianza La nota Obsidian _Soluzioni ammissibili_ scrive $f(x_\star) \ge f(x)\ \forall x \in S$. Per un punto di **minimo** la disuguaglianza corretta è $f(x^\star) \le f(x)$ per ogni $x \in S$: il valore in $x^\star$ non è superato da nessun altro punto ammissibile. Questa è la versione delle dispense [@roma2023, Def. 2.1.3]. La versione con "$\ge$" descrive un punto di massimo.

Concettualmente non c'è nulla di nuovo rispetto a quanto visto per le funzioni da $\mathbb{R}$ in $\mathbb{R}$. La differenza è che ora le funzioni dipendono da più variabili, per esempio $(x_1, x_2)$ oppure $(x_1, x_2, x_3, x_4)$. Con due variabili il grafico di $f$ è una superficie nello spazio, e si cerca **il punto che sta più in basso** su quella superficie, restando sopra l'insieme $S$.

> [!tip] Approfondimento — Problemi illimitati #approfondimento Le dispense introducono anche un terzo caso, non nominato esplicitamente a lezione ma utile già dalla prossima lezione. Il problema $\min_{x \in S} f(x)$ si dice **illimitato (inferiormente)** se per ogni $M > 0$ esiste un punto $x \in S$ tale che $f(x) < -M$ [@roma2023, Def. 2.1.2]. In questo caso non può esistere una soluzione ottima. È ciò che accade all'esempio della pubblicità se si dimentica il vincolo $x_1 \le 30$.

### Classificazione dei problemi

A seconda di come sono fatte la funzione obiettivo e i vincoli si parla di programmazione **lineare** o **non lineare**; a seconda delle variabili, di programmazione **continua** (variabili in $\mathbb{R}^n$) o **intera** (variabili a valori discreti). Una buona parte della ricerca operativa si occupa di programmazione intera, che è più difficile: gli insiemi discreti sono più difficili da gestire del continuo. Per affrontarla bisogna prima saper fare la programmazione continua, perché i metodi per l'intera si costruiscono su quelli per la continua.

## L'insieme ammissibile descritto da disuguaglianze

Spesso, come in tutti gli esempi visti finora, l'insieme $S$ è descritto da **disuguaglianze** date da funzioni:

$$ S = \left{ x \in \mathbb{R}^n ;\middle|; \begin{aligned} g_1(x) &\ge b_1 \ &\ ,\vdots \ g_m(x) &\ge b_m \end{aligned} \right}, \qquad g_i : \mathbb{R}^n \to \mathbb{R},\ b_i \in \mathbb{R},\ i = 1, \dots, m. $$

Negli esempi visti le funzioni $g_i$ erano lineari. Questo è il caso più facile da trattare analiticamente, ed è per questo che la maggior parte dei metodi noti lavora con insiemi descritti in questo modo. Nella seconda parte del corso si vedrà che alcuni algoritmi si possono formulare in modo più generale, ma al momento di implementarli si ricade quasi sempre in questa forma.

> [!warning] Discrepanza tra fonti — indici Nella nota Obsidian _Soluzioni ammissibili_ i vincoli sono indicati come $g_x(x) \ge b_1, \dots, g_n(x) \ge b_n$. Gli indici corretti sono $g_1, \dots, g_m$ e $b_1, \dots, b_m$: i vincoli sono $m$, mentre $n$ è il numero di variabili. È la notazione delle dispense [@roma2023, §2.2].

### Osservazione: scrivere tutto con "$\ge$" non è restrittivo

I vincoli che emergono da un problema reale possono essere di tipo "$\le$", "$\ge$" o "$=$". Scriverli tutti nella forma $g(x) \ge b$ non fa perdere generalità.

**Vincoli di tipo "$\le$".** Basta cambiare segno a entrambi i membri:

$$ 3x_1 + 7x_2 \le 3 \quad \Longleftrightarrow \quad -3x_1 - 7x_2 \ge -3 . $$

**Vincoli di uguaglianza.** Un'uguaglianza equivale a due disuguaglianze contemporanee, e quella di tipo "$\le$" si riporta a "$\ge$" cambiando segno:

$$ 8x_1 - 2x_2 = 1 \quad \Longleftrightarrow \quad \begin{cases} 8x_1 - 2x_2 \ge 1 \ 8x_1 - 2x_2 \le 1 \end{cases} \quad \Longleftrightarrow \quad \begin{cases} \phantom{-}8x_1 - 2x_2 \ge 1 \ -8x_1 + 2x_2 \ge -1 \end{cases} $$

In generale, come riassumono le dispense [@roma2023, Oss. 2.2.1]: $g(x) \le b \iff -g(x) \ge -b$ e $g(x) = b \iff \big(g(x) \ge b \text{ e } -g(x) \ge -b\big)$. Questi "trucchetti" elementari verranno usati spessissimo: a seconda del contesto converrà scrivere i vincoli come uguaglianze o come disuguaglianze.

> [!warning] Sezione ricostruita — inizio (Contenuto ricostruito per colmare una lacuna della trascrizione.) La registrazione della seconda parte della lezione inizia con l'esempio delle automobili già avviato. I contenuti di questa sezione e i dati dell'esempio successivo sono attestati dagli appunti manuali presi a lezione e dalle dispense [@roma2023, Def. 2.2.2 ed Es. 3.4.2]; l'esposizione discorsiva è ricostruita.

### Stato di un vincolo in un punto

Sia dato un vincolo $g(x) \ge b$, con $g : \mathbb{R}^n \to \mathbb{R}$, e un punto $\bar x \in \mathbb{R}^n$.

> [!important] Definizione — vincolo soddisfatto, violato, attivo, ridondante
> 
> - Il vincolo è **soddisfatto** in $\bar x$ se $g(\bar x) \ge b$.
> - Il vincolo è **violato** in $\bar x$ se $g(\bar x) < b$.
> - Il vincolo è **attivo** in $\bar x$ se $g(\bar x) = b$.
> - Il vincolo è **ridondante** se si può eliminare senza cambiare l'insieme ammissibile $S$.

Geometricamente, nel piano ($n = 2$) e con $g$ lineare, l'equazione $g(x) = b$ individua una retta che divide il piano in due semipiani: da una parte i punti in cui il vincolo è soddisfatto ($g(x) > b$), dall'altra quelli in cui è violato ($g(x) < b$). I punti in cui il vincolo è **attivo** stanno esattamente sulla retta, cioè sul **bordo** della regione ammissibile definita da quel vincolo. Un vincolo attivo è quindi soddisfatto "al limite". Negli appunti c'è uno schizzo di questa situazione: semipiano $g(x) < b$ tratteggiato, retta $g(x) = b$, semipiano $g(x) > b$.

Un esempio di vincolo ridondante compare nel problema di miscelazione risolto nella lezione 3: lì il vincolo $140x_1 \ge 70$ implica $x_1 \ge \tfrac12$, quindi il vincolo di non negatività $x_1 \ge 0$ si può eliminare senza cambiare $S$ (si veda [[Lezione 03 - Miscelazione, trasporto e risoluzione grafica]]).

### I dati dell'esempio delle automobili

Un'azienda automobilistica produce tre modelli di auto: **economica** ($E$), **normale** ($N$) e **di lusso** ($L$). Ogni auto, per essere completata, deve passare per **tre reparti** $A$, $B$ e $C$ (nelle dispense sono tre robot). La tabella riporta i **minuti** di lavorazione per auto in ciascun reparto, il profitto per auto e le **ore** di disponibilità giornaliera dei reparti:


|                 | $E$      | $N$      | $L$      |     | $\max \frac{h}{\text{giorno}}$ |
| --------------- | -------- | -------- | -------- | --- | ------------------------------ |
| $A$             | $20$     | $30$     | $62$     |     | $8$                            |
| $B$             | $31$     | $42$     | $51$     |     | $8$                            |
| $C$             | $16$     | $81$     | $10$     |     | $5$                            |
|                 |          |          |          |     |                                |
| $\text{Prezzo}$ | $1\ 000$ | $1\ 500$ | $2\ 200$ |     |                                |

Le auto di lusso non devono superare il **20%** della produzione totale; le auto economiche devono essere almeno il **40%** del totale. Si suppone di vendere tutto ciò che si produce.

> [!warning] Sezione ricostruita — fine

## Allocazione con risorse concorrenti: l'esempio delle automobili

**Variabili.** Si decide quante auto di ciascun tipo produrre al giorno:

$$ x_1, x_2, x_3 = \text{numero di auto di tipo } E, N, L \text{ prodotte al giorno}. $$

**Funzione obiettivo** (da massimizzare):

$$ 1,000,x_1 + 1,500,x_2 + 2,200,x_3 . $$

**Vincoli di disponibilità delle risorse.** Con il profilo di produzione $(x_1, x_2, x_3)$ il reparto $A$ viene usato per $20x_1 + 30x_2 + 62x_3$ minuti. Questo tempo totale deve essere al più il tempo disponibile, cioè 8 ore. Qui c'è la classica trappola delle **unità di misura**: i tempi di lavorazione sono in minuti, le disponibilità in ore. Una disuguaglianza deve confrontare grandezze nella stessa unità, quindi non si può scrivere "$\le 8$": bisogna scrivere $8 \cdot 60 = 480$ minuti. Lo stesso vale per $B$ (8 ore) e per $C$ (5 ore, cioè 300 minuti):

$$ \begin{aligned} 20x_1 + 30x_2 + 62x_3 &\le 480, \ 31x_1 + 42x_2 + 51x_3 &\le 480, \ 16x_1 + 81x_2 + 10x_3 &\le 300 . \end{aligned} $$

**Vincoli di mercato.** Sono vincoli di natura diversa, che vengono da un'analisi di mercato: le auto di lusso, per esempio, oltre una certa quantità non si vendono. Il numero di auto di lusso non deve superare il 20% del totale prodotto, e quello delle auto economiche deve esserne almeno il 40%:

$$ x_3 \le \frac{20}{100},(x_1 + x_2 + x_3), \qquad x_1 \ge \frac{40}{100},(x_1 + x_2 + x_3). $$

Portando tutte le variabili a primo membro, i vincoli di mercato si riscrivono nella forma lineare consueta: $-0.2x_1 - 0.2x_2 + 0.8x_3 \le 0$ e $0.6x_1 - 0.4x_2 - 0.4x_3 \ge 0$.

**Non negatività.** $x_1 \ge 0$, $x_2 \ge 0$, $x_3 \ge 0$.

> [!important] Modello delle automobili (risorse concorrenti) $$ \begin{aligned} \max \quad & 1000x_1 + 1500x_2 + 2200x_3 \ \text{s.t.} \quad & 20x_1 + 30x_2 + 62x_3 \le 480 \ & 31x_1 + 42x_2 + 51x_3 \le 480 \ & 16x_1 + 81x_2 + 10x_3 \le 300 \ & x_3 \le 0.2,(x_1 + x_2 + x_3) \ & x_1 \ge 0.4,(x_1 + x_2 + x_3) \ & x_1, x_2, x_3 \ge 0 \end{aligned} $$

È un problema di **programmazione lineare**, e **continua** per scelta di chi ha costruito il modello: le auto sono indivisibili e a rigore servirebbero variabili intere. Le dispense giustificano questa approssimazione [@roma2023, Oss. 3.4.3]. Con variabili continue si ottiene un problema di programmazione lineare, molto più trattabile di uno di programmazione lineare intera; l'approssimazione è tanto più accettabile quanto più i valori delle variabili sono grandi. Arrotondare la soluzione a valori interi, però, ne fa perdere in generale l'ottimalità.

Questa formulazione corrisponde ai cosiddetti **problemi di allocazione di risorse concorrenti**: per produrre un'auto bisogna usare **tutte e tre** le risorse.

## Allocazione con risorse alternative

Si cambia ora il problema. Si supponga che un'auto **non debba più passare per tutti e tre i reparti**, ma possa essere prodotta **interamente in uno qualsiasi** di essi: in $A$, oppure in $B$, oppure in $C$. Per esempio, l'auto economica potrebbe essere prodotta in tre stabilimenti diversi. Le risorse sono allora **alternative**, e bisogna decidere non solo quanto produrre di ciascun tipo, ma anche **chi produce che cosa**.

I gradi di libertà aumentano, e con essi le variabili. Bisogna specificare quante auto economiche produce $A$, quante $B$, quante $C$, e lo stesso per le normali e per le auto di lusso: invece di tre variabili ne servono **nove**. Poiché i dati sono organizzati in una tabella, conviene una notazione a due indici, $i$ per la riga e $j$ per la colonna:

$$ x_{ij} = \text{numero di auto di tipo } j \text{ prodotte dal reparto } i, \qquad i \in {A, B, C} \equiv {1, 2, 3},\ j \in {E, N, L} \equiv {1, 2, 3}. $$

La docente insiste su un punto: **quando si introducono le variabili, si dice sempre che cosa sono**. Il nome si può scegliere liberamente, ma il significato va spiegato, altrimenti il modello non si capisce.

**Funzione obiettivo.** Le auto economiche prodotte in totale sono quelle prodotte da $A$, più quelle prodotte da $B$, più quelle prodotte da $C$: $x_{11} + x_{21} + x_{31}$. Lo stesso vale per gli altri tipi:

$$ 1000,(x_{11} + x_{21} + x_{31}) + 1500,(x_{12} + x_{22} + x_{32}) + 2200,(x_{13} + x_{23} + x_{33}). $$

**Vincoli di capacità.** Il reparto $A$ può sempre lavorare al massimo 8 ore al giorno, ma ora vi si lavorano solo le auto con indice di riga $i = 1$:

$$ \begin{aligned} 20x_{11} + 30x_{12} + 62x_{13} &\le 480, \ 31x_{21} + 42x_{22} + 51x_{23} &\le 480, \ 16x_{31} + 81x_{32} + 10x_{33} &\le 300 . \end{aligned} $$

**Vincoli di mercato.** Il totale delle auto di lusso è $x_{13} + x_{23} + x_{33}$, quello delle economiche $x_{11} + x_{21} + x_{31}$, e la produzione totale è la somma di tutte le variabili:

$$ x_{13} + x_{23} + x_{33} \le \frac{20}{100} \sum_{i=1}^{3}\sum_{j=1}^{3} x_{ij}, \qquad x_{11} + x_{21} + x_{31} \ge \frac{40}{100} \sum_{i=1}^{3}\sum_{j=1}^{3} x_{ij}. $$

**Non negatività.** $x_{ij} \ge 0$ per ogni $i, j$.

Uno studente ha fatto notare la differenza con il problema dei lavoratori della prima lezione: qui si può **dividere** la produzione di un tipo di auto tra più reparti, per esempio cinque auto economiche nel reparto 1 e venti nel reparto 3. La docente ha confermato. È esattamente il significato del modello: lo stesso problema, declinato in due modi diversi.

## Il modello generale di allocazione ottima di risorse

Si generalizza ora il primo dei due casi, quello con **risorse concorrenti**, in modo da poterlo adattare a situazioni diverse. Ci sono $n$ **prodotti** $P_1, \dots, P_n$ e $m$ **risorse scarse** $R_1, \dots, R_m$. Come negli esempi, si costruisce una tabella con i prodotti sulle colonne e le risorse sulle righe:


|          | $p_1$    | $p_2$    | $\ldots$ | $p_n$    |     |       |
| -------- | -------- | -------- | -------- | -------- | --- | ----- |
| $R_1$    | $a_{11}$ | $a_{12}$ |          | $a_{1n}$ |     | $b_1$ |
| $R_2$    | $a_{21}$ | $a_{22}$ |          | $a_{2n}$ |     | $b_2$ |
| $\vdots$ |          |          |          |          |     |       |
| $R_m$    | $a_{m1}$ | $a_{m2}$ |          | $a_{mn}$ |     | $b_m$ |

dove:

- $a_{ij}$ è la **quantità di risorsa $R_i$ necessaria per un'unità di prodotto $P_j$**. A lezione la docente ha prima scritto $c_{ij}$ e poi ha chiesto di sostituirlo ovunque con $a_{ij}$, perché la lettera $c$ suggerisce un costo e qui non lo è;
- $b_i$ è la **disponibilità massima** della risorsa $R_i$;
- $c_j$ è il **profitto** per un'unità di prodotto $P_j$. Nelle dispense si chiama $c$ anche se è un profitto.

**Variabili.** $x_1, \dots, x_n$, quantità dei prodotti $P_1, \dots, P_n$ che si sceglie di produrre.

**Vincoli.** La risorsa $R_1$ viene usata per $a_{11}$ unità per ogni unità di $P_1$, $a_{12}$ per ogni unità di $P_2$, e così via. In totale se ne usano $a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n$, che non deve superare $b_1$. Lo stesso vale per tutte le risorse, e si aggiungono i vincoli di produzione (non si producono quantità negative):

$$ \begin{cases} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n \le b_1 \ a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n \le b_2 \ \qquad\vdots \ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n \le b_m \ x_j \ge 0 \quad \forall, j = 1, \dots, n \end{cases} $$

### La forma matriciale

Questa struttura ricorda quella dei sistemi lineari, che non si scrivono quasi mai per esteso: occupano molto spazio e sono poco leggibili. Si introducono allora la **matrice dei coefficienti** e i vettori delle incognite e dei termini noti:

$$ A = (a_{ij})_{\substack{i = 1, \dots, m \ j = 1, \dots, n}} \in \mathbb{R}^{m \times n}, \qquad x = \begin{pmatrix} x_1 \ \vdots \ x_n \end{pmatrix} \in \mathbb{R}^n, \qquad b = \begin{pmatrix} b_1 \ \vdots \ b_m \end{pmatrix} \in \mathbb{R}^m . $$

Un sistema lineare si scriverebbe $Ax = b$; qui invece si scrive

$$ A x \le b . $$

> [!warning] Attenzione — disuguaglianza tra vettori Si sta usando una notazione probabilmente mai vista prima: una disuguaglianza **tra vettori**. Per $u, v \in \mathbb{R}^m$, $u \le v$ significa che **ogni componente** di $u$ è minore o uguale della corrispondente componente di $v$: $$ u \le v \iff u_i \le v_i \quad \forall, i = 1, \dots, m. $$ Quindi $Ax \le b$ riassume esattamente le $m$ disuguaglianze scritte sopra, e $x \ge 0$ (dove $0$ è il vettore nullo di $\mathbb{R}^n$) riassume gli $n$ vincoli di non negatività.

L'insieme ammissibile si scrive in modo compatto:

$$ S = { x \in \mathbb{R}^n \mid A x \le b,\ x \ge 0 }. $$

**Funzione obiettivo.** Il profitto totale è prezzo per quantità per ogni prodotto, sommato su tutti i prodotti. Introducendo il vettore $c = (c_1, \dots, c_n)^T$ dei profitti:

$$ c_1x_1 + c_2x_2 + \dots + c_nx_n = \sum_{j=1}^{n} c_j x_j = c^T x, $$

dove $c^T$ indica il **trasposto** di $c$ (vettore riga), così che $c^T x$ è il prodotto scalare tra $c$ e $x$.

> [!important] Problema di allocazione ottima di risorse (risorse concorrenti) — forma generale $$ \begin{aligned} \max \quad & c^T x \ \text{s.t.} \quad & A x \le b \ & x \ge 0 \end{aligned} \qquad x \in \mathbb{R}^n $$
> 
> - $A \in \mathbb{R}^{m \times n}$: la tabella dei consumi unitari di risorse;
> - $b \in \mathbb{R}^m$: le disponibilità massime delle risorse;
> - $c \in \mathbb{R}^n$: i profitti unitari (i "prezzi").
> 
> È un problema di **programmazione lineare**: funzione obiettivo lineare, $n$ incognite, $m$ vincoli lineari di risorsa più $n$ vincoli lineari di non negatività, per un totale di $m + n$ vincoli.

La docente ha fatto notare quanto la forma compatta sia più leggibile di tutti i sistemi scritti per esteso. Inizialmente aveva scritto i vincoli con "$\ge$" e ha poi corretto alla lavagna: in un problema di allocazione di risorse i vincoli sono di tipo "$\le$", perché le risorse hanno una disponibilità **massima**.

> [!example] Esercizio lasciato a lezione — il modello generale con risorse alternative Per mancanza di tempo la docente ha lasciato come esercizio la formulazione generale del caso con **risorse alternative**, cioè il caso in cui ogni prodotto, per essere finito, richiede **una sola** delle risorse. Ecco la formulazione delle dispense [@roma2023, §3.4.1, "Formulazione 2"], da confrontare con il proprio tentativo.
> 
> - **Variabili**: $x_{ij}$ = quantità di prodotto $P_j$ fabbricata usando la risorsa $R_i$, con $i = 1, \dots, m$ e $j = 1, \dots, n$ (in totale $mn$ variabili).
> - **Funzione obiettivo** (da massimizzare): $\displaystyle \sum_{j=1}^{n} c_j \sum_{i=1}^{m} x_{ij}$.
> - **Vincoli di capacità**: per ogni risorsa entrano solo i prodotti fabbricati con quella risorsa, $$ \sum_{j=1}^{n} a_{ij}, x_{ij} \le b_i, \qquad i = 1, \dots, m. $$
> - **Non negatività**: $x_{ij} \ge 0$ per ogni $i, j$.
> 
> Le dispense osservano che la matrice dei coefficienti $(a_{ij})$ è la stessa del caso con risorse concorrenti, ma cambiano sostanzialmente le variabili. L'esempio delle automobili con nove variabili è un caso particolare di questo modello, con in più i vincoli di mercato.

## Problemi di miscelazione — impostazione

Negli ultimi minuti la docente ha introdotto un nuovo tipo di problema, i **problemi di miscelazione**, con un esempio che propone ogni anno: i succhi di frutta. In questi problemi i vincoli rappresentano tipicamente la **qualità della miscela**. Gli esempi classici vengono dall'ambito alimentare, con vincoli sulla presenza di certi nutrienti, ma in generale si produce una sostanza miscelata che deve contenere determinati componenti.

Un'industria produce succhi di frutta mescolando **polpa di frutta** e **dolcificante**. La tabella riporta il contenuto di ciascun componente per **100 grammi** di ciascuna sostanza, e il costo:

|                   | $\text{polpa}$ | $\text{dolcificante}$ |
| ----------------- | -------------- | --------------------- |
| $\text{vit C}$    | $140\text{mg}$ | $0$                   |
| $\text{sali}$     | $20\text{mg}$  | $10\text{mg}$         |
| $\text{zuccheri}$ | $25\text{g}$   | $50\text{g}$          |
|                   |                |                       |
| $\text{Costo}$    | $\text{€}4$    | $\text{€}6$           |

Il succo deve contenere **almeno** $70\ \text{mg}$ di vitamina C, **almeno** $30\ \text{mg}$ di sali minerali e **almeno** $75\ \text{g}$ di zucchero. Bisogna decidere come miscelare polpa e dolcificante per soddisfare questi vincoli **minimizzando il costo**. Secondo le dispense e gli appunti della lezione 3, i costi si intendono per ettogrammo, cioè per 100 g.

La docente ha indicato le variabili e ha lasciato come esercizio la scrittura del modello, che sarebbe stato risolto nella lezione successiva con il prof. Molinari:

$$ x_1 = \text{quantità di polpa}, \qquad x_2 = \text{quantità di dolcificante}, $$

entrambe misurate in **unità di 100 grammi** (la quantità di polpa è $x_1 \cdot 100\ \text{g}$).

> [!warning] Discrepanza tra fonti — requisiti del succo La nota Obsidian _Problemi di miscelazione_ riporta i requisiti come "$\le 70$ mg di vitamina C, $\le 30$ mg di sali minerali, $\le 70$ g di zucchero". La trascrizione ("almeno 70 mg di vitamina C, 30 mg di sali minerali e 75 g di zucchero"), gli appunti scansionati e le dispense [@roma2023, Es. 3.4.12] concordano invece su **requisiti minimi**: $\ge 70$ mg, $\ge 30$ mg, $\ge 75$ g. Valgono questi ultimi. Con dei "$\le$" il problema di minimo costo avrebbe una soluzione banale: non comprare nulla.

Il modello e la sua soluzione grafica sono svolti in [[Lezione 03 - Miscelazione, trasporto e risoluzione grafica#Il modello del problema di miscelazione]].

## Riepilogo

- Per costruire un modello si determinano, nell'ordine, **variabili** (dichiarandone sempre il significato), **funzione obiettivo** e **vincoli**, facendo attenzione alle **unità di misura**.
- Il nome di un problema dipende dalla struttura delle funzioni (lineare o non lineare) e dal tipo di variabili (continue o intere). Fertilizzanti e automobili sono problemi di **programmazione lineare continua**; l'agenzia pubblicitaria è un problema di **programmazione non lineare**.
- $\max_{x\in S} f(x) = -\min_{x \in S}(-f(x))$: ci si può limitare ai problemi di minimo.
- Problema **inammissibile** se $S = \varnothing$; **soluzione ammissibile** = punto di $S$; **soluzione ottima** $x^\star$ se $f(x^\star) \le f(x)$ per ogni $x \in S$.
- Si usano solo vincoli non stretti. Ogni vincolo si può scrivere nella forma $g(x) \ge b$; un vincolo può essere soddisfatto, violato, attivo o ridondante.
- Allocazione ottima di risorse concorrenti: $\max, c^T x$ con $Ax \le b$, $x \ge 0$, dove la disuguaglianza tra vettori va intesa **componente per componente**. Con risorse alternative le variabili diventano $x_{ij}$.