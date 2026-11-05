# Reti Logiche · fase 2: copertura del programma

Il confronto è fatto con `revisione/programmi/reti-logiche.md`, cioè la sintesi della pagina ufficiale 2026/27 (testo: Donzellini, Oneto, Ponta, Anguita, *Introduzione al progetto di sistemi digitali*, Springer 2018). Gli appunti sono del 2025/26. Le posizioni rimandano alle trascrizioni (`trascrizione/Lnn`). In questa fase non è stato aggiunto nulla.

## 1. Matrice di copertura

| ID | Argomento | Stato | Dove | Note |
|---|---|---|---|---|
| RL-01 | Algebra booleana e reti combinatorie | parziale | L01, L02 p. 1-2, L03 p. 1, L07 p. 1, Esercizi | Ci sono le funzioni di due variabili, le porte, le tabelle di verità, De Morgan e alcune semplificazioni. Mancano gli assiomi e i teoremi dell'algebra di Boole in forma ordinata (assorbimento, consenso, idempotenza, involuzione), il principio di dualità (solo accennato in L01), l'enunciato generale del teorema di Shannon (la versione 1 è lasciata in bianco), mintermini e maxtermini come forme canoniche |
| RL-02 | Sintesi e minimizzazione con le mappe, reti standard, ritardi | completo | L02 p. 2-3, L03, L05, L06 p. 1, L07 | Mappe a 2, 3, 4 variabili, indifferenze, SOP e POS, NAND, variabili riportate, MUX, DEMUX, decoder, alee. Mancano il codificatore (*encoder*) e il comparatore fra le reti standard, la definizione di implicante primo ed essenziale, e il termine di consenso come rimedio alle alee |
| RL-03 | Aritmetica binaria e reti aritmetiche | parziale | L04, L07 p. 2 | Basi, BCD, Gray, somma, sottrazione, prodotto, complemento a 2, half e full adder, sommatore a cascata, ALU con MUX. Mancano la regola dell'overflow in complemento a 2, il sottrattore realizzato con il sommatore, il comparatore come rete; virgola mobile solo accennata |
| RL-04 | Flip-flop: struttura, funzionamento, caratteristiche dinamiche | parziale | L06 p. 1-3, L08 p. 1 | Latch SR a NOR e NAND, D, JK, abilitazione, PR e CL, tempi $t_s$, $t_h$, $t_p$, $t_w$. Mancano il motivo per cui servono i flip flop sul fronte (il latch JK oscilla e un latch trasparente non basta in una rete con retroazione), lo schema master-slave o edge-triggered, la metastabilità |
| RL-05 | Registri e contatori, analisi temporale | parziale | L08, L09 p. 1, L06 p. 3-4, Materiale del docente | Registri PIPO, SISO, SIPO, PISO, universale; contatori sincroni con FF T, contatore universale con sommatore, contatore modulo 4; LFSR come esercizio. Manca la formula del periodo minimo di una rete sincrona ($T_{min} \ge t_{p,FF} + t_{comb} + t_s$) e il vincolo di hold; mancano il contatore modulo N qualsiasi e il collegamento in cascata con TC ed enable |
| RL-06 | MSF con ASM, tabelle di stato e mappe | completo | L09 p. 2-3, L10, L11, L12, L13, Esercizi | Moore e Mealy, ASM con blocchi di stato, condizionali e uscite condizionate, procedura completa con FF D e JK, molti esempi, gestione degli stati non usati. Va scritta la procedura di analisi (dal circuito all'ASM) in modo generale: c'è un solo esempio (L10) |
| RL-07 | MSF come controllore: sistemi controllore-datapath | da verificare | Esercizi 172948 (solo la specifica) | C'è solo la specifica di un sistema con due FSM e un contatore (TRG, CL, BSY, ETX, SER), senza soluzione. Nessuna lezione ne parla: forse è stato fatto dopo il 10/12 o nelle esercitazioni |
| RL-08 | Simulazione di semplici sistemi digitali | da verificare | L06 p. 3-4, Materiale del docente | Ci sono solo le schermate del simulatore Deeds e un esercizio compilato a mano. È negli obiettivi, non nell'elenco |

## 2. Argomenti extra

- Bit di parità e somma di controllo (L04 p. 3): pertinente alle reti combinatorie (rete di parità con XOR) e al trasmettitore di L13. Si tiene come esempio di rete con XOR.
- Virgola fissa e mobile (L04 p. 2-3): accennate. Non sono nell'elenco del programma; si tiene un riquadro breve senza lo standard IEEE 754 (domanda 4).

## 3. Lacune e aggiunte proposte

Tutte le aggiunte vengono dal testo del corso (Donzellini e altri, 2018), riformulate, oppure da nozioni standard verificabili. Nessuna figura del libro viene copiata.

| ID | Cosa aggiungere | Quanto | Dove |
|---|---|---|---|
| RL-01 | Assiomi e teoremi dell'algebra di Boole con la dualità; teorema di espansione di Shannon nelle due forme; mintermini e maxtermini | ~700 parole | Modulo 1 |
| RL-02 | Implicanti primi ed essenziali; encoder e comparatore; termine di consenso contro le alee | ~600 parole | Moduli 1 e 2 |
| RL-03 | Overflow in complemento a 2; sottrattore con il sommatore; comparatore come differenza | ~450 parole | Modulo 2 |
| RL-04 | Perché serve il fronte: trasparenza del latch, oscillazione del JK; FF sul fronte e master-slave; metastabilità in due righe | ~500 parole | Modulo 3 |
| RL-05 | Periodo minimo e vincolo di hold di una rete sincrona; contatore modulo N; cascata di contatori | ~550 parole | Modulo 3 |
| RL-06 | Procedura generale di analisi di una MSF; scelta della codifica degli stati | ~350 parole | Modulo 4 |
| RL-07 | Architettura controllore-datapath, con l'esercizio dei fogli (misura della durata di un impulso) svolto | ~900 parole | Modulo 4, dopo la risposta alla domanda 3 |
| RL-08 | Come si verifica un progetto con il simulatore: stimoli, diagramma temporale atteso, confronto | ~250 parole | Modulo 4 |

## 4. Domande per l'autore

1. **Lezioni mancanti.** Ci sono appunti delle lezioni dopo il 10/12 o delle date senza file (6/10, 15/10, 20/10, 27/10, 12/11, 19/11, 26/11, 3/12)? Alcune erano esercitazioni con il simulatore?
2. **Data della Lezione 11.** Il file non ha la data: è del 24 novembre?
3. **Controllore-datapath e simulazione (RL-07, RL-08).** Sono stati fatti a lezione o nelle esercitazioni? Per ora li scrivo come aggiunte, partendo dalla specifica del foglio 172948.
4. **Virgola mobile.** È stata chiesta all'esame? Per ora resta un riquadro breve senza IEEE 754.
5. **L09, "contatore modulo 8 / INUTILE".** Si parlava del contatore modulo 16 a 4 FF o del contatore decimale (la tabella arriva a 9)?
6. **L07, esercizio 3.** Il terzo fattore della sintesi OR-AND è $(C + \bar{B})$ o $(\bar{C} + \bar{B})$? E il simbolo "≠" fra le due mappe che cosa indica?
7. **L12, lavatrice.** $J_Z$ è "$1 + START \cdot L$" o "$X + Y + START \cdot L$"? Lo stato finale torna in attesa o resta fermo fino al reset?
8. **L09, rilevatore di fronti.** Gli stati sono 2 (come scritto) o 4 (come nel diagramma)?
9. **L02, esercizio del circuito.** Il circuito di partenza dà proprio $F = ADC + \bar{C}(\bar{A}D + A(B + D))$? Se sì, il risultato giusto è $AD + \bar{C}D + AB\bar{C}$.
10. **L03 e L06, mappe 4×4 colorate.** Non sono leggibili con sicurezza: va bene sostituirle con esempi nuovi verificati?
11. **Esercizi del docente.** Va bene usare gli esercizi del simulatore come "esercizi tipo", con il circuito ridisegnato, il testo riscritto e la soluzione nostra?
12. **Esercitazione 09.** Qual era la specifica del ricevitore (pacchetto 1 1 B 0 0)? Senza, le mappe di $J_0$, $K_0$, $J_1$, $K_1$ non si possono controllare e restano fuori.

## 5. Stato dopo le aggiunte (fasi 4-5, 4 novembre 2026)

| ID | Stato | Dove nei moduli |
|---|---|---|
| RL-01 | completo | 1.1-1.4, 1.7 |
| RL-02 | completo | 1.5-1.6, 2.1-2.3 |
| RL-03 | completo | 2.4-2.7 |
| RL-04 | completo | 3.1-3.3 |
| RL-05 | completo | 3.4-3.7 |
| RL-06 | completo | 4.1-4.8 |
| RL-07 | completo, ma come aggiunta | 4.9 (domanda 3) |
| RL-08 | completo, ma come aggiunta | 4.10 (domanda 3) |
