---

## corso: Teoria dei Sistemi lezione: 5 data: 2026-10-06 argomenti: [espansione in fratti semplici, errori tipici nell'espansione, numero di fratti e di funzioni, poli e limitatezza di funzioni composte, esercizio con divisione e poli immaginari, metodo dei residui, poli semplici, poli multipli] fonti: [trascrizione parte 1, appunti manuali, dispensa del docente (italiano), dispensa del docente (inglese)] tags: [teoria-dei-sistemi, lezione]
---
# Lezione 5 — Fratti semplici, interpretazione e metodo dei residui

Come nelle lezioni precedenti, ampi tratti della registrazione coincidono con il tempo lasciato agli studenti per gli esercizi e contengono solo rumore o conversazioni, esclusi da questi appunti.

La lezione ha tre parti:

1. un riepilogo dell'espansione in fratti semplici, con gli errori da non commettere;
2. un esercizio completo, che il docente usa per mostrare come si «legge» un'antitrasformata prima ancora di calcolarla;
3. il **metodo dei residui**, che permette di calcolare i coefficienti dell'espansione senza risolvere grandi sistemi lineari.

## 1. Riepilogo: che cosa vuol dire espandere in fratti semplici

### 1.1 Il principio, e il modo in cui lo si fraintende

Una trasformata di Laplace che sia un rapporto di polinomi si può spezzare nella somma di tante frazioni più semplici, i **fratti semplici**. Ciascuno ha un proprio coefficiente moltiplicativo, e riportando tutto al minimo comune multiplo si deve ritrovare esattamente la frazione di partenza.

