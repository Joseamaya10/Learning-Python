t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)


t3 = t1 + [3]
print(t3)
t1 is t3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def chop(lista):
    del lista[0]
    del lista[-1]
    return lista
print(chop(lista))

fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])