countries_and_capitals = {"poland": "warsaw", "germany": "berlin", "czechia": "prague"}
try:
    print(2 / 0)
    print(countries_and_capitals['USA'])

except ZeroDivisionError:
    print("Nie dziel cholero przez zero ! ")
except KeyError:
    print("nima usa")
finally:
    print("zawsze to poleci")
