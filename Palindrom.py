def czy_palindrom(wyraz):
    while " " in wyraz:
        wyraz.remove(" ")
    if wyraz == wyraz[::-1]:
        return True
    else:
        return False