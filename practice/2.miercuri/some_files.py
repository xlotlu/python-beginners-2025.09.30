"""
fp = open("path/către/fișier")
# avem fp
fp.close()

with open("path/către/fișier") as fp:
    # avem fp
    pass
"""

# creați un fișier într-un editor text,
# citiți-i conținutul în python, și
# faceți print
#
# folosiți forma with ...

with open("demo.txt") as f:
    content = f.read()
    print(content)

# faceți replace la toate caracterele
# "a" cu "!"
# scrieți stringul rezultat în alt fișier

with open("demo.txt") as f:
    content = f.read()

    with open("output.txt", 'w') as f2:
        f2.write(content.replace("a", "!"))


# blocul with introduce un "context manager"
# (adică cineva care face un lucru specific
# la instanțiere, și un alt lucru specific
# la ieșirea din bloc)
#
# (open rulează fp.close() la ieșire)

# de asemenea poate să introducă context managere
# multiple

with open("demo.txt") as f, \
     open("output.txt", 'w') as f2:
    f2.write(f.read().replace("a", "@@@"))

# scrieți o funcție `sed(infile, outfile, txt, replacement)`
# care citește contentul din `infile`, și schimbă
# orice apariție a lui `txt` cu `replacement`
# și scrie rezultatul în `outfile`

def sed(infile, outfile, txt, replacement):
    with open(infile) as f, \
         open(outfile, 'w') as f2:
        f2.write(f.read().replace(txt, replacement))

sed("demo.txt", "output.txt", "a", "bla")

# scrieți funcția `grep(pattern, filename)`
# care face output tuturor liniilor din fișier
# care conțin `pattern`
#
# hint: un file pointer este iteraaaabil

def grep(pattern, filename):
    with open(filename) as f:
        for line in f:
            if pattern in line:
                print(line)

# modificați funcția grep să returneze o listă
# cu liniile care conțin `pattern`
def grep(pattern, filename):
    matches = []
    with open(filename) as f:
        for line in f:
            if pattern in line:
                matches.append(line)

    return matches

# temă pentru acasă:
# faceți funcția grep să primească parametrul opțional highlight
#def grep(pattern, filename, highlight=False):
#    pass
#
# dacă highlight == True, să continue să facă print
# fiecărei linii, dar colorizând apariția lui `pattern`
# în linie.
#
# sugestie: pentru pasul 1 (rezolvarea algoritmului)
# nu vă chinuiți cu escape characters de colorizare
# ci folosiți un caracter simplu pt. highlight.
# (spre exemplu: "!")

# temă pentru acasă 2:
# scrieți o funcție care primind un txt,
# returnează un dicționar de forma {'word': count, etc...}
#
# funcția numără apariția fiecărui cuvânt în `txt`.

s = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."

def count_words(txt):
    out = {}

    # aflăm cumva care sunt cuvintele unice
    # le punem în dicționar
    # și incrementăm count-ul după cum este nevoie

    return out

print(count_words(txt))