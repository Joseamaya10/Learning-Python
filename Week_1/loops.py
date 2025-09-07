n = 0
while True:
    if n == 3:
        break 
    print(n)
    n = n + 1
print("Loop ended")
print("-----------------------")
for i in [2,1,5]:
    print(i)
print("Loop ended")
print("-----------------------")

numbers = [1, 3, 56, 87, 100, 98, 12 ,23, 200]
def find_highest(highest, number):
    for num in number:
        if highest < num:
            highest = num
    return highest

print(find_highest(500000, [1, 200, 1000, 500, 2000, 4000, 200000, 3000000, 1000000, 10000000, 90000, 333, 99999, 1009293, 10100000]))

highest = [1, 200, 1000, 500, 2000, 4000, 200000, 3000000, 1000000, 10000000, 90000, 333, 99999, 1009293, 10100000]
print(max(highest))
print("Loop ended")
print("-------------------------")
 
 #finding the error in the code
 
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 0, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

smallest = 6
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 2, 15, 1, 74, 0, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)