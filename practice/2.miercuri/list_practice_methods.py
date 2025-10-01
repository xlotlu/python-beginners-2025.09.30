# dată fiind lista
lst = [
    'Constanța', 'București', 'Iași',
    'Brașov', 'Timișoara', 'Cluj', 'Satu Mare',
    'Constanța', 'București', 'Iași',
]

# all sequences have the `.count()` method
# all sequences are iterable:
#     for elem in seq: print(elem)
# all sequences are addressable by index:
#     seq[15]
# all sequences have a length

#1. obțineți-i lungimea
print(len(lst))

#2. adăugați la listă "Galați"
lst.append("Galați")

#3. extindeți lista cu ["Arad", "Constanța", "Sibiu", "Iași"]
lst.extend(["Arad", "Constanța", "Sibiu", "Iași"])

#4. numărați de câte ori apare "Iași" în listă
count = 0
for elem in lst:
    if elem == "Iași":
        count += 1
print(count)

print(lst.count("Iași"))

#5. ștergeți primul element salvându-i valoarea într-o variabilă
var = lst.pop(0)

#6. ștergeți al 2lea element fără a îi salva valoarea
del lst[1]

#7. inserați la începutul listei "Brăila"
lst.insert("Brăila")

#8. inserați la începutul listei toate elementele din
#   ("Copenhaga", "Berlin", "Paris")
tup = ("Copenhaga", "Berlin", "Paris")

# this reverses elements:
for elem in tup:
    lst.insert(0, elem)

# this doesn't:
for elem in reversed(tup):
    lst.insert(0, elem)

# this works
lst = list(tup) + lst

#9. sortați lista in-place, în ordine inversă
lst.sort(reverse=True)

#10. (facem împreună) găsim și ștergem toate duplicatele
# v1: cod elegant, multe cicluri de procesor
for elem in lst:
    while lst.count(elem) > 1:
        lst.remove(elem)

# v2: folosim o listă intermediară
#     unde adăugăm elementele unice
newlst = []

for elem in lst:
    if elem not in newlst:
        newlst.append(elem)
# folosim temporar mai multă memorie,
# cu mai puține cicluri de procesor
lst = newlst

# v3: algoritmic, eficient

# necesită sortare prealabilă!
lst.sort()
# ținem minte elementul precedent
old_elem = None
# iterăm în ordine inversă, deoarece
# vom șterge din listă în timp ce iterăm pe ea.
#
# de asemenea, iterăm după index, nu după element
# (pentru a putea șterge după index (eficient))
for idx in range(len(lst) - 1, -1, -1):
    elem = lst[idx]
    if elem == old_elem:
        # avem de șters indexul curent
        #print("dup:", idx, elem)
        del lst[idx]
    
    old_elem = elem

# v4: (o luăm înainte)
lst = set(lst)
