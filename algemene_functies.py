# Opgave 8.1.1 maak functie "mijn_functie_2()" in bestand "algemene_functies.py"

# Opgave 8.1.2 Maak een functie "mijn_functie_1()" en kies uit argumenten en krijg teruggeefwaarde uit de lijst
lijst = { 2 : 4, 4 : 16, 10 : 100, 12 : 144 }
def mijn_functie_1(a):
    return a * a
print(mijn_functie_1(4))


# Opgave 8.1.3 maak functie "mijn_functie_2()" geimporteerd uit 'aanbieding.py' plaats in bestand "algemene_functies.py" 
def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
print(mijn_functie_2(100,20))            # vul de waarden van a en b  in.
