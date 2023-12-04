# Napisz funkcję, która przyjmuje następujące argumenty: imie (str), wiek (int), wzrost_m
# (float), a zwraca napis: “Jan, lat 20, 1.75 m wzrostu” - oczywiście argumenty należy
# podstawić do szablonu.



def dane(imie: str, wiek: int, wzrost: float) -> str:
    
   #return imie + ", lat" + str(wiek) + ", " + str(wzrost) + " m wzrost"
    return f"{imie}, lat {wiek}, {wzrost:.2f} m wzrostu"


print(dane("a",2,2))
   