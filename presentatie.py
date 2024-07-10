def presenteer(dict, totaal):                           #L10.1.8 maak functie presenteer.      
    for key in dict:
        print(key, ':', dict[key], 'euro')
    print("================================")               
    print('Totaal:', totaal, 'euro', end='\n\n')                  
    