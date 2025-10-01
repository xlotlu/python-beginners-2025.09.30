# slicing

# A. dat fiind string-ul
s = "Bună ziua, exersăm din plin"

# obțineți:
# - slice-ul de la al 7lea la al 12lea caracter inclusiv
s[6:13]

# - ultimele 3 caractere din string
s[-3:]

# - ultimele 3 caractere din string, inversate
#   (de la dreapta la stânga)
s[:-4:-1]

# - de la al 12lea caracter la al 7lea, inclusiv
#   de la dreapta la stânga
s[12:5:-1]

# B. dată fiind lista
cities = [
    'Berlin',
    'Brașov',
    'București',
    'Cluj',
    'Constanța',
    'Copenhaga',
    'Iași',
    'Paris',
    'Satu Mare',
    'Timișoara'
]

# obțineți:
# - al 3lea element
cities[2]

# - slice-ul de lungime 3, începând de la al 3lea element
cities[2:2+3]

# - slice-ul cu ultimele 3 elemente
cities[-3:]

# - slice-ul cu ultimele 3 elemente în ordine inversă
cities[:-4:-1]

# - toată lista reversată, folosind sintaxa de slicing
cities[::-1]
