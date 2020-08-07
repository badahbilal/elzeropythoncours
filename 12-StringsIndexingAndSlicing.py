# Indexing (access single item)

myString = "I love Python"

print(myString[1])
print(myString[2])
print(myString[-1])
print(myString[-6])


# Slising (Access Multiple Sequence Items)
# [strat:End]
# [start:end:Steps]

print(myString[8:11])
print(myString[1:5])

print(myString[:11])  # start from the beginning
print(myString[8:])  # go to the end

print(myString[::3])
