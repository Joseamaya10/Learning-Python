counter = 0
suma = 0
values = [4, 10, 87, 90, 15, 23, 67, 200]
for value in values:
    suma = suma + value
    counter += 1
    print(counter, suma, value)
print("el promedio es:", suma/counter)
print(sum(values)) 

Edad = int(input("Cual es tu edad?"))
if Edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")