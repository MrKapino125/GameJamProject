import pygame
import card
import state
import eventhandler
import time
import timer
import cardloader
import soundloader

pygame.init()
pygame.font.init()
pygame.mixer.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chaotic Cards")
clock = pygame.time.Clock()
eventHandler = eventhandler.Eventhandler()
background = pygame.image.load("res/gdbackground4compri.jpg")
timer = timer.Timer()
cardLoader = cardloader.Cardloader()
soundLoader = soundloader.Soundloader()
soundLoader.play()

states = None
currentState = None
reset_lock = False


def init():
    global states
    global currentState

    states = [state.MenuState(screen, eventHandler, timer, cardLoader, soundLoader), state.GameState(screen, eventHandler, timer, cardLoader, soundLoader),
              state.EndState(screen, eventHandler, timer, cardLoader, soundLoader)]
    currentState = states[0]


def reset(full=False):
    global currentState
    if full:
        return init()
    init()
    currentState = states[1]

def tick():
    global currentState

    currentState = currentState.tick(states)
    eventHandler.tick()
def render():
    screen.blit(background, (0, 0))
    currentState.render()

init()
while True:
    if eventHandler.is_pressed["r"] and not reset_lock:
        reset_lock = True
        if eventHandler.is_pressed["shift"]:
            reset()
        if eventHandler.is_pressed["strg"]:
            reset(True)

    if not eventHandler.is_pressed["r"]:
        reset_lock = False

    tick()
    render()

    pygame.display.update()
    clock.tick(60)
