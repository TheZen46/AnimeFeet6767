#  main(int argc, char *argv[]) {
#     char *str = "abcd";
#     int i;
#     for (i = 0;str[i] != '\0';i++)
#         ;
#     printf(stdio, "%s\n", str);
#     }

.text
.globl main

main:
    addi s0, zero, testo # s0 = const char *str
    li     t0, 0         # i = 0
loop:                    # Start of for loop
    add    t1, t0, s0    # Add the byte offset for str[i]
    lb     t1, 0(t1)     # Dereference str[i]
    beqz   t1, end       # if str[i] == 0, break for loop
    addi   t0, t0, 1     # Add 1 to our iterator
    j      loop          # Jump back to condition (1 backwards)
end: # End of for loop

    # load syscall number
    addi  a7, zero, 64  
    # load file descriptor  
    addi  a0, zero, 1  
    # load buffer    
    add  a1, zero, s0
    # load count
    add  a2, zero, t0 
    # stampa del contenuto del buffer su
    # terminale      
    ecall                  

    li a7, 93			// mettere in a0 il numero 10
    ecall
    
.data
testo: .asciz "abcd"