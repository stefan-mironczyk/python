

# B.8.2 Variable Parameter


# einen Stern (*) = Tupel

def ein_stern(x, *y, z):
  print(x, y, z)

ein_stern(1, 2, 3, 4, 5, z=6) 


# zwei Sterne (**) = Dictionary

def zwei_sterne(x, **y):
  print(x, y)

zwei_sterne(1, a=2, b=3, c=4, d=5)



# Argumente als Liste oder Dictionaries gesammelt übergeben

def zwei_parameter(x, y):
  print(x, y)

liste = [1, 2]
zwei_parameter(*liste) 


dictionary = {"y": 2,"x": 1}
zwei_parameter(**dictionary) 





# B.8.3 Typ-Annotation

def linear(x: int, m: int, b: int) -> int :
    return(m * x + b)

print(linear(1,2,3))            # output: 5

#o.

def optional_funktion(x: str, y: int=0):
    print(x, y)
optional_funktion("maus",6)   # output: maus 6


# zulässige Aufrufe

def sterne_funktion(*x: str, **y: int):
    print(x, y)

sterne_funktion("Ich", "heiße", "Max") # output: ("Ich", "heiße", "Max") {}

sterne_funktion(a=1, b=2)  # output: () {"a" : 1,"b": 2}

sterne_funktion("Ich", "heiße", "Marianne", z=0)  # output: ("ich", "hieße", "Marianne") {z: 0}

sterne_funktion(1, 2, 3, 4, 5, z=6) # output: (1, 2, 3, 4, 5) {z: 6}



def zwei_sterne(x, **y):
   print(x, y)
zwei_sterne(1, a=2, b=3, c=4, d=5) ## output: 1 {"a": 2, "b": 3, "c": 4, "d": 5}



def funktion( x : float ) -> int:
        return str( x )
funktion(7)