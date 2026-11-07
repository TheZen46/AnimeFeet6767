# Modulo 1 — Lezione 3: Cercare e trasformare testo

> Corso "Università CyberSecurity" · Modulo 1 *Fondamenti* · Lezione 3 di 10
> In questa cartella: `Lezione.md` (questo testo), `Soluzioni.md` (da aprire solo dopo aver provato), `setup_sfida.sh` (prepara la mini-CTF dell'Esercizio 14).

## 0. Obiettivi, prerequisiti, ripasso, piano

**Al termine della lezione sarai in grado di:**

1. spiegare che cos'è un file di testo a livello di byte (righe, terminatori, `\r\n` di Windows, byte contro caratteri) e perché questo cambia il risultato dei comandi;
2. leggere e scrivere espressioni regolari nelle tre varianti che incontrerai (POSIX di base, POSIX estese, PCRE), e prevedere che cosa corrisponde;
3. spiegare come funziona un motore di espressioni regolari e perché alcune espressioni possono richiedere un tempo esponenziale (ReDoS);
4. usare con sicurezza `grep`, `tr`, `cut`, `sort`, `uniq`, `comm`, `sed`, `awk` e `strings`, conoscendo il modello di funzionamento di ciascuno e non solo qualche opzione;
5. comporre questi strumenti in catene che risolvono problemi tipici delle gare: estrarre una flag da un file enorme, analizzare un log, contare frequenze, decodificare un ROT13, trovare stringhe in un binario.

**Prerequisiti:** Lezioni 1 e 2. In particolare: virgolette ed espansioni (L1 §7–8), globbing (L1 §8.7, L2 §13), `find` (L2 §14), tipi di file e `od` (L2 §11).

**Tempo:** circa 4 ore di lettura e prove al terminale, 3–4 ore di esercizi.

**Ripasso dalle lezioni precedenti.**
- Il **globbing** è fatto dalla shell sui **nomi di file**; le **espressioni regolari** di questa lezione sono interpretate dai **programmi** (`grep`, `sed` …) sul **contenuto**. Usano simboli simili con significati diversi: `*` nel glob è "qualunque stringa", nelle regex è "zero o più volte l'elemento precedente". Per questo un'espressione regolare va **sempre** messa tra virgolette singole, così la shell non la tocca (L1 §7).
- Un file è una sequenza di byte senza struttura per il kernel (L2 §1.1). "Testo" è un'interpretazione di quei byte.
- `find` trova i file per nome e proprietà (L2 §14); questa lezione insegna a cercare **dentro** i file.

**Una nota sulle pipe.** In questa lezione useremo spesso l'operatore `|`, che collega l'output di un comando all'input del successivo: `comando1 | comando2`. Lo studieremo a fondo nella Lezione 4; per ora basta sapere che `cat f | grep x` fa passare il contenuto di `f` attraverso `grep`. I programmi di questa lezione sono **filtri**: se non ricevono nomi di file, leggono lo standard input e scrivono sullo standard output, ed è proprio questo che li rende componibili (L1 §1, la filosofia di McIlroy).

**Convenzione tipografica.** Come nelle lezioni precedenti. Negli schemi, `␊` indica il byte a capo (`\n`, 0x0a) e `␍` il ritorno carrello (`\r`, 0x0d), quando serve renderli visibili.

**Piano della lezione.**

| Parte | Sezioni | Domanda a cui risponde |
|---|---|---|
| I. Il testo come dato | 1–2 | Che cos'è una riga? Come guardo un file senza farmi ingannare? |
| II. Le espressioni regolari | 3–6 | Come descrivo un insieme di stringhe? Come funziona il motore? |
| III. Gli strumenti | 7–13 | `grep`, `tr`, `cut`, `sort`, `uniq`, `sed`, `awk`, `strings` |
| IV. Composizione e sicurezza | 14–15 | Come si combinano? Dove si nascondono i pericoli? |
| V. La pratica | 16–21 | Esempi svolti, esercizi, autoverifica, riepilogo, fonti |

---

# Parte I — Il testo come dato

## 1. Che cos'è un file di testo

### 1.1 Righe e terminatori

Per un sistema Unix un file di testo è una sequenza di **righe**, e una riga è una sequenza di caratteri **terminata** dal byte a capo, `\n` (*line feed*, valore 10, esadecimale `0a`). Lo standard POSIX è preciso: una riga **include** il suo terminatore, e un file di testo corretto termina con `\n`. Conseguenze pratiche:

- `wc -l` non conta le righe: conta i caratteri `\n`. Un file che contiene `senza a capo` senza terminatore ha **0** righe per `wc -l`;
- molti strumenti trattano in modo speciale l'ultima riga se manca il terminatore (e alcuni, come `read` in bash, la perdono: Lezione 4);
- il byte `\n` è un byte come un altro: `grep`, `sed` e `awk` lavorano **una riga alla volta** proprio perché tagliano il flusso a ogni `\n`.

```
$ printf 'senza a capo' | wc -l
0
$ printf 'una\ndue\n' | wc -l
2
```

### 1.2 Il problema di Windows: `\r\n`

Windows (e molti protocolli di rete, come HTTP) termina le righe con **due** byte: `\r\n` (*carriage return* + *line feed*, `0d 0a`), un'eredità delle telescriventi, dove il carrello doveva tornare a inizio riga e poi la carta avanzare. Su Linux il `\r` resta **dentro** la riga, come ultimo carattere, invisibile a schermo. È una delle trappole più frequenti nelle gare, perché un file preparato su Windows sembra identico ma non si comporta allo stesso modo:

```
$ printf 'riga1\r\nriga2\r\n' > win.txt
$ cat win.txt
riga1
riga2
$ grep -c 'riga1$' win.txt        # "riga1" alla fine della riga?
0
$ cat -A win.txt                  # -A mostra i caratteri invisibili
riga1^M$
riga2^M$
```

`cat -A` mostra `^M` per `\r` (Ctrl-M, carattere 13), `$` alla fine di ogni riga, `^I` per la tabulazione. La riga non finisce con `riga1` ma con `riga1\r`, per questo l'ancora `$` non corrisponde. Rimedi: `tr -d '\r' < win.txt > unix.txt`, oppure `sed 's/\r$//'`, oppure `dos2unix` se installato. `file win.txt` lo segnala: *ASCII text, with CRLF line terminators*.

### 1.3 Byte e caratteri

Un **byte** è un numero da 0 a 255. Un **carattere** è un simbolo astratto (una lettera, una cifra, un ideogramma). Il legame tra i due è la **codifica** (*encoding*): in ASCII ogni carattere è un byte; in **UTF-8**, la codifica dominante oggi, i caratteri ASCII restano un byte e gli altri ne occupano da 2 a 4. La lettera `é` in UTF-8 è `c3 a9`, due byte. Studieremo le codifiche a fondo nella Lezione 7; per ora conta un solo fatto: **molti strumenti di testo dipendono dalla *locale***, cioè dalle variabili `LANG` e `LC_*` (L1 §12.2), che dicono loro quale codifica usare e come ordinare.

```
$ printf 'é\n' | wc -m -c          # in una locale UTF-8: 2 caratteri (é e \n), 3 byte
      2       3
$ printf 'é\n' | LC_ALL=C wc -m    # nella locale C ogni byte è un carattere
3
```

La locale influenza anche l'ordinamento (`sort`), gli intervalli nelle espressioni regolari (`[a-z]` può includere lettere accentate, o perfino maiuscole, in alcune locale), il significato di `\w` e di `[[:alpha:]]`. Per risultati prevedibili e veloci, negli script e quando analizzi dati binari si usa **`LC_ALL=C`**: ogni byte è un carattere, e l'ordine è quello numerico dei byte.

### 1.4 Testo o binario?

Non c'è una distinzione formale: un file "binario" è un file in cui compaiono byte che non formano testo leggibile, in particolare byte zero. Gli strumenti di testo se ne accorgono: `grep` su un file con byte zero risponde `binary file matches` invece di stampare la riga (l'opzione `-a` lo forza a trattarlo come testo), e `cat` di un binario può riempire il terminale di caratteri di controllo e perfino cambiarne le impostazioni (`reset` lo ripara). Per guardare un binario si usano `od` o `xxd` (L2 §11) e, per estrarne le parti leggibili, `strings` (§13).

## 2. Guardare un file senza farsi ingannare

