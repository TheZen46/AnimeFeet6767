---
corso: Statistica
modulo: 2
titolo: Probabilità e variabili aleatorie
programma: [STA-01, STA-02, STA-03, STA-04]
anno_accademico: 2026/27
autore: Mobius
versione: 2026-11-05
---

# 2 · Probabilità e variabili aleatorie

**In questo modulo.** Servono il linguaggio degli insiemi (unione, intersezione, complementare), le serie numeriche e gli integrali, anche impropri, di Analisi 1. Il modulo costruisce il modello matematico dei fenomeni casuali: spazio campionario, eventi, assiomi della probabilità. Si impara a contare i casi con il calcolo combinatorio, a usare la probabilità condizionata, la formula delle probabilità totali e quella di Bayes, e a riconoscere eventi indipendenti. Nella seconda parte si introducono le variabili aleatorie, discrete e con densità, la loro legge e la funzione di ripartizione, e si impara a trovare la legge di una funzione di una variabile aleatoria. Il modulo 3 continua con i valori attesi e le leggi notevoli.

## 2.1 Esperimenti, eventi, assiomi

Un **esperimento aleatorio** è una procedura che, ripetuta più volte nelle stesse condizioni, produce risultati diversi. L'insieme dei possibili risultati è lo **spazio campionario** $\Omega$. Qualche esempio: lancio di una moneta, $\Omega = \{T, C\}$; lancio di un dado, $\Omega = \{1, \dots, 6\}$; numero di lanci necessari perché esca testa, $\Omega = \mathbb{N} \setminus \{0\}$; altezza di uno studente scelto a caso, $\Omega = \mathbb{R}$ (o un suo intervallo).

Un **evento** è un sottoinsieme $E \subseteq \Omega$, cioè una collezione di possibili risultati. Se il risultato dell'esperimento è $\omega$, si dice che $E$ **si è verificato** se $\omega \in E$, e che non si è verificato se $\omega \notin E$. Gli eventi si combinano con le operazioni sugli insiemi:

- $\Omega$ è l'evento **certo**, $\emptyset$ l'evento **impossibile**, $\{\omega\}$ un evento **elementare**;
- l'**opposto** $\bar E = \{\omega \in \Omega \mid \omega \notin E\}$ si verifica quando $E$ non si verifica;
- l'**intersezione** $E \cap F$ si verifica quando si verificano entrambi, l'**unione** $E \cup F$ quando se ne verifica almeno uno;
- $E$ e $F$ sono **disgiunti** (incompatibili) se $E \cap F = \emptyset$.

Nel lancio di un dado, con $E$ = "esce un numero pari" $= \{2, 4, 6\}$ e $F$ = "esce un numero primo" $= \{2, 3, 5\}$: se esce 4, $E$ si è verificato e $F$ no; $\bar E = \{1, 3, 5\}$, $E \cap F = \{2\}$, $E \cup F = \{2, 3, 4, 5, 6\}$.

> [!definizione] Probabilità
> Una **probabilità** su $\Omega$ associa a ogni evento $E$ un numero $P[E]$ tale che
>
> 1. $P[\Omega] = 1$;
> 2. $0 \le P[E] \le 1$ per ogni evento $E$;
> 3. se $E_1, E_2, \dots$ sono eventi a due a due disgiunti, $P[E_1 \cup E_2 \cup \dots] = P[E_1] + P[E_2] + \dots$
>
> La coppia $(\Omega, P)$ è uno **spazio di probabilità**.

Conviene pensare a $P[E]$ come all'area di $E$ dentro un quadrato $\Omega$ di area 1: le proprietà che seguono diventano evidenti disegnando gli insiemi.

Il programma distingue tre modi di assegnare le probabilità. La definizione **classica** vale per esiti equiprobabili: casi favorevoli su casi possibili (paragrafo 2.2). La definizione **a posteriori** (frequentista) prende come probabilità di un evento il limite della sua frequenza relativa quando l'esperimento si ripete molte volte; la legge dei grandi numeri del modulo 3 ne è la giustificazione. La definizione **assiomatica** è quella sopra, che comprende le altre due come casi particolari.

> [!teorema] Proprietà della probabilità
>
> 1. $P[\emptyset] = 0$ e $P[\bar E] = 1 - P[E]$;
> 2. se $E \subseteq F$ allora $P[E] \le P[F]$;
> 3. $P[E \cup F] = P[E] + P[F] - P[E \cap F]$;
> 4. principio di inclusione-esclusione per tre eventi:
> $$P[E_1 \cup E_2 \cup E_3] = \sum_i P[E_i] - \sum_{i < j} P[E_i \cap E_j] + P[E_1 \cap E_2 \cap E_3].$$

La 3 si vede scomponendo $E \cup F$ in tre parti disgiunte, $E \setminus F$, $E \cap F$ e $F \setminus E$: sommando $P[E]$ e $P[F]$ si conta due volte l'intersezione. In generale, per $n$ eventi si sommano le probabilità singole, si tolgono quelle delle intersezioni a due, si aggiungono quelle a tre, e così via a segni alterni.

## 2.2 Spazi finiti ed equiprobabili

Uno spazio di probabilità è **finito** se $\Omega = \{\omega_1, \dots, \omega_N\}$. Allora basta conoscere le probabilità degli eventi elementari $p_i = P[\{\omega_i\}]$, che sono numeri $p_i \ge 0$ con $p_1 + \dots + p_N = 1$: per l'additività, la probabilità di un evento è la somma delle $p_i$ dei suoi elementi. Per esempio, una moneta truccata ha $P[T] = p$ e $P[C] = q = 1 - p$, con $0 \le p \le 1$; la moneta è equilibrata se $p = q = \frac12$.

