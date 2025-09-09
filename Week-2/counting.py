fh = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
inp = fh.read()
print(len(inp))
print(inp[:20])

fh = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
count = 0
for line in fh:
    if line.startswith("From:"):
        print(line.strip())
        count = count + 1
print("Line Count: ", count)

fh = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
for line in fh:
    line = line.strip()
    if not line.startswith("From:"): 
        continue
    print(line)

fh = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
for line in fh:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)