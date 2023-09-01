import math
import random

import pygame

class Card:
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
        super().__init__("res/math_card.png", screen, eventHandler, timer)
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
                    self.done()
                    return True
                if 702 <= mousePos[0] <= 876:
                    return False
                if 1000 <= mousePos[0] <= 1174:
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
        super().__init__("res/memory_card.png", screen, eventHandler, timer)
        self.started = False
        self.sequence = []
        self.inputs = 0
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
        super().__init__("res/minefield_card.png", screen, eventHandler, timer)

        self.field = [[False, False, True, False, False, True, False],
                      [False, True, False, False, False, True, False],
                      [False, True, False, True, False, False, False],
                      [True, False, False, False, True, False, False],
                      [False, False, True, True, False, False, False],
                      [False, True, False, False, False, True, True],
                      [False, True, False, True, False, False, False]]
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
        if not self.eventHandler.is_pressed["w"]:
            self.eventHandler.is_lockedp["w"] = False

        if self.eventHandler.is_pressed["a"] and not self.eventHandler.is_lockedp["a"]:
            self.eventHandler.is_lockedp["a"] = True
            if self.player_pos[1] > 0:
                self.player_pos[1] -= 1
        if not self.eventHandler.is_pressed["a"]:
            self.eventHandler.is_lockedp["a"] = False

        if self.eventHandler.is_pressed["s"] and not self.eventHandler.is_lockedp["s"]:
            self.eventHandler.is_lockedp["s"] = True
            if self.player_pos[0] < 6:
                self.player_pos[0] += 1
        if not self.eventHandler.is_pressed["s"]:
            self.eventHandler.is_lockedp["s"] = False

        if self.eventHandler.is_pressed["d"] and not self.eventHandler.is_lockedp["d"]:
            self.eventHandler.is_lockedp["d"] = True
            if self.player_pos[1] < 6:
                self.player_pos[1] += 1
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
        super().__init__("res/notclickbutton_card.png", screen, eventHandler, timer)
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
                    self.done()
                    return True
                if 702 <= mousePos[0] <= 876:
                    return False
                if 1000 <= mousePos[0] <= 1174:
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