Lo spazio è **equiprobabile** se tutti i risultati hanno la stessa probabilità: allora $p_i = \frac{1}{N}$ e
$$P[E] = \frac{\# E}{\# \Omega} = \frac{\text{casi favorevoli}}{\text{casi possibili}}.$$

Con un dado equilibrato, $P[\text{pari}] = \frac36 = 50\%$ e $P[\text{primo}] = \frac46 \approx 67\%$. La somma di queste due probabilità supera 1, e non c'è contraddizione: i due eventi non sono disgiunti (hanno in comune il 2), e infatti $P[E \cup F] = \frac12 + \frac23 - \frac16 = \frac56$.

> [!attenzione] Scegliere bene lo spazio campionario
> Lanciando due dadi, la somma va da 2 a 12, ma lo spazio $\{2, \dots, 12\}$ **non** è equiprobabile. Lo è lo spazio delle 36 coppie ordinate (primo dado, secondo dado). La somma 7 si ottiene con 6 coppie, quindi $P[\text{somma } 7] = \frac{6}{36} = \frac16$; la somma 11 con 2 coppie, $(5, 6)$ e $(6, 5)$, quindi $P = \frac{2}{36} = \frac{1}{18}$.

Con tre dadi la somma 9 e la somma 10 si ottengono entrambe con sei terne non ordinate di numeri, ma contando le permutazioni la 9 ha 25 casi su $6^3 = 216$ e la 10 ne ha 27: $P[9] \approx 11{,}6\%$, $P[10] = \frac18 = 12{,}5\%$.

## 2.3 Calcolo combinatorio

Negli spazi equiprobabili tutto si riduce a contare. Si ricordano il **fattoriale** $n! = 1 \cdot 2 \cdots n$, con $0! = 1$, e il **coefficiente binomiale**
$$\binom{n}{k} = \frac{n!}{k!\,(n - k)!}, \qquad 0 \le k \le n.$$

Il problema tipico è: in quanti modi si possono scegliere $k$ oggetti da un'urna che contiene $n$ oggetti distinti? Dipende da due cose: se l'oggetto estratto viene rimesso nell'urna (estrazione **con ripetizione**, lo stesso oggetto può uscire più volte) o no, e se l'ordine conta (**disposizioni**) o no (**combinazioni**).

| | Conta l'ordine | Non conta l'ordine |
|---|---|---|
| Senza ripetizione ($k \le n$) | $n(n-1)\cdots(n-k+1) = \dfrac{n!}{(n-k)!}$ | $\dbinom{n}{k}$ |
| Con ripetizione | $n^k$ | $\dbinom{n + k - 1}{k}$ |

Per $k = n$ le disposizioni senza ripetizione sono le **permutazioni**, $n!$. Le combinazioni si ottengono dalle disposizioni dividendo per $k!$, perché ogni gruppo di $k$ oggetti si può ordinare in $k!$ modi.

> [!teorema] Proprietà del coefficiente binomiale
> $$\binom{n}{0} = \binom{n}{n} = 1, \qquad \binom{n}{k} = \binom{n}{n - k}, \qquad \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k},$$
> $$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k} \quad (\text{binomio di Newton}).$$

> [!esempio] Urne, lotto, poker
>
> - Un'urna contiene 12 palline rosse e 8 bianche e se ne estraggono 4 senza reimmissione. I casi possibili sono $\binom{20}{4}$; per avere 2 rosse e 2 bianche si scelgono 2 rosse fra 12 e 2 bianche fra 8: $P = \binom{12}{2}\binom{8}{2} / \binom{20}{4} \approx 38\%$.
> - Al lotto si estraggono 5 numeri su 90. Un terno secco (tre numeri giocati, tutti estratti) ha probabilità $\binom{87}{2} / \binom{90}{5} = \frac{5 \cdot 4 \cdot 3}{90 \cdot 89 \cdot 88} = \frac{1}{11748} \approx 8{,}5 \cdot 10^{-5}$. Se la vincita fosse $V$ volte la posta, il gioco sarebbe equo per $(1 - p) \cdot 1 = p V$, cioè $V = \frac1p - 1 = 11747$; il lotto ne paga 4500.
> - A poker si ricevono 5 carte da un mazzo di 52 (13 valori, 4 semi): i casi possibili sono $\binom{52}{5} \approx 2{,}6 \cdot 10^6$. Una **doppia coppia** si forma scegliendo i due valori delle coppie, $\binom{13}{2}$, i semi di ciascuna coppia, $\binom42^2$, e la quinta carta fra le 44 di altro valore: $123\,552$ casi, $P \approx 4{,}8\%$. Un **full** (tris e coppia): $13 \cdot 12 \cdot \binom43 \binom42 = 3744$ casi, $P \approx 0{,}14\%$.
> - I monomi di grado 6 in tre variabili $x, y, z$ corrispondono a scegliere 6 volte una variabile con ripetizione senza ordine: $\binom{8}{6} = 28$. Quelli che contengono tutte e tre le variabili si ottengono moltiplicando $xyz$ per un monomio di grado 3: $\binom{5}{3} = 10$. Scegliendone uno a caso, $P = \frac{10}{28} = \frac{5}{14} \approx 36\%$.

## 2.4 Probabilità condizionata

Spesso si sa che un evento $E$ si è verificato e ci si chiede quanto sia probabile un altro evento $F$. L'informazione riduce lo spazio dei risultati possibili a $E$.

> [!definizione] Probabilità condizionata
> Se $P[E] > 0$, la **probabilità di $F$ dato $E$** è
> $$P[F \mid E] = \frac{P[E \cap F]}{P[E]}.$$

Fissato $E$, la funzione $F \mapsto P[F \mid E]$ è una probabilità (verifica gli assiomi): è la distribuzione di probabilità condizionata al fatto che $E$ si è verificato. Rovesciando la definizione si ottiene la **regola del prodotto** e, iterandola, la **regola della catena**:
$$P[E \cap F] = P[E]\, P[F \mid E], \qquad P[E_1 \cap \dots \cap E_n] = P[E_1]\, P[E_2 \mid E_1] \cdots P[E_n \mid E_1 \cap \dots \cap E_{n-1}].$$

