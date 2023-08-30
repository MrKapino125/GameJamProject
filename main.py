import pygame
import card
import state
import eventhandler
import time

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CardGame")
clock = pygame.time.Clock()

eventHandler = eventhandler.Eventhandler()
states = [state.MenuState(screen, eventHandler), state.GameState(screen, eventHandler), state.EndState(screen, eventHandler)]
currentState = states[0]
background = pygame.image.load("res/gdbackground4.png")

counter = 0
start = time.time()

def tick():
    global currentState
    global counter
    global start

    currentState = currentState.tick(states)
    eventHandler.tick()

    counter += 1
    deltatime = time.time()
    if deltatime - start >= 1:
        print("Fps", counter)
        start = time.time()
        counter = 0

def render():
    screen.blit(background, (0, 0))
    currentState.render()

while True:
    tick()
    render()

    pygame.display.update()
    clock.tick(60)
