#!/usr/bin/env bash
# Prepara la sfida della Lezione 1 in ~/l1_sfida. Non leggere oltre: esegui e basta.
set -e
D="$HOME/l1_sfida"; mkdir -p "$D/.strumenti"
d(){ printf '%s' "$1" | base64 -d; }
d 'TDF7bGFfc2hlbGxf' > "$D/-parte1"
d 'bm9uX21lbnRlXw==' > "$D/parte 2 di 3"
cat > "$D/.strumenti/rivela" <<'X'
#!/usr/bin/env bash
if [ "$CHIAVE" = "apriti" ]; then printf '%s\n' "$(printf 'bWFpfQ==' | base64 -d)"; exit 0
else echo "la CHIAVE non e' nel mio ambiente" >&2; exit 3; fi
X
chmod +x "$D/.strumenti/rivela"
echo "La chiave si chiama CHIAVE e vale: apriti" > "$D/.suggerimento"
echo "Sfida pronta in $D"
