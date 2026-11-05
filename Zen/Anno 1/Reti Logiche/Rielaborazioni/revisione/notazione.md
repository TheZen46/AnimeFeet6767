# Reti Logiche · notazione comune

Notazione proposta per tutti i moduli. Dove gli appunti usano due forme per la stessa cosa, la tabella indica quale si tiene.

## Algebra e funzioni

| Oggetto | Notazione | Note |
|---|---|---|
| Insieme dei valori | $\mathbb{B} = \{0, 1\}$ | Come in L01 |
| Negazione | $\bar{A}$ | Negli esercizi compare anche $!A$ (stile C) e $A'$: si usa solo $\bar{A}$; per espressioni lunghe $\overline{A + B}$ |
| AND, OR | $A \cdot B$ o $AB$, $A + B$ | Il punto solo quando aiuta la lettura |
| XOR, XNOR | $A \oplus B$, $\overline{A \oplus B}$ | – |
| Somma di prodotti, prodotto di somme | SOP (forma AND-OR), POS (forma OR-AND) | Negli appunti "SH1" e "SH2": si dice una volta che corrispondono alle due forme del teorema di Shannon |
| Indifferenza | – (trattino) | Negli appunti anche "X" maiuscola in qualche mappa: la X è riservata alle variabili riportate e di stato |

## Mappe di Karnaugh

| Oggetto | Notazione | Note |
|---|---|---|
| Ordine di righe e colonne | Codice Gray 00, 01, 11, 10, con le variabili scritte nell'angolo ($AB \backslash CD$) | Negli appunti le etichette sono sui lati e in L11, L12 l'ordine delle colonne è YZ = 00, 10, 11, 01: tutte le mappe si riscrivono nell'ordine standard |
| Mappe nel testo | Tabelle Markdown con la prima colonna per le righe | – |
| Variabili riportate | Lettere minuscole o maiuscole come negli appunti ($x$, $y$, $I$), dentro le celle | – |

## Circuiti sequenziali

| Oggetto | Notazione | Note |
|---|---|---|
| Stato presente e successivo | $Q$ (o $X$) e $Q^+$ (o $X^+$) | Negli appunti $Q_t$ e $Q_{t-1}$, $I_x$ per lo stato successivo: si usa $Q^+$ nelle tabelle e $D_X$, $J_X$, $K_X$ per gli ingressi dei FF |
| Ingressi attivi bassi | $\overline{RES}$, $\overline{PR}$, $\overline{CL}$ | – |
| Clock | CK | Negli appunti anche "Clock": si usa CK |
| Fronte | PET (*positive edge triggered*), NET (*negative edge triggered*) | – |
| Tabella caratteristica e di eccitazione | caratteristica: ingressi → $Q^+$; eccitazione: transizione $Q \to Q^+$ → ingressi | Negli appunti di L06-L07 "tabella di eccitazione" indica la caratteristica: si corregge |
| Tempi | $t_s$ (*setup*), $t_h$ (*hold*), $t_p$ (con $t_{PLH}$, $t_{PHL}$), $t_w$, $T_{min}$, $f_{max}$ | – |

## Macchine a stati

| Oggetto | Notazione | Note |
|---|---|---|
| Nomi degli stati | lettere minuscole a, b, c, … o nomi brevi (wait, L1, stop) | Come negli appunti |
| Codifica | variabili di stato $X$, $Y$, $Z$ (o $X_1$, $X_0$) con lo stato scritto come $XYZ = 010$ | – |
| ASM | blocco di stato (rettangolo con il nome a lato e il codice sopra), blocco condizionale (rombo, uscite 0 e 1), uscita condizionata (ovale) | Nelle uscite si scrivono solo quelle che valgono 1, come in L09 |
| Macchina | MSF (macchina a stati finiti), con FSM come sinonimo inglese solo alla prima occorrenza | Negli esercizi compare FSM-A, FSM-B: nei nomi dei blocchi si tiene |

## Incoerenze trovate

- Ordine delle colonne delle mappe diverso fra le lezioni (vedi sopra).
- "Tabella di eccitazione" usata per due cose diverse (L06-L07 contro L11-L12).
- $T_{min}$ chiamato frequenza (L08).
- Lo stato successivo indicato come $I_x$ (L09-L10), $Q_t$ (L08), "stato successivo" (L11): si uniforma a $Q^+$ o $X^+$.
