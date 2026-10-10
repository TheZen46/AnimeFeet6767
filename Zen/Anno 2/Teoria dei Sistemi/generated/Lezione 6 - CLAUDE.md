---

## corso: Teoria dei Sistemi lezione: 6 data: 2026-10-08 argomenti: [metodo dei residui, residui e identificazione combinati, coppia di poli immaginari semplici, polinomi a coefficienti reali e complesso coniugato, parte reale e immaginaria di G(jω0), angolo aggiunto, modulo e fase di numeri complessi] fonti: [trascrizione parte 1, appunti manuali, dispensa del docente (inglese), dispensa del docente (italiano)] tags: [teoria-dei-sistemi, lezione]
---
# Lezione 6 — Residui e poli immaginari semplici

Questa nota ricostruisce la sesta lezione. Le fonti sono:

- la trascrizione della registrazione (parte 1);
- la nota personale «Antitrasformata di Laplace», nelle parti sui residui e su $G(j\omega_0)$;
- la dispensa in inglese del docente (§2.2.2, formule 2.26–2.31 ed esempio E/2.2/5, pp. 18–19);
- la dispensa italiana (cap. 1, pp. 28–29), per il richiamo al metodo dei residui.

La lezione completa i metodi per l'antitrasformata con due strumenti.

1. Il primo è l'uso **combinato** di residui e identificazione dei polinomi: si calcolano con i residui i coefficienti dei poli reali semplici e si risolve un sistema più piccolo per gli altri.
2. Il secondo è un metodo per estrarre direttamente la **parte oscillante** dell'antitrasformata quando la trasformata contiene una coppia di **poli immaginari semplici**. Il docente avverte che il risultato tornerà, nella stessa forma, tra quattro o cinque lezioni, e che conviene impararlo già in quella forma.

## 1. Riepilogo e uso combinato con l'identificazione

L'ultima cosa vista nella [[Zen/Anno 2/Teoria dei Sistemi/generated/Lezione 5 - CLAUDE|lezione 5]] è il **metodo del calcolo dei residui**. La formula è generale, ma è davvero conveniente solo in alcuni casi particolari: soprattutto per i poli reali semplici, per i quali il coefficiente si ottiene con un limite, senza derivate, ed è già il coefficiente reale dell'esponenziale.

La lezione si apre con un esempio che mostra come combinare i due metodi.

> [!example] $F(s) = \dfrac{1}{(s+1)(s+2)(s^2+4)}$ — residui più identificazione 
> L'espansione nella forma della tabella ($\omega=2$) è $$F(s) = \frac{A}{s+1} + \frac{B}{s+2} + C,\frac{2}{s^2+4} + D,\frac{s}{s^2+4}.$$ **Poli reali semplici con i residui:** $$A = \lim_{s\to-1}\frac{1}{(s+2)(s^2+4)} = \frac{1}{(1)(5)} = \frac{1}{5}, \qquad B = \lim_{s\to-2}\frac{1}{(s+1)(s^2+4)} = \frac{1}{(-1)(4+4)} = -\frac{1}{8}.$$ **Identificazione con due sole incognite.** Si riporta al minimo comune multiplo come per i fratti semplici. Il numeratore $A(s+2)(s^2+4) + B(s+1)(s^2+4) + 2C(s+1)(s+2) + D,s(s+1)(s+2)$ deve essere uguale a $1$. Con $A$ e $B$ già noti, bastano due equazioni:
> 
> - coefficiente di $s^3$: $A + B + D = 0$, quindi $D = -\frac{1}{5} + \frac{1}{8} = -\frac{3}{40}$;
> - termine noto: $8A + 4B + 4C = 1$, quindi $\frac{8}{5} - \frac{1}{2} + 4C = 1$, cioè $C = -\frac{1}{40}$.
> 
> Le altre due equazioni (coefficienti di $s^2$ e di $s$) restano come verifica. Il problema si è ridotto a un piccolo sistema lineare. $$f(t) = \frac{1}{5},e^{-t} - \frac{1}{8},e^{-2t} - \frac{1}{40}\sin 2t - \frac{3}{40}\cos 2t .$$ Nel §3 la parte oscillante verrà ritrovata con un metodo diretto.

