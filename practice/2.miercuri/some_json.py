# dată fiind lista

lst = [
    {'Name': 'Jane', 'Age': '20', 'City': 'Berlin'},
    {'Name': 'Mike', 'Age': '17', 'City': 'Brașov'},
    {'Name': 'Anna', 'Age': '25', 'City': 'București'},
    {'Name': 'Sam', 'Age': '40', 'City': 'Cluj'},
    {'Name': 'Dan', 'Age': '34', 'City': 'Constanța'},
    {'Name': 'Andrew', 'Age': '42', 'City': 'Sfântu Gheorgh'},
]

# 1. transformați-o într-un string json
import json
print(json.dumps(lst, indent=2))

# 2. creeați un dicționar "ages", în care
#    cheile sunt numele persoanelor, și valorile
#    vârsta lor respectivă

ages = {}
for d in lst:
    name = d['Name']
    age = d['Age']

    ages[name] = age

print(ages)

# 3. transformați dicționarul într-un string json

print(json.dumps(ages))


# 4. dată fiind lista `lst` de mai sus
# și dat fiind dicționarul
hobbies = {
    "Jane": ["skying", "diving"],
    "Sam": ["guitar", "cooking"],
    "Andrew": ["books"],
}

# modificați fiecare element din lst,
# astfel încât să primească cheia "hobbies"
# cu valoarea din dicționarul de mai sus

# strategie:
# cum găsim omul după nume în lst?
#
# idee: o funcție custom după care să facem search?
#       lista nu suportă așa ceva
#
# idee: iterăm prin listă, obținem numele omului
#       și apoi verificăm dacă există cheia în hobbies

for person in lst:
    name = person['Name']

    if name in hobbies:
        person['hobbies'] = hobbies[name]

print(lst)

# problem: acum nu toate persoanele au cheia hobbies.
# cum facem să aibă toți hobbies, chiar dacă în sursa de
# date nu aveau?

for person in lst:
    name = person['Name']

    if name in hobbies:
        person['hobbies'] = hobbies[name]
    else:
        person['hobbies'] = []

print(lst)


# pentru situația combinată când
# 1) vrem să verificăm dacă există cheia,
#    și dacă da să îi luăm valoarea și
# 2) dacă nu, să îi punem o valoare default
for person in lst:
    name = person['Name']

    hlist = hobbies.get(name, [])

    person['hobbies'] = hlist
