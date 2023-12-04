from math import sqrt

def prostokat(a: float, b: float):
    obwod = 2 * a + 2 * b
    pole = a * b
    przekatna = sqrt(a**2 + b**2)
    
    
    return obwod, pole, przekatna 

a = prostokat(2,4)[1]

print(a)