L'esempio non è scelto a caso. Rientra nella serie dei «trucchi» per l'antitrasformata, ma introduce anche un concetto che servirà per studiare la risposta dei sistemi a segnali particolari.

## 2. Il problema: una coppia di poli immaginari semplici

### 2.1 Le ipotesi

Si consideri una trasformata della forma

$$F(s) = \frac{N(s)}{D(s),\big(s^2+\omega_0^2\big)}$$

con queste ipotesi:

- $N$ e $D$ sono polinomi **primi tra loro**: nessuna radice del numeratore coincide con una radice del denominatore;
- nel denominatore c'è una coppia di **poli immaginari** $\pm j\omega_0$;
- la coppia è **semplice**: $D(s)$ non contiene a sua volta le radici $\pm j\omega_0$. $D$ può avere tutte le radici che vuole, ma non un altro fattore $s^2+\omega_0^2$.

### 2.2 La forma da usare

Conviene raccogliere tutto ciò che non riguarda la coppia immaginaria in una funzione $G(s)$, in modo che accanto rimanga esattamente la forma della tabella per il seno:

$$F(s) = \underbrace{\frac{N(s)}{\omega_0,D(s)}}_{G(s)}\cdot\frac{\omega_0}{s^2+\omega_0^2} .$$

In linea di principio l'espansione in fratti semplici richiederebbe di trovare tutte le radici di $D$ e di mettere una frazione per ciascuna, più due per la coppia $\pm j\omega_0$. Il fattore $s^2+\omega_0^2$ ha grado $2$ e quindi «se ne porta via» esattamente due:

$$F(s) = E_G(s) + C_1,\frac{\omega_0}{s^2+\omega_0^2} + C_2,\frac{s}{s^2+\omega_0^2},$$

dove $E_G(s)$ indica l'insieme delle frazioni relative alle radici di $D$, quante che siano. Il docente ribadisce che non bisogna farsi ingannare dalla scrittura: anche se il fattore $s^2+\omega_0^2$ compare una volta sola, le frazioni sono **due**, perché il denominatore ha grado $2$. Le si scrive in questa forma perché l'antitrasformata si legge subito:

$$f(t) = \mathcal{L}^{-1}{E_G(s)} + C_1\sin\omega_0 t + C_2\cos\omega_0 t .$$

### 2.3 Perché l'identificazione non basta

Se $D(s)$ è un polinomio generico, di cui non si conosce la forma, non si può impostare l'identificazione dei polinomi: non si sa nemmeno quante frazioni ci siano in $E_G$, né quali equazioni scrivere. Spesso, inoltre, interessa soltanto la **parte oscillante** dell'antitrasformata. Serve quindi un modo per calcolare $C_1$ e $C_2$ senza toccare il resto.

## 3. Il calcolo con i residui sui poli immaginari

### 3.1 L'eccezione

Il docente si «rimangia la parola» data nella lezione precedente: per una volta usa la formula dei residui anche per poli **non reali**. Lo si può fare perché i poli $\pm j\omega_0$ sono **semplici**, e quindi basta un limite.

Si riscrivono le due frazioni della coppia nella forma «dei matematici», con i poli complessi in evidenza:

$$C_1,\frac{\omega_0}{s^2+\omega_0^2} + C_2,\frac{s}{s^2+\omega_0^2} = \frac{\bar c_1}{s+j\omega_0} + \frac{\bar c_2}{s-j\omega_0},$$

dove $s^2+\omega_0^2 = (s+j\omega_0)(s-j\omega_0)$. I coefficienti $\bar c_1$, $\bar c_2$ (con il soprassegno, per distinguerli) non sono $C_1$ e $C_2$, ma sono legati a essi.

Per i poli semplici vale la formula dei residui:

