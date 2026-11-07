#!/usr/bin/env bash
# Prepara la sfida della Lezione 4 in ~/l4_sfida. Non leggere oltre: esegui e basta.
# Crea solo file dentro ~/l4_sfida.
set -e
D="$HOME/l4_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
mkdir -p "$D"; cd "$D"

cat > porta1 <<'X'
#!/usr/bin/env bash
for i in $(seq 1 5000); do
  echo "L4{falso_$((RANDOM % 9000 + 1000))_"
  [ "$i" -eq 2718 ] && printf '%s\n' "$(printf 'TDR7Zmx1c3NpXw==' | base64 -d)" >&2
done
X

cat > porta2 <<'X'
#!/usr/bin/env bash
if ! { read -r k <&3; } 2>/dev/null; then
  echo "porta2: mi serve la chiave su un descrittore che non è né 0, né 1, né 2" >&2; exit 1
fi
if [ "$k" = "apriti" ]; then printf '%s\n' "$(printf 'ZV9waXBlXw==' | base64 -d)"; else echo "porta2: chiave sbagliata" >&2; exit 2; fi
X
echo "apriti" > chiave.txt

cat > oracolo <<'X'
#!/usr/bin/env bash
[ $# -eq 1 ] || { echo "uso: oracolo NUMERO (da 0 a 999)" >&2; exit 2; }
for c in $(printf 'MTc6YyAxMDE6aSAyMzM6YyA0MDQ6bCA2NjY6aSA5OTk6Xw==' | base64 -d); do
  [ "${c%%:*}" = "$1" ] && { printf '%s' "${c#*:}"; exit 0; }
done
echo "no" >&2; exit 1
X

cat > porta4 <<'X'
#!/usr/bin/env bash
inizio=$SECONDS
for i in $(seq 1 50); do
  a=$((RANDOM % 1000)); b=$((RANDOM % 1000))
  echo "Domanda $i di 50: quanto fa $a + $b?"
  if ! read -r -t 10 r; then echo "Troppo lento."; exit 1; fi
  if [ "$r" != "$((a + b))" ]; then echo "Sbagliato: $a + $b = $((a + b))."; exit 1; fi
done
if (( SECONDS - inizio > 10 )); then echo "Giusto, ma troppo lento: avevi 10 secondi in tutto."; exit 1; fi
echo "Bravo: $(printf 'ZV9jb3Byb2Nlc3NpfQ==' | base64 -d)"
X
chmod +x porta1 porta2 oracolo porta4

cat > LEGGIMI.txt <<'X'
La flag è divisa in quattro pezzi, uno per programma. Non leggere i programmi: usali.
1. porta1 urla tante bugie su un canale e sussurra la verità sull'altro.
2. porta2 vuole la chiave (è in chiave.txt), ma non la legge da nessuno dei canali soliti.
3. oracolo risponde a un numero da 0 a 999. Quasi sempre dice "no". Mettendo in fila le risposte buone, in ordine, hai il terzo pezzo.
4. porta4 fa 50 domande e ti dà 10 secondi in tutto. Nessun umano ce la fa: scrivi uno script che risponda per te.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
