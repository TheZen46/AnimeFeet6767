# Modulo 1 — Lezione 3: soluzioni

> Apri questo file solo dopo aver provato gli esercizi. Gli output sono stati verificati con GNU grep 3.11, GNU sed 4.9, mawk 1.3.4 e Python 3 su Linux; il contenuto di `/etc/passwd` e `/usr/bin` sarà diverso sul tuo sistema. I riferimenti `§` rimandano alle sezioni di `Lezione.md`.

## ★ Base

**1.**
```
$ printf 'user=admin\r\npass=1234\r\n' > conf.txt
$ cat -A conf.txt
user=admin^M$
pass=1234^M$
$ od -c conf.txt
0000000   u   s   e   r   =   a   d   m   i   n  \r  \n   p   a   s   s
0000020   =   1   2   3   4  \r  \n
$ tr -d '\r' < conf.txt > unix1.txt
$ sed 's/\r$//' conf.txt > unix2.txt
$ grep -c '^pass=1234$' unix1.txt unix2.txt
unix1.txt:1
unix2.txt:1
```
`file conf.txt` dice *ASCII text, with CRLF line terminators*; sui file corretti solo *ASCII text* (alcune versioni recenti di `file` riconoscono certi contenuti come *CSV text* e non segnalano il CRLF: `cat -A` resta il controllo affidabile). Differenza tra i due metodi: `tr -d '\r'` toglie **tutti** i `\r`, anche quelli in mezzo a una riga; `sed 's/\r$//'` solo quello finale. Di solito è indifferente; con dati binari no (§1.2).

**2.**
| Regex | Corrisponde in | Perché |
|---|---|---|
| (a) `^a.c$` | `abc`, `a.c` | esattamente tre caratteri: `a`, uno qualsiasi, `c` |
| (b) `ab*c` | `ac`, `abc`, `abbc` | `b*` ammette zero `b`; `Abc` non ha una `a` minuscola |
| (c) `ab+c` | `abc`, `abbc` | almeno una `b` |
| (d) `a\.c` | `a.c` | il punto è letterale |
| (e) `^[[:upper:]][a-z]{2}$` | `Abc` | una maiuscola e **esattamente** due minuscole fino alla fine: `Abcd` ne ha tre |
| (f) `[^0-9]` | tutte tranne `123` | basta **un** carattere che non sia una cifra in un punto qualsiasi |
| (g) `^[^0-9]+$` | tutte tranne `123` | qui **tutta** la riga deve essere senza cifre; in questi dati coincide con (f), ma `a1` passerebbe (f) e non (g) |

La coppia (f)–(g) è il cuore del punto 3 del §15: senza ancore, una regex controlla solo che **esista** una sottostringa adatta.

**3.**
```
$ grep '/bin/bash$' /etc/passwd             # (a): $ evita di prendere ad esempio /bin/bash2
$ grep -c '/bin/bash$' /etc/passwd          # (b)
$ grep -v 'nologin' /etc/passwd             # (c)
$ grep -E '^[^:]*:[^:]*:0:' /etc/passwd     # (d)
root:x:0:0:root:/root:/bin/bash
```
In (d), `[^:]*:` corrisponde a "un campo e il suo separatore": due volte saltano nome e password, poi `0:` deve essere il terzo campo **intero**. Cercare solo `:0:` troverebbe anche un utente con GID 0 (quarto campo) o un campo di commento che contiene `:0:`; cercare `:0` troverebbe anche UID 0**1000**. Un'alternativa più leggibile: `awk -F: '$3 == 0' /etc/passwd`.

**4.**
```
$ head -n 15 /etc/services | tail -n 1
$ sed -n '15p' /etc/services
$ awk 'NR == 15' /etc/services
$ sed -n '15,20p' /etc/services            # righe da 15 a 20 (anche: awk 'NR>=15 && NR<=20')
```
`sed -n '15p;20q'` si ferma alla riga 20 senza leggere il resto del file: su file enormi fa la differenza.

