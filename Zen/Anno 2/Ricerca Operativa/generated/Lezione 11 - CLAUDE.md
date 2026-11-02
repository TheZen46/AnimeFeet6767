---
corso: Ricerca Operativa
lezione: 11
data: 2026-10-30
docente: Silvia Villa
argomenti: [fase 1 del simplesso, variabili artificiali in base, vincoli ridondanti, scambio degenere, prima SBA per la fase 2, variabili artificiali solo dove servono, dualità, problema primale, problema duale, stima dal basso del valore ottimo, variabili duali, duale di un problema in forma generale]
fonti: [trascrizione, dispense]
tags: [ricerca-operativa, lezione]
---

# Lezione 11 — Uscita dalla fase 1 e introduzione alla dualità

> [!info] Fonti di questa nota
> Trascrizione della lezione (un'unica parte; le conversazioni di sottofondo sono escluse). Per questa lezione **non** sono disponibili appunti manuali. I tre esercizi sono gli Esempi 6.5.2, 6.5.6 e 6.5.5 delle dispense [@roma2023, §6.5.3]: i frammenti numerici della trascrizione coincidono con quelli degli esempi, e i dati non udibili nella registrazione sono presi da lì, come indicato caso per caso. La parte sulla dualità segue lo stesso percorso delle dispense [@roma2023, §7.1]; le note di Di Summa [@disumma2015, §4.1–4.2] costruiscono il duale in un altro modo. I calcoli aggiunti per verifica sono indicati esplicitamente.

> [!warning] Data della lezione — ricostruita
> La trascrizione riporta come data di registrazione il **31/10/2026**, un sabato. Nelle lezioni 9 e 10 la data di registrazione segue la lezione di uno o due giorni, e le lezioni della docente si tengono il martedì e il venerdì: la data più plausibile è **venerdì 30/10/2026**, indicata nel front-matter. Non ci sono appunti datati che permettano di verificarla.

La prima parte della lezione completa la **fase 1** con due esercizi in cui, alla fine del problema ausiliario, restano variabili artificiali in base: si vedono in azione l'**eliminazione dei vincoli ridondanti** e lo **scambio degenere**. Un terzo esercizio mostra che le variabili artificiali vanno aggiunte solo dove servono. La seconda parte introduce la **dualità**: a ogni problema di programmazione lineare, detto **primale**, si associa un problema **duale** che fornisce una stima dal basso del valore ottimo.

## Esercizio 1: un vincolo ridondante

È l'esercizio lasciato a metà nella [[Lezione 10 - Fase 1 e problema ausiliario|lezione 10]]:

$$
\begin{cases}
\min\ 2x_1 + 3x_2 + x_3 \\
x_1 + x_2 + x_3 = 2 \\
-x_1 + 2x_2 = 1 \\
3x_2 + x_3 = 3 \\
x \ge 0 .
\end{cases}
$$

Serve una SBA da cui partire: si passa al problema ausiliario, con tre variabili artificiali, una per equazione, e funzione obiettivo $\alpha_1 + \alpha_2 + \alpha_3$. La docente precisa che qui si può fare direttamente perché i termini noti $2, 1, 3$ sono positivi; se ce ne fosse uno negativo bisognerebbe prima cambiare segno alla riga, altrimenti la $\alpha$ corrispondente avrebbe il segno sbagliato.

**Tableau iniziale.** La matrice identità sotto le $\alpha$ dice che $\alpha_1, \alpha_2, \alpha_3$ sono in base, ma nella riga dei costi hanno coefficiente $1$: non è ancora la forma canonica. Come sempre nel problema ausiliario, basta sostituire la riga 0 con $R_0 - R_1 - R_2 - R_3$:

| base | $x_1$ | $x_2$ | $x_3$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $0$ | $-6$ | $-2$ | $0$ | $0$ | $0$ | $-6$ |
| $\alpha_1$ | $1$ | $1$ | $1$ | $1$ | $0$ | $0$ | $2$ |
| $\alpha_2$ | $-1$ | $2$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $\alpha_3$ | $0$ | $3$ | $1$ | $0$ | $0$ | $1$ | $3$ |

**Iterazione 1.** I costi ridotti $(0, -6, -2)$ hanno entrate negative: la soluzione corrente non è ottima. Le colonne corrispondenti non sono fatte solo di elementi non positivi, quindi il test di illimitatezza fallisce. La docente osserva però che, "messa in modalità algoritmo", ha fatto un controllo inutile: il problema ausiliario è limitato dal basso da $0$, quindi il test di illimitatezza deve **sempre** fallire, "se no c'è qualcosa che non va". Entra la variabile col costo più negativo, **$x_2$**. Rapporti: $2/1 = 2$, $1/2 = \tfrac12$, $3/3 = 1$, tutti e tre perché gli elementi sono tutti strettamente positivi; il minimo è $\tfrac12$: **esce $\alpha_2$**, e il pivot è il $2$.

Si divide la riga del pivot per $2$, ottenendo $\left(-\tfrac12, 1, 0, 0, \tfrac12, 0 \mid \tfrac12\right)$; poi $R_0 \leftarrow R_0 + 6R_2$, $R_1 \leftarrow R_1 - R_2$, $R_3 \leftarrow R_3 - 3R_2$:

| base | $x_1$ | $x_2$ | $x_3$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $-3$ | $0$ | $-2$ | $0$ | $3$ | $0$ | $-3$ |
| $\alpha_1$ | $\tfrac32$ | $0$ | $1$ | $1$ | $-\tfrac12$ | $0$ | $\tfrac32$ |
| $x_2$ | $-\tfrac12$ | $1$ | $0$ | $0$ | $\tfrac12$ | $0$ | $\tfrac12$ |
| $\alpha_3$ | $\tfrac32$ | $0$ | $1$ | $0$ | $-\tfrac32$ | $1$ | $\tfrac32$ |

**Iterazione 2.** In base ci sono $\alpha_1, x_2, \alpha_3$. Ci sono ancora costi ridotti negativi; il più negativo è $-3$: **entra $x_1$**. Rapporti: $\tfrac32 / \tfrac32 = 1$ (riga di $\alpha_1$) e $\tfrac32 / \tfrac32 = 1$ (riga di $\alpha_3$). C'è un pareggio: per convenzione esce la variabile di indice minore, "quella più in alto, la prima che incontro": **esce $\alpha_1$**. Il pivot è $\tfrac32$. Dopo l'operazione di pivot:

| base | $x_1$ | $x_2$ | $x_3$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $0$ | $0$ | $0$ | $2$ | $2$ | $0$ | $0$ |
| $x_1$ | $1$ | $0$ | $\tfrac23$ | $\tfrac23$ | $-\tfrac13$ | $0$ | $1$ |
| $x_2$ | $0$ | $1$ | $\tfrac13$ | $\tfrac13$ | $\tfrac13$ | $0$ | $1$ |
| $\alpha_3$ | $0$ | $0$ | $0$ | $-1$ | $-1$ | $1$ | $0$ |

I costi ridotti sono tutti non negativi: si è all'ottimo del problema ausiliario. L'angolo in alto a destra è $0$: nella SBA corrente $\alpha_1 + \alpha_2 + \alpha_3 = 0$, quindi **il problema originale è ammissibile**. La docente aveva scritto un valore diverso da $0$ e sono stati gli studenti a correggerla: "ci sarebbe stata una bella differenza", perché con un valore positivo il problema sarebbe risultato inammissibile. I tableau qui riportati sono verificati.

**Uscita dalla fase 1.** In base ci sono $x_1$ e $x_2$, ma anche $\alpha_3$: non è il caso fortunato, è il caso 2 della lezione 10.

1. **Si cancellano le colonne delle $\alpha$ fuori base**, $\alpha_1$ e $\alpha_2$. Questo si fa in tutti i casi, ed è il primo passo.
2. **Si esamina la riga della $\alpha$ in base**, $\alpha_3$. Il suo termine noto è $0$, come deve essere: il problema è ammissibile e la somma delle $\alpha$ è nulla. Accanto all'$1$ di $\alpha_3$, i coefficienti delle variabili originali sono **tutti nulli**: l'equazione è diventata $0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = 0$. Il vincolo corrispondente è **ridondante** e si elimina, insieme ad $\alpha_3$.

Il motivo si vede anche sul sistema di partenza: la terza equazione è la **somma delle prime due** ($x_1 - x_1$ si cancella, $x_2 + 2x_2 = 3x_2$, resta $x_3$, e $2 + 1 = 3$). Non dà nessuna informazione in più. Il rango della matrice $A$ non era $3$, e la fase 1 serve proprio a eliminare i vincoli ridondanti e ottenere una matrice di rango $m$, qui $2$ (la docente ha detto "rango $n$", per un lapsus).

Il tableau che resta è quello del problema originale, con due equazioni e due variabili in base, $x_1$ e $x_2$:

| base | $x_1$ | $x_2$ | $x_3$ | $\bar b$ |
| --- | --- | --- | --- | --- |
| $x_1$ | $1$ | $0$ | $\tfrac23$ | $1$ |
| $x_2$ | $0$ | $1$ | $\tfrac13$ | $1$ |

La SBA di partenza è $\bar x = (1, 1, 0)$. Resta da scrivere la riga dei costi, $(2, 3, 1 \mid 0)$, che così non è in forma canonica: bisogna annullare i coefficienti delle variabili in base, "per esempio togliendo due volte la prima riga e tre volte la seconda", e poi si parte con la fase 2.

> [!example] Completamento della fase 2 (calcolo non svolto a lezione)
> $(2, 3, 1 \mid 0) - 2\left(1, 0, \tfrac23 \mid 1\right) - 3\left(0, 1, \tfrac13 \mid 1\right) = \left(0, 0, -\tfrac43 \;\middle|\; -5\right)$: valore $5$ nella SBA di partenza e costo ridotto $-\tfrac43$ per $x_3$. **Entra $x_3$**; rapporti $1 / \tfrac23 = \tfrac32$ (riga di $x_1$) e $1 / \tfrac13 = 3$ (riga di $x_2$): **esce $x_1$**. Dopo il pivot la riga 0 è $(2, 0, 0 \mid -3)$, e l'unico costo ridotto, quello di $x_1$, vale $2 > 0$. La soluzione ottima, unica, è $x^* = \left(0, \tfrac12, \tfrac32\right)$, con valore $3$. Controllo sui tre vincoli originali: $0 + \tfrac12 + \tfrac32 = 2$, $0 + 1 = 1$, $\tfrac32 + \tfrac32 = 3$.

## Esercizio 2: uno scambio degenere

Per non risolvere un altro problema da capo, la docente scrive direttamente il tableau **alla fine della fase 1** di un esercizio: tre variabili artificiali, ottimo del problema ausiliario con $\alpha_1 = \alpha_2 = \alpha_3 = 0$, quindi problema originale ammissibile.

> [!warning] Sezione ricostruita — inizio
> Il tableau non è leggibile nella trascrizione e per questa lezione non ci sono appunti. I frammenti registrati (tre variabili artificiali, di cui due in base alla fine; $x_1$ in base con valore $10$; nella riga di $\alpha_1$ un solo coefficiente non nullo sulle $x$, pari a $-1$; un $4$ da annullare nella riga di $x_1$; SBA finale degenere con $x_3$ e $x_1$ in base) coincidono con l'Esempio 6.5.6 delle dispense, di cui si riportano i dati [@roma2023, Esempio 6.5.6]. Il vettore dei costi è omesso, come a lezione: "per quello che dobbiamo fare non ci serve".

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\alpha_1$ | $0$ | $0$ | $-1$ | $0$ | $1$ | $0$ | $-2$ | $0$ |
| $x_1$ | $1$ | $2$ | $4$ | $2$ | $0$ | $0$ | $6$ | $10$ |
| $\alpha_2$ | $0$ | $0$ | $0$ | $0$ | $0$ | $1$ | $-4$ | $0$ |

> [!warning] Sezione ricostruita — fine

Le variabili artificiali in base sono due, ed entrambe valgono $0$: "se abbiamo un problema ammissibile necessariamente abbiamo degli zeri". È una base **degenere**. Si costruisce la SBA del problema originale come prima.

1. **Si cancellano le colonne delle $\alpha$ fuori base**: qui solo $\alpha_3$.
2. **$\alpha_2$**: nella sua riga, a parte l'$1$, ci sono solo zeri sulle $x$. Rappresenta un **vincolo ridondante**: la riga e $\alpha_2$ scompaiono.
3. **$\alpha_1$**: nella sua riga c'è l'$1$, ma c'è anche un $-1$ sotto $x_3$. Il primo vincolo **non** è ridondante e non si può cancellare. Si deve sostituire $\alpha_1$ con una variabile $x$: si sceglie un elemento non nullo nella parte delle $x$ (qui ce n'è uno solo, il $-1$) e si fa uno **scambio degenere**: **esce $\alpha_1$, entra $x_3$**.

