countries_and_capitals = {"poland": "warsaw", "germany": "berlin", "czechia": "prague"}

file = open("countries_and_capitals.txt", "w+")
for country, capital in countries_and_capitals.items():
    file.write(country + "-" + capital + "\n")

file.close()
file = open("countries_and_capitals.txt")
line = ""
for char in file.readline():
    line += char
print("read first line: ", line)
# for now cusor is after first line, to read whole file should it be opened once again
for line in file.readlines():
    print(line)
# this should not do anything
for line in file.readlines():
    print(line)
# once again opened without closing ?
file_second_open = open("countries_and_capitals.txt")
for line in file_second_open.readlines():
    print(line)
file.close()
file_second_open.close()
