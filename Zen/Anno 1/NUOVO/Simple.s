// somma di due numeri interi

.globl main			// chiamata procedura main
.text				// sezione text

main:
la t0, valore	// load valore in t0
lw t1, 0(t0)			// load word 0(valore) in t1
lw t2, 4(t0)			// load word 4(valore) in t2
add t3, t1, t2		// somma due numeri in t3
sw t3, 8(t0)			// store word t3 in 8(t0)
li a7, 93			// mettere in a0 il numero 10
ecall 				// chiamata a sistema

.data					// sezione dati
valore: .word 10, 20, 0	// inizializzazione valore
