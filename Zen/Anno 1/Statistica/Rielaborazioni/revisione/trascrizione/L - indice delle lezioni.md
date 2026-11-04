# Indice delle lezioni scritte a mano

Gli appunti del corso sono in due serie, tutte e due dell'autore:

- **serie A** (`Appunti_mano/`, tablet Samsung): lezioni 1-7, una pagina fitta per lezione;
- **serie B** (`_da_verificare/Lezioni iPad/`, iPad): lezioni 5-22, più distese e complete.

Le lezioni 5-7 sono in tutte e due le serie: per quelle si è seguita la serie B, più completa, controllando la A. Le pagine sono state lette tutte; i calcoli degli esempi usati nei moduli sono stati rifatti (`strumenti/verifica.py`). Qui sotto, per ogni lezione, gli argomenti e gli esempi nell'ordine degli appunti, con i punti corretti segnati da ⚠.

## Statistica descrittiva (serie A)

**L01 · mer 25/02/2026.** Dati, unità sperimentale, numerosità del campione; variabili quantitative (valori reali o vettori: una matrice, un'immagine) e qualitative (valori in un "dizionario"). Valori distinti, frequenze assolute e relative. Esempio: i 253 iscritti al corso divisi per corso di laurea (134 gestionale, 111 informatica, 8 altro: 53%, 44%, 3%); diagramma a barre e a torta. Tabella a due vie corso di laurea × nazionalità (italiani 127, 101, 6; stranieri 7, 10, 2), frequenze congiunte e marginali, profili riga e colonna. Notazione $n_{ij}$, $f_{ij}$, $n_{i\cdot}$, $n_{\cdot j}$.

**L02 · gio 26/02/2026.** Esercizio: 50 persone, genere × colore degli occhi (F 5, 8, 7; M 4, 6, 20): frequenze relative, marginali, profili riga e colonna. Esempio del test diagnostico (malattia all'1%, 1000 persone, falsi positivi 10%, falsi negativi 20%): fra i positivi solo il 7,5% è malato. Regola del prodotto $f_{ij} = f_{j\mid i}\, f_{i\cdot}$. Funzione di distribuzione cumulata empirica, a gradini.

**L03 · mar 03/03/2026.** Media empirica (anche dalle frequenze); proprietà: sta fra minimo e massimo, si trasforma linearmente; dati centrati. Quartili e mediana definiti con le frequenze cumulate.

**L04 · mer 04/03/2026.** Boxplot (scatola, baffi, mediana). Media e mediana a confronto: con i dati 1, …, 10 la media è 5,5; sostituendo 10 con 100 la media sale a 14,5 e la mediana resta 5. Percentili; esempio con otto valori e frequenze 1/6, 1/12 (Q1 = 4, Q2 = 8, Q3 = 10; 10°, 30°, 90° percentile 1, 4, 12). ⚠ La mediana è scritta in modo ambiguo ("58"): è 8. Varianza della popolazione $\sigma^2$ e del campione $s^2$, deviazione standard, unità di misura; esempio dei due studenti con media 24 (tutti 24 / metà 18 e metà 30). Proprietà della varianza. Coefficiente di correlazione e sue proprietà; esempio di tabella a due vie $X \in \{1, 2\}$, $Y \in \{-1, 0, 1\}$, non svolto (svolto nel modulo 1).

Il formulario a mano (`Formulari e riassunti/Formulario.pdf`) aggiunge il boxplot con i limiti $Q_1 - \frac32 \mathrm{IQR}$, $Q_3 + \frac32 \mathrm{IQR}$ e la retta dei minimi quadrati (errore di Laplace e di Legendre-Gauss, teorema della retta $y = \bar y + \rho \frac{\sigma_y}{\sigma_x}(x - \bar x)$): la lezione sulla regressione non è fra gli appunti.

## Probabilità (serie B, con la A per le lezioni 5-7)

**L05 · mar 10/03/2026 (2 h).** Esperimento aleatorio, spazio campionario (moneta, dado, prima testa, altezza), eventi e operazioni, disgiunti. Assiomi della probabilità. Dado equilibrato, casi favorevoli su casi possibili. Due dadi (somma 7: 1/6; somma 11: 1/18), tre dadi (somma 9: 25/216; somma 10: 1/8).

**L06 · mer 11/03/2026 (3 h).** ⚠ Nella serie A il file è datato 11/02: la data giusta è 11/03. Proprietà della probabilità, inclusione-esclusione. Problema dei compleanni, con l'approssimazione $1 - e^{-n(n-1)/730}$ e la probabilità che qualcuno sia nato il proprio giorno; tabella incollata (non ripresa). Spazi finiti ed equiprobabili, moneta truccata. Calcolo combinatorio: fattoriale, binomiale, disposizioni e combinazioni con e senza ripetizione, proprietà del binomiale, binomio di Newton.

**L07 · mer 18/03/2026 (3 h).** Urna con 12 rosse e 8 bianche (2 e 2 su 4 estratte: 38%); terno secco al lotto (1/11748, vincita equa); coincidenze nelle estrazioni (1/10); poker (doppia coppia 4,8%, full 0,14%); monomi di grado 6 in tre variabili (5/14). Probabilità condizionata, con esempi (due carte di fiori, dado a 4 facce, scala reale), regola del prodotto e della catena; dieci coppie in dieci cabine.

**L08 · "18/03/2026" (2 h).** ⚠ Stessa data della L07: una delle due è sbagliata (la L08 è probabilmente del 24 o 25 marzo). Probabilità totali; seconda carta di fiori (1/4); dado e lanci di moneta (4 teste: 29/384). Formula di Bayes (prima carta di fiori sapendo la seconda: 4/17; dado sapendo 4 teste: 10/29); exit poll (12/23). Indipendenza di due e tre eventi, differenza fra disgiunti e indipendenti; moneta truccata (2 teste e 1 croce: 4/9).

## Variabili aleatorie (serie B)

**L09 · mer 25/03/2026 (3 h).** Variabile aleatoria, eventi $\{X \in I\}$, finite e discrete; esempi (teste in 3 lanci, lanci fino alla prima testa, tempo d'attesa, indicatrice). Legge di una variabile, tabella e grafico; 3 lanci di moneta equilibrata e truccata. Variabili diverse con la stessa legge.

**L10 · mer 01/04/2026 (2 h).** Variabili discrete, somma della serie (lanci fino alla prima testa, in base 2). Variabili con densità; proprietà; esempi: uniforme su $(\frac12, 1)$, $f(x) = mx$, densità a tratti con due parametri, densità di Cauchy.

**L11 · mer 08/04/2026 (3 h).** Funzione di ripartizione nel caso discreto e con densità, proprietà, teorema inverso; esempio $F(x) = \sqrt x$. Funzioni di variabili aleatorie: caso discreto (gioco da 11 euro con 4 lanci, $Y = X^2 - 2X - 3$) e caso con densità (due metodi).

**L12 · gio 09/04/2026 (2 h).** Esempi: $Y = -3X + 1$ con $f_X(x) = 2x$; $Y = (3X - 1)^2$ con $X$ uniforme; una variabile mista. ⚠ Nella densità $f_X$ e in $f_Y$ compare "1" al posto di 0 fuori dall'intervallo.

## Valori attesi e leggi notevoli (serie B)

**L13 · data non scritta (probabilmente mer 15/04/2026).** Speranza nei casi finito, discreto e con densità; esempi (moneta, dado, $2x$, esponenziale, una densità senza speranza finita). Proprietà, formula di trasferimento, formula delle code; speranza della geometrica; $Y = \sin X$.

**L14 · gio 16/04/2026 (2 h).** Speranza condizionata e formula delle torri. ⚠ Urna con 12 monete equilibrate e 8 truccate: il risultato è $\frac{13}{10}$, non $\frac{13}{20}$ come scritto. Dado e lanci di moneta ($\frac72 p$). Varianza e proprietà, disuguaglianza di Chebyshev, varianze di indicatrice e uniformi. Covarianza e correlazione, proprietà; variabili scorrelate ma non indipendenti; esempio di legge congiunta (cov = −1/16).

**L15 · mer 22/04/2026.** Bernoulli, binomiale (dado lanciato 8 volte; urna con 7 monete equilibrate e 3 truccate), geometrica e assenza di memoria. ⚠ Nell'esercizio dell'urna la domanda b) dice "3 teste" ma il calcolo usa 2 teste: si tiene 2.

**L16 · gio 23/04/2026 (2 h).** Lotto: il numero che non esce da 257 estrazioni. Pascal; esempi con la moneta; tempi di primo e secondo successo. Poisson (⚠ "Pascal(λ)" scritto al posto di Poisson), approssimazione della binomiale; overbooking; sito web.

**L17 · mer 29/04/2026 (3 h).** Banca con due sportelli (somma e condizionamento di Poisson). Ipergeometrica, confronto con la binomiale (lampadine). Urna con due estrazioni senza reimmissione. Uniforme discreta e continua (⚠ funzione di ripartizione scritta senza il valore 1 per $x > b$). Esponenziale, assenza di memoria, call center.

**L18 · gio 30/04/2026 (2 h).** Normale standard e generale, proprietà, funzione di ripartizione $\Phi$, maggiorazione delle code, uso delle tavole; esempio $N(1; 0{,}16)$.

**L19 · mer 06/05/2026 (2 h).** Quantili e valori critici; altezze degli studenti (⚠ $\delta = 8 \cdot 0{,}6745 \approx 5{,}40$ cm, non 5,46); biscotti in gita. Legge dei grandi numeri e teorema del limite centrale.

**L20 · gio 07/05/2026 (2 h).** Intervalli per la media dal TLC e da Chebyshev, tabella dei coefficienti. Moneta lanciata 100 volte (esatto, Chebyshev, TLC; numero di lanci). Ristorante con Poisson(225) e un caso in cui il TLC non si applica.

## Inferenza (serie B)

**L21 · mer 13/05/2026 (3 h).** Popolazione, parametro, campione, stima e stimatore; stimatori corretti e consistenti, errore quadratico medio; media e varianza campionaria (con dimostrazione). Intervallo di confidenza per la media con varianza nota, interpretazione; esempio dei pesci (⚠ numerosità 245,2 da arrotondare a 246). Intervalli per una proporzione.

**L22 · gio 14/05/2026 (2 h).** Moneta con 60 teste su 100 (⚠ scritto "α = 5%" per il livello del 90%). Leggi chi-quadro e t di Student; teorema sui campioni normali; intervalli per la media con varianza ignota e per la varianza; esercizi (pezzi venduti, ore di straordinario); schema riassuntivo.

Gli appunti finiscono qui. Le lezioni successive (test di ipotesi, confronto di medie, chi-quadro, ANOVA) non ci sono.
