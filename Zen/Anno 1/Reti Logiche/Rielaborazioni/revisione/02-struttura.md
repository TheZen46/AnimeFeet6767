# Reti Logiche · fase 3: struttura in moduli

> Su indicazione dell'autore (4 novembre 2026) non ci si ferma per l'approvazione: la struttura si applica così, con la strada A per le aggiunte come in Analisi 1A, e le domande si raccolgono per il passaggio finale.

## Numero di moduli

Il catalogo prevede 4 moduli. Con 6 CFU (circa 48-60 ore) sono circa 12-15 ore l'uno, coerenti con la regola. L'ordine è quello del programma, con uno spostamento: i ritardi di propagazione e le alee (RL-02) vanno nel modulo 2, insieme alle reti standard e all'aritmetica, perché preparano il passaggio alle reti sequenziali del modulo 3.

Le parole sono stimate dalla trascrizione, senza le descrizioni delle figure, più le aggiunte e gli esercizi svolti. A circa 500 parole per pagina, il corso intero viene sulle 35-40 pagine A4.

| Modulo | Titolo | ID | Lezioni | Parole (appunti + aggiunte) | Aggiunte |
|---|---|---|---|---|---|
| 1 | Algebra booleana e sintesi delle reti combinatorie | RL-01, RL-02 (mappe) | L01, L02, L03 p. 1, p. 4-5, L05, L07 p. 1, Esercizi | ~2600 + ~900 | ~25% |
| 2 | Reti combinatorie standard, ritardi e aritmetica | RL-02 (reti standard, ritardi), RL-03 | L02 p. 2-3, L03 p. 1-3, L04, L06 p. 1, L07 p. 2 | ~2700 + ~800 | ~23% |
| 3 | Flip-flop, registri e contatori | RL-04, RL-05 | L06, L07 p. 2-3, L08, L09 p. 1, Materiale del docente | ~2300 + ~1200 | **~35%** |
| 4 | Macchine a stati finiti e progetto con ASM | RL-06, RL-07, RL-08 | L09 p. 2-3, L10, L11, L12, L13, Esercizi | ~3200 + ~1300 | **~30%** |

Nei moduli 3 e 4 le aggiunte superano il 15%: nel 3 mancano la teoria dei flip flop sul fronte e l'analisi temporale, nel 4 il controllore-datapath e la simulazione. Si seguono comunque, come in Analisi 1A, tutte segnate `[!aggiunta]` con la fonte.

## Schema di ogni modulo

- `# N · Titolo`, poi il paragrafo "In questo modulo" con i prerequisiti (i moduli precedenti, per nome) e gli obiettivi presi dal programma ufficiale.
- Sezioni `## N.1`, `## N.2`, …: definizioni e teoremi nei callout `[!definizione]` e `[!teorema]`, poi il commento in prosa; tabelle di verità e mappe come tabelle Markdown; circuiti e diagrammi temporali come figure SVG ridisegnate.
- "Esempi ed esercizi svolti": vengono dagli esercizi degli appunti, ricalcolati e controllati. L'esame è a problemi di progetto.
- "Riepilogo" in prosa.

## Modulo 1 · Algebra booleana e sintesi delle reti combinatorie

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 1.1 Variabili e funzioni booleane | $\mathbb{B} = \{0, 1\}$, funzioni $\mathbb{B}^n \to \mathbb{B}$, principio di enumerazione: $2^n$ righe e $2^{2^n}$ funzioni | L01, L02 p. 1 | – |
| 1.2 Le porte logiche | Funzioni di una variabile; le 16 funzioni di due variabili; AND, OR, NOT, NAND, NOR, XOR, XNOR con simboli e tabelle | L01 | – |
| 1.3 Algebra di Boole | Assiomi, teoremi, De Morgan, dualità, consenso; semplificazione algebrica | L01, L02, L07 p. 1, Esercizi | Assiomi e teoremi in tabella, dualità (RL-01) |
| 1.4 Forme canoniche | Teorema di Shannon nelle due forme, mintermini e maxtermini, SOP e POS, reti a due livelli | L02 p. 1-2 | Enunciato generale, mintermini e maxtermini (RL-01) |
| 1.5 Mappe di Karnaugh | Dalla tabella alla mappa, adiacenza, regole di raggruppamento, mappe a 2, 3, 4 variabili, sintesi SOP e POS | L02 p. 2-3, L03 p. 1, L05, L07 p. 1 | Implicanti primi ed essenziali (RL-02) |
| 1.6 Indifferenze e variabili riportate | Indifferenze sulle uscite e sugli ingressi; mappe a variabili riportate, sintesi quasi minima | L03 p. 1, p. 4-5, L07 p. 1 | – |
| 1.7 Reti con sole NAND o NOR | Completezza funzionale, trasformazione di una SOP in sole NAND | L03 p. 1 | Trasformazione POS → NOR |
| Esempi ed esercizi svolti | Esercizio del circuito (corretto), esercizi di L07, fogli di esercizi | L02, L07, Esercizi | – |

