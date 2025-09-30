# Exercițiu:
# scrieți o funcție `count_appearances(term, text, insensitive=False)`
# ce returnează numărul de apariții al lui `term` în `text`.
def count_appearances(term, text, insensitive=False):
    if insensitive:
        term = term.casefold()
        text = text.casefold()
    return text.count(term)

# testați funcția pe string-ul
s = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."

print(count_appearances("it", s))

print(count_appearances("it", s, True))


print("""
There are 2 difficult problems in computing:
  - naming things
  - cache invalidation
  - off-by-one errors
""")