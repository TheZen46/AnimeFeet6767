# Fisica Generale 1 · fase 1: inventario e integrità

Corso: Fisica Generale 1 (6 CFU, 1° anno, 2° semestre). Programma di riferimento: `revisione/programmi/fisica-generale-1.md`. La pagina ufficiale non pubblica un programma: gli argomenti FG1-01…03 vengono dagli obiettivi, FG1-04…07 sono stati aggiunti dalle lezioni.
Originali: cartella `Fisica 1/` sul computer dell'autore. Nessun originale è stato modificato.

## 1. File e uso

| File | Pagine | Tipo | Uso |
|---|---|---|---|
| `Appunti_mano/Lezione 01…19` (18 file) | 44 | a mano | Inventario e copertura (`trascrizione/`) |
| `Rielaborazioni/FISICA1.pdf` | 31 | battuta (~10.000 parole) | Base dei quattro moduli |
| `Rielaborazioni/fisica1es1.pdf`, `fisica1es2.pdf` | 8 + 8 | battute, guide di formule | Controllo (equilibrio del corpo rigido) |
| `Formulari e riassunti/Elaborazione formulario.pdf` | 3 | a mano | Controllo |
| `Esercizi/` (3 file) | 19 | a mano, esercizi svolti | Non usati nei moduli (domanda 2) |

L'indice delle lezioni è in `trascrizione/L - indice delle lezioni.md`.

### Lezioni mancanti

Manca la **lezione 18** (fra il 05/05 e il 12/05/2026). Il corso finisce con la lezione 19 del 12/05; se ci sono state lezioni dopo, non sono fra gli appunti.

## 2. Problemi tecnici

| Livello | Dove | Problema | Correzione |
|---|---|---|---|
| DA CORREGGERE | `FISICA1.pdf` | Molte "Figura N" descritte a parole ma non disegnate | Due figure ridisegnate (traiettorie del proiettile, rotolamento); le altre rese nel testo |
| DA CORREGGERE | `fisica1es1.pdf` | Rimandi `[cite: …]` rimasti nel testo | Non ripresi |
| NOTA | `FISICA1.pdf` | Note fra parentesi sul confronto con gli appunti a mano ("negli appunti è riportato…") | Risolte nel testo, vedi § 3 |

## 3. Errori di sostanza trovati

| Livello | Dove | Negli appunti o nella dispensa | Corretto |
|---|---|---|---|
| DA CORREGGERE | dispensa § 8.2.1, teorema del momento angolare | La dimostrazione arriva a $\frac{dL_\Omega}{dt} = \tau_\Omega - v_\Omega \times p$, ma l'enunciato e l'ultima riga scrivono $+ v_\Omega \times p$ | $\tau_\Omega - v_\Omega \times p$ |
| DA CORREGGERE | lezione 5 (segnalato nella dispensa) | Forza per accelerare l'auto: $1{,}1 \cdot 10^4$ N | $2{,}08 \cdot 10^3$ N |
| DA CORREGGERE | lezioni (segnalato nella dispensa) | $g \approx 9{,}5$ m/s² | $9{,}8$ m/s² |
| DA CORREGGERE | lezione 15 (segnalato nella dispensa) | Momento d'inerzia dell'asta con $l^3$; della sfera con $R^3$ | $\frac{1}{12}Ml^2$, $\frac25 MR^2$ |
| NOTA | dispensa § 6.2.1 | Unità di $\alpha$ nella densità dell'asta scritta "m²" negli appunti | $\mathrm{m^{-1}}$ |
| NOTA | dispensa § 5.1 | Dimostrazione dell'equivalenza fra le due definizioni di forza conservativa resa in modo confuso | Riscritta |

Gli esempi della dispensa ripresi nei moduli e quelli nuovi sono stati ricalcolati con `strumenti/verifica.py` (72 controlli, nessun errore).

## 4. Rischi per la vendita

| Livello | Rischio | Cosa fare |
|---|---|---|
| NOTA | La dispensa battuta e le due guide sono state scritte con uno strumento di scrittura assistita (rimandi `[cite]`, figure solo descritte) | Il testo dei moduli è riscritto |
| NOTA | Nessun nome di docenti o compagni nei moduli | – |
