# # Intrebare 1:
# # se da urm cod:
#
# v1 = "Hello World"
#
# print(v1[0], v1[1], v1[-6])

# Primitive data type. int

x1 = 10

def change(x1):
    x1 = 11

change(x1)
print(x1)



x2 = [10, 324, 234 ,23, 12]

def change(x2):
    x2[3] = 11


change(x2)
print(x2)


print("==========================Curs Functii 06===================================")


#
# def process_data(list1):
#     # o sa primeasca list1 = [3, 5, 10, 11, 300]
#     # O sa returneze, de exemplu:
#
#     # ex_dictionar = {
#     #     "odd_numbers": [3, 5, 11, 13, 201],
#     #     "even_numbers": [2, 4, 8, 10, 12, 200, 340],
#     #     "odd_total": 233,
#     #     "even_total": 576
#     # }
#
#     result = {}
#     odd_list = []
#     even_list = []
#
#     for n in list1:
#         if is_even(n):
#             even_list.append(n)
#         else:
#             odd_list.append(n)
#
#     result["odd_numbers"] = odd_list
#     result["even_numbers"] = even_list
#     result["odd_total"] = list_total(odd_list)
#     result["even_total"] = list_total(even_list)
#     return result

# Built in functions and tools:

print("===================================Other Functions=======================================")

# map(), filter(), reduce(), sorted(), funtii lambda

# Funtii lambda(ANONIMA----> NU ARE UN NUME!)


# funtii map

lista2 = [3, 5, 10, 20, 1, 9, 12, 16]
# 3
# 5
# 10
# 20
# 1
# 9

def mult2(nr):
    return nr * 2
def pow_2(nr):
    return nr ** 2
# lista3 = []
# for num in lista2:
#     lista3.append(mult2(num))
#
# print(lista3)
result1 = list(map(pow_2, lista2))

print(result1)

# def div_%(x):
#     return x / 5
# result2 = list(map(div_5, lista2))

result3 = list(map(lambda x: x / 5, lista2))

print(result3)

# Filter:

nr_pare = list(filter(lambda x: x % 2 == 0, lista2))

print(nr_pare)

nr_mari5 = list(filter(lambda x: x > 5, lista2))
print(nr_mari5)
print("==========================Exercitii========================")
lista5 = [7, 10, 14, 13, 30, 60]
#
# rezult = {
#     7: "impar",
#     10: "par",
#     14: "par",
#     13: "impar",
#     30: "par",
#     60: "par"
# }
# #
# strings = list(map(lambda x: "par" if x%2 == 0 else "impar", lista5))
rezult = dict(
    map(lambda x: (x, "par" if x % 2 == 0 else "impar"), lista5)
)

print(rezult)