$$\bar c_1 = \lim_{s\to -j\omega_0}(s+j\omega_0),G(s),\frac{\omega_0}{(s+j\omega_0)(s-j\omega_0)} = G(-j\omega_0),\frac{\omega_0}{-2j\omega_0} = -\frac{G(-j\omega_0)}{2j},$$

$$\bar c_2 = \lim_{s\to j\omega_0}(s-j\omega_0),G(s),\frac{\omega_0}{(s+j\omega_0)(s-j\omega_0)} = G(j\omega_0),\frac{\omega_0}{2j\omega_0} = \frac{G(j\omega_0)}{2j}.$$

Nel primo limite, sostituendo $s=-j\omega_0$ nel fattore rimasto $s - j\omega_0$ si ottiene $-2j\omega_0$, e gli $\omega_0$ si semplificano. Il secondo si calcola «esattamente all'altra maniera». Il calcolo è lecito perché $G$ non ha poli in $\pm j\omega_0$, per l'ipotesi di coppia semplice: $G(\pm j\omega_0)$ è un numero complesso finito.

### 3.2 Una proprietà dei polinomi a coefficienti reali

Per andare avanti serve una proprietà che il docente chiede agli studenti di conoscere, o di verificare da soli.

> [!important] Polinomi e complesso coniugato Sia $P(s)$ un polinomio a **coefficienti reali**. Sostituendo a $s$ un numero complesso si ottiene un numero complesso. Sostituendo il **complesso coniugato** di quel numero si ottiene il **complesso coniugato** del risultato: $$P(\bar s) = \overline{P(s)} .$$ Lo stesso vale per un rapporto di polinomi a coefficienti reali. In particolare $$G(-j\omega_0) = \overline{G(j\omega_0)} .$$

La verifica, accennata a lezione, usa la forma polare. Si scrive il polinomio come $P(s) = \sum_{i=0}^{n} a_i s^i$ con $a_i$ reali, e il numero complesso come $s = \rho,e^{j\theta}$. Allora $s^i = \rho^i e^{ji\theta}$: si eleva il modulo alla $i$ e l'indice entra nell'esponente. Per la formula di Eulero,

$$P(\rho e^{j\theta}) = \sum_{i=0}^{n} a_i\rho^i\cos(i\theta) + j\sum_{i=0}^{n} a_i\rho^i\sin(i\theta) .$$

Il primo addendo è la parte reale, il secondo la parte immaginaria. Il coniugato $\bar s = \rho e^{-j\theta}$ ha lo stesso modulo e fase opposta. Il coseno è pari, quindi la parte reale non cambia; il seno è dispari, quindi la parte immaginaria cambia segno. Il risultato è il coniugato di prima. Per un rapporto di polinomi il discorso si ripete per numeratore e denominatore, e il rapporto dei coniugati è il coniugato del rapporto.

### 3.3 Il risultato: seno e coseno

Si indicano la parte reale e la parte immaginaria di $G(j\omega_0)$ con $A$ e $B$, «per risparmiare gesso»:

$$G(j\omega_0) = \underbrace{\mathrm{Re},G(j\omega_0)}_{A} + j,\underbrace{\mathrm{Im},G(j\omega_0)}_{B}, \qquad G(-j\omega_0) = A - jB .$$

Le due frazioni con i poli complessi si antitrasformano come esponenziali complessi, perché $\frac{1}{s-a}\to e^{at}$ vale anche per $a$ complesso:

$$\frac{A+jB}{2j},e^{j\omega_0 t} - \frac{A-jB}{2j},e^{-j\omega_0 t} = A,\underbrace{\frac{e^{j\omega_0 t} - e^{-j\omega_0 t}}{2j}}_{\sin\omega_0 t} + B,\underbrace{\frac{e^{j\omega_0 t} + e^{-j\omega_0 t}}{2}}_{\cos\omega_0 t} .$$

Nel passaggio si usa $\frac{jB}{2j} = \frac{B}{2}$ e si raccolgono le formule di Eulero per seno e coseno. Le parti immaginarie si sono elise e resta una funzione reale, come deve essere.

