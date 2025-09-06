fruit = "orange"
index = 0
letter = fruit[index]
count = 0
for letter in fruit:
    print(count, letter)
    count += 1

while index < len(fruit):
    letra = fruit[index]
    print(index, letra)
    index += 1
    
    s = "practicing with python"
    
print(s[0:7])
print(s[:80])
print(s[10:])
print("Banana" < "banana") # uppercase letters are "less than" lowercase letters

My_Last_names = ["Vergara", "amaya"]
My_Last_names.sort()
print(My_Last_names)

Capitalized_Names = [names.capitalize() for names in My_Last_names]
print(Capitalized_Names)
Capitalized_Names.sort()
print(Capitalized_Names)

print("-------------------------------------")
print("-------------------------------------")

Last_names = "Vergara amaya"
encuentra_maya = Last_names.find("maya")
print(encuentra_maya)


Ramdom_string = "Hi, I'm learning python. Python is fun. Python is easy to learn."
piece_of_word = Ramdom_string.find("fun")
piece_of_word2 = Ramdom_string.find(".", piece_of_word)
print(piece_of_word, piece_of_word2)
word = Ramdom_string[piece_of_word-1:piece_of_word2]
print(word)
