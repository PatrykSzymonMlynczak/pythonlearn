tupla = ("asd", "dsa", "sda", 3, [3, 4.1])
krotka = 'df', 12, "3452fd", [3, 56.3], (3, "df", 12), 12
# round parentheses, or without any
# tuple is immutable - inserting only once, removing impossible
# can handle multiple different types
# can be created new tuple from two others
# tuple can be multiplicated
# fastest than list, even 10 times
# can be used as a key in dictionary
# can be uses as constan parameters as days of week

first = tupla[0]  # first
last = tupla[-1]  # last: minus is just setting start indexing on the right side
sec_to_last = tupla[1:]  # from second to last

print("first", " -> ", first)
print("last", last)
print("sec_to_last", sec_to_last)
print("tupla", tupla)
print("krotka", krotka)
nowakrota = krotka + tuple("krotka")
print("ocurrence of 12 ->", krotka.count(12))
print(12 in krotka)  # is true that exist in
print(nowakrota)
print(tupla * 3)

trikrotka = ("param1", 2, [3, 2])
param1, num, lista = trikrotka
print(param1, num, lista)