> [!important] Parte oscillante dovuta a una coppia di poli immaginari semplici Se $F(s) = G(s),\dfrac{\omega_0}{s^2+\omega_0^2}$ e $G$ non ha poli in $\pm j\omega_0$: $$\mathcal{L}^{-1}{F(s)} = \mathcal{L}^{-1}{E_G(s)} + \mathrm{Re},G(j\omega_0),\sin\omega_0 t + \mathrm{Im},G(j\omega_0),\cos\omega_0 t .$$ I coefficienti del seno e del coseno si trovano **sostituendo $s = j\omega_0$ in $G$**, senza conoscere nulla del resto dell'espansione.

Il docente mette in guardia sul fattore $\omega_0$. $G$ va costruita in modo che accanto rimanga esattamente $\frac{\omega_0}{s^2+\omega_0^2}$, la forma del seno in tabella. Se $\omega_0 = 1$ il numeratore è $1$; se $\omega_0^2 = 4$, cioè $\omega_0 = 2$, il numeratore deve essere $2$, e il fattore $\frac{1}{2}$ finisce dentro $G$.

## 4. Seno e coseno insieme: il metodo dell'angolo aggiunto

### 4.1 Una sola sinusoide

Dalle superiori si dovrebbe ricordare il cosiddetto **metodo dell'angolo aggiunto**. «Detto così dalla sua definizione fa schifo», commenta il docente, ma significa semplicemente scrivere la somma di un seno e di un coseno della stessa pulsazione come un'unica sinusoide, moltiplicata per un'ampiezza e sfasata. Si cercano $M$ e $\varphi$ tali che

$$A\sin\omega_0 t + B\cos\omega_0 t = M\sin(\omega_0 t + \varphi) .$$

Per la formula di addizione, $M\sin(\omega_0 t + \varphi) = M\cos\varphi,\sin\omega_0 t + M\sin\varphi,\cos\omega_0 t$. L'uguaglianza deve valere per ogni $t$, quindi i coefficienti del seno e del coseno devono coincidere:

$$M\cos\varphi = A, \qquad M\sin\varphi = B .$$

Elevando al quadrato e sommando, $M^2(\cos^2\varphi + \sin^2\varphi) = M^2 = A^2 + B^2$. Facendo il rapporto, $\tan\varphi = B/A$. Poiché $A$ e $B$ sono la parte reale e la parte immaginaria di $G(j\omega_0)$:

$$M = \sqrt{A^2+B^2} = |G(j\omega_0)|, \qquad \varphi = \angle G(j\omega_0) .$$

> [!important] Forma modulo e fase $$\mathcal{L}^{-1}\left{G(s),\frac{\omega_0}{s^2+\omega_0^2}\right} = \mathcal{L}^{-1}{E_G(s)} + |G(j\omega_0)|,\sin\big(\omega_0 t + \angle G(j\omega_0)\big).$$ Se in una funzione «fatta di un sacco di roba» interessa solo il pezzo di antitrasformata dovuto alla coppia di poli immaginari, non si deve antitrasformare tutto. Si costruisce $G$, se ne calcolano modulo e fase in $j\omega_0$, e la parte oscillante è questa sinusoide.

> [!warning] La fase va presa nel quadrante giusto La relazione $\tan\varphi = B/A$ non basta a determinare $\varphi$, perché la tangente ha periodo $\pi$: $(A, B)$ e $(-A, -B)$ danno lo stesso rapporto. Bisogna tenere conto dei segni di $A$ e $B$, cioè usare l'arcotangente «a quattro quadranti». Lo precisa anche la nota iniziale della dispensa in inglese. In pratica, $\varphi$ è l'angolo del numero complesso $A + jB$ nel piano di Gauss.

### 4.2 Perché modulo e fase spesso convengono

Il docente fa notare che il secondo metodo è spesso più rapido. Per calcolare parte reale e parte immaginaria di un rapporto di polinomi grossi bisogna sostituire $j\omega_0$, sviluppare tutti i conti, separare parti reali e immaginarie sopra e sotto, razionalizzare e infine separare di nuovo. Per modulo e fase, invece, basta ricordare due regole sui numeri complessi:

