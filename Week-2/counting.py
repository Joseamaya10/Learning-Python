fh = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
count = 0
inp = fh.read()
print(len(inp))
print(inp[:20])
for line in fh:
    if line.startswith("From:"):
        print(line)