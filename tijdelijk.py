# 7.1.9. elementen met meer dan 5 of meer karakters worden in hoordletters geprint 
prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
    }

aanbieding = prijzen["vanille"] * 1   # 10% korting
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

reclame_tekst2 = reclame_tekst[:60]

reclame_tekst3 = reclame_tekst.upper()

reclame_tekst4 = reclame_tekst3.split()

for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())