- il **prodotto** di numeri complessi ha per modulo il **prodotto dei moduli** e per argomento la **somma degli argomenti**;
- il **rapporto** ha per modulo il **rapporto dei moduli** e per argomento la **differenza** tra l'argomento del numeratore e quello del denominatore.

Se $G$ è già fattorizzata, modulo e fase si calcolano fattore per fattore, «quasi a occhio».

## 5. Esempio svolto nei due modi

> [!example] La parte oscillante di $F(s) = \dfrac{1}{(s+1)(s+2)(s^2+4)}$ I poli sono $-1$ e $-2$, reali negativi, e la coppia immaginaria semplice $\pm2j$, quindi $\omega_0 = 2$. Per avere il seno della tabella si scrive $$F(s) = \underbrace{\frac{1}{2(s+1)(s+2)}}_{G(s)}\cdot\frac{2}{s^2+4} .$$
> 
> **Primo modo: parte reale e parte immaginaria.** Si sostituisce $s = 2j$: $$G(2j) = \frac{1}{2(2j+1)(2j+2)} = \frac{1}{2(4j^2 + 4j + 2j + 2)} = \frac{1}{2(-2+6j)} = \frac{1}{-4+12j}.$$ Si razionalizza moltiplicando sopra e sotto per il coniugato $-4-12j$. Al denominatore $16 + 144 = 160$: $$G(2j) = \frac{-4-12j}{160} = -\frac{1}{40} - \frac{3}{40},j .$$ Quindi $A = -\frac{1}{40}$, $B = -\frac{3}{40}$, e la parte oscillante è $$-\frac{1}{40}\sin 2t - \frac{3}{40}\cos 2t,$$ in accordo con il §1.
> 
> **Secondo modo: modulo e fase.** $$|G(2j)| = \frac{1}{2,|2j+1|,|2j+2|} = \frac{1}{2\cdot\sqrt5\cdot\sqrt8} = \frac{1}{2\cdot\sqrt5\cdot2\sqrt2} = \frac{1}{4\sqrt{10}} .$$ La fase è quella del numeratore meno quella di tutto ciò che sta sotto. Il numeratore $1$ è un numero reale positivo, «appoggiato sull'asse reale», quindi ha fase $0$. Al denominatore la fase di un prodotto è la somma delle fasi: $\angle 2 = 0$, $\angle(1+2j) = \arctan 2$, $\angle(2+2j) = \frac{\pi}{4}$. Quindi $$\angle G(2j) = 0 - \Big(0 + \arctan 2 + \frac{\pi}{4}\Big) = -\frac{\pi}{4} - \arctan 2 \approx -1{,}89\ \text{rad}.$$ La parte oscillante è $$\frac{1}{4\sqrt{10}},\sin!\Big(2t - \frac{\pi}{4} - \arctan 2\Big).$$
> 
> **Le due forme coincidono.** Il docente osserva che, venendo dallo stesso risultato, le due espressioni devono essere uguali, anche se a occhio è difficile dimostrarlo («non so quanto vale l'arcotangente di 2»). La verifica, non svolta a lezione, si fa con le formule di addizione. Con $\cos(\arctan 2) = \frac{1}{\sqrt5}$ e $\sin(\arctan 2) = \frac{2}{\sqrt5}$: $$\cos\Big(\frac{\pi}{4} + \arctan 2\Big) = \frac{\sqrt2}{2}\cdot\frac{1}{\sqrt5} - \frac{\sqrt2}{2}\cdot\frac{2}{\sqrt5} = -\frac{1}{\sqrt{10}}, \qquad \sin\Big(\frac{\pi}{4} + \arctan 2\Big) = \frac{\sqrt2}{2}\cdot\frac{2}{\sqrt5} + \frac{\sqrt2}{2}\cdot\frac{1}{\sqrt5} = \frac{3}{\sqrt{10}} .$$ Con $\varphi = -(\frac{\pi}{4} + \arctan 2)$ si ha quindi $M\cos\varphi = \frac{1}{4\sqrt{10}}\cdot\big(-\frac{1}{\sqrt{10}}\big) = -\frac{1}{40} = A$ e $M\sin\varphi = \frac{1}{4\sqrt{10}}\cdot\big(-\frac{3}{\sqrt{10}}\big) = -\frac{3}{40} = B$.
> 
> Il punto $(A, B)$ sta nel terzo quadrante, entrambi negativi, e infatti $\varphi \approx -1{,}89$ rad $\approx -108°$ è un angolo del terzo quadrante. Un'arcotangente «a un quadrante», $\arctan\frac{B}{A} = \arctan 3 \approx 1{,}25$ rad, darebbe una fase sbagliata di $\pi$.

> [!warning] Nota personale «Antitrasformata di Laplace» I calcoli numerici di questo esempio nella nota sono corretti. Ci sono però alcuni refusi:
> 
> - nella riga $\angle G(2j) = 0 - \angle(\dots) = (0 + \arctan 2 + \frac{\pi}{4})$ manca il segno meno davanti alla parentesi. Il risultato finale $\sin(2t - \frac{\pi}{4} - \arctan 2)$ è invece corretto;
> - quel risultato è etichettato «$G(2j) = \dots$», ma è la **parte oscillante dell'antitrasformata**, non il valore di $G$;
> - nella derivazione generale, il secondo termine dell'antitrasformata è scritto $-\frac{A-jB}{2j}e^{j\omega_0 t}$, mentre deve essere $+\frac{A+jB}{2j}e^{j\omega_0 t}$. Nella riga successiva il secondo $\frac{B}{2}e^{-j\omega_0 t}$ deve essere $\frac{B}{2}e^{+j\omega_0 t}$. Il risultato finale, $\mathrm{Re},G\sin + \mathrm{Im},G\cos$, è giusto;
> - nei limiti per $C_1$ e $C_2$ va scritto $\lim (s\pm j\omega_0)F(s)$, non $\lim F(s)$: il fattore compare solo nel passaggio successivo.

## 6. Esempio con due coppie di poli immaginari

> [!example] $F(s) = \dfrac{1}{(s^2+1)(s^2+4)}$ Ci sono due coppie di poli immaginari semplici, $\pm j$ e $\pm2j$. L'espansione nella forma della tabella è $$F(s) = A,\frac{1}{s^2+1} + B,\frac{s}{s^2+1} + C,\frac{2}{s^2+4} + D,\frac{s}{s^2+4}.$$ Per la prima coppia $\omega_0 = 1$ e il numeratore del seno è $1$; per la seconda $\omega_0 = 2$ e il numeratore è $2$. Come risponde il docente a una domanda: «per forza, è la $\omega$».
> 
> **Coppia $\pm j$.** Si scrive $F = G_1(s),\frac{1}{s^2+1}$ con $G_1(s) = \frac{1}{s^2+4}$. Allora $G_1(j) = \frac{1}{-1+4} = \frac{1}{3}$: reale positivo, con modulo $\frac{1}{3}$ e fase $0$. Il contributo è $\frac{1}{3}\sin t$.
> 
> **Coppia $\pm2j$.** Si scrive $F = G_2(s),\frac{2}{s^2+4}$ con $G_2(s) = \frac{1}{2(s^2+1)}$. Allora $G_2(2j) = \frac{1}{2(-4+1)} = -\frac{1}{6}$: un numero reale negativo, con modulo $\frac{1}{6}$. La sua fase è $\pi$, o equivalentemente $-\pi$: un numero sul semiasse reale negativo si raggiunge girando di mezzo giro da una parte o dall'altra. Il contributo è $$\frac{1}{6}\sin(2t - \pi) = \frac{1}{6}\big(\sin 2t\cos\pi - \cos 2t\sin\pi\big) = -\frac{1}{6}\sin 2t .$$ In forma parte reale/parte immaginaria: $\mathrm{Re},G_2(2j) = -\frac{1}{6}$ è il coefficiente del seno, $\mathrm{Im},G_2(2j) = 0$ quello del coseno.
> 
> $$f(t) = \frac{1}{3}\sin t - \frac{1}{6}\sin 2t .$$
> 
> **Verifica con l'identificazione.** Il numeratore comune $A(s^2+4) + B,s(s^2+4) + 2C(s^2+1) + D,s(s^2+1)$ deve essere uguale a $1$: $$\begin{cases} B + D = 0 & (s^3)\ A + 2C = 0 & (s^2)\ 4B + D = 0 & (s^1)\ 4A + 2C = 1 & (s^0) \end{cases}$$ Come fa notare il docente, le equazioni vanno **a coppie**. $B$ e $D$ compaiono solo nella prima e nella terza, che insieme danno $B = D = 0$. Dalla seconda e dalla quarta, sottraendo, $3A = 1$: quindi $A = \frac{1}{3}$ e $C = -\frac{1}{6}$. È lo stesso risultato.
> 
> Nel caso specifico, ammette il docente, l'identificazione non richiedeva molto lavoro. Il metodo di $G(j\omega_0)$ diventa davvero conveniente quando il denominatore è complicato e serve solo la parte oscillante.

> [!warning] Il fattore $\omega_0$ in $G$ Nella nota personale, per la coppia $\pm2j$ compaiono due scritture: $\frac{1}{2(s^2+1)}\cdot\frac{2}{s^2+4}$ e $\frac{1}{s^2+1}\cdot\frac{1}{s^2+4}$. Solo la prima ha la forma $G(s),\frac{\omega_0}{s^2+\omega_0^2}$ richiesta dalla formula. Usando la seconda, cioè $G = \frac{1}{s^2+1}$, si otterrebbe $G(2j) = -\frac{1}{3}$: il **doppio** del valore corretto. Nella trascrizione compare proprio il valore $-\frac{1}{3}$, a cui il docente ha poi applicato il fattore $\frac{1}{2}$.

## 7. Altre applicazioni

### 7.1 Un esempio dalla dispensa

> [!example] Dispensa inglese, esempio E/2.2/5: $F(s) = \dfrac{s+2}{(s+1)(s^2+1)}$ Il polo reale semplice $-1$ si tratta con il residuo: $c_1 = \lim_{s\to-1}\frac{s+2}{s^2+1} = \frac{1}{2}$. Per la coppia $\pm j$ ($\omega_0 = 1$) si prende $G(s) = \frac{s+2}{s+1}$: $$M = |G(j)| = \frac{|2+j|}{|1+j|} = \frac{\sqrt5}{\sqrt2} = \sqrt{\frac{5}{2}}, \qquad \varphi = \angle(2+j) - \angle(1+j) = \arctan\frac{1}{2} - \frac{\pi}{4} .$$ $$f(t) = \frac{1}{2},e^{-t} + \sqrt{\frac{5}{2}},\sin!\Big(t + \arctan\frac{1}{2} - \frac{\pi}{4}\Big).$$ Con parte reale e parte immaginaria: $G(j) = \frac{(2+j)(1-j)}{2} = \frac{3}{2} - \frac{1}{2}j$, quindi la parte oscillante è anche $\frac{3}{2}\sin t - \frac{1}{2}\cos t$. Il calcolo con l'espansione completa dà lo stesso risultato.

### 7.2 Ritorno all'esercizio della lezione 5 (osservazione non svolta a lezione)

Nella [[Lezione 05 - Fratti semplici, interpretazione e metodo dei residui#3. Esercizio in aula — leggere un'antitrasformata prima di calcolarla|lezione 5]] si era trovata, risolvendo un sistema $4\times4$, l'antitrasformata di $\frac{s^4}{(s+1)(s+2)(s^2+4)}$. La sua parte oscillante era $-\frac{2}{5}\sin 2t - \frac{6}{5}\cos 2t$. Con il metodo di questa lezione la si ottiene in una riga, osservando che

$$\frac{s^4}{(s+1)(s+2)(s^2+4)} = \underbrace{\frac{s^4}{2(s+1)(s+2)}}_{G(s)}\cdot\frac{2}{s^2+4}, \qquad G(2j) = \frac{(2j)^4}{2(2j+1)(2j+2)} = 16\cdot\Big(-\frac{1}{40} - \frac{3}{40}j\Big) = -\frac{2}{5} - \frac{6}{5},j .$$

Poiché $(2j)^4 = 16$, la parte oscillante è esattamente $16$ volte quella dell'esempio del §5. Parte reale e parte immaginaria danno subito i coefficienti di seno e coseno, senza divisione e senza sistema. Il resto dell'antitrasformata (impulso ed esponenziali) va calcolato a parte, ma la parte oscillante non dipende da esso.

## 8. Dove porta questo metodo

Il docente insiste perché il risultato venga imparato **in questa forma**, $|G(j\omega_0)|,\sin(\omega_0 t + \angle G(j\omega_0))$. Tra qualche lezione, quando lo si rivedrà, si capirà subito perché.

> [!tip] Collegamento con il seguito del corso La dispensa in inglese riprende esattamente questa costruzione nel §3.2 (_Frequency Response_, p. 31). Si considera un sistema descritto da una funzione $T(s)$ (la _funzione di trasferimento_, introdotta più avanti nel corso) e lo si sollecita con un ingresso sinusoidale, la cui trasformata contiene una coppia di poli immaginari semplici. La trasformata dell'uscita ha allora la forma studiata in questa lezione. Se il sistema è stabile, a regime l'uscita è una sinusoide della stessa pulsazione, con ampiezza moltiplicata per $|T(j\omega_0)|$ e sfasata di $\angle T(j\omega_0)$. È la **risposta in frequenza**, che si rappresenta con i diagrammi di Bode.

## Domande di autoverifica

Domande nello stile dei «perché» d'esame, con una traccia di risposta.

1. _Perché conviene calcolare prima con i residui i coefficienti dei poli reali semplici?_ Si ottengono con un limite, senza sistema. Inseriti nell'identificazione, riducono il numero di incognite.
2. _Perché per la coppia $\pm j\omega_0$ si possono usare i residui anche se i poli sono complessi?_ I poli sono semplici, quindi basta un limite senza derivate. I due coefficienti complessi risultano coniugati e si ricombinano in seno e coseno reali.
3. _Perché $G(-j\omega_0)$ è il complesso coniugato di $G(j\omega_0)$?_ $G$ è un rapporto di polinomi a coefficienti reali. Sostituendo il coniugato, la parte reale (somma di coseni, funzione pari) non cambia e la parte immaginaria (somma di seni, funzione dispari) cambia segno.
4. _Perché in $G$ va inserito il fattore $\frac{1}{\omega_0}$?_ La formula presuppone che accanto a $G$ resti $\frac{\omega_0}{s^2+\omega_0^2}$, la forma esatta del seno in tabella. Altrimenti i coefficienti risultano moltiplicati per $\omega_0$.
5. _Perché la fase non si può calcolare semplicemente come $\arctan\frac{B}{A}$?_ La tangente ha periodo $\pi$, quindi l'arcotangente non distingue $(A, B)$ da $(-A, -B)$. Bisogna considerare i segni, cioè il quadrante di $A + jB$.
6. _Che cosa succederebbe se la coppia $\pm j\omega_0$ fosse doppia?_ $G$ avrebbe ancora un polo in $\pm j\omega_0$ e il limite non sarebbe finito. Inoltre comparirebbero anche termini $t\sin\omega_0 t$ e $t\cos\omega_0 t$: il metodo di questa lezione non si applica.
7. _Perché il metodo è utile anche se non si conosce $D(s)$?_ La parte oscillante dipende solo dal valore di $G$ in $j\omega_0$, non dalla struttura del resto dell'espansione.