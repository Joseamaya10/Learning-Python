values = [86, 24, 97, 17, 56, 3, 100, 34, 65, 29,-5, 10, -23, -2, 45]
smallest = None
for value in values:
    if smallest is None or value < smallest:
        smallest = value
print("New smallest found:", smallest)

#Another way to do it

