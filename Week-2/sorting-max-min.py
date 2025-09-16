# highest = None
# while True:
#     number = input("Type a number: ")
#     if number == "done":
#         break
#     elif highest is None or number > highest:
#         highest = number
# print(highest)

numbers = list()
while True:
    number = input("Type numbers one by one to see which is greater and when you finish type 'done': ")
    if number == "done":
        break
    else:
        number = float(number)
        numbers.append(number)
    
print(max(numbers))
print(min(numbers))