import pygame

class Card:
    def __init__(self, url, screen):
        self.surface = pygame.image.load(url)
        surface_size = self.surface.get_size()
        size = screen.get_size()
        self.pos = ((size[0]-surface_size[0])/2, 3*(size[1]-surface_size[1])/4)

    def render(self, surface):
        pass
    def done(self):
        self.pos[0] += 1


class ClickCard(Card):
    def __init__(self, screen):
        super().__init__("res/slicecardtest.png", screen)
    def render(self, screen):
        screen.blit(self.surface, self.pos)
