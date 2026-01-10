a=3
aux =989
a = aux*5

TIMEOUT_MGS_X = 500
print(a)
print(id(a))
suma_doua_numere = 0

check_flag = False
print(type(check_flag))

#variabilele se scriu cu litera mica(snake case (cu underscore___))
example = 5
# example += 3
example +=1
print(example)

b=6
c=a+b
# print(c)

#0,1,2,3,4,..9
# This is for statement
#produs = 1*2*3*4*..*9
suma1 = 0
produs = 1
for i in range(10):
    suma1 = suma1 + i
    produs = produs * (i+1)
print(suma1)

suma2 = 9*(9+1)/2
# print(suma2)
print(produs)
print(type(suma2))

var_flag = True

if var_flag == True:
    print("Astazi este miercuri!!")
else:
    print("Astazi nu este miercuri!!")



for i in range(20):
    if i % 2 == 0:
        print(f"Numarul, {i} este par: ")