Lo scambio è un pivot come gli altri: il $-1$ deve diventare $1$ e sotto vanno messi degli zeri. Il pivot è negativo, ma il termine noto della riga è $0$: anche moltiplicando per $-1$ resta $0$, e la base trovata è ammissibile. Si moltiplica la prima riga per $-1$, ottenendo $(0, 0, 1, 0 \mid -1 \mid 0)$ (nelle colonne $x_1, \dots, x_4$, $\alpha_1$ e termine noto); poi, per annullare il $4$ della riga di $x_1$, si sottraggono a questa quattro volte la nuova prima riga, ottenendo $(1, 2, 0, 2 \mid 4 \mid 10)$. Ora $\alpha_1$ è fuori base e la sua colonna si elimina. Il tableau del problema di partenza è

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- |
| $x_3$ | $0$ | $0$ | $1$ | $0$ | $0$ |
| $x_1$ | $1$ | $2$ | $0$ | $2$ | $10$ |

e si può partire con la SBA $(10, 0, 0, 0)$, con $x_3$ e $x_1$ in base e $x_2$, $x_4$ fuori base. È una SBA **degenere**: $x_3$ è in base ma vale $0$.

## Esercizio 3: variabili artificiali solo dove servono

Un piccolo "sconto" che a volte ci si può permettere passando al problema ausiliario: se alcune variabili sono già "nel modo giusto" per stare in base, non serve aggiungere variabili artificiali per tutte le righe.

