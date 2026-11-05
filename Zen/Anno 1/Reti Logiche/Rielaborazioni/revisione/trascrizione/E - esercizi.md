# Esercizi e fogli sparsi

Trascrizione fedele dei fogli in `Esercizi/` e `_da_verificare/`. Segni usati: `[?]` lettura incerta, `[illeggibile]`. Mappe con X sulle righe; l'ordine delle colonne segue le etichette di ogni foglio.

## `Esercizi/Note_261103_172930.pdf`

> [!figura] Diagramma temporale di A, B, C e dell'uscita, con i valori 0 1 1 1 0 0 1 0 nei successivi intervalli.

Mappa (riga $\bar{A}$: 0 1 1 1; riga A: 0 0 0 1) → $\bar{A}C + B\bar{C}$ (con due porte AND e una porta OR).

> [!figura] Circuito: A, B, C con i negati, due AND e una OR che dà U.

## `Esercizi/Note_261103_172930 - Copia.pdf` (contenuto diverso dal precedente)

Mappa (riga $\bar{X}$: 1 0 1 0; riga X: 1 0 0 1) → $X\bar{Z} + \bar{Y}\bar{Z} + \bar{X}YZ$.

Stessa mappa, sintesi OR-AND → $(X + \bar{Y} + Z)(\bar{X} + \bar{Z})(Y + \bar{Z})$.

Mappa (riga $\bar{X}$: 0 0 1 1; riga X: 0 1 0 1) → $X\bar{Y}Z + \bar{X}Y + Y\bar{Z}$ | $(Y + Z) \cdot (X + Y) \cdot (\bar{X} + \bar{Y} + \bar{Z})$.

$x + xy + xyz + xyzw + xz + xw + xzw = x(1 + y(1 + z + zw) + z + w + zw) = x(1 + (y + 1)(1 + z + zw))$ [= x].

Tabelle X Y | U e X Y Z | U con le colonne lette come numeri esadecimali (1111 1011 → FB; 0011 1100 → 3C; 1110 → E).

Semplificazioni con la notazione "!" per la negazione:

- $B = XY + !XZ$;
- $(XY + YZ + !XZ) \cdot ![(XY + !XZ)] + X$ → $(B + YZ)!B + X$ → $!BB + !BYZ + X$ → $!BYZ + X$ → $(!X + !Y)(X + !Z) \cdot YZ + X$ → $(!X!Z + X!Y + !Y!Z)YZ + X$ → $!XY + XZ + X$ [?];
- $(XY + YZ + !XZ) \cdot (!X!Z + X!Y + !Y!Z) + X + XY$; $!(XY) \cdot !(!XZ) = (!X + !Y)(X + !Z)$;
- $A + BC + BD = A + B(C + D)$; $!Z(!X + !Y) \cdot X!Y$ [?].

## `Esercizi/Note_261103_172948.pdf`

5 bit: bit d'inizio, $B_0$, $B_1$, $B_2$, bit di fine; ogni bit dura un clock. 3 FF E-PET ($Q_0$, $Q_1$, $Q_2$). LNA, LNB → sequenze seriali d'uscita.

Solito controllo: se il pacchetto non arriva giusto niente output; se la sequenza è corretta → $Q_2 = 0$ → uscita segnale su LNA, $Q_2 = 1$ → uscita segnale su LNB. Poi c'è P, che è l'EXOR tra $Q_0$ e $Q_1$.

X Y Z W K [variabili di stato?].

Il sistema riceve in ingresso un segnale IN: solitamente = 0; segnali che durano da 1 a 7 impulsi di CK. Il sistema misura la durata degli impulsi e trasmette il valore sulla linea (uscita SER); il sistema usa CNT.

- FSM-A → avvisa FSM-B attraverso TRG quando è terminato l'impulso, dicendo che in $Q_0$-$Q_1$-$Q_2$ ci sono i valori della durata dell'impulso. Quando necessario FSM-A azzera i valori su CNT attraverso CL. Quando il sistema è alla ricerca di un segnale, FSM-A attiva BSY.
- FSM-B → genera l'uscita SER quando riceve l'impulso TRG: i bit di uscita sono start bit "1" – $Q_0$ – $Q_1$ – $Q_2$ – stop bit "0". Genera l'uscita ETX per informare FSM-A dell'invio del dato su SER.

## `Esercizi/Note_261103_172951.pdf`

> [!figura] Schermata di un diagramma ASM del simulatore: a (00) con i rombi IN1, IN2; b (01) cancellato con un tratto; un blocco di uscita condizionata cancellato con "NO"; c (10, OUT).

> [!figura] Ricevitore: ingresso LN, uscite OK ed ERR; pacchetto 1 1 B 0 0 [?]; un FF JK esterno (B) comandato dalla MSF con J e K.

> [!figura] Foto di un ASM disegnato su carta: a con il rombo LN, poi rombi LN in cascata; rami con gli stati K e J (che comandano il FF esterno); una parte tratteggiata in rosso (cancellata); in fondo gli stati OK ed ERR; correzioni in blu sui ritorni.

## `Esercizi/esercitazione 09_261103_172946.pdf`

Mappa degli stati (riga $\bar{X}$: a, b, d, c [?]; riga X: e, f, –, –) [la codifica in alto: XYZ = 000].

Tabella di eccitazione del JK (0 → 0: 0 –; 0 → 1: 1 –; 1 → 0: – 1; 1 → 1: – 0) e tabella J K | $Q_t$ (00 → $Q_{t-1}$, le altre righe non compilate).

(Scritta a margine, non pertinente.) Mappe delle uscite:

- $K_0 = \overline{LN}\,\bar{X}YZ$ [?] (riga $\bar{X}$: 0, $\overline{LN}$, 0, 0; riga X: 0, 0, –, –);
- $J_0 = LN\,\bar{X}YZ$ [?] (riga $\bar{X}$: 0, LN, 0, 0; riga X: 0, 0, –, –);
- $K_1 = \overline{LN}\,Y\bar{Z}$ [?] (riga $\bar{X}$: 0, 0, 0, $\overline{LN}$; riga X: 0, 0, –, –);
- $J_1 = LN\,Y\bar{Z}$ [?] (riga $\bar{X}$: 0, 0, 0, LN; riga X: 0, 0, –, –);
- OK (riga $\bar{X}$: 0 0 0 0; riga X: 0 0 – –) → $OK = X\bar{Z}$;
- ERR (riga $\bar{X}$: 0 0 0 0; riga X: 0 1 – –) → $ERR = XZ$.

## `_da_verificare/Note_261103_172950.pdf`

Numero "1444444425" in testa e disegni confusi di blocchi e rombi, senza testo leggibile: non usato.
