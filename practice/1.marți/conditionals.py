
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

if tod != "acum":
    print("nu e acum, e atunci")


name = "John")
#tod = input("Introduceti momentul zilei morning/noon/evening/night: ")
tod = "morning"


if tod == "morning":
    print("Buna dimineata, " + name + "!")
elif tod == "noon":
    print("Buna ziua, " + name + "!")
elif tod == "evening":
    print("Buna seara, " + name + "!")
elif tod == "night":
    print("Noapte buna, " + name + "!")
else:
    print("Salut, " + name + " Mai baga o fisa!")

# Exercițiu:
# repetați exercițiul de mai sus,
# scriind o funcție `greet_by_time()`
# ce returnează salutul potrivit pentru ora curentă.
#
# folosiți funcția datetime.now() pentru a obține
# ora curentă (atributul `hour` de pe obiectul rezultat).
# 
# dacă ora < 10: bună dimineața
# dacă ora >= 10 și < 17: bună ziua
# dacă ora >= 17 și < 22: bună seara
# dacă ora >= 23: noapte bună




from datetime import datetime

def greet_by_time():
    now = datetime.now()
    if now.hour < 10:
        return "bună dimineața"
    elif now.hour < 17:
        return "bună ziua"
    elif now.hour < 22:
        return "bună seara"
    else:
        return "noapte bună"

print(greet_by_time(), input("numele tău? "))