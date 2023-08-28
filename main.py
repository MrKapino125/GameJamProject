import pygame
import card
import state
import eventhandler
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
clickcard = card.ClickCard(screen)

cards = [clickcard]
states = [state.MenuState(), state.GameState()]
currentState = states[0]
eventHandler = eventhandler.Eventhandler()


def tick():
    global currentState

    currentState = currentState.tick(eventHandler, states)
    eventHandler.tick()

def render(screen):
    #screen.blit(surface1, (50, 50))
    #screen.blit(surface2, (250, 50))
    #screen.blit(surface3, (50, 250))
    #screen.blit(surface4, (250, 250))

    #cards[0].render(screen)
    currentState.render(screen)

while True:
    tick()
    render(screen)

    pygame.display.update()
    clock.tick(60)