## Modulo 2 · Reti combinatorie standard, ritardi e aritmetica

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 2.1 Multiplexer | MUX 2→1 (specifica, tabella, SOP, POS, circuito), MUX 4→1, MUX costruito con MUX più piccoli, MUX come rete universale | L02 p. 1-3, L03 p. 2-3, L07 p. 2 | – |
| 2.2 Demultiplexer, decoder, encoder | DEMUX 1→4 e 1→8, decoder $n \to 2^n$, porta programmabile | L03 p. 1-3 | Encoder e encoder con priorità (RL-02) |
| 2.3 Ritardi e alee | Ritardo di propagazione, diagramma temporale, alea statica su $\bar{A}B + AC$ e termine di consenso | L02 p. 2, L06 p. 1 | Termine di consenso (RL-02) |
| 2.4 Numeri e codici | Notazione posizionale, conversioni fra basi 2, 8, 10, 16; BCD; Gray; parità | L04 p. 1, p. 3, L07 p. 2 | – |
| 2.5 Somma e sottrazione | Somma in colonna, half adder, full adder, sommatore a cascata, overflow | L04 p. 2-3 | – |
| 2.6 Numeri negativi | Modulo e segno (e perché non basta), complemento a 2, estensione del segno, overflow | L04 p. 2, L07 p. 2 | Regola dell'overflow, sottrattore (RL-03) |
| 2.7 Prodotto, comparatore e ALU | Prodotto per somme di prodotti parziali; comparatore; ALU con MUX; virgola fissa e mobile in un riquadro | L04 p. 2-3, L07 p. 2 | Comparatore (RL-03) |
| Esempi ed esercizi svolti | Conversioni e operazioni di L07, MUX di L07, XOR con il MUX | L07 | – |

## Modulo 3 · Flip-flop, registri e contatori

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 3.1 Dalla retroazione alla memoria | Rete con retroazione, elemento che memorizza un 1, set e reset | L06 p. 1-2 | – |
| 3.2 Latch | Latch SR a NOR e a NAND, tabella caratteristica, stato vietato; latch con abilitazione; latch D; latch JK e oscillazione | L06 p. 2-3 | Trasparenza, metastabilità (RL-04) |
| 3.3 Flip-flop sul fronte | PET e NET, FF D, JK, T; PR e CL; tabelle caratteristiche e di eccitazione | L06 p. 3, L08 p. 1, L09 p. 1, L11 p. 2 | Master-slave (RL-04) |
| 3.4 Temporizzazioni | $t_s$, $t_h$, $t_p$, $t_w$, periodo minimo | L08 p. 1 | Periodo minimo di una rete sincrona e vincolo di hold (RL-05) |
| 3.5 Registri | PIPO, SISO, SIPO, PISO, registro universale | L08 p. 2 | – |
| 3.6 Contatori | Contatore sincrono con FF T, contatore modulo 4 con FF D, contatore universale con sommatore, TC | L08 p. 2, L09 p. 1 | Modulo N e cascata (RL-05) |
| 3.7 Analisi di reti sincrone | Dal circuito al diagramma temporale: JK + D, LFSR, esercizio del simulatore | L07 p. 2-3, L08 p. 1, L06 p. 4, Materiale | – |
| Esempi ed esercizi svolti | Diagrammi completati | L07, L08, Materiale | – |

## Modulo 4 · Macchine a stati finiti e progetto con ASM

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 4.1 La macchina a stati finiti | Struttura (rete dello stato successivo, registro, rete delle uscite), Moore e Mealy, ingressi sincronizzati | L09 p. 2, L12 p. 1 | – |
| 4.2 Il linguaggio ASM | Blocco di stato, blocco condizionale, uscita condizionata, stato di reset; contatore modulo 4 e up/down | L09 p. 2-3, L12 p. 1 | – |
| 4.3 Procedura di progetto | Specifica, ASM, registro e codifica, tabella degli stati, sintesi con FF D e con FF JK; esempio delle luci | L11 | Scelta della codifica (RL-06) |
| 4.4 Analisi di una MSF | Dal circuito alle equazioni, alla tabella, all'ASM | L10 p. 2 | Procedura generale (RL-06) |
| 4.5 Strutture base | Sincronizzatore, rilevatore di fronti, rilevatore di impulso lungo, generatore di sequenze, rilevatore di due pulsanti | L09 p. 3, L10 | – |
| 4.6 Moore e Mealy a confronto | ES. 10 in tre versioni, Es. 9 | L11, L12 | – |
| 4.7 Stati non usati ed errori | Bit flip, stati di errore, ritorno al reset | L12 p. 1 | – |
| 4.8 Progetti completi | Lavatrice (sintesi JK), trasmettitore seriale | L12, L13 | – |
| 4.9 Controllore e datapath | Architettura, segnali di controllo e di stato, esempio della misura della durata di un impulso | Esercizi 172948 | Tutto il paragrafo (RL-07) |
| 4.10 Simulazione | Verifica di un progetto con il simulatore | L06, Materiale | Tutto il paragrafo (RL-08) |
| Esempi ed esercizi svolti | ENB/SEL completato, Es. 9 con JK corretto | L11, L12 | – |
