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


# Exercițiu:
# setăm of variabilă `tod` ("time of day")
# dacă tod == "morning": salutul va fi:
#    "Bună dimineața, {nume}"
# dacă tod == "noon": salutul va fi:
#    "Bună ziua, {nume}"
# dacă tod == "evening": salutul va fi:
#    "Bună seara, {nume}"
# dacă tod == "night": salutul va fi:
#    "Noapte bună, {nume}"

tod = "acum"

if tod == "acum":
    print("nu e acum, e atunci")


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