> [!esempio] Due carte di fiori
> Si estraggono due carte da un mazzo di 52. Con $E$ = "la prima è di fiori" e $F$ = "la seconda è di fiori", $P[E] = \frac{13}{52}$ e, sapendo che la prima è di fiori, ne restano 12 su 51: $P[F \mid E] = \frac{12}{51}$. Quindi $P[E \cap F] = \frac{13}{52} \cdot \frac{12}{51}$, lo stesso risultato di $\binom{13}{2}/\binom{52}{2}$.

> [!attenzione] Il condizionato dell'opposto
> In generale $P[F \mid \bar E] \neq 1 - P[F \mid E]$. Nell'esempio, $P[F \mid \bar E] = \frac{13}{51}$, mentre $1 - P[F \mid E] = \frac{39}{51}$. Vale invece $P[\bar F \mid E] = 1 - P[F \mid E]$: si complementa l'evento, non la condizione.

Altri due esempi. Si lancia due volte un dado a 4 facce e si sa che la somma è 4: le coppie possibili sono $(1, 3)$, $(2, 2)$, $(3, 1)$, quindi $P[\text{primo lancio } 3 \mid \text{somma } 4] = \frac13$. A poker la probabilità di una scala reale (asso, re, donna, fante e dieci dello stesso seme) è $\frac{4}{\binom{52}{5}} \approx 1{,}5 \cdot 10^{-6}$; sapendo che la prima carta ricevuta è l'asso di cuori, deve essere la scala reale di cuori e le altre quattro carte sono determinate: $\frac{1}{\binom{51}{4}} \approx 4 \cdot 10^{-6}$, circa $\frac{13}{5}$ volte di più.

## 2.5 Probabilità totali e formula di Bayes

Una famiglia di eventi $E_1, \dots, E_n$ è una **partizione** di $\Omega$ se gli eventi sono a due a due disgiunti e la loro unione è $\Omega$: in ogni prova se ne verifica esattamente uno. Il caso più semplice è la partizione $\{E, \bar E\}$.

> [!teorema] Formula delle probabilità totali
> Se $E_1, \dots, E_n$ è una partizione di $\Omega$, per ogni evento $F$
> $$P[F] = P[F \mid E_1]\, P[E_1] + \dots + P[F \mid E_n]\, P[E_n].$$
> In particolare $P[F] = P[F \mid E]\, P[E] + P[F \mid \bar E]\, P[\bar E]$.

Basta scrivere $F$ come unione disgiunta degli $F \cap E_i$ e applicare la regola del prodotto. La formula si usa quando l'esperimento avviene in due stadi: prima si verifica uno degli $E_i$, poi $F$ con una probabilità che dipende da quale. Per la seconda carta di fiori: $P[F] = \frac{12}{51}\cdot\frac{13}{52} + \frac{13}{51}\cdot\frac{39}{52} = \frac{13}{52} = \frac14$, come se la prima carta non ci fosse.

> [!teorema] Formula di Bayes
> Se $E_1, \dots, E_n$ è una partizione e $P[F] > 0$,
> $$P[E_k \mid F] = \frac{P[F \mid E_k]\, P[E_k]}{P[F \mid E_1]\, P[E_1] + \dots + P[F \mid E_n]\, P[E_n]}.$$

La formula "rovescia" il condizionamento: dalle probabilità dell'effetto date le cause si risale alla probabilità di una causa dato l'effetto osservato. Le $P[E_k]$ si dicono probabilità **a priori**, le $P[E_k \mid F]$ **a posteriori**.

> [!esempio] Dado e moneta
> Si lancia un dado equilibrato e poi una moneta equilibrata tante volte quanto è uscito sul dado. Con $E_i$ = "il dado dà $i$" e $F$ = "escono 4 teste", si ha $P[F \mid E_i] = 0$ per $i \le 3$ e $P[F \mid E_i] = \binom{i}{4}/2^i$ altrimenti: $\frac{1}{16}$, $\frac{5}{32}$, $\frac{15}{64}$ per $i = 4, 5, 6$. Per le probabilità totali
> $$P[F] = \frac16\left(\frac{4}{64} + \frac{10}{64} + \frac{15}{64}\right) = \frac{29}{384} \approx 7{,}6\%.$$
> Sapendo che sono uscite 4 teste, la probabilità che il dado abbia dato 5 è, per Bayes, $\frac{\frac16 \cdot \frac{10}{64}}{\frac{29}{384}} = \frac{10}{29} \approx 34\%$.

> [!esempio] Exit poll
> In un ballottaggio il candidato A prende il 45% dei voti e B il 55%. All'uscita dai seggi risponde al sondaggio il 40% degli elettori di A e il 30% di quelli di B. Con $E$ = "ha votato A" e $F$ = "risponde":
> $$P[E \mid F] = \frac{0{,}40 \cdot 0{,}45}{0{,}40 \cdot 0{,}45 + 0{,}30 \cdot 0{,}55} = \frac{180}{345} = \frac{12}{23} \approx 52\%.$$
> Il sondaggio darebbe vincente A, che perde: la diversa disponibilità a rispondere distorce il campione.

## 2.6 Eventi indipendenti

> [!definizione] Indipendenza
> Due eventi $E$, $F$ sono **indipendenti** se $P[E \cap F] = P[E]\, P[F]$. Tre eventi $E_1, E_2, E_3$ sono indipendenti se $P[E_i \cap E_j] = P[E_i]\, P[E_j]$ per ogni $i \neq j$ e inoltre $P[E_1 \cap E_2 \cap E_3] = P[E_1]\, P[E_2]\, P[E_3]$.

Se $P[E] > 0$, l'indipendenza equivale a $P[F \mid E] = P[F]$: sapere che $E$ si è verificato non cambia la probabilità di $F$. Le prove ripetute di un esperimento (lanci successivi di una moneta, estrazioni con reimmissione) si modellano come indipendenti.

