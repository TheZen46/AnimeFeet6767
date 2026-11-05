# Analisi Matematica 1A · fase 3: struttura in moduli

> Approvata il 3 novembre 2026 così com'è, con la strada A per le aggiunte: il materiale delle lezioni mancanti non era disponibile.

## Numero di moduli

Analisi 1A non è ancora in `catalog.yaml`. Con 6 CFU (circa 60 ore) e la regola di circa 12 ore per modulo, i moduli sono **5**. L'ordine è quello del programma, con uno spostamento: il teorema del limite della derivata va dopo de l'Hôpital, perché la dimostrazione lo usa (negli appunti lo precede).

Le parole sono stimate dalla trascrizione, formule comprese. A circa 450 parole per pagina, il corso intero verrebbe sulle 35 pagine A4.

| Modulo | Titolo | ID | Lezioni | Parole (appunti + aggiunte) | Aggiunte |
|---|---|---|---|---|---|
| 1 | Numeri reali e funzioni | AM1A-01…07, 18 | L02, L03, L04, Formulario | ~2000 + ~1500 | **~40%** |
| 2 | Successioni e limiti | AM1A-08, 09 | L05, L06, L07 (sottosuccessioni), Formulario | ~1900 + ~1300 | **~40%** |
| 3 | Continuità e confronto locale | AM1A-10, 11, 15 (asintoti) | L05, L06, L07, L08 | ~2300 + ~400 | ~17% |
| 4 | Derivate e teoremi del valor medio | AM1A-12, 13, 16 | L08, L09, L10 | ~2700 + ~500 | ~18% |
| 5 | Monotonia, convessità, studio di funzione e Taylor | AM1A-14, 15, 17 | L09, L10, L11 | ~2400 + ~1300 | **~55%** |

Nei moduli 1, 2 e 5 le aggiunte superano di molto il 15%, perché mancano gli appunti di due lezioni e della fine del corso. Ci sono tre strade possibili:

- **A.** Faccio tutte le aggiunte, segnate come `[!aggiunta]` con la fonte. Il prodotto è completo, ma un terzo dei moduli 1, 2 e 5 è scritto da me sul Canuto-Tabacco, e va controllato con più attenzione.
- **B.** Aggiungo solo ciò che serve a non lasciare buchi logici: definizioni usate prima di essere date, teoremi citati, dimostrazioni interrotte. Il resto lo segnalo come "non trattato in questi appunti". Le aggiunte scendono a circa il 15-20%.
- **C.** Prima recuperi il materiale delle lezioni mancanti (domande 1 e 2 di `01-copertura.md`), poi decidiamo.

Ti consiglio la **C**, e se non c'è materiale la **A**. Un esame a esercizi richiede argomenti completi, e chi compra il modulo 2 si aspetta i teoremi sui limiti.

## Schema di ogni modulo

- `# N · Titolo`, poi il paragrafo "In questo modulo" con i prerequisiti (i moduli precedenti, per nome) e gli obiettivi presi dal programma ufficiale.
- Sezioni `## N.1`, `## N.2`, …: definizioni, enunciati e dimostrazioni nei callout `[!definizione]` e `[!teorema]`, poi il commento in prosa.
- "Esempi ed esercizi svolti" alla fine di ogni sezione o del modulo. Vengono dagli esempi degli appunti e dagli esercizi del formulario. L'esame è a esercizi, e oggi gli appunti ne hanno pochi.
- "Riepilogo" in prosa, con le formule e i risultati chiave.

## Modulo 1 · Numeri reali e funzioni