| Comando | Effetto | Opzioni utili |
|---|---|---|
| `cat f` | stampa il file | `-n` numera le righe, `-A` mostra i caratteri invisibili, `-v` mostra i caratteri di controllo |
| `less f` | visualizzatore con scorrimento e ricerca (gli stessi tasti di `man`, L1 §13.4) | `-N` numeri di riga, `-S` non va a capo nelle righe lunghe |
| `head f` / `tail f` | prime / ultime 10 righe | `-n 20`; `-c 100` (byte); `tail -n +5` dalla riga 5 in poi; `head -n -3` tutto tranne le ultime 3 |
| `tail -f f` | segue il file mentre cresce | indispensabile per i log |
| `wc f` | righe, parole, byte | `-l`, `-w`, `-c` (byte), `-m` (caratteri) |
| `nl f` | numera le righe non vuote | |
| `tac f` | stampa le righe in ordine inverso | |
| `rev f` | inverte i caratteri di ogni riga | |
| `fold -w 60 f` | spezza le righe lunghe | |
| `column -t` | allinea in colonne (pacchetto `bsdextrautils`, non sempre installato) | |

Due combinazioni da ricordare. `head -n 20 f | tail -n 1` stampa la ventesima riga (lo fa anche `sed -n 20p f`, §10). `cat -A f | head` è il primo controllo da fare quando un file "sembra giusto" ma i comandi non funzionano: tabulazioni al posto di spazi, `\r` finali, spazi in coda, caratteri invisibili.

---

# Parte II — Le espressioni regolari

## 3. Che cos'è un'espressione regolare

### 3.1 L'idea

Un'**espressione regolare** (*regular expression*, *regex*) è una formula che descrive un **insieme di stringhe**. `ca.a` descrive "c, a, un carattere qualsiasi, a": `casa`, `cava`, `ca8a`, … Un programma come `grep` legge ogni riga e si chiede: *questa riga contiene almeno una sottostringa che appartiene all'insieme?*

### 3.2 Un po' di storia

Le espressioni regolari nascono come oggetto **matematico**. Nel 1951 il logico Stephen Kleene le definisce per descrivere i linguaggi riconosciuti dai modelli di neuroni di McCulloch e Pitts, e introduce l'operatore di ripetizione che da lui prende il nome, la *stella di Kleene* `*`. Nella teoria dei linguaggi formali un linguaggio è **regolare** se è descritto da un'espressione costruita con tre sole operazioni:

| Operazione | Notazione | Significato |
|---|---|---|
| concatenazione | `ab` | `a` seguito da `b` |
| alternativa | `a|b` | `a` oppure `b` |
| stella di Kleene | `a*` | zero o più ripetizioni di `a` |

Il **teorema di Kleene** dimostra che i linguaggi regolari sono esattamente quelli riconosciuti da un **automa a stati finiti**: una macchina con un numero finito di stati che legge un carattere alla volta. È ciò che rende le regex efficienti, e anche ciò che le limita: un automa finito non può "contare" senza limite, quindi nessuna espressione regolare in senso stretto riconosce le stringhe con parentesi bilanciate, o un documento HTML ben formato.

Nel 1968 Ken Thompson, lo stesso di Unix (L1 §3), pubblica un algoritmo per trasformare una regex in un automa e simularlo (*Regular Expression Search Algorithm*, Communications of the ACM), e lo implementa negli editor QED ed `ed`. In `ed` il comando per stampare le righe che corrispondono a un'espressione si scrive `g/re/p` (*global*, *regular expression*, *print*): nel 1973 Thompson ne fa un programma separato, e il nome resta, **`grep`**.

### 3.3 Regex e glob: non confonderli

| | Glob (shell, L1 §8.7) | Espressione regolare |
|---|---|---|
| chi lo interpreta | la shell, prima di eseguire il comando | il programma (`grep`, `sed`, `awk`, `find -regex` …) |
| su che cosa | nomi di file esistenti | qualunque testo |
| deve corrispondere | all'**intero** nome | a una **parte** della riga, salvo ancore |
| `*` | qualunque stringa | zero o più volte l'elemento **precedente** |
| `?` | un carattere qualsiasi | zero o una volta l'elemento precedente (ERE) |
| `.` | un punto letterale | un carattere qualsiasi |
| `[abc]` | un carattere dell'insieme | uguale |
| `[!abc]` | negazione | `[^abc]` |

Il glob `*.txt` corrisponde alla regex `^.*\.txt$`. Se scrivi `grep *.txt file` senza virgolette, la shell espande `*.txt` nei nomi dei file della directory prima che `grep` parta: un errore difficile da diagnosticare. **Virgolette singole, sempre.**

## 4. La sintassi

### 4.1 I mattoni

