#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.
# HECHO POR MÍ
fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
lista_correos = list()
counts = dict()
for line in fhand:
    lista = line.strip()
    lista = lista.split()
    if len(lista) < 1: continue
    if lista[0] != "From": continue
    lista_correos.append(lista[1])
for correo in lista_correos:
    counts[correo] = counts.get(correo, 0) + 1
print(counts)

print()
print()
#Hecho por mí, mejorado
fhand = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
counts = dict()
for line in fhand:
    lista = line.strip()
    lista = lista.split()
    if len(lista) < 1: continue
    if lista[0] != "From": continue
    counts[lista[1]] = counts.get(lista[1], 0) + 1
print(counts)

print()
print()

# Get the file name input from the user.  HECHO POR CHATGPT
file_name = input('Enter file name: ')
try:
    # Open the file
    handle = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

email_counts = dict()  # Create an empty dictionary to hold the email counts

# Loop through each line in the file
for line in handle:
    if line.startswith('From '):  # Check for lines starting with 'From '
        words = line.split()  # Split the line into words
        email = words[1]  # The second word in the line is the email address
        # Add the email to the dictionary and increment its count
        email_counts[email] = email_counts.get(email, 0) + 1

# Print the dictionary containing email counts
print(email_counts)


