#!/usr/bin/env bash
# Prepara la sfida della Lezione 3 in ~/l3_sfida. Non leggere oltre: esegui e basta.
# Crea solo file dentro ~/l3_sfida.
set -e
D="$HOME/l3_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
mkdir -p "$D"; cd "$D"
d(){ printf '%s' "$1" | base64 -d; }
P1=$(d 'TDN7aWxfdGVzdG9f'); P2=$(d 'c2lfZG9tYV8='); P3=$(d 'Y29uX2dyZXBf'); P4=$(d 'c2VkX2VfYXdrfQ==')
# Parte 1: un log web con molti pezzi falsi
awk -v vero="$P1" 'BEGIN {
  srand(); split("200 200 200 200 301 302 404 404 403 500", st, " ")
  split("/ /index.html /login /admin.php /api/v1/users /robots.txt /static/app.js /teiera", pg, " ")
  split("GET GET GET POST HEAD", mt, " ")
  r = 1500 + int(rand()*1000)
  for (i = 1; i <= 3000; i++) {
    ip = int(rand()*223)+1 "." int(rand()*256) "." int(rand()*256) "." int(rand()*254)+1
    p = pg[int(rand()*8)+1]; s = st[int(rand()*10)+1]
    if (rand() < 0.08) { f = ""; for (k = 0; k < 9; k++) f = f substr("abcdefghijklmnopqrstuvwxyz_", int(rand()*27)+1, 1); p = "/teiera?pezzo=L3{" f "_" }
    if (i == r) { p = "/teiera?pezzo=" vero; s = 418 }
    printf "%s - - [07/Nov/2026:%02d:%02d:%02d +0000] \"%s %s HTTP/1.1\" %s %d \"-\" \"Mozilla/5.0\"\n", ip, int(i/180)%24, int(i/3)%60, i%60, mt[int(rand()*5)+1], p, s, int(rand()*9000)+100
  }
}' > access.log
# Parte 2: ogni riga compare due volte, tranne una
awk -v vero="$P2" 'BEGIN { srand(); for (i = 0; i < 600; i++) { w = ""; for (k = 0; k < 7; k++) w = w substr("abcdefghijklmnopqrstuvwxyz", int(rand()*26)+1, 1); print w "_"; print w "_" } print vero }' | awk 'BEGIN{srand()} {print rand() "\t" $0}' | sort | cut -f2 > parole.txt
# Parte 3: un dump binario
head -c 40000 /dev/urandom > dump.bin
printf '\0\0' >> dump.bin; printf '%s' "$P3" | sed 's/./&\x00/g' >> dump.bin; printf '\0\0' >> dump.bin
head -c 40000 /dev/urandom >> dump.bin
# Parte 4: un CSV arrivato da Windows
R4=$(printf '%s' "$P4" | tr 'A-Za-z' 'N-ZA-Mn-za-m')
awk -v vero="$R4" 'BEGIN { srand(); n = int(rand()*200)+50; print "id,valore,etichetta\r"
  split("pubblico interno bozza archivio", et, " ")
  for (i = 1; i <= 300; i++) { v = ""; for (k = 0; k < 10; k++) v = v substr("abcdefghijklmnopqrstuvwxyz_", int(rand()*27)+1, 1)
    if (i == n) printf "%d,%s,segreto\r\n", i, vero; else printf "%d,%s,%s\r\n", i, v, et[int(rand()*4)+1] } }' > dati.csv
cat > LEGGIMI.txt <<'X'
La flag è divisa in quattro pezzi.
1. access.log: molti pezzi sono falsi. Quello vero l'ha servito una teiera (cerca il codice HTTP giusto).
2. parole.txt: ogni riga ha un gemello, tranne una.
3. dump.bin: qualcuno ha scritto il pezzo usando due byte per ogni lettera.
4. dati.csv: il pezzo ha l'etichetta "segreto", ed è scritto 13 lettere più in là. Il file arriva da Windows.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