| Elemento | Significato | Esempio | Corrisponde a |
|---|---|---|---|
| carattere normale | sé stesso | `flag` | `flag`, `myflag2` |
| `.` | un carattere qualsiasi (tranne `\n`) | `f.ag` | `flag`, `f-ag` |
| `[...]` | un carattere dell'insieme | `[aeiou]` | una vocale |
| `[a-z]`, `[0-9A-F]` | intervalli | `[0-9a-f]` | una cifra esadecimale minuscola |
| `[^...]` | un carattere **non** nell'insieme | `[^0-9]` | qualunque cosa tranne una cifra |
| `^` | inizio della riga (ancora) | `^root` | righe che iniziano con `root` |
| `$` | fine della riga (ancora) | `bash$` | righe che finiscono con `bash` |
| `\` | rende letterale il carattere speciale che segue | `\.` | un punto |

Dentro le parentesi quadre quasi tutti i caratteri speciali perdono il loro significato: `[.*]` è "un punto o un asterisco". Le eccezioni sono `^` all'inizio (negazione), `-` tra due caratteri (intervallo; per un trattino letterale mettilo primo o ultimo, `[a-z-]`), `]` (per includerlo mettilo primo, `[]a]`) e `\` in alcune varianti.

Le **classi POSIX** si scrivono dentro le parentesi quadre e, a differenza degli intervalli, hanno un significato definito anche nelle locale non inglesi:

| Classe | Equivale (in locale C) a |
|---|---|
| `[[:digit:]]` | `[0-9]` |
| `[[:alpha:]]` | `[A-Za-z]` |
| `[[:alnum:]]` | `[A-Za-z0-9]` |
| `[[:upper:]]`, `[[:lower:]]` | `[A-Z]`, `[a-z]` |
| `[[:space:]]` | spazio, `\t`, `\n`, `\r`, `\v`, `\f` |
| `[[:xdigit:]]` | `[0-9A-Fa-f]` |
| `[[:punct:]]` | punteggiatura |
| `[[:print:]]` | caratteri stampabili, spazio compreso |

Nota le **doppie** parentesi: `[[:digit:]]` è "un insieme che contiene la classe delle cifre". `[:digit:]` da solo è l'insieme dei caratteri `:`, `d`, `i`, `g`, `t`.

### 4.2 Quantificatori

Si applicano all'elemento **immediatamente precedente** (un carattere, una classe, un gruppo):

| Quantificatore | Significato | Esempio | Corrisponde a |
|---|---|---|---|
| `*` | zero o più | `ab*c` | `ac`, `abc`, `abbbc` |
| `+` | una o più | `ab+c` | `abc`, `abbbc` (non `ac`) |
| `?` | zero o una | `colou?r` | `color`, `colour` |
| `{n}` | esattamente n | `[0-9]{4}` | quattro cifre |
| `{n,}` | almeno n | `a{2,}` | `aa`, `aaa`, … |
| `{n,m}` | da n a m | `[0-9a-f]{2,8}` | da 2 a 8 cifre esadecimali |

`.*` è "qualunque cosa, anche niente": il jolly delle regex. Attenzione a `a*`, che corrisponde anche alla stringa vuota, e quindi a **ogni** riga.

### 4.3 Gruppi, alternative, riferimenti

| Elemento | Significato | Esempio |
|---|---|---|
| `(...)` | raggruppa: un quantificatore si applica al gruppo intero | `(ab)+` → `ab`, `abab` |
| `a|b` | alternativa | `cat|dog`; `^(GET|POST) ` |
| `\1`, `\2` … | **riferimento all'indietro**: ripete esattamente il testo catturato dal gruppo n | `(abc)\1` → `abcabc`; `(.)\1` → due caratteri uguali consecutivi |

I gruppi servono anche a **catturare** pezzi di testo da riusare in una sostituzione (`sed`, §10). I riferimenti all'indietro sono un'estensione che va **oltre** i linguaggi regolari della teoria (§3.2): `(.+)\1` descrive le stringhe "ripetute due volte", che nessun automa finito può riconoscere. Per questo i motori che li supportano non possono usare solo automi, con le conseguenze del §5.

### 4.4 Tre dialetti: BRE, ERE, PCRE

Purtroppo la sintassi non è una sola. Ne incontrerai tre.

| | **BRE** (POSIX di base) | **ERE** (POSIX estese) | **PCRE** (stile Perl) |
|---|---|---|---|
| dove | `grep`, `sed` (default) | `grep -E`, `sed -E`, `awk`, `egrep` | `grep -P`, Python, JavaScript, PHP, la maggior parte dei linguaggi |
| `+ ? | ( ) { }` | **letterali**; speciali solo con il backslash: `\+ \? \| \( \) \{ \}` (le versioni `\+ \? \|` sono estensioni GNU) | speciali così come sono | speciali così come sono |
| riferimenti `\1` | sì | sì in GNU (non nello standard POSIX) | sì |
| `\d \w \s` (cifra, parola, spazio) | `\w \s` sì in GNU; `\d` no | come BRE | sì |
| `\b` confine di parola | GNU: `\b`, `\<`, `\>` | GNU: `\b`, `\<`, `\>` | `\b` |
| quantificatori pigri `*? +?` | no | no | sì (§4.5) |
| *lookahead* / *lookbehind* `(?=…)` `(?<=…)` | no | no | sì |

Regola pratica: usa **`grep -E`** e **`sed -E`** come predefiniti, così `+`, `?`, `|` e le parentesi funzionano come ti aspetti; passa a **`grep -P`** quando ti servono `\d`, i quantificatori pigri o i *lookaround*. Un esempio dello stesso concetto nei tre dialetti, "una o più cifre seguite da `px`":

```
$ grep    '[0-9]\+px' f      # BRE (GNU)
$ grep -E '[0-9]+px'  f      # ERE
$ grep -P '\d+px'     f      # PCRE
```

### 4.5 Quale corrispondenza? Più lunga, più a sinistra, avida, pigra

Quando una regex può corrispondere in più modi, quale sceglie il motore?

- **Più a sinistra**: tutti i motori scelgono la corrispondenza che **inizia** prima nella riga.
- Tra quelle che iniziano nello stesso punto, i motori **POSIX** (BRE ed ERE) scelgono la **più lunga** (*leftmost-longest*).
- I motori **PCRE** provano le alternative nell'ordine in cui sono scritte, e i quantificatori sono **avidi** (*greedy*): prendono più caratteri che possono, poi ne restituiscono uno alla volta se il resto non corrisponde. Aggiungendo `?` dopo il quantificatore diventano **pigri** (*lazy*): ne prendono meno che possono.

La differenza conta quando estrai qualcosa delimitato da caratteri che compaiono più volte:

```
$ echo 'flag{uno} e flag{due}' | grep -oE 'flag\{.*\}'
flag{uno} e flag{due}
$ echo 'flag{uno} e flag{due}' | grep -oP 'flag\{.*?\}'
flag{uno}
flag{due}
$ echo 'flag{uno} e flag{due}' | grep -oE 'flag\{[^}]*\}'
flag{uno}
flag{due}
```

`.*` avido arriva fino all'**ultima** `}` della riga. Il quantificatore pigro risolve in PCRE; la classe negata `[^}]*` ("qualunque cosa tranne `}`") risolve in **qualunque** dialetto, ed è la forma da preferire. `grep -o` stampa solo le parti che corrispondono, una per riga (§7).

### 4.6 Confini di parola

`\b` corrisponde alla **posizione** tra un carattere di parola (lettera, cifra, `_`) e uno che non lo è; `\<` e `\>` (GNU) all'inizio e alla fine di una parola. Non consumano caratteri.

```
$ echo 'cat category concat' | grep -o '\bcat\b'
cat
```

`grep -w cat` fa la stessa cosa in modo più leggibile (§7).

## 5. Come funziona un motore di espressioni regolari

### 5.1 Automi: NFA e DFA

L'algoritmo di Thompson (§3.2) traduce una regex in un **automa finito non deterministico** (NFA): un grafo di stati in cui, da uno stato, lo stesso carattere può portare a più stati. Ci sono due modi di eseguirlo.

- **Simulazione parallela**: si tiene l'insieme di **tutti** gli stati in cui l'automa potrebbe trovarsi, e lo si aggiorna a ogni carattere letto. Il tempo è proporzionale a (lunghezza del testo) × (dimensione della regex): **lineare** nel testo, sempre. L'insieme di stati si può anche precalcolare, ottenendo un automa **deterministico** (DFA), ancora più veloce. Usano questa strada GNU `grep` (per le espressioni senza riferimenti all'indietro), `awk`, RE2 di Google, il motore di Rust.
- **Backtracking**: si prova una strada alla volta e, se fallisce, si torna indietro all'ultima scelta e si prova la successiva. È semplice da implementare e permette funzioni che gli automi non hanno (riferimenti all'indietro, *lookaround*), ma nel caso peggiore il tempo è **esponenziale**. Usano questa strada PCRE, Perl, Python, Java, JavaScript, .NET.

### 5.2 Il backtracking catastrofico e il ReDoS

Considera `^(a+)+$` applicata a `aaaaaaaaaaaaaaaaaaaaaaaa!`: 24 lettere `a` e un punto esclamativo finale. La regex non può corrispondere (c'è `!` prima della fine). Un motore a backtracking, però, prima di arrendersi prova **tutti i modi** di dividere le 24 `a` tra le ripetizioni del gruppo esterno e quelle del `+` interno: sono 2^23, circa otto milioni. Ogni `a` in più **raddoppia** il tempo. Misurato in Python su una macchina comune:

| Lunghezza | Tempo |
|---|---|
| 20 `a` + `!` | 0,07 s |
| 22 `a` + `!` | 0,19 s |
| 24 `a` + `!` | 0,79 s |
| 30 `a` + `!` | circa 50 s (stima: ×4 ogni due caratteri) |

GNU `grep -P` usa PCRE2 con un limite di backtracking e si arrende con un errore (`exceeded PCRE's backtracking limit`, codice di uscita 2); `grep -E` con la stessa espressione risponde subito, perché usa un automa.

Se un servizio applica una regex vulnerabile a un input scelto dall'utente (un campo di un modulo web, un'intestazione HTTP), un singolo input di poche decine di caratteri può bloccare un processore per minuti: è il **ReDoS** (*Regular expression Denial of Service*), classificato come **CWE-1333** (*Inefficient Regular Expression Complexity*). Lo schema da riconoscere è un **quantificatore annidato su qualcosa che può corrispondere in più modi**: `(a+)+`, `(a|a)*`, `(\w+\s?)*`. Le difese: motori a tempo lineare (RE2), limiti di tempo e di lunghezza dell'input, riscrivere l'espressione senza ambiguità (`^a+$` descrive lo stesso insieme di `^(a+)+$`). Torneremo sull'argomento nel Modulo 6 (web).

## 6. Espressioni utili in gara

| Obiettivo | Espressione (ERE, salvo indicazione) | Note |
|---|---|---|
| una flag `nome{...}` | `[A-Za-z0-9_]+\{[^}]*\}` | adatta il prefisso al formato della gara |
| flag di pwn.college | `pwn\.college\{[^}]*\}` | il punto va protetto |
| indirizzo IPv4 (forma) | `([0-9]{1,3}\.){3}[0-9]{1,3}` | accetta anche `999.1.1.1`: verifica i valori a parte |
| stringa esadecimale lunga | `[0-9a-fA-F]{16,}` | hash, chiavi, dati codificati (Lezione 7) |
| probabile Base64 | `[A-Za-z0-9+/]{16,}={0,2}` | Lezione 7 |
| indirizzo email (approssimato) | `[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}` | una regex "perfetta" per le email non esiste |
| righe vuote o solo spazi | `^[[:space:]]*$` | con `grep -v` le elimini |
| commenti di configurazione | `^[[:space:]]*#` | `grep -vE '^[[:space:]]*(#|$)' f` mostra solo le righe attive |
| richieste HTTP in un log | `"(GET|POST|PUT|DELETE) [^ ]+` | |

Non cercare di scrivere la regex perfetta: in gara serve quella che separa ciò che cerchi dal rumore **in quei dati**. Si parte larga, si guarda il risultato, si stringe.

---

# Parte III — Gli strumenti

## 7. `grep`

### 7.1 Il modello

`grep [opzioni] MODELLO [file ...]` legge i file (o lo standard input), li divide in righe e stampa ogni riga che contiene almeno una corrispondenza del modello. Tutto qui: le opzioni cambiano **quale dialetto** usare, **che cosa** stampare e **dove** cercare.

### 7.2 Le opzioni

