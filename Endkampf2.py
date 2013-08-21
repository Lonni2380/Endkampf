import random
#....
#Schadensmodell
#Heiltrank = Voller Schaden
#Ausweichen + Biss: 0
#Ausweichen + Feuer: 0.5
#Ausweichen + Tatze: 1
#Verstecken + Feuer: 1
#Verstecken + Biss: 0.5
#Verstecken + Tatze: 0
#Deckung + Biss: 1
#Deckung + Feuer 0
#Deckung + Tatze 0.5

#Drachenaktionen
s = {}
s["feuer"] = {"deckung":0,"ausweichen":0.5,"verstecken":1,"heiltrank":1}
s["biss"] = {"deckung":1,"ausweichen":0,"verstecken":0.5,"heiltrank":1}
s["klaue"] = {"deckung":0.5,"ausweichen":1,"verstecken":0,"heiltrank":1}
s["schlafen"] = {"deckung":0,"ausweichen":0,"verstecken":0,"heiltrank":0}
s["eilegen"] = {"deckung":0,"ausweichen":0,"verstecken":0,"heiltrank":0}
#Variablen
b = "Enderdragon"
bhp = 100
shp = 50
schaden = 10
maxschaden = 15
runde = 0
chance = 0.2
ei = False
deckung = False
ausweichen = False
verstecken = False
drachenaktion = ["feuer",
                 "klaue",
                 "biss",
                 "schlafen",
                 "eilegen"]
#Menü
menuA = ["Spiel beenden",
        "Normaler Angriff",
        "Ultimativer Angriff",]
         
         
menuD = ["Spiel beenden",
        "deckung",
        "ausweichen",
        "verstecken",
        "heiltrank",]
       
while bhp > 0 and shp > 0:
    runde = runde + 1
    print("Autsch!!",b,"hat noch",bhp,"Leben übrig!")
    print("Boss:"+"۞" * int(bhp))
    while True:
        for x in menuA:
            print(menuA.index(x),x)
        x = input("Gib hier die Befehle ein!   :")
        print()
        if x <"0" or x > "6" or len(x)>1:
            print("FALSCHE EINGABE!!!")
            continue
        else:
            print("Super")
            break
    if x == "0":
        break
    elif x == "1":
        schaden = random.randint(0,maxschaden)
        print("Goblin greift an! Runde:",runde)
        print(b,"erleidet",schaden,"Schaden")
        bhp = bhp-schaden
        print("Boss:"+"۞" * int(bhp))

    elif x == "2":
        print ("Du versuchst den Ultimativen Angriff")
        treffer = random.random()
        if treffer < chance:
            print("Hurra!! Ultimativer treffer geglückt")
            schaden = maxschaden*2
            print(b,"erleidet",schaden,"Schaden")
            bhp = bhp-schaden
        else:
            print("Oh Fehlschlag")
    #Drache Schlägt Zurück
    deckung = False
    ausweichen = False
    verstecken = False
    while True:
        for x in menuD:
            print(menuD.index(x),x)
        x = input("Gib hier die Befehle ein!   :")
        print()
        if x <"0" or x > "6" or len(x)>1:
            print("FALSCHE EINGABE!!!")
            continue
        else:
            print("Super")
            break
    if x == "0":
        break
    
    elif x == "4":
        print("Du hast den Heiltrank getrunken")
        shp = shp + random.randint(15,25)
        print("du hast jetzt",shp,"hitpoints")
        print("♥" * int(shp))

    elif x == "1":
        deckung = True
    elif x == "2":
        ausweichen = True
    elif x == "3":
        verstecken = True
#Drachenaktionen
    aktion = random.choice(drachenaktion)
    if aktion == "feuer":
        print("Der Drache spuckt Feuer")
    elif aktion == "klaue":
        print("Der Drache kratzt zurück")
    elif aktion == "biss":
        print("der drache Beißt")
    elif aktion == "schlafen":
        print("der drache schläft")
#Schadensberechnung
    schaden = s[aktion][menuD[int(x)]] * random.randint(5,10)
    shp = shp - schaden
    print("Du erleidest",schaden,"Schaden")
    print("Du hast noch",shp,"Leben")
    print("♥" * int(shp))

    
    
    
    
    
    
    
        
        
    
        
        
    
    
    
    
        
        

    
    
    
    