> [!example] Testo
> $$
> \begin{cases}
> \min\ -x_1 \\
> x_1 + x_2 \ge 6 \\
> 2x_1 + 3x_2 \le 4 \\
> x_1, x_2 \ge 0
> \end{cases}
> $$

> [!warning] Dati presi dalle dispense
> Nella trascrizione si sentono la funzione obiettivo (un minimo nella sola $x_1$), il primo vincolo $x_1 + x_2 \ge 6$, le quattro variabili e due vincoli della forma standard e il risultato finale ($x_1 = 2$, $\alpha_1 = 4$). Il secondo vincolo non è udibile. Tutti i frammenti coincidono con l'Esempio 6.5.5 delle dispense, da cui è preso il secondo vincolo [@roma2023, Esempio 6.5.5].

**Forma standard.** Nel primo vincolo $x_1 + x_2$ è più grande di $6$: per avere l'uguaglianza bisogna togliere qualcosa, quindi si sottrae una surplus $x_3$. Nel secondo si aggiunge una slack $x_4$:

$$
\begin{cases}
\min\ -x_1 \\
x_1 + x_2 - x_3 = 6 \\
2x_1 + 3x_2 + x_4 = 4 \\
x_1, \dots, x_4 \ge 0 .
\end{cases}
$$

Quattro variabili, due vincoli.

