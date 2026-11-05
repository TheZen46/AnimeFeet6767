# Fisica Generale 1 · registro delle correzioni e delle aggiunte

Ogni esempio dei moduli è stato ricalcolato con `strumenti/verifica.py`. Qui sono elencate le correzioni di sostanza, gli esempi costruiti per i moduli e le aggiunte.

## Correzioni di sostanza

| # | Modulo | Dove | Prima | Dopo | Motivo | Fonte |
|---|---|---|---|---|---|---|
| 1 | 4 · 4.6 | dispensa § 8.2.1 | $\frac{dL_\Omega}{dt} = \tau_\Omega + v_\Omega \times p$ | $\tau_\Omega - v_\Omega \times p$ | Errore di segno nell'enunciato: la dimostrazione dà il segno meno | `verifica.py` |
| 2 | 2 · 2.1 | L05 | $F \approx 1{,}1 \cdot 10^4$ N per l'auto | $2{,}08 \cdot 10^3$ N | Errore numerico negli appunti (già segnalato nella dispensa) | `verifica.py` |
| 3 | tutti | lezioni | $g \approx 9{,}5$ m/s² | $9{,}8$ m/s² | Valore standard | – |
| 4 | 4 · 4.2 | L15 | Momenti d'inerzia dell'asta e della sfera con esponenti 3 | $\frac{1}{12}Ml^2$, $\frac25 MR^2$ | Controllo dimensionale e integrazione | `verifica.py` |
| 5 | 3 · 3.5 | dispensa § 6.2.1 | Unità di $\alpha$ "m²" | $\mathrm{m^{-1}}$ | $\alpha x$ deve essere un numero puro | Controllo dimensionale |
| 6 | 3 · 3.2 | dispensa § 5.1 | Equivalenza delle definizioni di forza conservativa | Riscritta | Passaggi confusi | – |

## Esempi costruiti per i moduli

La dispensa ha pochi esempi numerici; questi sono stati scritti per i moduli, sugli argomenti delle lezioni:

| Modulo | Esempi |
|---|---|
| 1 | Frenata di un'auto; lancio a 30° con gittata e altezza massima; disco che fa due giri al secondo; barca che attraversa il fiume; legge oraria da un'accelerazione variabile |
| 2 | Valori numerici per le due scatole e i piani inclinati; giro della morte con $R = 1$ m; molla e pendolo; piano inclinato con massa appesa; ascensore; curva piana |
| 3 | Molla da 200 N/m; caduta da 5 m; equilibri di $U = x^3 - 3x$; potenza di un'auto; fucile; urti fra carrelli; molla che lancia un blocco; pendolo balistico; esplosione |
| 4 | Atwood con valori numerici; pattinatrice; trave appoggiata; disco tirato da una fune; gara fra sfera e cilindro; momento angolare in moto rettilineo |

## Aggiunte

Nessun blocco `[!aggiunta]`: gli argomenti trattati sono tutti negli appunti (`01-copertura.md`). La gravitazione universale e la legge di Hooke, usate nel modulo 2, sono negli appunti.

## Ampliamento del 5 novembre 2026

Dopo le risposte alle domande (`revisione/AMPLIAMENTO-ANNO-1.md`): FG1-1 nessun appunto delle lezioni mancanti, ma nel materiale nuovo ci sono gli appunti a mano delle esercitazioni (70 pagine) e i testi delle 12 esercitazioni del 2025; FG1-2 sì a un'appendice completa di esercizi, anche d'esame.

| Dove | Che cosa | ID |
|---|---|---|
| Moduli 1-4, "Esercizi dalle esercitazioni" | 23 esercizi (più un guidato) delle esercitazioni 1, 3, 4, 5, 6, 8, 10, 11 (testi riformulati, risultati confrontati con quelli ufficiali): caduta e incontri, tempi minimi, leggi orarie, piani inclinati con attrito, pendolo conico, molle in serie e in parallelo, lavoro lungo percorsi diversi e conservatività, catena, urti elastici e obliqui, urto con molla, statica di travi e scale, momenti d'inerzia, pulegge, rotolamento, oscillazioni con carrucola | FG1-01 … FG1-07 |
| Moduli 1-4, "Esercizi sul modello delle prove d'esame" | 6 esercizi nuovi sul modello delle prove del 2025-2026 (leggi orarie, oscillatori, massa che ruota su una molla, molla e piano inclinato, biglia colpita dalla stecca, asta che urta una massa) | FG1-01 … FG1-07 |
| Moduli 1-4 | 12 esercizi guidati e un formulario per modulo | tutti |

FG1-3 (programma del docente) è rimasta senza risposta: gli ID del programma restano quelli ricavati dalle lezioni.

Gli appunti a mano delle esercitazioni (`Appunti Esercitazioni_compressed`, 70 pagine) non sono ancora stati trascritti: gli esercizi seguono i testi delle esercitazioni corrispondenti, con soluzioni scritte per esteso e controllate sui risultati ufficiali. La trascrizione degli appunti, per riprenderne i passaggi e le figure, è il prossimo passo per questo corso. Controlli: `strumenti/verifica_ampliamento.py`, 83 controlli.
