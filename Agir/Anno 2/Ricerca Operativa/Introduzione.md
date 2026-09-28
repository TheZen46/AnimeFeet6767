Ricerca operativa <- Operational research / Operations research
anche nota come
Teoria delle decisioni <- Management science

È la disciplina che studia lo sviluppo e l'applicazione di metodi scientifici per la soluzione di **problemi di decisione**

## Problemi di decisione (oggi)
- Alta dimensionalità (tante variabili)
- Alta complessità
- Decisioni complesse

### Approccio quantitativo
- Sviluppo del modello
- Algoritmi per la soluzione

# Storia
Regno Unito, 1936
	Viene fondata la Bawdsey Research Station
		Esperimenti sui radar
1937
	Posizionamento nuovi radar
1938
	Report menziona la parola RO
1941
	Nasce la "operational research section"

Oggi viene utilizzata per la gestione e l'utilizzo efficiente di risorse scarse

^Esempio
Dantzig, 1986
70 lavoratori, 70 lavori ^77438c

La tabella indica il tempo impiegato da ogni lavoratore ($R_n$) per svolgere uno specifico lavoro ($C_n$)

|          | $L_1$ | $L_2$ | $\dots$ | $L_{70}$ |
| -------- | ----- | ----- | ------- | -------- |
| $R_1$    | 1     | 10    |         |          |
| $R_2$    | 3     | 1     |         |          |
| $\vdots$ |       |       |         |          |
| $R_{70}$ | 9     | 7     |         |          |
$70!$ possibilità ($\sim 10^{100}$)

$\begin{array}{c}\fbox{Analisi del problema} \\\mskip{15mu}\downarrow\star \\\fbox{Costruzione del modello} \\\downarrow \\\fbox{Analisi del modello} \\\downarrow \\\fbox{Soluzione numerica del modello}& \rightarrow \text{Soluzioni approssimate} (\text{e.g.}\ Ax=b\Rightarrow x=A^{-1}b)\\\downarrow\\\mskip{34mu}\fbox{Validazione}\rightarrow\star\end{array}$


Modelli di RO: modelli astratti di tipo matematico
Descrivono problemi di decisione con:
1) **Variabili**
2) **Funzione obiettivo** da minimizzare o massimizzare
3) **Vincoli** (relazioni tra le variabili) $\rightarrow$ equazioni, disequazioni

Applicazioni tradizionali RO
- Industriali
	- Pianificazione produzione
	- Gestione ottima risorse (e.g. magazzini) 
	- Localizzazione degli impianti
- Progettazione
	- Reti
	- Strutturale
- Organizzazione
	- Turni personale
	- Project planning
	- Manutenzione beni
	- Instradamento veicoli
	- Liste di attesa (ambito sanitario)
	- Localizzazione ambulanze
- Problemi scientifici
	- Diagnostica per immagini

Temi attuali
- AI (ML)
- Mercato dell'energia
- Logistica
