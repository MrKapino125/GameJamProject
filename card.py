import math
import random

import pygame

import state


class Card:
    holding = "testtest12"
    def __init__(self, url, screen, eventHandler, timer):
        self.surface = pygame.image.load(url)
        self.surface_size = self.surface.get_size()
        self.size = screen.get_size()
        self.pos = [(self.size[0]-self.surface_size[0])/2, 5*(self.size[1]-self.surface_size[1])/6]
        self.screen = screen
        self.eventHandler = eventHandler
        self.timer = timer
        self.win = False
        self.end = False
        self.counter = 0
        self.numberfont = pygame.font.SysFont("segoescript", 49)
        self.numberfont.set_bold(True)

    def tick(self):
        duration = 0.4 * self.timer.fps
        self.counter += 1
        if self.win:
            self.counter += 1
            self.pos[0] += 1350 / duration
            if self.counter == duration:
                self.counter = 0
                self.win = False

    def render(self, counter):
        self.screen.blit(self.surface, self.pos)
        self.drawNumber(counter)
    def done(self):
        self.win = True
        self.end = True

    def drawNumber(self, counter):
        number = self.numberfont.render(str(counter), True, (255, 236, 177))
        if counter < 10:
            self.screen.blit(number, (self.pos[0] + 30, self.pos[1] + 460))
        else:
            self.screen.blit(number, (self.pos[0] + 10, self.pos[1] + 465))


class ClickCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/click_card.png", screen, eventHandler, timer)
    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if self.pos[0] < mousePos[0] < self.pos[0] + self.surface_size[0] and self.pos[1] < mousePos[1] < self.pos[1] + self.surface_size[1]:
                self.done()
                return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return

class SliceCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/slice_card.png", screen, eventHandler, timer)
        self.started = False
        self.clicked = False

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.clicked = True
            mousePos = self.eventHandler.mousePos
            if not self.started:
                if 676 <= mousePos[0] <= 1000 and mousePos[1] <= 360:
                    self.started = True
            if self.started:
                if 676 <= mousePos[0] <= 1000 and mousePos[1] >= 783:
                    self.done()
                    self.eventHandler.is_lockedc["left"] = True
                    return True
            if mousePos[0] < 676 or mousePos[0] > 1000:
                self.started = False
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
            self.started = False
            if self.clicked:
                self.clicked = False
                return False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return

class MathCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/math_card0.png",
                 "1": "res/math_card1.png",
                 "2": "res/math_card2.png",
                 "3": "res/math_card3.png",
                 "4": "res/math_card4.png",
                 "5": "res/math_card5.png",
                 "6": "res/math_card6.png",}
        self.x = random.randint(0,6)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        match self.x:
            case 0:
                self.answer = 0
            case 1:
                self.answer = 1
            case 2:
                self.answer = 2
            case 3:
                self.answer = 0
            case 4:
                self.answer = 1
            case 5:
                self.answer = 1
            case 6:
                self.answer = 0
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    if self.answer == 0:
                        self.done()
                        return True
                    else:
                        return False
                if 702 <= mousePos[0] <= 876:
                    if self.answer == 1:
                        self.done()
                        return True
                    else:
                        return False
                if 1000 <= mousePos[0] <= 1174:
                    if self.answer == 2:
                        self.done()
                        return True
                    else:
                        return False
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))

class RememberCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/memory_card.png",
                 "1": "res/memory_card.png",
                 "2": "res/memory_card.png",
                 "3": "res/memory_card.png",
                 "4": "res/memory_card.png",
                 "5": "res/memory_card.png",
                 "6": "res/memory_card.png", }
        self.x = random.randint(0, 6)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        self.started = False
        self.sequence = []
        self.inputs = 0
        if self.x in range(7):
            self.answer = [2,2,1,2,3,1,3]
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    self.sequence.append(1)
                    self.started = True
                    self.inputs += 1
                if 702 <= mousePos[0] <= 876:
                    self.sequence.append(2)
                    self.started = True
                    self.inputs += 1
                if 1000 <= mousePos[0] <= 1174:
                    self.sequence.append(3)
                    self.started = True
                    self.inputs += 1

            if self.sequence != self.answer[:self.inputs]:
                self.started = False
                self.inputs = 0
                self.sequence = []
                return False
            if self.sequence == self.answer:
                self.done()
                return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))
        if self.started:
            surface = pygame.Surface((950 - self.inputs*125, 120))
            surface.fill((255,236,177))
            self.screen.blit(surface, (350 + self.inputs*125, 435))

class MinefieldCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/minefield_card.png",
                 "1": "res/minefield_card1.png",
                 "2": "res/minefield_card2.png", }
        self.x = random.randint(0, 2)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        if self.x == 0:
            self.field = [[False, False, True, False, False, True, False],
                          [False, True, False, False, False, True, False],
                          [False, True, False, True, False, False, False],
                          [True, False, False, False, True, False, False],
                          [False, False, True, True, False, False, False],
                          [False, True, False, False, False, True, True],
                          [False, True, False, True, False, False, False]]
        elif self.x == 1:
            self.field = [[True, False, True, False, False, False, False],
                          [False, False, False, True, False, False, False],
                          [False, True, False, False, False, False, True],
                          [False, False, True, False, True, False, False],
                          [False, True, False, True, False, True, False],
                          [False, True, True, False, True, False, False],
                          [False, True, False, False, False, False, False]]
        else:
            self.field = [[False, False, True, False, True, False, False],
                          [False, True, False, False, False, False, True],
                          [False, False, True, False, True, False, False],
                          [False, True, True, False, False, True, False],
                          [True, False, False, False, True, False, False],
                          [False, False, True, True, False, True, False],
                          [False, True, False, False, False, False, False]]
        self.player_pos = [6,0]
        self.font = pygame.font.SysFont("segoescript", 50)
        self.xtxt = self.font.render("x", True, "Red")

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            print(self.eventHandler.mousePos)
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        if self.eventHandler.is_pressed["w"] and not self.eventHandler.is_lockedp["w"]:
            self.eventHandler.is_lockedp["w"] = True
            if self.player_pos[0] > 0:
                self.player_pos[0] -= 1
        elif self.eventHandler.is_pressed["a"] and not self.eventHandler.is_lockedp["a"]:
            self.eventHandler.is_lockedp["a"] = True
            if self.player_pos[1] > 0:
                self.player_pos[1] -= 1
        elif self.eventHandler.is_pressed["s"] and not self.eventHandler.is_lockedp["s"]:
            self.eventHandler.is_lockedp["s"] = True
            if self.player_pos[0] < 6:
                self.player_pos[0] += 1
        elif self.eventHandler.is_pressed["d"] and not self.eventHandler.is_lockedp["d"]:
            self.eventHandler.is_lockedp["d"] = True
            if self.player_pos[1] < 6:
                self.player_pos[1] += 1

        if not self.eventHandler.is_pressed["w"]:
            self.eventHandler.is_lockedp["w"] = False

        if not self.eventHandler.is_pressed["a"]:
            self.eventHandler.is_lockedp["a"] = False

        if not self.eventHandler.is_pressed["s"]:
            self.eventHandler.is_lockedp["s"] = False

        if not self.eventHandler.is_pressed["d"]:
            self.eventHandler.is_lockedp["d"] = False

        if self.field[self.player_pos[0]][self.player_pos[1]]:
            self.field[self.player_pos[0]][self.player_pos[1]] = "x"
            self.player_pos = [6,0]
            return False
        if self.player_pos == [6,2]:
            self.done()
            return True
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        surface = pygame.Surface((35,35))
        surface.fill("Green")
        self.screen.blit(surface, (606 + self.player_pos[1]*50 + 5, 391 + self.player_pos[0]*50 + 7))
        for y in range(7):
            for x in range(7):
                if self.field[y][x] == "x":
                    self.screen.blit(self.xtxt, (606 + x*50 + 5, 391 + y*50 - 17))

class RightCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/right_card.png", screen, eventHandler, timer)
        self.hint_counter = 0
        self.hint = False
        self.stronghint = False
        self.font1 = pygame.font.SysFont("segoescript", 30)
        self.font2 = pygame.font.SysFont("segoescript", 20)
        self.hinttxt = self.font1.render("hint: your mouse!", True, "Red")
        self.stronghinttxt = self.font2.render("right click! -.-", True, "Red")
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            self.hint_counter += 1
            return False
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        if self.eventHandler.is_clicked["right"] and not self.eventHandler.is_lockedc["right"]:
            self.eventHandler.is_lockedc["right"] = True
            self.done()
            return True
        if not self.eventHandler.is_clicked["right"]:
            self.eventHandler.is_lockedc["right"] = False

        if self.hint_counter >= 10:
            self.hint = True
        if self.hint_counter >= 25:
            self.stronghint = True
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    self.screen.blit(self.hover_surface, (403, 628))
                if 702 <= mousePos[0] <= 876:
                    self.screen.blit(self.hover_surface, (702, 628))
                if 1000 <= mousePos[0] <= 1174:
                    self.screen.blit(self.hover_surface, (1000, 628))
        if self.hint:
            self.screen.blit(self.hinttxt, (self.size[0]/2 + 130, self.size[1]/2 + 45))
        if self.stronghint:
            self.screen.blit(self.stronghinttxt, (self.size[0]/2 + 220, self.size[1]/2 + 90))

class ImpossiblequizCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/impossiblequiz_card.png", screen, eventHandler, timer)
        self.wrong = False
        self.alpha = 0
        self.wrongImg = pygame.image.load("res/wrong_impossiblequiz.png")
        self.counter = 0
        self.hover_surface = pygame.Surface((782 - 429, 673 - 569))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            if 429 <= mousePos[0] <= 782:
                if 569 <= mousePos[1] <= 673:
                    self.alpha = 255
                    self.wrong = True
                    self.counter = 0
                    return False
                if 679 <= mousePos[1] <= 783:
                    self.alpha = 255
                    self.wrong = True
                    self.counter = 0
                    return False
            if 798 <= mousePos[0] <= 1151:
                if 569 <= mousePos[1] <= 673:
                    self.alpha = 255
                    self.wrong = True
                    self.counter = 0
                    return False
                if 679 <= mousePos[1] <= 783:
                    self.done()
                    return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        if self.wrong:
            duration = self.timer.fps*0.9
            self.counter += 1
            if self.counter < duration/2:
                return
            self.alpha -= 255 / (duration/2)
            if self.alpha < 0:
                self.alpha = 0
                self.wrong = False
                self.counter = 0
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 429 <= mousePos[0] <= 782:
            if 569 <= mousePos[1] <= 673:
                self.screen.blit(self.hover_surface, (429, 569))
            if 679 <= mousePos[1] <= 783:
                self.screen.blit(self.hover_surface, (429, 679))
        if 798 <= mousePos[0] <= 1151:
            if 569 <= mousePos[1] <= 673:
                self.screen.blit(self.hover_surface, (798, 569))
            if 679 <= mousePos[1] <= 783:
                self.screen.blit(self.hover_surface, (798, 679))
        if self.wrong:
            self.wrongImg.set_alpha(self.alpha)
            self.screen.blit(self.wrongImg, (self.size[0]/2 - self.wrongImg.get_width()/2, self.size[1]/2 + 10))

class NotclickbuttonCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/notclickbutton_card.png",
                 "1": "res/notclickbutton_card1.png",
                 "2": "res/notclickbutton_card2.png",}
        self.x = random.randint(0, 2)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        if self.x == 0:
            self.answer = 0
        if self.x == 1:
            self.answer = 2
        if self.x == 2:
            self.answer = 0
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    if self.answer == 0:
                        self.done()
                        return True
                    else:
                        return False
                if 702 <= mousePos[0] <= 876:
                    if self.answer == 1:
                        self.done()
                        return True
                    else:
                        return False
                if 1000 <= mousePos[0] <= 1174:
                    if self.answer == 2:
                        self.done()
                        return True
                    else:
                        return False
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))

class MessageCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/message_card.png", screen, eventHandler, timer)
        self.count = 0
        self.hint = False
        self.hintfont = pygame.font.SysFont("segoescript", 30)
        self.hinttxt = self.hintfont.render("hint: capital letters", True, "Red")
        self.hint_surface = pygame.image.load("res/message_card_hovered.png")
        self.buffer = self.surface
        self.started = False
        self.startTime = None


    def tick(self):
        super().tick()
        if self.end:
            return

        if not self.started:
            self.startTime = self.timer.time
            self.started = True
        if self.timer.time - self.startTime > 40:
            self.hint = True

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if self.pos[0] <= mousePos[0] <= self.pos[0] + 85 and self.pos[1] <= mousePos[1] <= self.pos[1] + 85:
                self.done()
                return True
            return False

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return

        mousePos = self.eventHandler.mousePos
        if self.pos[0] <= mousePos[0] <= self.pos[0] + 85 and self.pos[1] <= mousePos[1] <= self.pos[1] + 85:
            self.surface = self.hint_surface
            super().render(counter)
        else:
            self.surface = self.buffer
        if self.hint:
            self.screen.blit(self.hinttxt, (self.pos[0] + self.surface_size[0]/2 - self.hinttxt.get_width()/2, self.pos[1] + self.surface_size[1] - 120))


class LabyrinthCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/labyrinth_card.png", screen, eventHandler, timer)
        self.starting = False
        self.clicked = False
        self.font = pygame.font.SysFont("segoescript", 40)

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.clicked = True
            mousePos = self.eventHandler.mousePos
            if not self.starting:
                if math.sqrt((mousePos[0] - (self.pos[0] + 207))**2 + (mousePos[1] - (self.pos[1] + 282))**2) <= 53:
                    self.starting = True
            else:
                if math.sqrt((mousePos[0] - 1219) ** 2 + (mousePos[1] - 600) ** 2) <= 80 or math.sqrt((mousePos[0] - (self.pos[0] + 207)) ** 2 + (mousePos[1] - (self.pos[1] + 282)) ** 2) <= 95 or 523 <= mousePos[0] <= 714 and 514 <= mousePos[1] <= 623 or 606 <= mousePos[0] <= 714 and 374 <= mousePos[1] <= 550 or 635 <= mousePos[0] <= 872 and 389 <= mousePos[1] <= 473 or 780 <= mousePos[0] <= 865 and 397 <= mousePos[1] <= 741 or 779 <= mousePos[0] <= 1078 and 670 <= mousePos[1] <= 748 or 1005 <= mousePos[0] <= 1080 and 547 <= mousePos[1] <= 670 or 1080 <= mousePos[0] <= 1214 and 547 <= mousePos[1] <= 645:
                    pass
                else:
                    self.starting = False
                    self.eventHandler.is_lockedc["left"] = True
                    self.clicked = False
                    return False
                if math.sqrt((mousePos[0] - 1219) ** 2 + (mousePos[1] - 600) ** 2) <= 52:
                    self.eventHandler.is_lockedc["left"] = True
                    self.done()
                    return True

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
            self.starting = False
            if self.clicked:
                self.clicked = False
                return False
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        if self.starting:
            surface = self.font.render("traversing...", True, "Red")
            self.screen.blit(surface, (self.pos[0] + 700, self.pos[1] + 100))

class PressCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/press_card.png", screen, eventHandler, timer)
        self.hide_surface = pygame.Surface((94, 107))
        self.hide_surface.fill((255, 236, 177))
        self.checks = [not self.eventHandler.is_pressed["j"], not self.eventHandler.is_pressed["o"],
                  not self.eventHandler.is_pressed["l"], not self.eventHandler.is_pressed["g"],
                  not self.eventHandler.is_pressed["w"], not self.eventHandler.is_pressed["d"]]
        self.buttons = [self.eventHandler.is_pressed["a"], self.eventHandler.is_pressed["n"],
                   self.eventHandler.is_pressed["x"], self.eventHandler.is_pressed["q"],
                   self.eventHandler.is_pressed["p"], self.eventHandler.is_pressed["e"],
                   self.eventHandler.is_pressed["k"], self.eventHandler.is_pressed["h"],
                   self.eventHandler.is_pressed["z"], self.eventHandler.is_pressed["f"]]
        self.attempt = False
        self.count = 0

    def tick(self):
        super().tick()
        if self.end:
            return
        checks = [not self.eventHandler.is_pressed["j"], not self.eventHandler.is_pressed["o"],
                       not self.eventHandler.is_pressed["l"], not self.eventHandler.is_pressed["g"],
                       not self.eventHandler.is_pressed["w"], not self.eventHandler.is_pressed["d"]]
        buttons = [self.eventHandler.is_pressed["a"], self.eventHandler.is_pressed["n"],
                        self.eventHandler.is_pressed["x"], self.eventHandler.is_pressed["q"],
                        self.eventHandler.is_pressed["p"], self.eventHandler.is_pressed["e"],
                        self.eventHandler.is_pressed["k"], self.eventHandler.is_pressed["h"],
                        self.eventHandler.is_pressed["z"], self.eventHandler.is_pressed["f"]]
        self.checks = checks
        self.buttons = buttons

        self.count = 0
        for button in buttons:
            if button:
                self.count += 1
            else:
                break

        if self.count > 0:
            self.attempt = True
        if self.count == 0 and self.attempt:
            self.attempt = False
            return False

        if all(buttons) and all(checks):
            self.done()
            return True


    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        if not (self.count > 0 or self.buttons[1]):
            self.screen.blit(self.hide_surface, (1057, 656))  # N
        if not (self.count > 1 or self.buttons[2]):
            self.screen.blit(self.hide_surface, (334, 464))  # X
        if not (self.count > 2 or self.buttons[3]):
            self.screen.blit(self.hide_surface, (1132, 466))  # Q
        if not (self.count > 3 or self.buttons[4]):
            self.screen.blit(self.hide_surface, (413, 690))  # P
        if not (self.count > 4 or self.buttons[5]):
            self.screen.blit(self.hide_surface, (615, 438))  # E
        if not (self.count > 5 or self.buttons[6]):
            self.screen.blit(self.hide_surface, (932, 484))  # K
        if not (self.count > 6 or self.buttons[7]):
            self.screen.blit(self.hide_surface, (857, 667))  # H
        if not (self.count > 7 or self.buttons[8]):
            self.screen.blit(self.hide_surface, (593, 685))  # Z
        if not (self.count > 8 or self.buttons[9]):
            self.screen.blit(self.hide_surface, (481, 534))  # F

class TriangleCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/triangle_card.png", screen, eventHandler, timer)
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
        self.hint = False
        self.hint_surface = pygame.Surface((200, 65))
        self.hint_surface.fill((255, 236, 177))

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    return False
                if 702 <= mousePos[0] <= 876:
                    self.hint = True
                    return False
                if 1000 <= mousePos[0] <= 1174:
                    self.done()
                    return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if not self.hint:
            self.screen.blit(self.hint_surface, (self.pos[0] + 201, self.pos[1] + 93))
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))

class ColorCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/color_card.png", screen, eventHandler, timer)
        self.rgb = [0, 0, 0]

        self.red = pygame.Surface((95, 59))
        self.green = pygame.Surface((95, 59))
        self.blue = pygame.Surface((95, 59))
        self.red.fill("Red")
        self.green.fill("Green")
        self.blue.fill("Blue")
        self.answerrgb = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]
        self.answer_surface = pygame.Surface((175, 175))
        self.guess_surface = pygame.Surface((175, 175))
        self.answer_surface.fill((self.answerrgb[0] * 51, self.answerrgb[1] * 51, self.answerrgb[2] * 51))


    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_pressed["r"] and not self.eventHandler.is_lockedp["r"]:
            self.eventHandler.is_lockedp["r"] = True
            self.rgb[0] = (self.rgb[0] + 1) % 6
        if not self.eventHandler.is_pressed["r"]:
            self.eventHandler.is_lockedp["r"] = False

        if self.eventHandler.is_pressed["g"] and not self.eventHandler.is_lockedp["g"]:
            self.eventHandler.is_lockedp["g"] = True
            self.rgb[1] = (self.rgb[1] + 1) % 6
        if not self.eventHandler.is_pressed["g"]:
            self.eventHandler.is_lockedp["g"] = False

        if self.eventHandler.is_pressed["b"] and not self.eventHandler.is_lockedp["b"]:
            self.eventHandler.is_lockedp["b"] = True
            self.rgb[2] = (self.rgb[2] + 1) % 6
        if not self.eventHandler.is_pressed["b"]:
            self.eventHandler.is_lockedp["b"] = False

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            if math.sqrt((449 - mousePos[0])**2 + (421 - mousePos[1])**2) <= 54:
                self.rgb[0] = (self.rgb[0] + 1) % 6
            if math.sqrt((569 + 49 - mousePos[0])**2 + (421 - mousePos[1])**2) <= 54:
                self.rgb[1] = (self.rgb[1] + 1) % 6
            if math.sqrt((735 + 48 - mousePos[0])**2 + (421 - mousePos[1])**2) <= 54:
                self.rgb[2] = (self.rgb[2] + 1) % 6
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        if self.rgb == self.answerrgb:
            self.done()
            return True



    def render(self, counter):
        super().render(counter)
        for i in range(self.rgb[0]):
            self.screen.blit(self.red, (self.pos[0] + 150, self.pos[1] + 494 - 59 * (i+1)))
        for i in range(self.rgb[1]):
            self.screen.blit(self.green, (self.pos[0] + 319, self.pos[1] + 494 - 59 * (i+1)))
        for i in range(self.rgb[2]):
            self.screen.blit(self.blue, (self.pos[0] + 485, self.pos[1] + 494 - 59 * (i+1)))

        self.guess_surface.fill((self.rgb[0] * 51, self.rgb[1] * 51, self.rgb[2] * 51))
        self.screen.blit(self.guess_surface, (self.pos[0] + 781, self.pos[1] + 72))
        self.screen.blit(self.answer_surface, (self.pos[0] + 781, self.pos[1] + 304))
        if self.end:
            return

class AlphabetCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/alphabet_card.png", screen, eventHandler, timer)
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
        self.hover_interface = pygame.image.load("res/interface_hovered.png")
        self.hintfont = pygame.font.SysFont("segoescript", 25)
        self.hinttxt = self.hintfont.render("hint: There is a C somewhere", True, "Red")
        self.hint = False
        self.start = None

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.start is None:
            self.start = self.timer.time
        if self.timer.time - self.start > 30:
            self.hint = True


        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    return False
                if 702 <= mousePos[0] <= 876:
                    return False
                if 1000 <= mousePos[0] <= 1174:
                    return False
            if 77 <= mousePos[1] <= 177:
                if 763 <= mousePos[0] <= 843:
                    self.done()
                    return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if self.hint:
            self.screen.blit(self.hinttxt, (self.pos[0] + self.surface_size[0]/2 - self.hinttxt.get_width()/2, self.pos[1] + self.surface_size[1]/2 - 70))
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))
        if 77 <= mousePos[1] <= 177:
            if 763 <= mousePos[0] <= 843:
                self.screen.blit(self.hover_interface, (250, 37.5 / 2))
                time = self.timer.time
                if time > 1000:
                    time = str(int(time))
                else:
                    time = str(int(time * 10) / 10)
                timetxt = pygame.font.SysFont("segoescript", 75).render(time, True, "Red")
                cards_lefttxt = pygame.font.SysFont("segoescript", 75).render(str(31 - counter), True, "Red")
                self.screen.blit(timetxt, (400, 75))
                if 31 - counter < 10:
                    self.screen.blit(cards_lefttxt, (1150, 75))
                else:
                    self.screen.blit(cards_lefttxt, (1100, 75))

class ReactionCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/reaction_card.png", screen, eventHandler, timer)
        self.letter = chr(random.randint(97, 122))
        self.starttime = 0
        self.letterfont = pygame.font.SysFont("segoescript", 100)

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.timer.time - self.starttime > 0.65:
            self.starttime = self.timer.time
            newletter = chr(random.randint(97, 122))
            while newletter == self.letter:
                newletter = chr(random.randint(97, 122))
            self.letter = newletter
        for button in self.eventHandler.is_pressed:
            if self.eventHandler.is_pressed[button] and not self.eventHandler.is_lockedp[button]:
                self.eventHandler.is_lockedp[button] = True
                if button == self.letter.lower():
                    self.done()
                    return True
                else:
                    return False
            if not self.eventHandler.is_pressed[button]:
                self.eventHandler.is_lockedp[button] = False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        surface = self.letterfont.render(self.letter.upper(), True, "Black")
        self.screen.blit(surface, (self.pos[0] + self.surface_size[0]/2 - surface.get_width()/2, self.pos[1] + self.surface_size[1]/2 - surface.get_height()/2))

class LightsCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/lights_card.png", screen, eventHandler, timer)
        self.lights = [True, False, True, False, True, False]

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            for i in range(6):
                if math.sqrt((mousePos[0] - (479 + 129*i))**2 + (mousePos[1] - 605)**2) <= 50:
                    self.lights[i] = not self.lights[i]
                    if i > 0:
                        self.lights[i-1] = not self.lights[i-1]
                    if i < 5:
                        self.lights[i + 1] = not self.lights[i + 1]

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        for i in range(6):
            if self.lights[i]:
                break
        else:
            self.done()
            return True
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        for i in range(6):
            if self.lights[i]:
                pygame.draw.circle(self.screen, "Yellow", (479 + 129*i, 605), 50) # 609

class ButtonsCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/buttons_card.png", screen, eventHandler, timer)
        self.hover_surface = pygame.Surface((100, 75))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
        self.answer = [random.randint(0,6), random.randint(0,3)]

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            for y in range(4):
                for x in range(7):
                    if 361 + x * 130 <= mousePos[0] <= 361 + 100 + x * 130 and 416 + y * 90 <= mousePos[1] <= 416 + 75 + y * 90:
                        if [x,y] == self.answer:
                            self.done()
                            return True

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        for y in range(4):
            for x in range(7):
                if 361 + x*130 <= mousePos[0] <= 361 + 100 + x*130 and 416 + y*90 <= mousePos[1] <= 416 + 75 + y*90:
                    self.screen.blit(self.hover_surface, (361 + x*130, 416 + y*90))

class WingdingsCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/wingdings_card.png", screen, eventHandler, timer)
        self.answer = chr(random.randint(97, 122))
        self.guess = None
        self.font_answer = pygame.font.SysFont("wingdings", 65)
        self.font_guess = pygame.font.SysFont("wingdings", 95)
        self.answer_surface = self.font_answer.render(self.answer, True, "Red")

    def tick(self):
        super().tick()
        if self.end:
            return
        for button in self.eventHandler.is_pressed:
            if not button.isalpha() or len(button) > 1:
                continue
            if self.eventHandler.is_pressed[button] and not self.eventHandler.is_lockedp[button]:
                self.eventHandler.is_lockedp[button] = True
                self.guess = button
                self.wronglock = False
            if not self.eventHandler.is_pressed[button]:
                self.eventHandler.is_lockedp[button] = False

        if self.guess == self.answer:
            self.done()
            return True

    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        self.screen.blit(self.answer_surface, (self.size[0] / 2 + 68, self.pos[1] + 57))
        if self.guess is not None:
            guess_surface = self.font_guess.render(self.guess, True, "Black")
            self.screen.blit(guess_surface, (self.size[0]/2 - guess_surface.get_width()/2, self.size[1]/2 + self.pos[1]/2 - 30))

class ReplikaCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/replika_card.png", screen, eventHandler, timer)
        self.hover_surface = pygame.Surface((60, 60))
        self.hover_surface.set_alpha(15)
        self.hover_surface.set_colorkey((255, 255, 255))
        self.light_surface = pygame.Surface((60, 60))
        self.light_surface.fill("White")
        self.answer = []
        for _ in range(5):
            row = []
            for _ in range(5):
                row.append(random.randint(0, 1))
            self.answer.append(row)
        self.guess = []
        for _ in range(5):
            row = []
            for _ in range(5):
                row.append(random.randint(0, 1))
            self.guess.append(row)


    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            for y in range(5):
                for x in range(5):
                    if 860 + x * 75 <= mousePos[0] <= 860 + 60 + x * 75 and 416 + y * 75 <= mousePos[1] <= 416 + 60 + y * 75:
                        self.guess[y][x] = not self.guess[y][x]

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
        if self.guess == self.answer:
            self.done()
            return True
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        for y in range(5):
            for x in range(5):
                if self.answer[y][x]:
                    self.screen.blit(self.light_surface, (378 + x * 75, 416 + y * 75))
                if self.guess[y][x]:
                    self.screen.blit(self.light_surface, (860 + x * 75, 416 + y * 75))
                if 860 + x * 75 <= mousePos[0] <= 860 + 60 + x * 75 and 416 + y * 75 <= mousePos[1] <= 416 + 60 + y * 75:
                    self.screen.blit(self.hover_surface, (860 + x * 75, 416 + y * 75))

class AsteroidsCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/asteroids_card.png", screen, eventHandler, timer)
        self.middle = (self.pos[0] + self.surface_size[0]/2, self.pos[1] + self.surface_size[1]/2)
        self.points = [(650, 450, 50), (600, 600, 40), (620, 510, 15), (720, 380, 35), (683, 555, 20), (695, 675, 60), (740, 522, 32), (835, 404, 55), (835, 482, 18), (823, 527, 25), (744, 602, 20), (912, 602, 75), (805, 703, 37), (745, 760, 32), (870, 720, 18), (961, 700, 24), (903, 762, 25), (1032, 758, 34), (1070, 681, 40), (1048, 603, 32), (1071, 505, 45), (952, 493, 25), (988, 463, 15), (1017, 399, 39), (1118, 387, 50), (1160, 521, 32), (1132, 615, 32), (468, 379, 3)]
        self.player = [self.middle[0] - 335, self.middle[1] - 2]


    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_pressed["w"]:
            self.player[1] -= 3
        if self.eventHandler.is_pressed["a"]:
            self.player[0] -= 3
        if self.eventHandler.is_pressed["s"]:
            self.player[1] += 3
        if self.eventHandler.is_pressed["d"]:
            self.player[0] += 3
        if self.player[0] < 351:
            self.player[0] = 351
        if self.player[1] < 349:
            self.player[1] = 349
        if self.player[1] > 791:
            self.player[1] = 791
        if self.player[0] > 1149:
            self.done()
            return True
        for point in self.points:
            if math.sqrt((self.player[0] - point[0])**2 + (self.player[1] - point[1])**2) < point[2] + 5:
                self.player = [self.middle[0] - 335, self.middle[1] - 2]
                return False

    def render(self, counter):
        super().render(counter)
        for point in self.points:
            pygame.draw.circle(self.screen, "Red", (self.pos[0] - 250 + point[0], point[1]), point[2])
        if self.end:
            return
        pygame.draw.circle(self.screen, "Green", self.player, 8)

class GraphCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/graph_card.png", screen, eventHandler, timer)
        self.points = [(797, 356, 20), (665, 503, 20), (925, 503, 20), (665, 743, 20), (925, 743, 20)]
        self.edges = [[(797, 356), (665, 503)], [(797, 356), (925, 503)], [(665, 503), (925, 503)], [(665, 503), (665, 743)], [(665, 503), (925, 743)], [(925, 503), (665, 743)], [(925, 503), (925, 743)], [(665, 743), (925, 743)]]
        self.edges_copy = list(self.edges)
        self.starting = False
        self.clicked = False
        self.way = []
        self.current = [(0, 0), (0, 0)]

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            mousePos = self.eventHandler.mousePos
            if not self.starting:
                for i in range(5):
                    if math.sqrt((mousePos[0] - (self.points[i][0])) ** 2 + (mousePos[1] - (self.points[i][1])) ** 2) <= 20:
                        self.way.append((self.points[i][0], self.points[i][1]))
                        self.starting = True
                        self.clicked = True
            else:
                for i in range(5):
                    if math.sqrt((mousePos[0] - (self.points[i][0])) ** 2 + (mousePos[1] - (self.points[i][1])) ** 2) <= 20:
                        if self.points[i] == self.way[len(self.way) - 1] or [(self.points[i][0], self.points[i][1])] in self.way:
                            continue
                        if [self.way[len(self.way) - 1], (self.points[i][0], self.points[i][1])] in self.edges_copy or [(self.points[i][0], self.points[i][1]), self.way[len(self.way) - 1]] in self.edges_copy:
                            for j in range(len(self.edges_copy)):
                                if self.edges_copy[j] == [self.way[len(self.way) - 1], (self.points[i][0], self.points[i][1])] or self.edges_copy[j] == [(self.points[i][0], self.points[i][1]), self.way[len(self.way) - 1]]:
                                    self.current = self.edges_copy.pop(j)
                                    new_edge = (self.points[i][0], self.points[i][1])
                                    self.way.append(new_edge)
                                    break

            if len(self.edges_copy) == 0:
                self.eventHandler.is_lockedc["left"] = True
                self.done()
                return True

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
            self.starting = False
            self.edges_copy = list(self.edges)
            self.way = []
            if self.clicked:
                self.clicked = False
                return False

    def render(self, counter):
        super().render(counter)
        for point in self.points:
            pygame.draw.circle(self.screen, "Red", (self.pos[0] - 250 + point[0], point[1]), point[2])
        for i in range(len(self.way) - 1):
            point1 = (self.way[i][0] + self.pos[0] - 250, self.way[i][1])
            point2 = (self.way[i+1][0] + self.pos[0] - 250, self.way[i+1][1])
            pygame.draw.line(self.screen, "Red", point1, point2, 5)
        if self.end:
            return

class PrimeCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/prime_card1.png",
                 "1": "res/prime_card4.png",
                 "2": "res/prime_card2.png",
                 "3": "res/prime_card3.png", }
        self.x = random.randint(0, 3)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        self.buttons = [False, False, False, False, False, False]
        if self.x == 0:
            self.correct = [self.buttons[0]] + self.buttons[2:4] + [self.buttons[5]]
            self.wrong = [self.buttons[1]] + [self.buttons[4]]
        if self.x == 1:
            self.correct = self.buttons[:2] + self.buttons[4:]
            self.wrong = self.buttons[2:4]
        if self.x == 2:
            self.correct = [self.buttons[0]] + [self.buttons[5]]
            self.wrong = self.buttons[1:5]
        if self.x == 3:
            self.correct = [self.buttons[0]] + self.buttons[3:]
            self.wrong = self.buttons[1:3]
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    self.buttons[3] = not self.buttons[3]
                if 702 <= mousePos[0] <= 876:
                    self.buttons[4] = not self.buttons[4]
                if 1000 <= mousePos[0] <= 1174:
                    self.buttons[5] = not self.buttons[5]
            if 380 <= mousePos[1] <= 380 + 124:
                if 403 <= mousePos[0] <= 575:
                    self.buttons[0] = not self.buttons[0]
                if 702 <= mousePos[0] <= 876:
                    self.buttons[1] = not self.buttons[1]
                if 1000 <= mousePos[0] <= 1174:
                    self.buttons[2] = not self.buttons[2]

        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
        if self.x == 0:
            self.correct = [self.buttons[0]] + self.buttons[2:4] + [self.buttons[5]]
            self.wrong = [self.buttons[1]] + [self.buttons[4]]
        if self.x == 1:
            self.correct = self.buttons[:2] + self.buttons[4:]
            self.wrong = self.buttons[2:4]
        if self.x == 2:
            self.correct = [self.buttons[0]] + [self.buttons[5]]
            self.wrong = self.buttons[1:5]
        if self.x == 3:
            self.correct = [self.buttons[0]] + self.buttons[3:]
            self.wrong = self.buttons[1:3]
        if all(self.correct) and not any(self.wrong):
            self.done()
            return True
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        if self.buttons[0]:
            self.screen.blit(self.hover_surface, (403, 380))
        if self.buttons[1]:
            self.screen.blit(self.hover_surface, (702, 380))
        if self.buttons[2]:
            self.screen.blit(self.hover_surface, (1000, 380))
        if self.buttons[3]:
            self.screen.blit(self.hover_surface, (403, 628))
        if self.buttons[4]:
            self.screen.blit(self.hover_surface, (702, 628))
        if self.buttons[5]:
            self.screen.blit(self.hover_surface, (1000, 628))
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))
        if 380 <= mousePos[1] <= 380 + 124:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 380))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 380))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 380))

class PolygonCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/polygon_card.png", screen, eventHandler, timer)
        self.sequence = []
        for _ in range(6):
            x = random.randint(0,12)
            while x in self.sequence:
                x = random.randint(0,12)
            self.sequence.append(x)
        self.guess = None
        self.clicked = False
        self.count = 0
        self.font = pygame.font.SysFont("segoescript", 42)
        self.hovered = [pygame.image.load("res/polygon_card0.png"),pygame.image.load("res/polygon_card1.png"),pygame.image.load("res/polygon_card2.png"),pygame.image.load("res/polygon_card3.png"),pygame.image.load("res/polygon_card4.png"),pygame.image.load("res/polygon_card5.png"),pygame.image.load("res/polygon_card6.png"),pygame.image.load("res/polygon_card7.png"),pygame.image.load("res/polygon_card8.png"),pygame.image.load("res/polygon_card9.png"),pygame.image.load("res/polygon_card10.png"),pygame.image.load("res/polygon_card11.png"),pygame.image.load("res/polygon_card12.png")]

    def tick(self):
        super().tick()
        if self.end:
            return

        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            if 416 <= mousePos[0] <= 515 and 352 <= mousePos[1] <= 533:
                self.guess = 4
                self.clicked = True
            if 295 <= mousePos[0] <= 407 and 470 <= mousePos[1] <= 581:
                self.guess = 12
                self.clicked = True
            if 334 <= mousePos[0] <= 416 and 613 <= mousePos[1] <= 694:
                self.guess = 0
                self.clicked = True
            if 439 <= mousePos[0] <= 601 and 626 <= mousePos[1] <= 751:
                self.guess = 5
                self.clicked = True
            if 540 <= mousePos[0] <= 710 and 494 <= mousePos[1] <= 575:
                self.guess = 10
                self.clicked = True
            if 636 <= mousePos[0] <= 800 and 598 <= mousePos[1] <= 766:
                self.guess = 8
                self.clicked = True
            if 812 <= mousePos[0] <= 991 and 642 <= mousePos[1] <= 756:
                self.guess = 9
                self.clicked = True
            if 857 <= mousePos[0] <= 986 and 532 <= mousePos[1] <= 592:
                self.guess = 2
                self.clicked = True
            if 1019 <= mousePos[0] <= 1227 and 704 <= mousePos[1] <= 785:
                self.guess = 3
                self.clicked = True
            if 1218 <= mousePos[0] <= 1301 and 582 <= mousePos[1] <= 682:
                self.guess = 7
                self.clicked = True
            if 1039 <= mousePos[0] <= 1193 and 501 <= mousePos[1] <= 658:
                self.guess = 6
                self.clicked = True
            if 1175 <= mousePos[0] <= 1251 and 379 <= mousePos[1] <= 496:
                self.guess = 1
                self.clicked = True
            if 1010 <= mousePos[0] <= 1115 and 346 <= mousePos[1] <= 491:
                self.guess = 11
                self.clicked = True
        if self.clicked:
            self.clicked = False
            if self.guess == self.sequence[self.count]:
                self.count += 1
        if self.count == 6:
            self.done()
            return True


        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

    def render(self, counter):
        super().render(counter)
        if self.end:
            return

        mousePos = self.eventHandler.mousePos
        if 416 <= mousePos[0] <= 515 and 352 <= mousePos[1] <= 533:
            self.screen.blit(self.hovered[4], self.pos)
            self.drawNumber(counter)
        if 295 <= mousePos[0] <= 407 and 470 <= mousePos[1] <= 581:
            self.screen.blit(self.hovered[12], self.pos)
            self.drawNumber(counter)
        if 334 <= mousePos[0] <= 416 and 613 <= mousePos[1] <= 694:
            self.screen.blit(self.hovered[0], self.pos)
            self.drawNumber(counter)
        if 439 <= mousePos[0] <= 601 and 626 <= mousePos[1] <= 751:
            self.screen.blit(self.hovered[5], self.pos)
            self.drawNumber(counter)
        if 540 <= mousePos[0] <= 710 and 494 <= mousePos[1] <= 575:
            self.screen.blit(self.hovered[10], self.pos)
            self.drawNumber(counter)
        if 636 <= mousePos[0] <= 800 and 598 <= mousePos[1] <= 766:
            self.screen.blit(self.hovered[8], self.pos)
            self.drawNumber(counter)
        if 812 <= mousePos[0] <= 991 and 642 <= mousePos[1] <= 756:
            self.screen.blit(self.hovered[9], self.pos)
            self.drawNumber(counter)
        if 857 <= mousePos[0] <= 986 and 532 <= mousePos[1] <= 592:
            self.screen.blit(self.hovered[2], self.pos)
            self.drawNumber(counter)
        if 1019 <= mousePos[0] <= 1227 and 704 <= mousePos[1] <= 785:
            self.screen.blit(self.hovered[3], self.pos)
            self.drawNumber(counter)
        if 1218 <= mousePos[0] <= 1301 and 582 <= mousePos[1] <= 682:
            self.screen.blit(self.hovered[7], self.pos)
            self.drawNumber(counter)
        if 1039 <= mousePos[0] <= 1193 and 501 <= mousePos[1] <= 658:
            self.screen.blit(self.hovered[6], self.pos)
            self.drawNumber(counter)
        if 1175 <= mousePos[0] <= 1251 and 379 <= mousePos[1] <= 496:
            self.screen.blit(self.hovered[1], self.pos)
            self.drawNumber(counter)
        if 1010 <= mousePos[0] <= 1115 and 346 <= mousePos[1] <= 491:
            self.screen.blit(self.hovered[11], self.pos)
            self.drawNumber(counter)

        for i in range(6):
            if i < self.count:
                color = "Green"
            else:
                color = "Red"
            number = self.font.render(str(self.sequence[i]), True, color)
            self.screen.blit(number, (self.size[0]/2 - number.get_width()/2 - 190 + 65*i, self.pos[1] + 90))

class TargetCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/target_card.png", screen, eventHandler, timer)
        self.target = random.randint(0,3)
        self.cover = pygame.Surface((150,150))
        self.cover.fill((255, 236, 177))
        self.count = 0

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_pressed["w"] and not self.eventHandler.is_lockedp["w"]:
            self.eventHandler.is_lockedp["w"] = True
            if self.target == 0:
                self.newTarget()
            else:
                return False
        if self.eventHandler.is_pressed["a"] and not self.eventHandler.is_lockedp["a"]:
            self.eventHandler.is_lockedp["a"] = True
            if self.target == 1:
                self.newTarget()
            else:
                return False
        if self.eventHandler.is_pressed["s"] and not self.eventHandler.is_lockedp["s"]:
            self.eventHandler.is_lockedp["s"] = True
            if self.target == 2:
                self.newTarget()
            else:
                return False
        if self.eventHandler.is_pressed["d"] and not self.eventHandler.is_lockedp["d"]:
            self.eventHandler.is_lockedp["d"] = True
            if self.target == 3:
                self.newTarget()
            else:
                return False

        if self.count == 10:
            self.done()
            return True

        if not self.eventHandler.is_pressed["w"]:
            self.eventHandler.is_lockedp["w"] = False
        if not self.eventHandler.is_pressed["a"]:
            self.eventHandler.is_lockedp["a"] = False
        if not self.eventHandler.is_pressed["s"]:
            self.eventHandler.is_lockedp["s"] = False
        if not self.eventHandler.is_pressed["d"]:
            self.eventHandler.is_lockedp["d"] = False
    def render(self, counter):
        super().render(counter)
        if self.end:
            return
        if self.target != 3:
            self.screen.blit(self.cover, (946, 489))
        if self.target != 2:
            self.screen.blit(self.cover, (728, 646))
        if self.target != 1:
            self.screen.blit(self.cover, (514, 489))
        if self.target != 0:
            self.screen.blit(self.cover, (729, 341))
    def newTarget(self):
        new_target = random.randint(0, 3)
        while new_target == self.target:
            new_target = random.randint(0, 3)
        self.target = new_target
        self.count += 1

