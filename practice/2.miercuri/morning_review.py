# ok...

#1. repetați stringul "tra la la" de 5 ori
print("tra la la" * 5)

for x in range(5):
    print("tra la la")

#2. obțineți partea întreagă a împărțirii lui 17 la 4
17 // 4


#3. obțineți restul împărțirii lui 17 la 4
17 % 4

#4. date fiind variabilele
name = "Jane"
is_student = True # și apoi False
# scrieți un if / else care să printeze
# "Jane is a student" / "Jane is not a student"

if is_student:
    print("Jane is a student")
else:
    print("Jane is not a student")

#5. dat fiind string-ul
s = "Bună dimineațaa!"

# - obțineți al 7lea caracter din string
s[6]

# - obțineți penultimul caracter din string
idx = len(s) - 2
s[idx]
s[-2]

# - verificați dacă începe cu "Bu"
s.startswith("Bu")

# - verificați dacă se termină cu "aa"
s.endswith("aa")

# - numărați apariția caracterului "a" în `s`
s.count("a")

# - găsiți poziția pe care apare substringul "dimi"
s.find("dimi")

#6. dat fiind string-ul
t1 = "===Column header==="
# extrageți numele coloanei fără caracterele "="
s.strip("=")

#7. dat fiind string-ul
t2 = "Column header"
# generați un string nou cu lungime de 25 de caractere
# pad-uit la stânga și la dreapta cu caracterul "="
t2.center(25, "=")

#8. scrieți o funcție `cube(x)` ce calculează x la puterea a 3a

def cube(x):
    return x ** 3

#9. luați un număr întreg ca input de la utilizator,
# folosiți funcția `cube()` pentru a calcula rezultatul,
# și faceți print cu textul:
# "Cubul numărului <număr> este <cub>."
num = int(input("zi un număr "))
print(cube(int(num)))

# principle of least astonishment