ID: AM1A-01, 02, 03, 04 (per le funzioni), 05, 06, 07, 18. Prerequisiti: nessuno.

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 1.1 Insiemi numerici | $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$; scrittura decimale; proprietà algebriche e di ordine | L02 § 1.1 | Retta orientata, densità di $\mathbb{Q}$ (AM1A-01) |
| 1.2 Valore assoluto e intervalli | Definizione, disuguaglianza triangolare e la sua conseguenza; tipi di intervallo | L02 | – |
| 1.3 Estremo superiore e inferiore | Maggioranti e minoranti, massimo e minimo, sup e inf, caratterizzazione, completezza | L02 | Conclusione dell'esempio $\sqrt{2}$ |
| 1.4 Induzione e coefficienti binomiali | Principio di induzione; fattoriale, binomiali, formula di Stifel | L03 | Induzione con un esempio (AM1A-18, solo dopo la tua risposta alla domanda 4) |
| 1.5 Funzioni | Definizione, dominio, codominio, immagine, controimmagine, grafico; esempi | L02 § 2.1, L04 § 2.1 | – |
| 1.6 Iniettività, inversa, restrizione, composizione | Definizioni, osservazioni, esempi con $x^2$ | L04 | – |
| 1.7 Funzioni monotone | Definizioni, esempi, "strettamente monotona ⇒ iniettiva" e il controesempio $1/x$ | L04 | – |
| 1.8 Funzioni elementari | Potenze con esponente naturale, razionale, reale, negativo | L04 § 2.2, Formulario | Esponenziali e logaritmi; funzioni trigonometriche e inverse con identità e grafici (AM1A-02, 06) |
| 1.9 Grafici e operazioni sulle funzioni | – | – | Traslazioni, dilatazioni, simmetrie, valore assoluto (AM1A-03) |

## Modulo 2 · Successioni e limiti

ID: AM1A-08, 09. Prerequisiti: modulo 1.

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 2.1 Intorni | Intorni di un punto e degli infiniti | L05 § 3.1 | – |
| 2.2 Limiti di successioni | Convergenza, divergenza, successioni indeterminate; esempi $1/n$ e $n^2$ | L05 § 3.2 | – |
| 2.3 Successioni monotone e numero $e$ | Teorema con dimostrazione; $(1 + 1/n)^n$ | L05 § 3.2 | Dimostrazione che $(1 + 1/n)^n$ è crescente e limitata |
| 2.4 Sottosuccessioni | Definizione, esempi con $(-1)^n$, limite delle sottosuccessioni | L07 § 4.5 | – |
| 2.5 Limiti di funzione | Limiti all'infinito e al finito; esempio svolto con $\varepsilon$ e $B$ | L05 § 3.3 | Casi con $-\infty$ mancanti; limite destro e sinistro |
| 2.6 Teoremi sui limiti | – | – | Unicità, permanenza del segno, confronto, algebra dei limiti (il § 4.1 mancante) |
| 2.7 Forme indeterminate | Elenco; polinomi e funzioni razionali all'infinito | L06 § 4.2 | – |
| 2.8 Limiti notevoli | $\sin x / x$, $\tan x / x$, $(1 - \cos x)/x^2$, arcsin, arctan, logaritmo ed esponenziale | L06 § 4.2, Formulario | Dimostrazione di $\sin x / x \to 1$ |
| 2.9 Sostituzione | Teorema, esempio, uso per mostrare che un limite non esiste ($\sin y$) | L06 § 4.3 | Forme $1^\infty$, $0^0$, $\infty^0$ |

## Modulo 3 · Continuità e confronto locale

ID: AM1A-11, 10, 15 (asintoti). Prerequisiti: moduli 1 e 2.

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 3.1 Funzioni continue | Definizione, legame con il limite, continuità della composta | L05 § 3.3, L06 § 4.3 | Tipi di discontinuità |
| 3.2 Permanenza del segno ed esistenza degli zeri | Enunciati, dimostrazione per bisezione, esempi (polinomi di grado dispari, $e^x + \sin x$) | L06 § 4.4, L07 § 4.4 | Fine della dimostrazione |
| 3.3 Valori intermedi | Teorema, corollario sull'immagine di un intervallo, controesempi | L07 § 4.4 | – |
| 3.4 Teoremi di Bolzano-Weierstrass e di Weierstrass | Enunciati e dimostrazioni | L07 § 4.5 | – |
| 3.5 Continuità, monotonia e inversa | Iniettiva ⇔ strettamente monotona su un intervallo; continuità dell'inversa | L07 § 4.5 | – |
| 3.6 Asintoti | Orizzontali e obliqui; esempio | L07 § 5.1 | Asintoti verticali |
| 3.7 Infinitesimi, infiniti e simboli di Landau | $O$, $o$, $\sim$; ordine, campioni, parte principale | L08 § 5.2 | – |