**5.**
```
$ echo 'Ciao Mondo' | tr 'a-z' 'A-Z'                     # (a) CIAO MONDO   (anche: tr '[:lower:]' '[:upper:]')
$ echo 'a1b2c3' | tr -d '0-9'                            # (b) abc
$ echo 'molti     spazi   qui' | tr -s ' '               # (c) molti spazi qui
$ echo 'Btav tvbeab ha rfrepvmvb' | tr 'A-Za-z' 'N-ZA-Mn-za-m'   # (d) Ogni giorno un esercizio
```

## ★★ Intermedio

**6.**
```
$ L='x <b>uno</b> y <b>due</b> z <b>tre</b>'
$ echo "$L" | grep -oE '<b>[^<]*</b>' | sed -E 's/<\/?b>//g'       # ERE + sed: qualunque grep
uno
due
tre
$ echo "$L" | grep -oP '<b>\K[^<]*(?=</b>)'                       # PCRE (anche con .*? al posto di [^<]*)
uno
due
tre
```
`grep -oE '<b>.*</b>'` restituisce `<b>uno</b> y <b>due</b> z <b>tre</b>` in un pezzo solo: `.*` è avido e, nei motori POSIX, la corrispondenza scelta è la più lunga che inizia più a sinistra, quindi arriva all'**ultima** `</b>` (§4.5).

**7.**
```
$ ls -l /usr/bin | tail -n +2 | cut -d' ' -f5
                     (righe vuote, o numeri di link, o nomi di gruppo: dipende dall'allineamento)
$ ls -l /usr/bin | tail -n +2 | awk '{print $5, $NF}' | sort -rn | head -5
199114624 pandoc
112566024 dockerd
...
```
`ls -l` allinea le colonne con spazi multipli: per `cut`, ogni spazio è un separatore e due spazi consecutivi racchiudono un campo vuoto, quindi la numerazione dei campi cambia da riga a riga (§9.1, Esempio 4). `awk` divide su sequenze di spazi. `sort -rn` ordina numericamente in modo decrescente sulla prima colonna. Limite: `$NF` è l'ultima parola, quindi per i link simbolici stampa la **destinazione**, e i nomi con spazi vengono tagliati; per uno script serio `find /usr/bin -maxdepth 1 -type f -printf '%s %f\n' | sort -rn | head -5`.

**8.**
```
$ cut -d: -f7 /etc/passwd | sort | uniq -c | sort -rn             # (a)
$ cut -d: -f1,3 /etc/passwd | sort -t: -k2,2nr | tr ':' ' '        # (b)
$ awk -F: '$3 < 65534 && $3 > max {max = $3; u = $1} END {print u, max}' /etc/passwd   # (c)
```
(b): `cut` tiene nome e UID; `sort -t: -k2,2nr` ordina sul secondo campo (solo quello: `2,2`), numericamente (`n`), al contrario (`r`). (c): awk scorre le righe tenendo il massimo visto finora tra quelli sotto 65534 (che è `nobody`, un valore convenzionale); una variabile non inizializzata vale 0, quindi `max` parte da 0.

**9.**
```
$ sed -n '2,4p' c.txt                                   # (a)  Port 22 / (riga vuota) / PermitRootLogin yes
$ sed -E '/^[[:space:]]*(#|$)/d' c.txt                  # (b)
$ sed -E 's/^([^,]+), (.+)$/\2 \1/' c.txt               # (c)  Rossi, Mario → Mario Rossi
$ sed 's|/usr/local|/opt|' c.txt                        # (d)  path=/opt/bin
$ sed '/PermitRootLogin/s/yes/no/' c.txt                # (e)
```
(b) usa un solo indirizzo regex per due casi: righe che, dopo eventuali spazi, iniziano con `#` oppure finiscono subito (righe vuote). (c) cattura "tutto fino alla virgola" e "il resto", poi li scambia. (e) combina un indirizzo e un comando: la sostituzione si applica solo alle righe che corrispondono a `/PermitRootLogin/` (§10.2). È esattamente come si modifica una configurazione in uno script; con `-i` diventerebbe permanente (§10.5).

