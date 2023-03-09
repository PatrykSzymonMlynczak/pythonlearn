x = "green"

if x == 'red':
    print("stop")
elif x == 'yellow':
    print('prepare to go ')
else:
    print('go')

print("Jedź!") if x == 'green' else print("Czekaj!")

number = 1

while number <= 3:
    print(number)
    number += 1

for number in range(1, 13, 3):
    if number == 7:
        continue  # break
    print(number)

lista = ["a", "b", "c"]
nejm = "nejm"

for x in nejm:
    print(x)

for x in lista:
    print(x)
list.append("dee")
print(lista.count("a"))
print(lista[0])
print(lista.pop(0))  # taking element from list
print(lista[0])
list.remove(0)
print(len(lista))
lista.clear()

nowa = []



