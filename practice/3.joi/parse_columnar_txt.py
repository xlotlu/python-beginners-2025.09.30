SEPARATOR = "|"

def parse_header(s):
    columns = []

    for col in s.split("|")[1:-1]:
        columns.append(col.strip("#"))

    return columns

def parse_row(s, sep=SEPARATOR):
    lst = []
    for i in s.split(sep)[1:-1]:
        lst.append(i.strip(" "))
    return lst


# scrieți o funcție process_report
# care, dat fiind stringul
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
# returnează o listă de dicționare,
# unde cheile provin din numele coloanelor
# și valorile din fiecare celulă.
#
# fiecare dicționar reprezintă un row
# din sursa de date.

def process_report(report) :
    report = report.strip()

    lines = report.split("\n")

    header = parse_header(lines[1])
    #print (header)

    out = []

    rows = lines[3:-1]
    for r in rows:
        row = parse_row(r)

        """
        d = {}

        # v.1: brute force-ish, by list index
        for idx in range(len(header)):
            k, v = header[idx], row[idx]
            d[k] = v

        # v.2: the same, but improved
        for idx, k in enumerate(header):
            v = row[idx]
            d[k] = v
        """

        # v.3: nice and elegant, because `zip()`
        d = dict(zip(header, row, strict=True))
        
        out.append(d)
    
    return out


print(
    process_report(report)
)
