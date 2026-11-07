#!/usr/bin/env bash
# Prepara la sfida della Lezione 2 in ~/l2_sfida. Non leggere oltre: esegui e basta.
# Crea file solo dentro ~/l2_sfida e avvia un processo "guardiano" (sleep) che si chiude da solo dopo 2 ore.
set -e
D="$HOME/l2_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
mkdir -p "$D"; cd "$D"
d(){ printf '%s' "$1" | base64 -d; }
# Parte 1: un labirinto di note quasi identiche
for i in $(seq 1 40); do
  p="labirinto/$((RANDOM%5))/$((RANDOM%7))/$i"; mkdir -p "$p"; echo "non qui" > "$p/nota.txt"
done
p="labirinto/$((RANDOM%5))/$((RANDOM%7))/41"; mkdir -p "$p"; d 'TDJ7dHV0dG9f' > "$p/nota.txt"
touch -d '2019-03-14 15:09' "$p/nota.txt"
# Parte 2: un'immagine che non è un'immagine
d 'ZV91bl9maWxlXw==' | gzip -c > foto.png
# Parte 3: una porta che sembra rotta
mkdir -p ingresso archivio; d 'YW5jaGVfcXVhbmRvXw==' > archivio/p3.txt
ln -s archivio/p3.txt ingresso/porta
# Parte 4: il guardiano
d 'bm9uX2NfZX0=' > .ultimo_pezzo
nohup bash -c 'exec 3<.ultimo_pezzo; rm -f .ultimo_pezzo; exec -a guardiano sleep 7200' >/dev/null 2>&1 &
sleep 0.5
cat > LEGGIMI.txt <<'X'
La flag è divisa in quattro pezzi.
1. Tra 41 note uguali, una sola è vecchia di anni.
2. Una foto che non si lascia guardare.
3. Una porta che non si apre: leggi bene dove porta.
4. L'ultimo pezzo è stato cancellato, ma il guardiano lo tiene ancora in mano.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
