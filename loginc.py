a = 5
print(2 < a < 100)
name = "patryk"
print(len(name))
print(name.capitalize())
print(name.upper())
print(name[0:2])  # two first
print(name[0:])  # whole
print(name[-3:])  # last 3 charakters

channel = "Jak nauczyc sie programowania"
new = channel.split(" ") # ['Jak', 'nauczyc', 'sie', 'programowania']

print(new)
print(type(new))
joinstr = "-_-"
joined = joinstr.join(new)
print(joined)   # Jak-_-nauczyc-_-sie-_-programowania
print(type(new))

print(joined.rstrip("n"))