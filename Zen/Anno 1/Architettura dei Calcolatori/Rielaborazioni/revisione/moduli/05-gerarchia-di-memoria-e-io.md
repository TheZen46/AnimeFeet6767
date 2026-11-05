---
corso: Architettura dei Calcolatori
modulo: 5
titolo: La gerarchia di memoria, la cache e l'input/output
programma: [ADC-05, ADC-01]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 5 · La gerarchia di memoria, la cache e l'input/output

**In questo modulo.** Si usano le prestazioni e il CPI del modulo 1 e la pipeline del modulo 4. Il processore è molto più veloce della memoria principale, e la distanza cresce da decenni. Si vede come la si colma con una gerarchia di memorie sempre più grandi e lente, che funziona grazie al principio di località. Il cuore del modulo è la cache: come si trova un dato, le funzioni di corrispondenza (diretta, associativa a insiemi, completamente associativa), la dimensione, la sostituzione, le politiche di scrittura, le cause dei miss, l'effetto sulle prestazioni, le cache a più livelli e il collegamento con la DRAM. Dopo un cenno alla memoria virtuale, l'ultima parte tratta l'input/output: bus, polling, interruzioni e DMA. Alla fine del modulo si sa scomporre un indirizzo in tag, indice e offset, simulare a mano una sequenza di accessi, dimensionare una cache e calcolare il tempo medio di accesso e il CPI con gli stalli di memoria.

> [!aggiunta] Aggiunta in revisione · fonte: slide del corso (Gerarchia di memoria, Input-Output); Patterson e Hennessy, *Struttura e progetto dei calcolatori*, edizione RISC-V, cap. 5 e 6 (ADC-05, ADC-01)
> Il modulo è scritto in revisione dal materiale del corso. Le sequenze di accessi sono simulate con `strumenti/cache.py`, i conti controllati con `strumenti/verifica_ampliamento.py`.

## 5.1 Perché una gerarchia di memoria

Le prestazioni dei processori sono cresciute per molti anni di circa il 55% all'anno, quelle della DRAM di circa il 7%: un accesso alla memoria principale costa oggi centinaia di cicli di clock. Una memoria insieme grande, veloce ed economica non esiste. Le tecnologie disponibili sono:

- **SRAM**: 6 transistor per bit, accesso intorno al nanosecondo, costosa e poco densa; è *statica*, conserva il dato finché è alimentata. Si usa per le cache.
- **DRAM**: 1 transistor e un condensatore per bit, accesso di qualche decina di nanosecondi, densa ed economica; è *dinamica*, il condensatore si scarica e il contenuto va rinfrescato periodicamente (ogni pochi millisecondi). Si usa per la memoria principale.
- **Memoria secondaria** (dischi magnetici e flash): enorme e permanente, ma con tempi da microsecondi a millisecondi.

La soluzione è una **gerarchia**: registri, cache di primo livello (L1, separate per istruzioni e dati), cache di secondo e terzo livello, memoria principale, memoria secondaria. Ogni livello è più grande, più lento e meno caro per bit del precedente, e contiene un sottoinsieme dei dati del livello sotto. Se quasi tutti gli accessi trovano il dato nei livelli alti, il sistema appare veloce quasi come il primo livello e grande come l'ultimo.

Questo funziona per il **principio di località**. **Località temporale**: un dato appena usato verrà probabilmente usato di nuovo presto (le variabili di un ciclo, le istruzioni del ciclo stesso); conviene tenere vicino al processore i dati usati di recente. **Località spaziale**: dopo un indirizzo verranno probabilmente usati quelli vicini (le istruzioni in sequenza, gli elementi di un array); conviene spostare verso l'alto interi blocchi di dati contigui.

Chi gestisce i passaggi fra i livelli: fra registri e memoria il compilatore; fra cache e memoria principale l'hardware (il controllore della cache); fra memoria principale e disco il sistema operativo, con la memoria virtuale (5.8).

## 5.2 Terminologia

Il **blocco** (o **linea**) è l'unità di informazione che si trasferisce fra due livelli. Se il dato cercato è nel livello superiore si ha un **hit**, altrimenti un **miss**, e il blocco va preso dal livello inferiore.

