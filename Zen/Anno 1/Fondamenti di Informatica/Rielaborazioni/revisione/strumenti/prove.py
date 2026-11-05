"""Ingressi e uscite attese dei programmi dei moduli 3-7."""

FILE_DATI = {
    "voti.txt": "Anna 27\nBruno 15\nCarla 30\nDario 17\nElena 18\n",
    "misure.txt": "T1 20 22 21\nT2 25 24 29\nP1 10 11 15\n",
    "temperature.txt": "12.5\n14\n9.5\n16\n13\n",
    "presenze.txt": "104 5\n1 1 0 1 1 0\n1 1 1 1 1 0\n0 1 0 0 1 0\n1 1 1 1 0 0\n",
}
SOLO_COMPILAZIONE = {"prototipi.cpp"}

PROVE = {
    # ---- modulo 3
    "somma.cpp": [("3 4\n", "Inserisci due interi: La somma e' 7\n")],
    "giudizio.cpp": [("17\n", "insufficiente\n"), ("18\n", "sufficiente\n"), ("27\n", "buono\n"),
                     ("30\n", "ottimo\n"), ("31\n", "voto non valido\n")],
    "calcolatrice.cpp": [("6 * 7\n", "42\n"), ("6 x 7\n", "42\n"), ("1 / 0\n", "divisione per zero\n"),
                         ("7 / 2\n", "3.5\n"), ("1 ^ 2\n", "operatore sconosciuto\n")],
    "media.cpp": [("4 -3 8 6 -1\n", "media 6\n"), ("-1\n", "nessun valore\n")],
    "validazione.cpp": [("0 11 7\n", "Numero fra 1 e 10: " * 3 + "".join(
        "7 x %d = %d\n" % (i, 7 * i) for i in range(1, 11)))],
    "espressioni.cpp": [("", "3 1\n3 3.5\n10 8 3\n1 1\n2 1\n")],
    "intervalli.cpp": [("", "11 40 50 146\n")],
    "cifre.cpp": [("4096\n", "19\n")],
    "mcd.cpp": [("84 36\n", "12\n"), ("17 5\n", "1\n")],
    "primo.cpp": [("97\n", "97 e' primo\n"), ("91\n", "91 non e' primo\n"), ("2\n", "2 e' primo\n")],
    "binario.cpp": [("45\n", "00101101\n"), ("255\n", "11111111\n")],
    "triangolo.cpp": [("3\n", "  *\n ***\n*****\n")],
    "traccia.cpp": [("5\n", "5 35\n1\n")],
    "conta.cpp": [("-4 -9 -2 0\n", "0 positivi, 3 negativi\nmassimo -2\n"),
                  ("3 8 -1 8 0\n", "3 positivi, 1 negativi\nmassimo 8\n"),
                  ("0\n", "0 positivi, 0 negativi\n")],
    "serie.cpp": [("1000\n", "1.64393 0.0009995\n")],
    # ---- modulo 4
    "potenza.cpp": [("", "1024 0.125\n")],
    "riferimenti.cpp": [("", "8 3 3 2\n")],
    "overloading.cpp": [("", "9 2.5 11\n")],
    "array.cpp": [("0 6 5 7 -2 9 7 1\n", "massimo in posizione 3\nil 7 e' in posizione 1\n"
                   "-2 1 5 7 7 9 \ndopo l'ordinamento il 7 e' in posizione 4\n")],
    "matrici.cpp": [("", "10 26 42 \n1 5 9 \n2 6 10 \n3 7 11 \n4 8 12 \n")],
    "stringhe.cpp": [("una frase di prova\nOsso\n", "18 7 1\nuna frase di prova-Osso dopo\n")],
    "voti.cpp": [("", "5 voti, media 21.4\nAnna Carla Elena \n")],
    "studenti.cpp": [("", "Bruno (12/1/2007) 28\nAnna (3/5/2006) 26.5\nCarla (30/9/2006) 24.25\nCarlotta\n")],
    "esadecimale.cpp": [("B6\n", "182\n"), ("1G\nff\nFF\n", "stringa non valida, riprova\n" * 2 + "255\n")],
    "misure.cpp": [("", "T1 21\nT2 26\nP1 12\nmigliore: T2\n")],
    "diagonali.cpp": [("", "55 35 1\n0\n")],
    "parole.cpp": [("  il compilatore   segnala un errore \n", "5 compilatore\n")],
    "passaggi.cpp": [("", "14 12 27\n")],
    "fusione.cpp": [("", "1 2 3 4 9 10 12 \n")],
    "temperature.cpp": [("", "5 13 2\n")],
    # ---- modulo 5
    "puntatori.cpp": [("", "7 17 1\nr e' nullo\n")],
    "aritmetica.cpp": [("", "15 16 23 5\n108 23\n9\n")],
    "dinamico.cpp": [("3\n", "10 11 12 99 \n")],
    "matrice_dinamica.cpp": [("3 4\n", "11 4\n")],
    "ricorsione.cpp": [("", "3628800 12 14 1\n101101\n31\n")],
    "template.cpp": [("", "21 9.75 t empt\n")],
    "traccia_puntatori.cpp": [("", "14 7 21\n")],
    "filtra.cpp": [("", "4: 12 30 19 25\n")],
    "ricorsione_array.cpp": [("", "19 5 -1\n")],
    "fibonacci.cpp": [("", "6765 6765 21891\n")],
    "traccia_ricorsione.cpp": [("", "\n2:2 3:3 2:2 4:5 5\n")],
    "conta_template.cpp": [("", "3 2\n")],
    "tartaglia.cpp": [("7\n", "1 6 15 20 15 6 1 \n")],
    # ---- modulo 6
    "data.cpp": [("", "29/2/2028\n1/3/2028\n1/1/2000\n1 1/1/2027\n")],
    "frazione.cpp": [("", "1/6 3/4 -1/2\n11/12 1/8 1 9/4\n3/4\n")],
    "vettore.cpp": [("", "1 2 3 \n100 2 3 \n11 22 33 \n1 3 \n")],
    "presenze.cpp": [("", "corso 104, piu' assiduo: 1\n1 sotto il 70%, presenti alla lezione 2: 2, "
                          "getP(9, 0) = -1\n4\n")],
    "contatore.cpp": [("", "3 2 4 1\n")],
    # ---- modulo 7
    "lista.cpp": [("", "3 8 6 5 \n3 6 \n3 8 6 5 \n2 2 4 7 9 \n5 1\n")],
    "pila.cpp": [("", "1 0 0\n14 7\n0 3 2\n")],
    "coda.cpp": [("", "0 1* 2 0* 2 2* \n5a 3c\n")],
    "pila_lista.cpp": [("", "9 25 25 16 9 4 1 \n")],
    "lista_rovescia.cpp": [("", "50 40 30 20 10 \n10 20 30 40 50 \n150\n")],
    "coda_circolare.cpp": [("", "11110\n2: 3 4 6 7\n")],
}
