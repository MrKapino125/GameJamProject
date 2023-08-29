import pygame
import card
import state
import eventhandler

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
surface1 = pygame.Surface((150, 150))
surface1.fill("Red")
#surface1.set_alpha(100)
surface2 = pygame.Surface((150, 150))
surface2.fill("Blue")
surface3 = pygame.Surface((150, 150))
surface3.fill("Yellow")
surface4 = pygame.Surface((150, 150))
surface4.fill("Green")
clickcard = card.ClickCard(screen)

cards = [clickcard]
states = [state.MenuState(screen), state.GameState()]
currentState = states[0]
eventHandler = eventhandler.Eventhandler()


def tick():
    global currentState

    currentState = currentState.tick(eventHandler, states)
    eventHandler.tick()

def render(screen):
    background = pygame.Surface((1600, 900))
    background.fill((213,205,237))
    screen.blit(background, (0, 0))
    #pygame.draw.circle(screen, "Red", (600, 750), 50)
    #screen.blit(surface2, (250, 50))
    #screen.blit(surface3, (50, 250))
    #screen.blit(surface4, (250, 250))

    #cards[0].render(screen) #cards farbe: (249,235,204)
    currentState.render(screen)

while True:
    tick()
    render(screen)

    pygame.display.update()
    clock.tick(60)