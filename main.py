import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 800))
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
surface5 = pygame.image.load("res/matthias_pb.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface1, (50, 50))
    screen.blit(surface2, (250, 50))
    screen.blit(surface3, (50, 250))
    screen.blit(surface4, (250, 250))
    screen.blit(surface5, (0, 0))

    pygame.display.update()
    clock.tick(60)