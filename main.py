import pygame
import card
import state
import eventhandler

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CardGame")
clock = pygame.time.Clock()

eventHandler = eventhandler.Eventhandler()
states = [state.MenuState(screen, eventHandler), state.GameState(screen, eventHandler)]
currentState = states[0]
background = pygame.image.load("res/gdbackground4.png")


def tick():
    global currentState

    currentState = currentState.tick(states)
    eventHandler.tick()

def render():
    screen.blit(background, (0, 0))
    currentState.render()

while True:
    tick()
    render()

    pygame.display.update()
    clock.tick(60)
