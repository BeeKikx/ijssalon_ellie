# Opgave 8.1.12a - importeer functie mijn_functie_2(a,b) uit bestand 'algemene functies.py'
def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
print(mijn_functie_2(100,200))            # vul de waarden van a en b  in.

# opgave 8.1.12b - maak functie combinatie(invoer_lijst_2) in het bestand 'reclame.py'
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

# Opgave 8.1.4 - bestand 'reclame.py' aan map 'IJssalon-start'

# Opgave 8.1.5 - plaats functie "aanbieding_1()" met 3 parameters
# Als functie wordt aangeroepen moet de teruggeefwaarde vd functie worden weergegeven
smaak = ("Aardbei")
prijs = 3.60
korting = 0.1
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro '''
    return uitvoer
print(aanbieding_1(smaak, 3.25, 0.12))



# Opgave 8.1.6 maak functie 'inkomsten_totaal(x)' in bestand 'reclame.py'
def inkomsten_totaal(x):
    totaal = 0
    for getal in x:
        totaal += getal
    return totaal

lijst = [220 , 430 , 125 , 160 , 205 , 90 , 345]
print ("Totale inkomsten : €" , inkomsten_totaal(lijst))



# Opgave 8.1.7 extra argument (btw) aan functie 'inkomsten_totaal()'
def inkomsten_totaal(x):
    totaal = 0
    for getal in x:
        totaal += getal
    return totaal

lijst = [220 , 430 , 125 , 160 , 205 , 90 , 345]
btw = inkomsten_totaal(lijst) * (0.01 * 9)
print(f"Het totaal van alle inkomsten van deze week is : €{inkomsten_totaal(lijst)} euro, waarover : € {btw} euro btw betaald dient te worden.")



# Opgave 8.1.8 maak functie 'laag_en_hoog(lijst)' in het bestand 'reclame.py'
def laag_en_hoog(lijst):
    global x, y
    x = str(max(lijst))
    y = str(min(lijst))
    return 

lijst = [220 , 430 , 125 , 160 , 205 , 90 , 345]
z=(laag_en_hoog(lijst))
print(f"Het laagste inkomen: €" , y, "het hoogste inkomen: €" , x )



# Opgave 8.1.9 maak een functie 'gemiddelde()'  in het bestand 'reclame.py'
def gemiddelde(lijst):
    global x
    x = sum(lijst) / len(lijst)
    return x

lijst = [220 , 430 , 125 , 160 , 205 , 90 , 345]
x = gemiddelde(lijst)
print(f"Het gemiddelde inkomen: €" , x)  


# Opgave 8.1.10 maak functie 'gemiddelde(lijst)' met teruggeefwaarde een string
def gemiddelde(lijst):
    x = sum(lijst)
    return x

lijst = [220 , 430 , 125 , 160 , 205 , 90 , 345]
x = gemiddelde(lijst)
print(f"De gemiddelde inkomsten zijn € {x} euro")  



# Opgave 8.1.11 maak functie meervoudig() met teruggeefwaarde een string  in het bestand 'reclame.py'
def meervoudig(invoer_lijst):
    global x, y
    x = str(max(invoer_lijst))
    y = str(min(invoer_lijst))
    return 
    
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
z = meervoudig(invoer_lijst)
print(f"Het laagste inkomen: €" , y, "het hoogste inkomen: €" , x )

# Opgave 8.1.12 maak functie combinatie(invoer_lijst_2). Deze roept functie meervoudig(invoer_lijst_2) aan 
# Plaats deze aan het begin van het bestand "reclame.py"