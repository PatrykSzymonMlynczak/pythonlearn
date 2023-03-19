coun_info = {}
coun_info["poljaki"] = ("łorsoł", 38, ["sd","sads"])
coun_info["Dojcze"] = ("Berlin", 83.02)
coun_info["Słowaki"] = ("Bratisława", 5.45)

for country in coun_info:
    print(country)




def metoda():
    country = input("Jakiego kraja  info chcesz ? ")
    info = coun_info.get(country)
    print()
    print(country)
    print("---------")
    print("Capitol:", info[0])
    print("Wiela ich:", info[1], "miljonuf")


def sum(a , b):
    print(a+ b)

sum(1,2)

def sum(a , b):
    return a+b

print(sum(1,2))
