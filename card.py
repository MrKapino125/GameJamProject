import pygame

class Card:
    def render(self, surface):
        pass

class clickCard(Card):
    def render(self, screen):
        size = screen.get_size()
        surface = pygame.image.load("res/slicecardtest.png")
        surface_size = surface.get_size()
        screen.blit(surface, ((size[0]-surface_size[0])/2, 3*(size[1]-surface_size[1])/4))
