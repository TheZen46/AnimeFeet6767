#!/usr/bin/env bash
# Prepara la sfida della Lezione 6 in ~/l6_sfida. Non leggere oltre: esegui e basta.
# Crea file e directory solo dentro ~/l6_sfida; non richiede privilegi e non ne usa.
set -e
D="$HOME/l6_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala (o eliminala, ricordando di ridarle i permessi con chmod -R u+rwx) e riprova"; exit 1; fi
umask 022
mkdir -p "$D"; cd "$D"
d(){ printf '%s' "$1" | base64 -d; }
# 1. il file chiuso
d 'TDZ7aV9wZXJtZXNzaV8=' > chiuso.txt; echo >> chiuso.txt; chmod 000 chiuso.txt
# 2. l'archivio che si può leggere ma non attraversare
mkdir archivio
for n in registro inventario "$(d 'cmFjY29udGFub18=')" verbale protocollo; do echo "niente qui" > "archivio/$n"; done
chmod 444 archivio
# 3. le firme: contano solo quelle con il bit giusto
mkdir firme
veri=(07 13 21 28); pezzi=('Y2g=' 'aV8=' 'cHU=' 'b18=')
for i in $(seq -w 1 30); do
  printf '%s' "$(head -c 2 /dev/urandom | od -A n -t x1 | tr -d ' \n' | cut -c1-2)" > "firme/f$i"
  case $((10#$i % 3)) in 0) chmod 2755 "firme/f$i" ;; 1) chmod 1755 "firme/f$i" ;; *) chmod 0755 "firme/f$i" ;; esac
done
for k in 0 1 2 3; do d "${pezzi[$k]}" > "firme/f${veri[$k]}"; chmod 4755 "firme/f${veri[$k]}"; done
# 4. il codice scritto nei permessi
mkdir codice
i=0
for m in 146 141 162 145 137 143 157 163 141 175; do i=$((i+1)); : > "codice/c$(printf '%02d' $i)"; chmod "$m" "codice/c$(printf '%02d' $i)"; done
cat > LEGGIMI.txt <<'X'
La flag è divisa in quattro pezzi. Nessuno è nascosto: sono tutti protetti, o scritti, dai permessi.
1. chiuso.txt non si lascia leggere. Ma di chi è?
2. In archivio/ non si entra. Però i nomi si vedono, e un nome è il messaggio.
3. In firme/ ci sono trenta file. Conta solo chi ha il bit dell'utente proprietario (setuid), in ordine di nome.
4. In codice/ i file sono vuoti: il messaggio è nei loro permessi, letti in ottale come codici ASCII.
Alla fine rimetti in ordine: ridai a te stesso i permessi su tutto, così potrai cancellare la cartella.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
