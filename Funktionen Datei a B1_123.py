# Grundsätzlich die Definition der Funktion
def stern():
   print("-----------------")
   print("*** Trennung ****")
   print("-----------------")

# Programm
x = 12
y = 5

stern() # 1. Aufruf
print("x =", x, ", y =", y)

stern() # 2. Aufruf
print("x + y =", x + y)

stern() # 3. Aufruf
print("x - y =", x - y)

stern() # 4. Aufruf


#----------------------------------------------------------------|||


# Definition der Funktion   >>>
def quadrat(x):
    q = x*x
    print(f"Zahl: {x}, Quadrat: {q}")

# Programm
quadrat(4.5)
a = 3
quadrat(a)
quadrat(2*a)

for i in 5.0, 6.0:
    quadrat(i)

#----------------------------------------------------------------|||


# Definition der Funktion
def berechnung(x,y,z):
   ergebnis = (x+y) * z
   print("Ergebnis:", ergebnis)
# Programm
berechnung(2,3,5)
berechnung(5,2,3)


#----------------------------------------------------------------|||


# Definition Funktion, Rückgabe der Werte mehrmals  >>>

def multi_print(name, count):
  for i in range(0, count):
    print(name)
multi_print("Hallo!", 5)

#----------------------------------------------------------------|||


# Funktionen mit Rückgabewert
# Definition der Funktion

def mittelwert(x,y):
   ergebnis = (x+y) / 2
   return ergebnis

# Programm
c = mittelwert(3, 9)
print("Mittelwert:", c)

x = 99
print("Mittelwert:", mittelwert(x,4))

y = -5.1
z = 2.8
print(f"Mittelwert: {mittelwert(y,z)}")

#----------------------------------------------------------------|||

# Typhinweise
# Es folgt ein Programm mit Typhinweisen: >>>

a:int = 42
b:float = 42.5
c:str = "Hallo"
d:bool = True
print("Variablen:", a, b, c, d)

def mittelwert(x:float, y:float) -> float:
   ergebnis = (x+y) / 2
   return ergebnis

print("Mittelwert:", mittelwert(3.4, 9.4))






#----------------------------------------------------------------|||


# Funktion Steuerbrechnung  >>>

def steuer(gehalt):
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18
    print(f"Gehalt: {gehalt} Euro, Steuer: {steuerbetrag} Euro")
    
# Programm
for i in 1800, 2200, 2500, 2900:
    steuer(i)


#----------------------------------------------------------------|||



# Am Ende einer Funktion findest du oft eine return-Anweisung. 
# Hinter diesem Schlüsselwort steht der sogenannte Rückgabewert
# der Funktion.  >>>

def return_element(name):
  return name
print(return_element("Hi"))

def summe(a,b,c):
   s = a + b + c
   return s

x = summe(3, 1, 2)

print(x) 

#----------------------------------------------------------------|||


# In Python kannst du auch mehrere Objekte gleichzeitig zurückgeben. >>>

def summe_produkt(a,b,c):
   summe = a + b + c
   produkt = a * b * c
   return summe, produkt

x, y = summe_produkt(3, -1, 2)

print(x, y) 


#----------------------------------------------------------------|||

# Aufgabe Celsius zu Fahrenheit

def celsius_zu_fahrenheit(x):
   return x * 9/5 + 32

print(celsius_zu_fahrenheit(100))




