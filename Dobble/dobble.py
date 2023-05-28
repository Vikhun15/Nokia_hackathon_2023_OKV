from dobble_generator import GenerateCards
import sys

szamipt = 0

if len(sys.argv) > 1:
    szamipt = int(sys.argv[1])
else:
    szamipt = int(input("Kérek egy számot! "))


kartyak = GenerateCards(szamipt)

for i in kartyak:
    print(i)
