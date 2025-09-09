count = 0
total = 0
while True:
    value = input("Enter a number, and when you finish, type 'done':")
    if value == "done": break
    value = float(value)
    total += value
    count = count + 1
print("avarege: ", total / count)

print("------------------------------------")

print("Another method")
lista = list()
while True:
    value = input("Enter a number, and when you finish, type 'done':")
    if value == "done": break
    lista.append(float(value))
print("avarege: ", sum(lista) / len(lista))