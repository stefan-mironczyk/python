 # Das Programm ist alles andere als eine gute Passwortabfrage und soll nur das Prinzip einer if-Abfrage aufzeigen. 
# Der Code innerhalb des Blocks (der eingerückte Code) wird dann und nur dann ausgeführt, 
# wenn der Ausdruck nach dem Schlüsselwort if zu True ausgewertet wird.

print("Bitte Passwort eingeben.")
passwort = input()
if passwort == "4544":
    print("Du solltest definitiv ein anderes Passwort nutzen.")
print("Login erfolgreich!")


# Es folgt eine Modifizierung des Codes so, dass die Ausgabe „Du solltest definitiv ein anderes Passwort nutzen.“ 
# immer dann getätigt wird, wenn ein anderes Passwort als „123“ vom Nutzer eingegeben wird.

print("Bitte Passwort eingeben.")
passwort = input()
if passwort == "123":
    print("Du solltest definitiv ein anderes Passwort nutzen.")
else:
    print("Na immerhin ist dein Passwort nicht 123.")
print("Login erfolgreich!")

# Schauen wir uns den Code noch einmal Zeile für Zeile an:

#print(„Bitte Passwort eingeben.“)
##Gibt den Text „Bitte Passwort eingeben.“ auf dem Bildschirm aus.

#passwort=input()
#Das Programm wartet auf eine Eingabe des Nutzers und speichert diese in der Variable passwort.

#if passwort==„123“:
#Wenn die Eingabe des Nutzers gleich  „123“ ist, wird der folgende Block abgearbeitet.

#print(„Du solltest definitiv ein anderes Passwort nutzen.“)
#Der Text „Du solltest definitiv ein anderes Passwort nutzen.“ wird auf dem Bildschirm ausgegeben.

#else:
#Wenn die Eingabe des Nutzers nicht gleich „123“ ist, wird der folgende Block abgearbeitet.

#print(„Na immerhin ist dein Passwort nicht 123.“ )
#Der Text „Na immerhin ist dein Passwort nicht 123.“ wird auf dem Bildschirm ausgegeben.

#print(„Login erfolgreich!“)
#Der Text "Login erfolgreich!" wird auf dem Bildschirm ausgegeben.


 
# Es folgt eine weitere Modifizierung des Codes 

print("Bitte Passwort eingeben.")
passwort = input()
if passwort == "123":
    print("Du solltest definitiv ein anderes Passwort nutzen.")
elif passwort == "password":
    print("Dein Passwort war zwischen 2013-2020 das zweitbeliebteste Passwort der Welt!")
elif passwort == "123456":
    print("Dein Passwort war zwischen 2013-2020 das beliebteste Passwort der Welt!")
else:
    print("Dein Passwort ist nicht unter den zwei beliebtesten Passwörtern der Welt!")
print("Login erfolgreich!")

# Was passiert in diesem Programm?
# - Ausgabe „Bitte Passwort eingeben“ und warten auf Eingabe
# - Auswertung Abfrage 1 (==„123“), falls True: Ausgabe Text
# - Auswertung Abfrage 2 (==„password“), falls True: Ausgabe Text
# - Auswertung Abfrage 3 (==„123456“), falls True: Ausgabe Text
# - Falls Abfragen 1 bis 3 False: Ausgabe Text
# - Ausgabe Text



# Es folgt eine weitere Modifizierung des Codes 
# Eine Bedingung kann zusätzlich mit Hilfe von logischen Operatoren erweitert werden, 
# wenn man beispielsweise Anforderungen an die Länge eines Passworts stellen möchte, 
# dazu folgendes Beispiel:

print("Bitte Passwort eingeben.")
passwort = input()
if passwort == "password":
    print("Dein Passwort war zwischen 2013-2020 das beliebteste Passwort der Welt!")
elif passwort != "123456" and len(passwort) > 8:
    print("Herzlichen Glückwunsch! Dein Passwort ist länger als acht Zeichen und nicht das beliebteste der Welt!")
else:
    print("Du solltest die Wahl deines Passworts überdenken.")
print("Login erfolgreich!")

