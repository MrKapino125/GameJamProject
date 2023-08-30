import pygame

class Card:
    def __init__(self, url, screen, eventHandler):
        self.surface = pygame.image.load(url)
        self.surface_size = self.surface.get_size()
        self.size = screen.get_size()
        self.pos = [(self.size[0]-self.surface_size[0])/2, 5*(self.size[1]-self.surface_size[1])/6]
        self.screen = screen
        self.eventHandler = eventHandler
        self.win = False
        self.end = False
        self.counter = 0

    def tick(self):
        if self.win:
            self.counter += 1
            self.pos[0] += 1350 / 6
            if self.counter == 6:
                self.counter = 0
                self.win = False

    def render(self):
        pass
    def done(self):
        self.win = True
        self.end = True


class ClickCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/click_card.png", screen, eventHandler)
    def render(self):
        self.screen.blit(self.surface, self.pos)
    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if mousePos[0] > self.pos[0] and mousePos[0] < self.pos[0] + self.surface_size[0] and mousePos[1] > self.pos[1] and mousePos[1] < self.pos[1] + self.surface_size[1]:
                self.done()
                return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

class SliceCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/slice_card.png", screen, eventHandler)
        self.state = None
        self.clicked = False

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.clicked = True
            mousePos = self.eventHandler.mousePos
            if self.state is None:
                if mousePos[0] >= 676 and mousePos[0] <= 1000 and mousePos[1] <= 360:
                    self.state = "starting"
            if self.state == "starting":
                if mousePos[0] >= 676 and mousePos[0] <= 1000 and mousePos[1] >= 360 and mousePos[1] <= 783:
                    self.state = "going"
            if self.state == "going":
                if mousePos[0] >= 676 and mousePos[0] <= 1000 and mousePos[1] <= 360:
                    self.state = "starting"
                if mousePos[0] >= 676 and mousePos[0] <= 1000 and mousePos[1] >= 783:
                    self.done()
                    return True
            if mousePos[0] < 676 or mousePos[0] > 1000:
                self.state = None
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
            self.state = None
            if self.clicked:
                self.clicked = False
                return False
    def render(self):
        self.screen.blit(self.surface, self.pos)
