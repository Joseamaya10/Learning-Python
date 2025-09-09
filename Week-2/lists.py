stuff = list()
stuff.append("hello")
stuff.append(0) # The method append add a single item in the end of a list
stuff.extend([1, 2]) # The method extend add multiple items on a list
stuff.insert(4, 3) # The method insert add an item in a specific position of a list
stuff.reverse() # The method reverse reverse the order of the items in a list
print(stuff)
#stuff.sort() # The method sort sort the items in a list but only if they are comparable
print(1 in stuff) # The operator in check if an item is in a list
