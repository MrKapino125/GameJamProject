import pygame


class Eventhandler:
    def __init__(self):
        self.mousePos = (0,0)
        self.is_pressed = {"a": False,
                           "b": False,
                           "c": False,
                           "d": False,
                           "e": False,
                           "f": False,
                           "g": False,
                           "h": False,
                           "i": False,
                           "j": False,
                           "k": False,
                           "l": False,
                           "m": False,
                           "n": False,
                           "o": False,
                           "p": False,
                           "q": False,
                           "r": False,
                           "s": False,
                           "t": False,
                           "u": False,
                           "v": False,
                           "w": False,
                           "x": False,
                           "y": False,
                           "z": False,
                           "1": False,
                           "2": False,
                           "3": False,
                           "4": False,
                           "5": False,
                           "6": False,
                           "7": False,
                           "8": False,
                           "9": False,
                           "0": False,
                           }
        self.is_clicked = {"left": False,
                           "right": False,
                           "middle": False}
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                uni = event.key
                if (uni > 122 or uni < 97) and (uni < 48 or uni > 57):
                    break
                self.is_pressed[chr(uni)] = True
            if event.type == pygame.KEYUP:
                uni = event.key
                if (uni > 122 or uni < 97) and (uni < 48 or uni > 57):
                    break
                self.is_pressed[chr(uni)] = False

            if event.type == pygame.MOUSEMOTION:
                self.mousePos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.is_clicked["left"]
                if event.button == 2:
                    self.is_clicked["middle"]
                if event.button == 3:
                    self.is_clicked["right"]