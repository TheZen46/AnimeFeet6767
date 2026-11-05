# Statistica · fase 1: inventario e integrità

Corso: Statistica (6 CFU, 1° anno, 2° semestre). Programma di riferimento: `revisione/programmi/statistica.md` (UniGe 2026/27).
Originali: cartella `Statistica/` sul computer dell'autore. Nessun originale è stato modificato.

## 1. File e uso

| File | Pagine | Tipo | Uso |
|---|---|---|---|
| `Appunti_mano/Lezione 01…07` | 7 fogli | a mano (tablet), una pagina fitta per lezione | Base del modulo 1 (lezioni 1-4); controllo delle lezioni 5-7 |
| `_da_verificare/Lezioni iPad/` (9 file) | 106 | a mano (iPad), lezioni 5-22 | Base dei moduli 2-4 |
| `Formulari e riassunti/Formulario.pdf` | 3 di 4 | a mano | Boxplot, retta dei minimi quadrati (modulo 1), riepilogo di probabilità |
| `Formulari e riassunti/Formulario totale.pdf` | 1 | a mano | Indice degli argomenti, controllo della copertura |
| `Rielaborazioni/probabilità.pdf`, `formulars Prob.pdf`, `fofumenfo.pdf` | 10, 5, 19 | battute (LaTeX) | Riassunti delle stesse lezioni: controllo delle formule |
| `Materiale del docente/` (prova parziale del 28/05/2025 con soluzione, tavole) | 22 | del docente | Solo consultazione: argomenti d'esame, valori delle tavole |
| `_da_verificare/Note_261103_173456.pdf` | 3 | – | Pagine bianche |

Due file della cartella `_da_verificare/` sono stati esclusi su indicazione dell'autore e non sono stati aperti.

Le due serie di appunti a mano sono di due dispositivi diversi; l'autore ha confermato che sono tutte sue. Le lezioni 5-7 sono in tutte e due: la serie iPad è più completa e si è seguita quella.

L'indice dettagliato delle lezioni, con gli argomenti e gli esempi nell'ordine degli appunti, è in `trascrizione/L - indice delle lezioni.md`.

### Lezioni mancanti

Gli appunti coprono le lezioni dal 25/02 al 14/05/2026 (22 lezioni). Mancano:

- la lezione sulla **regressione lineare** (c'è solo nel formulario a mano, senza esempi);
- tutte le lezioni dopo il 14/05: **test di ipotesi**, confronto fra medie, test chi-quadro, **ANOVA**. Il test sulla media è nella prova parziale del docente, quindi è stato fatto a lezione.

## 2. Problemi tecnici

| Livello | Dove | Problema | Correzione |
|---|---|---|---|
| DA CORREGGERE | `Appunti_mano/Lezione 06` | Data 11/02/2026 nel nome del file: il contenuto è la lezione 6 dell'11/03 | Data corretta nell'indice |
| DA CORREGGERE | Serie iPad, L07 e L08 | Stessa data (18/03/2026) su due lezioni diverse | Segnalato; non incide sui moduli |
| DA CORREGGERE | Serie iPad, L06 | Tabella del problema dei compleanni incollata da un'altra fonte | Non ripresa: la tabella del modulo 2 è ricalcolata |
| DA CORREGGERE | Dispense battute | "Spazio per il grafico", "Figura N" senza figura | Le figure utili sono ridisegnate (5) |
| NOTA | Serie A | Grafia molto fitta, letta a 190 dpi | – |
| NOTA | Serie iPad | Diversi grafici a mano | Ridisegnati quelli necessari, gli altri resi a parole |

## 3. Errori di sostanza trovati

| Livello | Dove | Negli appunti | Corretto |
|---|---|---|---|
| DA CORREGGERE | L05 (in tutte e due le serie) | Dado, $E$ = pari, $F$ = primo: "$E \cup F = \Omega$, evento certo", $P[E \cup F] = 1$ | $E \cup F = \{2, 3, 4, 5, 6\}$ (manca l'1), $P = \frac56$ |
| DA CORREGGERE | L14, urna di monete | $\mathbb{E}[X] = \frac{9 + 4}{10} = \frac{13}{20}$ | $\frac{13}{10}$ |
| DA CORREGGERE | L17, uniforme continua | $F(x) = \frac{x - a}{b - a}$ su $[a, b]$, "0 altrove" | 0 per $x < a$, 1 per $x > b$ |
| DA CORREGGERE | L19, altezze | $\delta = \sigma \varphi_{0,75} = 5{,}46$ | $8 \cdot 0{,}6745 \approx 5{,}40$ cm |
| DA CORREGGERE | L21, pesci | Numerosità $n = 245$ | $245{,}2$, quindi $n = 246$ (si arrotonda per eccesso) |
| DA CORREGGERE | L22, moneta | Per il livello del 90%: "$\alpha = 5\%$, $\alpha/2 = 0{,}025$, $z = 1{,}645$" | $\alpha = 10\%$, $\alpha/2 = 0{,}05$ (il valore 1,645 è giusto) |
| DA CORREGGERE | L15, urna di monete | Domanda b) "sapendo che sono uscite 3 teste", calcolo con 2 teste | Domanda riscritta con 2 teste |
| DA CORREGGERE | L12 | Densità uguale a 1 (invece di 0) fuori dall'intervallo, due volte | 0 |
| DA CORREGGERE | L16 | "$N \sim \mathrm{Pascal}(\lambda)$" nella somma di Poisson | Poisson |
| DA CORREGGERE | L04 | Mediana scritta "58" (confusa con la frequenza cumulata 58%) | 8 |
| NOTA | L20 | $z_{0,005} = 2{,}56$ nella tabella | $2{,}576$ |
| NOTA | L14 | Chebyshev: "$\sigma = \mathrm{VAR}[X]$" | $\sigma^2 = \mathrm{Var}[X]$ |
| NOTA | L19 | "$P[\lvert Z\rvert > -1{,}25]$" | $P[\lvert Z\rvert > 1{,}25]$ |

Tutti gli esempi dei moduli sono stati ricalcolati con `strumenti/verifica.py` (157 controlli, nessun errore): probabilità esatte con frazioni, integrali con sympy, valori della normale, della t, della chi-quadro e della F con scipy.

## 4. Rischi per la vendita

| Livello | Rischio | Cosa fare |
|---|---|---|
| DA CORREGGERE | `fofumenfo.pdf` riporta un numero di matricola nel frontespizio | Non usato né citato nei moduli |
| DA CORREGGERE | Le dispense battute sono state scritte con uno strumento di scrittura assistita (frasi di servizio, segnaposto delle figure) | Usate solo per controllo; i moduli sono scritti dagli appunti a mano |
| NOTA | Materiale del docente (prova d'esame, tavole) | Non copiato: consultato per gli argomenti e per i valori critici, che sono ricalcolati |
| NOTA | Nei moduli nessun nome di docenti o compagni; il nome del produttore di mele della prova d'esame non è ripreso | – |