Il docente avverte che, se ci si limita a questa descrizione, si può essere indotti in errore. Dire «trovo una somma di frazioni che, rimesse insieme, danno lo stesso denominatore» dimentica un'informazione fondamentale: nell'espansione bisogna mettere **tutte** le frazioni che servono, senza dimenticarne nessuna (vedi [[Lezione 04 - Antitrasformata di Laplace e fratti semplici#6.3 Quali fratti mettere, e quanti|lezione 4, §6.3]]).

### 1.2 Tre errori da evitare

Il docente riprende una frazione della lezione precedente e ne ricava tre avvertenze.

> [!example] $\dfrac{s}{(s+1)^2}$ non è un fratto semplice Il denominatore appartiene alla classe della tabella: è $(s-a)^{k+1}$ con $a=-1$ e $k=1$. Il numeratore, però, non è un numero ma $s$. Se si va a cercare in tabella non si trova nulla: **non è un fratto semplice**, e va quindi decomposto. Ciascun pezzo deve appartenere alla tabella, moltiplicato per un coefficiente: $$\frac{s}{(s+1)^2} = \frac{A}{s+1} + \frac{B}{(s+1)^2} = \frac{A(s+1) + B}{(s+1)^2} .$$ Il primo fratto corrisponde a $a=-1$, $k=0$; il secondo a $a=-1$, $k=1$. Identificando i numeratori, $A = 1$ e $A + B = 0$, quindi $B = -1$: $$\frac{s}{(s+1)^2} = \frac{1}{s+1} - \frac{1}{(s+1)^2} \qquad\Longrightarrow\qquad f(t) = e^{-t} - t,e^{-t}.$$ Nella registrazione il calcolo dei coefficienti non si sente; è stato completato e verificato in questi appunti.

Le altre due avvertenze riguardano ciò che **non** si può aggiungere all'espansione.

- **Non si possono inventare denominatori.** A una somma come quella sopra non si può aggiungere, ad esempio, una frazione con denominatore $s^4+7$. Riducendo allo stesso denominatore comparirebbe un fattore $s^4+7$ che nella frazione di partenza non c'è. I denominatori dell'espansione devono essere tutti fattori del denominatore di partenza.
- **Le frazioni devono essere diverse tra loro.** Uno studente propone di aggiungere un'altra frazione con denominatore $s+1$. È corretta come forma, ma $\frac{A}{s+1}$ e $\frac{C}{s+1}$ sono la **stessa frazione**: insieme danno $\frac{A+C}{s+1}$, cioè un unico coefficiente. Se fossero ammesse frazioni ripetute se ne potrebbe mettere «un milione», tutte uguali, e il problema non avrebbe più una soluzione unica.

### 1.3 La procedura, e il legame tra fratti e funzioni

Il principio generale con cui si opera è quello della lezione 4.

1. Se il numeratore non è di grado inferiore al denominatore, prima si fa la **divisione**. Si ottiene una somma di termini senza denominatore (impulsi) più una frazione con il numeratore di grado inferiore.
2. Si lascia perdere il numeratore, «che sarà quello che è», e si **fattorizza il denominatore**, individuandone i poli e la loro molteplicità.
3. Si scrive l'espansione: gruppi di frazioni, ciascun gruppo relativo a un polo.

Il docente aggiunge un'osservazione che dà senso al conteggio. A ogni fratto semplice corrisponde, leggendo la tabella, **una funzione** nell'antitrasformata. Se si mettono $57$ frazioni ci sono $57$ funzioni nell'antitrasformata. Il numero di frazioni da mettere, e quindi di funzioni, è pari al **grado del denominatore**: con un denominatore di grado $7$ ci vogliono $7$ frazioni.

> [!example] Un denominatore di grado 6 Si consideri un denominatore formato da un fattore di primo grado, un fattore di primo grado al cubo e uno al quadrato, ad esempio $(s+1)(s+2)^3(s+3)^2$. Il grado è $1 + 3 + 2 = 6$, quindi servono sei frazioni: $$\frac{A}{s+1} + \frac{B}{s+2} + \frac{C}{(s+2)^2} + \frac{D}{(s+2)^3} + \frac{E}{s+3} + \frac{F}{(s+3)^2}.$$ Ogni frazione si traduce in una funzione. Ad esempio, $\frac{D}{(s+2)^3}$ ha $a=-2$ e $k=2$, e nell'antitrasformata diventa $D,\frac{t^2}{2},e^{-2t}$. Complessivamente l'antitrasformata contiene $$e^{-t},\quad e^{-2t},\quad t,e^{-2t},\quad \tfrac{t^2}{2}e^{-2t},\quad e^{-3t},\quad t,e^{-3t},$$ ciascuna con il proprio coefficiente. I coefficienti «saranno quello che dovranno essere»: per conoscerli bisogna fare i conti, per sapere quali funzioni ci sono no.
> 
> Nella registrazione si sentono chiaramente i gradi dei tre fattori e alcune delle frazioni scritte alla lavagna; le radici $-1$, $-2$, $-3$ sono ricostruite da queste ultime.

## 2. Dai poli alle proprietà di una funzione composta

### 2.1 Estendere il legame poli–andamento

Il legame tra poli e andamento nel tempo era stato stabilito per le singole funzioni della tabella (lezione 3). Con l'espansione in fratti semplici diventa evidente che vale anche per le funzioni **composte**. Ogni fratto corrisponde a un polo e a una funzione della tabella, e l'antitrasformata è la somma di quelle funzioni.

- Se fattorizzando il denominatore si trovano radici con **parte reale positiva**, nell'antitrasformata ci saranno sicuramente funzioni che divergono. A quei fratti corrispondono funzioni con $a>0$, esponenziali reali crescenti o oscillazioni dentro un inviluppo che si allarga. L'antitrasformata **non può essere limitata**.
- Se tutte le radici hanno **parte reale negativa**, l'antitrasformata è composta solo da funzioni che tendono a zero, perché l'esponenziale decrescente prima o poi prevale su qualunque potenza del tempo. È **limitata e tende a zero**.

### 2.2 La regola riassuntiva

> [!important] Poli e andamento dell'antitrasformata 
> Data una trasformata di Laplace razionale, si calcolano i suoi poli.
> 
> 1. Se **tutti** i poli hanno parte reale negativa, l'antitrasformata è limitata e tende a zero per $t\to\infty$.
> 2. Se esiste **almeno un** polo a parte reale positiva, e/o almeno un polo a parte reale nulla con molteplicità maggiore di $1$, l'antitrasformata **non è limitata**.
> 3. Se ci sono poli a parte reale negativa, «tutti quelli che volete», ed eventualmente poli a parte reale nulla, ma solo di molteplicità unitaria, l'antitrasformata è **limitata**.
> 
> Il terzo caso, osserva il docente, è semplicemente il **complemento** dei primi due: tutto ciò che non rientra negli altri due casi.

Il docente sceglie le parole con cura: dice «non è limitata» e non «diverge a più o meno infinito». Se nell'antitrasformata ci sono seni e coseni, ad esempio $t\sin t$, la funzione non tende né a $+\infty$ né a $-\infty$. Oscilla diventando, in modulo, sempre più grande, e basta. «Non limitata» è l'espressione corretta in tutti i casi.

Come già osservato nelle lezioni 3 e 4, queste affermazioni riguardano la parte dell'antitrasformata priva di impulsi: un eventuale impulso, che proviene dalla divisione, non sta in nessun «tubo».

## 3. Esercizio in aula — leggere un'antitrasformata prima di calcolarla

### 3.1 La domanda d'esame

Il docente propone un esercizio da svolgere in aula, precisando che a lezione serve anche «farsi un po' male» con i conti. All'esame, però, non chiederebbe di calcolare l'antitrasformata, se non come ultima risorsa per decidere se far proseguire l'esame. Chiederebbe invece di **dire che funzioni ci sono**: basta il tempo di guardare la trasformata.

> [!example] Esercizio: $F(s) = \dfrac{s^4}{(s+1)(s+2)(s^2+4)}$ **Lettura della trasformata.** Il docente anticipa una cosa che può sembrare in contraddizione con quanto detto finora: le frazioni da mettere nell'espansione sono **quattro**, ma le funzioni nell'antitrasformata sono **cinque**. Il motivo è che numeratore e denominatore hanno lo stesso grado ($4$). Prima si deve fare la divisione, e il quoziente, qui un numero, corrisponde a una funzione che non fa parte delle quattro: un **impulso**. Solo nel resto della divisione servono le quattro frazioni legate ai poli $-1$, $-2$ e $\pm2j$: $$\delta(t),\quad e^{-t},\quad e^{-2t},\quad \sin 2t,\quad \cos 2t .$$
> 
> **Divisione.** Per dividere bisogna fare il contrario di ciò che serve per i fratti semplici: moltiplicare i fattori del denominatore fino a ottenere un polinomio. $$(s+1)(s+2)(s^2+4) = (s^2+3s+2)(s^2+4) = s^4 + 3s^3 + 6s^2 + 12s + 8 .$$ Il quoziente è $1$ e il resto è $s^4 - (s^4 + 3s^3 + 6s^2 + 12s + 8) = -(3s^3 + 6s^2 + 12s + 8)$, quindi $$F(s) = 1 - \frac{3s^3 + 6s^2 + 12s + 8}{(s+1)(s+2)(s^2+4)} .$$ Il termine $1$ è l'impulso di ordine zero ($s^k$ con $k=0$).
> 
> **Impostazione del sistema.** Agli studenti è stato chiesto di impostare il sistema senza necessariamente risolverlo. Per la coppia $\pm2j$ si usa la forma della tabella con $\omega = 2$, cioè $\frac{2}{s^2+4}$ per il seno e $\frac{s}{s^2+4}$ per il coseno: $$\frac{3s^3 + 6s^2 + 12s + 8}{(s+1)(s+2)(s^2+4)} = \frac{A}{s+1} + \frac{B}{s+2} + C,\frac{2}{s^2+4} + D,\frac{s}{s^2+4} .$$ Riducendo allo stesso denominatore, il numeratore è $$A(s+2)(s^2+4) + B(s+1)(s^2+4) + 2C(s+1)(s+2) + D,s(s+1)(s+2),$$ e raccogliendo le potenze di $s$ si identifica con $3s^3 + 6s^2 + 12s + 8$: $$\begin{cases} A + B + D = 3 & (s^3)\ 2A + B + 2C + 3D = 6 & (s^2)\ 4A + 4B + 6C + 2D = 12 & (s^1)\ 8A + 4B + 4C = 8 & (s^0) \end{cases}$$
> 
> **Soluzione** (non svolta a lezione, verificata con il calcolo simbolico): $$A = -\frac{1}{5}, \qquad B = 2, \qquad C = \frac{2}{5}, \qquad D = \frac{6}{5} .$$ Ricordando il segno meno davanti alla frazione: $$f(t) = \delta(t) + \frac{1}{5},e^{-t} - 2,e^{-2t} - \frac{2}{5}\sin 2t - \frac{6}{5}\cos 2t .$$

### 3.2 Che cosa si poteva dire senza fare i conti

Tornando alla domanda iniziale, che cosa si poteva dire dell'andamento della funzione guardando soltanto la trasformata?

- C'è un **impulso**, perché il grado del numeratore è uguale a quello del denominatore e la divisione dà una costante.
- I poli sono $-1$ e $-2$, reali negativi, e la coppia $\pm2j$, sull'asse immaginario con molteplicità $1$.
- Non ci sono poli a parte reale positiva né poli a parte reale nulla multipli: la funzione (a parte l'impulso) è **limitata**.
- **Non può tendere a zero**, perché ci sono poli sull'asse immaginario. Un polo nell'origine darebbe una costante; una coppia $\pm j\omega$ dà una sinusoide che resta per sempre.

Il docente propone anche una variante. Se il fattore fosse stato $(s^2+4)^2$, le frazioni sarebbero state sei e non quattro: alle due precedenti si aggiungerebbero quelle con $(s^2+4)^2$ al denominatore, cioè i termini $t\sin 2t$ e $t\cos 2t$. I poli $\pm2j$ avrebbero molteplicità $2$, poli a parte reale nulla con molteplicità maggiore di $1$, e la funzione **non** sarebbe stata limitata.

> [!warning] Nota personale «Antitrasformata di Laplace - Esercizi» 
> L'impostazione e il sistema riportati nella nota sono corretti. Tre precisazioni:
> 
> - la conclusione «funzione limitata» è giustificata con «nessun polo con parte reale positiva». Questo non basta: serve anche che i poli sull'asse immaginario siano **semplici**, come è qui. Con $(s^2+4)^2$ la conclusione sarebbe falsa;
> - la limitatezza riguarda la parte senza impulsi: l'antitrasformata contiene anche $\delta(t)$;
> - nella riga dell'antitrasformata gli esponenziali sono scritti `e{^-t}` e `e{^-2t}`, che in LaTeX non producono $e^{-t}$ ed $e^{-2t}$. Inoltre in quella riga manca il segno meno che, nella riga precedente, precede la frazione.

## 4. Il metodo dei residui

### 4.1 Il problema

Il docente pone una domanda provocatoria. Si consideri

$$F(s) = \frac{1}{(s+1)(s+2)\cdots(s+100)} .$$

Il denominatore ha grado $100$, con cento poli reali semplici. Quali funzioni ci sono nell'antitrasformata? Lo si sa subito: $e^{-t}, e^{-2t}, \dots, e^{-100t}$, una per frazione. Per conoscerne i coefficienti, però, con il metodo visto finora bisognerebbe risolvere un sistema di $100$ equazioni in $100$ incognite.

Esistono metodi per evitarlo, almeno in casi speciali come questo. Quello che il docente presenta è il metodo che di solito insegnano i matematici. Il docente precisa però che nel corso non si è «teorici della trasformata di Laplace»: la si usa. Alla fine fornirà un insieme di metodi per trovare i pezzi dell'antitrasformata, e, «come tutti gli ingegneri che si rispettano», bisognerà scegliere di volta in volta quello che porta al risultato giusto nel minor tempo. Se un metodo dà il risultato in cento anni e un altro in un secondo, è meglio il secondo. Molti studenti tendono a usare questo metodo sempre, anche quando è più complicato delle alternative.

### 4.2 L'espansione «dei matematici»

Si fattorizza il denominatore mettendo in evidenza i poli distinti e la loro molteplicità:

$$F(s) = \frac{N(s)}{(s-p_1)^{\mu_1}(s-p_2)^{\mu_2}\cdots(s-p_{n_d})^{\mu_{n_d}}}, \qquad p_i\in\mathbb{C} .$$

Qui $n_d$ è il numero di poli **distinti** e $\mu_i$ la molteplicità di $p_i$. Un polinomio a coefficienti reali di grado $32$ ha nel campo complesso $32$ radici, contate con la molteplicità, e lo si può fattorizzare mettendo in evidenza quante sono distinte e quante volte si ripete ciascuna. I $p_i$ sono liberi di essere numeri complessi.

A differenza dei fratti semplici «del corso», che usano le forme reali della tabella, qui si usano le **frazioni parziali** generali: numeri divisi per $(s-p)$ elevato a una potenza, con $p$ anche complesso.

$$F(s) = \sum_{i=1}^{n_d}\sum_{k=1}^{\mu_i}\frac{c_{i,k}}{(s-p_i)^k} .$$

Il secondo indice $k$ coincide sempre con l'esponente del denominatore. Per una coppia di poli complessi semplici, ad esempio $\pm2j$, compaiono due frazioni $\frac{c_1}{s-2j} + \frac{c_2}{s+2j}$, ciascuna con $k=1$ soltanto. È la stessa idea della lezione 4: si mettono tutte le frazioni necessarie, ma nella forma «matematica».

### 4.3 Il coefficiente di grado massimo

Si isolano dalla doppia sommatoria i termini relativi al primo polo, che è un polo qualunque:

$$F(s) = \frac{c_{1,1}}{s-p_1} + \frac{c_{1,2}}{(s-p_1)^2} + \dots + \frac{c_{1,\mu_1}}{(s-p_1)^{\mu_1}} + \sum_{i=2}^{n_d}\sum_{k=1}^{\mu_i}\frac{c_{i,k}}{(s-p_i)^k} .$$

Si moltiplicano entrambi i membri per $(s-p_1)^{\mu_1}$. In ciascun termine del primo gruppo si cancellano tanti fattori $(s-p_1)$ quanti ce ne sono al denominatore, fino all'ultimo, in cui si cancellano tutti e rimane solo il coefficiente:

$$(s-p_1)^{\mu_1}F(s) = c_{1,1}(s-p_1)^{\mu_1-1} + c_{1,2}(s-p_1)^{\mu_1-2} + \dots + c_{1,\mu_1} + (s-p_1)^{\mu_1}\sum_{i=2}^{n_d}\sum_{k=1}^{\mu_i}\frac{c_{i,k}}{(s-p_i)^k} .$$

Si fa ora tendere $s$ a $p_1$. Tutti i termini che contengono $(s-p_1)$ elevato a una potenza positiva si annullano. Questo vale anche per l'ultima sommatoria, che non ha poli in $p_1$ perché gli altri poli sono diversi. Resta solo il coefficiente di grado massimo:

$$c_{1,\mu_1} = \lim_{s\to p_1},(s-p_1)^{\mu_1}F(s) .$$

Uno dei coefficienti dell'espansione si trova quindi con un limite, «senza dover risolvere mille per mille equazioni».

### 4.4 Gli altri coefficienti: la formula generale

Per trovare gli altri coefficienti dello stesso polo si deriva. Derivando una volta rispetto a $s$ l'espressione $(s-p_1)^{\mu_1}F(s)$, il termine costante $c_{1,\mu_1}$ sparisce e il penultimo, $c_{1,\mu_1-1}(s-p_1)$, diventa la costante $c_{1,\mu_1-1}$. Tutti i termini in cui $(s-p_1)$ compare ancora elevato a una potenza positiva si annullano nel limite $s\to p_1$. Derivando due volte si trova il coefficiente precedente (diviso per $2!$), e così via. Ogni derivazione «abbassa di un grado» tutto ciò che era rimasto e porta giù gli esponenti come fattori.

> [!important] Formula dei residui (dispensa italiana, Equazione 3, p. 29) $$c_{i,k} = \lim_{s\to p_i}\ \frac{1}{(\mu_i-k)!},\frac{d^{,\mu_i-k}}{ds^{,\mu_i-k}}\Big[(s-p_i)^{\mu_i}F(s)\Big], \qquad k = 1,\dots,\mu_i .$$ Per un **polo semplice** ($\mu_i = 1$) c'è un solo coefficiente e la formula si riduce a un limite senza derivate: $$c_i = \lim_{s\to p_i},(s-p_i),F(s) .$$

Il docente ammette che la formula generale «non è proprio la più bella cosa che uno possa vedere», né la più comoda da usare: «a nessuno viene in mente di usarla, se non per dimostrare qualcosa». Diventa invece semplicissima quando il polo è semplice, perché non ci sono derivate da fare. La dispensa italiana chiama **residui del polo** tutti i coefficienti $c_{i,k}$ (p. 28).

> [!example] Un polo doppio (dispensa italiana, Esempio PM 14, p. 29) $$F(s) = \frac{1}{s^2(s+3)} = \frac{A}{s} + \frac{B}{s^2} + \frac{C}{s+3}.$$
> 
> - Polo semplice $-3$: $C = \lim_{s\to-3}(s+3)F(s) = \lim_{s\to-3}\frac{1}{s^2} = \frac{1}{9}$.
> - Polo doppio $0$, coefficiente di grado massimo: $B = \lim_{s\to0}s^2F(s) = \lim_{s\to0}\frac{1}{s+3} = \frac{1}{3}$.
> - Polo doppio $0$, coefficiente successivo, con una derivata: $A = \lim_{s\to0}\frac{d}{ds}\frac{1}{s+3} = \lim_{s\to0}\left(-\frac{1}{(s+3)^2}\right) = -\frac{1}{9}$.
> 
> Quindi $f(t) = -\frac{1}{9} + \frac{1}{3},t + \frac{1}{9},e^{-3t}$ per $t \ge 0$.

### 4.5 Quando conviene usarlo

Il docente conclude con un'indicazione pratica. Il metodo dei residui ha un **senso pratico soprattutto nel caso di poli reali semplici**:

- se il polo è semplice non ci sono derivate da calcolare;
- se il polo è reale, il residuo è un numero reale ed è **direttamente il coefficiente** della funzione esponenziale nell'antitrasformata della funzione reale.

Per i poli complessi, invece, il metodo dà coefficienti complessi, che vanno poi ricombinati per ottenere seni e coseni. La dispensa in inglese lo dice esplicitamente (p. 17): questo metodo, «anche se elegante», si usa per i coefficienti dei poli reali, mentre per i poli complessi si ricorre all'identificazione dei polinomi. Nella lezione 6 il docente farà un'eccezione per una coppia di poli immaginari semplici. Si può anche **combinare** i due metodi: calcolare con i residui i coefficienti dei poli reali semplici e usarli per ridurre il numero di incognite del sistema di identificazione (dispensa inglese, esempio E/2.2/4).

> [!tip] Approfondimento: residui e metodo di Heaviside #approfondimento
> 
> - **Il nome.** In analisi complessa il **residuo** di una funzione in un polo $p$ è, in senso stretto, il coefficiente di $\frac{1}{s-p}$ nello sviluppo in serie di Laurent attorno a $p$, cioè il nostro $c_{i,1}$. Per un polo di ordine $m$ vale $c_{i,1} = \frac{1}{(m-1)!}\lim_{s\to p}\frac{d^{m-1}}{ds^{m-1}}\big[(s-p)^mF(s)\big]$, che è la formula precedente con $k=1$ [@mathworld_residue]. La dispensa usa il termine in senso più ampio, per tutti i coefficienti $c_{i,k}$.
> - **Il trucco della copertura.** La formula per i poli semplici è nota nei testi anglosassoni come _cover-up method_, ed è attribuita a Oliver Heaviside. Per calcolare il coefficiente di $\frac{1}{s-p}$ si «copre» con un dito il fattore $(s-p)$ nella frazione di partenza e si sostituisce $s=p$ in ciò che resta. Con le radici ripetute il trucco dà solo il coefficiente della potenza più alta, esattamente come il limite del §4.3 [@miller_orloff_coverup].

### 4.6 Esercizio proposto

> [!example] $F(s) = \dfrac{1}{(s+1)(s+2)(s+3)(s+4)}$ L'antitrasformata contiene quattro funzioni: $e^{-t}$, $e^{-2t}$, $e^{-3t}$, $e^{-4t}$. Il docente chiede di:
> 
> 1. calcolare i coefficienti con il metodo dei residui;
> 2. impostare il sistema $4\times4$ con il «metodo lungo», cioè l'identificazione dei polinomi, **senza risolverlo**;
> 3. sostituire nel sistema i valori trovati con i residui e verificare che lo soddisfano.
> 
> **Residui.** Ciascun polo è semplice, quindi basta coprire il fattore corrispondente e sostituire: $$A = \lim_{s\to-1}\frac{1}{(s+2)(s+3)(s+4)} = \frac{1}{(1)(2)(3)} = \frac{1}{6}, \qquad B = \lim_{s\to-2}\frac{1}{(s+1)(s+3)(s+4)} = \frac{1}{(-1)(1)(2)} = -\frac{1}{2},$$ $$C = \lim_{s\to-3}\frac{1}{(s+1)(s+2)(s+4)} = \frac{1}{(-2)(-1)(1)} = \frac{1}{2}, \qquad D = \lim_{s\to-4}\frac{1}{(s+1)(s+2)(s+3)} = \frac{1}{(-3)(-2)(-1)} = -\frac{1}{6}.$$
> 
> **Sistema di identificazione.** Il numeratore comune è $A(s+2)(s+3)(s+4) + B(s+1)(s+3)(s+4) + C(s+1)(s+2)(s+4) + D(s+1)(s+2)(s+3)$, e deve essere uguale a $1$: $$\begin{cases} A + B + C + D = 0 & (s^3)\ 9A + 8B + 7C + 6D = 0 & (s^2)\ 26A + 19B + 14C + 11D = 0 & (s^1)\ 24A + 12B + 8C + 6D = 1 & (s^0) \end{cases}$$ Sostituendo i residui, ad esempio nella prima e nell'ultima equazione: $\frac{1}{6} - \frac{1}{2} + \frac{1}{2} - \frac{1}{6} = 0$ e $4 - 6 + 4 - 1 = 1$. Le altre due si verificano allo stesso modo.
> 
> $$f(t) = \frac{1}{6},e^{-t} - \frac{1}{2},e^{-2t} + \frac{1}{2},e^{-3t} - \frac{1}{6},e^{-4t}.$$
> 
> Nella registrazione l'elenco delle funzioni dettato dal docente salta $e^{-3t}$; le funzioni sono quattro, una per polo.

> [!warning] Nota personale «Antitrasformata di Laplace»: refusi negli indici I valori di $A$, $B$, $C$, $D$ nella nota sono corretti, ma le formule contengono alcuni refusi di copiatura:
> 
> - la formula generale è scritta $C_1 = \lim_{s\to-p_1}(s-p_1)F(s)$: il limite va fatto per $s\to p_1$, non $s\to-p_1$;
> - nelle righe di $B$, $C$, $D$ restano $(s-p_1)$ e $s\to-1$ copiati dalla riga di $A$, invece di $(s+2)$ e $s\to-2$, e così via;
> - nella riga di $D$ il denominatore rimasto deve essere $(s+1)(s+2)(s+3)$, non $(s+1)(s+2)(s+4)$, anche se il valore calcolato, $\frac{1}{(-3)(-2)(-1)}$, è giusto;
> - nella moltiplicazione per $(s-p_1)^{k_1}$, l'esponente del primo termine deve essere $k_1 - 1$, non $k_{i-1}$;
> - nella riga $F(s) = \frac{}{(s+1)(s+2)\ldots(s+100)}$ il numeratore è vuoto: va scritto $1$.

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. _Perché $\frac{s}{(s+1)^2}$ non è un fratto semplice, anche se il denominatore è in tabella?_ Perché in tabella il numeratore di $\frac{1}{(s-a)^{k+1}}$ è una costante. Con $s$ al numeratore l'antitrasformata non si legge direttamente: va spezzata in $\frac{A}{s+1} + \frac{B}{(s+1)^2}$.
2. _Perché nell'espansione non si possono mettere due frazioni con lo stesso denominatore?_ Sarebbero la stessa frazione con coefficiente somma: i coefficienti non sarebbero più determinati in modo unico.
3. _Perché le funzioni nell'antitrasformata di $\frac{s^4}{(s+1)(s+2)(s^2+4)}$ sono cinque, se le frazioni sono quattro?_ Numeratore e denominatore hanno lo stesso grado: la divisione dà una costante, cioè un impulso, che si aggiunge alle quattro funzioni delle frazioni.
4. _Perché quella funzione è limitata ma non tende a zero?_ I poli $-1$ e $-2$ danno termini che si smorzano; i poli $\pm2j$, semplici, danno una sinusoide che resta per sempre, limitata ma senza limite.
5. _Perché moltiplicando per $(s-p_1)^{\mu_1}$ e facendo il limite si ottiene proprio $c_{1,\mu_1}$?_ Tutti gli altri termini del gruppo di $p_1$ contengono ancora $(s-p_1)$ a una potenza positiva. I termini degli altri poli sono moltiplicati per $(s-p_1)^{\mu_1}$ e non hanno poli in $p_1$. Nel limite si annullano tutti, tranne la costante $c_{1,\mu_1}$.
6. _Perché il metodo dei residui è comodo soprattutto per i poli reali semplici?_ Non richiede derivate e restituisce direttamente il coefficiente reale dell'esponenziale. Con poli complessi i coefficienti sono complessi e vanno ricombinati.
7. _Perché è più corretto dire «non limitata» che «diverge a infinito»?_ Termini come $t\sin t$ crescono in modulo oscillando, senza tendere né a $+\infty$ né a $-\infty$.