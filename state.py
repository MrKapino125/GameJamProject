import pygame
import math

class State:
    def __init__(self):
        self.s_lock = False
        self.left_lock = False
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
        if eventHandler.is_pressed["s"] and not self.s_lock:
            self.s_lock = True
        if not eventHandler.is_pressed["s"]:
            self.s_lock = False
        if eventHandler.is_pressed["a"]:
            return states[1]

        if eventHandler.is_clicked["left"] and not self.left_lock:
            mousePos = eventHandler.mousePos
            width = self.screen.get_width()
            height = self.screen.get_height()
            if math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 3.5 * width / 10)**2) < self.green_size:
                self.green_size = 65
                self.yellow_size = 50
                self.red_size = 50
            elif math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 5 * width / 10)**2) < self.yellow_size:
                self.green_size = 50
                self.yellow_size = 65
                self.red_size = 50
            if math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 6.5 * width / 10)**2) < self.red_size:
                self.green_size = 50
                self.yellow_size = 50
                self.red_size = 65
            play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
            if mousePos[0] > play_pos[0] and mousePos[0] < play_pos[0] + self.play_width and mousePos[1] > play_pos[1] and mousePos[1] < play_pos[1] + self.play_height:
                return states[1]
            self.left_lock = True
        if not eventHandler.is_clicked["left"]:
            self.left_lock = False

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
    def __init__(self):
        super().__init__()
        self.card = pygame.image.load("res/card_prototype.png")

    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["s"] and not self.s_lock:
            self.s_lock = True
        if not eventHandler.is_pressed["s"]:
            self.s_lock = False
        if eventHandler.is_pressed["d"]:
            return states[0]
        return self
    def render(self, screen):
        pass
        #screen.blit(self.card, (screen.get_width()/2 - self.card.get_width()/2, screen.get_height()/2 - self.card.get_height()/4))
        #surface = pygame.Surface((1100, 550))
        #surface.fill("Red")
        #screen.blit(surface, ((screen.get_width() / 2 - 1100 / 2, screen.get_height() / 2 - 550 / 3)))