> [!attenzione] Disgiunti non vuol dire indipendenti
> Se $E$ e $F$ hanno probabilità positive e sono disgiunti, $P[E \cap F] = 0 \neq P[E]\, P[F]$: non sono indipendenti, anzi, se si verifica uno l'altro è escluso. Per eventi disgiunti $P[E \cup F] = P[E] + P[F]$; per eventi indipendenti $P[E \cup F] = P[E] + P[F] - P[E]\, P[F]$.

Esempio: una moneta truccata ha probabilità di testa doppia di quella di croce, quindi $P[T] = \frac23$, $P[C] = \frac13$. Lanciandola 3 volte, l'evento "2 teste e 1 croce" è l'unione disgiunta di $TTC$, $TCT$, $CTT$, e per l'indipendenza dei lanci ciascuno ha probabilità $\left(\frac23\right)^2 \cdot \frac13$: in totale $3 \cdot \frac{4}{27} = \frac49$, contro $\frac38$ per una moneta equilibrata.

## 2.7 Variabili aleatorie e loro legge

> [!definizione] Variabile aleatoria
> Dato uno spazio di probabilità $(\Omega, P)$, una **variabile aleatoria** è una funzione $X : \Omega \to \mathbb{R}$, che associa a ogni risultato $\omega$ un numero $X(\omega)$.

Si scrive $\{X \in I\} = \{\omega \in \Omega \mid X(\omega) \in I\}$ per l'evento "$X$ assume un valore in $I$", e allo stesso modo $\{X = x\}$, $\{X \le x\}$, $\{X > x\}$. Esempi: il numero di teste in 3 lanci, $X \in \{0, 1, 2, 3\}$; il numero di lanci fino alla prima testa, $X \in \{1, 2, \dots\}$; il tempo di attesa a un call center, $X \in [0, +\infty)$. Un esempio fondamentale è la **variabile indicatrice** di un evento $E$:
$$\mathbb{1}_E(\omega) = \begin{cases} 1 & \omega \in E, \\ 0 & \omega \notin E, \end{cases}$$
che vale 1 in caso di "successo" e 0 di "insuccesso".

Una variabile è **finita** se assume un numero finito di valori $x_1, \dots, x_n$, **discreta** se ne assume un'infinità numerabile $x_1, x_2, \dots$. In entrambi i casi gli eventi $\{X = x_k\}$ formano una partizione di $\Omega$ e $X = \sum_k x_k \mathbb{1}_{\{X = x_k\}}$.

> [!definizione] Legge di una variabile aleatoria
> La **legge** (o distribuzione) di $X$ è la funzione che a ogni insieme $I \subseteq \mathbb{R}$ associa $\mu_X(I) = P[X \in I]$. Per una variabile finita o discreta è determinata dalla **densità discreta** $p_k = P[X = x_k]$, con $p_k \ge 0$ e $\sum_k p_k = 1$, e
> $$P[X \in I] = \sum_{k \,:\, x_k \in I} p_k.$$

La legge si rappresenta con una tabella $x_k \mapsto p_k$ o con un grafico a bastoncini. Per il numero di teste in 3 lanci di una moneta equilibrata i valori 0, 1, 2, 3 hanno probabilità $\frac18, \frac38, \frac38, \frac18$; con la moneta truccata del paragrafo 2.6, $\frac{1}{27}, \frac{6}{27}, \frac{12}{27}, \frac{8}{27}$.

Due variabili diverse possono avere la stessa legge; si scrive $X \sim Y$. Lanciando due volte una moneta equilibrata, sia $X$ l'indicatrice di "testa al primo lancio" e $Y$ quella di "testa al secondo". Sul risultato $(T, C)$ si ha $X = 1$ e $Y = 0$, quindi $X \neq Y$; ma entrambe valgono 0 o 1 con probabilità $\frac12$, quindi $X \sim Y$.

Per una variabile discreta la condizione $\sum p_k = 1$ è la somma di una serie. Per il numero $N$ di lanci di una moneta equilibrata fino alla prima testa, $P[N = n] = \left(\frac12\right)^{n-1} \cdot \frac12 = \frac{1}{2^n}$ ($n - 1$ croci e poi una testa), e infatti $\sum_{n \ge 1} \frac{1}{2^n} = 1$ (in base 2 è $0{,}111\ldots_2 = 1$).

## 2.8 Variabili con densità

Per grandezze che variano con continuità (tempi, lunghezze, pesi) ogni singolo valore ha probabilità nulla, e la probabilità si assegna agli intervalli con un integrale.

