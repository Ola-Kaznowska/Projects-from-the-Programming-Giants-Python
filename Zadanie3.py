# Napisz funkcję, która otrzymuje liczbę całkowitą a zwraca sumę jej cyfr.
# Dla liczby 249 otrzymujemy 2+4+9 czyli 15


def suma(liczba):
    #249%10 = 9
    #24%10 = 4
    wynik = 0
    
    for i in str(liczba):
        wynik += int(i)  
        pass
    return wynik
print(suma(125))
        
    