---
corso: Ricerca Operativa
lezione: 9
data: 2026-10-23
docente: Silvia Villa
argomenti: [forma tableau, operazioni di pivot, cambio di base senza inversione, esempio completo di fase 2, interpretazione geometrica del simplesso, scelta della variabile entrante, convergenza della fase 2, iterazioni degeneri, ciclaggio, esempio di Beale, regola di Bland, complessità del simplesso, metodi di punto interno, fase 1, variabili artificiali, problema ausiliario]
fonti: [trascrizione, appunti manuali, dispense]
tags: [ricerca-operativa, lezione]
---

# Lezione 9 — Forma tableau, convergenza e ciclaggio

> [!info] Fonti di questa nota
> Trascrizione della lezione (un'unica parte; la ripresa dopo la pausa è registrata solo in parte), appunti manuali (scansione della lezione 9, due pagine, ricevuta in due copie identiche) e dispense [@roma2023, §6.4.4–6.4.6, §6.5]. Le note di Di Summa [@disumma2015, §3.1, §3.4–3.6, §5.2] trattano la forma tableau, il ciclaggio e la complessità. Le parti prese solo da queste fonti, e i calcoli aggiunti per verifica, sono indicati esplicitamente.

> [!warning] Discrepanza tra fonti — data della lezione
> La trascrizione riporta come data di registrazione il **25/10/2026** (una domenica), gli appunti scansionati il **23/10/2026** (un venerdì). La data di registrazione delle trascrizioni segue la lezione di uno o due giorni (lo stesso accade nelle lezioni 10 e 11), quindi nel front-matter è indicato il 23/10.

La lezione chiude la **fase 2** del metodo del simplesso. Si introduce la **forma tableau**, che permette di passare da una base alla successiva con operazioni di **pivot** (i passi del metodo di Gauss), senza mai invertire matrici. Si risolve un esempio completo, interpretandolo sul disegno. Poi si discute la **convergenza**: il metodo termina se non ripete mai una base, ma con le basi degeneri può **ciclare**; la **regola di Bland** lo impedisce. In chiusura si apre la **fase 1** con il metodo delle **variabili artificiali**.

## Il problema: cambiare base senza invertire

Nella [[Lezione 08 - Test di illimitatezza e cambio di base|lezione 8]] si è visto quale variabile entra e quale esce. Per scrivere la nuova forma canonica bisognerebbe costruire la nuova matrice di base e invertirla. Si vuole evitare questo passaggio: si opererà direttamente sui coefficienti delle equazioni con i passi del **metodo di eliminazione di Gauss**, che non cambiano l'insieme delle soluzioni del sistema lineare.

## La forma tableau

Per scrivere tutto in forma matriciale c'è un'idea "non molto furba, ma che aiuta": trasformare la funzione obiettivo in un vincolo. Si introduce una variabile $x_0$ che vale esattamente $c^T x$:

$$
\begin{cases}
\min\ c^T x \\
Ax = b \\
x \ge 0
\end{cases}
\qquad\Longleftrightarrow\qquad
\begin{cases}
\min\ x_0 \\
-x_0 + c^T x = 0 \\
Ax = b \\
x \ge 0 .
\end{cases}
$$

Così la funzione obiettivo diventa un'equazione come le altre, e si potrà operare anche sui suoi coefficienti. Interessa però lavorare su problemi già in **forma canonica**. Fissata una base ammissibile $B$, come nelle lezioni 7 e 8, si scrivono le variabili in base in funzione di quelle fuori base e la funzione obiettivo usando solo le variabili fuori base:

$$
\begin{cases}
\min\ x_0 \\
-x_0 + \gamma^T x_N = -\bar x_0 \\
x_B + \bar N x_N = \bar b \\
x \ge 0
\end{cases}
\qquad
\begin{aligned}
\gamma^T &= c_N^T - c_B^T B^{-1} N && \text{(costi ridotti)} \\
\bar x_0 &= c_B^T B^{-1} b && \text{(valore nella SBA corrente)} \\
\bar N &= B^{-1} N, \quad \bar b = B^{-1} b .
\end{aligned}
$$

Le barre servono a non portarsi dietro $B^{-1}$ ogni volta. La prima equazione è $x_0 = \bar x_0 + \gamma^T x_N$, cioè la funzione obiettivo in forma canonica.

> [!warning] Discrepanza nella trascrizione — $\gamma_N$
> A lezione il vettore dei costi ridotti è stato scritto prima come $\gamma_N$ e la docente si è corretta: $\gamma$ moltiplica già soltanto le variabili fuori base e si indica semplicemente con $\gamma$. Negli appunti compare ancora "$\gamma = (\gamma_B, \gamma_N)$", residuo della stessa svista.

**Il tableau.** Si scrive la matrice dei coefficienti di questo sistema, supponendo per il momento che le variabili in base siano le prime $m$:

$$
\begin{array}{c|ccc|ccc|c}
 & x_{B} & & & x_N & & & \\ \hline
x_0 & 0 & \cdots & 0 & \gamma_1 & \cdots & \gamma_{n-m} & -\bar x_0 \\ \hline
x_{B_1} & & & & & & & \\
\vdots & & I_m & & & \bar N & & \bar b \\
x_{B_m} & & & & & & &
\end{array}
$$

- La **riga 0** è quella della funzione obiettivo, diversa dalle altre (per questo la si separa con una linea): le variabili in base hanno coefficiente $0$, quelle fuori base hanno i **costi ridotti**, e a destra c'è $-\bar x_0$, il valore della funzione obiettivo nella SBA corrente **cambiato di segno**.
- Le altre righe sono i vincoli: sotto le variabili in base c'è l'**identità**, sotto quelle fuori base $\bar N = B^{-1}N$, a destra $\bar b = B^{-1} b$.

C'è anche la colonna di $x_0$, con $-1$ nella riga 0 e $0$ altrove. Le operazioni sulle righe le lasciano sempre così (si sottraggono multipli di zero), quindi "siccome ai matematici non piace fare fatica inutile" la colonna non si scrive.

Perché sotto le variabili in base c'è l'identità? Perché $Ax = b$ si scrive $B x_B + N x_N = b$ e, moltiplicando per $B^{-1}$, $x_B + B^{-1}N x_N = B^{-1}b$: nella prima equazione compare solo la prima variabile in base, nella seconda solo la seconda, e così via. Ne segue un fatto importante: **ogni riga del tableau è associata a una variabile in base**, quella che ha $1$ in quella riga. Si annota il suo nome a sinistra della riga.

Nella pratica le colonne **non si riordinano**: le variabili restano nel loro ordine naturale ($x_1, x_2, \dots$, annotate in alto), altrimenti a ogni passo bisognerebbe spostare colonne e si farebbe confusione. Le colonne delle variabili in base sono allora colonne della matrice identità sparse nel tableau.

**Che cosa si legge dal tableau.** Tutti i passi della fase 2 si fanno guardando il tableau.

| passo | dove guardare | che cosa fare |
| --- | --- | --- |
| test di ottimalità | riga 0, colonne delle variabili | se non ci sono elementi negativi la SBA è ottima |
| test di illimitatezza | per ogni $\gamma_h < 0$, la colonna sotto $\gamma_h$ (è la colonna di $\bar N$) | se non ha elementi strettamente positivi il problema è illimitato |
| variabile entrante | riga 0 | una colonna $h$ con $\gamma_h < 0$ (nel corso: la più negativa) |
| variabile uscente | colonna $h$ e colonna $\bar b$ | rapporti $\bar b_i / \bar N_{ih}$ per $\bar N_{ih} > 0$; la riga $k$ del minimo |
| SBA corrente | colonna $\bar b$ e nomi delle righe | variabili in base $=\bar b$, le altre $= 0$; valore $=-(\text{angolo in alto a destra})$ |

## L'operazione di pivot

Si supponga di aver scelto la colonna $h$ (con $\gamma_h < 0$) e, col rapporto minimo, la riga $k$. L'elemento $\bar N_{kh} > 0$ all'incrocio si chiama **pivot**, "come quando facevate i sistemi lineari: è la stessa cosa". La variabile $x_h$ deve entrare in base al posto di quella della riga $k$: nella nuova forma canonica la sua colonna deve diventare una **colonna dell'identità**, con $1$ nella riga $k$ e $0$ in tutte le altre righe, **compresa la riga 0** (una variabile in base ha costo ridotto nullo). Si può fare perché il pivot è non nullo:

1. si divide la riga $k$ per il pivot, così l'elemento diventa $1$;
2. a ogni altra riga, riga 0 compresa, si sottrae un opportuno multiplo della nuova riga $k$, così da annullare l'elemento nella colonna $h$.

Sono operazioni elementari sulle righe: il sistema che si ottiene è equivalente al precedente ed è in forma canonica rispetto alla nuova base. La nuova riga 0 contiene i nuovi costi ridotti e, a destra, il nuovo valore cambiato di segno; la colonna di destra contiene la nuova $\bar b$. Nessuna inversa è stata calcolata.

```pseudo
procedura PIVOT(T, k, h)              // T: tableau con righe 0..m; k: riga del pivot; h: colonna entrante
    p ← T[k][h]                        // pivot, > 0 per il criterio del rapporto minimo
    T[k] ← T[k] / p                    // ora T[k][h] = 1
    per ogni riga i ≠ k, i = 0, …, m:  // riga 0 compresa
        T[i] ← T[i] − T[i][h] · T[k]   // ora T[i][h] = 0
    variabile in base della riga k ← x_h
```

> [!tip] Approfondimento — Il tableau nei testi #approfondimento
> Le note di Di Summa usano la stessa idea con il problema di massimo e una variabile $z$: la riga in cima contiene gli **opposti** dei costi ridotti, e il criterio di ottimalità diventa "nessun elemento negativo nella prima riga" anche lì, perché i due cambi di segno si compensano [@disumma2015, §3.1 e §3.4]. Le dispense calcolano la nuova $B^{-1}N$ con un'operazione di pivot sulla matrice $(\pi_h \mid \text{colonne fuori base} \mid B^{-1}b)$ [@roma2023, §6.4.4]. È la stessa operazione, scritta senza la riga dei costi.

## Esempio: la fase 2 sul tableau

> [!example] Testo
> $$
> \begin{cases}
> \min\ -x_1 - 2x_2 \\
> -2x_1 + x_2 \le 2 \\
> -x_1 + 2x_2 \le 7 \\
> x_1 \le 3 \\
> x_1, x_2 \ge 0
> \end{cases}
> $$

Per passare alle uguaglianze si aggiungono tre slack. D'ora in poi non le si chiama più $s_1, s_2, s_3$, che crea confusione, ma direttamente $x_3, x_4, x_5$:

$$
\begin{cases}
\min\ -x_1 - 2x_2 \\
-2x_1 + x_2 + x_3 = 2 \\
-x_1 + 2x_2 + x_4 = 7 \\
x_1 + x_5 = 3 \\
x_i \ge 0,\ i = 1, \dots, 5 .
\end{cases}
$$

> [!warning] Discrepanza tra fonti — il secondo vincolo in forma standard
> Negli appunti il secondo vincolo è scritto $-x_1 + 2x_2 - x_4 = 7$. Il vincolo di partenza è un "$\le$", quindi si aggiunge una **slack**: $-x_1 + 2x_2 + x_4 = 7$. Il tableau degli appunti, con $+1$ sotto $x_4$, è coerente con la versione corretta.

Le slack danno subito una base ammissibile: $I_B = \{3, 4, 5\}$, $B = I$, $B^{-1}b = b = (2, 7, 3) \ge 0$. La SBA è $\bar x = (0, 0, 2, 7, 3)$. Anche i costi ridotti sono già pronti: le variabili in base non compaiono nella funzione obiettivo, quindi $\gamma = (-1, -2)$ e $\bar x_0 = 0$. Il tableau iniziale è:

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $-1$ | $-2$ | $0$ | $0$ | $0$ | $0$ |
| $x_3$ | $-2$ | $1$ | $1$ | $0$ | $0$ | $2$ |
| $x_4$ | $-1$ | $2$ | $0$ | $1$ | $0$ | $7$ |
| $x_5$ | $1$ | $0$ | $0$ | $0$ | $1$ | $3$ |

### Iterazione 1

1. **Ottimalità.** Nella riga 0 ci sono elementi negativi, $\gamma_1 = -1$ e $\gamma_2 = -2$: non si può affermare che la SBA sia ottima.
2. **Illimitatezza.** Sotto $\gamma_1$ la colonna è $(-2, -1, 1)$: il terzo elemento è positivo. Sotto $\gamma_2$ la colonna è $(1, 2, 0)$: ci sono elementi positivi. Il test fallisce.
3. **Cambio di base.** Entrambi i costi ridotti sono negativi e si potrebbe scegliere quello che si vuole; seguendo "la regola che piace a me" si prende il più negativo, $\gamma_2 = -2$: **entra $x_2$**. Rapporti sulla colonna di $x_2$: $2/1 = 2$ (riga di $x_3$) e $7/2$ (riga di $x_4$); nella riga di $x_5$ c'è uno $0$ e il rapporto non si calcola. Il minimo è $2$: **esce $x_3$**.

Il pivot è l'$1$ nella riga di $x_3$, che è già uguale a $1$: non serve dividere. Bisogna annullare gli altri elementi della colonna di $x_2$: alla riga 0 si aggiunge due volte la riga del pivot, alla riga di $x_4$ si sottrae due volte la riga del pivot, la riga di $x_5$ ha già uno $0$.

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $-5$ | $0$ | $2$ | $0$ | $0$ | $4$ |
| $x_2$ | $-2$ | $1$ | $1$ | $0$ | $0$ | $2$ |
| $x_4$ | $3$ | $0$ | $-2$ | $1$ | $0$ | $3$ |
| $x_5$ | $1$ | $0$ | $0$ | $0$ | $1$ | $3$ |

La nuova SBA è $\bar x = (0, 2, 0, 3, 3)$, con valore $-4$ (l'angolo in alto a destra cambiato di segno). La colonna di $x_2$ è ora una colonna dell'identità: la matrice identità "c'è sempre", solo con le colonne sparse.

> [!example] Domanda di uno studente — gli zeri nel rapporto minimo
> *Nella riga di $x_5$, con lo $0$, si doveva calcolare $0/3$?* No: si dovrebbe calcolare $3/0$, che non ha senso. Zeri ed elementi negativi della colonna entrante **non** si considerano nel rapporto minimo, solo le entrate strettamente positive: sono quelle che limitano la crescita della variabile entrante, perché possono rendere negativa una variabile in base. Il motivo sta nella dimostrazione della lezione 8.

### Iterazione 2

1. **Ottimalità.** Nella riga 0 c'è $-5$ sotto $x_1$: la SBA non è ottima. "Finché abbiamo un elemento negativo su quella riga sappiamo che non abbiamo vinto."
2. **Illimitatezza.** Solo $\gamma_1$ è negativo (l'altro è positivo, per fortuna); la sua colonna, $(-2, 3, 1)$, ha elementi strettamente positivi. Il test fallisce.
3. **Cambio di base.** **Entra $x_1$**. Rapporti: la riga di $x_2$ ha $-2$ e non conta; riga di $x_4$: $3/3 = 1$; riga di $x_5$: $3/1 = 3$. Il minimo è $1$: **esce $x_4$**. Il pivot è il $3$ nella riga di $x_4$.

Si divide la riga del pivot per $3$, ottenendo $(1, 0, -\tfrac23, \tfrac13, 0 \mid 1)$. Poi: alla riga 0 si aggiungono $5$ volte la nuova riga (per esempio, sotto $x_3$: $2 + 5 \cdot (-\tfrac23) = \tfrac63 - \tfrac{10}{3} = -\tfrac43$; a destra: $4 + 5 = 9$); alla riga di $x_2$ si aggiunge $2$ volte la nuova riga; alla riga di $x_5$ si sottrae la nuova riga.

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $0$ | $0$ | $-\tfrac43$ | $\tfrac53$ | $0$ | $9$ |
| $x_2$ | $0$ | $1$ | $-\tfrac13$ | $\tfrac23$ | $0$ | $4$ |
| $x_1$ | $1$ | $0$ | $-\tfrac23$ | $\tfrac13$ | $0$ | $1$ |
| $x_5$ | $0$ | $0$ | $\tfrac23$ | $-\tfrac13$ | $1$ | $2$ |

La nuova SBA è $\bar x = (1, 4, 0, 0, 2)$, con valore $-9$. Nella riga 0 c'è ancora $-\tfrac43$: non si è all'ottimo e servirebbe un altro passo, che a lezione non è stato fatto ("fate ancora un passo"). La docente ha lamentato la difficoltà dei conti alla lavagna; i tableau qui riportati coincidono con quelli degli appunti e sono verificati.

> [!example] Svolgimento del passo lasciato (calcolo non svolto a lezione)
> **Entra $x_3$** ($\gamma = -\tfrac43$). Nella sua colonna, $(-\tfrac13, -\tfrac23, \tfrac23)$, l'unico elemento positivo è nella riga di $x_5$: rapporto $2 / \tfrac23 = 3$, **esce $x_5$**. Dopo il pivot:
>
> | base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $\bar b$ |
> | --- | --- | --- | --- | --- | --- | --- |
> | (riga 0) | $0$ | $0$ | $0$ | $1$ | $2$ | $13$ |
> | $x_2$ | $0$ | $1$ | $0$ | $\tfrac12$ | $\tfrac12$ | $5$ |
> | $x_1$ | $1$ | $0$ | $0$ | $0$ | $1$ | $3$ |
> | $x_3$ | $0$ | $0$ | $1$ | $-\tfrac12$ | $\tfrac32$ | $3$ |
>
> La riga 0 non ha più elementi negativi, anzi i costi ridotti delle variabili fuori base, $(1, 2)$, sono strettamente positivi: $\bar x = (3, 5, 3, 0, 0)$ è l'**unica** soluzione ottima, con valore $-13$. Nel piano, $x^* = (3, 5)$.

## Interpretazione geometrica

Il problema vive in $\mathbb{R}^2$, quindi si può vedere che cosa ha fatto l'algoritmo. Le tre rette sono:

- $-2x_1 + x_2 = 2$, per $(0, 2)$ e $(-1, 0)$;
- $-x_1 + 2x_2 = 7$, per $(-7, 0)$ e $\left(0, \tfrac72\right)$;
- $x_1 = 3$.

Con $x_1, x_2 \ge 0$ si ottiene un pentagono, non vuoto, con vertici $(0,0)$, $(0,2)$, $(1,4)$, $(3,5)$, $(3,0)$.

**Il percorso.** Si è partiti dalla SBA $(0,0,2,7,3)$: in particolare $x_1 = x_2 = 0$, cioè l'**origine**. L'origine non sta su nessuna delle tre rette, e le slack $2, 7, 3$ dicono di quanto non le soddisfa con l'uguale. Al primo passo è entrata in base $x_2$: ci si è mossi da $(0,0)$ a $(0,2)$. Al secondo è entrata $x_1$: ci si è mossi da $(0,2)$ a $(1,4)$, che sta sulla prima e sulla seconda retta (le slack $x_3$ e $x_4$ sono nulle, fuori base). La funzione obiettivo ha vettore $(-1, -2)$; spostando le rette di livello nel verso di decrescita, come nella soluzione grafica, si vede che a ogni passo la funzione è diminuita, come deve essere nel simplesso. Il passo successivo, non fatto, porta in $(3, 5)$.

| iterazione | SBA | punto del piano | valore |
| --- | --- | --- | --- |
| 0 | $(0, 0, 2, 7, 3)$ | $(0, 0)$ | $0$ |
| 1 | $(0, 2, 0, 3, 3)$ | $(0, 2)$ | $-4$ |
| 2 | $(1, 4, 0, 0, 2)$ | $(1, 4)$ | $-9$ |
| 3 (non svolta) | $(3, 5, 3, 0, 0)$ | $(3, 5)$ | $-13$ |

Per arrivare alla soluzione ottima si sono visitati quattro vertici.

> [!warning] Discrepanza nella trascrizione — il valore dopo il primo passo
> Ricapitolando i valori, la docente dice "siamo partiti da 0, poi siamo passati a, mi pare, $-2$, e adesso siamo a $-9$". Nel vertice $(0, 2)$ il valore è $-x_1 - 2x_2 = -4$, come nel tableau dopo il primo pivot (angolo in alto a destra $4$).

> [!tip] Schema da disegnare
> Figura consigliata in Excalidraw: assi tra $-1$ e $6$; le tre rette e il pentagono $(0,0)$–$(0,2)$–$(1,4)$–$(3,5)$–$(3,0)$ colorato; frecce numerate lungo i lati per il percorso del simplesso $(0,0) \to (0,2) \to (1,4) \to (3,5)$, con accanto i valori $0, -4, -9, -13$; il vettore $-c = (1, 2)$, direzione di decrescita. In un altro colore, il percorso alternativo $(0,0) \to (3,0) \to (3,5)$ della sezione seguente.

### Se all'inizio fosse entrata $x_1$

Dopo la pausa la docente ha mostrato che cosa sarebbe successo con l'altra scelta possibile al primo passo, $\gamma_1 = -1$ invece di $\gamma_2 = -2$. La registrazione di questa parte è quasi del tutto assente.

> [!warning] Sezione ricostruita — inizio
> Della discussione resta solo la conclusione, riportata dopo questo riquadro. Il percorso alternativo è ricostruito con le regole del corso (calcolo verificato).
>
> Dal tableau iniziale **entra $x_1$**: nella sua colonna, $(-2, -1, 1)$, l'unico elemento positivo è nella riga di $x_5$, rapporto $3$, quindi **esce $x_5$** e si arriva in $(3, 0)$, con valore $-3$. Nel nuovo tableau la riga 0 è $(0, -2, 0, 0, 1 \mid 3)$: **entra $x_2$**, rapporti $8/1$ (riga di $x_3$) e $10/2 = 5$ (riga di $x_4$), **esce $x_4$** e si arriva in $(3, 5)$, con valore $-13$. Qui la riga 0 è $(0, 0, 0, 1, 2 \mid 13)$: è l'ottimo, raggiunto con **due** pivot invece di tre, visitando tre vertici invece di quattro.

> [!warning] Sezione ricostruita — fine

La conclusione della docente: "non posso sapere se mi conviene andare qua o andare qua". La scelta di $\gamma_h$ influenza l'algoritmo e può influenzarne l'efficienza, ma non c'è un criterio che permetta di scegliere bene. Quello del costo ridotto più negativo è un criterio molto utilizzato; può andare bene o male. Quello di cui si è sicuri è che c'è un teorema di convergenza.

## Convergenza della fase 2

L'osservazione di partenza è semplice: **se a ogni iterazione si generasse una base ammissibile diversa da tutte le precedenti**, l'algoritmo terminerebbe in un numero finito di passi, perché le basi ammissibili sono in numero finito: prima o poi le si guarderebbe tutte.

Attenzione a un punto sottile: a ogni iterazione la base **cambia** (esce una variabile, ne entra un'altra), ma nulla vieta che dopo qualche passo si torni a una base da cui si era già passati.

> [!important] Teorema — convergenza della fase 2
> Se durante le iterazioni della fase 2 non viene mai generata due volte la stessa base ammissibile, allora esiste un indice $\bar k$ tale che la matrice di base ammissibile $B_{\bar k}$ al passo $\bar k$ corrisponde a una **SBA ottima**, oppure soddisfa il **criterio di illimitatezza**.

*Idea della dimostrazione.* Finché nessuno dei due criteri è soddisfatto, il metodo è in grado di generare una nuova base ammissibile. Le basi sono finite e, per ipotesi, non si ripetono: a un certo punto si arriva a una base da cui non se ne può generare un'altra nuova, e lì uno dei due criteri deve essere soddisfatto. L'algoritmo termina con una SBA ottima, cioè una soluzione del problema, oppure affermando, col criterio di illimitatezza, che il problema è illimitato. $\square$ È il Teorema 6.4.7 delle dispense [@roma2023].

**Quando le basi non si ripetono?** Due osservazioni.

1. **La funzione obiettivo non cresce mai.** Il simplesso non fa passi inutili: passando da una SBA alla successiva il valore è **minore o uguale**. Il "minore o uguale" ricorda che la diminuzione può essere stretta oppure no.
2. **Quando la diminuzione è stretta.** Entrando in base, la variabile $x_h$ è moltiplicata per $\gamma_h < 0$: la variazione del valore è $\gamma_h \cdot t$, dove $t$ è il valore che $x_h$ assume nella nuova SBA. È strettamente negativa se e solo se $t > 0$. Se la SBA corrente è **non degenere**, tutte le variabili in base sono strettamente positive, quindi anche tutti i rapporti $\bar b_i / \bar N_{ih}$ lo sono, e $t > 0$.

> [!important] Corollario — il caso non degenere
> Se tutte le SBA incontrate sono **non degeneri**, la funzione obiettivo decresce strettamente a ogni iterazione, le basi sono tutte diverse e la fase 2 termina in un numero finito di passi.

Due basi uguali corrisponderebbero allo stesso vertice e quindi allo stesso valore della funzione obiettivo, mentre i valori sono strettamente decrescenti [@roma2023, Corollario 6.4.14].

"Siamo soddisfatti? No": le iterazioni degeneri capitano spessissimo, in tutti i casi di interesse, quindi questa non è una risposta soddisfacente. In presenza di SBA degeneri l'algoritmo **può non convergere**. Se non converge in un numero finito di passi, siccome le basi sono finite, deve tornare su una base già visitata: esistono $k_1 < k_2$ con $B_{k_1} = B_{k_2}$. Ma la stessa base corrisponde allo stesso vertice e allo stesso valore della funzione obiettivo; poiché il valore non cresce mai, è rimasto **costante** in tutte le iterazioni tra $k_1$ e $k_2$. L'unico modo in cui il valore resta costante è $t = 0$: sono tutte **iterazioni degeneri**. Le iterazioni degeneri sono "il problema del metodo del simplesso", come annunciato quando le si era introdotte.

> [!important] Definizione — ciclaggio
> Se $B_{k_1} = B_{k_2}$ con $k_1 < k_2$, dopo $B_{k_2}$ l'algoritmo (con una regola di scelta deterministica) ripercorre la stessa strada che da $B_{k_1}$ l'aveva portato a $B_{k_2}$, e così all'infinito. Questo fenomeno si chiama **ciclaggio**.

## Un esempio di ciclaggio: Beale

Il ciclaggio può succedere davvero: c'è un esempio famoso, dovuto a Beale [@beale1955], in cui usando la regola del costo ridotto più negativo si entra in un ciclo. La docente lo ha scritto senza svolgerlo, perché "è fattibile" provarlo a casa.

$$
\begin{cases}
\min\ -\tfrac34 x_4 + 20x_5 - \tfrac12 x_6 + 6x_7 \\
x_1 + \tfrac14 x_4 - 8x_5 - x_6 + 9x_7 = 0 \\
x_2 + \tfrac12 x_4 - 12x_5 - \tfrac12 x_6 + 3x_7 = 0 \\
x_3 + x_6 = 1 \\
x \ge 0
\end{cases}
\qquad n = 7,\ m = 3 .
$$

Si parte dalla base $\{x_1, x_2, x_3\}$, con SBA $(0, 0, 1, 0, 0, 0, 0)$: è **degenere**, perché sono in base $x_1, x_2, x_3$ e ci si aspetterebbero tre componenti non nulle, invece $x_1 = x_2 = 0$. Con la regola del costo ridotto più negativo, e uscita dell'indice più piccolo in caso di pareggio, le basi visitate sono (calcolo verificato)

$$
\{x_1, x_2, x_3\} \to \{x_4, x_2, x_3\} \to \{x_4, x_5, x_3\} \to \{x_6, x_5, x_3\} \to \{x_6, x_7, x_3\} \to \{x_1, x_7, x_3\} \to \{x_1, x_2, x_3\} ,
$$

tutte nello stesso vertice $(0, 0, 1, 0, 0, 0, 0)$, tutte con valore $0$, e tutte con passo $t = 0$: dopo sei pivot si torna alla base di partenza, senza mai raggiungere la base ottima $\{x_1, x_4, x_6\}$ [@roma2023, Esempio 6.4.15].

> [!warning] Discrepanza tra fonti — il coefficiente di $x_4$ e la lunghezza del ciclo
> Negli appunti, e nelle dispense da cui l'esempio è tratto, la funzione obiettivo è scritta $\tfrac34 x_4 + 20x_5 - \tfrac12 x_6 + 6x_7$, con il **più** davanti a $\tfrac34 x_4$. Con quel segno l'esempio non cicla: alla prima iterazione l'unico costo ridotto negativo è quello di $x_6$, entra $x_6$, esce $x_3$ e il criterio di ottimalità è subito soddisfatto (verificato). Nell'esempio di Beale il coefficiente è $-\tfrac34$, ed è con questo segno che si ottiene il ciclo descritto e la base ottima $\{x_1, x_4, x_6\}$ indicata dalle dispense. Inoltre a lezione il ciclo è stato descritto come "di ordine 7, dopo 7 iterazioni ritornate a questa base": le basi elencate sono sette contando due volte quella iniziale, ma i pivot sono **sei**.

**In pratica.** La regola del costo ridotto più negativo è tra le più usate, e i fenomeni di ciclaggio non si osservano spesso, anche su problemi molto grandi. Le iterazioni degeneri ci saranno sicuramente, ma raramente si entra in un ciclo. Per risolvere il problema si usano le **regole anti-ciclaggio**, che spesso si applicano solo quando ci si accorge di essere entrati in un ciclo; chi vuole essere sicuro le applica fin dall'inizio. Nelle applicazioni pratiche ci sono poi molte altre euristiche, che nel corso non si vedono.

## La regola di Bland

La regola anti-ciclaggio più famosa (ce ne sono altre) è quella di **Bland**, molto semplice.

> [!important] Regola anti-ciclaggio di Bland
> - **Variabile entrante**: tra le variabili fuori base con costo ridotto negativo entra quella di **indice più piccolo** (non quella col costo ridotto più negativo).
> - **Variabile uscente**: se il rapporto minimo è raggiunto su più variabili, esce quella di **indice più piccolo**.
>
> Con questa regola il metodo del simplesso non cicla e la fase 2 termina in un numero finito di passi [@bland1977; @roma2023, Teorema 6.4.8; @disumma2015, Teorema 3.4].

Nell'esempio di questa lezione $\gamma_1$ e $\gamma_2$ erano entrambi negativi: con Bland si sarebbe dovuto scegliere $\gamma_1$, cioè far entrare $x_1$, il percorso più breve della sezione ricostruita.

> [!warning] Precisazione — le due metà della regola
> A lezione e negli appunti la regola è enunciata solo per la variabile **entrante**. Per garantire la terminazione serve anche la scelta dell'indice più piccolo tra le variabili **uscenti** a pari rapporto, che nel corso è già la convenzione adottata dalla lezione 8. Gli indici sono quelli delle **variabili**: nel tableau con le colonne nell'ordine naturale, la variabile entrante di Bland è il primo elemento negativo della riga 0 da sinistra.

> [!example] Verifica — Bland sull'esempio di Beale (calcolo aggiunto)
> Applicando la regola di Bland all'esempio di Beale (con $-\tfrac34$) entrano nell'ordine $x_4, x_5, x_6, x_1, x_2, x_4$. I primi quattro pivot sono ancora degeneri, ma al quinto il passo è positivo e si lascia il vertice degenere. Dopo sei pivot si arriva alla base $\{x_6, x_1, x_4\}$, con SBA $x^* = \left(\tfrac34, 0, 0, 1, 0, 1, 0\right)$ e valore $-\tfrac54$, dove i costi ridotti sono tutti non negativi: è l'ottimo indicato dalle dispense.

## Complessità: un numero finito di passi, ma quanti?

Quella appena vista è una convergenza interessante, perché garantisce un numero **finito** di passi. Ma il numero di vertici può crescere esponenzialmente con la dimensione: il cubo $[0,1]^n$, un poliedro molto semplice, ha $2^n$ vertici ([[Lezione 05 - Teorema fondamentale e forma standard|lezione 5]]), e nulla vieta che in casi particolarmente sfortunati il simplesso debba visitarli tutti. Un numero finito di passi può essere enorme. Per questo nella pratica il metodo non si implementa in modo così ingenuo: si usano euristiche, si decide da dove partire, si fanno prove, "uno magari sa in che zona andare a cercare".

Esistono altri algoritmi per la programmazione lineare, con garanzie migliori: **polinomiali** nella dimensione e nel numero di iterazioni. Il più noto è l'algoritmo di **Karmarkar** [@karmarkar1984], sviluppato in un'azienda privata, un algoritmo **a punti interni**: si avvicina alla soluzione in modo radicalmente diverso, con una successione di punti che sta sempre **dentro** il poliedro, senza muoversi sui vertici. Dal punto di vista teorico funziona meglio, ma in pratica il simplesso funziona molto bene ed è spesso preferito, specialmente in grandi dimensioni.

> [!tip] Approfondimento — Simplesso, ellissoide e punti interni #approfondimento
> Le note di Di Summa riassumono lo stato delle conoscenze [@disumma2015, §5.2]. Per tutte le regole di pivot proposte finora si conoscono esempi che richiedono un numero di iterazioni esponenziale nel numero di variabili; il primo è quello di Klee e Minty [@klee1972], costruito per la regola del costo ridotto più negativo; costruzioni dello stesso tipo esistono anche per la regola di Bland. Non è noto se esista una regola di pivot che renda il simplesso polinomiale: è uno dei problemi aperti più importanti dell'ottimizzazione. Il primo algoritmo polinomiale per la programmazione lineare è il **metodo dell'ellissoide** di Khachiyan (1979), importante in teoria ma non efficiente in pratica. Algoritmi efficienti sia in teoria sia in pratica sono arrivati con i **metodi di punto interno**, di cui quello di Karmarkar (1984), sviluppato ai Bell Laboratories di AT&T, è il capostipite. I solutori commerciali usano sia il simplesso (primale o duale) sia i metodi di punto interno, a seconda del problema.

## La fase 1: il metodo delle variabili artificiali

Finora si è lavorato con delle ipotesi che ora si vogliono rimuovere. Dato il problema in forma standard $\min c^T x$, $Ax = b$, $x \ge 0$, la **fase 1** deve:

1. stabilire se $P = \{ x \in \mathbb{R}^n \mid Ax = b,\ x \ge 0 \} \neq \varnothing$;
2. ottenere una matrice di rango $m$, uguale al numero delle righe;
3. fornire una SBA da cui partire.

Termina o stabilendo che il poliedro è vuoto, oppure con una matrice di rango $m$ e una SBA. Il metodo che si vede è quello delle **variabili artificiali**.

**Un'ipotesi innocente.** Si assume $b \ge 0$. Non è una vera ipotesi, solo una riscrittura del problema: se qualche $b_i < 0$, basta moltiplicare per $-1$ la riga corrispondente.

**Il problema ausiliario.** Per ogni riga si aggiunge una variabile artificiale $\alpha_i \ge 0$, e si considera il nuovo problema

$$
\text{(PA)}\qquad
\begin{cases}
\min\ \alpha_1 + \alpha_2 + \dots + \alpha_m \\
Ax + I_m \alpha = b \\
x \ge 0,\ \alpha \ge 0 .
\end{cases}
$$

È un nuovo problema di programmazione lineare, in forma standard, e ha tre proprietà che il problema originale non ha garantite:

- **il poliedro è non vuoto**: con $x = 0$ deve essere $\alpha = b$, e $b \ge 0$, quindi il punto $(0, \dots, 0 \mid b)$ (prima le $x$, poi le $\alpha$) è ammissibile;
- **la matrice dei coefficienti** $\begin{pmatrix} A & I_m \end{pmatrix}$, di taglia $m \times (n+m)$, **ha rango $m$** "alla grande", perché contiene la matrice identità;
- **c'è una SBA**: si prende come base l'identità, cioè si mettono in base le $\alpha$ e fuori base le $x$; poiché $b \ge 0$ la soluzione di base $(0 \mid b)$ è ammissibile.

Al problema ausiliario si può quindi applicare la fase 2. Perché farlo? Perché la sua soluzione dà informazioni sul problema originale. Quali, la docente lo lascia come domanda per la lezione successiva: "provate a pensarci su".

> [!warning] Discrepanza tra fonti — il vettore dei costi del problema ausiliario
> Negli appunti la funzione obiettivo è scritta "$\sum \alpha_i = c^T x$, $c = (1, \dots, 1)^T$". All'inizio della lezione 10 la docente corregge l'imprecisione: le variabili del problema ausiliario sono sia le $x$ sia le $\alpha$, quindi il vettore dei costi ha $0$ in corrispondenza delle $x$ e $1$ in corrispondenza delle $\alpha$, e sta in $\mathbb{R}^{n+m}$.

## Riepilogo

- **Forma tableau**: con $x_0 = c^T x$ la funzione obiettivo diventa un'equazione. Rispetto a una base, riga 0 $= (0 \mid \gamma^T \mid -\bar x_0)$, righe dei vincoli $= (I \mid B^{-1}N \mid B^{-1}b)$. Ogni riga è associata a una variabile in base; le colonne restano nell'ordine naturale.
- Dal tableau si leggono il test di ottimalità (riga 0 senza negativi), il test di illimitatezza (colonna sotto un $\gamma_h < 0$ senza positivi), la variabile entrante e il rapporto minimo (solo sulle entrate positive).
- **Pivot**: si divide la riga del pivot per il pivot e si annulla il resto della colonna, riga 0 compresa. Si passa così da una forma canonica alla successiva senza invertire matrici.
- Esempio: $\min -x_1 - 2x_2$ sul pentagono; percorso $(0,0) \to (0,2) \to (1,4) \to (3,5)$, valori $0, -4, -9, -13$. Scegliendo l'altra variabile entrante si arriva in due passi: la scelta influenza l'efficienza, ma non c'è un criterio per scegliere bene.
- **Convergenza**: se nessuna base si ripete, la fase 2 termina con una SBA ottima o con il criterio di illimitatezza. La funzione obiettivo non cresce mai; decresce strettamente nelle iterazioni non degeneri. Se tutte le SBA sono non degeneri, si termina.
- Con SBA degeneri si può **ciclare** (esempio di Beale, con $-\tfrac34 x_4$: sei pivot degeneri riportano alla base iniziale). In pratica è raro.
- **Regola di Bland**: entra la variabile di indice più piccolo con $\gamma_h < 0$, esce quella di indice più piccolo a pari rapporto: il simplesso non cicla.
- La terminazione è finita ma il numero di passi può essere esponenziale; esistono algoritmi polinomiali a punti interni (Karmarkar).
- **Fase 1**: con $b \ge 0$ si aggiungono variabili artificiali e si risolve $\min \sum \alpha_i$, $Ax + I\alpha = b$, $x, \alpha \ge 0$: poliedro non vuoto, rango $m$, SBA $(0 \mid b)$ già pronta.
