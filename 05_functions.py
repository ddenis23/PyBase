import copy

var1 = "Hello"


def change_pariable(param1):
    param1 = "this is not a hello"

# pass by value
change_pariable(var1)

print(var1)

var2 = [30, 100]

def change_varaible_list(param1):
    param1.append(99)

print(var2)
# pass by reference
change_varaible_list(var2)
print(var2)


# max si suma dintr-o lista

lista2 = [40, 90, 100, 10, 4, 1]

def get_total(param1):
    total = 0
    for i in param1:
        total += i
    return total
print(get_total(lista2))

def max_number(param1):
    max =param1[0]
    for nr in param1:
        if nr > max:
            max = nr
    return max

print(max_number(lista2))

print("===============Dictionar===============")
print()
student = {
    "name" : "Dionis",
    "age" : 25,
    "wight" : 74,
    "backpack" : ["keys", "Wallet", "phone"],
    0: "nothing at all",
    (1, 2): "alpha and beta",
}
print(student)
print(student["name"])
print(student["backpack"][1])

for k in student.keys():
    print(k)

for key, value in student.items():
    print(key, "  >>>>>>>>  ", value)
student["age"] = 33
print(student)
student["address"] = "Bucuresti"

print(student.get("nnnn", "default value"))

if "address" in student:
    print("Avem adresa pentru acest student")
else:
    print("Studentul acesta nu are adresa!!")

student2 = student.copy()

student["restante"] = 3
print("Student original:")
print(f"studentul 2 cu restante: {student["restante"]}")
# deep copy example
student3 = copy.deepcopy(student)

student3["backpack"] = "Casti"

print("=====================Function dict exercises========================")
# creaza o functie care aduna toate numerele din dictionar

dict2 = {
    "name" : "Omega",
    "dimensions" : 6,
    "size" : 13,
    "count" : -1,
    "axis" : "y",
    "trees": "all",
}

def add_all_numbers(param1):
    total = 0
    for key in dict2.keys():
        valoare = dict2[key]
        if isinstance(valoare, int):
            total += valoare
    return total




print(add_all_numbers(dict2))

print("=================Odd/Even numbers======================")
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

lista3 = [5, 10, 4, 30, 25, 7]

def add_all_evens(param1):
    total = 0
    for num in lista3:
        if num % 2 == 0:
            total += num
    return total

print(f"Rezultatul adunarii numerelor pare din lista 3 este {add_all_evens(lista3)}")