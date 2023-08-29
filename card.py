import pygame

class Card:
    def __init__(self, url, screen):
        self.surface = pygame.image.load(url)
        self.surface_size = self.surface.get_size()
        self.size = screen.get_size()
        self.pos = ((self.size[0]-self.surface_size[0])/2, 3*(self.size[1]-self.surface_size[1])/4)

    def tick(self):
        pass
    def render(self, surface):
        pass
    def done(self):
        self.pos[0] += 1


class ClickCard(Card):
    def __init__(self, screen):
        super().__init__("res/cardblack.png", screen)
    def render(self, screen):
        screen.blit(self.surface, self.pos)
    def tick(self, eventHandler):
        if eventHandler.is_clicked["left"] and not eventHandler.is_lockedc["left"]:
            eventHandler.is_lockedc["left"] = True

            mousePos = eventHandler.mousePos
            if mousePos[0] > self.pos[0] and mousePos[0] < self.pos[0] + self.surface_size[0] and mousePos[1] > self.pos[1] and mousePos[1] < self.pos[1] + self.surface_size[1]:
                print("YOU WIN")
        if not eventHandler.is_clicked["left"]:
            eventHandler.is_lockedc["left"] = False
