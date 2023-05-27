from dobble_generator import GenerateCards



szamipt = int(input("Kérek egy számot! "))


kartyak = GenerateCards(szamipt)

for i in kartyak:
    print(i)
