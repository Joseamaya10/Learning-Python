fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
lista_dias = list()
for line in fhand:
    line = line.strip()
    if line.startswith("From"):
        line = line.split()
        if len(line) < 3:
            continue
        days = line[2]
        lista_dias.append(days)
days = lista_dias
counts = dict()
for day in days:
    counts[day] = counts.get(day, 0) + 1
print(counts)

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
counts['quincy'] = counts['quincy'] + 1
print(counts.get('quincy', 0))