**Un'artificiale sola.** Per partire con la fase 1 bisognerebbe aggiungere due variabili artificiali, per avere la matrice identità nel tableau iniziale. Ma la colonna della slack $x_4$, $(0, 1)^T$, è già una colonna dell'identità: è inutile aggiungere un'artificiale per il secondo vincolo, basta $\alpha_1$ per il primo. "Non cambia niente, le aggiungete tutte e due, ma fate più fatica." Il problema ausiliario è

$$
\begin{cases}
\min\ \alpha_1 \\
x_1 + x_2 - x_3 + \alpha_1 = 6 \\
2x_1 + 3x_2 + x_4 = 4 \\
x \ge 0,\ \alpha_1 \ge 0 ,
\end{cases}
$$

e la base di partenza è $\{\alpha_1, x_4\}$. La funzione obiettivo è la somma delle sole variabili artificiali introdotte, e il teorema della lezione 10 vale "pari pari", con la stessa dimostrazione: il problema ausiliario ha valore ottimo $0$ se e solo se il problema originale è ammissibile.

**Fase 1.** Per i costi ridotti si sottrae alla riga 0 la sola riga di $\alpha_1$:

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $\alpha_1$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $-1$ | $-1$ | $1$ | $0$ | $0$ | $-6$ |
| $\alpha_1$ | $1$ | $1$ | $-1$ | $0$ | $1$ | $6$ |
| $x_4$ | $2$ | $3$ | $0$ | $1$ | $0$ | $4$ |

