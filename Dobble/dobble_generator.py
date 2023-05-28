def GenerateCards(n):
    kartya_szam = n - 1

    kartyak = []

    for i in range(kartya_szam + 1):

        # A kartyakhoz hozzáillesztjük a kezdőszámot (1)
        kartyak.append([1])
        for j in range(kartya_szam):
            # Hozzáadunk n - 1nyi számot a lista elemeihez
            # Pl, ha n = 3, akkor 2 darab számot hozzáadunk
            # A legelső ilyen szám az első kártyán (0 + 1) + (0 * (n - 1) + 1) = 2
            # A második ilyen szám az első kártyán (1 + 1) + (0 * (n - 1) + 1) = 3
            # És így tovább...
            kartyak[i].append((j + 1) + (i * kartya_szam) + 1)

    # Hozzáadunk kartya_szam x kartya_szam-nyi kártyát
    for i in range(kartya_szam):
        for j in range(kartya_szam):
            kartyak.append([i + 2])
            for k in range(kartya_szam):
                val = (kartya_szam + 1 + kartya_szam * k + (i * k + j) % kartya_szam) + 1
                kartyak[len(kartyak) - 1].append(val)

    return kartyak


if __name__ == "__main__":
    for i in GenerateCards(3):
        print(i)



