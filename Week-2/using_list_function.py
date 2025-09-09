saludo = "Hola Mundo"
saludo2 = "Hola Mundo"
greeting = list(saludo)
print(greeting) #The function list() creates a list of characters from a string
greeting2 = saludo2.split() 
print(greeting2)
#The function split() creates a list of words from a string, by default it uses space as separator. 
#It also needs to be assigned to a variable because it does not modify the original string.
s = 'spam-spam-spam'
ss = s.split("-")
print(ss) 

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))

fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
