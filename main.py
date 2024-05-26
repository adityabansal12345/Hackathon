# import pygame as py
# import random as rd
# import time as tm


# flashcards = {1: 2,
#        3: 4,
#        5: 6,
#        7: 8,
#        9: 10,
#        11: 12,
#        13: 14,
#        15: 16,
#        17: 18,
#        19: 20,
#        21: 22,
#        }
# print(dict[1])

# print(rd.randint(1,10))

import time
import pygame

background_color = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Flashcard')
screen.fill(background_color)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False