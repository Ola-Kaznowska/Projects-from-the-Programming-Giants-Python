import pygame



pygame.init()


win = pygame.display.set_mode((500, 500))


pygame.display.set_mode("Pierwsza gra Oli")


run = True
# pętla główna
while run:
    # obsługa zdarzeń 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False