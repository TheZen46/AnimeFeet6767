"""Verifica di Fondamenti di Informatica.

Parte 1: conti di matematica discreta dei moduli 1 e 2.
Parte 2: tutti i programmi C++ dei moduli 3-7. Un blocco ```cpp che comincia
con "// file: nome.cpp" apre un programma, "// segue: nome.cpp" lo continua.
Ogni programma viene compilato (g++ -std=c++17 -Wall -Wextra, con AddressSanitizer
e UBSan per trovare perdite di memoria e accessi fuori dai limiti) ed eseguito con
gli ingressi di PROVE, confrontando l'uscita.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from discreta import controlla as controlla_discreta
from prove import PROVE, FILE_DATI, SOLO_COMPILAZIONE

MOD = Path(__file__).resolve().parent.parent / "moduli"


def programmi():
    progs, ordine = {}, []
    for md in sorted(MOD.glob("0[3-9]-*.md")):
        for blocco in re.findall(r"```cpp\n(.*?)```", md.read_text(), re.S):
            m = re.match(r"// (file|segue): (\S+)", blocco)
            assert m, (md.name, "blocco cpp senza intestazione", blocco[:60])
            nome = m.group(2)
            if m.group(1) == "file":
                assert nome not in progs, ("doppio", nome)
                progs[nome] = blocco
                ordine.append((md.name, nome))
            else:
                progs[nome] += "\n" + blocco
            for riga in blocco.splitlines():
                assert len(riga) <= 80, (nome, riga)
    return progs, ordine


def main():
    n = controlla_discreta()
    progs, ordine = programmi()
    eseguiti = 0
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        for nome, testo in FILE_DATI.items():
            (d / nome).write_text(testo)
        for modulo, nome in ordine:
            src = d / nome
            src.write_text(progs[nome])
            exe = d / (nome + ".out")
            r = subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", "-g",
                                "-fsanitize=address,undefined", "-o",
                                str(exe), str(src)], capture_output=True, text=True)
            assert r.returncode == 0 and not r.stderr.strip(), (nome, r.stderr)
            if nome in SOLO_COMPILAZIONE:
                n += 1
                continue
            assert nome in PROVE, ("manca la prova per", nome)
            for ingresso, atteso in PROVE[nome]:
                r = subprocess.run([str(exe)], input=ingresso, capture_output=True,
                                   text=True, cwd=d, timeout=10)
                assert r.returncode == 0 and not r.stderr, (nome, r.stderr[:500])
                if r.stdout != atteso:
                    print("ERRORE", modulo, nome, repr(ingresso))
                    print("atteso:", repr(atteso))
                    print("avuto: ", repr(r.stdout))
                    sys.exit(1)
                n += 1
            eseguiti += 1
    print("verifica Fondamenti: %d controlli superati, %d programmi eseguiti"
          % (n, eseguiti))


if __name__ == "__main__":
    main()
