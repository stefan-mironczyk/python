print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())

if gehalt > 2500:
    steuerbetrag = gehalt * 0.42
else:
    steuerbetrag = gehalt * 0.18

print(f"Es ergibt sich eine Steuer von {steuerbetrag} Euro")


# Es folgt eine Modifizierung des Codes so die Berechnung der Steuer weiter verändert werden kann und um einen Steuersatz erweitert läuft
# Gehalt Steuersatz
# # mehr als 4.000 Euro 26 %
# 2.500 bis 4.000 Euro 22 %
# weniger als 2.500 Euro 18 %
 

print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())

if gehalt > 4000:
    steuerbetrag = gehalt * 0.26
elif gehalt < 2500:
    steuerbetrag = gehalt * 0.18
else:
    steuerbetrag = gehalt * 0.22

print(f"Es ergibt sich eine Steuer von {steuerbetrag} Euro")


# S.48 o S.58