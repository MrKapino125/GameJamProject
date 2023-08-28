import pygame

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
        self.red_size = 50
        self.yellow_size = 50
        self.green_size = 65
    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["s"] and not self.s_lock:
            print("eichel")
            self.s_lock = True
        if not eventHandler.is_pressed["s"]:
            self.s_lock = False
        if eventHandler.is_pressed["a"]:
            return states[1]

        if eventHandler.is_clicked["left"] and not self.left_lock:
            mousePos = eventHandler.mousePos
            width = self.screen.get_width()
            print(abs((mousePos[1] - 750) / (mousePos[0] - 3.5 * width / 10)))
            print(mousePos)
            if abs((mousePos[1] - 750) / (mousePos[0] - 3.5 * width / 10)) < self.green_size:
                self.green_size = 65
                self.yellow_size = 50
                self.red_size = 50
            elif abs((mousePos[1] - 750) / (mousePos[0] - 5 * width / 10)) < self.yellow_size:
                self.green_size = 50
                self.yellow_size = 65
                self.red_size = 50
            if abs((mousePos[1] - 750) / (mousePos[0] - 6.5 * width / 10)) < self.red_size:
                self.green_size = 50
                self.yellow_size = 50
                self.red_size = 65
            self.left_lock = True
        if not eventHandler.is_clicked["left"]:
            self.left_lock = False

        return self
    def render(self, screen):
        width = screen.get_width()
        pygame.draw.circle(screen, "Yellow", (width / 2, 750), self.yellow_size)
        pygame.draw.circle(screen, "Green", (3.5 * width / 10, 750), self.green_size)
        pygame.draw.circle(screen, "Red", (6.5 * width / 10, 750), self.red_size)

class GameState(State):
    def __init__(self):
        super().__init__()

    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["s"] and not self.s_lock:
            print("vulva")
            self.s_lock = True
        if not eventHandler.is_pressed["s"]:
            self.s_lock = False
        if eventHandler.is_pressed["d"]:
            return states[0]
        return self
    def render(self, screen):
        pass