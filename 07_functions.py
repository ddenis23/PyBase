student = {
    "name": "Adrian",
    "age": 30,
    "height": 70,
    "weight": 90,
    "backpack": ["keys", "wallet", "camera", "phone"],
    0: "nothing at all",
    (1, 2): "alpha and omega"
}


student2 = {
    "name": "Marius",
    "age": 25,
    "weight": 76,
    "baclback": []
}

student3 = {
    "name": "Catalin",
    "age": 30,
    "height": 70,
    "weight": 90,
    "backpack": ["keys", "wallet", "camera"],
    0: "nothing at all",
    (1, 2): "alpha and omega"
}

def get_back_pack(param1):
    return param1["backpack"]
def func_goala():
    pass

print(get_back_pack(student3))

# clase
class Dog:
    pass

# dog este o clasa
var1 = Dog()
# var1 -> instanta al vlasei dog
print(var1)

print("=============================CLass Properties==================================")

# var4 = Dog()
# var4.name = "Spot"
# var4.owner = "Iulian"
# var4.legs = 4
# var4.last_vaccine = 2025
# print(var4.__dict__)
# print(var4.name)
#
# var5 = Dog()
# var5.name = "Shadow"
# print(var5.__class__)
# print(var5.__dict__)
# self -> referinta la instanta cu care lucram, sau obiectul!!
class Cat():
    def __init__(self, name, owner, legs, last_vaccine=None):
        self.name = name
        self.owner = owner
        self.legs = legs
        self.last_vaccine = last_vaccine
        # metoda
        #
    def make_sound(self):
        print(self.name, "Meowww")

    def take_a_bite(self, param1):
        a_bite = param1.pop(0)
        print(f"{self.name} took a bite of {a_bite}")

var6 = Cat("Missy", "Vlad", 4, 2025)
print(var6.__dict__)
var7 = Cat("Kitkat", "Ana-Maria", 4)
var7.make_sound()

snacks = ["fish_snack", "meat_popsickle", "milk", "catnip", "fresh_nap"]
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)

# snacks.pop(0)