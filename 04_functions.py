
def user_hello(name):
    print(name)
    # print("Hello World")
    print(f"this is {name} speaking. I am happy to be here>")


user_hello("Adrian")
user_hello("Jack")
user_hello("Tom")
user_hello("Dionis")
print("=================================")

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

result1 = add(2, 20)

print(result1 + 20)

result2 = multiply(2, 20)
print(result2)

# (2 + 10) * 13

result3 = multiply(add(2, 10), 13)
print(result3)
print("=========================")


def slice_list_in_half(param_list):
    return param_list[(len(param_list)+1)//2: len(param_list)]

lista1 = [40, 99, 101, 8, 67, 1, 13, 888, 777]

rezultat = slice_list_in_half(lista1)
print(rezultat)

def slice_first_half(param_list):
    return param_list[:len(param_list)//2]
print(slice_first_half(list(range(1, 1000))))