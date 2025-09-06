Found = False
lista = [43, 12, 5, 7, 9, 2, 1, 0, -1, -5, -10, (4-2)]
for element in lista:
    if element == 2:
        Found = True
        print(Found, element)
        print(f"Element found {element}")
    else:
        Found = False
        print(Found, element)