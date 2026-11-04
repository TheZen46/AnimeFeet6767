# Analisi Matematica 1B · registro delle correzioni e delle aggiunte

Fasi 4 e 5, svolte il 4 novembre 2026. Testo di partenza: le dispense `trascrizione/D1`…`D4`, controllate sulle lezioni a mano (`L`). Tutti i conti dei moduli sono verificati con `strumenti/verifica.py` (calcolo simbolico).

## 1. Correzioni di sostanza

| # | Modulo, sezione | Prima | Dopo | Motivo |
|---|---|---|---|---|
| 1 | 4.8 | Esempio dell'autovalore carente con $A = \begin{pmatrix} 1&1&0\\0&0&1\\-1&3&-1 \end{pmatrix}$ e $P(\lambda) = -\lambda(\lambda-2)^2$, segnato "VERIFICARE" (D4 § 5.2.2) | Esempio nuovo con $A = \begin{pmatrix} 0&1&0\\0&0&1\\0&-4&4 \end{pmatrix}$, autovettore $(1,2,4)$ e generalizzato $(0,1,4)$ | La matrice data ha $P(\lambda) = -\lambda^3 + 4\lambda - 4$; i conti successivi non tornano |
| 2 | 4.3 | Unicità per le separabili "se $h \in C^1$ e $h(y_0) \neq 0$"; domini di $g$ e $h$ scambiati (D4 teorema 3.1) | "se $h \in C^1$ (o localmente lipschitziana), e anche se $h(y_0) \neq 0$" | La condizione era più restrittiva del necessario |
| 3 | 4.3 | Soluzione di Peano "$\frac{2}{3}t^{3/2}$" [lettura dell'estrazione] (D4 es. 3.4) | $\left(\frac{2t}{3}\right)^{3/2}$, con la famiglia di soluzioni raccordate | Solo questa risolve $y' = \sqrt[3]{y}$ |
| 4 | 1, esercizio 2 | $\frac{1}{x^2 \sin x}$ "di ordine 4" [lettura] (L06 p. 1) | Ordine 3 | $\sin x \sim x$ |
| 5 | 1.4 | Integrabili "le funzioni continue (anche a tratti)" (D1 § 3.3) | Le continue, le limitate con un numero finito di discontinuità, le monotone | Serve la limitatezza |
| 6 | 2.4 | Criteri del rapporto e della radice con le conclusioni ripetute (D2 § 4.4) | Un solo enunciato, con il caso $L = 1$ commentato | Residuo |
| 7 | 2.4 | Criterio integrale con una sola catena di disuguaglianze, senza dimostrazione esplicita (D2 § 4.3) | Dimostrazione con $f(n+1) \le \int_n^{n+1} f \le f(n)$ e la stima del resto | Precisazione |
| 8 | 3.2 | Definizione di insieme connesso illeggibile (D3 § 2.3) | Riscritta | Formula persa |
| 9 | 3.4 | – | Detto che la maggiorazione in polari deve essere uniforme in $\theta$, con il controesempio $\frac{x^2 y}{x^4 + y^2}$ | È l'errore più frequente all'esame |
| 10 | 4.1 | Legge oraria della caduta con attrito resa in modo illeggibile dall'estrazione (D4 § 1.1) | $y = h_0 - \frac{mg}{k}t + \frac{m^2 g}{k^2}(1 - e^{-kt/m})$, verificata | – |
| 11 | 4.3 | Logistica con $y(0) = 2$ senza dominio della soluzione (D4 es. 3.3) | Definita per $t > -\frac{\ln 2}{2}$ | Il denominatore si annulla |

## 2. Correzioni di forma

- Tolti ~390 rimandi `[cite: …]`, due numeri di matricola, le didascalie di figure mai disegnate e la descrizione di un disegno a margine.
- Notazione uniformata (`notazione.md`); sistemi scritti $f(t, y)$.
- Testo riformulato in prosa in tutti i moduli, senza riprendere le frasi delle dispense.
- Tre figure ridisegnate (`figure/`): somme di Riemann, criterio integrale, curve di livello di paraboloide e cono.

## 3. Aggiunte

| Modulo, sezione | Aggiunta | ID | Fonte |
|---|---|---|---|
| 1.1 | Primitive su insiemi che non sono intervalli; funzione senza primitive | AM1B-01 | Canuto-Tabacco, *Analisi Matematica 1* |
| 2.5 | Dimostrazione della convergenza assoluta; idea della dimostrazione di Leibniz e la serie $\sum \frac{(-1)^n}{n}$ | AM1B-02 | Canuto-Tabacco, *Analisi Matematica 1* |
| 3.5 | Funzione derivabile ma non continua | AM1B-03 | Canuto-Tabacco, *Analisi Matematica 2* |
| 3.6 | Significato del gradiente, ortogonalità alle curve di livello | AM1B-04, 05 | Canuto-Tabacco, *Analisi Matematica 2* |
| 4.6 | Equazione di ordine $n$ come sistema | AM1B-09 | Canuto-Tabacco, *Analisi Matematica 2* |
| 4.8 | Autovalori complessi nei sistemi | AM1B-11 | Canuto-Tabacco, *Analisi Matematica 2* |

Esercizi svolti nuovi (applicano solo il testo): modulo 1, esercizi 3-4; modulo 2, esercizi 3-5; modulo 3, esercizi 2-3; modulo 4, esercizi 1-4. Gli altri esempi ed esercizi vengono dalle dispense o dalle lezioni (L06, L08, L15, L23).