Ci sono costi ridotti negativi, quindi la soluzione non è ottima. $x_1$ e $x_2$ hanno lo stesso costo ridotto, $-1$: si sceglie $x_1$, di indice minore. Rapporti: $6/1 = 6$ e $4/2 = 2$: **entra $x_1$, esce $x_4$**. Dopo il pivot (calcolo verificato):

| base | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $\alpha_1$ | $\bar b$ |
| --- | --- | --- | --- | --- | --- | --- |
| (riga 0) | $0$ | $\tfrac12$ | $1$ | $\tfrac12$ | $0$ | $-4$ |
| $\alpha_1$ | $0$ | $-\tfrac12$ | $-1$ | $-\tfrac12$ | $1$ | $4$ |
| $x_1$ | $1$ | $\tfrac32$ | $0$ | $\tfrac12$ | $0$ | $2$ |

I costi ridotti sono tutti non negativi: la soluzione è ottima. È $x_1 = 2$, $x_2 = x_3 = x_4 = 0$, $\alpha_1 = 4$: il valore ottimo del problema ausiliario è $4 \neq 0$, quindi **il problema originale è inammissibile**. Tutto funziona come prima, con meno fatica.

> [!example] Verifica diretta
> La docente aveva anticipato che dai dati "potremmo già sapere tutto". Infatti, per $x \ge 0$, il secondo vincolo dà $2(x_1 + x_2) \le 2x_1 + 3x_2 \le 4$, cioè $x_1 + x_2 \le 2$, incompatibile con $x_1 + x_2 \ge 6$ (passaggio aggiunto).

## La duality

Dato un problema di programmazione lineare, che d'ora in poi si chiama **problema primale** perché è il primo, quello che si vuole risolvere, è possibile associargli un altro problema di programmazione lineare, il **problema duale**. È un'idea profonda in ottimizzazione, che non vale solo per i problemi lineari ma anche, per esempio, per quelli convessi. Si affianca al problema di partenza un problema "gemello" che dà informazioni in più e che, nei casi buoni, ha la stessa soluzione. Serve dal punto di vista teorico, perché dà informazioni sul primale, e dal punto di vista algoritmico, perché a volte il duale è più facile da risolvere.

Nel corso la trattazione sarà limitata: si costruisce il duale, sperabilmente più facile, lo si risolve e si torna al primale. In pratica, però, la dualità "è un po' come spalancare una porta": esistono metodi **primali-duali** in cui si dà "un colpo alla botte e uno al cerchio", facendo un passo su un problema e uno sull'altro, e risolvere i due problemi insieme è, in alcuni casi, più facile che risolvere quello di partenza. Le interpretazioni economiche e gli esempi sono rimandati; oggi si fa "la parte più noiosa", la costruzione del problema duale.

### L'idea: una stima dal basso del valore ottimo (by zen)

Per questa costruzione il problema primale si scrive **in forma generale**:

$$
\text{(P)}\qquad \min\ c^T x \quad \text{s.t.} \quad Ax \ge b, \qquad A \in \mathbb{R}^{m \times n},\ b \in \mathbb{R}^m,\ c, x \in \mathbb{R}^n .
$$

