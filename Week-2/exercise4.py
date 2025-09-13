#Exercise 4: Add code to the above program to figure out who has the most messages 
# in the file. After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) 
# to find who has the most messages and print how many messages the person has.

fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
counts = dict()
for line in fhand:
    lista = line.strip()
    lista = lista.split()
    if len(lista) < 1: continue
    if lista[0] != "From": continue
    counts[lista[1]] = counts.get(lista[1], 0) + 1

contador = None
for key, value in counts.items():
    if contador is None or value > contador:
        contador = value
print(f"The email of the person who sent the most messages is {key} with {contador} messages")

#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of 
# who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your 
# dictionary.

fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
lista_dominios = list()
diccionario_correos = dict()
for line in fhand:
    if line.startswith("From"):
        line = line.split()
        correos = line[1].split("@")
        dominios = correos[1]
        lista_dominios.append(dominios)
        
for dominio in lista_dominios:
    diccionario_correos[dominio] = diccionario_correos.get(dominio, 0) + 1
print(diccionario_correos)
     