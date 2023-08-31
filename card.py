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

    def render(self, counter):
        self.screen.blit(self.surface, self.pos)
        font = pygame.font.SysFont("segoescript", 49)
        font.set_bold(True)
        number = font.render(str(counter), True, (255,236,177))
        if counter < 10:
            self.screen.blit(number, (self.pos[0]+30, self.pos[1]+460))
        else:
            self.screen.blit(number, (self.pos[0] + 10, self.pos[1] + 465))
    def done(self):
        self.win = True
        self.end = True


class ClickCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/click_card.png", screen, eventHandler)
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

    def render(self, counter):
        super().render(counter)

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

    def render(self, counter):
        super().render(counter)

class MathCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/math_card.png", screen, eventHandler)

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

class RememberCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/memory_card.png", screen, eventHandler)
        self.started = False
        self.sequence = []
        self.inputs = 0
        self.answer = [2,2,1,2,3,1,3]
        self.font = pygame.font.SysFont("segoescript", 92)

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
        if self.started:
            surface = pygame.Surface((950, 120))
            surface.fill((255,236,177))
            self.screen.blit(surface, (300, 435))
            text = self.font.render("did you?", True, "Red")
            self.screen.blit(text, (self.screen.get_width()/2 - text.get_width()/2, 435))

class MinefieldCard(Card):
    def __init__(self, screen, eventHandler):
        super().__init__("res/minefield_card.png", screen, eventHandler)
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