Si supponga di avere un punto ammissibile $\bar x$, e che il problema abbia soluzione ottima $x^*$, con valore ottimo $M = c^T x^*$. Quanto è distante il valore nel punto corrente dall'ottimo, cioè quanto vale $c^T \bar x - M$? Spesso non serve calcolare la soluzione esatta: basta una soluzione vicina all'ottimo, e "anche se sbaglio di qualche centesimo non mi interessa". Il problema è che, se non si è risolto il problema, $M$ non si conosce; e se lo si è risolto, le soluzioni subottimali non interessano più. Si vuole quindi **stimare** quanto si è lontani dall'ottimo, in termini di valore della funzione costo, **senza calcolarlo**.

Il trucco è questo. Sia $u \in \mathbb{R}^m$ con $u \ge 0$: deve avere la stessa dimensione di $b$, una componente per vincolo. Allora

$$
c^T x^* + u^T (b - Ax^*) \;\le\; c^T x^* .
$$

Infatti $u^T(b - Ax^*) = \sum_{i=1}^m u_i\, (b - Ax^*)_i$: ogni $u_i \ge 0$ per scelta, e ogni $(b - Ax^*)_i \le 0$ perché $x^*$ è ammissibile ($Ax^* \ge b$). Ogni prodotto è "più per meno", quindi la somma è $\le 0$. Riordinando il membro di sinistra,

$$
c^T x^* + u^T b - u^T A x^* = \left(c^T - u^T A\right) x^* + u^T b \;\le\; c^T x^* .
$$

Il pezzo $(c^T - u^T A)\, x^*$ contiene ancora l'incognita $x^*$. Ma con una scelta furba di $u$ lo si può **annullare**: se $u$ soddisfa $c^T - u^T A = 0$, cioè, trasponendo, $A^T u = c$, resta

$$
u \ge 0,\ A^T u = c \quad\Longrightarrow\quad b^T u \;\le\; c^T x^* = M .
$$

Si è trovato un **minorante del valore ottimo** che si sa calcolare. E quindi anche la distanza del punto corrente dall'ottimo si può stimare:

$$
0 \;\le\; c^T \bar x - M \;\le\; c^T \bar x - b^T u .
$$

Non si calcola $c^T \bar x - M$, ma se $c^T \bar x - b^T u$ è più piccolo di $10$, anche la distanza dal costo ottimo sarà più piccola di $10$.

**La stima migliore.** La disuguaglianza vale, ma magari tra $b^T u$ e $c^T x^*$ c'è tanta differenza. Si può scegliere $u$ ancora più furbo: quello che **massimizza** il limite dal basso, cioè che dà la stima più precisa del minimo del problema originale, tra tutti gli $u$ che rispettano le condizioni richieste.

> [!important] Definizione — problema duale
> Il **problema duale** del problema primale $\min c^T x$, $Ax \ge b$ è
> $$
> \text{(D)}\qquad
> \begin{cases}
> \max\ b^T u \\
> A^T u = c \\
> u \ge 0 .
> \end{cases}
> $$
> Le variabili $u \in \mathbb{R}^m$ si chiamano **variabili duali**: ce n'è una per ogni vincolo del primale.

Ogni volta che si trova una $u$ ammissibile per il duale si ha una stima della distanza dall'ottimo, cioè un **certificato di ottimalità** basato sulle variabili duali. Il duale è ancora un problema di programmazione lineare, e per di più in forma standard, con $m$ variabili; la docente osserva che, quando i vincoli del primale sono meno delle variabili, può essere vantaggioso risolvere il duale. Si noti che il duale ha $m$ variabili e $n$ vincoli di uguaglianza: le dimensioni del primale si scambiano.

Dimenticando come ci si è arrivati, si leggono le corrispondenze:

| primale (P) | duale (D) |
| --- | --- |
| $\min$ | $\max$ |
| vettore dei costi $c$ | vettore dei termini noti $c$ (in $A^T u = c$) |
| vettore dei termini noti $b$ | vettore dei costi $b$ |
| matrice $A$, $m$ vincoli | matrice $A^T$, $m$ variabili duali $u \ge 0$ |

