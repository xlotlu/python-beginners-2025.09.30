#### dicționare ####

# o structură de date care asociază
# o valoare unei chei

person = {
    'name': 'Jane',
    'age': 20,
    'city': 'București',
}

for key, value in person.items():
    print(key, value)

# accesul se face cu sintaxa d[cheie]
# cu care se face și assignment:
# d[cheie] = new_value

# creați un dicționar numit person
# care să conțină următoarele
# perechi cheie-valoare:

# 'name': 'Andrew'
# 'age': 32
# 'occupation': 'sysadmin'
# 'hobbies': ["biking", "guitar"]

# apoi:
# - printați valoarea pentru cheia "age"

# - schimbați-i vârsta la 33

# - adăugați o cheie nouă, "friends",
#   cu valoarea ["Jane", "John", "Jim"]

# - adăugați "knitting" la lista de hobby-uri



# opțional:
# modificați funcția `process_report()`
# astfel încât să returneze o listă
# de dicționare de forma
# {"Name": ..., "Age": ..., "City": ...}