**10.**
```
$ awk '{s += $2} END {print s, s/NR}' voti.txt                       # (a)  127 25.4
$ awk 'NR == 1 || $2 > m {m = $2; c = $1} END {print c, m}' voti.txt  # (b)  anna 30
$ awk '{s[$1] += $2; n[$1]++} END {for (k in s) print k, s[k]/n[k]}' voti.txt | sort   # (c)
anna 29
bruno 25.5
carla 18
$ awk '{s[$1] += $2; n[$1]++} END {for (k in s) if (s[k]/n[k] >= 25) print k}' voti.txt | sort   # (d)
anna
bruno
```
In (b), `NR == 1 ||` inizializza il massimo con il primo valore: senza, con voti tutti negativi il massimo resterebbe 0. In (c) due array con lo stesso indice (il nome) accumulano somma e conteggio; `sort` perché l'ordine di `for (k in s)` non è garantito (§11.3).

**11.**
```
$ awk '{print $1}' mini.log | sort | uniq -c | sort -rn | head -1          # (a)   3 10.0.0.1
$ awk '$9 ~ /^4/' mini.log | wc -l                                         # (b)   3  (403, 404, 400)
$ awk '{s += $10} END {print s}' mini.log                                  # (c)   960
$ grep -F '../' mini.log                                                   # (d)   la richiesta di /../../etc/passwd
$ awk -F'"' '$6 == "curl"' mini.log | awk '{print $1}' | sort -u           # (e)   10.0.0.1 10.0.0.2
```
(b) usa l'operatore `~` di awk, "corrisponde alla regex", sul campo 9. (d) usa `-F` perché `.` sarebbe speciale. (e) è il trucco più interessante: con `"` come separatore, i campi sono le parti **tra** virgolette, e il sesto è lo *User-Agent*. Un log è un formato a più livelli di separatori, e conviene sceglierne uno diverso per ogni domanda. Il codice 400 sulla richiesta di traversal dice che il server l'ha rifiutata: l'attacco c'è stato, ma probabilmente non è riuscito (Modulo 6).

**12.**
```
$ strings -n 10 /bin/ls | wc -l                     # (a) qualche centinaio (580 nel sistema di prova)
$ strings /bin/ls | grep -i usage                   # (b) Usage: %s [OPTION]... [FILE]...
$ strings /bin/ls | grep GLIBC_ | sort -uV | tail -1   # (c) per esempio GLIBC_2.38
```
Le stringhe `GLIBC_2.x` sono le **versioni dei simboli** della libreria C richieste dal programma (Modulo 2): ti dicono la versione **minima** di glibc con cui il binario funziona, e quindi, approssimativamente, su quale distribuzione è stato compilato. Nel Modulo 4 questa informazione serve a scegliere la versione giusta della libreria quando si analizza un binario di una sfida.

## ★★★ Sfida

**13.**
```
$ C='uls tlggv kls jhttpu ...'      # il testo cifrato completo
$ echo "$C" | grep -o '[a-z]' | sort | uniq -c | sort -rn | head -4
     30 h
     19 l
     17 y
     15 p
```
**Prima ipotesi**, quella "da manuale": la più frequente in italiano è la `e`, quindi `h → e`, spostamento 3 (da `e` a `h`). Decifrando con `tr 'd-za-c' 'a-z'` si ottiene un testo senza senso. **Seconda ipotesi**: `h → a`, spostamento 7.
```
$ echo "$C" | tr 'h-za-g' 'a-z'
nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura che la diritta via era smarrita ahi quanto a dir qual era e cosa dura esta selva selvaggia e aspra e forte che nel pensier rinova la paura
```
La conferma viene dalla seconda lettera più frequente, `l`, che con spostamento 7 diventa `e`. In un testo breve le frequenze reali si discostano da quelle medie della lingua: qui, nei primi versi della *Commedia*, la `a` supera la `e`. Per questo l'analisi delle frequenze va usata come **ordine dei tentativi**, verificando ogni ipotesi, e funziona meglio su testi lunghi. Nel Modulo 5 la renderemo quantitativa (test del chi quadro).

**14.** Flag: `L3{il_testo_si_doma_con_grep_sed_e_awk}`