> [!tip] Approfondimento — La disuguaglianza vale per ogni punto ammissibile #approfondimento
> Nel ragionamento si è usato $x^*$ solo per il fatto che è ammissibile ($Ax^* \ge b$). Ripetendo gli stessi passaggi con un qualunque $x$ ammissibile per (P) e un qualunque $u$ ammissibile per (D) si ottiene $b^T u \le c^T x$: è il **teorema di dualità debole** [@roma2023, Teorema 7.1.1]. In particolare, se (P) è illimitato inferiormente, il duale non può avere punti ammissibili, e viceversa. Le note di Di Summa enunciano lo stesso risultato per la coppia in forma standard $\max c^T x$, $Ax = b$, $x \ge 0$ e il suo duale [@disumma2015, Teorema 4.1 e Corollario 4.3].

### Il duale di un problema in forma generale

Ora il percorso inverso a quello fatto finora. Fino a qui non importava come fosse scritto un poliedro, perché lo si poteva sempre riscrivere come serviva. Ora invece si vuole un problema con un po' di uguaglianze, un po' di disuguaglianze, variabili vincolate in segno e no, e capire qual è il duale tenendo conto di tutte queste specificità, per non dover ripetere il percorso ogni volta. Il primale si scrive

$$
\text{(P)}\qquad
\begin{cases}
\min\ c^T x + d^T y \\
Cx + Dy = h \\
Ex + Fy \ge g \\
x \ge 0 ,
\end{cases}
$$

con matrici e vettori di dimensioni opportune. Le variabili **vincolate in segno** si chiamano $x$, quelle **libere** $y$, perché avranno ruoli diversi nella costruzione; si separano i vincoli di **uguaglianza** da quelli di **disuguaglianza**, scritti con "$\ge$" perché il problema è di minimo.

**Ricondursi al caso noto.** L'unico duale che si sa scrivere, per ora, è quello di $\min c^T x$, $Ax \ge b$. Si riscrive quindi (P) in quella forma, per un'opportuna matrice e un opportuno vettore. L'uguaglianza diventa due disuguaglianze, e il vincolo $x \ge 0$ si scrive come $I x + 0\, y \ge 0$:

$$
\begin{pmatrix} C & D \\ -C & -D \\ E & F \\ I & 0 \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
\;\ge\;
\begin{pmatrix} h \\ -h \\ g \\ 0 \end{pmatrix} .
$$

**Le variabili duali.** Ce n'è una per vincolo, quindi si dividono in quattro vettori, uno per blocco di vincoli: $t$ (con la dimensione di $h$), $w$ (dimensione di $h$), $v$ (dimensione di $g$), $z$ (dimensione di $x$), tutti $\ge 0$.

**La funzione obiettivo duale** è il prodotto scalare del vettore dei termini noti con il vettore delle variabili duali:

$$
h^T t - h^T w + g^T v + 0^T z .
$$

**I vincoli duali.** La trasposta di una matrice a blocchi si fa blocco per blocco; il vincolo "matrice trasposta per variabili duali uguale al vettore dei costi" si spezza in due parti, una per le $x$ e una per le $y$:

$$
\begin{cases}
\max\ h^T t - h^T w + g^T v \\
C^T t - C^T w + E^T v + z = c \\
D^T t - D^T w + F^T v = d \\
t \ge 0,\ w \ge 0,\ v \ge 0,\ z \ge 0 .
\end{cases}
$$

**Due semplificazioni.**

- Il termine $0^T z$ nella funzione obiettivo non serve. Nel primo vincolo le $z$, non negative, si comportano come **variabili di slack**: si possono eliminare trasformando l'uguaglianza in $C^T t - C^T w + E^T v \le c$.
- Le variabili $t$ e $w$ compaiono sempre insieme, e sempre come differenza $t - w$: $h^T(t - w)$, $C^T(t - w)$, $D^T(t - w)$. Sono entrambe non negative, quindi la differenza **non ha vincoli di segno**. Si dà un nome nuovo alla differenza, $s = t - w$, variabile libera.

Il risultato è il **problema duale** di (P):

$$
\text{(D)}\qquad
\begin{cases}
\max\ h^T s + g^T v \\
C^T s + E^T v \le c \\
D^T s + F^T v = d \\
v \ge 0 ,\quad s \text{ libera}.
\end{cases}
$$