- **Hit rate**: frazione degli accessi che sono hit; **miss rate** $= 1 - \text{hit rate}$.
- **Hit time**: tempo per accedere al livello superiore, compreso il tempo per capire se è un hit.
- **Miss penalty**: tempo per portare il blocco dal livello inferiore, sistemarlo e consegnare il dato al processore.

Di solito l'hit time è molto minore della miss penalty, e il **tempo medio di accesso** è
$$\text{AMAT} = \text{hit time} + \text{miss rate} \times \text{miss penalty}.$$

## 5.3 La cache a corrispondenza diretta

La cache deve rispondere a due domande: il dato è presente? Se sì, dove? Nella cache **a corrispondenza diretta** (*direct mapped*) ogni blocco della memoria può stare in un solo posto:
$$\text{posizione} = (\text{indirizzo del blocco}) \bmod (\text{numero di blocchi della cache}).$$
Se il numero di blocchi è una potenza di 2, il modulo sono semplicemente i bit bassi dell'indirizzo del blocco. Molti blocchi di memoria condividono la stessa posizione: per sapere quale c'è davvero, ogni posizione conserva anche i bit alti dell'indirizzo, il **tag**, e un **bit di validità** che dice se la posizione contiene qualcosa (all'accensione sono tutte vuote).

Un indirizzo di memoria si divide così in tre campi:

| tag | indice | offset nel blocco |
|---|---|---|
| bit alti, confrontati con quelli memorizzati | sceglie la posizione | sceglie la parola e il byte |

Con blocchi di $2^m$ parole da 4 byte l'offset ha $m + 2$ bit; con $2^n$ blocchi l'indice ha $n$ bit; con indirizzi di 32 bit il tag ha $32 - n - m - 2$ bit. Una lettura usa l'indice per scegliere la posizione, confronta il tag e controlla il bit di validità: se coincidono è un hit e l'offset sceglie la parola.

La dimensione effettiva della cache comprende anche tag e bit di validità:
$$\text{bit totali} = 2^n \times (\text{bit del blocco} + \text{bit del tag} + 1).$$
Con 16 KB di dati in blocchi di 4 parole (esempio delle slide): $2^{10}$ blocchi, tag di 18 bit, $2^{10} \times (128 + 18 + 1) = 147$ Kbit, cioè circa 18,4 KB per 16 KB di dati.

**La dimensione del blocco.** Blocchi più grandi sfruttano meglio la località spaziale e riducono il miss rate, ma a parità di capacità diminuisce il numero di blocchi: oltre un certo punto i blocchi si contendono le posizioni e il miss rate risale. In più cresce la miss penalty, perché c'è più da trasferire. Per limitarla si può far ripartire il processore appena arriva la parola richiesta (*early restart*) o farla arrivare per prima (*requested word first*).

## 5.4 Le scritture

In una lettura il controllo del tag e la lettura del dato si possono fare insieme. Con le scritture bisogna decidere come tenere coerenti cache e memoria.

**Write-through.** Ogni scrittura aggiorna sia la cache sia la memoria. È semplice e la memoria è sempre aggiornata, ma ogni scrittura costerebbe un accesso alla memoria: si aggiunge un **write buffer**, una coda in cui il processore lascia le scritture e prosegue, mentre la memoria le smaltisce. Il processore si ferma solo se il buffer è pieno.

**Write-back.** Si scrive solo nella cache, e il blocco viene ricopiato in memoria quando viene sostituito. Serve un bit in più per blocco, il **dirty bit**, che dice se il blocco è stato modificato: i blocchi non modificati si possono sostituire senza riscriverli. Riduce molto il traffico verso la memoria quando un blocco viene scritto più volte, ma per un certo tempo la memoria contiene dati vecchi.

**Scrittura con miss.** Con **write allocate** si porta il blocco in cache e poi lo si scrive (di solito insieme al write-back); con **no-write allocate** si scrive direttamente nel livello inferiore senza caricare il blocco (di solito con il write-through).

**Miss in lettura.** Si ferma la pipeline, si legge il blocco dal livello inferiore (riscrivendo prima, con il write-back, il blocco sostituito se è sporco), lo si scrive in cache e si ripete l'accesso. Le cache più evolute sono **non bloccanti**: continuano a servire gli hit mentre un miss è in corso (*hit under miss*).

## 5.5 Le cause dei miss e le cache associative

I miss hanno tre cause (le "tre C"):

