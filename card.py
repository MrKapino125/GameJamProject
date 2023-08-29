import pygame

class Card:
    def __init__(self, url, screen, eventHandler):
        self.surface = pygame.image.load(url)
        self.surface_size = self.surface.get_size()
        self.size = screen.get_size()
        self.pos = ((self.size[0]-self.surface_size[0])/2, 5*(self.size[1]-self.surface_size[1])/6)
        self.screen = screen
        self.eventHandler = eventHandler

    def tick(self):
        pass
    def render(self):
        pass
    def done(self):
        self.pos[0] += 1


class ClickCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/cardblack.png", screen, eventHandler)
    def render(self):
        #surface = pygame.Surface((1100,225))
        #surface.fill("Red")
        self.screen.blit(self.surface, self.pos)
        #self.screen.blit(surface, (250, 37.5/2))
    def tick(self):
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if mousePos[0] > self.pos[0] and mousePos[0] < self.pos[0] + self.surface_size[0] and mousePos[1] > self.pos[1] and mousePos[1] < self.pos[1] + self.surface_size[1]:
                print("YOU WIN")
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

class SliceCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/slicecardtest.png", screen, eventHandler)
        self.state = None

    def tick(self):
        if self.eventHandler.is_clicked["left"]:
            mousePos = self.eventHandler.mousePos
            if self.state is None:
                if mousePos[0] >= 698 and mousePos[0] <= 883 and mousePos[1] <= 318:
                    self.state = "starting"
            if self.state == "starting":
                if mousePos[0] >= 698 and mousePos[0] <= 883 and mousePos[1] >= 318 and mousePos[1] <= 750:
                    self.state = "going"
            if self.state == "going":
                if mousePos[0] >= 698 and mousePos[0] <= 883 and mousePos[1] <= 318:
                    self.state = "starting"
                if mousePos[0] >= 698 and mousePos[0] <= 883 and mousePos[1] >= 750:
                    print("You Win")
            if mousePos[0] < 698 or mousePos[0] > 883:
                self.state = None
        if not self.eventHandler.is_clicked["left"]:
            self.state = None
    def render(self):
        self.screen.blit(self.surface, self.pos)