La docente ha lasciato il commento alla lezione successiva ("pensate a cosa è successo"): il minimo è diventato un massimo, e alcune variabili duali sono vincolate in segno, le $v$, che sono quelle relative ai vincoli di **disuguaglianza** del primale. La stessa costruzione è svolta nelle dispense, con $u$ al posto di $s$ [@roma2023, §7.1, problema (7.1.6)].

> [!warning] Discrepanza nella trascrizione — il problema duale finale
> Nella registrazione l'ultimo passaggio è in parte confuso (la nuova variabile è detta prima "$T - Q$ doppio", poi $S$, e i vincoli sono letti in modo incompleto). La forma riportata sopra è quella che segue dai passaggi precedenti, e coincide con quella delle dispense.

> [!tip] Approfondimento — Come leggere le corrispondenze #approfondimento
> Confrontando (P) e (D) si leggono le regole che la docente commenterà nella prossima lezione, riassunte così anche nelle dispense [@roma2023, §7.1]:
>
> | primale (min) | duale (max) |
> | --- | --- |
> | vincolo di uguaglianza ($Cx + Dy = h$) | variabile duale **libera** ($s$) |
> | vincolo di disuguaglianza "$\ge$" ($Ex + Fy \ge g$) | variabile duale **$\ge 0$** ($v$) |
> | variabile **$\ge 0$** ($x$) | vincolo duale "$\le$" ($C^T s + E^T v \le c$) |
> | variabile **libera** ($y$) | vincolo duale di **uguaglianza** ($D^T s + F^T v = d$) |
>
> Ogni vincolo di un problema corrisponde a una variabile dell'altro; i termini noti di uno sono i costi dell'altro. Le dispense osservano anche che la costruzione è simmetrica: il duale del duale è il primale. Il caso del paragrafo precedente ($\min c^T x$, $Ax \ge b$, con sole variabili libere e soli vincoli "$\ge$") è un caso particolare: variabili duali $\ge 0$ e vincoli duali di uguaglianza $A^T u = c$.

## Riepilogo

- Fine fase 1 con valore $0$: si cancellano le colonne delle $\alpha$ fuori base; per ogni $\alpha$ rimasta in base (valore $0$, base degenere) si guarda la sua riga sulle $x$. Se è tutta nulla, il vincolo è **ridondante** e si cancella; altrimenti si fa uno **scambio degenere** su un elemento non nullo, di qualunque segno, perché il termine noto è $0$.
- Esercizio 1: $\min 2x_1 + 3x_2 + x_3$; la fase 1 trova la ridondanza del terzo vincolo (somma dei primi due) e la SBA $(1, 1, 0)$; la fase 2 porta all'ottimo $\left(0, \tfrac12, \tfrac32\right)$, valore $3$.
- Esercizio 2: tableau finale con $\alpha_1, \alpha_2$ in base; $\alpha_2$ indica un vincolo ridondante, $\alpha_1$ si scambia con $x_3$ (pivot $-1$); SBA degenere $(10, 0, 0, 0)$.
- Le variabili artificiali servono solo nelle righe che non hanno già una colonna dell'identità (per esempio una slack). Esercizio 3: con una sola $\alpha$, valore ottimo $4 > 0$: problema inammissibile.
- **Dualità**: per $\min c^T x$, $Ax \ge b$ e ogni $u \ge 0$ con $A^T u = c$ vale $b^T u \le c^T x^*$: un minorante calcolabile del valore ottimo, che stima la distanza di un punto ammissibile dall'ottimo. Il **duale** è $\max b^T u$, $A^T u = c$, $u \ge 0$: una variabile duale per vincolo, min $\leftrightarrow$ max, costi $\leftrightarrow$ termini noti.
- Per il primale generale $\min c^T x + d^T y$, $Cx + Dy = h$, $Ex + Fy \ge g$, $x \ge 0$: il duale è $\max h^T s + g^T v$, $C^T s + E^T v \le c$, $D^T s + F^T v = d$, $v \ge 0$, $s$ libera.
