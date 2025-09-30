print("Salutare, eu sunt Ionuț")

print("este marți, 30 septembrie")

# Exercițiu:
# capturați input-ul utilizatorului într-o variabilă `name`
# după care, faceți print string-ului "Salut, {name}".
#
# aveți la îndemână:
# funcția `input()` cu parametrul opțional prompt
# faptul că string-urile sunt concatenabile cu operatorul +
# și funcția `print()`


# aici așteptăm input de la utilizator
name = input("Introduceti numele: ")

# aici salutăm utilizatorul
print("Salut, " + name)

# True / False
condition1 = False
condition2 = False
condition3 = False

if condition1:
    # do something
    print("varianta 1")
elif condition2:
    # do something else
    print("varianta 2")
elif condition3:
    # oricâte elif-uri
    print("varianta 3")
else:
    # când nu a match-uit niciuna din condiții
    print("nu a fost nici-una din variante")