- **obbligatori** (*compulsory*): il primo accesso a un blocco; si riducono con blocchi più grandi;
- **di capacità**: la cache non contiene tutti i blocchi usati dal programma; si riducono con una cache più grande;
- **di conflitto**: più blocchi usati insieme vanno nella stessa posizione, anche se altrove c'è posto; si riducono aumentando l'associatività.

Per ridurre i conflitti si rende più flessibile il posizionamento dei blocchi. All'estremo opposto della corrispondenza diretta c'è la cache **completamente associativa**: un blocco può stare in qualsiasi posizione, ma per trovarlo bisogna confrontare il tag con tutti i tag della cache, con un comparatore per ogni blocco. Il compromesso è la cache **associativa a $n$ vie** (*set associative*): la cache è divisa in **insiemi** di $n$ blocchi; un blocco va in un insieme preciso,
$$\text{insieme} = (\text{indirizzo del blocco}) \bmod (\text{numero di insiemi}),$$
ma al suo interno in una qualsiasi delle $n$ vie. L'indice sceglie l'insieme, e si confrontano in parallelo gli $n$ tag. A parità di capacità, raddoppiando le vie si dimezza il numero di insiemi: l'indice perde un bit e il tag ne guadagna uno. La corrispondenza diretta è il caso a una via, la completamente associativa quello con un solo insieme.

Il prezzo dell'associatività: $n$ comparatori, un multiplexer per scegliere la via (più ritardo sull'hit time), e una politica di **sostituzione** quando l'insieme è pieno. La più usata è **LRU** (*least recently used*): si sostituisce il blocco non usato da più tempo. Per due vie basta un bit per insieme; con più vie l'LRU esatto è costoso e si usano approssimazioni (come NRU, *not recently used*) o una scelta casuale.

## 5.6 Le prestazioni della cache

Gli stalli dovuti alla memoria si aggiungono al CPI della pipeline:
$$\text{CPI} = \text{CPI}_{base} + \frac{\text{accessi}}{\text{istruzione}} \times \text{miss rate} \times \text{miss penalty},$$
separando di solito le istruzioni (un accesso per istruzione) dai dati (un accesso per ogni `lw` o `sw`). Due osservazioni importanti. Se il processore diventa più veloce, la miss penalty *in cicli* cresce, perché la memoria non accelera: il peso degli stalli aumenta (guidato 3). E ridurre il CPI di base serve sempre meno, perché la parte dovuta ai miss resta.

**Cache a più livelli.** Una cache di secondo livello (L2), più grande e più lenta della L1 ma molto più veloce della memoria, riduce la miss penalty della L1: un miss in L1 che trova il dato in L2 costa poche decine di cicli invece di centinaia. I due livelli hanno obiettivi diversi: la L1 deve avere un hit time minimo (è piccola, spesso a poche vie), la L2 un miss rate basso (è grande, più associativa, con blocchi più grandi). Si distingue il miss rate **locale** della L2 (miss della L2 diviso accessi alla L2, che sono solo i miss della L1) da quello **globale** (miss della L2 diviso tutti gli accessi): il locale è molto più alto del globale, perché alla L2 arrivano solo gli accessi "difficili". Con due livelli
$$\text{AMAT} = \text{hit time}_{L1} + \text{miss rate}_{L1} \times (\text{hit time}_{L2} + \text{miss rate locale}_{L2} \times \text{miss penalty}_{L2}).$$

**Il software.** Le prestazioni della cache dipendono anche da come il programma accede ai dati: scorrere una matrice per righe (come è memorizzata in C) sfrutta la località spaziale, scorrerla per colonne no. Gli algoritmi possono essere riorganizzati a blocchi (*blocking*) per riusare i dati finché sono in cache.

## 5.7 Cache e DRAM

La miss penalty dipende da come la cache è collegata alla DRAM. In una DRAM l'indirizzo si dà in due parti: prima la riga (segnale RAS), che viene copiata in un buffer, poi la colonna (CAS); parole successive della stessa riga si leggono molto più in fretta della prima. Le SDRAM sono sincrone con il bus; le DDR trasferiscono un dato su entrambi i fronti del clock, e le generazioni successive (DDR2, DDR3, DDR4) aumentano la velocità di trasferimento e il prefetch interno, abbassando la tensione.

