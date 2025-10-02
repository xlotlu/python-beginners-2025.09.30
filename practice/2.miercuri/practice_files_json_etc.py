# exercițiu
#
# 1. încărcați datele din "ages.json" în python,
# folosind funcția `json.load()`.
#
# inspectați datatype-ul rezultat folosind
# funcția `type()`, și faceți print obiectului.
import json

# !!! funcția json.load() deschide direct filepointer-ul !!!

with open("data/ages.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))

# 2. încărcați adițional datele din
# "ages_update.json"
#
# faceți "merge" între cele două dicționare
# astfel încât să aveți un dataset unificat:
#  -- datele din "ages_update.json" vor suprascrie
#  acolo unde este cazul, datele din "ages.json"
#  (valorile neatinse rămân, valorile noi apar, valorile
#   modificate se modifică)

with open("data/ages.json") as f, \
     open("data/ages_update.json") as fup:
    data = json.load(f)
    updates = json.load(fup)

    # următoarele fac același lucru:

    # for k, v in updates.items():
    #     data[k] = v

    # for k in updates.keys():
    #     data[k] = updates[k]

    data.update(updates)

# 3. scrieți noul dataset într-un fișier
# "ages_latest.json"

with open("data/ages.json") as f, \
     open("data/ages_update.json") as fup, \
     open("data/ages_latest.json", 'w') as ffinal:
    data = json.load(f)
    updates = json.load(fup)
    
    data.update(updates)

    json.dump(data, ffinal, indent=2)

# 4. opțional: scrieți datele finale
#    înapoi în "ages.json", astfel
#
#   v1) deschideți "ages.json" o dată pentru citire,
#       apoi încă o dată pentru scriere.
#   v2) deschideți-l pentru citire și scriere simultană
#   v3) deschideți-l pentru citire.
#       scrieți într-un fișier temporar ".temp.ages.json".
#       mutați pe ".temp.ages.json" peste "ages.json".


from os import path, rename

def apply_updates(infile, updatefile):
    dir, fname = path.split(infile)
    tempfile = path.join(dir, f".temp.{fname}")

    with open(infile) as f, \
         open(updatefile) as fup, \
         open(tempfile, 'w') as ftemp:
        # we load the original data
        data = json.load(f)
        # we load the updates data
        updates = json.load(fup)
        # we apply the updates in-place
        data.update(updates)

        # and write to the temp file
        json.dump(data, ftemp, indent=2)

    rename(tempfile, infile)
    # pt. atomicitate
    # 1) write new file
    # 2) rename old file into something temporary
    # 3) rename new file into old file
    # 4) remove temporary (old) file


DATA_DIR = "/home/john/Work/Curs/Python/py-beginners-2025.09.30/data"

apply_updates(
    path.join(DATA_DIR, "ages.json"),
    path.join(DATA_DIR, "ages_update.json")
)