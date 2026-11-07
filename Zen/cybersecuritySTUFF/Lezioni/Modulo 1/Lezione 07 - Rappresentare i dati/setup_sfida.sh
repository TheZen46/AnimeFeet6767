#!/usr/bin/env bash
# Prepara la sfida della Lezione 7 in ~/l7_sfida. Non leggere oltre: esegui e basta.
# Crea quattro file solo dentro ~/l7_sfida; non avvia processi e non richiede privilegi.
set -e
D="$HOME/l7_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
mkdir -p "$D"; cd "$D"
d(){ printf '%s' "$1" | base64 -d; }
# 1. strati: testo -> esadecimale -> base64
d 'TDd7aV9ieXRlXw==' | od -A n -t x1 | tr -d ' \n' | base64 > strati.txt
# 2. numeri a 32 bit, nell'ordine dei byte della rete
p=$(d 'bm9uX2hhbm5vXw==')
for ((i = 0; i < ${#p}; i++)); do printf "\\x00\\x00\\x00\\x$(printf '%02x' "'${p:i:1}")"; done > numeri.bin
# 3. bit scritti con due lettere
p=$(d 'dW5fc29sb18=')
for ((i = 0; i < ${#p}; i++)); do
  v=$(printf '%d' "'${p:i:1}"); b=""
  for ((k = 7; k >= 0; k--)); do (( (v >> k) & 1 )) && b+="I" || b+="o"; done
  printf '%s ' "$b"
done > bit.txt; echo >> bit.txt
# 4. testo in un'altra codifica
p=$(d 'c2lnbmlmaWNhdG99')
{ printf '\xff\xfe'; for ((i = 0; i < ${#p}; i++)); do printf '%s\x00' "${p:i:1}"; done; printf '\n\x00'; } > ultimo.txt
cat > LEGGIMI.txt <<'X'
La flag è divisa in quattro pezzi, uno per file. Nessuno è cifrato: sono solo rappresentati in modi diversi.
1. strati.txt: due rappresentazioni una dentro l'altra. Toglile nell'ordine giusto.
2. numeri.bin: ogni carattere è un intero senza segno a 32 bit, scritto nell'ordine dei byte della rete.
3. bit.txt: otto bit per carattere, ma qualcuno ha usato lettere al posto delle cifre.
4. ultimo.txt: cat lo mostra quasi bene, grep non lo trova. Chiediti con quale codifica è scritto.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
