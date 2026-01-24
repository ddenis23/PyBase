# Tuplu

coordonate_punct1 = (3, 5)
coordonate_punct2 = (0, 10)

persoana1 = ("Dionis", 25, "Bucuresti", "Student", True, 400, 173, 72)

print(coordonate_punct1)
print(coordonate_punct2)

# assign
#error
# persoana1[3] = "Tutore"
# print(persoana1[3])

persoana2 = ("Dionis", 25, "Bucuresti", "Tutore", True, 400, 173, 72)

tuplu2 = ("Tudor", (30, "Cluj", "Tamplar", ("Universitate", "Europa", ("Chisinau", "Bucuresti", ("Moldova", "Ucraina", "Romania")))))
print(tuplu2[1][3][2][2][1])

print("=============END============")

# End tuples

# Sets

# {1, 23, 53, 645, 34}
# {}
# {3, 4, 3} -> not a set

var2 = {3, 4, 10, 0, 40}


var2.add(100)
var2.remove(10)
print(var2)


# Complexitate
# O(n)
persoane = ["Tudor", "Darius", "Vlad", "Maria", "Adrian", "Flavia", "Vlad", "Marius"]

print(persoane)

var4 = set(persoane)
print(var4)

# 7 Pasi
# Complexitatea codului este O(n) ---> n = numarul de elemente -----> Liniar
if "Marius" in persoane:
    print("Marius este printre noi!!")

else:
    print("Marius nu este printre noi!!")

# 1 Pas
# Complexitatea este O(1) ---> Constant
if "Marius" in var4:
    print("Marius este printre noi!!")

else:
    print("Marius nu este printre noi!!")

# END SETS

print("===========END=============")

# Lists + Strings

str1 = "LOG: Hello this is vlad the impaler."
str2 = "WARN: My story is way overblown"
str3 = "ERROR:&$!@#$%^&*())(*&^%$#!@#"

list3 = ["adrian", "client", "studenti"]
list4 = [str1, str2, str3]

# print(list4[0].split(":"))

print(len(list4))
print(list(range(len(list4))))


for i in range(len(list4)):
    # print(list4[i])
    list4[i] = list4[i].split(":")

print(list4)

print("========================")


list5 = []

# task: split all the strings in our list, split them using the":" character.
# example: "

