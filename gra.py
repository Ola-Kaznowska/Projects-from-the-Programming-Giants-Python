# 9. Napisz program aplikacji graficznej, która co 3 sekundy zmienia kolor tła. Nowy
# kolor tła powinien być losowany.
# Pamiętaj o wykorzystaniu liczby klatek do wykrycia kiedy mijają kolejne 3 sekundy
# Pamiętaj o budowaniu koloru RGB:
# RGB składa się z trzech kolorów, każdy może przyjąć wartość od 0 do 255 (włącznie)
# RGB = [R, G, B] możesz przechowywać to jako listę

# 10.Dodaj do swojego wykrywanie naciśnięcia klawisza 'b'.
# Jeśli taki klawisz zostanie naciśnięty kolor tła powinien zmienić się na czarn

import pygame
from random import randint
from time import sleep
pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My game")

background_color = [randint(0,255),randint(0,255),randint(0,255)]

game_status = True

fps_counter = 0

black = False

while game_status:
    fps_counter += 1

    events = pygame.event.get()

    for event in events:
        print(event)

        if event.type == pygame.QUIT:
            game_status = False
        pass

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_b]:
        black = True
        screen_surface.fill([0,0,0])
    
    if fps_counter % 60 * 3 == 0 and not black:
        background_color = [randint(0,255),randint(0,255),randint(0,255)]
        screen_surface.fill(background_color)


    pygame.display.update()
    clock.tick(60)
    pass

pygame.quit()
quit()