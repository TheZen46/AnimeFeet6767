#!/usr/bin/env bash
# Prepara la sfida della Lezione 5 in ~/l5_sfida. Non leggere oltre: esegui e basta.
# Crea file solo dentro ~/l5_sfida e avvia quattro processi innocui (sleep e un piccolo bash)
# che terminano da soli dopo 2 ore.
set -e
D="$HOME/l5_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
mkdir -p "$D"; cd "$D"
d(){ printf '%s' "$1" | base64 -d; }

# 1. il custode porta il pezzo nel nome
nohup bash -c "exec -a 'custode[$(d 'TDV7aV9wcm9jZXNzaV8=')]' sleep 7200" >/dev/null 2>&1 &

# 2. il messaggero porta il pezzo nell'ambiente
nohup env PEZZO="$(d 'cGFybGFub18=')" bash -c 'exec -a messaggero sleep 7200' >/dev/null 2>&1 &

# 3. la sentinella parla solo se riceve il segnale giusto
cat > "$D/.sentinella" <<'X'
R="$(dirname "$0")/risposta.txt"
trap 'printf "%s\n" "$(printf "fF2cflGaj9VY" | rev | base64 -d 2>/dev/null)" > "$R"' USR1
trap 'echo "Non è il segnale giusto." > "$R"' USR2 HUP
while (( SECONDS < 7200 )); do sleep 1; done
X
nohup bash -c "exec -a sentinella bash '$D/.sentinella'" >/dev/null 2>&1 &

# 4. l'ostinato vive in un nascondiglio e ignora SIGTERM
N="$D/.$(head -c 6 /dev/urandom | od -A n -t x1 | tr -d ' \n')"
mkdir -p "$N"; d 'YXNjb2x0YXJlfQ==' > "$N/pezzo4.txt"
( cd "$N" && nohup bash -c "trap '' TERM; exec -a ostinato sleep 7200" >/dev/null 2>&1 & )
sleep 0.5

cat > LEGGIMI.txt <<'X'
La flag è divisa in quattro pezzi, e quattro processi la custodiscono.
1. Il custode porta il suo pezzo scritto addosso: basta guardarlo.
2. Il messaggero lo porta con sé, nel suo ambiente.
3. La sentinella parla solo se riceve il segnale giusto, e scrive la risposta in risposta.txt.
   (Non è SIGTERM, e non è SIGKILL: quelli la zittiscono per sempre.)
4. L'ostinato non dice niente, ma vive dove è nascosto il pezzo. E non muore facilmente.
Alla fine, termina tu tutti e quattro i processi.
X
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
