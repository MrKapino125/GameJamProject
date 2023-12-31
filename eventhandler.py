import pygame
from sys import exit

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
                           "shift": False,
                           "strg": False,
                           "back": False
                           }
        self.is_clicked = {"left": False,
                           "right": False,
                           "middle": False}
        self.is_lockedc = self.is_clicked.copy()
        self.is_lockedp = self.is_pressed.copy()
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                uni = event.key
                if uni == 1073742049:
                    self.is_pressed["shift"] = True
                if uni == 1073742048:
                    self.is_pressed["strg"] = True
                if uni == 8:
                    self.is_pressed["back"] = True
                if 122 >= uni >= 97 or 48 <= uni <= 57:
                    self.is_pressed[chr(uni)] = True

            if event.type == pygame.KEYUP:
                uni = event.key
                if uni == 1073742049:
                    self.is_pressed["shift"] = False
                if uni == 1073742048:
                    self.is_pressed["strg"] = False
                if uni == 8:
                    self.is_pressed["back"] = False
                if 122 >= uni >= 97 or 48 <= uni <= 57:
                    self.is_pressed[chr(uni)] = False

            if event.type == pygame.MOUSEMOTION:
                self.mousePos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.is_clicked["left"] = True
                if event.button == 2:
                    self.is_clicked["middle"] = True
                if event.button == 3:
                    self.is_clicked["right"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_clicked["left"] = False
                if event.button == 2:
                    self.is_clicked["middle"] = False
                if event.button == 3:
                    self.is_clicked["right"] = False