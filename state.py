import pygame
import math
import card

class State:
    def __init__(self, screen, eventHandler):
        self.screen = screen
        self.eventHandler = eventHandler
    def tick(self, eventHandler, states):
        pass
    def render(self, screen):
        pass


class MenuState(State):
    def __init__(self, screen, eventHandler):
        super().__init__(screen, eventHandler)
        self.play_button = pygame.image.load("res/play_button.png")

        self.red_size = 50
        self.yellow_size = 50
        self.green_size = 65
        self.play_width = 750
        self.play_height = 150
    def tick(self, states):
        if self.eventHandler.is_pressed["s"] and not self.eventHandler.is_lockedp["s"]:
            self.eventHandler.is_lockedp["s"] = True
        if not self.eventHandler.is_pressed["s"]:
            self.eventHandler.is_lockedp["s"] = False
        if self.eventHandler.is_pressed["a"]:
            return states[1]

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
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
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        return self
    def render(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        pygame.draw.circle(self.screen, (236, 193, 94), (width / 2, 750), self.yellow_size + 10)
        pygame.draw.circle(self.screen, "Yellow", (width / 2, 750), self.yellow_size)
        pygame.draw.circle(self.screen, (236, 193, 94), (3.5 * width / 10, 750), self.green_size + 10)
        pygame.draw.circle(self.screen, "Green", (3.5 * width / 10, 750), self.green_size)
        pygame.draw.circle(self.screen, (236, 193, 94), (6.5 * width / 10, 750), self.red_size + 10)
        pygame.draw.circle(self.screen, "Red", (6.5 * width / 10, 750), self.red_size)

        play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
        #pygame.draw.polygon(play_button, "Green", [(100, 75), (100, 225), (200, 150)])
        self.screen.blit(self.play_button, (play_pos))

class GameState(State):
    def __init__(self, screen, eventHandler):
        super().__init__(screen, eventHandler)
        self.cardtest = card.ClickCard(screen, eventHandler)
        self.interface = pygame.image.load("res/interface.png")

    def tick(self, states):
        if self.eventHandler.is_pressed["d"]:
            return states[0]
        self.cardtest.tick()
        return self
    def render(self):
        self.screen.blit(self.interface, (250, 37.5/2))
        self.cardtest.render()