"""Conti dei moduli 1 e 2 (insiemi, relazioni, funzioni, strutture, combinatoria)."""
from itertools import combinations, product
from math import comb, perm, factorial


def parti(A):
    return [frozenset(c) for r in range(len(A) + 1) for c in combinations(A, r)]


def proprieta(A, R):
    rif = all((a, a) in R for a in A)
    sim = all((b, a) in R for a, b in R)
    ant = all(a == b or (b, a) not in R for a, b in R)
    tra = all((a, d) in R for a, b in R for c, d in R if b == c)
    return rif, sim, ant, tra


def controlla():
    ok = 0
    # ---- modulo 1
    A = ["2", "x", "#"]
    P = parti(A)
    assert len(P) == 8
    X = [frozenset({"2"}), frozenset({"x"})]
    magg = [S for S in P if all(x <= S for x in X)]
    assert set(magg) == {frozenset({"2", "x"}), frozenset(A)}
    assert min(magg, key=len) == frozenset({"2", "x"})
    assert [S for S in P if len(S) == 2] == [frozenset({"2", "x"}), frozenset({"2", "#"}),
                                             frozenset({"x", "#"})]
    assert not frozenset({"2", "x"}) <= frozenset({"x", "#"})
    R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 1), (3, 4), (4, 3)}
    assert proprieta([1, 2, 3, 4], R) == (True, True, False, True)
    Z = range(-6, 7)
    assert proprieta(Z, {(a, b) for a in Z for b in Z if (a - b) % 2 == 0}) == (True, True, False, True)
    assert proprieta(Z, {(a, b) for a in Z for b in Z if a < b}) == (False, False, True, True)
    assert proprieta(Z, {(a, b) for a in Z for b in Z if abs(a - b) <= 1}) == (True, True, False, False)
    D = [1, 2, 3, 4, 6, 12]
    def mm(X):
        return ([d for d in D if all(d % x == 0 for x in X)], [d for d in D if all(x % d == 0 for x in X)])
    assert mm([2, 3]) == ([6, 12], [1]) and mm([2, 4]) == ([4, 12], [1, 2]) and mm([4, 6]) == ([12], [1, 2])
    funz = list(product(range(2), repeat=3))
    assert 2 ** 6 == 64 and len(funz) == 8 and sum(set(f) == {0, 1} for f in funz) == 6
    assert len(list(product(range(3), repeat=2))) == 9 and perm(3, 2) == 6
    assert 25 + 18 - 10 == 33 and 40 - 33 == 7
    abc = ["a", "b", "c", "d"]
    Rg = {(x, x) for x in abc} | {("a", "b"), ("a", "c"), ("a", "d"), ("b", "d"), ("c", "d")}
    assert proprieta(abc, Rg) == (True, False, True, True)
    cl = {r: [x for x in range(12) if x % 4 == r] for r in range(4)}
    assert cl[1] == [1, 5, 9] and sum(map(len, cl.values())) == 12
    f = {n: n % 3 for n in range(1, 7)}
    assert {f[n] for n in (1, 4, 6)} == {0, 1} and [n for n in f if f[n] == 0] == [3, 6]
    assert [n for n in f if f[n] in (1, 2)] == [1, 2, 4, 5]
    assert all(abs(2 * x + 1) == abs(2 * x + 1) for x in range(3)) and abs(2 * 0 + 1) == abs(2 * -1 + 1)
    # esercizi più impegnativi
    coppie = [(a, b) for a in range(-4, 5) for b in range(-4, 5) if b != 0]
    eqv = {(p, q) for p in coppie for q in coppie if p[0] * q[1] == p[1] * q[0]}
    assert proprieta(coppie, eqv)[:2] == (True, True) and proprieta(coppie, eqv)[3]
    def partizioni(s):
        if not s:
            yield []
            return
        primo, resto = s[0], s[1:]
        for p in partizioni(resto):
            for i in range(len(p)):
                yield p[:i] + [[primo] + p[i]] + p[i + 1:]
            yield [[primo]] + p
    assert sum(1 for _ in partizioni([1, 2, 3, 4])) == 15
    ok += 14 + 2
    # ---- modulo 2
    Zr = range(-20, 21)
    st = lambda a, b: a + b + 1  # noqa: E731
    assert all(st(st(a, b), c) == st(a, st(b, c)) for a in Zr for b in Zr for c in (-3, 0, 5))
    assert all(st(a, -1) == a and st(a, -a - 2) == -1 for a in Zr)
    med = lambda a, b: (a + b) / 2  # noqa: E731
    assert med(med(0, 0), 4) == 2 and med(0, med(0, 4)) == 1
    tab = {("e", x): x for x in "eab"} | {(x, "e"): x for x in "eab"}
    tab |= {("a", "a"): "b", ("a", "b"): "e", ("b", "a"): "e", ("b", "b"): "a"}
    assert all(tab[tab[x, y], z] == tab[x, tab[y, z]] for x in "eab" for y in "eab" for z in "eab")
    assert {a: b for a in range(1, 7) for b in range(1, 7) if a * b % 7 == 1} == {1: 1, 2: 4, 3: 5, 4: 2, 5: 3, 6: 6}
    assert [a for a in range(6) if any(a * b % 6 == 1 for b in range(6))] == [1, 5]
    assert [a for a in range(1, 5) if any(a * b % 5 == 1 for b in range(1, 5))] == [1, 2, 3, 4]
    assert (2 * 4) % 8 == 0 and [5 * k % 6 for k in range(6)] == [0, 5, 4, 3, 2, 1]
    assert (comb(12, 3), perm(12, 3), comb(14, 3), 12 ** 3) == (220, 1320, 364, 1728)
    assert comb(12, 2) + perm(12, 2) == 198
    assert len({tuple(sorted(c)) for c in product(range(12), repeat=3)}) == 364
    assert (36 ** 8, 26 ** 8, 36 ** 8 - 26 ** 8) == (2821109907456, 208827064576, 2612282842880)
    assert factorial(11) // (2 * 2) == 9979200 and sorted("INFORMATICA").count("I") == 2
    assert comb(6, 2) * comb(8, 3) == 840 and comb(14, 5) - comb(8, 5) == 1946
    assert comb(8, 3) == 56 and comb(5, 3) * 2 ** 2 == 40
    assert sum(1 for n in range(1, 101) if n % 2 == 0 or n % 3 == 0 or n % 5 == 0) == 74
    assert (comb(9, 5), perm(9, 5), 9 * comb(8, 4)) == (126, 15120, 630) and 630 == 5 * 126
    assert comb(40, 4) == 91390 and 4 * comb(10, 4) == 840
    assert all(comb(n, k) == comb(n - 1, k - 1) + comb(n - 1, k) for n in range(1, 15) for k in range(1, n))
    assert sum(1 for f in product(range(3), repeat=5) if set(f) == {0, 1, 2}) == 150 == 3**5 - 3 * 2**5 + 3
    assert [x for x in range(7) if 3 * x % 7 == 4] == [6] and [x for x in range(12) if 5 * x % 12 == 7] == [11]
    assert [x for x in range(12) if 4 * x % 12 == 6] == []
    assert factorial(10) // 2 == 1814400 and 2 * (factorial(10) // 2) + factorial(10) // 4 == 4536000
    ok += 17 + 4
    return ok
