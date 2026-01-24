#
# 1. Creati o lista de numere de la 1 la 100, din 3 in 3, folosind range(), exemplu de lista:
# [0, 3, 6, 9, 12, 15,......]
# 2. Adaugati la sfarsitul listei numere de la 300 la 600, din 10 in 10, sa arate lista in urmatorul fel:
#
# [0, 3, 6, ....., 99, 300, 310, 320, ....., 590, 600]
#
# 3. Stergeti din lista mare numerele 51, 54, 66, 400
# 4. Numarati cate numere se afla in lista.
# 5. Calculati suma tuturor numerelor din lista. Calculati media acestui total.
# 6. Inversati lista, sa fie sortata de la cel mai mare numar la cel mai mic numar.
# 7. Printati cel mai mare numar din lista.
# 8. Faceti un slice din lista, de la mijloc pana la sfarsitul listei.



lista = list(range(0, 100, 3))

lista.extend(range(300, 601, 10))
print(lista)
de_sters = [51, 54, 66, 400]
for numar in de_sters:
    if numar in lista:
        lista.remove(numar)

print("Numar elemente:", len(lista))

suma = sum(lista)
media = suma / len(lista)
print("Suma:", suma)
print("Media:", media)

lista.sort(reverse=True)

print("Cel mai mare numar:", max(lista))

mijloc = len(lista) // 2
slice_lista = lista[mijloc:]
print("Slice:", slice_lista)
