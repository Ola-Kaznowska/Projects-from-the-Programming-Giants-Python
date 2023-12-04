# Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
# występować powtórzenia, a zwraca listę unikalnych elementów.
# Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]

# Należy zaprezentować instrukcję in: elem in lista





def dane(lista: list) -> list:
    wynik = []
    
    for i in lista:
        
        if i not in wynik:
            wynik.append(i)
            pass
            continue
        pass
    return wynik
    print(wynik)
dane([5])