# practice
# [*] având un cap de tabel primit în format text de forma
s = "|###Name###|#Age#|######City######|"
# vrem să obținem o listă cu numele coloanelor


# pattern de acumulare
# 0. avem obiectul sursă
cities = []
# 1. ne definim obiectul nou
lst = []
# 2. iterăm prin obiectul sursă
for city in cities:
    # 3. facem transformarea dorită
    transformed = "#" + city
    # 4. adăugăm la listă
    lst.append()


# [*] rezolvare

def parse_header(s):
    # ne declarăm obiectul cu rezultatele
    columns = []
    # observăm că "|" este separator de coloane
    # facem split după el, ceea ce rezultă 
    # în 2 elemente în plus la început și la sfârșit.
    # lucrăm pe slice-ul care _nu_ conține
    # indexul 0 și indexul final
    for col in s.split("|")[1:-1]:
        # observăm că coloanele sunt pad-uite
        # cu "#". alegerea corectă este str.strip()
        columns.append(col.strip("#"))

    return columns

# exercițiul 2
# dat fiind un string de forma
report = """
-----------------------------------
|###Name###|#Age#|######City######|
-----------------------------------
| Jane     |  20 | Berlin         |
| Mike     |  17 | Brașov         |
| Anna     |  25 | București      |
| Sam      |  40 | Cluj           |
| Dan      |  34 | Constanța      |
| Andrew   |  42 | Sfântu Gheorgh |
-----------------------------------
"""

# generați o listă nouă formată din tuple de forma
# (name, age, city)

# a) scriem o funcție care să proceseze un row de text

r = "| Jane     |  20 | Berlin         |"

# OCD = obsessive compulsive disorder

SEPARATOR = "|"

def parse_row(s, sep=SEPARATOR):
    lst = []
    for i in s.split(sep)[1:-1]:
        lst.append(i.strip(" "))
    return lst

# b) scriem o funcție care să ia tot inputul
#    și să separe headerul de row-uri.
#
#    aceasta va chema la rândul său pe
#    `parse_header()` o dată
#    și parse_row() repetat
#    
#    și
#    1) face print la header
#    2) returnează o listă de liste
#       (sau tuple, după cum a returnat `parse_row()`)

def process_report(report) :
    # sanitizăm datele de input
    report = report.strip()
    # am făcut asta făcând overwrite la variabila
    # deja declarată (anume argumentul primit de funcție)

    # întrebare: ce este aia o linie?
    # răspuns:   o înșiruire de caractere "pe axa x"
    #
    # Î: axa y este definită de cine?
    # R: de "separatorul" newline

    lines = report.split("\n")

    header = parse_header(lines[1])
    print (header)

    rows = lines[3:-1]
    for r in rows:
        print(parse_row(r))

process_report(report)

