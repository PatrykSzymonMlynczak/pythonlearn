eggs = {'name': 'Zophie', 'species': 'kot', 'age': '8'}
ham = {'species': 'kot', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  # dictionary order does not matter

print("species" in ham)
print("kot" in ham.values())
ham.setdefault("nowyklucz", "cokolwiek")
ham.setdefault("nowyklucz", "to już nie zadziała ")

# liczenie wystąpień danych znaków w ciągu
message = 'jakieś tam zdanie.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

import pprint
pprint.pprint(sorted(count.items()))