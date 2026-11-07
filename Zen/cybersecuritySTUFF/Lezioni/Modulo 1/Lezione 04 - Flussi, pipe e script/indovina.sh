#!/usr/bin/env bash
segreto=$(( RANDOM % 1000000 + 1 )); tentativi=0
echo "Ho pensato un numero tra 1 e 1000000. Hai 25 tentativi."
while (( tentativi < 25 )); do
    IFS= read -r n || exit 1
    tentativi=$((tentativi + 1))
    if ! [[ $n =~ ^[0-9]+$ ]]; then echo "non è un numero"; continue; fi
    if (( n < segreto )); then echo "più alto"
    elif (( n > segreto )); then echo "più basso"
    else echo "giusto in $tentativi tentativi"; exit 0; fi
done
echo "tentativi finiti: era $segreto"; exit 1
