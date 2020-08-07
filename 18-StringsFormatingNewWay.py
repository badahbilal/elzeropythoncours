

name = "BADAH"
age = 24
rank = 10

print("my name is : " + name)

print("My name is : {}".format("BADAH"))
print("My name is : {}".format(name))
print("My name is : {} and My Age is {}".format(name, age))
print("My name is : {:s} and My Age is {:d} and My Rank is {:f}".format(
    name, age, rank))

n = "Badah"
l = "Python"
y = 10

print("My name is {} I am {} Developer with {} Years Exp ".format(n, l, y))

myNumber = 10
print("My Number is : {}".format(myNumber))
print("My Number is : {:f}".format(myNumber))
print("My Number is : {:.2f}".format(myNumber))

# truncate String
myLongString = "Hello Peaoples of Elzero web school I Love You all"
print("Messgae is {}".format(myLongString))
print("Messgae is {:.14s}".format(myLongString))

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")


# https://pyformat.info/