## Modulo 4 · Derivate e teoremi del valor medio

ID: AM1A-12, 13, 16. Prerequisiti: moduli 2 e 3.

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 4.1 Derivata | Rapporto incrementale, derivata, significato geometrico, derivabile ⇒ continua | L08 § 6.1 | – |
| 4.2 Derivate delle funzioni elementari | Costanti, seno, coseno, esponenziale, potenze, tangente, logaritmo, inverse trigonometriche | L08, L09 | Calcolo di arcsin' e arctan' |
| 4.3 Regole di derivazione | Somma, prodotto, catena, quoziente, inversa | L08, L09 | Dimostrazione corretta della catena (inventario, bloccante 5) |
| 4.4 Derivata destra e sinistra | Punti angolosi, cuspidi, flessi a tangente verticale; esercizio con $\alpha$ e $\beta$ | L09 | Conclusione dell'esercizio |
| 4.5 Estremi e teorema di Fermat | Definizioni (corrette), punti critici, Fermat | L09 § 6.2 | – |
| 4.6 Rolle, Cauchy, Lagrange | Enunciati, dimostrazioni, formule dell'incremento finito, funzioni a derivata nulla | L09 § 6.3, L10 | – |
| 4.7 Teorema di de l'Hôpital | Enunciato | L10 § 6.7 | Dimostrazione (caso $0/0$ da destra) |
| 4.8 Limite della derivata | Teorema e corollari | L09 | – (spostato qui) |

## Modulo 5 · Monotonia, convessità, studio di funzione e Taylor

ID: AM1A-14, 15, 17. Prerequisiti: modulo 4.

| Sezione | Contenuto | Origine | Aggiunte |
|---|---|---|---|
| 5.1 Monotonia e segno della derivata | Teorema e dimostrazione | L09 § 6.4 | Dimostrazione di "⇐" e di (II) |
| 5.2 Ricerca degli estremi | Criterio del segno di $f'$; esempio $x \arctan x$ | L10 | – |
| 5.3 Derivate successive | Derivata seconda, derivate di ordine $k$, classi $C^k$ | L10 § 6.5 | – |
| 5.4 Convessità e flessi | Definizioni, legame con $f'$ e $f''$, esempi | L10 § 6.5 | – |
| 5.5 Studio di funzione | Schema dei passi | L10 § 6.6 | Uno studio completo con grafico |
| 5.6 Formula di Taylor | Polinomio, resto di Peano (con dimostrazione) e di Lagrange | L11 § 7.1 | – |
| 5.7 Sviluppi notevoli e operazioni | $e^x$, $\ln(1+x)$, $\sin x$; unicità; somma, prodotto, quoziente | L11 | $\cos x$, $(1+x)^\alpha$, $\arctan x$, $1/(1-x)$; composizione; fine del quoziente |
| 5.8 Applicazioni degli sviluppi | – | – | Limiti, ordine di infinitesimo, natura dei punti critici (AM1A-17) |

## Cosa approvare

1. Numero e titoli dei moduli.
2. Strada A, B o C per le aggiunte.
3. Lo spostamento del limite della derivata nel modulo 4, dopo de l'Hôpital.
4. La sezione "Esempi ed esercizi svolti" in ogni modulo: va bene che io completi gli esercizi del formulario e degli appunti, segnando i conti rifatti nel registro?

Scrivi "approvo" con le eventuali modifiche, e rispondi alle domande di `01-copertura.md`.
