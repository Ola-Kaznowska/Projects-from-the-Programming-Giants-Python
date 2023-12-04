import random as rd  

def losowe(rozmiar, minimum = 0, maximum = 100):
    wynik = []
    for i in range(rozmiar):
        i = rd.randint(minimum, maximum)
        wynik.append(i)
    return wynik
print(losowe(100))