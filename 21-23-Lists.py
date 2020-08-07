# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

""" myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A"]
print(myAwesomeList) 

# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

"""

myAwesomeList = ["One", "Two", "There", 1, 2, 2.18]

print(myAwesomeList)


print(myAwesomeList[1])
print(myAwesomeList[-1])

print(myAwesomeList[0:4:2])

myAwesomeList[2: 5] = ["qdfdjlsd"]
print(myAwesomeList)
# myAwesomeList[6] = "ksjfml"
myAwesomeList.append(["One", "Twsqo", "There", 1, 2, 2.18])

print(myAwesomeList)
# print(myAwesomeList[4][1])


a = [1, 2, 3, 4]

b = [1, 2, 3, 41, 2, 3, 41, 2, 3, 4]

a.extend(b)

print(a)
a.sort()
print(a)

c = a
d = a.copy()
print(a)
print(c)
print(d)
a.append(49)
print(a)
print(c)
print(d)

print(a.count(1))
# print(a.index(10))
print(a)
print(a.pop(-1))
print(a)