| Gruppo | Opzione | Effetto |
|---|---|---|
| dialetto | `-E` / `-P` / `-F` | ERE / PCRE / **stringa fissa**, nessun carattere speciale (§4.4) |
| corrispondenza | `-i` | ignora maiuscole e minuscole |
| | `-w` / `-x` | la corrispondenza deve essere una parola intera / la riga intera |
| | `-v` | **inverte**: stampa le righe che **non** corrispondono |
| | `-e MOD` | specifica un modello (ripetibile: `-e a -e b` = a oppure b); utile se il modello inizia con `-` |
| | `-f file` | legge i modelli da un file, uno per riga |
| output | `-n` | numero di riga |
| | `-o` | solo la parte che corrisponde, una per riga |
| | `-c` | conta le righe che corrispondono (non le corrispondenze!) |
| | `-l` / `-L` | solo i nomi dei file che contengono / non contengono corrispondenze |
| | `-h` / `-H` | senza / con il nome del file davanti a ogni riga |
| | `-A n`, `-B n`, `-C n` | n righe di contesto dopo / prima / attorno |
| | `--color=auto` | evidenzia (spesso già attivo con un alias, L1 §10.1) |
| dove | `-r` / `-R` | ricorsivo nelle directory (`-R` segue anche i link simbolici, L2 §9.4) |
| | `--include='*.py'`, `--exclude-dir=.git` | filtra i file nella ricerca ricorsiva (glob, non regex) |
| | `-a` | tratta i binari come testo |
| | `-z` | le "righe" sono separate da byte zero invece che da `\n` |
| controllo | `-q` | silenzioso: non stampa nulla, conta solo il codice di uscita |
| | `-m n` | si ferma dopo n righe |

### 7.3 Codice di uscita

`grep` comunica il risultato anche con il codice di uscita (L1 §11): **0** se ha trovato almeno una riga, **1** se non ha trovato nulla, **2** se c'è stato un errore (file inesistente, regex non valida). Con `-q` è il modo idiomatico per fare un test in uno script:

```
$ grep -q '^hacker:' /etc/passwd && echo "l'utente esiste"
```

### 7.4 Le trappole

- **`-c` conta righe, non occorrenze.** Per contare le occorrenze: `grep -o modello f | wc -l`.
- **Un modello che contiene caratteri speciali** va scritto con `-F` se lo vuoi letterale: `grep 'a.b'` trova anche `axb`; `grep -F 'a.b'` no. Indirizzi IP, percorsi, frammenti di codice: usa `-F`.
- **Un modello che inizia con `-`** viene preso per un'opzione (lo stesso problema dei nomi di file, L1 §6.2): `grep -e '-v' f` oppure `grep -- '-v' f`.
- **`grep` su un binario** stampa `binary file matches`: aggiungi `-a`, oppure usa `strings` (§12).
- **`grep -r` senza `--include`** su una directory grande può impiegare molto: restringi con `--include` o combina con `find` (L2 §14.4).

```
$ grep -rn --include='*.py' 'password' .          # dove compare "password" nei sorgenti Python?
$ grep -rl 'pwn.college{' / 2>/dev/null           # quali file contengono una flag?
$ grep -vE '^[[:space:]]*(#|$)' /etc/ssh/sshd_config   # solo le righe di configurazione attive
$ grep -C 2 -n 'Failed password' /var/log/auth.log  # i tentativi di accesso falliti, con contesto
```

## 8. `tr`: trasformare caratteri

`tr` (*translate*) lavora sui **caratteri**, non sulle righe, e legge **solo** dallo standard input (non accetta nomi di file: si usa con `<` o in una pipe).

| Forma | Effetto | Esempio |
|---|---|---|
| `tr SET1 SET2` | sostituisce ogni carattere di SET1 con il corrispondente di SET2 | `tr 'a-z' 'A-Z'` (maiuscolo) |
| `tr -d SET` | elimina i caratteri di SET | `tr -d '\r'` (da Windows a Unix, §1.2) |
| `tr -s SET` | comprime le ripetizioni consecutive | `tr -s ' '` (spazi multipli → uno) |
| `tr -c ...` | usa il **complemento** di SET1 | `tr -cd '[:print:]'` (tiene solo i caratteri stampabili) |

Gli insiemi accettano intervalli (`a-z`), classi (`[:digit:]`, `[:space:]`) e sequenze di escape (`\n`, `\t`, `\0`, `\r`).

```
$ echo 'Uryyb, unpxre!' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
Hello, hacker!
$ tr '\0' '\n' < /proc/self/environ           # l'ambiente, una variabile per riga (L2 §12.2)
$ tr -cs '[:alpha:]' '\n' < testo.txt        # una parola per riga: ogni sequenza di non-lettere diventa un a capo
```

Il primo esempio è il **ROT13**: ogni lettera è sostituita da quella 13 posizioni più avanti nell'alfabeto. Poiché l'alfabeto inglese ha 26 lettere, applicarlo due volte riporta al testo originale. È un caso particolare del **cifrario di Cesare**, e compare spesso nelle sfide introduttive: lo riprenderemo con tutti i cifrari classici nel Modulo 5. L'ultimo esempio è la base dell'**analisi delle frequenze** (§14).

## 9. Tagliare, ordinare, contare: `cut`, `paste`, `sort`, `uniq`, `comm`

### 9.1 `cut` e `paste`

`cut` estrae **colonne**:

| Forma | Effetto |
|---|---|
| `cut -d: -f1` | campo 1, con `:` come separatore |
| `cut -d: -f1,7` / `-f3-` | campi 1 e 7 / dal 3 in poi |
| `cut -c1-8` | caratteri da 1 a 8 di ogni riga |
| `cut -b1-8` | byte da 1 a 8 |

```
$ cut -d: -f1,7 /etc/passwd
root:/bin/bash
hacker:/bin/bash
nobody:/usr/sbin/nologin
```

