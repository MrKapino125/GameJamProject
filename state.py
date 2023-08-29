import pygame
import math
import card

class State:
    def __init__(self):
        pass
    def tick(self, eventHandler, states):
        pass
    def render(self, screen):
        pass


class MenuState(State):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.play_button = pygame.image.load("res/play_button.png")

        self.red_size = 50
        self.yellow_size = 50
        self.green_size = 65
        self.play_width = 750
        self.play_height = 150
    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["s"] and not eventHandler.is_lockedp["s"]:
            eventHandler.is_lockedp["s"] = True
        if not eventHandler.is_pressed["s"]:
            eventHandler.is_lockedp["s"] = False
        if eventHandler.is_pressed["a"]:
            return states[1]

        if eventHandler.is_clicked["left"] and not eventHandler.is_lockedc["left"]:
            eventHandler.is_lockedc["left"] = True

            mousePos = eventHandler.mousePos
            width = self.screen.get_width()
            height = self.screen.get_height()
            if math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 3.5 * width / 10)**2) < self.green_size + 10:
                self.green_size = 65
                self.yellow_size = 50
                self.red_size = 50
            elif math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 5 * width / 10)**2) < self.yellow_size + 10:
                self.green_size = 50
                self.yellow_size = 65
                self.red_size = 50
            if math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 6.5 * width / 10)**2) < self.red_size + 10:
                self.green_size = 50
                self.yellow_size = 50
                self.red_size = 65
            play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
            if mousePos[0] > play_pos[0] and mousePos[0] < play_pos[0] + self.play_width and mousePos[1] > play_pos[1] and mousePos[1] < play_pos[1] + self.play_height:
                return states[1]
        if not eventHandler.is_clicked["left"]:
            eventHandler.is_lockedc["left"] = False

        return self
    def render(self, screen):
        width = screen.get_width()
        height = screen.get_height()

        pygame.draw.circle(screen, (236, 193, 94), (width / 2, 750), self.yellow_size + 10)
        pygame.draw.circle(screen, "Yellow", (width / 2, 750), self.yellow_size)
        pygame.draw.circle(screen, (236, 193, 94), (3.5 * width / 10, 750), self.green_size + 10)
        pygame.draw.circle(screen, "Green", (3.5 * width / 10, 750), self.green_size)
        pygame.draw.circle(screen, (236, 193, 94), (6.5 * width / 10, 750), self.red_size + 10)
        pygame.draw.circle(screen, "Red", (6.5 * width / 10, 750), self.red_size)

        play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
        #pygame.draw.polygon(play_button, "Green", [(100, 75), (100, 225), (200, 150)])
        screen.blit(self.play_button, (play_pos))

class GameState(State):
    def __init__(self, screen):
        super().__init__()
        self.cardtest = card.ClickCard(screen)

    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["d"]:
            return states[0]
        self.cardtest.tick(eventHandler)
        return self
    def render(self, screen):
        self.cardtest.render(screen)