try:
    # chestii
    1 / 0
    pass
except KeyError:
    pass
except IndexError:
    #...
    pass
else:
    print("eu mă rulez doar dacă try a mers bine")
finally:
    print("eu mă rulez __întotdeauna__ la final!")


try:
    # chestii
    1 / 0
    pass
except KeyError as e:
    pass
except IndexError as e:
    #...
    pass
except Exception as e:
    # putem captura excepția!
    print("a fost o excepție", type(e), e)
    raise e
else:
    print("eu mă rulez doar dacă try a mers bine")
finally:
    print("eu mă rulez __întotdeauna__ la final!")
