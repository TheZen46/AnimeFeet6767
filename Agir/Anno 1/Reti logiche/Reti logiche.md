Reti logiche = Reti combinatorie + Reti sequenziali (basati su flip-flop)

Flip-flop
	Registri
	Contatori

Data rete sequenziale:
	Analisi
	Sintesi

## F-F PET (Flip-Flop Positive Edge Triggered)
Agiscono quando il clock presenta un fronte positivo
Sono tipi di F-F PET:
	D Flip-Flop
	JK Flip-Flop
### D Flip-Flop
| D   | Q   |
| --- | --- |
| 0   | 0   |
| 1   | 1   |

### JK Flip-Flop
| J   | K   | Q                    |
| --- | --- | -------------------- |
| 0   | 0   | $Q_{t-1}$            |
| 0   | 1   | 0                    |
| 1   | 0   | 1                    |
| 1   | 1   | $\overline{Q_{t-1}}$ |
### Preset
$\overline{PR}\longrightarrow$ forza il F-F allo stato '1' quando attivato (attivo basso)

### Clear
$\overline{CL}\longrightarrow$ forza il F-F allo stato '0' quando attivato (attivo basso)

# Temporizzazioni
![[Temporizzazione.png]]
$t_s\rightarrow$ tempo di setup (min)
$t_h\rightarrow$ tempo di hold (min)
$t_p\rightarrow$ tempo di propagazione
	$t_{PHL}\rightarrow$ tempo di propagazione alto-basso
	$t_{PLH}\rightarrow$ tempo di propagazione basso-alto
$t_W\text{ (W=width)}\rightarrow$ ampiezza dell'impulso (min)

$\frac{1}{t_{min}}\rightarrow$ frequenza massima del clock

# Analisi
![[JK; D.png]]
![[JK; D (TD).png]]

# Analisi combinatoria-sequenziale
![[D2; D1; D0.png]]

![[D2; D1; D0 (TD).png]]
$X=Q_1\oplus Q_2$
$D_2=X\oplus \text{Seed}$


![[Pasted image 20251105101354.png]]
![[!D xor D (TD).png]]

# Blocchi costitutivi delle reti sequenziali

## Registri
### PIPO
Parallel Input Parallel Output
![[PIPO.png]] SISO

### SISO
Serial Input Serial Output
![[SISO.png]]

Usato nei cavi (USB)

### SIPO
Serial Input Parallel Output
![[SIPO.png]]
Per cambiare lo scorrimento ($\leftarrow$ al posto di $\rightarrow$)
### PISO
Parallel Input Serial Output
![[PISO.png]]

### Registro Universale
![[Universale.png]]

| $S_0$ | $S_1$ | Reg                    |
| ----- | ----- | ---------------------- |
| 0     | 0     | Memorizza              |
| 0     | 1     | Spostamento a destra   |
| 1     | 0     | Spostamento a sinistra |
| 1     | 1     | Caricamento parallelo  |
# Contatore
## In avanti
| Q3  | Q2  | Q1  | Q0  | n   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 1   | 1   |
| 0   | 0   | 1   | 0   | 2   |
| 0   | 0   | 1   | 1   | 3   |
| 0   | 1   | 0   | 0   | 4   |
| 0   | 1   | 0   | 1   | 5   |
| 0   | 1   | 1   | 0   | 6   |
| 0   | 1   | 1   | 1   | 7   |
| 1   | 0   | 0   | 0   | 8   |
| 1   | 0   | 0   | 1   | 9   |
| 1   | 0   | 1   | 0   | 10  |
| 1   | 0   | 1   | 1   | 11  |
| 1   | 1   | 0   | 0   | 12  |
| 1   | 1   | 0   | 1   | 13  |
| 1   | 1   | 1   | 0   | 14  |
| 1   | 1   | 1   | 1   | 15  |
![[Contatore (in avanti).png]]
![[Contatore (Registro Parallelo).png]]