Il modello delle slide per un blocco di più parole su un bus largo una parola: 1 ciclo di bus per mandare l'indirizzo, un certo numero di cicli per ogni accesso alla DRAM, 1 ciclo per trasferire una parola (il trasferimento di una parola si sovrappone alla lettura della successiva, tranne l'ultimo). Si confrontano tre organizzazioni:

- ogni parola richiede un accesso completo alla DRAM;
- le parole del blocco stanno nella stessa riga, e dopo la prima basta l'accesso di colonna, più breve;
- la memoria è **interallacciata** (*interleaved*) in banchi: le parole del blocco stanno in banchi diversi, letti in parallelo, e poi trasferite una per ciclo.

La **larghezza di banda** è il numero di byte trasferiti per ciclo di bus durante un miss. L'esercizio 6 fa i conti: lo scopo è scegliere DRAM e bus adatti alla dimensione dei blocchi della cache.

## 5.8 Un cenno alla memoria virtuale

Fra memoria principale e disco la gerarchia è gestita dal sistema operativo con la **memoria virtuale**. Ogni programma usa indirizzi **virtuali**, divisi in pagine (tipicamente di 4 KB); il sistema operativo decide in quale pagina **fisica** della memoria principale sta ogni pagina virtuale, oppure se è sul disco. L'indirizzo virtuale si divide in numero di pagina virtuale e offset nella pagina; la traduzione sostituisce il numero di pagina virtuale con quello fisico, usando la **tabella delle pagine** del processo. Se la pagina non è in memoria si ha un **page fault**, un'eccezione gestita dal sistema operativo, che la carica dal disco: costa milioni di cicli, per questo la corrispondenza è completamente associativa, la sostituzione approssima LRU e la scrittura è sempre write-back. La memoria virtuale serve anche a proteggere i processi uno dall'altro, perché ciascuno vede solo le sue pagine: è la virtualizzazione del modulo 1 applicata alla memoria.

Per non leggere la tabella delle pagine in memoria a ogni accesso, il processore tiene le traduzioni recenti in una piccola cache, il **TLB** (*translation lookaside buffer*), che nella figura della gerarchia delle slide compare accanto alle cache L1 (ITLB e DTLB).

## 5.9 L'input/output

I dispositivi di I/O sono molto diversi per comportamento (ingresso, uscita, memorizzazione), per interlocutore (una persona o una macchina) e per velocità: fra una tastiera e una scheda di rete ci sono circa otto ordini di grandezza. Le misure di prestazione sono il **throughput** (quanti dati o quante operazioni per unità di tempo) e il **tempo di risposta** (la latenza di una singola operazione, decisiva nei sistemi in tempo reale).

**I bus.** Un bus è un collegamento condiviso fra più sottosistemi. È versatile ed economico, ma è un collo di bottiglia, e la sua velocità è limitata dalla lunghezza e dal numero di dispositivi. Si distinguono il bus processore-memoria (corto, veloce, proprietario), i bus di I/O (lunghi, più lenti, standard, come USB e SATA) e i bus di collegamento (*backplane*, come PCI Express). Un bus **sincrono** ha un clock fra le linee di controllo e un protocollo fisso rispetto al clock: poca logica e alta velocità, ma tutti i dispositivi devono seguire lo stesso clock e il bus deve essere corto per evitare lo sfasamento del clock (*clock skew*). Un bus **asincrono** non ha clock e usa un protocollo di **handshaking** con linee di controllo apposite (richiesta, conferma, dato pronto): si adatta a dispositivi di velocità diverse ed è più lento. La tendenza è passare da bus paralleli e larghi a collegamenti seriali punto a punto molto veloci (SATA al posto di ATA parallelo, PCIe al posto di PCI).

**Comandare i dispositivi.** Il processore comunica con un dispositivo attraverso i suoi registri (di stato, di controllo, dei dati), con istruzioni speciali di I/O oppure, come in RISC-V, con l'**I/O mappato in memoria**: a ogni dispositivo è assegnata una zona dello spazio degli indirizzi, e `lw` e `sw` su quegli indirizzi diventano letture e comandi per il dispositivo. Il sistema operativo fa da intermediario, perché i dispositivi sono condivisi fra i programmi e vanno protetti.

**Sapere quando il dispositivo è pronto.** Ci sono tre modi.

