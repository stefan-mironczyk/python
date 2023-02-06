#Beispiel: Berechnung der pythagoräischen Zahlen

#Das folgende Programm berechnet alle pythagoräischen Zahlen bis zu einer einzugebenden maximalen Zahl:

from math import sqrt
n = int(input("Maximale Zahl? "))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)


#z.B.
            
"""Bsp: Maximale Zahl? 10
3 4 5
6 8 10"""
