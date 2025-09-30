# Exercițiu:
# scrieți o funcție ce face print() parametrului primit

def myfunc(param):
    print(param)

myfunc("bla bli blu")


# scrieți o funcție ce returnează parametrul primit înmulțit cu 3
def multiply_string(param):
    s = param * 3
    return s

def multiply_string(param):
    return param * 3

def greet(name, times=1):
    # salută pe `name` de `times` ori
    for i in range(times):
        print("Hello " + name)

def greet(name, times=1):
    # salută pe `name` de `times` ori
    while times:
        print("Hello " + name)
        times -= 1
