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

Gli appunti a mano delle esercitazioni (`Appunti Esercitazioni_compressed`, 70 pagine, esercitazioni 1 e 3-12) sono trascritti in `trascrizione/E - esercitazioni 2025 (appunti a mano).md`, con le note di revisione fra parentesi quadre. Le soluzioni degli appunti sono state confrontate con quelle dei moduli e con i risultati ufficiali delle esercitazioni.

| Dove | Che cosa | ID |
|---|---|---|
| Modulo 2, "Altri esercizi delle esercitazioni" | Esercizi 9-10: angolo limite su un piano scabro; blocchetti sovrapposti su un piano inclinato | FG1-01 |
| Modulo 3, "Altri esercizi delle esercitazioni" | Esercizi 12-19: attrito variabile lungo il piano; molla su piano inclinato con legge oraria; blocco, molla e carrucola; tensione del pendolo e distacco del filo; distacco da una cupola; quattro molle a croce; guida mobile; cuneo mobile | FG1-02, FG1-04 … FG1-06 |
| Modulo 4, "Altri esercizi delle esercitazioni" | Esercizi 13-17: cono e disco forato; ribaltamento di un cubo; sbarra su due ruote (gennaio 2019); Atwood con molla (settembre 2017); disco, cuneo e freno (luglio 2024) | FG1-03 |

### Confronto fra appunti a mano, ricalcolo e risultati ufficiali

| Esercizio | Appunti | Ricalcolo | Risultato ufficiale | Scelta |
|---|---|---|---|---|
| ES3-4, accelerazione dei blocchetti | 0,73 m/s² | 0,73 m/s² | 0,75 m/s² | 0,73, con il valore ufficiale fra parentesi (differenza di arrotondamento di $g$ e degli angoli) |
| ES6-2, attrito nel punto più basso | 9,06 N | 9,3 N con $d$ non arrotondato | 9,06 N | 9,3 N, con il valore ufficiale fra parentesi |
| ES7-2, inversione del coseno | $\cos^{-1}(1/3)$ | $\cos^{-1}(-1/3) = 109{,}5°$ | 109,5° | segno corretto |
| ES8-2, velocità iniziale | $v_0 = v_A\sin\theta_A$ | $v_0 = v_A\cos\theta_A$ | — | componente orizzontale corretta |
| ES9-2, coefficiente statico | 0,57 | 0,577 ($\tan30°$) | 0,58 | arrotondamento |
| ES9-3, spostamento | −58 mm | −58 mm | "(- 8 mm, 1.7 mm)" nel testo estratto | probabile cifra persa nell'estrazione del testo ufficiale; esercizio non usato |
| ES9-2, velocità in C | 2,55 m/s | 2,55 m/s | 2,6 m/s | arrotondamento |
| ES12-14, posizione minima sulla sbarra | $\frac{M}{2ML}$ in un passaggio | $\frac{M}{2m_1}$ | — | refuso degli appunti, risultato 0,55 m giusto; esercizio non usato |
| ES12-1, momento angolare | $33\cdot10^{-3}$ kg m²/s | — | $3{,}3\cdot10^{-4}$ kg m²/s | lettura incerta degli appunti; esercizio non usato |
| ES12-18, giri prima dell'arresto | 1,76 | 1,78 | 1,76 | 1,78, con il valore ufficiale fra parentesi |

Le letture incerte (ES9-5 $\mu_D = 0{,}8$, ES11-3 $\mu_s = 0{,}5$, parti di ES12-2 e ES12-4) sono segnate nella trascrizione; gli esercizi che le contengono non sono stati usati se non confermati dal testo ufficiale. Controlli: `strumenti/verifica_ampliamento.py`, 119 controlli.
