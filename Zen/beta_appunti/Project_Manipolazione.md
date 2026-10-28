---
titolo: "Manipolazione ed esfiltrazione da sistemi elettronici isolati"
sottotitolo: "Canali fisici, capacità offensive duali e difesa delle infrastrutture — una trattazione teorico-pratica"
autore: "Mobius"
data: "2026-10-28"
tipo: "Tesi / monografia di ricerca"
ambito: "Hardware security · side-channel analysis · critical infrastructure protection"
---

# Nota su ambito ed etica (leggere prima)

Questo documento è una **tesi di ricerca a scopo di studio e difesa**. Tratta un campo accademico consolidato — *hardware security* e *side-channel analysis* — con decenni di letteratura peer-reviewed e conferenze dedicate (IACR CHES, USENIX Security, IEEE S&P, FDTC). L'obiettivo è duplice: comprendere *perché* certi fenomeni che sembrano fantascienza sono fisicamente reali, e capire *come se ne proteggono* sistemi e infrastrutture.

**Cosa il documento contiene:** la fisica dei fenomeni, i modelli di guasto e di fuga d'informazione, le *categorie* di capacità offensive, l'analisi del mercato e della governance (controlli all'export), e un trattamento esteso della difesa.

**Cosa il documento NON contiene, per scelta:** parametri operativi (timing e tensioni di glitch, mappe di sonde, frequenze di sintonia, potenze), payload o procedure contro sistemi reali, guide costruttive di armi o strumenti di spionaggio. Questa non è una limitazione alla profondità intellettuale: la sostanza di questo campo sta nella fisica e nei modelli, non nel *tuning* operativo. Dove finisce la ricerca e inizia il danno concreto, il testo si ferma al "come e perché funziona".

Il framing "uso militare / spionaggio / vendita agli stati" è affrontato come **analisi di un panorama documentato** (mercato dell'intercettazione, industria dello spyware commerciale, armi a energia diretta) e del suo quadro normativo — non come progettazione di prodotti. È esattamente il tipo di analisi che si trova in rapporti di policy (Carnegie, Atlantic Council) e in letteratura di security studies.

---

# 1. Introduzione

## 1.1 La tesi centrale: "isolato" non significa "silenzioso"

Il senso comune assume che un dispositivo privo di scheda di rete, o posto su un circuito chiuso ("air-gapped"), sia per ciò stesso inattaccabile a distanza. Questa tesi parte dalla confutazione di quell'assunto, su base fisica.

Il punto è semplice e profondo: **ogni computazione è anche un evento fisico**. Spostare elettroni dentro un chip significa far scorrere correnti, caricare e scaricare capacità parassite, dissipare calore, far vibrare materiali piezoelettrici e magnetici. Tutti questi fenomeni sono *correlati ai dati elaborati*, e nessuno di essi rispetta il confine logico della "rete". Un sistema isolato non comunica di proposito, ma continua a *trasudare* informazione — e, specularmente, può essere *perturbato* dall'esterno — attraverso canali fisici non previsti dal progettista.

Da qui l'intero campo si organizza in due famiglie speculari:

- **Side-channel passivi** — *leggere* ciò che il dispositivo lascia trapelare senza volerlo.
- **Fault injection attivi** — *iniettare* un disturbo fisico per indurre un errore mirato.

A queste si aggiunge una terza superficie, spesso sottovalutata, che è la più vicina al "potere a distanza" dell'immaginario: l'**attacco ai sensori**, in cui non si colpisce il calcolatore ma l'organo di senso di cui esso si fida ciecamente.

## 1.2 Perché il tema sembra fantascienza (e dove lo è davvero)

L'immaginario — un operatore che con un gesto piega a sé l'elettronica circostante, accende e spegne lampioni, manipola la rete elettrica via etere — è fantascienza nella sua forma "a gesto e a distanza illimitata". Ma poggia su un nucleo scientifico reale. Questa tesi mantiene costantemente la distinzione tra:

1. ciò che è **fisicamente dimostrato** in laboratorio (gran parte dei side-channel e del fault injection);
2. ciò che è **reale ma vincolato** da potenze, prossimità e indiscriminatezza (le armi elettromagnetiche);
3. ciò che è **networking travestito da magia** (la compromissione di reti IoT e sistemi di controllo);
4. ciò che **non esiste** in forma portatile (piegare "quel" dispositivo via etere con eleganza).

## 1.3 Il principio fisico unificante

Il meccanismo di accoppiamento è, in larghissima parte, **l'induzione elettromagnetica**: una corrente variabile genera un campo (Ampère-Maxwell); un campo variabile induce una tensione in un conduttore vicino (Faraday). Prossimità, frequenza e risonanza determinano quanta energia o informazione attraversa il "vuoto" apparente. È la stessa fisica di RFID, ricarica wireless e interferenza EMI — qui usata in senso avversariale. Gli altri canali (acustico, termico, ottico) sono varianti dello stesso principio generale: *una grandezza fisica osservabile o perturbabile correla con lo stato interno del sistema*.

---

# 2. Fondamenti teorici

## 2.1 Correlazione dato–fenomeno fisico

In logica CMOS, la commutazione di un transistor dissipa energia prevalentemente in modo dinamico (carica/scarica di capacità). Il consumo istantaneo dipende da *quanti e quali* bit commutano: in prima approssimazione è funzione del **peso di Hamming** del dato manipolato e della **distanza di Hamming** tra stati successivi di un registro. Ne segue il teorema operativo di tutto il side-channel: *se una grandezza fisica è funzione (anche rumorosa) di un valore intermedio segreto, l'osservazione di quella grandezza riduce l'entropia del segreto*. La crittanalisi a canale laterale è, a questo livello, un problema di stima statistica.

## 2.2 I margini e la loro violazione

Un circuito digitale è sincrono e opera entro margini: tensione di alimentazione, periodo di clock, temperatura, integrità del segnale. Il corretto campionamento di un flip-flop richiede che l'ingresso sia stabile per un tempo di *setup* prima del fronte di clock. Se si viola transitoriamente un margine — un abbassamento di tensione, un fronte di clock anticipato, un impulso EM che induce correnti spurie — il dato non si stabilizza in tempo: un bit viene campionato errato, un'istruzione corrotta. Questo è il fondamento del fault injection: **spingere il sistema fuori dall'inviluppo operativo per un istante preciso**, dove "preciso" significa sia nel tempo (quale ciclo) sia nello spazio (quale area del die).

## 2.3 I "modelli di guasto" (fault models)

La ricerca ha formalizzato gli effetti riproducibili di una perturbazione su un microcontrollore. I due modelli classici, verificati empiricamente, sono:

- **Instruction skip** — un'istruzione viene saltata (il *fetch* o la *decode* falliscono). Se l'istruzione saltata è un controllo di sicurezza (una verifica di password, un confronto di firma, il salto condizionato che nega l'accesso), l'effetto può essere il bypass del controllo.
- **Instruction replacement / data corruption** — l'opcode o l'operando vengono alterati, con effetti dipendenti dall'architettura.

Lavori su architetture ARMv7-M mostrano che perturbare la *cache delle istruzioni* produce un modello di guasto ad alta occorrenza e riproducibile, descrivibile proprio come sostituzione/salto di istruzione, e che ciò apre attacchi al *control flow*. Questa formalizzazione è ciò che trasforma il fault injection da "far rompere il chip" a **ingegneria dell'errore mirato**.

## 2.4 Dal guasto al segreto: la crittanalisi differenziale dei guasti

Il ponte teorico tra "indurre un errore" ed "estrarre una chiave" è la **Differential Fault Analysis (DFA)** (Biham & Shamir, 1997; Boneh, DeMillo & Lipton su RSA, 1997). L'idea: si fa calcolare al dispositivo lo stesso risultato due volte, una corretta e una con un guasto in un punto noto dell'algoritmo; confrontando output corretto e guasto, le proprietà algebriche dello schema (es. la struttura dell'AES o la riduzione CRT in RSA) permettono di risalire a frammenti di chiave con complessità drasticamente ridotta rispetto alla forza bruta. È il motivo per cui *anche* un algoritmo matematicamente solido è vulnerabile nella sua *implementazione* fisica.

---

# 3. Canali laterali passivi (side-channel)

## 3.1 Emanazioni elettromagnetiche: TEMPEST e Van Eck

**Teoria.** Schermi, cavi video e CPU irradiano onde radio il cui contenuto è correlato ai bit trasmessi. Nel 1985 Wim van Eck pubblicò la dimostrazione che si poteva ricostruire a distanza l'immagine di un monitor captandone le emissioni — lavoro che portò alla luce pubblica il programma di schermatura noto come **TEMPEST**. Il principio: la trasmissione dell'immagine si basa su segnali rapidi e periodici (temporizzazione di riga e quadro) da cui, mediando nel tempo, si inferisce l'intensità dei pixel.

**Stato dell'arte.** Il passaggio da VGA analogico a HDMI aveva reso l'attacco molto più arduo, per via della codifica digitale a 10 bit (TMDS) e della banda larga. Nel 2024 il progetto **Deep-TEMPEST** (Universidad de la República, Uruguay) ha riformulato il problema come *inverse problem* e ha addestrato una rete convoluzionale profonda (architettura DRUNet) a ricostruire l'immagine dallo spettro captato, abbattendo il *Character Error Rate* sul testo di oltre 60 punti percentuali rispetto agli strumenti precedenti. Il dato impressionante: basterebbe hardware di cattura (una SDR) nel sedile posteriore di un'auto vicino a un edificio. Esistono implementazioni open (TempestSDR, gr-tempest su GNU Radio) usate anche in replica accademica (es. Comenius University, 2024/2025).

**Difesa.** Schermatura (gabbie di Faraday, cavi e stanze TEMPEST-certificate), riduzione alla sorgente ("soft TEMPEST": font e rendering che minimizzano l'emissione), e contromisure a livello contenuto suggerite dagli stessi ricercatori (cavi meglio schermati, barriere fisiche, rumore a basso livello o gradienti di colore sullo sfondo che degradano la ricostruzione).

**Categoria di strumenti.** Software-Defined Radio + toolkit di demodulazione/sincronizzazione + modello di post-processing ML.

## 3.2 Analisi dei consumi: SPA, DPA, CPA

**Teoria.** Misurando il profilo di assorbimento di corrente nel tempo si inferisce cosa calcola il chip. Con la **Simple Power Analysis (SPA)** si distinguono a occhio operazioni diverse in una singola traccia (es. le iterazioni di un'esponenziazione modulare). Con la **Differential/Correlation Power Analysis (DPA/CPA)** (Kocher, Jaffe & Jun, 1999) si applica statistica su migliaia di tracce, correlando il consumo con un modello (tipicamente il peso di Hamming di un valore intermedio predetto in funzione di un'ipotesi di sotto-chiave): la sotto-chiave corretta emerge come picco di correlazione. Variante gemella: i **timing attack** (Kocher, 1996), che sfruttano la dipendenza del tempo di esecuzione dal segreto.

**Perché è potente.** Il dispositivo non "comunica" nulla; tradisce sé stesso attraverso una grandezza (il consumo) che quasi nessun progetto non-sicurezza protegge.

**Difesa.** Due famiglie complementari: *masking* (randomizzare i valori intermedi con maschere casuali, così che il consumo non correli più col segreto non mascherato) e *hiding* (rendere il consumo uniforme o rumoroso: logiche bilanciate dual-rail, jitter temporale, esecuzione a tempo costante). È una corsa agli armamenti: a ogni contromisura corrispondono attacchi di ordine superiore (higher-order DPA) che la aggirano combinando più punti di fuga.

**Categoria di strumenti.** Oscilloscopio + sonda di corrente/shunt; in ambito didattico-ricerca la piattaforma **ChipWhisperer** (NewAE) è lo standard de facto, nata proprio per *insegnare* SCA e fault injection su bersagli di prova legittimi.

## 3.3 Canali acustici, magnetici, microarchitetturali

- **Acustico.** Il *coil whine* e le micro-vibrazioni di componenti correlano col calcolo: celebre l'estrazione di chiavi RSA via analisi acustica (Genkin, Shamir, Tromer, 2014).
- **Magnetico.** Campi magnetici a bassa frequenza dalla CPU attraversano schermature che bloccherebbero i canali radio ad alta frequenza.
- **Microarchitetturale.** **Spectre** e **Meltdown** (2018) sono side-channel temporali sulla esecuzione speculativa delle CPU moderne: puro software, nessun contatto fisico, eppure permettono di leggere memoria oltre i confini di privilegio. Dimostrano che il "canale laterale" non richiede affatto prossimità fisica quando la fuga è nel comportamento temporale del processore stesso.

Il filo rosso resta invariato: *una grandezza osservabile correla con lo stato interno*.

---

# 4. Esfiltrazione da sistemi air-gapped (covert channel)

Qui si va oltre la lettura: si tratta di **far uscire dati da un computer fisicamente scollegato**, trasformando componenti ordinari in trasmettitori. Il corpus di riferimento è quello di **Mordechai Guri** (Ben-Gurion University); la sua survey *Mind The Gap* (2024) cataloga i canali covert per mezzo fisico: elettromagnetico, elettrico, ottico, termico, acustico. Una survey indipendente (Park et al., *Sensors*, 2023) conferma la tassonomia e la contiguità concettuale con i side-channel.

**Premessa decisiva, spesso ignorata.** Tutte queste tecniche richiedono che il malware sia **già presente** nella macchina isolata (via USB, supply-chain, insider). Il covert channel è *l'ultimo miglio* dell'esfiltrazione, non il modo per *entrare*. L'air-gap resta una barriera formidabile all'ingresso; ciò che questi lavori smontano è l'idea che sia una barriera all'*uscita*.

Esempi rappresentativi (sono proof-of-concept: lenti, a corto raggio, rumorosi — dimostrano la fisica, non costituiscono armi pratiche):

| Canale | Meccanismo (principio) | Ricevitore tipico |
|---|---|---|
| **GSMem** | Modula le emissioni del bus di memoria su bande cellulari | Telefono vicino |
| **Fansmitter / DiskFiltration** | Codifica dati nel rumore acustico di ventole / attuatori HDD | Microfono |
| **LED-it-GO / CTRL-ALT-LED** | LED di HDD o tastiera come trasmettitori ottici (lampeggio impercettibile) | Fotodiodo / camera |
| **LANTENNA** | Il cavo Ethernet diventa antenna; segnali captati a distanza di metri | SDR |
| **PowerHammer** | Iniezione di segnale sulle linee di alimentazione | Sonda di corrente |
| **MAGNETO** | Campi magnetici a bassa frequenza dalla CPU; attraversa gabbie di Faraday | Magnetometro |

**Difesa.** Zone rosse prive di elettronica personale; gabbie di Faraday; *audio-gap* (nessun altoparlante/microfono); monitoraggio spettrale delle emissioni anomale; air-gap *rafforzato* con distanze fisiche minime (zone di rispetto). Il principio blue-team: *ogni canale fisico che non monitori è una porta d'uscita*.

---

# 5. Manipolazione attiva: fault injection

È la parte più vicina al "potere" dell'immaginario: **far compiere al chip un'operazione che non dovrebbe**, tramite un disturbo fisico mirato.

## 5.1 Le tecniche, dal grossolano al chirurgico

- **Voltage / clock glitching.** Si abbassa transitoriamente la tensione o si accorcia un ciclo di clock. Economico ed efficace; tipicamente usato per bypassare la *read-out protection* (RDP) di un microcontrollore e leggerne il firmware. La ricerca *Glitching in 3D* (CanSecWest 2024) ha mostrato un bypass completo della RDP su STM32F4, notando però che cali di tensione a timing specifici possono **danneggiare permanentemente** il dispositivo — un rischio reale di questa classe.
- **EMFI (Electromagnetic Fault Injection).** Un impulso EM da una sonda ravvicinata induce il guasto *senza contatto*, con risoluzione spaziale. Il problema pratico centrale è *dove* colpire: lavori recenti (Probst et al., FDTC 2024, su STM32F303) mostrano un fatto elegante — le posizioni che producono modifica dei dati coincidono quasi interamente con le aree ad **alto rapporto segnale-rumore delle emanazioni EM**. Cioè i punti da cui il chip *emette di più* (side-channel) sono anche quelli da cui è *più vulnerabile* all'iniezione (fault): una simmetria profonda tra lettura passiva e attacco attivo. Framework recenti (es. *EMMap*, 2024) sistematizzano la mappatura spaziale della suscettibilità.
- **Laser Fault Injection (LFI).** La tecnica più precisa e costosa: un laser (spesso infrarosso, dal retro del die) colpisce singoli transistor. Richiede decapsulazione del chip. Dominio dei laboratori specializzati e delle valutazioni di certificazione (smartcard, secure element).
- **Rowhammer** (Kim et al., 2014). Caso speciale e concettualmente rivoluzionario: *martellando* ripetutamente righe di DRAM **via software** si inducono bit-flip nelle righe adiacenti per diafonia elettrica. Fault injection **senza alcun hardware esterno**: dimostra che i confini passivo/attivo e hardware/software sono porosi.

## 5.2 Difesa

Ridondanza temporale e spaziale (eseguire due volte e confrontare; variabili duplicate e complementari); sensori on-die anti-glitch e anti-EM; rilevatori di tensione/clock fuori range; mesh attive sul package che rilevano la decapsulazione; *instruction stream integrity* e costrutti software *fault-tolerant* (verifiche duplicate dei salti critici, "double-check" dei confronti di sicurezza). Le smartcard e i secure element moderni integrano queste contromisure a strati, e sono valutati contro fault injection in schemi di certificazione (Common Criteria, EMVCo).

**Categoria di strumenti.** Generatori di glitch e trigger temporali (ChipWhisperer); generatori di impulsi EM open-source a basso costo (PicoEMP); posizionatori automatici — la ricerca 2024 usava una stampante 3D riadattata per muovere la sonda EM su X/Y/Z; stazioni laser nei laboratori. Bersagli: dev-board (STM32, ESP32) in ambiente di test. Si noti che questi *sono anche* gli strumenti legittimi della valutazione di sicurezza: lo stesso banco serve all'attaccante di laboratorio e al difensore che certifica un prodotto.

---

# 6. Attacco ai sensori (sensor spoofing)

Questa superficie è la risposta realistica alla domanda "posso spegnere un lampione mentre ci passo vicino?". Non si attacca il calcolatore: si **inganna l'organo di senso** di cui il sistema si fida.

## 6.1 Il principio

Un sistema di controllo (un lampione con fotocellula, un drone con IMU, un'auto con LiDAR) chiude un anello: *sensore → calcolo → attuazione*. Se il calcolo si fida acriticamente del sensore, falsificare l'ingresso fisico del sensore equivale a dettare l'uscita del sistema — **senza toccare software né rete**.

## 6.2 Esempi documentati

- **Fotocellula crepuscolare (il caso "lampione").** Molti lampioni si accendono al buio tramite un sensore di luce. Illuminarne il sensore con luce sufficiente → "crede" sia giorno → si spegne, per il tempo in cui lo si illumina. Fisica elementare, reale, usata come scherzo. È letteralmente la versione realistica del "lo spengo finché sono nella sua zona": raggio d'azione = finché il fascio colpisce il sensore; durata = finché lo si mantiene.
- **Light Commands** (Sugawara, Fu et al., 2019/2020). Un laser *modulato* puntato sul microfono MEMS di uno smart speaker inietta comandi vocali **silenziosi** a distanza: il MEMS risponde alla luce modulata come fosse suono.
- **WALNUT** (Trippel et al., 2017) e Son et al. (2015). Onde sonore alla **frequenza di risonanza** di accelerometri/giroscopi MEMS ne falsificano le letture, fino a destabilizzare un drone in volo.
- **GPS spoofing.** Segnali satellitari contraffatti, più forti di quelli autentici, inducono un ricevitore a calcolare posizione/tempo errati.

## 6.3 Rilevanza per la robotica

Questa è la famiglia di maggior interesse per un ingegnere robotico: IMU, encoder, LiDAR, camere e ricevitori GNSS sono tutti potenziali bersagli di spoofing fisico. La difesa è concettualmente ricca:

- **Sensor fusion** e ridondanza eterogenea (incrociare sensori di natura fisica diversa, così che un singolo attacco non li inganni coerentemente tutti).
- **Validazione di plausibilità** (filtri che rifiutano lett­ure fisicamente incoerenti con il modello dinamico).
- **Filtraggio** delle bande di risonanza note; smorzamento meccanico; schermatura ottica/acustica mirata.
- **Autenticazione del segnale** dove possibile (es. GNSS con firma).

---

# 7. Infrastrutture, reti ed energia: dove finisce la "magia"

Qui la distanza tra immaginario e realtà è massima, ed è il punto più istruttivo. Vanno distinte quattro vie.

## 7.1 Via A — Irradiare energia: IEMI / armi a radiofrequenza (reale ma vincolata)

Esiste un campo militare e di protezione civile serio: **IEMI** (*Intentional Electromagnetic Interference*), noto anche come "electromagnetic terrorism", e le armi a **microonde ad alta potenza (HPM)**. La letteratura è aperta e abbondante: il rapporto *Meta-R-323* di Metatech (W. Radasky, per la FERC) analizza l'impatto dell'IEMI sulla rete elettrica; progetti UE del FP7 — **STRUCTURES** e **HIPOW** — hanno studiato la protezione delle infrastrutture critiche contro attacchi HPM; esistono standard dedicati (IEC sottocomitato SC 77C su fenomeni HPEM transitori; CIGRÉ WG C4.206 sulla protezione delle sottostazioni AT).

La teoria classifica gli effetti in quattro classi: **interference, upset, deception, permanent damage** (dal disturbo reversibile fino alla distruzione dell'hardware). L'accoppiamento avviene per irradiazione diretta o per correnti indotte sulle linee (coupling to lines).

Ma i vincoli sono decisivi, e separano nettamente la realtà dall'anime:
- servono **potenze elevate e antenne grandi** per effetti a distanza utile;
- l'effetto è **indiscriminato** (colpisce tutto nel cono d'irradiazione, non "quel" dispositivo in modo selettivo);
- è **pericoloso per l'operatore** e, nelle forme ad alta potenza, ingombrante;
- *distrugge o disturba*, non "accende/spegne con eleganza".

Nulla a che vedere con un gadget in tasca. È una capacità di guerra elettronica, non un potere da netrunner. Va anche distinto l'**HEMP** (impulso elettromagnetico da detonazione nucleare in quota), fenomeno affine ma di origine e scala completamente diverse, oggetto storico delle commissioni EMP.

## 7.2 Via B — Ingannare il sensore (cfr. §6)

La via realistica per il "lampione": sensor spoofing sulla fotocellula. È qui che l'immaginario trova il suo aggancio fisico credibile.

## 7.3 Via C — Compromettere la rete di controllo (networking, non magia)

I lampioni "smart" e l'illuminazione cittadina stanno su reti mesh wireless (ZigBee, oggi spesso cellulare/LoRa/NB-IoT) o su un sistema di gestione centralizzato. Il caso-scuola è *IoT Goes Nuclear* (Ronen, O'Flynn, Shamir, Weingarten, IEEE S&P 2017): sfruttando una falla nell'implementazione del protocollo ZigBee Light Link e nel processo di aggiornamento firmware delle lampadine Philips Hue, i ricercatori mostrarono che — partendo da **una singola lampadina infetta** inserita in città — un *worm* poteva propagarsi da lampada a lampada per sola vicinanza fisica, consentendo di accendere/spegnere tutte le luci, "brickarle" permanentemente, o generare disturbo radio. La presa di controllo fu dimostrata da quasi mezzo chilometro (via drone/auto), perché ZigBee non cifrava tutto il traffico. Philips **corresse** la vulnerabilità con un aggiornamento OTA.

Due punti teorici rilevanti:
- **Soglia critica ("massa critica").** Il worm si estingue se la densità di dispositivi vulnerabili è sotto una soglia, e dilaga sopra — una dinamica epidemica (percolazione) in cui la *densità di installato* è il parametro d'ordine.
- **Attacco indiretto alla rete elettrica.** Programmando molte lampade perché commutino in sincrono, i bruschi sbalzi di consumo possono stressare la rete. Non è interferenza EM: è un **attacco di carico coordinato**, mediato dal software. È la forma realistica (e inquietante) del "manipolare la rete elettrica".

## 7.4 Via D — I sistemi industriali (la rete "vera")

Semafori, sottostazioni, impianti idrici e illuminazione di livello infrastrutturale girano su **ICS/SCADA** (protocolli Modbus, DNP3, IEC 61850), storicamente nati **senza cifratura né autenticazione**, pensati per reti fisicamente isolate e affidabili. La superficie d'attacco non è fisica-elettromagnetica: è il fatto che questi sistemi sono sempre più *connessi* e intrinsecamente fragili sul piano dell'autenticazione. Gli incidenti reali lo confermano:

- **Stuxnet** (2010): sabotaggio mirato di PLC di centrifughe, ingresso via USB in rete isolata.
- **BlackEnergy** (blackout in Ucraina, 2015): attacco informatico *classico* alla rete di controllo elettrica — non interferenza a distanza.
- **Triton/Trisis** (2017): malware contro i *safety instrumented systems* di un impianto.
- **Colonial Pipeline** (2021): ransomware sul lato IT con impatto operativo.

Tutti attacchi di cyber-intrusione, non di "etere". È la dimostrazione che, per le infrastrutture, la minaccia dominante è *software e networking*, non la fisica EM esotica.

## 7.5 Sintesi onesta del caso "lampione"

- "Lo spengo mentre passo" → **sensor spoofing** sulla fotocellula (fisica elementare; raggio = finché illumini).
- "Controllo N lampioni per N tempo" → **compromissione della rete di controllo** (problema di cybersecurity, dimostrato a scala urbana, ma richiede violare quella rete).
- "Lo piego via etere con un gesto" → **non esiste** in forma portatile; la cosa più vicina è l'IEMI, che però distrugge in modo indiscriminato e richiede mezzi ingombranti.

---

# 8. La dimensione duale: capacità, mercato, controlli

Questa sezione affronta il framing "strumenti sviluppati e venduti agli stati per fini militari e di spionaggio" come **analisi di un panorama documentato** e del suo quadro normativo — non come progettazione di prodotti.

## 8.1 La natura duale

Ogni tecnica di questa tesi è *dual-use*: lo stesso banco di fault injection certifica una smartcard *e* la attacca; la stessa SDR fa ricerca TEMPEST difensiva *e* intercettazione; lo stesso exploit serve al penetration tester *e* allo spyware. Questo è il nodo etico e regolatorio centrale: non esiste una linea tecnica netta tra offesa e difesa, solo una linea di *intento e autorizzazione*.

## 8.2 Tassonomia delle capacità come "prodotti"

A grandi linee, il panorama delle capacità vendute o acquisite dagli stati si articola in:

1. **Intercettazione e SIGINT fisico.** Ricevitori TEMPEST, apparati di intercettazione delle emanazioni, equipaggiamenti di schermatura/valutazione. Categoria storicamente governativa, con fornitori specializzati per difesa e intelligence.
2. **Guerra elettronica / energia diretta.** Sistemi IEMI/HPM come capacità militare di *disturbo/neutralizzazione* dell'elettronica avversaria (droni, elettronica di bordo). Ricercati e prodotti nel contesto della difesa, non del mercato civile.
3. **Hardware security / fault-injection lab.** Strumentazione di analisi (SCA, FI, laser) — venduta legittimamente a laboratori di certificazione e vendor, ma intrinsecamente offensiva nelle mani sbagliate.
4. **Access-as-a-Service, spyware e zero-day.** Il segmento più documentato e politicamente caldo (§8.3).

## 8.3 Il mercato dello spyware commerciale e degli zero-day

È il caso meglio studiato dalla letteratura di policy, e il più rilevante per capire come "si vende agli stati".

- **Scala.** Uno studio del Carnegie Endowment (2023) documenta che **almeno 74 governi** hanno acquistato spyware commerciale o strumenti di digital forensics; Israele risulta il principale paese esportatore di tali tecnologie nell'inventario globale.
- **Attori.** Prima FinFisher (Germania) e Hacking Team (Italia) dominavano; dopo la loro uscita di scena sono subentrati NSO Group (Pegasus), Intellexa (Predator), Candiru e altri. Google (Threat Analysis Group, 2024) stima che una quota maggioritaria degli zero-day sfruttati "in-the-wild" contro i suoi prodotti sia attribuibile a *commercial surveillance vendors*.
- **Il mercato degli zero-day.** Si distinguono tre fasce: (a) **white market** — bug bounty e divulgazione responsabile; (b) **gray market** — broker (es. Zerodium, Crowdfense) che comprano exploit dai ricercatori e li rivendono, in esclusiva, a clienti governativi, con listini storicamente nell'ordine del milione/milioni di dollari per catene complete zero-click; (c) **black market** — forum criminali. Il nodo teorico è il *vulnerabilities equities dilemma*: uno stato che "stocca" uno zero-day per uso di intelligence lascia la stessa falla sfruttabile dagli avversari.
- **La resilienza del mercato.** La domanda governativa è strutturalmente alta: se un fornitore viene sanzionato, altri ne colmano il vuoto. È la ragione per cui la sola repressione di singoli vendor ha effetti limitati.

## 8.4 Il quadro di governance (controlli all'export e norme)

La risposta regolatoria è multilivello e tuttora contestata:

- **Wassenaar Arrangement.** Regime multilaterale volontario (dal 1996, ~42 stati) sul controllo di armi convenzionali e beni *dual-use*. Nel **2013** ha aggiunto controlli sull'*"intrusion software"* e sui sistemi di sorveglianza IP, recependoli negli Stati Uniti via EAR (Bureau of Industry and Security). L'implementazione ha generato un **dibattito acceso sull'overreach**: la definizione ampia rischiava di colpire anche strumenti legittimi di ricerca difensiva e penetration testing, tanto che l'industria chiese revisioni e gli USA proposero di eliminare alcuni controlli sulla "technology for development" degli exploit.
- **EU Dual-Use Regulation 2021/821.** Richiede licenze per l'export di certi software di intrusione/sorveglianza fuori dai partner fidati, con una *human-security clause*.
- **Azione specifica sullo spyware.** Executive Order USA (2023) che limita l'uso governativo di spyware commerciale a rischio; restrizioni ai visti per chi abusa di spyware; sanzioni (es. inserimento di NSO e Intellexa in liste di restrizione); iniziative multilaterali come il **Pall Mall Process** (UK/Francia, 2024) e la *Joint Statement* a guida USA.
- **Standard tecnici duali.** Sul versante difensivo delle infrastrutture, standard come IEC 62443, IEC SC 77C (per l'IEMI/HPEM) e le guide CISA/NIST (§9) costituiscono la contropartita "blue" del panorama.

## 8.5 La tensione etica di fondo

Il campo vive una contraddizione irrisolta: gli stessi strumenti servono a proteggere dissidenti e a perseguitarli, a mettere in sicurezza infrastrutture e a sabotarle. La letteratura converge su alcune idee: trasparenza del mercato (oggi opaco su vendor, acquirenti e licenze), controlli all'export calibrati per non soffocare la ricerca difensiva, e norme internazionali di comportamento statale. Per un autore che studi questo campo, il posizionamento onesto è *difensivo e analitico*: capire le capacità per neutralizzarle, documentare il mercato per regolamentarlo.

---

# 9. Difesa: red/blue a strati e framework

La chiave è pensare **a livelli**, perché a ogni strato attacco e difesa si rispondono. La *difesa in profondità* è il principio unificante: nessun singolo strato è sufficiente.

## 9.1 Il quadro a strati (red ↔ blue)

| Livello | Red (capacità) | Blue (difesa) |
|---|---|---|
| Transistor / silicio | Laser FI, power/EM analysis | sensori on-die, logiche bilanciate, mesh anti-decap |
| Chip / firmware | voltage/EM glitch, RDP bypass, DFA | ridondanza, anti-glitch, tempo costante, masking, secure boot |
| Emanazioni | TEMPEST, covert channel | schermatura, Faraday, audio-gap, monitoraggio spettrale |
| Sensori | spoofing ottico/acustico/RF, GNSS | sensor fusion, validazione plausibilità, filtraggio, autenticazione segnale |
| Rete IoT / mesh | worm ZigBee, hijack mesh | cifratura end-to-end, OTA firmato, segmentazione, rate-limiting |
| ICS / grid | intrusione SCADA, load manipulation | air-gap vero, IDS industriali, autenticazione protocolli, data diode |
| Infrastruttura fisica / EM | IEMI / HPM | hardening EM, filtri, SPD, zone di rispetto, standard IEC SC77C |

## 9.2 Difesa delle infrastrutture industriali: IEC 62443, Purdue, NIST

Per OT/ICS lo standard di riferimento è la serie **ISA/IEC 62443** (sviluppata da ISA99 e IEC TC65). Concetti portanti:

- **Zone e conduit.** Si partiziona il sistema in *zone* a pari requisiti di sicurezza, collegate da *conduit* controllati: la compromissione di una zona non dilaga. Si appoggia tipicamente al **modello Purdue** (livelli dal campo/PLC fino all'IT aziendale, con una DMZ IT/OT in mezzo).
- **Security Levels (SL 1–4)** e **maturity levels**: si definisce *quanto* robusta deve essere ogni zona in funzione della minaccia attesa.
- **Principi**: *security by design*, *least privilege*, *defense-in-depth*, separazione IT/OT.

Complementi fondamentali: **NIST SP 800-82** (guida alla sicurezza ICS), il **NIST Cybersecurity Framework** (funzioni Identify-Protect-Detect-Respond-Recover), le guide **CISA** sulla defense-in-depth per sistemi di controllo. Strumenti architetturali chiave: segmentazione, **data diode** (flusso unidirezionale per garantire che da una zona critica i dati possano uscire ma nessun comando possa entrare), IDS/IPS specifici per OT, whitelisting applicativo, hardening di PLC/HMI, e il *fattore umano* (formazione, incident response).

## 9.3 Difesa contro l'IEMI/HPM

Approccio da compatibilità elettromagnetica portato a livello di sicurezza: **schermatura** (involucri e cavi), **filtraggio** sulle linee in ingresso, **dispositivi di protezione da sovratensioni (SPD)**, ridondanza e progettazione per la resilienza, **stand-off** fisico (allontanare l'elettronica critica dal perimetro accessibile). Gli standard IEC SC 77C e i lavori CIGRÉ C4.206 forniscono criteri di test e irrobustimento per sottostazioni e controlli AT. Un punto emerso dalle survey di siti (es. QinetiQ su infrastrutture critiche UK/US): pochissimi operatori oggi *riconoscono* la minaccia IEMI, a differenza di quella cyber e fisica — il primo gap è di consapevolezza.

## 9.4 Il principio generale

La difesa non elimina i canali fisici (è impossibile): li **monitora, attenua e ridonda**, alzando il costo dell'attacco oltre il valore del bersaglio. La sicurezza è economica prima che assoluta: si progetta perché attaccare costi più di quanto renda.

---

# 10. Catalogo tecnico: elettronica attaccante ed elettronica attaccata

Le sezioni precedenti hanno proceduto canale per canale. Questo catalogo le riorganizza in due tabelle di sintesi — una centrata sulla piattaforma che osserva o perturba (l'elettronica *attaccante*, nel senso di strumento di analisi/red-team), una centrata sul sistema che la subisce (l'elettronica *attaccata*, nel senso di bersaglio/superficie) — utile come indice di riferimento rapido per chi debba progettare un banco di valutazione o una strategia di difesa a strati. Per ciascuna voce, i parametri operativi (timing, potenze, frequenze di sintonia) restano fuori per scelta (cfr. nota introduttiva): quello che segue è una mappa delle categorie, non un manuale.

## 10.1 Elettronica attaccante: piattaforme e la loro funzione

| Piattaforma / categoria | Funzione primaria | Principio fisico | Accessibilità | Uso legittimo gemello |
|---|---|---|---|---|
| SDR + toolkit demodulazione (TempestSDR, gr-tempest) | Ricezione passiva di emanazioni EM (video, bus) | Induzione EM, radiazione involontaria | Hobbistico/ricerca | Radioamatorismo, ricerca TEMPEST difensiva |
| Oscilloscopio + sonda di corrente/shunt | Acquisizione tracce di potenza (SPA/DPA/CPA) | Dissipazione dinamica CMOS correlata al dato | Didattico (ChipWhisperer) | Valutazione di sicurezza, certificazione smartcard |
| Generatore di glitch tensione/clock | Fault injection a basso costo | Violazione dei margini di setup/hold | Didattico | Red-teaming hardware autorizzato |
| Iniettore EM compatto (PicoEMP) | Fault injection senza contatto, risoluzione spaziale | Corrente indotta localmente da impulso EM | Laboratorio specializzato | Valutazione EMFI, ricerca accademica |
| Stazione laser (decap + posizionatore) | Fault injection a risoluzione di singolo transistor | Fotocorrente generata nel silicio | Laboratorio specializzato | Certificazione secure element (Common Criteria) |
| Trasmettitore covert acustico/ottico/magnetico (software su malware già presente) | Esfiltrazione da sistema air-gapped | Modulazione di una grandezza fisica ordinaria | Richiede presenza software pregressa | Ricerca accademica (corpus Guri), red-team autorizzato |
| Laser modulato su microfono MEMS / sorgente acustica a frequenza di risonanza | Sensor spoofing (iniezione comandi, destabilizzazione IMU) | Risposta non lineare del trasduttore fuori banda | Ricerca accademica specializzata | Valutazione di robustezza dei sensori |
| Simulatore/ripetitore GNSS | GPS/GNSS spoofing | Segnale contraffatto più forte del satellite autentico | Regolato (uso civile spesso illegale senza licenza) | Test di ricevitori, aviazione/difesa autorizzati |
| Generatore IEMI/HPM | Interferenza o danneggiamento a distanza | Irradiazione di energia EM ad alta potenza | Militare/governativo | Test di hardening EM (standard IEC SC 77C) |
| Exploit software + accesso iniziale (supply-chain, phishing, USB) | Compromissione della rete di controllo (IoT/ICS) | Vulnerabilità protocollari e di implementazione | Spettro ampio: criminale → statale | Penetration testing autorizzato, bug bounty |

## 10.2 Elettronica attaccata: superfici, canale sfruttato, mitigazione primaria

| Bersaglio | Canale fisico sfruttabile | Impatto tipico | Mitigazione architetturale primaria |
|---|---|---|---|
| Monitor, cavi video (VGA/HDMI) | Emanazione EM correlata al segnale video | Ricostruzione remota del contenuto visualizzato | Schermatura, soft-TEMPEST, rumore sullo sfondo |
| Microcontrollori / smartcard / secure element | Consumo di potenza, tempo di esecuzione, emanazione EM locale | Estrazione di chiavi crittografiche (DPA/CPA/DFA) | Masking, hiding, tempo costante, secure boot |
| Bus di memoria, DRAM | Emanazione EM del bus; diafonia elettrica tra righe (Rowhammer) | Esfiltrazione dati; corruzione di memoria senza accesso fisico | Schermatura, ECC, refresh rinforzato, isolamento dei privilegi |
| Ventole, HDD, LED di stato, altoparlanti/microfoni | Emissione acustica/ottica modulabile da software malevolo | Esfiltrazione da sistema air-gapped (ultimo miglio) | Zone prive di elettronica personale, audio-gap, monitoraggio anomalie |
| Linee di alimentazione | Iniezione/osservazione di segnale sulla rete elettrica interna | Esfiltrazione (PowerHammer) o probing sincronizzato | Filtraggio di linea, monitoraggio spettrale del consumo (Appendice A.2) |
| Sensori MEMS (microfoni, IMU, accelerometri/giroscopi) | Risposta non lineare a stimoli ottici/acustici fuori specifica | Comandi iniettati silenziosamente; letture di volo falsificate | Sensor fusion, validazione di plausibilità, filtraggio di banda |
| Ricevitori GNSS | Segnale satellitare contraffatto più forte dell'autentico | Posizione/tempo falsificati | Autenticazione del segnale, rilevamento anomalie di potenza/geometria |
| Reti mesh IoT (ZigBee e simili) | Vulnerabilità di protocollo e di aggiornamento firmware | Propagazione tipo worm; commutazione di carico coordinata | Cifratura end-to-end, OTA firmato, segmentazione, rate-limiting |
| PLC / HMI / SCADA (Modbus, DNP3, IEC 61850) | Assenza storica di cifratura/autenticazione nei protocolli OT | Sabotaggio di processo, manipolazione di setpoint | Zone/conduit IEC 62443, data diode, IDS industriali (Appendice A.3) |
| Elettronica di bordo (droni, veicoli) esposta a HPM | Accoppiamento diretto o su cablaggio | Interference/upset/deception/danneggiamento permanente | Schermatura, filtraggio, SPD, stand-off fisico |

Le due tabelle sono deliberatamente simmetriche alla matrice red/blue del §9.1: qui il livello di dettaglio è sulla *piattaforma* e sul *bersaglio* come categorie di prodotto/sistema, non sulla procedura. La domanda utile per un valutatore non è "come lo faccio", ma "quale di queste categorie è presente nel mio sistema, e a quale contromisura del §9.1 corrisponde ciò che ho già — o che mi manca".

---

# 11. Direzioni di ricerca e sviluppi futuri

- **Machine learning per i side-channel.** Deep-TEMPEST ha mostrato che reti neurali possono ricostruire segnali prima illeggibili; la stessa leva (profiling con reti profonde, *deep learning SCA*) sta ridisegnando l'analisi dei consumi. Contropartita difensiva: contromisure progettate *contro* avversari ML.
- **Automazione del fault injection.** Mappatura spaziale sistematica della suscettibilità (framework tipo EMMap), posizionamento robotico delle sonde, ricerca automatica dei "sweet spot": il fault injection da arte artigianale diventa pipeline riproducibile — il che aiuta tanto l'attaccante di laboratorio quanto il valutatore che certifica.
- **Nuovi canali covert** su componenti sempre più integrati (GPU, acceleratori AI, interconnessioni ottiche on-chip).
- **Sicurezza dei sensori nei sistemi autonomi.** Con la diffusione di robotica e veicoli autonomi, lo spoofing di IMU/LiDAR/GNSS diventa una frontiera critica: servono *sensor fusion* robusta per progetto e autenticazione dei segnali.
- **Convergenza cyber–fisica nelle infrastrutture.** L'integrazione IT/OT e l'arrivo di 5G/IoT industriale allargano la superficie; la ricerca difensiva si concentra su *zero-trust* in ambito OT e rilevamento di anomalie di processo (non solo di rete).
- **Governance del mercato duale.** Il nodo aperto resta normativo: come controllare l'export senza soffocare la ricerca difensiva, e come costruire norme statali credibili sullo spyware e sugli zero-day.

---

# 12. Conclusioni

Il "potere" che nell'immaginario permette di piegare l'elettronica a distanza è, nella sua forma letterale, fantascienza. Ma la tesi sostenuta qui è che sotto di esso vive un nucleo scientifico reale, maturo e sorprendentemente ricco: **nessun sistema è fisicamente silenzioso o impermeabile**, perché calcolare è un atto fisico che emette, assorbe e può essere perturbato. Da questa unica radice si diramano i side-channel (leggere), il fault injection (perturbare), lo spoofing dei sensori (ingannare), e la compromissione delle reti di controllo (il "netrunning", che è networking, non etere).

La distanza dalla finzione si misura in tre vincoli ricorrenti: **prossimità** (quasi tutto richiede vicinanza fisica), **presenza** (l'esfiltrazione air-gap presuppone un impianto già interno), **indiscriminatezza** (l'energia irradiata distrugge, non seleziona). Dove questi vincoli cadono — nei sensori ingannabili e nelle reti IoT insicure — l'effetto "da anime" diventa concreto, ed è lì che la difesa è più urgente.

Sul piano duale, lo stesso sapere è arma e scudo; il posizionamento responsabile di chi lo studia è difensivo, analitico e trasparente. La difesa, infine, non promette l'invulnerabilità: promette di rendere l'attacco più costoso del suo premio, strato su strato. È, in fondo, l'unico "potere" realistico — e quello che davvero protegge le infrastrutture da cui dipendiamo.

---

# Bibliografia essenziale

**Fondamenti side-channel e fault**
- van Eck, W. (1985). *Electromagnetic Radiation from Video Display Units: An Eavesdropping Risk?* Computers & Security 4(4), 269–286.
- Kuhn, M. (2003). *Compromising Emanations: Eavesdropping Risks of Computer Displays.* Univ. of Cambridge, TR 577.
- Kocher, P. (1996). *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems.* CRYPTO '96.
- Kocher, P., Jaffe, J., Jun, B. (1999). *Differential Power Analysis.* CRYPTO '99.
- Boneh, D., DeMillo, R., Lipton, R. (1997). *On the Importance of Checking Cryptographic Protocols for Faults.* EUROCRYPT '97.
- Biham, E., Shamir, A. (1997). *Differential Fault Analysis of Secret Key Cryptosystems.* CRYPTO '97.
- Genkin, D., Shamir, A., Tromer, E. (2014). *RSA Key Extraction via Low-Bandwidth Acoustic Cryptanalysis.* CRYPTO '14.
- Kim, Y. et al. (2014). *Flipping Bits in Memory Without Accessing Them (Rowhammer).* ISCA '14.
- Kocher, P. et al. (2018). *Spectre Attacks.* / Lipp, M. et al. (2018). *Meltdown.*

**Air-gap / covert channel**
- Guri, M. (2024). *Mind The Gap: Can Air-Gaps Keep Your Private Data Secure?* arXiv:2409.04190.
- Park, J. et al. (2023). *A Survey on Air-Gap Attacks.* Sensors 23(6), 3215. DOI 10.3390/s23063215.
- Guri, M. et al. *GSMem* (USENIX Security 2015); *LANTENNA* arXiv:2110.00104; *CTRL-ALT-LED* arXiv:1907.05851; *PowerHammer*; *MAGNETO*; *Fansmitter*; *DiskFiltration*.

**EMFI / glitching / TEMPEST moderno**
- (2015). *High Precision Fault Injections on the Instruction Cache of ARMv7-M.* arXiv:1510.01537.
- Probst, M. et al. (2024). *Switch-Glitch: Location of Fault Injection Sweet Spots by EM Emanation.* FDTC 2024.
- Santhosh, G. S. et al. (2024). *EMMap: Spatial EMFI Mapping and Fault Classification.* arXiv:2512.09049.
- Alt, M. (2024). *Glitching in 3D: Low Cost EMFI Attacks.* CanSecWest 2024.
- Fernández, S. et al. (2024). *Deep-TEMPEST: Using Deep Learning to Eavesdrop on HDMI.* arXiv:2407.09717.

**Sensori e infrastrutture**
- Ronen, E., O'Flynn, C., Shamir, A., Weingarten, A. (2017). *IoT Goes Nuclear: Creating a ZigBee Chain Reaction.* IEEE S&P 2017.
- Sugawara, T., Fu, K. et al. (2020). *Light Commands.* USENIX Security 2020.
- Trippel, T. et al. (2017). *WALNUT: Analog Attacks on Sensors.* IEEE EuroS&P 2017.

**IEMI / HPM**
- Radasky, W. / Metatech. *Meta-R-323: IEMI and Its Impact on the U.S. Power Grid* (FERC).
- Progetti UE FP7: **STRUCTURES**, **HIPOW** (Protection of Critical Infrastructure against HPM).
- IEC SC 77C (HPEM transient phenomena); CIGRÉ WG C4.206 (protezione sottostazioni AT da IEMI).

**Mercato duale e governance**
- Carnegie Endowment (2023). *Why Does the Global Spyware Industry Continue to Thrive?*
- Carnegie Endowment (2024). *Harmonizing Campaigns to Tame the Hacking Marketplace / Pall Mall Process.*
- Google TAG (2024). Report sui *commercial surveillance vendors* e gli zero-day.
- **Wassenaar Arrangement** (controlli 2013 su "intrusion software"); **EU Dual-Use Regulation 2021/821**; **US Executive Order on Spyware** (2023).

**Difesa ICS/OT**
- ISA/IEC 62443 (serie). NIST SP 800-82. NIST Cybersecurity Framework. CISA/NCCIC, *Defense-in-Depth for ICS* (2016). Modello Purdue.
- Casi: Stuxnet (2010); BlackEnergy / Ucraina (2015); Triton/Trisis (2017); Colonial Pipeline (2021).

**Strumentazione didattica legittima**
- NewAE *ChipWhisperer* (ecosistema open per SCA e fault injection su bersagli di test); *PicoEMP*; *TempestSDR* / *gr-tempest*.

---

# Appendice A — Codice dimostrativo e difensivo

I tre script che seguono accompagnano la tesi come materiale eseguibile. Sono stati scritti e verificati (eseguiti, con output reale riportato) nel rispetto del vincolo di ambito dichiarato nella nota introduttiva: **nessuno di essi tocca hardware reale, un target reale o un sistema in produzione**. Si dividono in due famiglie:

- **A.1** è una dimostrazione *didattica* del principio statistico della Correlation Power Analysis (§3.2), su dati interamente sintetici generati dallo script stesso.
- **A.2** e **A.3** sono strumenti *difensivi*: il primo è un rilevatore di anomalie di consumo (§9), il secondo una policy dichiarativa di segmentazione IEC 62443 (§9.2).

Dipendenza comune: Python 3 con NumPy (`pip install numpy`); A.3 non richiede esecuzione, è un file di configurazione YAML.

## A.1 Correlation Power Analysis su dati sintetici (`cpa_didattica_sintetica.py`)

Ricostruisce, su una S-box giocattolo e un modello di leakage generati a runtime, lo stesso principio statistico con cui una CPA reale separerebbe la sotto-chiave corretta dalle 255 ipotesi sbagliate: la correlazione di Pearson tra il consumo osservato e il peso di Hamming predetto per ciascuna ipotesi di chiave. Nessuna traccia è acquisita da uno strumento reale.

```python
"""
cpa_didattica_sintetica.py

Dimostrazione didattica di Correlation Power Analysis (CPA) su tracce
DI POTENZA COMPLETAMENTE SINTETICHE, generate dallo script stesso.

Scopo: illustrare il principio statistico alla base della DPA/CPA
(Kocher, Jaffe & Jun, 1999) - cioè che il consumo di un circuito CMOS
correla con il peso di Hamming del dato manipolato - senza alcun
hardware reale, alcun target reale e alcuna traccia acquisita.

Non è collegabile a un dispositivo reale: la "sbox" è una permutazione
casuale generata a runtime (non un cifrario reale), i "consumi" sono
numeri generati da un modello matematico + rumore gaussiano. Per
un'analisi su hardware vero servono: oscilloscopio, sonda di corrente,
un target reale, sincronizzazione del trigger - tutt'altro problema,
volutamente non affrontato qui.

Riferimento teorico: tesi, §3.2 "Analisi dei consumi: SPA, DPA, CPA".

Esecuzione: python3 cpa_didattica_sintetica.py
Dipendenze: numpy
"""

import numpy as np

rng = np.random.default_rng(seed=42)

# --- 1. Bersaglio giocattolo: una permutazione casuale a 8 bit -------------
# (sostituisce una vera S-box crittografica: qui serve solo a produrre
#  un valore intermedio che dipende da plaintext e "chiave" segreta)
N_VALUES = 256
toy_sbox = rng.permutation(N_VALUES).astype(np.uint8)


def hamming_weight(x: np.ndarray) -> np.ndarray:
    """Numero di bit a 1 in ciascun byte dell'array."""
    return np.unpackbits(x[:, None].astype(np.uint8), axis=1).sum(axis=1)


# --- 2. Simulazione dell'esperimento ----------------------------------------
N_TRACES = 2000
true_key_byte = 0x5A  # il "segreto" che l'esercizio prova a ritrovare

plaintexts = rng.integers(0, 256, size=N_TRACES, dtype=np.uint8)
intermediate = toy_sbox[plaintexts ^ true_key_byte]  # valore intermedio reale

# Modello di leakage: consumo = guadagno * peso_di_Hamming(intermedio) + rumore
LEAKAGE_GAIN = 1.0
NOISE_STD = 4.0
simulated_traces = (
    LEAKAGE_GAIN * hamming_weight(intermediate)
    + rng.normal(0, NOISE_STD, size=N_TRACES)
)


# --- 3. Attacco CPA: prova ogni ipotesi di chiave, correla con il modello --
def pearson_corr(a: np.ndarray, b: np.ndarray) -> float:
    a = a - a.mean()
    b = b - b.mean()
    denom = np.sqrt((a**2).sum() * (b**2).sum())
    return float((a * b).sum() / denom) if denom > 0 else 0.0


correlations = np.zeros(256)
for key_hypothesis in range(256):
    hyp_intermediate = toy_sbox[plaintexts ^ key_hypothesis]
    hyp_leakage_model = hamming_weight(hyp_intermediate)
    correlations[key_hypothesis] = abs(pearson_corr(hyp_leakage_model, simulated_traces))

recovered_key = int(np.argmax(correlations))

print("=== CPA didattica su dati sintetici (nessun hardware/target reale) ===")
print(f"Numero di tracce simulate:                  {N_TRACES}")
print(f"Chiave vera (nota solo alla simulazione):   0x{true_key_byte:02X}")
print(f"Chiave recuperata dalla CPA:                 0x{recovered_key:02X}")
print(f"Correlazione al picco:                       {correlations[recovered_key]:.3f}")
others_mean = (correlations.sum() - correlations[recovered_key]) / 255
print(f"Correlazione media sulle altre 255 ipotesi:  {others_mean:.3f}")
print()
print("Il distacco fra il picco e il rumore di fondo è la stessa statistica")
print("che, su tracce vere, separerebbe la sotto-chiave corretta da tutte")
print("le altre ipotesi (§3.2 della tesi).")
```

**Output reale (eseguito):**

```
=== CPA didattica su dati sintetici (nessun hardware/target reale) ===
Numero di tracce simulate:                  2000
Chiave vera (nota solo alla simulazione):   0x5A
Chiave recuperata dalla CPA:                 0x5A
Correlazione al picco:                       0.347
Correlazione media sulle altre 255 ipotesi:  0.029

Il distacco fra il picco e il rumore di fondo è la stessa statistica
che, su tracce vere, separerebbe la sotto-chiave corretta da tutte
le altre ipotesi (§3.2 della tesi).
```

La chiave viene recuperata correttamente (`0x5A`), e il picco di correlazione (0.347) si distacca nettamente dal rumore di fondo sulle altre 255 ipotesi (0.029 in media) — esattamente la separazione statistica che, su un bersaglio reale, un attaccante sfrutterebbe per recuperare una chiave byte per byte.

## A.2 Rilevamento difensivo di periodicità sospetta nel consumo (`rilevamento_anomalie_consumo.py`)

Strumento **blue-team**: non attacca nulla, osserva una serie di consumo e segnala quando contiene una periodicità innaturalmente regolare — una delle firme osservabili di un probing ripetuto (power analysis) o di una sincronizzazione di fault injection. La prima versione di questo script conteneva un bug di normalizzazione dell'autocorrelazione (bias verso i lag piccoli) corretto durante la stesura della tesi; il codice sotto è la versione corretta e verificata, con entrambi i casi di test (solo rumore / pattern iniettato) eseguiti realmente.

```python
"""
rilevamento_anomalie_consumo.py

Strumento di monitoraggio DIFENSIVO: cerca, in una serie temporale di
consumo energetico (es. da un sensore di corrente su un'alimentazione
critica), pattern compatibili con un probing ripetuto e periodico - una
delle firme osservabili quando qualcuno sta acquisendo molte tracce
ravvicinate per un attacco di tipo power-analysis, o sta sincronizzando
un fault injection.

Non esegue alcun attacco: analizza SOLO dati di monitoraggio e genera
un allarme con una stima di periodo e forza del segnale sospetto.
Pensato come punto di partenza per l'integrazione in un sistema di
monitoraggio reale (es. accanto a sensori di corrente su schede
critiche, armadi di distribuzione, linee di alimentazione).

Note di implementazione (due bug concettuali evitati volutamente):

1. Normalizzazione per-lag, non globale. np.correlate(..., mode="full")
   diviso solo per il valore a lag zero NON corregge per il numero di
   campioni effettivamente sovrapposti a ciascun lag, che decresce al
   crescere del lag: questo introduce un bias sistematico verso i lag
   piccoli. Qui ogni lag è normalizzato sul proprio numero di campioni
   sovrapposti (stima "unbiased" per quel lag) prima del confronto.

2. Primo massimo dopo il primo minimo, non massimo assoluto. Un segnale
   anche solo "lento" (non periodico) ha correlazione alta ai lag molto
   piccoli semplicemente perché campioni adiacenti si assomigliano - non
   è segno di periodicità. Il vero periodo fondamentale è dove la
   correlazione, dopo essere scesa sotto zero (un "mezzo ciclo" visto),
   torna a salire: è il primo ritorno ad alta correlazione DOPO un vero
   avvallamento, non il primo valore alto in assoluto. Cercare invece il
   massimo assoluto su tutta la finestra di ricerca è statisticamente
   fragile per un segnale quasi sinusoidale: la correlazione teorica
   risale a un valore simile a ogni multiplo del periodo, quindi il
   rumore decide quale di queste tante creste quasi equivalenti risulti
   il massimo assoluto, e può far "vincere" un'armonica lontana invece
   del periodo vero (osservato empiricamente nelle prime due versioni di
   questo script). Per non confondere un picco vero con una minuscola
   oscillazione di rumore proprio sul fondo dell'avvallamento, il picco
   è confermato solo dopo che il segnale è tornato a scendere in modo
   netto rispetto al massimo toccato nella risalita.

Per dataset più lunghi di quello qui usato, una densità spettrale di
potenza (FFT) resta l'alternativa più efficiente a questo ciclo esplicito,
con lo stesso principio di "primo picco", non "picco più alto in assoluto".

Riferimento teorico: tesi, §9 "Difesa: red/blue a strati e framework".

Esecuzione: python3 rilevamento_anomalie_consumo.py
Dipendenze: numpy
"""

import numpy as np


def rileva_periodicita_sospetta(
    serie: np.ndarray,
    campionamento_hz: float,
    soglia_autocorrelazione: float = 0.6,
    periodo_min_s: float = 0.0005,
    periodo_max_s: float = 0.5,
) -> dict:
    """
    Cerca un periodo dominante nella serie di consumo tramite
    autocorrelazione normalizzata per-lag, individuando il primo
    massimo locale che segue un primo minimo locale negativo (il primo
    "ritorno" ad alta correlazione dopo un vero avvallamento). Un picco
    forte a un periodo "troppo regolare" per il normale funzionamento
    del dispositivo è un indicatore (non una prova) di probing ripetuto.
    """
    serie = np.asarray(serie, dtype=float)
    serie = serie - serie.mean()
    n = serie.size
    varianza = float(serie.var())

    if varianza == 0.0:
        return {"allarme": False, "motivo": "serie costante, nessuna varianza"}

    lag_min = max(1, int(periodo_min_s * campionamento_hz))
    lag_max = min(n - 1, int(periodo_max_s * campionamento_hz))

    if lag_max <= lag_min + 1:
        return {"allarme": False, "motivo": "finestra di analisi troppo corta"}

    # Autocorrelazione normalizzata per ciascun lag candidato.
    valori = np.empty(lag_max - lag_min + 1)
    for idx, lag in enumerate(range(lag_min, lag_max + 1)):
        prodotto = np.dot(serie[:-lag], serie[lag:]) / (n - lag)
        valori[idx] = prodotto / varianza

    # 1) Primo minimo locale chiaramente negativo: segna la fine della
    #    "discesa liscia" iniziale e la presenza di un vero mezzo ciclo.
    i_min = None
    for i in range(1, len(valori) - 1):
        if valori[i] < 0 and valori[i] <= valori[i - 1] and valori[i] <= valori[i + 1]:
            i_min = i
            break

    # 2) Primo massimo "vero" dopo quel minimo: si segue la salita
    #    tenendo il massimo corrente, e si conferma il picco solo
    #    quando il segnale è ridisceso in modo netto (non una minuscola
    #    oscillazione di rumore) E quel massimo supera chiaramente il
    #    minimo di partenza - cioè è stato completato un intero ciclo.
    MARGINE = 0.05
    i_peak = None
    if i_min is not None:
        max_val = valori[i_min]
        max_idx = i_min
        for i in range(i_min + 1, len(valori)):
            if valori[i] > max_val:
                max_val = valori[i]
                max_idx = i
            elif valori[i] < max_val - MARGINE:
                if max_val > valori[i_min] + MARGINE:
                    i_peak = max_idx
                break

    if i_peak is not None:
        lag_scelto = lag_min + i_peak
        valore_scelto = float(valori[i_peak])
    else:
        # Nessun ciclo completo osservato nella finestra: fallback sul
        # massimo assoluto, utile solo come diagnostica (non implica
        # periodicità confermata se resta sotto soglia).
        i_fallback = int(np.argmax(valori))
        lag_scelto = lag_min + i_fallback
        valore_scelto = float(valori[i_fallback])

    allarme = valore_scelto >= soglia_autocorrelazione
    return {
        "allarme": allarme,
        "periodo_stimato_s": lag_scelto / campionamento_hz,
        "forza_periodicita": round(valore_scelto, 3),
        "soglia": soglia_autocorrelazione,
    }


if __name__ == "__main__":
    # Esempio con dati sintetici: rumore di fondo "normale" e, a metà
    # serie, un pattern periodico iniettato per simulare un probing.
    rng = np.random.default_rng(0)
    fs = 10_000  # Hz
    durata_s = 2.0
    t = np.arange(0, durata_s, 1 / fs)

    normale = rng.normal(0, 1.0, size=t.size)
    pattern_sospetto = 2.0 * np.sin(2 * np.pi * 50 * t)  # 50 Hz, molto regolare
    serie_osservata = normale.copy()
    meta = t.size // 2
    serie_osservata[meta:] += pattern_sospetto[meta:]

    print("=== Monitoraggio consumo: prima metà (solo rumore) ===")
    print(rileva_periodicita_sospetta(serie_osservata[:meta], campionamento_hz=fs))

    print()
    print("=== Monitoraggio consumo: seconda metà (pattern iniettato) ===")
    print(rileva_periodicita_sospetta(serie_osservata[meta:], campionamento_hz=fs))
```

**Output reale (eseguito):**

```
=== Monitoraggio consumo: prima metà (solo rumore) ===
{'allarme': False, 'periodo_stimato_s': 0.4668, 'forza_periodicita': 0.048, 'soglia': 0.6}

=== Monitoraggio consumo: seconda metà (pattern iniettato) ===
{'allarme': True, 'periodo_stimato_s': 0.0201, 'forza_periodicita': 0.671, 'soglia': 0.6}
```

Sul solo rumore, nessun allarme (forza 0.048, ben sotto soglia). Sul pattern iniettato a 50 Hz (periodo vero 0.02 s), lo strumento scatta l'allarme e stima il periodo a **0.0201 s** — la stessa periodicità del segnale iniettato, recuperata senza conoscerla a priori.

## A.3 Policy di segmentazione IEC 62443 — zone e conduit (`policy_zone_conduit_iec62443.yaml`)

Non è codice eseguibile ma un esempio dichiarativo di come si traduce in configurazione il modello di zone/conduit del §9.2: quattro zone a security level crescente verso il campo, tre conduit con whitelist di protocollo esplicite, e un diodo di dati fisico in uscita dalla zona più critica. Pensato come scheletro da adattare al proprio firewall industriale e alla propria analisi del rischio (IEC 62443-3-2), non come configurazione pronta all'uso.

```yaml
# policy_zone_conduit_iec62443.yaml
#
# Esempio didattico di policy di segmentazione a "zone e conduit"
# secondo il modello ISA/IEC 62443, applicata a un'infrastruttura OT
# semplificata (es. sottostazione / sistema di illuminazione cittadina
# centralizzato). Non è una configurazione pronta per la produzione: è
# uno scheletro concettuale da adattare con il proprio firewall/NGFW
# industriale e la propria analisi del rischio (IEC 62443-3-2).
#
# Riferimento teorico: tesi, §9.2 "Difesa delle infrastrutture
# industriali: IEC 62443, Purdue, NIST".

zones:
  - nome: IT-aziendale
    livello_purdue: "4-5"
    security_level_target: SL1
    descrizione: >
      Rete uffici, ERP, posta elettronica. Nessun accesso diretto ai
      controlli di processo.

  - nome: DMZ-IT-OT
    livello_purdue: "3.5"
    security_level_target: SL2
    descrizione: >
      Zona cuscinetto: storico dati, server di patch, jump host per
      accesso remoto autorizzato e auditato. Nessun dispositivo qui
      avvia connessioni dirette verso la zona di controllo.

  - nome: supervisione-SCADA
    livello_purdue: "2-3"
    security_level_target: SL3
    descrizione: >
      HMI, storici di processo, server SCADA. Comunica con la zona di
      controllo solo tramite i conduit definiti sotto.

  - nome: controllo-campo
    livello_purdue: "0-1"
    security_level_target: SL3-SL4
    descrizione: >
      PLC/RTU che pilotano direttamente gli attuatori fisici (es.
      interruttori di linea, alimentazione lampioni). Nessun accesso
      diretto da Internet o da IT-aziendale, in nessuna condizione.

conduits:
  - da: DMZ-IT-OT
    a: supervisione-SCADA
    protocolli_consentiti: [OPC-UA-over-TLS]
    direzione: bidirezionale
    autenticazione_richiesta: true
    note: >
      Unico varco autorizzato tra mondo IT e supervisione OT; tutto il
      traffico è loggato e ispezionato da un IDS OT.

  - da: supervisione-SCADA
    a: controllo-campo
    protocolli_consentiti: [Modbus-TCP-con-whitelist-funzioni]
    direzione: bidirezionale
    autenticazione_richiesta: true
    note: >
      Solo i function code Modbus necessari all'operatività sono
      permessi (whitelist, non blacklist); ogni comando di scrittura è
      loggato con utente e timestamp.

  - da: controllo-campo
    a: storico-dati
    protocolli_consentiti: [one-way-data-diode]
    direzione: solo-uscita
    autenticazione_richiesta: false
    note: >
      Diodo di dati fisico: i dati di processo possono USCIRE dalla
      zona critica verso lo storico, ma nessun comando può entrare da
      questo percorso. Garanzia a livello fisico, non solo logico.

regole_generali:
  - "Nessuna zona di controllo-campo è raggiungibile da IT-aziendale, nemmeno in modo indiretto."
  - "Ogni conduit ha una whitelist esplicita di protocolli, mai una blacklist."
  - "Le credenziali di controllo-campo non sono mai le stesse di IT-aziendale."
  - "Ogni variazione a questa policy richiede una nuova analisi del rischio (IEC 62443-3-2)."
```

Il punto architetturale da notare: il conduit verso lo storico dati è a **direzione singola** (`solo-uscita`, diodo fisico) — la stessa idea del data diode citata nel §9.2 come contropartita blue dell'esfiltrazione covert channel del §4: un canale che può solo far uscire telemetria non può, per costruzione fisica e non solo per regola software, far entrare un comando.