- **Polling**: il processore legge periodicamente il registro di stato del dispositivo. È semplice e il processore ha tutto sotto controllo, ma spreca cicli quando il dispositivo è lento o inattivo.
- **Interruzioni**: è il dispositivo a segnalare con un'interruzione che ha bisogno di attenzione. L'interruzione è asincrona rispetto alle istruzioni; il processore la serve fra un'istruzione e l'altra, come un'eccezione (4.7). Servono un modo per identificare il dispositivo e dei livelli di priorità: il gestore maschera le interruzioni di priorità uguale o minore, salva lo stato, riabilita quelle più urgenti e alla fine ripristina tutto.
- **DMA** (*direct memory access*): per i dispositivi veloci, come i dischi, anche un'interruzione per ogni parola costerebbe troppo. Il processore programma il controllore DMA (indirizzo del dispositivo, operazione, indirizzo in memoria, numero di byte), il controllore trasferisce da solo l'intero blocco contendendosi il bus con il processore, e alla fine manda una sola interruzione.

Con la DMA nascono due problemi. **Dati vecchi**: se un blocco di memoria è anche in cache, un ingresso DMA aggiorna la memoria ma non la cache, e con una cache write-back un'uscita DMA può leggere dalla memoria dati non ancora riscritti. Si risolve facendo passare l'I/O dalla cache (costoso), facendo invalidare o riscrivere dal sistema operativo i blocchi interessati (*cache flush*), o con hardware che invalida selettivamente i blocchi (*snooping*). **Memoria virtuale**: se la DMA usa indirizzi fisici, un trasferimento non deve attraversare il confine di una pagina, perché pagine virtuali consecutive possono non essere consecutive in memoria fisica; se usa indirizzi virtuali, il controllore deve tradurli. In entrambi i casi il sistema operativo non deve spostare le pagine coinvolte durante il trasferimento.

## Esempi ed esercizi svolti

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi sul modello delle slide (Gerarchia di memoria, Input-Output); sequenze simulate con `strumenti/cache.py`, conti controllati con `strumenti/verifica_ampliamento.py` (ADC-05)

**Esercizio 1. Dimensionare una cache.** Indirizzi di 32 bit, 64 KB di dati, blocchi di 32 byte. Campi dell'indirizzo e bit totali, a corrispondenza diretta e a 4 vie.

Blocchi: $64\,\text{KB} / 32\,\text{B} = 2048 = 2^{11}$. Offset: 5 bit. *Diretta*: indice 11 bit, tag $32 - 11 - 5 = 16$ bit. Ogni blocco ha $256$ bit di dati, 16 di tag e 1 di validità: $2^{11} \times 273 = 559\,104$ bit, cioè $68{,}25$ KB (il 6,6% in più dei dati). *4 vie*: $2048 / 4 = 512 = 2^9$ insiemi, indice 9 bit, tag 18 bit; $2^{11} \times 275 = 563\,200$ bit, più i bit per l'LRU. Più vie, più bit di tag e più comparatori (4 invece di 1).

**Esercizio 2. Una sequenza di accessi in tre cache.** Cache di 8 blocchi da una parola. Indirizzi in byte: 0, 8, 32, 0, 40, 8, 64, 32. Hit e miss con corrispondenza diretta, a 2 vie (LRU) e completamente associativa (LRU).

Gli indirizzi delle parole sono 0, 2, 8, 0, 10, 2, 16, 8.

*Diretta* (posizione = parola mod 8): 0, 2, 0, 0, 2, 2, 0, 0. Le parole 0, 8 e 16 si contendono la posizione 0, le parole 2 e 10 la posizione 2: ogni accesso caccia il blocco che servirà dopo. Otto miss, nessun hit.

*2 vie, 4 insiemi* (insieme = parola mod 4): tutte le parole vanno negli insiemi 0 e 2.

| Accesso | 0 | 8 | 32 | 0 | 40 | 8 | 64 | 32 |
|---|---|---|---|---|---|---|---|---|
| Insieme | 0 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| Esito | M | M | M | H | M | H | M | M |
| Insieme 0 dopo | 0 | 0 | 0, 32 | 32, 0 | 32, 0 | 32, 0 | 0, 64 | 64, 32 |

