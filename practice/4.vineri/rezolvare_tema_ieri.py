# grep cu highlight
def grep2(pattern, filename, highlight=True):
    list = []
    with open(filename) as f:
        for line in f:
            if pattern not in line:
                continue

            if highlight:
                line = line.replace(pattern,f"!{pattern}!")

            list.append(line)

    return list

# count de words
import re

def clean_words(s):
    return re.sub(r'[^\w\s]', ' ', s)

def clean_words_simple(s):
    return s.replace(","," ").replace("."," ")

def count_words(txt, insensitive=False):
    out = {}
    # aflăm cumva care sunt cuvintele unice
    # le punem în dicționar
    # și incrementăm count-ul după cum este nevoie
    
    if insensitive:
        txt = txt.lower()

    lst = txt.split()
    for word in lst:
        if word not in out:
            out[word] = 1
        else:
            out[word] +=1
    return out

print(count_words(clean_words(s)))
print(count_words(clean_words_simple(s)))