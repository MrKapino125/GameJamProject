import pygame
import card
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
surface1 = pygame.Surface((150, 150))
surface1.fill("Red")
surface2 = pygame.Surface((150, 150))
surface2.fill("Blue")
surface3 = pygame.Surface((150, 150))
surface3.fill("Yellow")
surface4 = pygame.Surface((150, 150))
surface4.fill("Green")
clickcard = card.clickCard()

cards = [clickcard]

def tick():
    pass

def render(screen):
    screen.blit(surface1, (50, 50))
    screen.blit(surface2, (250, 50))
    screen.blit(surface3, (50, 250))
    screen.blit(surface4, (250, 250))

    cards[0].render(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tick()
    render(screen)

    pygame.display.update()
    clock.tick(60)