> [!definizione] Densità di probabilità
> Una variabile aleatoria $X$ ha **densità** $f$ se per ogni $a < b$
> $$P[a \le X \le b] = \int_a^b f(x)\, dx,$$
> dove $f$ è continua tranne al più in un numero finito di punti $x_1, \dots, x_N$ (in cui l'integrale si intende improprio, come anche agli estremi $\pm\infty$).

![Figura 2.1 · La probabilità che $X$ cada in $[a, b]$ è l'area sotto la densità.](../figure/2-1.svg)

> [!teorema] Proprietà delle densità
>
> - $f(x) \ge 0$ e $\int_{-\infty}^{+\infty} f(x)\, dx = 1$;
> - $P[X = x] = 0$ per ogni $x$, quindi includere o no gli estremi non cambia nulla: $P[a \le X \le b] = P[a < X < b]$;
> - $P[X \le b] = \int_{-\infty}^b f(x)\, dx$ e $P[X \ge a] = \int_a^{+\infty} f(x)\, dx$;
> - se $f = 0$ fuori da $[m, M]$, allora $m \le X \le M$ con probabilità 1.

Viceversa, ogni funzione non negativa con integrale 1 è la densità di qualche variabile aleatoria. Il valore $f(x)$ non è una probabilità (può essere maggiore di 1): è una "probabilità per unità di lunghezza".

> [!esempio] Determinare la costante di una densità
>
> - Un numero estratto uniformemente fra $\frac12$ e 1 ha densità costante $c$ su $(\frac12, 1)$ e nulla altrove. L'area deve essere 1: $c \cdot \frac12 = 1$, quindi $c = 2$.
> - $f(x) = mx$ per $0 \le x \le 1$, nulla altrove: $\int_0^1 mx\, dx = \frac{m}{2} = 1$ dà $m = 2$. Allora $P[\lvert X\rvert \ge \frac12] = P[X \ge \frac12] = \int_{1/2}^1 2x\, dx = 1 - \frac14 = \frac34$.
> - $f(x) = a$ su $[-1, 0]$, $f(x) = b$ su $[1, \frac32]$, nulla altrove, con $a, b \ge 0$: la condizione $a + \frac{b}{2} = 1$ dà $b = 2 - 2a$ con $0 \le a \le 1$. C'è una famiglia di densità, non una sola.
> - $f(x) = \frac{a}{1 + x^2}$ su tutto $\mathbb{R}$: per simmetria $\int f = 2a \lim_{b \to +\infty} \arctan b = a\pi$, quindi $a = \frac{1}{\pi}$ (densità di Cauchy).

## 2.9 Funzione di ripartizione

> [!definizione] Funzione di ripartizione
> La **funzione di ripartizione** di $X$ è $F_X(x) = P[X \le x]$, definita per ogni $x \in \mathbb{R}$. Per una variabile discreta $F_X(x) = \sum_{x_k \le x} p_k$; per una variabile con densità $F_X(x) = \int_{-\infty}^x f(t)\, dt$.

Nel caso discreto $F_X$ è a gradini, con un salto di altezza $p_k$ in ogni $x_k$: per il numero di teste in 3 lanci vale 0 per $x < 0$, $\frac18$ su $[0, 1)$, $\frac12$ su $[1, 2)$, $\frac78$ su $[2, 3)$ e 1 per $x \ge 3$. Con densità è una funzione integrale: per $X$ uniforme su $(0, 1)$ vale 0 per $x < 0$, $x$ per $0 \le x \le 1$, 1 per $x > 1$.

> [!teorema] Proprietà della funzione di ripartizione
>
> 1. $F_X$ è crescente (non decrescente) e $0 \le F_X \le 1$;
> 2. $\lim_{x \to -\infty} F_X(x) = 0$ e $\lim_{x \to +\infty} F_X(x) = 1$;
> 3. $F_X$ è continua a destra, e il salto in $x_0$ è $P[X = x_0]$: $\lim_{x \to x_0^-} F_X(x) = F_X(x_0) - P[X = x_0]$;
> 4. $P[x_1 < X \le x_2] = F_X(x_2) - F_X(x_1)$;
> 5. $F_X = F_Y$ se e solo se $X \sim Y$: la funzione di ripartizione determina la legge;
> 6. se $X$ ha densità $f$, $F_X$ è continua, è di classe $C^1$ fuori dai punti di discontinuità $x_1, \dots, x_N$ di $f$, e lì $F_X' = f$.

Vale anche il viceversa della 6: se $F$ è crescente, con limiti 0 e 1, continua, e di classe $C^1$ fuori da un numero finito di punti, allora è la funzione di ripartizione di una variabile con densità $f = F'$ (con valori arbitrari nei punti eccezionali). Per esempio $F(x) = 0$ per $x \le 0$, $\sqrt{x}$ per $0 < x < 1$, 1 per $x \ge 1$ ha queste proprietà: è la funzione di ripartizione della densità $f(x) = \frac{1}{2\sqrt{x}}$ su $(0, 1)$.

## 2.10 Funzioni di variabili aleatorie

Se $X$ è una variabile aleatoria e $\phi : \mathbb{R} \to \mathbb{R}$ una funzione, $Y = \phi(X)$, cioè $Y(\omega) = \phi(X(\omega))$, è un'altra variabile aleatoria. Per esempio: si vincono 2 euro se esce testa e se ne perdono 3 se esce croce; con $X$ l'indicatrice di testa, il bilancio è $Y = 5X - 3$.

**Caso discreto.** Se $X$ è discreta, anche $Y$ lo è, con valori $\phi(x_k)$ (qualcuno può ripetersi), e
$$P[Y = y] = \sum_{k \,:\, \phi(x_k) = y} P[X = x_k].$$

> [!esempio] Un gioco da 11 euro
> Si pagano 11 euro per giocare; il banco lancia 4 volte una moneta equilibrata e paga il quadrato del numero di teste più 2 euro per ogni croce. Con $X$ = numero di teste, la vincita netta è $Y = X^2 + 2(4 - X) - 11 = X^2 - 2X - 3$.
>
> | $x$ | 0 | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|---|
> | $y = x^2 - 2x - 3$ | $-3$ | $-4$ | $-3$ | 0 | 5 |
> | $P[X = x]$ | $\frac{1}{16}$ | $\frac{4}{16}$ | $\frac{6}{16}$ | $\frac{4}{16}$ | $\frac{1}{16}$ |
>
> I valori $x = 0$ e $x = 2$ danno lo stesso $y$, quindi la legge di $Y$ è: $P[Y = -4] = \frac{4}{16}$, $P[Y = -3] = \frac{7}{16}$, $P[Y = 0] = \frac{4}{16}$, $P[Y = 5] = \frac{1}{16}$.

**Caso con densità.** Se $X$ ha densità $f_X$ e $\phi$ è regolare, si passa per la funzione di ripartizione:

1. si trovano i valori che $Y$ può assumere: se $a \le X \le b$ e $\phi$ manda $[a, b]$ in $[m, M]$, allora $F_Y(y) = 0$ per $y < m$ e $F_Y(y) = 1$ per $y > M$;
2. per $m < y < M$ si scrive $F_Y(y) = P[\phi(X) \le y] = P[X \in I_y]$, dove $I_y = \{x \mid \phi(x) \le y\}$; di solito $I_y$ è un intervallo $[a, x_2(y)]$ oppure $[x_1(y), x_2(y)]$, e allora $F_Y(y) = F_X(x_2(y))$ oppure $F_X(x_2(y)) - F_X(x_1(y))$;
3. si deriva: $f_Y(y) = F_Y'(y)$, direttamente o con la regola della funzione composta, $f_Y(y) = f_X(x_2(y))\, x_2'(y) - f_X(x_1(y))\, x_1'(y)$.

> [!esempio] Una trasformazione lineare
> $X$ ha densità $f_X(x) = 2x$ su $(0, 1)$, nulla altrove, e $Y = -3X + 1$. Per $0 \le X \le 1$ si ha $-2 \le Y \le 1$. Per $-2 < y < 1$:
> $$F_Y(y) = P[-3X + 1 \le y] = P\left[X \ge \tfrac{1 - y}{3}\right] = 1 - F_X\left(\tfrac{1 - y}{3}\right) = 1 - \left(\tfrac{1 - y}{3}\right)^2,$$
> perché $F_X(x) = x^2$ su $[0, 1]$. Derivando, $f_Y(y) = \frac{2}{9}(1 - y)$ su $(-2, 1)$, nulla altrove.

> [!esempio] Una trasformazione non monotona
> $X$ è uniforme su $(0, 1)$ e $Y = (3X - 1)^2$, con valori in $[0, 4]$. Per $y > 0$:
> $$F_Y(y) = P\left[-\sqrt{y} \le 3X - 1 \le \sqrt{y}\right] = P\left[\tfrac{1 - \sqrt{y}}{3} \le X \le \tfrac{1 + \sqrt{y}}{3}\right].$$
> Se $0 < y < 1$ entrambi gli estremi stanno in $[0, 1]$ e $F_Y(y) = \frac{2\sqrt{y}}{3}$; se $1 \le y < 4$ l'estremo sinistro è negativo e $F_Y(y) = \frac{1 + \sqrt{y}}{3}$. Derivando:
> $$f_Y(y) = \frac{1}{3\sqrt{y}} \ \text{per } 0 < y < 1, \qquad f_Y(y) = \frac{1}{6\sqrt{y}} \ \text{per } 1 < y < 4.$$

Non tutte le variabili sono discrete o con densità. Se $X$ è uniforme su $(0, 2)$ e $Y = 0$ per $X \le 1$, $Y = X - 1$ per $X > 1$, allora $P[Y = 0] = \frac12$ (quindi $Y$ non ha densità), ma per $0 < y < 1$ si ha $F_Y(y) = \frac{y + 1}{2}$, che cresce con continuità (quindi $Y$ non è discreta). La funzione di ripartizione ha un salto di $\frac12$ in 0 e poi una rampa.

## Esempi ed esercizi svolti

**Esercizio 1 (il problema dei compleanni).** In un gruppo di $n$ persone, qual è la probabilità che almeno due compiano gli anni lo stesso giorno? Si suppongono 365 giorni equiprobabili e indipendenti. L'evento opposto è "tutti nati in giorni diversi": il primo può essere nato in qualsiasi giorno, il secondo in 364 su 365, e così via. Per $n \le 365$:
$$p_n = 1 - \frac{365 \cdot 364 \cdots (365 - n + 1)}{365^n} = 1 - \left(1 - \frac{1}{365}\right)\left(1 - \frac{2}{365}\right)\cdots\left(1 - \frac{n-1}{365}\right).$$
Con $1 + x \approx e^x$ per $\lvert x\rvert$ piccolo, il prodotto è circa $e^{-(1 + 2 + \dots + (n-1))/365}$, quindi $p_n \approx 1 - e^{-n(n-1)/730}$. Tutt'altra cosa è la probabilità che qualcuno del gruppo sia nato **nel mio** compleanno: $q_n = 1 - \left(\frac{364}{365}\right)^n$.

| $n$ | 10 | 23 | 30 | 50 |
|---|---|---|---|---|
| $p_n$ | 0,117 | 0,507 | 0,706 | 0,970 |
| $1 - e^{-n(n-1)/730}$ | 0,116 | 0,500 | 0,696 | 0,965 |
| $q_n$ | 0,027 | 0,061 | 0,079 | 0,128 |

Con 23 persone si supera il 50%: il risultato sorprende perché si pensa a $q_n$ invece che a $p_n$. Per $n = 3$ si può anche usare l'inclusione-esclusione sugli eventi $E_{ij}$ = "$i$ e $j$ sono nati lo stesso giorno": $3 \cdot \frac{1}{365} - 3 \cdot \frac{1}{365^2} + \frac{1}{365^2} \approx 0{,}0082$.

**Esercizio 2 (coincidenze).** Da un'urna con palline numerate da 1 a $n$ se ne estraggono alcune una dopo l'altra senza reimmissione. Qual è la probabilità che alla terza estrazione esca la pallina numero 3? Con la regola della catena: non esce alla prima ($\frac{n-1}{n}$), non esce alla seconda ($\frac{n-2}{n-1}$), esce alla terza ($\frac{1}{n-2}$). Il prodotto è $\frac1n$: ogni pallina ha la stessa probabilità di uscire in ogni posizione. Con $n = 10$, $\frac{1}{10}$.

**Esercizio 3 (dieci coppie, dieci cabine).** Su una nave ci sono 10 cabine doppie prenotate da 10 coppie; all'imbarco le 20 persone sono assegnate alle cabine a caso. Qual è la probabilità che ogni coppia finisca nella stessa cabina? Con la regola della catena, cabina per cabina: la prima cabina riceve una delle 10 coppie con probabilità $\frac{10}{\binom{20}{2}}$, la seconda una delle 9 rimaste con probabilità $\frac{9}{\binom{18}{2}}$, e così via. Il prodotto si semplifica in
$$\frac{10!\, 2^{10}}{20!} = \frac{1}{19 \cdot 17 \cdot 15 \cdots 3 \cdot 1} \approx 1{,}5 \cdot 10^{-9}.$$

**Esercizio 4 (una densità a due parametri).** Nella densità $f = a$ su $[-1, 0]$, $f = b$ su $[1, \frac32]$ del paragrafo 2.8, con $a = \frac12$ si ha $b = 1$; allora $P[X > 0] = \frac{b}{2} = \frac12$ e $F_X(x) = \frac{x + 1}{2}$ su $[-1, 0]$, costante $\frac12$ su $[0, 1]$, $\frac12 + (x - 1)$ su $[1, \frac32]$. La funzione di ripartizione è continua, con un tratto piatto dove la densità è nulla.

### Altri esercizi svolti

**Esercizio 4. Il test diagnostico.** Una malattia colpisce il 2% della popolazione. Un test la rileva nel 95% dei malati (sensibilità) e dà esito negativo nel 90% dei sani (specificità). Una persona risulta positiva: qual è la probabilità che sia malata?

Con $M$ = "malato" e $+$ = "test positivo": $P(+ \mid M) = 0{,}95$, $P(+ \mid \bar M) = 0{,}10$. Per le probabilità totali $P(+) = 0{,}95 \cdot 0{,}02 + 0{,}10 \cdot 0{,}98 = 0{,}019 + 0{,}098 = 0{,}117$, e per Bayes
$$P(M \mid +) = \frac{0{,}019}{0{,}117} = 0{,}16.$$
Solo il 16% dei positivi è malato. Non è un difetto del test: la malattia è rara, e i falsi positivi, il 10% di una popolazione grande, sono molti più dei veri positivi. Per questo un test di screening positivo si conferma con un secondo test.

**Esercizio 5. Carte.** Da un mazzo di 40 carte con 4 assi se ne estraggono 5 senza reimmissione. Probabilità di esattamente 2 assi?

I casi possibili sono le $\binom{40}{5} = 658\,008$ mani; quelle favorevoli si ottengono scegliendo 2 assi fra 4 e 3 carte fra le 36 non assi: $\binom{4}{2}\binom{36}{3} = 6 \cdot 7140 = 42\,840$. La probabilità è $\frac{42\,840}{658\,008} = 0{,}065$. È la legge ipergeometrica.

**Esercizio 6. Una funzione di ripartizione con due parametri.** $F(x) = 0$ per $x < 0$, $F(x) = ax^2$ per $0 \le x < 2$, $F(x) = b$ per $x \ge 2$. Per quali $a, b$ è la funzione di ripartizione di una variabile con densità? Calcolare la densità e $P(0{,}5 \le X \le 1)$.

Serve $F(x) \to 1$ per $x \to +\infty$, quindi $b = 1$; serve la continuità (una variabile con densità non ha "salti"), quindi in 2 $4a = 1$, $a = \frac14$. La densità è la derivata, $f(x) = \frac{x}{2}$ su $(0, 2)$ e 0 altrove. $P(0{,}5 \le X \le 1) = F(1) - F(0{,}5) = \frac14 - \frac{1}{16} = \frac{3}{16}$.

**Esercizio 7. Dall'uniforme all'esponenziale.** $X$ è uniforme su $(0, 1)$ e $Y = -\frac12\ln X$. Trovare la legge di $Y$.

$Y$ è positiva. Per $y > 0$: $F_Y(y) = P\left(-\tfrac12\ln X \le y\right) = P(\ln X \ge -2y) = P(X \ge e^{-2y}) = 1 - e^{-2y}$. È l'esponenziale di parametro 2. È il modo in cui un computer genera numeri esponenziali a partire da numeri uniformi.

**Esercizio 8. Una trasformazione non monotona.** $X$ è uniforme su $(0, 1)$ e $Y = (2X - 1)^2$. Densità di $Y$?

$Y \in [0, 1]$. Per $0 \le y \le 1$: $F_Y(y) = P(|2X - 1| \le \sqrt y) = P\left(\frac{1 - \sqrt y}{2} \le X \le \frac{1 + \sqrt y}{2}\right) = \sqrt y$, la lunghezza dell'intervallo. Derivando, $f_Y(y) = \frac{1}{2\sqrt y}$ su $(0, 1)$. La densità è illimitata vicino a 0: tutti gli $X$ vicini a $\frac12$ finiscono vicino a $Y = 0$.

## Esercizi guidati

Ogni esercizio è diviso in passi: si prova un passo alla volta e si confronta solo dopo.

**Guidato 1. Bayes con tre macchine.** Tre macchine producono il 50%, il 30% e il 20% dei pezzi, con difettosità dell'1%, del 2% e del 3%. Un pezzo è difettoso: da quale macchina viene più probabilmente?

*Passo 1: le probabilità congiunte.* $P(M_1 \cap D) = 0{,}5 \cdot 0{,}01 = 0{,}005$; $P(M_2 \cap D) = 0{,}3 \cdot 0{,}02 = 0{,}006$; $P(M_3 \cap D) = 0{,}2 \cdot 0{,}03 = 0{,}006$.

*Passo 2: probabilità totale.* $P(D) = 0{,}017$.

*Passo 3: Bayes.* $P(M_1 \mid D) = \frac{0{,}005}{0{,}017} = 0{,}29$; $P(M_2 \mid D) = P(M_3 \mid D) = \frac{0{,}006}{0{,}017} = 0{,}35$.

*Passo 4: la lettura.* La macchina 1 produce metà dei pezzi ma è la meno probabile come origine di un difetto. Le probabilità a posteriori sommano a 1: è il controllo da fare sempre.

**Guidato 2. Due eventi indipendenti senza che sembri.** Si lanciano due dadi. $A$ = "la somma è 7", $B$ = "il primo dado mostra 3". Sono indipendenti?

*Passo 1.* $P(A) = \frac{6}{36} = \frac16$ (le coppie $(1, 6), \dots, (6, 1)$).

*Passo 2.* $P(B) = \frac16$.

*Passo 3.* $A \cap B = \{(3, 4)\}$, quindi $P(A \cap B) = \frac{1}{36} = P(A)P(B)$: indipendenti.

*Passo 4: il confronto.* Con "la somma è 8" al posto di 7 non lo sarebbero: $P = \frac{5}{36}$ e $P(\text{somma } 8 \cap B) = \frac{1}{36} \ne \frac{5}{216}$. Con la somma 7, qualunque sia il primo dado c'è sempre esattamente un valore del secondo che funziona, e sapere il primo non cambia niente.

**Guidato 3. $Y = X^2$ con $X$ uniforme su $(-1, 2)$.**

*Passo 1: i valori di $Y$.* $X \in (-1, 2)$, quindi $Y \in [0, 4)$.

*Passo 2: per $0 \le y \le 1$.* $Y \le y$ se $-\sqrt y \le X \le \sqrt y$, un intervallo tutto dentro $(-1, 2)$ di lunghezza $2\sqrt y$: $F_Y(y) = \frac{2\sqrt y}{3}$.

*Passo 3: per $1 < y < 4$.* Ora $-\sqrt y < -1$, e l'intervallo utile è $(-1, \sqrt y]$: $F_Y(y) = \frac{\sqrt y + 1}{3}$.

*Passo 4: la densità.* Derivando, $f_Y(y) = \frac{1}{3\sqrt y}$ su $(0, 1)$ e $\frac{1}{6\sqrt y}$ su $(1, 4)$. Controllo: $\int_0^1 \frac{dy}{3\sqrt y} + \int_1^4 \frac{dy}{6\sqrt y} = \frac23 + \frac13 = 1$.

## Riepilogo

Un esperimento aleatorio si modella con uno spazio campionario $\Omega$, i cui sottoinsiemi sono gli eventi, e una probabilità che verifica gli assiomi ($P[\Omega] = 1$, valori in $[0, 1]$, additività sugli eventi disgiunti); ne seguono la regola del complementare e l'inclusione-esclusione. Negli spazi equiprobabili la probabilità è casi favorevoli su casi possibili e si calcola con disposizioni ($n!/(n-k)!$ o $n^k$) e combinazioni ($\binom{n}{k}$ o $\binom{n+k-1}{k}$). La probabilità condizionata $P[F \mid E] = P[E \cap F]/P[E]$ dà la regola del prodotto e della catena, la formula delle probabilità totali su una partizione e la formula di Bayes per risalire dalle osservazioni alle cause. Due eventi sono indipendenti se la probabilità dell'intersezione è il prodotto, il che non ha niente a che fare con l'essere disgiunti. Una variabile aleatoria è una funzione numerica del risultato; la sua legge si descrive con la densità discreta nel caso discreto, con una densità $f$ (non negativa, di integrale 1) nel caso continuo, e in ogni caso con la funzione di ripartizione $F_X(x) = P[X \le x]$, crescente, continua a destra, con $F_X' = f$ dove $f$ è continua. La legge di $Y = \phi(X)$ si trova sommando le probabilità dei valori con la stessa immagine nel caso discreto, e passando per $F_Y$ e derivando nel caso con densità.

## Formulario

Regole del calcolo delle probabilità, combinatoria e variabili aleatorie, con i termini per l'orale.

### Regole

$$P(\bar E) = 1 - P(E), \quad P(E \cup F) = P(E) + P(F) - P(E \cap F), \quad P(F \mid E) = \frac{P(E \cap F)}{P(E)}, \quad P(E \cap F) = P(E)\,P(F \mid E).$$

$$P(F) = \sum_i P(F \mid E_i)P(E_i), \qquad P(E_k \mid F) = \frac{P(F \mid E_k)P(E_k)}{\sum_i P(F \mid E_i)P(E_i)} \qquad (E_i \text{ partizione}).$$

Indipendenza: $P(E \cap F) = P(E)P(F)$; per tre eventi servono anche le coppie.

### Combinatoria

| Conteggio | Formula |
|---|---|
| Disposizioni con ripetizione | $n^k$ |
| Disposizioni semplici | $\frac{n!}{(n - k)!}$ |
| Permutazioni | $n!$ |
| Combinazioni | $\binom{n}{k}$ |
| Ipergeometrica | $\frac{\binom{K}{k}\binom{N - K}{n - k}}{\binom{N}{n}}$ |

### Variabili aleatorie

- Discreta: $p(x) = P(X = x)$, $\sum p(x) = 1$. Con densità: $f \ge 0$, $\int f = 1$, $P(a \le X \le b) = \int_a^b f$.
- Ripartizione: $F(x) = P(X \le x)$, crescente, continua a destra, da 0 a 1; $f = F'$ dove $F$ è derivabile.
- Trasformazioni: si calcola $F_Y(y) = P(g(X) \le y)$ e si deriva; se $g$ è monotona, $f_Y(y) = f_X(g^{-1}(y))\,\lvert(g^{-1})'(y)\rvert$.

### Termini per l'orale

| Termine | In una riga |
|---|---|
| Spazio campionario | insieme dei risultati possibili dell'esperimento |
| Evento | sottoinsieme dello spazio campionario |
| Probabilità classica, frequentista, assiomatica | casi favorevoli su possibili; limite delle frequenze; funzione che rispetta gli assiomi di Kolmogorov |
| Eventi incompatibili / indipendenti | intersezione vuota / probabilità dell'intersezione uguale al prodotto |
| Partizione | eventi incompatibili la cui unione è tutto lo spazio |
| Probabilità a priori / a posteriori | prima e dopo l'osservazione, nella formula di Bayes |
| Variabile aleatoria | funzione che associa un numero a ogni risultato |
| Funzione di ripartizione | $F(x) = P(X \le x)$ |

### Domande che tornano spesso

- Gli assiomi della probabilità e le conseguenze ($P(\bar E)$, unione di due eventi).
- Definire la probabilità condizionata e dimostrare la formula delle probabilità totali e quella di Bayes.
- Eventi incompatibili e indipendenti: che differenza c'è?
- Proprietà della funzione di ripartizione; legame con la densità.
- Come si trova la legge di $Y = g(X)$, anche per $g$ non monotona?
