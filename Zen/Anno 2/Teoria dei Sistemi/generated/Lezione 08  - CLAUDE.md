---
corso: Teoria dei Sistemi
lezione: 8
data: 2026-10-25
argomenti: [equazioni differenziali lineari a coefficienti costanti, trasformata delle derivate di ordine n, sistemi causali, sistemi propri e strettamente propri, risposta nello stato zero, risposta a ingresso nullo, stato, funzione di trasferimento, risposta all'impulso, sistema massa-molla, risonanza, impulso rettangolare]
fonti: [trascrizione parte 1, appunti manuali, dispensa del docente (italiano), dispensa del docente (inglese)]
tags: [teoria-dei-sistemi, lezione]
---

# Lezione 8 — Equazioni differenziali, funzione di trasferimento e risposte

Questa nota ricostruisce l'ottava lezione. Le fonti sono:

- la trascrizione della registrazione (parte 1);
- le note personali «Equazioni differenziali» e «Lezione 8 - handwritten»;
- la dispensa italiana del docente (cap. 1, «Risoluzione di equazioni differenziali», pp. 29 e seguenti);
- la dispensa in inglese (cap. 3, *Linear Systems with Input/Output Representation*, e l'appendice A sulle equazioni differenziali lineari).

Finita la «cassetta degli attrezzi» sulla trasformata di Laplace, la lezione la usa per il suo scopo principale: risolvere le equazioni differenziali lineari a coefficienti costanti che descrivono i sistemi dinamici. Ne escono alcuni dei concetti centrali del corso:

- la scomposizione della soluzione in **risposta nello stato zero** e **risposta a ingresso nullo**;
- la nozione di **stato**;
- la **funzione di trasferimento** e la **risposta all'impulso**;
- con l'esempio massa-molla, il fenomeno della **risonanza**.

## 1. L'equazione differenziale di un sistema

### 1.1 La forma generale

In analisi si sono studiate equazioni differenziali lineari a coefficienti costanti con a destra una funzione nota, una $f(t)$ o $f(x)$. In teoria dei sistemi a destra c'è qualcosa di più ricco: una combinazione della funzione di **ingresso** $u(t)$ e delle sue derivate. L'ingresso rappresenta le cause esterne del disegno del primo giorno ([[Lezione 01 - Sistemi dinamici e funzioni generalizzate|lezione 1]]). Le cause esterne influiscono sul comportamento del sistema non solo attraverso il loro valore, ma anche attraverso la derivata prima, la seconda, e così via. È il modo più completo per rappresentare tutte le possibili dipendenze tra la causa e il comportamento che essa genera.

> [!important] Equazione ingresso-uscita
> $$y^{(n)}(t) + a_{n-1}\,y^{(n-1)}(t) + \dots + a_1\,\dot y(t) + a_0\,y(t) = b_m\,u^{(m)}(t) + \dots + b_1\,\dot u(t) + b_0\,u(t)$$
> - $y(t)$ è l'**uscita** e $u(t)$ l'**ingresso**, entrambe funzioni del tempo;
> - i coefficienti $a_i$ e $b_i$ sono **costanti**;
> - $y^{(n)}$ indica la derivata $n$-esima, **non** una potenza.

Conoscendo $u(t)$ si conoscono anche le sue derivate. Calcolando il secondo membro ci si riporta alla forma vista in analisi, e la si potrebbe risolvere con i metodi noti. La trasformata di Laplace offre però una strada più diretta.

### 1.2 Sistemi causali: perché $m \le n$

Per i **sistemi causali**, quelli in cui l'effetto non si realizza prima della causa, il grado di derivazione dell'uscita deve essere almeno pari a quello dell'ingresso: $m\le n$. Ne seguono due nomi, che si ritrovano nella trasformata (§3).

- **Strettamente proprio**: $m < n$. È il caso che si incontrerà «quasi sempre, non sempre, quasi sempre».
- **Proprio**: $m = n$.

> [!example] Perché $y = \dot u$ non è un sistema fisico
> Si consideri $y(t) = \dot u(t)$, con $n=0$ e $m=1$: l'uscita è la derivata dell'ingresso. Si immagini che l'ingresso sia stato una sinusoide fino a un certo istante $\bar t$. Per conoscere la derivata in $\bar t$ in senso analitico, il sistema dovrebbe conoscere il rapporto incrementale sia da sinistra **sia da destra**. Dovrebbe cioè sapere come continuerà l'ingresso dopo $\bar t$, che potrebbe fare «quello che vuole». La «scatoletta» che genera $y$ dovrebbe conoscere il futuro. In natura sistemi del genere non esistono. Esistono solo approssimazioni, che si rappresentano in un altro modo (ad esempio considerando la sola derivata sinistra).

## 2. Trasformare l'equazione

### 2.1 La trasformata delle derivate di ordine qualsiasi

L'equazione è un'uguaglianza tra funzioni, quindi le trasformate dei due membri devono essere uguali. La trasformata è un operatore lineare, quindi la trasformata di ciascun membro è la somma delle trasformate dei singoli pezzi.

Il docente raccomanda di rispettare la convenzione: lettere minuscole per le funzioni del tempo, maiuscole per le trasformate. In particolare **non** si deve scrivere qualcosa come $Y^{(n-1)}$: subito dopo non si saprebbe più di che cosa si sta parlando. Si scrive $\mathcal{L}\{y^{(n-1)}\}$, e l'unica sostituzione lecita è $\mathcal{L}\{y\} = Y(s)$.

Si applica poi ripetutamente la proprietà della derivata ([[Lezione 02 - Funzioni generalizzate e trasformata di Laplace|lezione 2]]), ogni volta sostituendo il risultato precedente:

$$\begin{aligned}
\mathcal{L}\{\dot y\} &= s\,Y(s) - y(0^-) ,\\
\mathcal{L}\{\ddot y\} &= s\,\mathcal{L}\{\dot y\} - \dot y(0^-) = s^2\,Y(s) - s\,y(0^-) - \dot y(0^-) ,\\
\mathcal{L}\{\dddot y\} &= s\,\mathcal{L}\{\ddot y\} - \ddot y(0^-) = s^3\,Y(s) - s^2\,y(0^-) - s\,\dot y(0^-) - \ddot y(0^-) .
\end{aligned}$$

Per induzione:

> [!important] Trasformata della derivata $n$-esima
> $$\mathcal{L}\{y^{(n)}\} = s^n\,Y(s) - \sum_{k=1}^{n} s^{\,n-k}\,y^{(k-1)}(0^-) .$$
> Il primo termine è $s$ elevato all'ordine della derivata, per $Y(s)$. Il secondo è un polinomio in $s$ di grado **$n-1$**, i cui coefficienti sono le **condizioni iniziali** $y(0^-), \dot y(0^-), \dots, y^{(n-1)}(0^-)$.

C'è una regola mnemonica. In ogni termine del polinomio, la potenza di $s$ più l'ordine di derivazione della condizione iniziale che la moltiplica fa sempre $n-1$. Per $n=3$: $s^2\,y$ ($2+0$), $s\,\dot y$ ($1+1$), $\ddot y$ ($0+2$). Con $y^{(12)}$ si avrebbe $s^{12}Y(s) - s^{11}y(0^-) - s^{10}\dot y(0^-) - \dots$

Questi polinomi sono **omogenei** nelle condizioni iniziali: se tutte le condizioni iniziali sono nulle, il polinomio è nullo. La stessa cosa vale per l'ingresso, con $U(s)$ al posto di $Y(s)$ e le condizioni iniziali $u^{(k)}(0^-)$.

### 2.2 Mettere tutto insieme

Il docente invita a fare il passo successivo «con la fantasia», come chi gioca a scacchi vede le mosse senza farle sulla scacchiera. Si sostituisce ogni trasformata nell'equazione e si raccolgono i termini. A sinistra, tutti i termini con $Y(s)$ si raccolgono in un unico polinomio in $s$; i termini con le condizioni iniziali dell'uscita formano un polinomio $P(s)$ di grado al più $n-1$. A destra succede lo stesso con l'ingresso, con un polinomio $Q(s)$ di grado al più $m-1$:

$$\underbrace{\big(s^n + a_{n-1}s^{n-1} + \dots + a_0\big)}_{D(s)}\,Y(s) - P(s) = \underbrace{\big(b_m s^m + \dots + b_0\big)}_{N(s)}\,U(s) - Q(s) .$$

Qui $P$ dipende da $y^{(k)}(0^-)$ per $k = 0,\dots,n-1$, e $Q$ da $u^{(k)}(0^-)$ per $k = 0,\dots,m-1$. La loro forma esatta non interessa: è riportata nella dispensa in inglese, ma ciò che conta è il grado e da che cosa dipendono i coefficienti.

È un'equazione **di primo grado** in $Y(s)$. Risolvendola:

> [!important] Soluzione nel dominio di $s$
> $$Y(s) = \underbrace{\frac{N(s)}{D(s)}\,U(s)}_{\text{risposta nello stato zero}} \;+\; \underbrace{\frac{Z(s)}{D(s)}}_{\text{risposta a ingresso nullo}}, \qquad Z(s) = P(s) - Q(s),$$
> dove $Z(s)$ è un polinomio di grado al più $n-1$ i cui coefficienti dipendono dalle condizioni iniziali di uscita e ingresso.

Se $u(t)$ è uno dei segnali considerati nel corso, $U(s)$ è un rapporto di polinomi. Allora $Y(s)$ è una **somma di rapporti di polinomi**, che si antitrasforma con i metodi delle lezioni 4–6. Per risolvere un'equazione differenziale lineare a coefficienti costanti basta quindi saper antitrasformare rapporti di polinomi, cioè, in ultima analisi, **saper trovare le radici di un polinomio**. Si è passati da un problema *funzionale*, in cui compaiono funzioni, a un problema *algebrico*. Inoltre, guardando i poli, si sa subito come sarà la soluzione, per il legame tra poli e andamento nel tempo.

## 3. Le due risposte, lo stato e la funzione di trasferimento

### 3.1 Risposta nello stato zero e risposta a ingresso nullo

La soluzione mostra la **linearità** del sistema. Nella [[Lezione 01 - Sistemi dinamici e funzioni generalizzate|lezione 1]] si erano distinte le **cause interne** e le **cause esterne**: in un sistema lineare ciascuna contribuisce per conto suo e l'effetto totale è la somma degli effetti. I due addendi di $Y(s)$ sono esattamente questi contributi, separati anche nel tempo dall'istante $0$.

- **Risposta a ingresso nullo**: il termine $Z(s)/D(s)$. È ciò che il sistema fa se da $0$ in avanti non si applica alcun ingresso. «Ingresso nullo» vuol dire che da zero in avanti non c'è nulla; prima di zero può esserci stato qualcosa, ma conta solo attraverso le condizioni iniziali.
- **Risposta nello stato zero**: il termine $\frac{N(s)}{D(s)}U(s)$. È la risposta del sistema all'ingresso applicato da $0$ in avanti, partendo da condizioni iniziali tutte nulle, cioè da una condizione di riposo.

### 3.2 Che cos'è lo stato

Il nome «stato zero» anticipa un concetto che il docente definisce fondamentale e che tornerà molte volte nel corso.

> [!important] Lo stato (idea intuitiva)
> Lo **stato** di un sistema in un istante è l'insieme delle informazioni che riassumono tutta la storia passata del sistema e che non dipendono da ciò che si farà da quell'istante in avanti.

«Lo stato del mondo adesso è quello che è»: è irrilevante che cosa sia successo dal Big Bang a oggi, e ci si potrebbe essere arrivati in un miliardo di modi. Le condizioni iniziali $y^{(k)}(0^-)$ e $u^{(k)}(0^-)$ raccolgono tutto ciò che è successo da $-\infty$ a $0^-$. Se fino a $0^-$ il sistema è rimasto a riposo, questi numeri sono tutti zero: lo **stato zero**, da cui il nome della risposta.

### 3.3 La funzione di trasferimento e la risposta all'impulso

> [!important] Funzione di trasferimento
> Il rapporto di polinomi
> $$T(s) = \frac{N(s)}{D(s)} = \frac{b_m s^m + \dots + b_1 s + b_0}{s^n + a_{n-1}s^{n-1} + \dots + a_0}$$
> si chiama **funzione di trasferimento** del sistema. Permette di calcolare la risposta nello stato zero a qualunque ingresso di cui si conosca la trasformata: $Y_{\text{stato zero}}(s) = T(s)\,U(s)$.

I nomi del §1.2 si applicano a $T(s)$. È **strettamente propria** se il grado del numeratore è minore di quello del denominatore ($m<n$), **propria** se è uguale ($m=n$). Per i sistemi con più ingressi e più uscite ci sarà una **matrice di trasferimento**, ogni elemento della quale è una funzione di trasferimento.

Si scelgano ora condizioni iniziali tutte nulle e, come ingresso, l'impulso $u(t) = \delta(t)$. Allora $Z(s) = 0$ e $U(s) = 1$, quindi

$$Y(s) = T(s) .$$

> [!important] Risposta all'impulso
> L'uscita di un sistema in stato zero sollecitato da un impulso si chiama **risposta all'impulso**, $h(t)$. Dal punto di vista di Laplace:
> $$T(s) = \mathcal{L}\{h(t)\} .$$
> La funzione di trasferimento è la trasformata di Laplace della risposta all'impulso.

## 4. Esempio: il sistema massa-molla

### 4.1 Il modello

Si consideri una massa $M$ appoggiata su un piano senza attrito, collegata a una parete fissa tramite una molla di costante elastica $K$ e tirata da una forza esterna $f(t)$. Sia $y(t)$ lo spostamento della massa dalla posizione di riposo della molla.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  \draw[very thick] (0,0) -- (0,1.8);
  \foreach \h in {0.1,0.4,...,1.7} \draw (0,\h) -- (-0.25,\h-0.25);
  \draw (0,0) -- (5.8,0);
  \draw[thick] (0,0.75) -- (0.4,0.75) -- (0.6,1.05) -- (0.9,0.45) -- (1.2,1.05) -- (1.5,0.45) -- (1.8,1.05) -- (2.1,0.45) -- (2.3,0.75) -- (2.7,0.75);
  \node at (1.45,1.35) {$K$};
  \draw[thick] (2.7,0) rectangle (4.1,1.5);
  \node at (3.4,0.75) {$M$};
  \draw[->,thick] (4.1,0.75) -- (5.3,0.75) node[right] {$f(t)$};
  \draw[dashed] (2.7,0) -- (2.7,-0.6);
  \draw[->] (2.7,-0.45) -- (3.9,-0.45) node[right] {$y(t)$};
\end{tikzpicture}
\end{document}
```

> [!tip] Rendering del disegno
> Il blocco `tikz` sopra viene disegnato in Obsidian dal plugin della community **TikZJax**; senza il plugin compare come codice. Il disegno usa solo comandi TikZ di base, per evitare librerie aggiuntive.

Per la seconda legge della dinamica, massa per accelerazione è uguale alla somma delle forze: la forza esterna $f$ e la forza elastica $-Ky$, che si oppone allo spostamento.

$$M\,\ddot y = -K\,y + f \qquad\Longrightarrow\qquad \ddot y + \frac{K}{M}\,y = \frac{1}{M}\,f .$$

È un'equazione della forma generale con $n=2$, $m=0$, $a_1 = 0$, $a_0 = \frac{K}{M}$, $b_0 = \frac{1}{M}$, e ingresso $u = f$. Conviene indicare $\omega_n = \sqrt{K/M}$, detta pulsazione naturale. Il docente la risolve direttamente con Laplace, invitando a confrontare il risultato con gli appunti di fisica:

$$s^2\,Y(s) - s\,y(0^-) - \dot y(0^-) + \frac{K}{M}\,Y(s) = \frac{1}{M}\,F(s)$$

$$Y(s) = \underbrace{\frac{1/M}{s^2 + \omega_n^2}}_{T(s)}\,F(s) + \frac{s\,y(0^-) + \dot y(0^-)}{s^2 + \omega_n^2} .$$

Per scrivere la soluzione qualcuno deve dire quali sono le condizioni iniziali e com'è fatta la forza.

### 4.2 Primo caso: una «ditata» a riposo

La massa è ferma a riposo, $y(0^-) = \dot y(0^-) = 0$, e riceve un colpo secco: una forza intensa che agisce per un tempo brevissimo, approssimata da un impulso, $f(t) = \delta(t)$. Quindi $F(s) = 1$ e resta solo la funzione di trasferimento:

$$Y(s) = \frac{1/M}{s^2+\omega_n^2} .$$

Per avere la forma del seno in tabella si moltiplica e si divide per $\omega_n$:

$$Y(s) = \frac{1}{M\,\omega_n}\cdot\frac{\omega_n}{s^2+\omega_n^2}, \qquad \frac{1}{M\,\omega_n} = \frac{1}{M\sqrt{K/M}} = \frac{1}{\sqrt{MK}},$$

$$y(t) = \frac{1}{\sqrt{MK}}\,\sin\!\Big(\sqrt{\tfrac{K}{M}}\;t\Big) .$$

È la risposta all'impulso del sistema, e si presta a considerazioni fisiche.

- Più la massa è **pesante**, meno si muove: l'ampiezza $\frac{1}{\sqrt{MK}}$ diminuisce. A parità di $K$, la pulsazione si abbassa.
- Più la molla è **rigida**, cioè $K$ grande, meno la massa si muove, perché la molla «è dura». La pulsazione invece aumenta: si muove poco ma più velocemente.

### 4.3 Secondo caso: spostare e lasciare andare

È il caso «duale». Non si applica alcuna forza, $f = 0$. La massa viene spostata di $\bar y$, tenuta ferma e poi lasciata: $y(0^-) = \bar y$, $\dot y(0^-) = 0$. Da quell'istante non agisce nessuna forza esterna; agisce solo il fatto che il sistema non era a riposo.

$$Y(s) = \frac{s\,\bar y}{s^2+\omega_n^2} \qquad\Longrightarrow\qquad y(t) = \bar y\,\cos\!\Big(\sqrt{\tfrac{K}{M}}\;t\Big) .$$

Viene un coseno e non un seno, e a pensarci è ovvio. Prima la massa partiva da zero, e il seno parte da zero. Ora parte dalla posizione $\bar y$, dove si trova il massimo dell'oscillazione, e il coseno parte dal massimo.

Il primo caso è una **risposta nello stato zero**: non era stato fatto niente prima, solo un colpo. Il secondo è una **risposta a ingresso nullo**: da quando si lascia la massa non c'è alcuna forza esterna. Se si fanno entrambe le cose, la risposta è la somma dei due contributi.

### 4.4 Terzo caso: la risonanza

L'ultimo caso, avverte il docente, verrà ripreso più avanti. Mette in relazione un fenomeno fisico notevole con quanto visto sulla limitatezza delle antitrasformate. Il sistema parte a riposo e la forza è una sinusoide **con la stessa pulsazione naturale** del sistema:

$$f(t) = \sin(\omega_n t), \qquad F(s) = \frac{\omega_n}{s^2+\omega_n^2} \qquad\Longrightarrow\qquad Y(s) = \frac{1}{M}\cdot\frac{\omega_n}{\big(s^2+\omega_n^2\big)^2} .$$

Che cosa fa $y(t)$? Basta guardare il denominatore. I poli sono le radici di $(s^2+\omega_n^2)^2$, un polinomio di grado $4$: ci sono quattro poli, ma nel piano di Gauss si possono disegnare solo **due** croci, perché $\pm j\omega_n$ compaiono ciascuno **due volte**. Sono poli a parte reale nulla con molteplicità maggiore di $1$, quindi l'antitrasformata **non è limitata**. Applicando alla massa una forza oscillante alla sua stessa pulsazione, l'oscillazione aumenta, aumenta, aumenta.

> [!example] Completamento: la soluzione esplicita (non svolta a lezione)
> Combinando le trasformate di $\sin\omega t$ e di $t\cos\omega t$ della tabella (lezione 2), cioè $\frac{\omega}{s^2+\omega^2}$ e $\frac{s^2-\omega^2}{(s^2+\omega^2)^2}$, si ricava
> $$\mathcal{L}^{-1}\left\{\frac{\omega}{(s^2+\omega^2)^2}\right\} = \frac{\sin\omega t - \omega t\cos\omega t}{2\omega^2},$$
> quindi, con $M\omega_n^2 = K$:
> $$y(t) = \frac{1}{2K}\Big(\sin\omega_n t - \omega_n t\cos\omega_n t\Big) .$$
> Il termine $\omega_n t\cos\omega_n t$ è una cosinusoide in un inviluppo che cresce **linearmente** nel tempo. Il grafico è per $K = M = 1$ ($\omega_n = 1$).

```chart
type: line
labels: [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]
series:
  - title: "y(t) in risonanza (K = M = 1)"
    data: [0, 0.02, 0.151, 0.446, 0.871, 1.301, 1.556, 1.463, 0.929, -0.014, -1.189, -2.302, -3.02, -3.066, -2.31, -0.831, 1.077, 2.958, 4.306, 4.699, 3.923, 2.057, -0.524, -3.217, -5.331, -6.269, -5.688, -3.614, -0.462, 3.041, 6.023, 7.686, 7.517, 5.439, 1.858, -2.408, -6.318, -8.862, -9.318, -7.456, -3.624]
  - title: "inviluppo t/2"
    data: [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8, 8.25, 8.5, 8.75, 9, 9.25, 9.5, 9.75, 10]
tension: 0.3
width: 80%
labelColors: false
fill: false
beginAtZero: false
```

Il docente porta esempi della vita quotidiana.

- **L'altalena.** Chi va in altalena riesce ad aumentare l'ampiezza dell'oscillazione dandosi la spinta con la stessa periodicità dell'altalena. Volendo può anche ridurla, andando «in controfase»: spingere quando si dovrebbe tirare e tirare quando si dovrebbe spingere. In termini di trasformate è come introdurre degli zeri che cancellano quei poli.
- **Il bicchiere di cristallo.** Un soprano che indovina la frequenza di risonanza di un bicchiere di cristallo, che come ogni oggetto con una certa conformazione simmetrica ha una risonanza naturale, può romperlo con un acuto.
- **I ponti.** I soldati che attraversano un ponte rompono il passo. La probabilità di cadenzare proprio alla frequenza di risonanza del ponte non è zero, e con una sfortuna considerevole il ponte potrebbe mettersi a oscillare sempre di più. Il docente cita anche il crollo del **Tacoma Narrows Bridge**: il ponte, che come una corda ha una propria frequenza di oscillazione, avrebbe cominciato a oscillare sempre di più sotto l'azione del vento fino a rompersi.

Questo fenomeno si chiama **condizione di risonanza**. «Ricordatevi che tutto è teoria dei sistemi»: volendo, tutto si riporta lì.

> [!tip] Approfondimento: il Tacoma Narrows Bridge non è un caso di risonanza forzata #approfondimento
> Il ponte di Tacoma crollò il 7 novembre 1940 ed è spesso citato come esempio di risonanza. L'analisi ingegneristica successiva ha però mostrato che la spiegazione è diversa. Il vento non applicava una forza periodica alla frequenza propria del ponte. Il crollo fu causato da un'instabilità **aeroelastica** di tipo torsionale (*flutter*): il moto stesso del ponte modificava le forze aerodinamiche in modo da alimentare l'oscillazione [@billah_scanlan1991]. L'American Physical Society, ricostruendo l'episodio, definisce scorretta la spiegazione «classica» per risonanza [@aps_tacoma]. In termini del corso, è più vicino a un sistema che diventa instabile, con poli che si spostano nel semipiano destro, che a un sistema stabile sollecitato alla sua pulsazione naturale. L'esempio dell'altalena e quello del bicchiere restano invece buoni esempi di risonanza.

## 5. Comunicazioni sul corso

Il docente ricorda di non accettare richieste di iscrizione al team di Microsoft Teams del corso: chi vuole entrare deve iscriversi su AulaWeb, dove trova il codice. A chi lo chiede direttamente non risponderà, oppure risponderà rimandando ad AulaWeb. Ha aggiunto che, se il numero di persone presenti in aula continuerà a diminuire, potrebbe cancellare il team con le registrazioni degli anni passati.

## 6. Esercizio — risposta a un impulso rettangolare

Il docente propone un esercizio «abbastanza semplice», da risolvere in due modi: con Laplace e con i metodi dell'analisi.

> [!example] Testo
> $$\dot y + y = u, \qquad u(t) = 1(t) - 1(t-1), \qquad y(0^-) = 0 .$$
> Trovare $y(t)$ per ogni $t \ge 0$, non solo per gli ultimi istanti.

L'ingresso è una finestra (*boxcar*, [[Lezione 02 - Funzioni generalizzate e trasformata di Laplace|lezione 2]]) di ampiezza $1$ e durata $1$: vale $1$ per $0\le t<1$ e $0$ dopo.

### 6.1 Con la trasformata di Laplace

L'equazione ha $n = 1$, $m = 0$, $a_0 = 1$, $b_0 = 1$. Le condizioni iniziali sono nulle, quindi resta solo la risposta nello stato zero:

$$T(s) = \frac{1}{s+1}, \qquad U(s) = \frac{1}{s} - \frac{1}{s}\,e^{-s} = \frac{1}{s}\big(1 - e^{-s}\big),$$

$$Y(s) = \frac{1}{s(s+1)} - \frac{1}{s(s+1)}\,e^{-s} .$$

I due pezzi sono la stessa funzione, il secondo cambiato di segno e moltiplicato per $e^{-s}$. Basta antitrasformarne uno e poi traslarlo. Con i residui, «ci si mette un attimo»: $\frac{1}{s(s+1)} = \frac{1}{s} - \frac{1}{s+1}$, quindi $\mathcal{L}^{-1}\big\{\frac{1}{s(s+1)}\big\} = 1 - e^{-t}$ (la stessa funzione dell'esempio della [[Lezione 07 - Teoremi del valore finale e del valore iniziale#4.5 Esempio svolto a lezione|lezione 7]]). Allora

$$y(t) = \big(1 - e^{-t}\big)\,1(t) - \big(1 - e^{-(t-1)}\big)\,1(t-1) .$$

Il secondo pezzo è stato traslato di $1$ e moltiplicato per $1(t-1)$, perché fino a $t=1$ non deve esistere. Leggendo per intervalli:

- per $0 \le t < 1$: $y(t) = 1 - e^{-t}$;
- per $t \ge 1$: $y(t) = 1 - e^{-t} - 1 + e^{-(t-1)} = e^{-(t-1)} - e^{-t} = (e - 1)\,e^{-t}$.

In $t = 1$ i due tratti si raccordano: entrambi valgono $1 - e^{-1}$.

```chart
type: line
labels: [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]
series:
  - title: "ingresso u(t)"
    data: [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - title: "uscita y(t)"
    data: [0, 0.221, 0.393, 0.528, 0.632, 0.492, 0.383, 0.299, 0.233, 0.181, 0.141, 0.11, 0.086, 0.067, 0.052, 0.04, 0.031, 0.025, 0.019, 0.015, 0.012]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: true
```

Il grafico è campionato ogni $0{,}25$: la discesa verticale dell'ingresso in $t=1$ appare come un tratto inclinato.

### 6.2 Con i metodi dell'analisi

Senza Laplace si risolve un tratto alla volta, come insegnato ad Analisi: si trova la soluzione tra $0$ e $1$, si calcola il valore in $1$ e lo si usa come condizione iniziale del tratto successivo.

**Tratto $0\le t<1$.** L'equazione è $\dot y + y = 1$. La soluzione è un integrale particolare più l'integrale generale dell'omogenea associata: $y(t) = 1 + A\,e^{-t}$. La condizione $y(0^-) = 0$ dà $A = -1$, quindi $y(t) = 1 - e^{-t}$. In $t = 1$ si arriva con $y(1) = 1 - e^{-1}$.

**Tratto $t \ge 1$.** Ora l'equazione è $\dot y + y = 0$: l'integrale particolare è nullo e $y(t) = B\,e^{-t}$. La condizione iniziale non è più zero ma il valore raggiunto: $B\,e^{-1} = 1 - e^{-1}$, quindi $B = e - 1$ e $y(t) = (e-1)\,e^{-t}$, come con Laplace.

> [!tip] Il commento del docente
> Con un'equazione del primo ordine e un ingresso a due tratti, i due metodi richiedono un lavoro simile. Con equazioni di ordine due o tre, o con ingressi fatti di molti pezzi, è molto più facile passare per la trasformata. Con Laplace la procedura è sempre la stessa: si trasforma, si antitrasforma, e «non dovete metterci niente di cervello». Con l'altro metodo bisogna ricostruire ogni volta la soluzione tratto per tratto.

> [!tip] Collegamento con il teorema del valore finale
> $Y(s) = \frac{1 - e^{-s}}{s(s+1)}$ non è un rapporto di polinomi, perché contiene $e^{-s}$. È proprio il caso segnalato dalla dispensa (lezione 7, §2.2): il fattore $\frac{1}{s}$ da solo darebbe un gradino, ma la differenza con la sua traslata si annulla per $t\to\infty$. Infatti $\lim_{s\to0}sY(s) = \lim_{s\to0}\frac{1-e^{-s}}{s+1} = 0$, e $y(t) = (e-1)e^{-t}\to0$.

## 7. Correzioni alla nota «Equazioni differenziali»

> [!warning] Refusi nella nota personale
> La struttura della nota è corretta. Ci sono alcuni refusi da sistemare:
> - **riga della trasformata del massa-molla**: è scritto $s^2Y(s) + s\,y(0^-) - \dot y(0^-)$, ma deve essere $s^2Y(s) - s\,y(0^-) - \dot y(0^-)$. La riga successiva, con i termini portati a destra, è corretta;
> - **espressione di $Y(s)$**: il numeratore della risposta a ingresso nullo è scritto $sY(0^-) + y(0^-)$, mentre deve essere $s\,y(0^-) + \dot y(0^-)$. Inoltre compare $F(x)$ al posto di $F(s)$;
> - **condizioni iniziali del primo caso**: è scritto $y(0^-) = \dot y(0^-)$, ma il senso è $y(0^-) = \dot y(0^-) = 0$. Lo stesso refuso compare nella riga sulla risposta all'impulso, dove la seconda condizione riguarda le $u^{(k)}(0^-)$, non di nuovo le $y^{(k)}(0^-)$;
> - **polinomio $Z$**: dipende da $u^{(k)}(0^-)$ per $k$ fino a $m-1$, non $n-1$;
> - **caso di risonanza**: «4 poli immaginari, molteplicità 2» va letto come **due** poli distinti $\pm j\omega_n$, ciascuno con molteplicità $2$ (quattro contando la molteplicità). La conclusione corretta è «non limitata», più precisa di «non converge».

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. *Perché per un sistema causale deve essere $m\le n$?* Con $m>n$ l'uscita dipenderebbe da derivate dell'ingresso di ordine più alto delle proprie. Nel caso limite $y=\dot u$, il sistema dovrebbe conoscere l'andamento futuro dell'ingresso per calcolarne la derivata.
2. *Perché il polinomio delle condizioni iniziali ha grado $n-1$?* Ogni applicazione della regola della derivata aggiunge una condizione iniziale moltiplicata per una potenza di $s$ inferiore di uno a quella di $Y$. Il termine di grado più alto è $s^{n-1}y(0^-)$.
3. *Perché la soluzione si separa in due addendi indipendenti?* Il sistema è lineare: l'effetto delle condizioni iniziali (cause interne) e quello dell'ingresso (cause esterne) si sommano.
4. *Che cosa rappresenta la funzione di trasferimento nel dominio del tempo?* È la trasformata della risposta all'impulso, cioè della risposta nello stato zero all'ingresso $\delta(t)$.
5. *Perché nella massa-molla un impulso dà un seno e uno spostamento iniziale dà un coseno?* Il primo parte da posizione nulla con velocità non nulla, il secondo dalla posizione massima con velocità nulla.
6. *Perché una forza sinusoidale alla pulsazione naturale fa crescere l'oscillazione senza limite?* La trasformata dell'uscita ha poli $\pm j\omega_n$ doppi, a parte reale nulla con molteplicità $2$: compare il termine $t\cos\omega_n t$, che non è limitato.
7. *Perché con Laplace l'esercizio del §6 non richiede di imporre la continuità in $t=1$?* La traslazione con $1(t-1)$ tiene conto automaticamente del cambio d'ingresso. La continuità della soluzione in $t=1$ risulta dal calcolo, come si verifica.
