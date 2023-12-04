#Napisz funkcję, która otrzyma jeden argument określający liczbę binarną. Funkcja ma
#wyświetlić ile wynosi podana liczba w zapisie dziesiętnym.
"""
liczby dziesiętne
4
5
6

9
10
11


19
20


minuty
9
10


60
1   00

kod binarny
0
1
10
11
100
101
110


Zapis liczb dziesiętnych
1348

8 * (10**0) + 4 * (10**1) + 3 * (10**2) + 1 * (10**3)

Zamiana liczb binarnych na dziesiętne
110
0 * (2**0) + 1 * (2**1) + 1 * (2**3)

1010
"""




def bin_to_dec(liczba):
    
    wynik = 0
    for i in range(len(liczba)):
       wynik += int (liczba [len(liczba) -1 - i]) * 2 ** i
    return wynik
    
    pass

print(bin_to_dec("101"))



def dec_to_bin(liczba):
    wynik = ""
    while liczba > 0:
        if liczba %2:
            wynik = "1" + wynik
            pass
        else:
            
            wynik = "0" + wynik
        liczba = liczba//2
    return wynik

print(dec_to_bin(5))
    
    
pass
    