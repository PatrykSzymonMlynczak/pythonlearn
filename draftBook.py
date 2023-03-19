# mozna mnożyć rózne elementy np stringi lub tablice,
# aby wymnożyć kazdy element potrzeba pętli w klamrach

tablica = [2, 3, 4]
druga = tablica * 2
print(druga)  # [2, 3, 4, 2, 3, 4]
mnożona = [item * 2 for item in tablica]
print(mnożona)  # [4, 6, 8]
string = "string" * 5
print(string)  # stringstringstringstringstring

import random

for i in range(5):
    print(random.randint(1, 2))


def hello():
    print("siemson")


pusta = print()
print(pusta is None)
print(pusta == None)

# separator
print("raz", "dwa", "czi", sep='-_-')


def spam():
    print(eggs)


eggs = 42
spam()

lista = [1, 2, "s", 4]
print(lista)
del lista[3]
print(lista)
nowa = []
nowa = range(5)
print(nowa[1])
print(2 in nowa)
rozmiar, kolor, typ = [13, "czarny", "kot"]

print(lista.index("1"))