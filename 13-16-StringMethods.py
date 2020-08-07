print(len("sqfjpqs opsdfk pqos"))

print("sdjfjdfk qpsofqksf    ".strip())
# == trim  strip("string") remove string
print("     sdjfjdfk qpsofqksf    ".rstrip())
print("     sdjfjdfk qpsofqksf    ".lstrip())

# title()
# make string after number capitale
print("I live 2d Graphics and 3g Technology and Python".title())
# make string after number minimal
print("I live 2D Graphics and 3G Technology and Python".capitalize())


a, b, c = "1", "11", "111"

print(a)
print(b)
print(c)

print(a.zfill(3))  # zfill add some namber of Zero on the right of string number
print(b.zfill(3))
print(c.zfill(3))

print("Badah".upper() + " BILAL".lower())


print("bilal badah mohamed mechdoud adelatif akrari zakaria zguimi".split())
print("bilal badah mohamed mechdoud adelatif akrari zakaria zguimi".split(" ", 2))
print("bilal badah mohamed mechdoud adelatif akrari zakaria zguimi".rsplit(" ", 2))

print("BADAH".center(11, "@"))

# serch how many time find the same string in main string
print("I love PHP and Python because PHP is very easy".count("PHP", 0, 23))

# change every character in the string between capital and minimal
print("i AM badah bILAL".swapcase())
print("i AM badah bILAL".swapcase().swapcase())

# chech if the main string start with the specific string
print("Bilal Badah".startswith("Ba", 6, 9))
print("Bilal Badah".startswith("B", 5, 9))

# chech if the main string end with the specific string
print("Bilal Badah".endswith("h", 5))
print("Bilal Badah".endswith("h", 5, 9))


# string.index("substring",strat,end) => string.indexOf()
# string.find("substring",start,end) => string.indexOf() defrent between find and index if index are not found substring then throw exception but find give us -1 as result

print("badah".rjust(10))
print("badah".rjust(10, "#"))  # add # in the left of string

print("""jsedfjsf spofjks
sfgskjgs
sdkgjspdgj
sdgkjsdgj""".splitlines())


print("ahdjapoizdk".isalpha())
# check if string just character dont have number
print("ahdjapoizdk 11".isalpha())
# check if string has character and number
print("ahdjapoizdk 11".isalnum())

# replace the old substring with new substrin in main string
print("bb aijdj bb jijoi bb oijh bb".replace("bb", "cc", 1))

# add all item of list in one string with separator character
print(",".join(["one", "two", "three"]))
print(" _ ".join(["one", "two", "three"]))
print(" - ".join(["one", "two", "three"]))