Limite importante: il separatore di `cut` è **un solo carattere**, e due separatori consecutivi delimitano un campo vuoto. Su testo allineato con più spazi (l'output di `ls -l`, di `ps`) `cut -d' '` non funziona: usa `awk` (§11), che per default tratta qualunque sequenza di spazi come un unico separatore, oppure comprimi prima con `tr -s ' '`.

`paste` fa l'opposto: affianca righe di file diversi (`paste f1 f2`), o unisce le righe di un file in una (`paste -sd, f` → `a,b,c`).

### 9.2 `sort`

| Opzione | Effetto |
|---|---|
| (nessuna) | ordine "alfabetico" secondo la locale |
| `-n` | numerico: `9 < 10 < 100` (senza `-n`: `10 < 100 < 9`) |
| `-h` | numerico con suffissi: `2K < 1M < 3G` (output di `du -h`, L2 §15) |
| `-V` | numeri di versione: `v1.9 < v1.10` |
| `-r` | inverte |
| `-u` | elimina i duplicati |
| `-t: -k3,3n` | separatore `:`, ordina per il campo 3 (solo il 3), numericamente |
| `-f` | ignora le maiuscole |
| `-R` | ordine casuale |

```
$ printf '10\n9\n100\n' | sort
10
100
9
$ printf '10\n9\n100\n' | sort -n
9
10
100
$ sort -t: -k3,3n /etc/passwd | head -3       # utenti ordinati per UID
```

`sort` legge **tutto** l'input prima di produrre output (deve vedere tutte le righe per ordinarle), e usa file temporanei se i dati sono enormi. Con `LC_ALL=C sort` l'ordine è quello dei byte (`A < Z < a < z`) ed è più veloce; nella locale italiana o inglese l'ordine ignora in parte maiuscole e punteggiatura, con risultati a volte sorprendenti.

### 9.3 `uniq`

`uniq` elimina le righe **consecutive** identiche. Funziona quindi solo su input **ordinato**: per questo si scrive quasi sempre `sort | uniq`.

| Opzione | Effetto |
|---|---|
| (nessuna) | una copia di ogni gruppo di righe uguali consecutive |
| `-c` | premette il numero di ripetizioni |
| `-d` | solo le righe che compaiono più di una volta |
| `-u` | solo le righe che compaiono **una sola** volta |
| `-i` | ignora le maiuscole |

La catena più utile di tutta la lezione, la **classifica delle frequenze**:

```
$ printf 'b\na\nb\nc\na\nb\n' | sort | uniq -c | sort -rn
      3 b
      2 a
      1 c
```

Ordina, conta i gruppi, riordina per conteggio decrescente. Con `| head` diventa "i primi dieci": gli indirizzi IP che fanno più richieste in un log, le parole più frequenti in un testo cifrato, i caratteri più comuni in un blob.

### 9.4 `comm` e `diff`

`comm f1 f2` confronta due file **ordinati** e stampa tre colonne: righe solo in f1, solo in f2, in entrambi. Con `-1`, `-2`, `-3` sopprimi le colonne: `comm -12 f1 f2` mostra solo le righe comuni (intersezione), `comm -23 f1 f2` quelle solo nel primo (differenza). `diff f1 f2` mostra invece le modifiche necessarie per passare da un file all'altro, riga per riga (`diff -u` nel formato usato dalle *patch*): utile per vedere che cosa è cambiato tra due versioni di una configurazione o di un sorgente.

## 10. `sed`: l'editor di flusso

### 10.1 Il modello

`sed` (*stream editor*, Lee McMahon, Bell Labs, 1974) applica un piccolo **programma** a ogni riga del flusso. Il ciclo di funzionamento (`info sed`, *Execution Cycle*):

1. legge una riga nello **spazio di lavoro** (*pattern space*), senza il `\n` finale;
2. esegue in ordine i comandi del programma il cui **indirizzo** corrisponde alla riga;
3. alla fine, salvo l'opzione `-n`, **stampa** lo spazio di lavoro e un `\n`;
4. ricomincia con la riga successiva.

Un comando è `[indirizzo]comando[argomenti]`. Senza indirizzo, si applica a tutte le righe.

### 10.2 Indirizzi

| Indirizzo | Righe selezionate |
|---|---|
| `5` | la riga 5 |
| `$` | l'ultima riga |
| `/regex/` | le righe che corrispondono |
| `3,7` | dalla 3 alla 7 |
| `/inizio/,/fine/` | da una riga che corrisponde a `inizio` alla successiva che corrisponde a `fine` |
| `1~2` (GNU) | dalla 1, una ogni 2 (le dispari) |
| `indirizzo!` | tutte le righe **tranne** quelle |

### 10.3 Comandi

| Comando | Effetto |
|---|---|
| `p` | stampa lo spazio di lavoro (si usa con `-n`) |
| `d` | cancella lo spazio di lavoro e passa alla riga successiva (niente stampa) |
| `s/regex/sostituto/flag` | **sostituzione** (§10.4) |
| `y/abc/xyz/` | traslitterazione carattere per carattere, come `tr` |
| `a testo` / `i testo` / `c testo` | aggiunge dopo / inserisce prima / sostituisce la riga con `testo` |
| `q` | esce (stampando la riga corrente) |
| `=` | stampa il numero di riga |

```
$ sed -n '5p' f                    # stampa solo la riga 5
$ sed -n '/BEGIN/,/END/p' f        # stampa un blocco delimitato
$ sed '/^#/d' f                    # elimina i commenti
$ sed '1d;$d' f                    # elimina la prima e l'ultima riga
$ sed -n '$=' f                    # numero di righe (come wc -l, ma conta anche l'ultima senza \n)
```

Più comandi si separano con `;` o con più opzioni `-e`.

### 10.4 La sostituzione

`s/regex/sostituto/flag` è il comando che userai nel 90% dei casi.

- Senza flag sostituisce solo la **prima** corrispondenza di ogni riga; con **`g`** tutte; con un numero `n` solo la n-esima; con **`i`** (GNU) ignora le maiuscole; con **`p`** stampa la riga se c'è stata una sostituzione (utile con `-n`).
- Nel sostituto, **`&`** è l'intero testo che ha corrisposto, e **`\1`** … **`\9`** i gruppi catturati.
- Il delimitatore può essere qualunque carattere: con i percorsi, `s|/usr/local|/opt|` evita di dover scrivere `\/` ovunque.

```
$ echo 'ciao mondo' | sed -E 's/(\w+) (\w+)/\2 \1/'      # scambia due parole
mondo ciao
$ echo 'a.b.c' | sed 's/./X/g'                           # . è "un carattere qualsiasi"!
XXXXX
$ echo 'a.b.c' | sed 's/\./X/g'
aXbXc
$ echo 'prezzo 42' | sed -E 's/[0-9]+/[&]/'               # & = ciò che ha corrisposto
prezzo [42]
$ sed -E 's/(password=).*/\1*****/' config.ini           # nasconde un valore, tiene la chiave
```

### 10.5 Modifica sul posto: `-i`

`sed -i 's/vecchio/nuovo/g' file` **sovrascrive** il file con il risultato. In realtà `sed` scrive un file temporaneo e lo rinomina sopra l'originale (la tecnica della `rename()` atomica, L2 §6.3): l'inode cambia, e un eventuale hard link all'originale non viene modificato. Con `-i.bak` conserva una copia dell'originale in `file.bak`. Prima di un `sed -i`, prova sempre il comando senza `-i` e guarda l'output: non c'è annullamento.

## 11. `awk`: un linguaggio per dati a colonne

### 11.1 Il modello

`awk` (Aho, Weinberger, Kernighan, Bell Labs, 1977: il nome sono le loro iniziali) è un vero linguaggio di programmazione, progettato per elaborare testo organizzato in **record** (per default le righe) e **campi** (per default le parole separate da spazi). Un programma awk è una lista di regole:

```
modello { azione }
```

Per ogni record, awk valuta ogni modello; se è vero, esegue l'azione. Un modello assente è sempre vero; un'azione assente è `{ print }`. Due modelli speciali: **`BEGIN`** (eseguito prima di leggere qualunque input) e **`END`** (dopo l'ultimo record).

| Variabile | Significato |
|---|---|
| `$0` | il record intero |
| `$1`, `$2`, … `$NF` | i campi; `$NF` è l'ultimo |
| `NF` | numero di campi del record corrente |
| `NR` | numero del record corrente (contato su tutti i file) |
| `FNR` | numero del record nel file corrente |
| `FS` / `OFS` | separatore dei campi in input / in output (`-F:` imposta `FS`) |
| `RS` / `ORS` | separatore dei record in input / in output |
| `FILENAME` | nome del file corrente |

Con il separatore di default, awk divide su **qualunque sequenza** di spazi e tabulazioni e ignora quelli iniziali: per questo funziona dove `cut` fallisce (§9.1).

### 11.2 Esempi graduati

```
$ awk '{print $1}' f                          # prima colonna
$ awk '{print $NF}' f                         # ultima colonna
$ awk -F: '$3 >= 1000 {print $1}' /etc/passwd # utenti "normali": UID ≥ 1000
$ awk 'NR==5' f                               # solo la riga 5 (modello senza azione)
$ awk 'NR>=10 && NR<=20' f                    # righe da 10 a 20
$ awk 'length($0) > 80' f                     # righe più lunghe di 80 caratteri
$ awk '/ERROR/ {n++} END {print n+0}' log     # quante righe contengono ERROR
$ awk '{s += $5} END {print s}' f             # somma della colonna 5
$ awk -F: '{printf "%-8s %5d\n", $1, $3}' /etc/passwd   # tabella formattata
```

Nell'esempio di `ERROR`, `n+0` stampa `0` invece di una riga vuota se non ci sono corrispondenze: in awk una variabile mai usata vale stringa vuota e numero zero insieme.

### 11.3 Array associativi

Gli array di awk sono **associativi**: l'indice è una stringa qualsiasi. Sono lo strumento ideale per raggruppare e contare.

```
$ printf 'x 10\ny 20\nx 5\n' | awk '{s[$1] += $2} END {for (k in s) print k, s[k]}'
x 15
y 20
$ awk '{print $1}' access.log | sort | uniq -c | sort -rn | head    # IP più attivi, con sort/uniq
$ awk '{c[$1]++} END {for (ip in c) print c[ip], ip}' access.log | sort -rn | head   # stessa cosa, in awk
```

L'ordine di `for (k in s)` non è garantito: se conta, aggiungi `| sort`.

### 11.4 awk come calcolatrice

```
$ awk 'BEGIN {print 2^10, 7/2, int(7/2), sprintf("%x", 255)}'
1024 3.5 3 ff
```

A differenza dell'aritmetica di bash (L1 §8.5), awk usa numeri **in virgola mobile**: `7/2` fa 3.5. Attenzione: i numeri molto grandi (oltre 2^53) perdono precisione, e per gli indirizzi a 64 bit del Modulo 3 conviene usare `$(( ))` o Python. Su Debian e Ubuntu l'`awk` predefinito è spesso **mawk**, più veloce ma con meno funzioni di **gawk** (GNU awk): se un esempio trovato in rete usa funzioni come `gensub` o `strftime`, installa e usa `gawk`.

## 12. `strings`: il testo dentro i binari

`strings file` stampa tutte le sequenze di almeno 4 caratteri stampabili consecutivi che trova in un file qualsiasi. È lo strumento di primo impatto su un eseguibile, un'immagine disco, un dump di memoria:

| Opzione | Effetto |
|---|---|
| `-n 8` | lunghezza minima 8 (riduce il rumore) |
| `-t x` / `-t d` | premette la posizione (*offset*) in esadecimale / decimale |
| `-e l` | cerca stringhe in **UTF-16 little-endian** (2 byte per carattere), comuni nei programmi Windows |
| `-a` | esamina tutto il file (default nelle versioni recenti) |

```
$ strings -n 8 blob | grep FLAG
NlbFLAGPART
$ strings -t x -n 8 blob | grep FLAG
    129 NlbFLAGPART
$ strings u16              # "SEGRETO" scritto in UTF-16: S\0E\0G\0...
$ strings -e l u16
SEGRETO
```

Nota `Nlb` davanti a `FLAGPART`: tre byte casuali che per caso erano stampabili e sono stati attaccati alla stringa. È normale. Nota anche che `strings` senza `-e l` non trova nulla nel secondo file: tra una lettera e l'altra c'è un byte zero, quindi nessuna sequenza raggiunge 4 caratteri.

`strings binario | grep -i flag` è il primo comando di molte sfide di reverse engineering, e a volte basta. Quando non basta è perché la flag è **costruita durante l'esecuzione**, cifrata o offuscata: allora serve l'analisi vera e propria dei Moduli 3 e 4. Il capitolo 5 di *Practical Binary Analysis* usa `strings` proprio come primo passo di un'analisi.

## 13. Altri strumenti da conoscere

| Strumento | A che cosa serve | Dove lo approfondiamo |
|---|---|---|
| `od`, `xxd`, `hexdump` | vedere i byte | L2 §11, Lezione 7 |
| `base64`, `base32` | codificare e decodificare (`-d`) | Lezione 7 |
| `iconv -f UTF-16 -t UTF-8` | convertire tra codifiche | Lezione 7 |
| `jq` | interrogare e trasformare JSON | Modulo 6 (web) |
| `split`, `csplit` | dividere un file in pezzi | |
| `shuf` | mescolare righe | |
| `md5sum`, `sha256sum` | impronte di file, per confrontarli | Modulo 5 |
| `vim`, `nano` | modificare file a mano | allegato pratico: impara almeno `nano` e le basi di `vim` (`i`, `Esc`, `:wq`, `:q!`) |

---

# Parte IV — Composizione e sicurezza

## 14. Comporre: ricette ragionate

Il valore di questi strumenti sta nella composizione. Ogni ricetta qui sotto va letta da sinistra a destra come una frase: che cosa entra, che cosa esce da ogni passaggio.

### 14.1 Estrarre flag da qualunque cosa

```
$ grep -aoE '[A-Za-z0-9_]+\{[^}]*\}' dump.bin | sort -u
```
`-a` tratta il binario come testo, `-o` stampa solo le corrispondenze, `sort -u` toglie i duplicati. Funziona su log, dump di memoria, catture di rete, immagini disco.

### 14.2 Analisi di un log web

Una riga del *Combined Log Format* di Apache e nginx:
```
203.0.113.7 - - [07/Nov/2026:17:30:01 +0000] "GET /admin.php?id=1 HTTP/1.1" 404 512 "-" "curl/8.5.0"
```
Campi separati da spazi: `$1` IP, `$4` data, `$6` metodo (con la virgoletta), `$7` percorso, `$9` codice di stato, `$10` byte.

```
$ awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -5      # chi fa più richieste?
$ awk '$9 == 404 {print $7}' access.log | sort | uniq -c | sort -rn | head   # quali pagine mancano?
$ awk '$9 >= 500' access.log | wc -l                                      # quanti errori del server?
$ grep -E '\.\./|%2e%2e|<script|UNION' -i access.log                      # tentativi di attacco tipici (Modulo 6)
$ awk '{print $9}' access.log | sort | uniq -c                           # distribuzione dei codici di stato
```

### 14.3 Analisi delle frequenze

```
$ tr -cs '[:alpha:]' '\n' < testo.txt | tr 'A-Z' 'a-z' | sort | uniq -c | sort -rn | head
$ grep -o . cifrato.txt | sort | uniq -c | sort -rn | head
```

La prima conta le parole (una per riga, tutto minuscolo, poi la classifica); la seconda i **singoli caratteri** (`grep -o .` stampa ogni carattere su una riga). In italiano le lettere più frequenti sono E, A, I, O; in inglese E, T, A, O. Se in un testo cifrato con una sostituzione semplice la lettera più frequente è `Q`, probabilmente `Q` sta per `E`: è il metodo con cui al-Kindi, nel IX secolo, rompeva i cifrari monoalfabetici, e lo applicheremo nel Modulo 5.

### 14.4 Confrontare insiemi

```
$ cut -d: -f1 /etc/passwd | sort > utenti.txt
$ ls /home | sort > home.txt
$ comm -23 utenti.txt home.txt      # utenti senza una directory in /home
$ comm -13 utenti.txt home.txt      # directory in /home che non corrispondono a nessun utente (sospette!)
```

### 14.5 Cercare dentro molti file

```
$ grep -rlI 'API_KEY' . --exclude-dir=.git                 # -I salta i binari
$ find / -name '*.conf' -type f -exec grep -l 'password' {} + 2>/dev/null
$ find . -type f -print0 | xargs -0 strings -n 10 | grep -i flag
```

La seconda e la terza combinano la ricerca per proprietà di `find` (L2 §14) con la ricerca nel contenuto, passando i nomi in modo sicuro (L2 §14.4).

### 14.6 Pulire dati sporchi

```
$ tr -d '\r' < win.txt | sed 's/[[:space:]]*$//' | grep -v '^$' > pulito.txt
```

Toglie i `\r` di Windows, gli spazi in coda, le righe vuote. Un passaggio da fare **prima** di qualunque analisi su dati che non hai prodotto tu.

## 15. Sicurezza: dove si nascondono i problemi

Questi strumenti sono spesso usati **dentro** script e programmi, con dati che vengono dall'esterno. Ecco i difetti più comuni, da conoscere sia per evitarli sia per riconoscerli nelle sfide.

1. **Dati trattati come modello.** Uno script che esegue `grep "$input" archivio` con un `input` scelto dall'utente gli permette di passare una regex arbitraria (`.*` restituisce tutto) o un'opzione (`-r`, `-f /etc/shadow`, se l'input inizia con `-`). Difesa: `grep -F -e "$input" -- archivio`. È la stessa classe di *argument injection* (CWE-88) vista con i nomi di file (L1 §6.2).
2. **ReDoS.** Una regex vulnerabile applicata a input esterno blocca il servizio (§5.2, CWE-1333).
3. **Regex di convalida incomplete.** Una convalida come `grep -qE '[0-9]+'` "accetta solo numeri"? No: accetta qualunque riga che **contenga** una cifra, come `1; rm -rf /`. Senza le ancore `^...$` la regex cerca una sottostringa. Inoltre `$` può corrispondere prima di un `\n` finale in alcuni motori (in PCRE e Python), quindi `abc\n` passa un controllo `^abc$`: per un controllo rigoroso si usano le ancore assolute (in PCRE `\A ... \z`; in Python `\A ... \Z`, attenzione: le lettere hanno significati diversi nei due dialetti) o la corrispondenza dell'intera stringa (`re.fullmatch` in Python). È una classe di difetti che vedremo spesso nel Modulo 6 (CWE-185, *Incorrect Regular Expression*; CWE-20, *Improper Input Validation*).
4. **Iniezione nei log.** Un attaccante che riesce a inserire un `\n` in un campo registrato in un log (un nome utente, un *User-Agent*) può creare righe false che sembrano legittime: chi analizza il log con `grep` vede eventi mai avvenuti (CWE-117, *Improper Output Neutralization for Logs*). Nelle analisi forensi, una riga di log non è una prova finché non ne hai verificato la coerenza.
5. **`sed -i` e `awk` che eseguono comandi.** GNU `sed` ha il comando `e` e il flag `e` di `s`, che **eseguono** testo come comando di shell; `awk` ha `system()` e `print | "comando"`. Uno script che costruisce un programma sed o awk concatenando input esterno può quindi diventare un'esecuzione di comandi (CWE-78). Se un input deve entrare in un programma awk, passalo come variabile con `-v nome="$input"`, mai incollandolo nel testo del programma.

Il filo comune è quello delle due lezioni precedenti: **ogni volta che un dato attraversa un confine** (diventa argomento, modello, programma, riga di log), la domanda è se il ricevente lo interpreterà come dato o come istruzione.

---

# Parte V — La pratica

## 16. Esempi svolti

### Esempio 1 — Costruire una regex per gradi

Obiettivo: estrarre da un file tutti gli indirizzi IPv4. Si parte larghi e si stringe guardando i risultati.

```
$ grep -oE '[0-9.]+' f                        # troppo largo: prende anche "3.14" e "2026."
$ grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' f # quattro gruppi di cifre separati da punti
$ grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' f    # stessa cosa, più compatta, cifre da 1 a 3
$ grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' f   # non dentro numeri più lunghi
```

Ogni passaggio corregge un difetto osservato: è così che si scrivono le regex nella pratica. L'ultima forma accetta ancora `999.999.999.999`; se serve escluderlo, si filtra dopo con awk (`awk -F. '$1<256 && $2<256 && $3<256 && $4<256'`) invece di complicare la regex.

### Esempio 2 — Le righe di Windows

```
$ printf 'user=admin\r\npass=1234\r\n' > conf.txt
$ grep -c '^pass=1234$' conf.txt
0
$ cat -A conf.txt
user=admin^M$
pass=1234^M$
$ tr -d '\r' < conf.txt | grep -c '^pass=1234$'
1
```

Il `\r` invisibile prima del `\n` impedisce all'ancora `$` di corrispondere (§1.2). Ogni volta che un confronto "evidente" fallisce, `cat -A`.

### Esempio 3 — Avido contro non avido

```
$ echo 'x <b>uno</b> y <b>due</b>' | grep -oE '<b>.*</b>'
<b>uno</b> y <b>due</b>
$ echo 'x <b>uno</b> y <b>due</b>' | grep -oE '<b>[^<]*</b>' | sed -E 's/<\/?b>//g'
uno
due
$ echo 'x <b>uno</b> y <b>due</b>' | grep -oP '<b>\K.*?(?=</b>)'
uno
due
```

La prima va dalla prima `<b>` all'ultima `</b>` (§4.5). La seconda usa una classe negata e poi toglie i tag con `sed` (`<\/?b>`: `<`, una `/` facoltativa, `b>`). La terza è PCRE pura: `\K` scarta dal risultato ciò che ha corrisposto finora, `.*?` è pigro, `(?=</b>)` è un *lookahead*, che controlla che segua `</b>` senza includerlo. Nota: estrarre dati da HTML con le regex va bene per un'occhiata veloce in gara; per un'analisi seria si usa un parser vero (Modulo 6).

### Esempio 4 — `cut` fallisce, `awk` funziona

```
$ ls -l /etc | head -3
total 1084
-rw-r--r--  1 root root     3040 Mar 14  2024 adduser.conf
drwxr-xr-x  2 root root     4096 Oct 27 19:50 alternatives
$ ls -l /etc | head -3 | cut -d' ' -f5
                                       (righe vuote o pezzi sbagliati)
$ ls -l /etc | tail -n +2 | head -2 | awk '{print $5, $NF}'
3040 adduser.conf
4096 alternatives
```

`ls -l` allinea le colonne con un numero variabile di spazi: per `cut` due spazi consecutivi delimitano un campo vuoto, quindi il quinto "campo" non è la dimensione. `awk` tratta ogni sequenza di spazi come un separatore (§11.1). `tail -n +2` salta la riga `total` (§2). Avvertenza generale: l'output di `ls` è fatto per gli occhi; negli script è meglio `stat -c '%s %n'` o `find -printf` (L2 §7.2).

### Esempio 5 — La classifica degli shell di login

```
$ cut -d: -f7 /etc/passwd | sort | uniq -c | sort -rn
     18 /usr/sbin/nologin
      2 /bin/bash
      1 /bin/sync
```

Una riga, quattro filtri: estrai il settimo campo, ordina, conta i gruppi, ordina per conteggio. Le righe con `nologin` sono account di servizio che non possono accedere in modo interattivo (Lezione 6). Su una macchina da analizzare, uno shell inatteso per un account di servizio (`www-data` con `/bin/bash`) è un indizio.

### Esempio 6 — ROT13 e cifrari di Cesare con `tr`

```
$ echo 'Pv fbab qryyr ertbyr' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
Ci sono delle regole
$ echo 'attacco' | tr 'a-z' 'd-za-c'      # Cesare con spostamento 3: a→d, b→e, ... x→a
dwwdffr
$ echo 'dwwdffr' | tr 'd-za-c' 'a-z'      # decifrare: insiemi scambiati
attacco
```

`tr` associa i caratteri **per posizione**: `d-za-c` è la sequenza `defg…xyzabc`, cioè l'alfabeto ruotato di 3. Per uno spostamento `k` il secondo insieme inizia dalla lettera `k`-esima (contando da 0) e ricomincia da `a`. Con `tr` puoi provare a mano tutti i 25 spostamenti; nel Modulo 5 lo faremo con un ciclo e un'analisi delle frequenze automatica.

## 17. Esercizi

Livello ★ base, ★★ intermedio, ★★★ sfida. Prova ogni esercizio **prima** di aprire `Soluzioni.md`. Lavora in una directory di prova (`mkdir ~/l3 && cd ~/l3`).

### ★ Base

1. Crea il file dell'Esempio 2 (`conf.txt`). Dimostra con `cat -A` e con `od -c` che ogni riga termina con `\r\n`. Trasformalo in un file Unix in due modi diversi (`tr` e `sed`), e verifica che `file` e `grep -c '^pass=1234$'` ora diano il risultato atteso.
2. **Leggere le regex.** Per ogni espressione (ERE), indica quali delle stringhe `ac`, `abc`, `abbc`, `a.c`, `Abc`, `Abcd`, `123` contengono una corrispondenza. Poi verifica con `printf '%s\n' ac abc abbc a.c Abc Abcd 123 | grep -E 'REGEX'`.
   (a) `^a.c$`  (b) `ab*c`  (c) `ab+c`  (d) `a\.c`  (e) `^[[:upper:]][a-z]{2}$`  (f) `[^0-9]`  (g) `^[^0-9]+$`
3. Da `/etc/passwd`, con un solo `grep` ciascuno: (a) le righe degli utenti con shell `/bin/bash`; (b) quanti sono; (c) le righe che **non** contengono `nologin`; (d) le righe con UID 0, usando una regex che guardi il **terzo** campo (non basta cercare `:0:`: perché?).
4. Stampa la quindicesima riga di `/etc/services` in **tre** modi diversi (`head`/`tail`, `sed`, `awk`). Poi stampa le righe da 15 a 20.
5. Con `tr`: (a) trasforma `Ciao Mondo` in maiuscolo; (b) togli tutte le cifre da `a1b2c3`; (c) comprimi gli spazi in `molti     spazi   qui`; (d) decodifica il ROT13 `Btav tvbeab ha rfrepvmvb`.

### ★★ Intermedio

6. Dalla riga `x <b>uno</b> y <b>due</b> z <b>tre</b>` estrai le tre parole in grassetto, una per riga, con **due** metodi: uno che funzioni con qualunque `grep -E`, uno con `grep -P`. Spiega perché `grep -oE '<b>.*</b>'` non va bene.
7. Dall'output di `ls -l /usr/bin | tail -n +2`, stampa solo dimensione e nome dei 5 file più grandi. Prima prova con `cut` e spiega perché fallisce; poi risolvi con `awk` e `sort`.
8. Da `/etc/passwd`: (a) la classifica degli shell di login (Esempio 5); (b) gli utenti ordinati per UID decrescente, solo nome e UID; (c) l'utente con l'UID più alto sotto 65534. Usa `cut`, `sort`, `awk` come preferisci, ma spiega ogni passaggio.
9. **`sed`.** Crea un file con queste righe:
   ```
   # configurazione
   Port 22

   PermitRootLogin yes
   # fine
   Rossi, Mario
   path=/usr/local/bin
   ```
   Con un comando `sed` per ciascuna richiesta: (a) stampa solo le righe dalla 2 alla 4; (b) elimina commenti e righe vuote; (c) trasforma `Rossi, Mario` in `Mario Rossi` con un riferimento all'indietro; (d) sostituisci `/usr/local` con `/opt` usando un delimitatore diverso da `/`; (e) cambia `yes` in `no` solo nella riga che contiene `PermitRootLogin`.
10. **`awk`.** Crea `voti.txt` con le righe `anna 28`, `bruno 24`, `anna 30`, `carla 18`, `bruno 27`. Con `awk`: (a) la somma e la media di tutti i voti; (b) il voto massimo e chi l'ha preso; (c) la media per studente (array associativo); (d) solo gli studenti con media ≥ 25.
11. **Log.** Crea un piccolo log con:
    ```bash
    printf '%s\n' \
    '10.0.0.1 - - [07/Nov/2026:10:00:01 +0000] "GET / HTTP/1.1" 200 512 "-" "curl"' \
    '10.0.0.2 - - [07/Nov/2026:10:00:02 +0000] "GET /admin HTTP/1.1" 403 128 "-" "curl"' \
    '10.0.0.1 - - [07/Nov/2026:10:00:03 +0000] "GET /x HTTP/1.1" 404 64 "-" "curl"' \
    '10.0.0.3 - - [07/Nov/2026:10:00:04 +0000] "POST /login HTTP/1.1" 200 256 "-" "Mozilla"' \
    '10.0.0.1 - - [07/Nov/2026:10:00:05 +0000] "GET /../../etc/passwd HTTP/1.1" 400 0 "-" "curl"' > mini.log
    ```
    Trova: (a) l'IP con più richieste; (b) quante risposte hanno codice 4xx; (c) il totale dei byte inviati; (d) le richieste che sembrano un tentativo di *path traversal*; (e) quali IP hanno usato `curl` come *User-Agent*.
12. **`strings`.** Su `/bin/ls`: (a) quante stringhe di almeno 10 caratteri contiene? (b) trova il messaggio d'uso (`Usage`); (c) qual è la versione più alta di GLIBC citata (suggerimento: `grep GLIBC_` e `sort -V`)? Che cosa ti dice questa informazione? (La ritroveremo nel Modulo 4.)

### ★★★ Sfida

13. **Analisi delle frequenze.** Questo testo italiano è cifrato con un cifrario di Cesare con spostamento sconosciuto:
    ```
    uls tlggv kls jhttpu kp uvzayh cpah tp ypayvchp wly buh zlsch vzjbyh jol sh kpypaah cph lyh zthyypah hop xbhuav h kpy xbhs lyh l jvzh kbyh lzah zlsch zlschnnph l hzwyh l mvyal jol uls wluzply ypuvch sh whbyh
    ```
    Con una catena di comandi, calcola la frequenza delle lettere. Fai un'ipotesi su quale lettera in chiaro corrisponde alla più frequente, deduci lo spostamento e decifra con `tr`. Se la prima ipotesi non funziona, prova la seconda: spiega perché la prima ipotesi "ovvia" potrebbe essere sbagliata su un testo breve.
14. **Mini-CTF.** Nella cartella di questa lezione c'è `setup_sfida.sh`. Eseguilo con `bash setup_sfida.sh`: crea `~/l3_sfida` con quattro file. **Non leggerne il contenuto.** Leggi `~/l3_sfida/LEGGIMI.txt` e ricostruisci la flag `L3{...}`. Ogni pezzo richiede uno strumento diverso, e almeno uno contiene una trappola descritta nella Parte I.
15. **ReDoS.** (a) Spiega perché `^(\w+\s?)*$` è vulnerabile al backtracking catastrofico, indicando il quantificatore annidato e l'ambiguità. (b) Misuralo con Python per input `'a'*n + '!'` con n = 16, 18, 20, 22:
    ```bash
    for n in 16 18 20 22; do python3 -c "
    import re, time; t = time.time(); re.match(r'^(\w+\s?)*\$', 'a'*$n + '!'); print($n, round(time.time()-t, 2), 's')"; done
    ```
    (c) Scrivi un'espressione equivalente per le stringhe "parole separate da un solo spazio facoltativo" che non abbia il problema, e verificala con lo stesso test.
16. **Teoria (sicurezza).** Un amministratore permette agli utenti di eseguire con privilegi, tramite `sudo`, uno script che contiene la riga `grep -i $1 /var/log/app.log`. (a) Quale input fa leggere a `grep` anche `/etc/shadow`? Spiega usando la divisione in parole (L1 §8.6). (b) Anche con `"$1"` tra virgolette, quale input inizia a cambiare il comportamento di `grep`, e perché? (c) Scrivi la riga corretta. (d) Quali classi CWE sono coinvolte?
17. **Teoria (convalida).** Un servizio controlla che un nome utente sia valido con `echo "$nome" | grep -qE '[a-z0-9]+'`. (a) Trova tre input che passano il controllo ma non dovrebbero (almeno uno pericoloso se il nome finisse in un comando). (b) Correggi la regex. (c) In Python, `re.match(r'^[a-z0-9]+$', nome)` accetta `'admin\n'`: perché, e quale funzione o ancora va usata per un controllo rigoroso?

### Allenamento su pwn.college

Nel dojo **Linux Luminarium** completa *Practicing Piping* e torna su *Comprehending Commands* per le sfide su `grep`, `find` e `diff`. Se nel dojo è disponibile il modulo sulle espressioni regolari o *Data Manipulation*, affrontalo dopo questa lezione. Come sempre, annota comando risolutivo e sezione della lezione.

## 18. Domande di autoverifica

1. Che cos'è una riga per POSIX? Perché `wc -l` può dare 0 su un file che contiene testo?
2. Che cosa cambia in un file con terminatori `\r\n`, e come lo riconosci?
3. Perché la locale influenza `sort`, `wc -m` e gli intervalli `[a-z]`? Quando usi `LC_ALL=C`?
4. Qual è la differenza tra un glob e un'espressione regolare? Perché le regex vanno tra virgolette singole?
5. Quali sono le differenze principali tra BRE, ERE e PCRE? Quale usi di default e perché?
6. Che cosa vuol dire "avido" e "pigro"? Come estrai il contenuto tra due delimitatori in modo portabile?
7. Come funziona un motore a backtracking, e perché `(a+)+$` può richiedere tempo esponenziale? Come si chiama l'attacco?
8. Perché `uniq` richiede quasi sempre `sort` prima? Scrivi la catena della classifica delle frequenze.
9. Descrivi il ciclo di funzionamento di `sed` e il significato di `-n`, `p`, `&`, `\1`, `-i`.
10. Descrivi il modello di `awk`: record, campi, `NR`, `NF`, `BEGIN`, `END`, array associativi. Quando preferisci `awk` a `cut`?
11. Che cosa fa `strings`, e perché a volte non trova una stringa che c'è? (Due motivi.)
12. Fai due esempi di dati esterni che diventano istruzioni attraverso `grep`, `sed` o `awk`, e la relativa difesa.

## 19. Riepilogo

- Il testo è una convenzione sui byte: righe terminate da `\n`, codifica decisa dalla locale. `\r` invisibili, ultime righe senza terminatore e locale diverse sono le cause più comuni di risultati sbagliati: `cat -A` e `LC_ALL=C` sono i primi rimedi.
- Un'espressione regolare descrive un insieme di stringhe con concatenazione, alternativa e ripetizione, più classi, ancore e gruppi. Ne esistono tre dialetti (BRE, ERE, PCRE): `grep -E` per default, `grep -P` quando servono le funzioni avanzate.
- I motori ad automa sono lineari; quelli a backtracking possono essere esponenziali, e questo è il ReDoS.
- `grep` filtra righe; `tr` trasforma caratteri; `cut`, `sort`, `uniq`, `comm` tagliano, ordinano, contano e confrontano; `sed` modifica il flusso riga per riga; `awk` è un linguaggio per dati a colonne; `strings` estrae il testo dai binari.
- La catena `sort | uniq -c | sort -rn` e l'estrazione con `grep -o` sono i due schemi più usati in gara.
- Ogni volta che un dato esterno diventa un modello, un programma o una riga di log, può essere interpretato come istruzione: `-F`, `--`, `-v` di awk, ancore complete.

## 20. Fonti

- **OccupyTheWeb**, *Linux Basics for Hackers*, cap. 2 (*Text Manipulation*: `head`, `tail`, `nl`, `grep`, `sed`, `more`, `less`).
- **Al Sweigart**, *Automate the Boring Stuff with Python*, 2ª ed., cap. 7 (*Pattern Matching with Regular Expressions*): regex in Python, avido e non avido, gruppi.
- **pwn.college**, *Linux Luminarium*, moduli *Practicing Piping* e *Comprehending Commands* (trascrizione 088 per l'introduzione ai comandi).
- **D. Andriesse**, *Practical Binary Analysis*, cap. 5 (*Basic Binary Analysis in Linux*): `strings`, `file` e i primi passi su un binario sconosciuto.
- **S. C. Kleene**, *Representation of Events in Nerve Nets and Finite Automata* (RAND, 1951; in *Automata Studies*, 1956).
- **K. Thompson**, *Regular Expression Search Algorithm*, Communications of the ACM 11(6), 1968.
- **A. V. Aho, B. W. Kernighan, P. J. Weinberger**, *The AWK Programming Language*, Addison-Wesley, 1988 (2ª ed. 2023).
- **R. Cox**, *Regular Expression Matching Can Be Simple And Fast* (2007), swtch.com/~rsc/regexp: automi contro backtracking, con le misure del caso esponenziale.
- **POSIX.1-2017**, *Base Definitions* cap. 9 *Regular Expressions* (BRE ed ERE) e definizione di *line* (cap. 3).
- **Manuali GNU**: `grep`, `sed` (`info sed`, *Execution Cycle*), `gawk`; pagine `regex(7)`, `tr(1)`, `sort(1)`, `uniq(1)`, `cut(1)`, `strings(1)`, `pcre2pattern(3)`.
- **MITRE CWE**: CWE-20, CWE-78, CWE-88, CWE-117, CWE-185, CWE-1333.

## 21. Prossima lezione

**Lezione 4 — Flussi, pipe e script**: i descrittori di file 0, 1, 2, tutte le redirezioni, le pipe e che cosa fa il kernel quando le crea, `xargs`, `tee`, la sostituzione di processo, e i primi script bash con condizioni, cicli e funzioni. Le catene di questa lezione diventeranno programmi.