class PasswordCard1(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/password_card1.png", screen, eventHandler, timer)
        self.password = ""
        self.font = pygame.font.SysFont("segoescript", 75)
        self.rule_font = pygame.font.SysFont("segoescript", 25)
        self.has_number = False
        self.has_j = False
        self.has_z = False
        self.has_q = False
        self.rule = False
        self.number_of = dict()

        self.hover_surface = pygame.Surface((407, 72))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            if 578 <= mousePos[0] <= 985 and 552 <= mousePos[1] <= 624:
                if self.has_number and self.has_j and self.has_z and self.has_q and self.rule and len(self.password) == 10:
                    Card.holding = self.password
                    self.done()
                    return True
                else:
                    return False
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        for button in self.eventHandler.is_pressed:
            if len(button) > 1:
                continue
            if self.eventHandler.is_pressed[button] and not self.eventHandler.is_lockedp[button]:
                self.eventHandler.is_lockedp[button] = True
                if len(self.password) < 10:
                    self.password += button
                    if button in self.number_of.keys():
                        self.number_of[button] += 1
                    else:
                        self.number_of[button] = 1
            if not self.eventHandler.is_pressed[button]:
                self.eventHandler.is_lockedp[button] = False
        if self.eventHandler.is_pressed["back"] and not self.eventHandler.is_lockedp["back"]:
            self.eventHandler.is_lockedp["back"] = True
            if len(self.password) > 0:
                self.number_of[self.password[len(self.password) - 1]] -= 1
                self.password = self.password[:len(self.password) - 1]
        if not self.eventHandler.is_pressed["back"]:
            self.eventHandler.is_lockedp["back"] = False

        if "q" in self.number_of.keys():
            if self.number_of["q"] > 0:
                self.has_q = True
            else:
                self.has_q = False
        if "j" in self.number_of.keys():
            if self.number_of["j"] > 0:
                self.has_j = True
            else:
                self.has_j = False
        if "z" in self.number_of.keys():
            if self.number_of["z"] > 0:
                self.has_z = True
            else:
                self.has_z = False
        for letter in self.password:
            if not letter.isalpha():
                self.has_number = True
                break
        else:
            self.has_number = False
        for key in self.number_of:
            if self.number_of[key] > 2:
                self.rule = False
                break
        else:
            self.rule = True

    def render(self, counter):
        super().render(counter)
        if len(self.password) == 10:
            rule1 = self.rule_font.render("must be 10 characters long", True, "Green")
        else:
            rule1 = self.rule_font.render("must be 10 characters long", True, "Red")

        if self.has_number:
            rule2 = self.rule_font.render("must include a number", True, "Green")
        else:
            rule2 = self.rule_font.render("must include a number", True, "Red")

        if self.has_j and self.has_q and self.has_z:
            rule3 = self.rule_font.render("must include j, q and z", True, "Green")
        else:
            rule3 = self.rule_font.render("must include j, q and z", True, "Red")

        if self.rule and len(self.password) == 10:
            rule4 = self.rule_font.render("must not repeat a letter more than once", True, "Green")
        else:
            rule4 = self.rule_font.render("must not repeat a letter more than once", True, "Red")

        self.screen.blit(rule1, (self.pos[0] + self.surface_size[0]/2 - rule1.get_width()/2 - 70, self.pos[1] + 335))
        self.screen.blit(rule2, (self.pos[0] + self.surface_size[0] / 2 - rule1.get_width() / 2 - 70, self.pos[1] + 335 + 45))
        self.screen.blit(rule3, (self.pos[0] + self.surface_size[0] / 2 - rule1.get_width() / 2 - 70, self.pos[1] + 335 + 90))
        self.screen.blit(rule4, (self.pos[0] + self.surface_size[0] / 2 - rule1.get_width() / 2 - 70, self.pos[1] + 335 + 135))
        password = self.font.render(self.password, True, "Black")
        self.screen.blit(password, (self.pos[0] + self.surface_size[0]/2 - password.get_width()/2 - 5, self.pos[1] + 140))
        if self.end:
            return

        mousePos = self.eventHandler.mousePos
        if 578 <= mousePos[0] <= 985 and 552 <= mousePos[1] <= 624:
            self.screen.blit(self.hover_surface, (578, 552))

class PasswordCard2(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/password_card2.png", screen, eventHandler, timer)
        self.cover = pygame.Surface((664 - 469, 646 - 638))
        self.cover.fill((255, 236, 177))
        self.point_cover = pygame.Surface((62, 62))
        self.point_cover.fill((255, 222, 134))
        self.hover = False
        self.clicks = 50
        self.show = False
        self.challcover = pygame.Surface((1137 - 480, 791 - 684))
        self.challcover.fill((255, 236, 177))
        self.leftfont = pygame.font.SysFont("segoescript", 35)
        self.password = ""
        self.faillock = False

    def tick(self):
        super().tick()
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 468 <= mousePos[0] <= 666 and 611 <= mousePos[1] <= 638:
            self.hover = True
        else:
            self.hover = False
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            if self.show and self.clicks > 0:
                self.clicks -= 1
            if self.hover:
                self.show = True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
        for button in self.eventHandler.is_pressed:
            if len(button) > 1:
                continue
            if self.eventHandler.is_pressed[button] and not self.eventHandler.is_lockedp[button]:
                self.eventHandler.is_lockedp[button] = True
                if len(self.password) < 10:
                    self.password += button
            if not self.eventHandler.is_pressed[button]:
                self.eventHandler.is_lockedp[button] = False
        if self.eventHandler.is_pressed["back"] and not self.eventHandler.is_lockedp["back"]:
            self.eventHandler.is_lockedp["back"] = True
            if len(self.password) > 0:
                self.password = self.password[:len(self.password) - 1]
        if not self.eventHandler.is_pressed["back"]:
            self.eventHandler.is_lockedp["back"] = False
        if len(self.password) < 10 and self.faillock:
            self.faillock = False
        if self.password == Card.holding:
            self.done()
            return True
        if len(self.password) == 10 and not self.faillock:
            self.faillock = True
            return False

    def render(self, counter):
        super().render(counter)
        if not self.show:
            self.screen.blit(self.challcover, (self.pos[0] - 250 + 480, 684))
        else:
            nums_left = self.leftfont.render(str(self.clicks), True, "Red")
            if self.clicks >= 10:
                self.screen.blit(nums_left, (self.pos[0] - 250 + 612, 680))
            else:
                self.screen.blit(nums_left, (self.pos[0] - 250 + 622, 680))
        if self.clicks == 0:
            password = self.leftfont.render(Card.holding, True, "Black")
            self.screen.blit(password, (self.pos[0] - 250 + 840, 732))
        for i in range(10 - len(self.password)):
            self.screen.blit(self.point_cover, (489 + 62*9 - 62*i, 508))
        if self.end:
            return
        if not self.hover:
            self.screen.blit(self.cover, (469, 638))

class OrderCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/order_card.png", screen, eventHandler, timer)
        self.answer = [5, 3, 4, 1, 6, 2]
        self.started = False
        self.sequence = []
        self.inputs = 0
        self.hover_surface = pygame.Surface((174, 124))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
        self.start = None
        self.hintfont = pygame.font.SysFont("segoescript", 15)
        self.hint = False
        self.hinttxt = self.hintfont.render("hint: the number appearing on screen from clicking a button corresponds to its place in the sequence", True, "Red")

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.start is None:
            self.start = self.timer.time
        if self.timer.time - self.start > 30:
            self.hint = True
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    self.sequence.append(4)
                    self.started = True
                    self.inputs += 1
                if 702 <= mousePos[0] <= 876:
                    self.sequence.append(5)
                    self.started = True
                    self.inputs += 1
                if 1000 <= mousePos[0] <= 1174:
                    self.sequence.append(6)
                    self.started = True
                    self.inputs += 1
            if 380 <= mousePos[1] <= 380 + 124:
                if 403 <= mousePos[0] <= 575:
                    self.sequence.append(1)
                    self.started = True
                    self.inputs += 1
                if 702 <= mousePos[0] <= 876:
                    self.sequence.append(2)
                    self.started = True
                    self.inputs += 1
                if 1000 <= mousePos[0] <= 1174:
                    self.sequence.append(3)
                    self.started = True
                    self.inputs += 1


        if self.sequence != self.answer[:self.inputs]:
            self.started = False
            self.inputs = 0
            self.sequence = []
        if self.sequence == self.answer:
            self.done()
            return True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
    def render(self, counter):
        super().render(counter)
        if self.inputs > 0:
            self.screen.blit(self.hover_surface, (self.pos[0] - 250 + 702, 628))
        if self.inputs > 1:
            self.screen.blit(self.hover_surface, (self.pos[0] - 250 + 1000, 380))
        if self.inputs > 2:
            self.screen.blit(self.hover_surface, (self.pos[0] - 250 + 403, 628))
        if self.inputs > 3:
            self.screen.blit(self.hover_surface, (self.pos[0] - 250 + 403, 380))
        if self.inputs > 4:
            self.screen.blit(self.hover_surface, (self.pos[0] - 250 + 1000, 628))
        if self.inputs > 5:
            self.screen.blit(self.hover_surface, (self.pos[0] - 250 + 702, 380))
        if self.hint:
            self.screen.blit(self.hinttxt, (self.pos[0] + self.surface_size[0]/2 - self.hinttxt.get_width()/2, self.pos[1] + self.surface_size[1] - 80))
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 628 <= mousePos[1] <= 752:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 628))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 628))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 628))
        if 380 <= mousePos[1] <= 380 + 124:
            if 403 <= mousePos[0] <= 575:
                self.screen.blit(self.hover_surface, (403, 380))
            if 702 <= mousePos[0] <= 876:
                self.screen.blit(self.hover_surface, (702, 380))
            if 1000 <= mousePos[0] <= 1174:
                self.screen.blit(self.hover_surface, (1000, 380))
        if self.eventHandler.is_clicked["left"]:
            mousePos = self.eventHandler.mousePos
            if 628 <= mousePos[1] <= 752:
                if 403 <= mousePos[0] <= 575:
                    three_surface = pygame.Surface((200, 80))
                    three_surface.fill((255, 253, 219))
                    self.screen.blit(three_surface, (1019, 90))
                    three_font = pygame.font.SysFont("segoescript", 75).render("3", True, "Red")
                    self.screen.blit(three_font, (1150, 75))
                if 702 <= mousePos[0] <= 876:
                    one_font = pygame.font.SysFont("segoescript", 100)
                    one = one_font.render("1", True, (246, 147, 244))
                    self.screen.blit(one, (1470, 705))
                if 1000 <= mousePos[0] <= 1174:
                    five_surface = pygame.Surface((50, 55))
                    five_surface.fill((255, 236, 177))
                    self.screen.blit(five_surface, (667, 539))
                    five_font = pygame.font.SysFont("segoescript", 72).render("5", True, "Red")
                    self.screen.blit(five_font, (663, 508))
            if 380 <= mousePos[1] <= 380 + 124:
                if 403 <= mousePos[0] <= 575:
                    four_font = pygame.font.SysFont("segoescript", 70)
                    four = four_font.render("4", True, (243, 224, 165))
                    self.screen.blit(four, (902, 670))
                if 702 <= mousePos[0] <= 876:
                    six_font = pygame.font.SysFont("segoescript", 30).render("6", True, (120, 120, 120))
                    self.screen.blit(six_font, (313, 118))
                if 1000 <= mousePos[0] <= 1174:
                    two_surface = pygame.Surface((74, 60))
                    two_surface.fill((236, 192, 94))
                    self.screen.blit(two_surface, (260, 757))
                    self.drawNumber(2)
        if not self.eventHandler.is_clicked["left"]:
            state.order_card_block = False

class TrailCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/trail_card.png",
                 "1": "res/trail_card.png",
                 "2": "res/trail_card.png",
                 "3": "res/trail_card.png",
                 "4": "res/trail_card.png",
                 "5": "res/trail_card.png",
                 "6": "res/trail_card.png"}
        self.x = random.randint(0, 6)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        if self.x in range(7):
            self.level_dict =  {"0" : pygame.image.load("res/trail_card1.png"),
                                "1" : pygame.image.load("res/trail_card2.png"),
                                "2" : pygame.image.load("res/trail_card3.png"),}
            self.buttons = ["j", "a", "m"]
        self.level = 1
    def tick(self):
        super().tick()
        if self.end:
            return

        for button in self.eventHandler.is_pressed:
            if len(button) > 1 or not button.isalpha():
                continue
            if self.eventHandler.is_pressed[button] and not self.eventHandler.is_lockedp[button]:
                self.eventHandler.is_lockedp[button] = True
                if button not in self.buttons:
                    return False
                if button == self.buttons[self.level - 1]:
                    self.level += 1
                    self.surface = self.level_dict[str(self.level - 2)]
            if not self.eventHandler.is_pressed[button]:
                self.eventHandler.is_lockedp[button] = False

        if self.level == 4:
            self.done()
            return True
    def render(self, counter):
        super().render(counter)
        if self.end:
            return


class ColorwordCard(Card):
    def __init__(self, screen, eventHandler, timer):
        cards = {"0": "res/colorword_card.png",
                 "1": "res/colorword_card1.png",
                 "2": "res/colorword_card2.png",
                 "3": "res/colorword_card3.png",}
        self.x = random.randint(0, 3)

        super().__init__(cards[str(self.x)], screen, eventHandler, timer)
        self.hover_surface = pygame.Surface((148, 109))
        self.hover_surface.set_alpha(30)
        self.hover_surface.set_colorkey((255, 255, 255))
        self.buttons = [False, False, False, False, False]
        if self.x == 0:
            self.sequence = [1,4,3,1,2]
        if self.x == 1:
            self.sequence = [0,4,1,0,4]
        if self.x == 2:
            self.sequence = [2,3,1,0,4]
        if self.x == 3:
            self.sequence = [0,4,0,0,0]
        self.level = 0
        self.check = pygame.image.load("res/check.png")
        self.check = pygame.transform.scale(self.check, (self.check.get_width()/6, self.check.get_height()/6))

    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            mousePos = self.eventHandler.mousePos
            if 644 <= mousePos[1] <= 753:
                for i in range(5):
                    if 362 + 180 * i <= mousePos[0] <= 511 + 180 * i:
                        self.buttons[i] = True
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False
        if any(self.buttons):
            if self.buttons[self.sequence[self.level]]:
                self.level += 1
            else:
                self.buttons = [False, False, False, False, False]
                return False
        if self.level == 5:
            self.done()
            return True

        self.buttons = [False, False, False, False, False]
    def render(self, counter):
        super().render(counter)
        for i in range(self.level):
            self.screen.blit(self.check, (self.pos[0] + 215 + 162*i, self.pos[1] + 230))
        if self.end:
            return
        mousePos = self.eventHandler.mousePos
        if 644 <= mousePos[1] <= 753:
            for i in range(5):
                if 362 + 180*i <= mousePos[0] <= 511 + 180*i:
                    self.screen.blit(self.hover_surface, (362 + 180*i, 644))

class MousebuttonsCard(Card):
    def __init__(self, screen, eventHandler, timer):
        super().__init__("res/mousebuttons_card.png", screen, eventHandler, timer)
        self.started = False
        self.now = 0
        self.last = 0
        self.clicks_left = 11
        self.cover = pygame.Surface((495, 37))
        self.cover.fill((255, 236, 177))
        self.font = pygame.font.SysFont("segoescript", 75)
        self.leftfont = pygame.font.SysFont("segoescript", 26)
    def tick(self):
        super().tick()
        if self.end:
            return
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True
            self.started = True
            if not self.last:
                self.clicks_left -= 1
            else:
                return False
            self.last = self.now
            self.now = random.randint(0,1)
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        if self.eventHandler.is_clicked["right"] and not self.eventHandler.is_lockedc["right"]:
            self.eventHandler.is_lockedc["right"] = True
            if self.last:
                self.clicks_left -= 1
            else:
                return False
            self.last = self.now
            self.now = random.randint(0,1)
        if not self.eventHandler.is_clicked["right"]:
            self.eventHandler.is_lockedc["right"] = False
        if self.clicks_left == 0:
            self.done()
            return True

    def render(self, counter):
        super().render(counter)
        if not self.now and self.started:
            text = self.font.render("left", True, "Red")
            self.screen.blit(text, (self.pos[0] + self.surface_size[0]/2 - text.get_width()/2, 642 - text.get_height()/2))
        if self.now:
            text = self.font.render("right ", True, "Red")
            self.screen.blit(text, (self.pos[0] + self.surface_size[0] / 2 - text.get_width() / 2, 642 - text.get_height() / 2))
        if self.started:
            self.screen.blit(self.cover, (self.pos[0] - 250 + 554, 731))
        if self.end:
            return
        if self.started:
            text = self.leftfont.render(str(self.clicks_left), True, "Red")
            self.screen.blit(text, (1054 - text.get_width()/2, 531 - text.get_height()/2))