```
$ cd ~/l3_sfida; cat LEGGIMI.txt
```
1. **Il log.** Ci sono centinaia di richieste `pezzo=L3{...` false; quella vera ha il codice **418** (*I'm a teapot*, RFC 2324, un pesce d'aprile diventato celebre):
   ```
   $ grep -c 'pezzo=' access.log
   256                                   (il numero varia)
   $ awk '$9 == 418' access.log
   31.251.26.37 - - [...] "POST /teiera?pezzo=L3{il_testo_ HTTP/1.1" 418 2380 "-" "Mozilla/5.0"
   ```
   Anche `grep '" 418 '` funziona: la virgoletta e gli spazi evitano corrispondenze con `418` dentro un IP o una dimensione.
2. **Le parole.** Ogni riga compare due volte tranne una: è la definizione di `uniq -u`, che richiede l'input ordinato (§9.3).
   ```
   $ sort parole.txt | uniq -u
   si_doma_
   ```
3. **Il dump.** "Due byte per ogni lettera" è l'UTF-16 (§12): ogni carattere ASCII è seguito da un byte zero, e `strings` normale non vede nulla.
   ```
   $ strings -e l -n 6 dump.bin
   con_grep_
   ```
   (Senza `-n 6` potresti vedere anche qualche sequenza casuale corta.)
4. **Il CSV.** La trappola è il `\r` di Windows (§1.2): l'etichetta è l'**ultimo** campo, quindi contiene `segreto\r`, e il confronto esatto fallisce.
   ```
   $ awk -F, '$3 == "segreto"' dati.csv | wc -l
   0
   $ cat -A dati.csv | head -2
   id,valore,etichetta^M$
   1,qkxbi_tazr,interno^M$
   $ tr -d '\r' < dati.csv | awk -F, '$3 == "segreto" {print $2}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
   sed_e_awk}
   ```
   `grep segreto dati.csv` avrebbe trovato la riga, perché `grep` cerca una sottostringa: ma è il confronto esatto, quello che faresti in uno script, a fallire. Il valore `frq_r_njx}` decifrato con ROT13 (§8) dà l'ultimo pezzo.

**15.**
(a) Il gruppo `(\w+\s?)` è ripetuto da `*`, e contiene a sua volta `\w+`. Poiché `\s?` può essere **vuoto**, una sequenza di `a` senza spazi si può dividere tra le ripetizioni del gruppo in tutti i modi possibili (`aaaa` = `a|aaa`, `aa|aa`, `a|a|a|a`, …): 2^(n−1) modi per n lettere. Quando la corrispondenza fallisce a causa del `!` finale, un motore a backtracking li prova tutti (§5.2).
(b) Misure tipiche: il tempo cresce di circa 4–5 volte ogni due caratteri in più (0,02 s a 18, 0,1 s a 20, mezzo secondo a 22 nel sistema di prova).
(c) `^\w+(\s\w+)*$`: ogni ripetizione del gruppo **deve** iniziare con uno spazio, quindi una sequenza di lettere senza spazi si può dividere in **un solo** modo. Il test risponde in un decimo di millisecondo per ogni n. Descrive lo stesso insieme (parole separate da uno spazio), salvo che non accetta uno spazio finale; se serve, `^\w+(\s\w+)*\s?$`.

**16.** Risposta modello.
(a) Con `$1` non quotato, l'argomento viene diviso in parole (L1 §8.6). L'input `. /etc/shadow` produce `grep -i . /etc/shadow /var/log/app.log`: `grep` riceve il modello `.` (qualunque carattere) e **due** file e, girando con i privilegi concessi da `sudo`, stampa tutte le righe non vuote di `/etc/shadow`, cioè gli hash delle password di tutti gli utenti.
(b) Con `"$1"` la divisione sparisce, ma un input che inizia con `-` viene ancora interpretato come opzione: `--file=/etc/shadow` fa usare a `grep` le righe di `/etc/shadow` come **modelli**; `-r` o `--include` cambiano dove cerca; `-v` inverte il risultato. È l'*argument injection* (L1 §6.2).
(c) `grep -i -F -e "$1" -- /var/log/app.log`: virgolette contro la divisione in parole, `-e` per dichiarare che il valore è un modello anche se inizia con `-`, `-F` perché sia una stringa letterale e non una regex (niente `.*`, niente ReDoS), `--` per chiudere le opzioni.
(d) CWE-88 (*Argument Injection*), e in senso più ampio CWE-77/CWE-78 (*Command Injection*) quando l'input arriva a formare il comando; se la regex fosse lasciata libera, anche CWE-1333 (ReDoS). Lo scenario è un classico delle configurazioni `sudo` errate, che riprenderemo nella Lezione 6.

