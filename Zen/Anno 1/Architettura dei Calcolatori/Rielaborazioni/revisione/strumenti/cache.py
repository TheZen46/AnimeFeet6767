"""Simulatore di cache con sostituzione LRU (indirizzi in byte)."""


def campi(ind, byte_blocco, insiemi, bit=32):
    """(tag, indice, offset) di un indirizzo."""
    ob = byte_blocco.bit_length() - 1
    ib = insiemi.bit_length() - 1
    return ind >> (ob + ib), (ind >> ob) & (insiemi - 1), ind & (byte_blocco - 1)


def simula(indirizzi, blocchi, byte_blocco=4, vie=1):
    """Restituisce la lista di 'H' (hit) e 'M' (miss)."""
    insiemi = blocchi // vie
    cache = [[] for _ in range(insiemi)]     # ogni insieme: tag in ordine LRU
    esito = []
    for a in indirizzi:
        tag, ind, _ = campi(a, byte_blocco, insiemi)
        s = cache[ind]
        if tag in s:
            s.remove(tag); s.append(tag); esito.append("H")
        else:
            if len(s) == vie:
                s.pop(0)
            s.append(tag); esito.append("M")
    return esito
