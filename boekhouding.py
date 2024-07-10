from helper import *                        # L10.1.4 import functies en variabelen uit helper
from presentatie import *					# L10.1.9 import alle functies en variabelen uit presentatie.py
import csv									# L10.1.10 importeer het pakker csv.
# L10.1.13 git init
# L10.1.13 git commit -m "Les 10 - repository nieuwe projectfolder in VScode"
# dictionary inkomsten
inkomsten = {
"Aardbeien-ijs-totaal" : 1000,
"Vanille-ijs-totaal" : 2000,
"Chocolade-ijs-totaal" : 1500,
"Water-ijsjes-totaal": 750,
}
# L10.1.8 2e dictionary
mijn_dict = {'vis': 10, 'vlees' : 25, 'overig' : 15}

totaal_inkomsten = som(inkomsten)           # L10.1.5 maak variabele totaal_inkomsten; ken de totale som aan deze variabele
totaal_inkomsten2 = som(mijn_dict)			# L10.1.8 gebruik 2e dictionary

presenteer(inkomsten, totaal_inkomsten)
presenteer(mijn_dict, totaal_inkomsten2)

with open('boekhouding.csv', 'w', newline='') as csvfile:
	for key, value in inkomsten.items():
		writer = csv.writer(csvfile, delimiter=';')
		writer.writerow([key, value])

with open('mijn_dict.csv', 'w', newline='') as csvfile:
	for key, value in mijn_dict.items():
		writer = csv.writer(csvfile, delimiter=';')
		writer.writerow([key, value])