(nell'ultima riga il blocco più recente è a destra). L'accesso a 64 sostituisce 32, il meno usato di recente, che serve subito dopo: due hit.

*Completamente associativa*: gli indirizzi diversi sono 5 e la cache ne contiene 8, quindi gli unici miss sono i 5 obbligatori: tre hit (il secondo 0, il secondo 8, il secondo 32).

*Classificazione*: nella cache diretta 5 miss sono obbligatori e 3 di conflitto; nessuno è di capacità, perché la cache completamente associativa della stessa dimensione non li ha.

**Esercizio 3. La località spaziale.** Cache diretta di 4 blocchi da 16 byte; un programma legge in ordine le 16 parole di un array che parte dall'indirizzo 0.

Ogni blocco contiene 4 parole. La prima lettura di ogni blocco è un miss, le altre tre sono hit: M H H H M H H H … , 4 miss e 12 hit, hit rate del 75%. Con blocchi di una parola sarebbero 16 miss.

**Esercizio 4. Tempo medio di accesso con uno e due livelli.** L1: hit time 1 ciclo, miss rate 5%; memoria: 100 cicli. Poi si aggiunge una L2 con hit time 10 cicli e miss rate locale del 40%.

Un livello: $\text{AMAT} = 1 + 0{,}05 \times 100 = 6$ cicli. Due livelli: la miss penalty della L1 diventa $10 + 0{,}4 \times 100 = 50$ cicli, e $\text{AMAT} = 1 + 0{,}05 \times 50 = 3{,}5$ cicli. Il miss rate globale della L2 è $0{,}05 \times 0{,}4 = 2\%$.

**Esercizio 5. Il CPI con gli stalli di memoria.** CPI di base 1,5; miss rate della cache istruzioni 2%, della cache dati 5%; il 30% delle istruzioni sono `lw` o `sw`; miss penalty 120 cicli. Poi si aggiunge una L2 con hit time 20 cicli e miss rate globale dell'1% (per istruzioni e dati).

Senza L2: stalli per istruzione $0{,}02 \times 120 + 0{,}3 \times 0{,}05 \times 120 = 2{,}4 + 1{,}8 = 4{,}2$, e $\text{CPI} = 5{,}7$. Il processore passa quasi tre quarti del tempo ad aspettare la memoria. Con la L2: ogni miss della L1 costa 20 cicli, e quelli che mancano anche la L2 altri 120:
$$\text{CPI} = 1{,}5 + (0{,}02 + 0{,}3 \times 0{,}05) \times 20 + (0{,}01 + 0{,}3 \times 0{,}01) \times 120 = 1{,}5 + 0{,}7 + 1{,}56 = 3{,}76.$$
L'accelerazione dovuta alla L2 è $5{,}7 / 3{,}76 \approx 1{,}52$.

**Esercizio 6. La miss penalty e la DRAM.** Blocchi di 8 parole, bus largo una parola: 1 ciclo per l'indirizzo, 25 cicli per un accesso alla DRAM, 6 cicli per le parole successive nella stessa riga, 1 ciclo per trasferire una parola.

(a) Ogni parola con un accesso completo: $1 + 8 \times 25 + 1 = 202$ cicli; banda $32/202 \approx 0{,}16$ byte per ciclo. (b) Parole nella stessa riga: $1 + 25 + 7 \times 6 + 1 = 69$ cicli; banda $32/69 \approx 0{,}46$. (c) Memoria interallacciata in 8 banchi: $1 + 25 + 8 \times 1 = 34$ cicli; banda $32/34 \approx 0{,}94$. L'interallacciamento divide la miss penalty per sei.

**Esercizio 7. Write-through o write-back?** Un ciclo esegue 100 volte `sw` sulla stessa parola, poi il blocco viene sostituito. Quante scritture arrivano alla memoria?

Con il write-through ogni `sw` scrive anche in memoria: 100 scritture di una parola (smaltite dal write buffer, se tiene il passo). Con il write-back le 100 scritture restano in cache e il blocco, sporco, viene riscritto una sola volta alla sostituzione. Al contrario, per dati scritti una sola volta e mai riletti il write-back non risparmia nulla.

**Esercizio 8. Indirizzi virtuali.** Indirizzi virtuali di 32 bit, pagine di 4 KB, voci della tabella delle pagine di 4 byte. Quanto è grande la tabella di un processo?

Offset: $4\,\text{KB} = 2^{12}$, 12 bit. Numero di pagina virtuale: 20 bit, cioè $2^{20}$ pagine. Tabella: $2^{20} \times 4\,\text{B} = 4$ MB per processo; è per questo che nei sistemi reali le tabelle sono a più livelli e si caricano solo le parti usate.

**Esercizio 9. Il costo del polling e della DMA.** Processore a 1 GHz; ogni interrogazione costa 400 cicli. (a) Un mouse interrogato 30 volte al secondo. (b) Un disco che trasferisce 4 MB/s a blocchi di 16 byte, interrogato ogni volta che può avere un dato. (c) Lo stesso disco con DMA a blocchi di 16 KB, con 1000 cicli per programmare il trasferimento e 500 per l'interruzione finale (1 MB = $10^6$ byte, 1 KB = $10^3$ byte).

(a) $30 \times 400 = 12\,000$ cicli al secondo: lo $0{,}0012\%$ del processore, trascurabile. (b) $4 \cdot 10^6 / 16 = 250\,000$ interrogazioni al secondo, $250\,000 \times 400 = 10^8$ cicli: il 10% del processore, solo per il disco. (c) $4 \cdot 10^6 / 16\,000 = 250$ trasferimenti al secondo, $250 \times 1500 = 375\,000$ cicli: lo $0{,}0375\%$.

## Esercizi guidati

> [!aggiunta] Aggiunta in revisione · fonte: esercizi nuovi; soluzioni controllate con `strumenti/cache.py` e `strumenti/verifica_ampliamento.py` (ADC-05)
> Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Da un indirizzo ai campi.** Nella cache diretta dell'esercizio 1, dove va l'indirizzo `0x1234ABCD`?

*Passo 1: i campi.* Tag 16 bit, indice 11, offset 5.

*Passo 2: in binario la parte bassa.* $\texttt{0xABCD} = 1010\,1011\,1100\,1101$.

*Passo 3: offset.* I 5 bit bassi, $01101 = 13$: è il byte 1 della parola 3 del blocco.

*Passo 4: indice.* I bit da 5 a 15, $10101011110_2 = 1374$ (`0x55E`).

*Passo 5: tag.* I 16 bit alti, `0x1234`. Il controllore guarda la posizione 1374, controlla il bit di validità e confronta il tag memorizzato con `0x1234`.

**Guidato 2. La stessa cache con blocchi più grandi.** Cache diretta da 32 byte. Accessi (indirizzi in byte): 0, 4, 16, 64, 68, 0, 20. Blocchi da 4 byte (8 blocchi) o da 16 byte (2 blocchi)?

*Passo 1: blocchi da 4 byte.* Parole 0, 1, 4, 16, 17, 0, 5; posizioni (mod 8) 0, 1, 4, 0, 1, 0, 5. Il 64 caccia lo 0, il 68 caccia il 4, il secondo 0 caccia il 64: tutti miss, 7 su 7.

*Passo 2: blocchi da 16 byte.* Blocchi di memoria 0, 0, 1, 4, 4, 0, 1; posizioni (mod 2) 0, 0, 1, 0, 0, 0, 1. Esiti: M, H (stesso blocco), M, M (il blocco 4 caccia lo 0), H, M (lo 0 caccia il 4), H (il blocco 1 è ancora lì). 4 miss e 3 hit.

*Passo 3: la morale.* Con blocchi più grandi la località spaziale (0 e 4, 64 e 68, 16 e 20) diventa hit; ma con soli 2 blocchi i conflitti fra 0 e 64 restano.

**Guidato 3. Un processore più veloce con la stessa memoria.** Il processore dell'esercizio 5 (senza L2) raddoppia la frequenza di clock; la memoria resta uguale. Di quanto migliora?

*Passo 1: la miss penalty in cicli.* La memoria impiega lo stesso tempo, quindi i cicli raddoppiano: 240.

*Passo 2: il nuovo CPI.* $1{,}5 + (0{,}02 + 0{,}3 \times 0{,}05) \times 240 = 1{,}5 + 8{,}4 = 9{,}9$.

*Passo 3: il confronto.* Tempo per istruzione: prima $5{,}7\,T$, ora $9{,}9 \times T/2 = 4{,}95\,T$. L'accelerazione è $5{,}7/4{,}95 \approx 1{,}15$, non 2: è la legge di Amdahl, perché la parte dovuta alla memoria non è accelerata.

## Riepilogo

La gerarchia di memoria sfrutta la località temporale e spaziale per dare l'illusione di una memoria grande come l'ultimo livello e veloce quasi come il primo: SRAM per le cache, DRAM per la memoria principale, dischi per la memoria secondaria. La cache a corrispondenza diretta mette ogni blocco in una sola posizione, data dall'indice; tag e bit di validità dicono se il blocco è presente. Le scritture si gestiscono con write-through e write buffer, o con write-back e dirty bit; nei miss in scrittura si sceglie fra write allocate e no-write allocate. I miss sono obbligatori, di capacità o di conflitto; i conflitti si riducono con le cache associative a $n$ vie, che richiedono più comparatori e una politica di sostituzione come LRU. Le prestazioni si misurano con il tempo medio di accesso e con gli stalli aggiunti al CPI; le cache a più livelli riducono la miss penalty, e l'organizzazione della DRAM e del bus (stessa riga, interallacciamento) la banda. La memoria virtuale traduce gli indirizzi a pagine con la tabella delle pagine e il TLB. L'I/O usa bus sincroni o asincroni, I/O mappato in memoria, polling, interruzioni e DMA, con i problemi di coerenza fra DMA e cache.

## Formulario

> [!aggiunta] Aggiunta in revisione · fonte: sintesi del modulo (ADC-05)

### Indirizzi e dimensioni

$$\text{offset} = \log_2(\text{byte per blocco}), \quad \text{indice} = \log_2(\text{insiemi}), \quad \text{tag} = 32 - \text{indice} - \text{offset}, \quad \text{insiemi} = \frac{\text{blocchi}}{\text{vie}}.$$

$$\text{posizione} = \text{blocco} \bmod \text{insiemi}, \qquad \text{bit totali} = \text{blocchi} \times (\text{bit del blocco} + \text{tag} + 1\ [+ 1\ \text{dirty}]).$$

### Prestazioni

$$\text{AMAT} = t_{hit} + m \cdot P, \qquad \text{AMAT}_2 = t_{L1} + m_{L1}(t_{L2} + m_{L2,loc} P_{mem}), \qquad m_{L2,glob} = m_{L1} \cdot m_{L2,loc}.$$

$$\text{CPI} = \text{CPI}_{base} + m_I \cdot P + f_{ld/st} \cdot m_D \cdot P.$$

Miss penalty con bus da una parola e blocchi di $k$ parole: $1 + k \cdot t_{DRAM} + 1$; stessa riga: $1 + t_{DRAM} + (k - 1) t_{col} + 1$; $k$ banchi: $1 + t_{DRAM} + k$. Banda = byte del blocco / miss penalty.

### Politiche

| Scelta | Opzioni |
|---|---|
| Posizionamento | diretta, $n$ vie, completamente associativa |
| Sostituzione | LRU, NRU, casuale |
| Scrittura (hit) | write-through (+ write buffer), write-back (+ dirty bit) |
| Scrittura (miss) | write allocate, no-write allocate |
| Miss | obbligatori, di capacità, di conflitto |
| I/O | polling, interruzioni, DMA |

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Località temporale, spaziale | riuso dello stesso dato; uso dei dati vicini |
| Blocco (linea) | unità di trasferimento fra due livelli |
| Hit time, miss penalty | tempo di un hit; costo di un miss |
| Tag, indice, offset | bit alti di confronto; posizione; parola e byte nel blocco |
| Bit di validità, dirty bit | posizione piena; blocco modificato |
| Write buffer | coda delle scritture verso la memoria |
| Miss rate locale, globale | rispetto agli accessi al livello; rispetto a tutti |
| Interallacciamento | parole consecutive in banchi diversi |
| TLB | cache delle traduzioni degli indirizzi |
| I/O mappato in memoria | registri dei dispositivi come indirizzi di memoria |
| DMA | trasferimento di blocchi senza il processore |
| Snooping | controllore che osserva il bus e invalida i blocchi |

### Domande che tornano spesso

- Perché serve una gerarchia di memoria e perché funziona? SRAM e DRAM.
- Come si trova un dato in una cache diretta, associativa a insiemi e completamente associativa? Calcolo di tag, indice e offset.
- Politiche di scrittura e di sostituzione; le tre cause dei miss.
- Formula dell'AMAT e del CPI con gli stalli; perché le cache a più livelli?
- Come si riduce la miss penalty con l'organizzazione della DRAM?
- Polling, interruzioni e DMA; i problemi della DMA con cache e memoria virtuale.
