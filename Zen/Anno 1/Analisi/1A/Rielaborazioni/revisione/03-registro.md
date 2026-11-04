# Analisi Matematica 1A · registro delle correzioni e delle aggiunte

Fasi 4 e 5, svolte il 3 novembre 2026 sulla struttura approvata (5 moduli). Per le lezioni mancanti si è seguita la strada A: aggiunte complete, ciascuna in un blocco `[!aggiunta]` con la fonte.

Il testo di partenza è `trascrizione/`. "L05 p. 2" vuol dire Lezione 05, pagina 2 del PDF originale.

## 1. Correzioni di sostanza

| # | Modulo, sezione | Prima (appunti) | Dopo | Motivo | Fonte |
|---|---|---|---|---|---|
| 1 | 4.5 | Massimo / minimo: "$f(x) \ge f(x_0)$ / $f(x) \le f(x_0)$" (L09 p. 2) | Massimo: $f(x) \le f(x_0)$; minimo: $f(x) \ge f(x_0)$; anche per la versione globale e quella stretta | Disuguaglianze scambiate | Definizione standard; Canuto-Tabacco |
| 2 | 5.1 | Nella dimostrazione, $\frac{f(y)-f(x)}{y-x} > 0$ e limite $> 0$ (L09 p. 4) | $\ge 0$ e limite $\ge 0$ | Per $f$ solo crescente il rapporto può essere nullo | – |
| 3 | 1.6 | Iniettiva: "ovvero $\forall x_1, x_2 \in X$" (L04 p. 1) | $x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$, con la forma equivalente | Definizione incompleta | – |
| 4 | 3.2 | Permanenza del segno con ipotesi $f(x_0) \ge 0$ (L06 p. 2) | $f(x_0) > 0$, con un blocco `[!attenzione]` e il controesempio $-x^2$ | Con $f(x_0) = 0$ la tesi è falsa | – |
| 5 | 4.3 | La regola della catena divide per $f(x_0+h) - f(x_0)$ (L08 p. 3) | Dimostrazione con la funzione ausiliaria $\varphi$ prolungata con $g'(y_0)$ | Il denominatore può annullarsi per infiniti $h$ | Canuto-Tabacco, cap. 6 |
| 6 | 1.5 | Esempio: $2 \mapsto c$ nella tabella, $(2, f)$ in immagine e grafico (L02 p. 3) | $2 \mapsto c$ ovunque: $\operatorname{im}(f) = \{b, c, d\}$ | Incoerenza interna | – |
| 7 | 1.3 | "Applicazione della completezza" ferma a $\{q \in \mathbb{Q} : q^2 < 2\}$ (L02 p. 2) | Conclusione: il sup esiste in $\mathbb{R}$, è $\sqrt{2}$, non è razionale | Esempio interrotto | Canuto-Tabacco, cap. 1 |
| 8 | 1.8 | Potenza a esponente irrazionale: ramo con il sup vuoto; dominio di $x^{m/n}$ non detto (L04 p. 2) | Definizione completa per $x \in [0,1)$ e $x \ge 1$; dominio $[0, +\infty)$ per $n$ pari | Definizione incompleta | Canuto-Tabacco, cap. 2 |
| 9 | 2.2 | Divergenza a $-\infty$: "$a_n \in I_K(-\infty)$" (L05 p. 1) | $a_n \in I_{-K}(-\infty)$ | Coerenza con la definizione di intorno | – |
| 10 | 2.3 | Teorema sulle monotone: manca "altrimenti" nel caso decrescente; la dimostrazione usa $l - \varepsilon \le a_{n_\varepsilon}$ (L05 p. 2) | "altrimenti" aggiunto; $l - \varepsilon < a_{n_\varepsilon}$ | Con $\le$ si ottiene solo $\lvert a_n - l \rvert \le \varepsilon$ | – |
| 11 | 2.5 | Limiti all'infinito: solo $+\infty$ e il limite finito (L05 p. 3) | Tutti i casi, anche $\lim = -\infty$ e $x \to -\infty$ | Definizione incompleta | – |
| 12 | 2.7 | Limite dei polinomi "$a_n \cdot (+\infty$ se $n$ pari, $\pm\infty$ se dispari)" (L06 p. 1) | Per $x \to +\infty$: $\operatorname{sgn}(a_n) \cdot \infty$; per $x \to -\infty$ dipende dalla parità; lo stesso per $P/Q$ | Casi confusi | – |
| 13 | 3.2 | Dimostrazione degli zeri ferma al primo passo di bisezione (L06 p. 2) | Passo induttivo, successioni monotone, limite comune, continuità; unicità con l'iniettività | Dimostrazione interrotta | Canuto-Tabacco, cap. 4 |
| 14 | 3.2 | "$x_0$ è l'unica soluzione di $e^x + \sin x = 0$" (L07 p. 1) | Unica in $[-\pi/2, 0]$ | In $\mathbb{R}$ ci sono infinite soluzioni negative | – |
| 15 | 2.4 | Sottosuccessione senza la condizione sugli indici (L07 p. 1) | $(n_k)$ strettamente crescente | Senza la condizione la definizione è sbagliata | – |
| 16 | 3.4 | Weierstrass: $\bar{x} \in \mathbb{R}$, conclusione non scritta (L07 p. 2) | $\bar{x} \in [a, b]$ (l'intervallo è chiuso), quindi $f(\bar{x}) = M$ è il massimo | Serve la chiusura per usare la continuità in $\bar{x}$ | – |
| 17 | 4.4 | Derivata destra e sinistra senza "finito"; poi "derivata $= +\infty$" (L09 p. 1) | Limite finito; il caso infinito si chiama tangente verticale | Coerenza con la definizione di derivata | – |
| 18 | 4.4 | Esercizio con $\alpha$, $\beta$ senza conclusione (L09 p. 1-2) | $\beta = 1$ (continuità) e $\alpha = 1$ (derivate laterali uguali) | Esercizio interrotto | Conti rifatti |
| 19 | 4.5 | Fermat senza la conclusione $f'(x_0) = 0$ (L09 p. 2) | Conclusione aggiunta | Dimostrazione interrotta | – |
| 20 | 4.6 | Rolle, caso 2: "raggiunto in $x_0 \in [a, b]$" (L09 p. 3) | $x_0 \in (a, b)$, perché $f(a) = f(b)$ e $m < M$ | Fermat vale solo nei punti interni | – |
| 21 | 4.7-4.8 | Il limite della derivata (L09) è dimostrato con de l'Hôpital, enunciato dopo (L10) | De l'Hôpital in 4.7, limite della derivata in 4.8 | Ordine logico | – |
| 22 | 5.4 | Esempio $x^2$ convessa: "$x_2^2 - x_1^2 - 2x_1 x_2 = (x_1 - x_2)^2$" (L10 p. 2) | $x_2^2 - x_1^2 - 2x_1 x_2 + 2x_1^2 = (x_2 - x_1)^2 > 0$ | Passaggio algebrico sbagliato | Conti rifatti |
| 23 | 5.4 | "$f'$ crescente ⇒ $f$ convessa": la disuguaglianza (**) non è scritta (L10 p. 2) | Dimostrazione completa con Lagrange, nei due casi $x_1 < x_2$ e $x_1 > x_2$ | Dimostrazione incompleta | – |
| 24 | 5.6 | Taylor-Peano: l'ultimo passaggio è segnato come de l'Hôpital (L11 p. 1) | Sostituzione esplicita di $(T_{n,x_0}f)^{(n-1)}$, con la spiegazione | $f^{(n)}$ esiste solo in $x_0$, de l'Hôpital non si applica | – |
| 25 | 5.7 | Prodotto: manca $+\,o((x - x_0)^n)$ e la conclusione (L11 p. 3) | $T_{n,x_0}(fg)$ è il troncamento al grado $n$ di $T_{n,x_0}f \cdot T_{n,x_0}g$ | Passaggio incompleto | – |
| 26 | 3.7 | $f = O(g)$ definito con l'esistenza del limite (L08 p. 1) | Definizione tenuta; aggiunta una `[!nota]` con la definizione usuale | Convenzione del corso, più restrittiva | – |
| 27 | 1.8 | $\ln$ e $\log$ usati per la stessa funzione (lezioni e formulario) | $\ln$ ovunque, $\log_a$ per le altre basi | Notazione (`notazione.md`) | – |
| 28 | 5.6-5.7 | $Tf_{n,x_0}$, $T\ln(1+x)_{n,x_0}$ per lo sviluppo in 0 | $T_{n,x_0} f$; pedice 0 per gli sviluppi in 0 | Notazione | – |

## 2. Aggiunte

Le aggiunte valgono circa il 17% del corso: 18% nel modulo 1, 19% nel 2, 14% nel 3, 8% nel 4, 25% nel 5. In tutto sono 22 blocchi, misurati in parole rispetto all'intero modulo.

| Modulo, sezione | Aggiunta | ID | Fonte |
|---|---|---|---|
| 1.1 | $\sqrt{2}$ non è razionale; retta orientata e densità di $\mathbb{Q}$ | AM1A-01 | Canuto-Tabacco, cap. 1 |
| 1.4 | Principio di induzione con un esempio | AM1A-18 | Canuto-Tabacco, cap. 1 |
| 1.8 | Esponenziale e logaritmo: definizione, proprietà, grafici | AM1A-02, 06 | Canuto-Tabacco, cap. 2 |
| 1.8 | Funzioni trigonometriche dalla circonferenza unitaria | AM1A-02 | Canuto-Tabacco, cap. 2 |
| 1.8 | Inverse trigonometriche: intervalli di invertibilità, domini, immagini | AM1A-05, 06 | Canuto-Tabacco, cap. 2 |
| 1.9 | Traslazioni, dilatazioni, simmetrie, valore assoluto | AM1A-03 | Canuto-Tabacco, cap. 2 |
| 2.3 | $(1 + 1/n)^n$ è crescente e limitata | AM1A-08 | Canuto-Tabacco, cap. 3 e appendice |
| 2.5 | Limite destro e sinistro | AM1A-09 | Canuto-Tabacco, cap. 3 |
| 2.6 | Unicità del limite, permanenza del segno, confronto, algebra dei limiti con le regole per $\pm\infty$ | AM1A-09 | Canuto-Tabacco, cap. 4 |
| 2.8 | Dimostrazione di $\sin x / x \to 1$ | AM1A-09 | Canuto-Tabacco, cap. 4 |
| 2.9 | Forme $1^\infty$, $0^0$, $\infty^0$ con $f^g = e^{g \ln f}$ | AM1A-09 | Canuto-Tabacco, cap. 4 |
| 3.1 | Continuità delle funzioni elementari; tipi di discontinuità | AM1A-11 | Canuto-Tabacco, cap. 3 |
| 3.2 | Fine della dimostrazione degli zeri | AM1A-11 | Canuto-Tabacco, cap. 4 |
| 3.6 | Asintoti verticali | AM1A-15 | Canuto-Tabacco, cap. 5 |
| 3.7 | Regole di calcolo con l'o piccolo | AM1A-10 | Canuto-Tabacco, cap. 5 |
| 4.3 | Dimostrazione della derivata dell'inversa; arcsin' e arctan' | AM1A-12, 13 | Canuto-Tabacco, cap. 6 |
| 4.7 | Dimostrazione di de l'Hôpital (caso $0/0$ da destra) | AM1A-16 | Canuto-Tabacco, cap. 6 |
| 5.1 | Monotonia: dimostrazione di "⇐" e del punto 2 | AM1A-14 | Canuto-Tabacco, cap. 6 |
| 5.5 | Studio completo di $x e^{-x}$ | AM1A-15 | Canuto-Tabacco, cap. 6; *Calculus Problems* |
| 5.7 | Sviluppi di $\cos x$, $(1+x)^\alpha$, $\frac{1}{1-x}$, $\arctan x$ | AM1A-17 | Canuto-Tabacco, cap. 7 |
| 5.7 | Quoziente e composizione degli sviluppi | AM1A-17 | Canuto-Tabacco, cap. 7 |
| 5.8 | Applicazioni: limiti, ordine di infinitesimo, natura dei punti critici | AM1A-17 | Canuto-Tabacco, cap. 7 |

I numeri di capitolo del Canuto-Tabacco vengono dalla struttura del libro e vanno controllati sull'edizione in uso. Nel prodotto finale le fonti spariscono insieme ai marcatori (fase 8).

## 3. Correzioni di lingua e di forma, per modulo

In tutti i moduli valgono le stesse correzioni:

- le abbreviazioni sono state sciolte ("t.c.", "p.to", "Th", "Dim", "Oss", "$\exists_0$", "B-W");
- gli elenchi di appunti sono diventati prosa;
- definizioni ed enunciati sono in callout, la notazione è uniforme (`notazione.md`);
- sono stati tolti il disegno e il "ho vinto" della L06, i disegni della L07 e della L10, l'espressione volgare della L08, la riga di Reti Logiche della L03 e i rimandi a pagine e appendici del libro.

Per modulo:

- **Modulo 1:** gli esempi di L02 e L04 sono riscritti con i conti per esteso. La tabella incompleta di immagini e controimmagini è diventata un esempio svolto.
- **Modulo 2:** l'esempio $\varepsilon$-$B$ di L05 è tenuto per intero, con la scelta di $B$ motivata.
- **Modulo 3:** gli esempi di L07 (zeri, valori intermedi, controesempi) sono riordinati per teorema.
- **Modulo 4:** le derivate elementari di L08 e L09 sono raccolte in un unico paragrafo, con i conti.
- **Modulo 5:** lo schema dello studio di funzione di L10 è diventato un elenco ordinato, seguito dall'esempio completo.

## 4. Figure

Le 19 figure, segnate `[!figura]` nei moduli, sono ridisegnate al computer in `figure/` (SVG, adatte al PDF in A4). Sono tutte grafici o schemi fatti ex novo: nessuna viene dal materiale del docente.
