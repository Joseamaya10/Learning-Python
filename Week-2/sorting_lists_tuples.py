c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

print()

import urllib.request
poema = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in poema:
    line = line.decode()
    words = line.split()
    for word in words:
      counts[word] = counts.get(word, 0) + 1
lista = list()
for key, value in counts.items():
    tupla = (value, key)
    lista.append(tupla)
lista = sorted(lista, reverse=True)
print(lista)
for value, key in lista[:10]:
    print(key, value)