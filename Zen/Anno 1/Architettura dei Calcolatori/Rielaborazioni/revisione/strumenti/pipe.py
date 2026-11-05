"""Conteggio dei cicli di una pipeline RISC-V a 5 stadi (IF ID EX MEM WB).

Ogni istruzione è (tipo, rd, sorgenti), tipo in alu, load, store, branch.
Il register file scrive nella prima metà del ciclo e legge nella seconda.
Con il forwarding i dati arrivano all'ingresso dell'ALU; i salti si decidono
in ID (oppure in MEM con decisione="mem") con previsione "non preso".
"""


def cicli(prog, forwarding=True, decisione="id", presi=()):
    """Restituisce (cicli totali, stalli per istruzione, ciclo ID di ognuna)."""
    d = []            # ciclo in cui l'istruzione è in ID e legge i registri
    stalli = []
    ultimo = {}       # registro -> indice dell'ultima istruzione che lo scrive
    for i, (tipo, rd, src) in enumerate(prog):
        minimo = 2 if i == 0 else d[-1] + 1
        if i and (i - 1) in presi:          # salto preso: si scarta il fetch
            minimo += 1 if decisione == "id" else 3
        base = minimo
        for r in src:
            if r == 0 or r not in ultimo:
                continue
            p = ultimo[r]
            tp = prog[p][0]
            if not forwarding:
                minimo = max(minimo, d[p] + 3)
            elif tipo == "branch" and decisione == "id":
                minimo = max(minimo, d[p] + (3 if tp == "load" else 2))
            else:
                minimo = max(minimo, d[p] + (2 if tp == "load" else 1))
        d.append(minimo)
        stalli.append(minimo - base)
        if rd:
            ultimo[rd] = i
    return d[-1] + 3, stalli, d


def predittore(esiti, bit=2, stato=None):
    """Previsioni corrette di un predittore a 1 o 2 bit (contatore saturato)."""
    if bit == 1:
        s = 1 if stato is None else stato
        giuste = 0
        for e in esiti:
            giuste += (s == 1) == e
            s = 1 if e else 0
        return giuste, s
    s = 3 if stato is None else stato     # 3, 2: prevede preso; 1, 0: non preso
    giuste = 0
    for e in esiti:
        giuste += (s >= 2) == e
        s = min(3, s + 1) if e else max(0, s - 1)
    return giuste, s
