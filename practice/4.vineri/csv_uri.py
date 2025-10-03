import csv

# reading a csv as lists
with open("/tmp/out.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


people = [
    ('Jane', 20),
    ('Mike', 17),
    ('Anna', 25),
    ('Sam', 40),
    ('Dan', 34),
]

# writing tuples into csv
with open("/tmp/out.csv", 'w') as f:
    writer = csv.writer(f)
    for person in people:
        writer.writerow(person)


# cum generăm o listă de dicționare?
# ATENȚIE: nu faceți așa, soluția simplă mai jos
with open("/tmp/out.csv") as f:
    reader = csv.reader(f)
    is_first = True
    for row in reader:
        if is_first:
            header = row
        else:
            print(dict(zip(header, row)))
        is_first = False

# citire ca dicționare (cum trebuie)
# aceasta este soluția simplă
with open("/tmp/out.csv") as f:
    dreader = csv.DictReader(f)

    for row in dreader:
        print(row)

# cu fieldnames specificat
with open("/tmp/out.csv") as f:
    dreader = csv.DictReader(f,
                             fieldnames=["numele", "vârsta"])

    for row in dreader:
        print(row)


people = [{'name': 'Jane', 'age': 20},
 {'name': 'Mike', 'age': 17},
 {'name': 'Anna', 'age': 25},
 {'name': 'Sam', 'age': 40},
 {'name': 'Dan', 'age': 34}]

# the dict writer
with open("/tmp/out.csv", 'w') as f:
    dwriter = csv.DictWriter(f,
                             fieldnames=people[0].keys())
    dwriter.writeheader()

    for p in people:
        dwriter.writerow(p)

# we can write all rows at once
with open("/tmp/out.csv", 'w') as f:
    dwriter = csv.DictWriter(f,
                             fieldnames=people[0].keys())
    dwriter.writeheader()
    dwriter.writerows(people)