**17.** Risposta modello.
(a) La regex non ha ancore, quindi accetta qualunque stringa che **contenga** una lettera minuscola o una cifra: `Admin!` (maiuscola e punteggiatura), `a b` (spazio), `x; rm -rf ~` (se il nome finisse in un comando di shell, un'esecuzione di comandi), `../../etc/passwd` (se finisse in un percorso, un *path traversal*), una stringa con un `\n` seguito da una seconda riga arbitraria (`grep` controlla riga per riga, e basta che **una** riga corrisponda).
(b) `grep -qxE '[a-z0-9]{1,32}'` (`-x`: l'intera riga) oppure `grep -qE '^[a-z0-9]{1,32}$'`. Il limite di lunghezza è una buona abitudine. Resta il problema delle righe multiple: in bash si controlla meglio senza `grep`, con `[[ $nome =~ ^[a-z0-9]{1,32}$ ]]`, che lavora sull'intera stringa (Lezione 4).
(c) In Python `$` corrisponde alla fine della stringa **oppure** subito prima di un `\n` finale; quindi `re.match(r'^[a-z0-9]+$', 'admin\n')` restituisce una corrispondenza. Per un controllo rigoroso: `re.fullmatch(r'[a-z0-9]+', nome)` oppure l'ancora assoluta `\Z` di Python (`r'\A[a-z0-9]+\Z'`). Attenzione: in PCRE `\Z` ha lo stesso difetto di `$` e l'ancora assoluta è `\z`. È la classe CWE-185 (*Incorrect Regular Expression*) e, più in generale, CWE-20.

## Domande di autoverifica: punti chiave attesi

1. Una sequenza di caratteri **terminata** da `\n`; `wc -l` conta i `\n`, quindi un file senza terminatore finale ne ha uno in meno (§1.1).
2. Ogni riga finisce con `\r` prima del `\n`: le ancore `$` e i confronti esatti falliscono. `cat -A` (`^M`), `od -c`, `file` (§1.2).
3. La locale stabilisce codifica e ordine: `wc -m` conta caratteri secondo la codifica, `sort` e gli intervalli seguono l'ordine della lingua. `LC_ALL=C` negli script e sui dati binari (§1.3).
4. Il glob è della shell, sui nomi di file, deve corrispondere al nome intero; la regex è del programma, sul testo, cerca una sottostringa. Le virgolette impediscono alla shell di espandere la regex come se fosse un glob (§3.3).
5. In BRE `+ ? | ( ) { }` sono letterali senza backslash; ERE li rende speciali; PCRE aggiunge `\d`, pigri, *lookaround*. Default: `grep -E` (§4.4).
6. Avido: più caratteri possibile; pigro: meno possibile. Portabile: classe negata, `\{[^}]*\}` (§4.5).
7. Prova una strada e torna indietro quando fallisce; con quantificatori annidati ambigui le strade sono esponenziali. ReDoS, CWE-1333 (§5).
8. `uniq` confronta solo righe consecutive. `sort | uniq -c | sort -rn` (§9.3).
9. Legge una riga nello spazio di lavoro, applica i comandi con indirizzo corrispondente, stampa (salvo `-n`). `p` stampa, `&` è la corrispondenza, `\1` il primo gruppo, `-i` modifica il file sostituendolo (§10).
10. Record (righe) e campi (parole); `NR` numero di record, `NF` numero di campi; `BEGIN` ed `END` prima e dopo l'input; array con indici stringa. `awk` quando i separatori sono sequenze di spazi o servono calcoli e condizioni (§11).
11. Estrae sequenze di caratteri stampabili. Non trova stringhe in UTF-16 senza `-e l`, né stringhe costruite a runtime o cifrate (§12).
12. Per esempio: input usato come modello di `grep` (`-F -e ... --`), input incollato in un programma awk (`-v`), input che finisce in una riga di log con un `\n` (neutralizzare gli a capo) (§15).
