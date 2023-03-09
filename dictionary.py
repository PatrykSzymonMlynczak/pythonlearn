countries_and_capitals = {"poland": "warsaw", "germany": "berlin"}
# adding new :
countries_and_capitals["Czechia"] = "Prague"

for capital in countries_and_capitals.values():
    print(capital)
print(countries_and_capitals.values())

for country in countries_and_capitals.keys():
    print(country)

for pair in countries_and_capitals.items():
    print(pair)

print(countries_and_capitals["Czechia"])  # showing key, but it must exist
print(countries_and_capitals.get("Poland"))  # do not need to exist
print(countries_and_capitals.setdefault("USA", "Washington DC"))
# if key is not exist it will create it, otherway it update value
countries_and_capitals.pop("poland")  # deleting value
#  countries_and_capitals.popitem()  # deleting list item

if "berlin" in countries_and_capitals.keys():
    print("jest")
if "berlin" in countries_and_capitals.values():
    print("we waljusach jes")
else: print("nima nikaj")