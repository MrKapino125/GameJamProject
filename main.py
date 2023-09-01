import pygame
import card
import state
import eventhandler
import time
import timer

pygame.init()
pygame.font.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CardGame")
clock = pygame.time.Clock()
eventHandler = eventhandler.Eventhandler()
background = pygame.image.load("res/gdbackground4.png")

states = None
currentState = None


def init():
    global states
    global currentState

    states = [state.MenuState(screen, eventHandler), state.GameState(screen, eventHandler),
              state.EndState(screen, eventHandler)]
    currentState = states[0]


def tick():
    global currentState

    currentState = currentState.tick(states)
    eventHandler.tick()
def render():
    screen.blit(background, (0, 0))
    currentState.render()

init()
while True:
    if eventHandler.is_pressed["r"] and not eventHandler.is_lockedp["r"]:
        eventHandler.is_lockedp["r"] = True
        init()

    if not eventHandler.is_pressed["r"]:
        eventHandler.is_lockedp["r"] = False

    tick()
    render()

    pygame.display.update()
    clock.tick(60)
