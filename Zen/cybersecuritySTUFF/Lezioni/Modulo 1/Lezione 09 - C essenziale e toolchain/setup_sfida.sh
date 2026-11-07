#!/usr/bin/env bash
# Prepara la mini-CTF della Lezione 9 in ~/l9_sfida. Non leggere oltre: esegui e basta.
# Crea cassaforte.c, un Makefile e LEGGIMI.txt. Il binario lo compili tu con `make`.
set -e
D="$HOME/l9_sfida"
if [ -e "$D" ]; then echo "$D esiste già: rinominala o eliminala e riprova"; exit 1; fi
command -v gcc >/dev/null || { echo "serve gcc (su Debian/Ubuntu: sudo apt install build-essential gdb)"; exit 1; }
mkdir -p "$D"; cd "$D"
cat > cassaforte.c <<'C'
// cassaforte.c — NON leggere questo file: è il "binario della sfida".
// Compilalo con: make
// La flag L9{...} è in quattro pezzi. Solo il primo si vede con `strings`.
// Gli altri tre richiedono gli strumenti della lezione: objdump, gdb, e un po' di testa.
// Non c'è bisogno di indovinare la password a caso.
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ANNO 2026
#define BASE 0x4c39
static const int chiave = (ANNO * 31) ^ BASE;     // calcolata dal compilatore (pezzo 2 = password)

static unsigned char p2[] = {0x41,0x52,0x50,0x50,0x5c,0x5d,0x47,0x52,0x6c,0x00};  // XOR 0x33
static unsigned char p3[] = {0x2a,0x33,0x2f,0x05,0x3e,0x3f,0x36,0x05,0x00};       // XOR 0x5a
static unsigned char p4[] = {0x1e,0x02,0x1f,0x0a,0x08,0x03,0x19,0x08,0x10,0x00};  // XOR 0x6d

static void decodifica(unsigned char *s, unsigned char k) {
    for (int i = 0; s[i]; i++) s[i] ^= k;
}

// Questa funzione non viene MAI chiamata da main (codice morto).
void regalo(void) {
    decodifica(p4, 0x6d);
    printf("Pezzo 4: %s\n", p4);
}

static int controlla(const char *pw) {
    char atteso[32];
    snprintf(atteso, sizeof atteso, "%d-apriti", chiave);   // la password vera, costruita a runtime
    return strcmp(pw, atteso) == 0;
}

int main(int argc, char *argv[]) {
    printf("Pezzo 1: L9{la_toolchain_\n");        // in chiaro in .rodata: lo trova strings
    decodifica(p3, 0x5a);                         // p3 viene decodificato subito, in memoria
    if (argc > 1 && controlla(argv[1])) {
        decodifica(p2, 0x33);
        puts("Accesso!");
        printf("Pezzo 2: %s\n", p2);              // solo con la password giusta
        printf("Pezzo 3: %s\n", p3);
    } else {
        puts("Password sbagliata. Ma la toolchain vede tutto lo stesso.");
    }
    return 0;
}
C
cat > Makefile <<'M'
CC = gcc
CFLAGS = -g -O0 -no-pie -fno-stack-protector
cassaforte: cassaforte.c
	$(CC) $(CFLAGS) -o $@ $<
.PHONY: pulisci
pulisci:
	rm -f cassaforte
M
cat > LEGGIMI.txt <<'T'
Mini-CTF della Lezione 9 — la cassaforte.

1. Compila:   make        (ottieni il binario ./cassaforte)
2. Eseguilo:  ./cassaforte            e poi   ./cassaforte PAROLA

La flag L9{...} è in quattro pezzi. Recuperali TUTTI senza indovinare la
password a tentativi e senza aprire cassaforte.c:

  Pezzo 1  si vede con uno strumento della Lezione 7 (guarda le stringhe).
  Pezzo 2  è stampato solo con la password giusta. La password è un numero
           seguito da una parola. Scoprila con gdb (fermati nella funzione che
           la controlla e leggi la variabile locale con cui ti confronta, dopo
           lo snprintf; oppure leggi la variabile globale `chiave`). Poi lancia
           ./cassaforte con quella password.
  Pezzo 3  è offuscato e diventa leggibile solo in memoria, a runtime. Con gdb,
           fermati DOPO che è stato decodificato e stampane il contenuto.
  Pezzo 4  lo stampa una funzione che main NON chiama mai (codice morto).
           Trovala con nm/objdump e chiamala tu da gdb (call), o salta a essa.

Strumenti utili: gcc, make, strings, nm, objdump, readelf, gdb.
Le soluzioni sono in Soluzioni.md (aprile solo dopo aver provato).
T
echo "Sfida pronta in $D (leggi LEGGIMI.txt)"
