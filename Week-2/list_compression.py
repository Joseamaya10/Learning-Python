import urllib.request
poema = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in poema:
    line = line.decode()
    words = line.split()
    for word in words:
      counts[word] = counts.get(word, 0) + 1

lista = sorted([(key, value) for value, key in counts.items()], reverse=True)
print(lista[:10])
for value, key in lista[:10]:
    print(key, value)