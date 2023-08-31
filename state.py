import pygame
import math
import card

import timer
timer = timer.Timer()

class State:
    def __init__(self, screen, eventHandler):
        self.screen = screen
        self.eventHandler = eventHandler

        self.light = False
        self.alpha = 0
        self.color = "Green"
        self.surface = pygame.Surface((screen.get_width(), screen.get_height()))
    def tick(self, states):
        duration = 6
        if self.light:
            self.alpha -= 255 / duration
            if self.alpha < 0:
                self.alpha = 0
                self.light = False

    def render(self):
        if self.light:
            self.surface.fill(self.color)
            self.surface.set_alpha(self.alpha)
            self.screen.blit(self.surface, (0,0))

    def correct(self):
        self.color = "Green"
        self.alpha = 255
        self.light = True
    def wrong(self):
        self.color = "Red"
        self.alpha = 255
        self.light = True


class MenuState(State):
    def __init__(self, screen, eventHandler):
        super().__init__(screen, eventHandler)
        self.play_button = pygame.image.load("res/play_button.png")
        self.play_button_hovered = pygame.image.load("res/play_button_hovered.png")

        self.red_size = 50
        self.yellow_size = 50
        self.green_size = 65
        self.play_width = 750
        self.play_height = 150
    def tick(self, states):
        if self.eventHandler.is_clicked["left"] and not self.eventHandler.is_lockedc["left"]:
            self.eventHandler.is_lockedc["left"] = True

            mousePos = self.eventHandler.mousePos
            width = self.screen.get_width()
            height = self.screen.get_height()
            if math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 3.5 * width / 10)**2) < self.green_size + 10:
                self.green_size = 65
                self.yellow_size = 50
                self.red_size = 50
            elif math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 5 * width / 10)**2) < self.yellow_size + 10:
                self.green_size = 50
                self.yellow_size = 65
                self.red_size = 50
            elif math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 6.5 * width / 10)**2) < self.red_size + 10:
                self.green_size = 50
                self.yellow_size = 50
                self.red_size = 65
            play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
            if mousePos[0] > play_pos[0] and mousePos[0] < play_pos[0] + self.play_width and mousePos[1] > play_pos[1] and mousePos[1] < play_pos[1] + self.play_height:
                timer.start()
                return states[1]
        if not self.eventHandler.is_clicked["left"]:
            self.eventHandler.is_lockedc["left"] = False

        return self
    def render(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        mousePos = self.eventHandler.mousePos

        if math.sqrt((mousePos[1] - 750) ** 2 + (mousePos[0] - 3.5 * width / 10) ** 2) < self.green_size + 10 and self.green_size == 50:
            self.green_color = (140, 255, 140)
        else:
            self.green_color = (0, 255, 0)
        if math.sqrt((mousePos[1] - 750) ** 2 + (mousePos[0] - 5 * width / 10) ** 2) < self.yellow_size + 10 and self.yellow_size == 50:
            self.yellow_color = (255, 255, 140)
        else:
            self.yellow_color = (255, 255, 0)
        if math.sqrt((mousePos[1] - 750) ** 2 + (mousePos[0] - 6.5 * width / 10) ** 2) < self.red_size + 10 and self.red_size == 50:
            self.red_color = (255, 140, 140)
        else:
            self.red_color = (255, 0, 0)

        pygame.draw.circle(self.screen, (236, 193, 94), (3.5 * width / 10, 750), self.green_size + 10)
        pygame.draw.circle(self.screen, self.green_color, (3.5 * width / 10, 750), self.green_size)
        pygame.draw.circle(self.screen, (236, 193, 94), (width / 2, 750), self.yellow_size + 10)
        pygame.draw.circle(self.screen, self.yellow_color, (width / 2, 750), self.yellow_size)
        pygame.draw.circle(self.screen, (236, 193, 94), (6.5 * width / 10, 750), self.red_size + 10)
        pygame.draw.circle(self.screen, self.red_color, (6.5 * width / 10, 750), self.red_size)

        play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
        if play_pos[0] < mousePos[0] < play_pos[0] + self.play_width and play_pos[1] < mousePos[1] < play_pos[1] + self.play_height:
            self.screen.blit(self.play_button_hovered, (play_pos))
        else:
            self.screen.blit(self.play_button, (play_pos))

class GameState(State):
    def __init__(self, screen, eventHandler):
        super().__init__(screen, eventHandler)
        self.clickCard = card.ClickCard(screen, eventHandler)
        self.sliceCard = card.SliceCard(screen, eventHandler)
        self.mathCard = card.MathCard(screen, eventHandler)
        self.rememberCard = card.RememberCard(screen, eventHandler)
        self.minefieldCard = card.MinefieldCard(screen, eventHandler)
        self.rightCard = card.RightCard(screen, eventHandler)
        self.impossiblequizCard = card.ImpossiblequizCard(screen, eventHandler)
        self.notclickbuttonCard = card.NotclickbuttonCard(screen, eventHandler)
        self.messageCard = card.MessageCard(screen, eventHandler)
        self.labyrinthCard = card.LabyrinthCard(screen, eventHandler)
        self.cards = [self.rightCard, self.minefieldCard, self.rememberCard, self.mathCard, self.sliceCard, self.clickCard,  self.impossiblequizCard, self.notclickbuttonCard, self.messageCard, self.labyrinthCard]
        self.interface = pygame.image.load("res/interface.png")

        self.cards_left = len(self.cards)
        self.current_card = self.cards[self.cards_left - 1]
        self.holding_card = None
        self.cardcounter = 1

    def tick(self, states):
        super().tick(states)
        timer.tick()
        wincheck = self.current_card.tick()

        if wincheck:
            self.correct()
            self.holding_card = self.current_card
            self.cards_left -= 1
            self.current_card = self.cards[self.cards_left - 1]
            self.cardcounter += 1
        elif wincheck == False:
            self.wrong()

        if self.holding_card is not None:
            self.holding_card.tick()

        if self.cards_left == 0:
            timer.stop()
            return states[2]
        return self
    def render(self):
        super().render()
        time = timer.time
        if time > 1000:
            time = str(int(time))
        else:
            time = str(int(time * 10) / 10)
        timetxt = pygame.font.SysFont("segoescript", 75).render(time, True, "Red")
        cards_lefttxt =  pygame.font.SysFont("segoescript", 75).render(str(self.cards_left), True, "Red")
        self.screen.blit(self.interface, (250, 37.5/2))
        self.current_card.render(self.cardcounter)
        self.screen.blit(timetxt, (400, 75))
        if self.cards_left < 10:
            self.screen.blit(cards_lefttxt, (1150, 75))
        else:
            self.screen.blit(cards_lefttxt, (1100, 75))
        if self.holding_card is not None:
            self.holding_card.render(self.cardcounter - 1)

class EndState(State):
    def __init__(self, screen, eventHandler):
        super().__init__(screen, eventHandler)

    def tick(self, states):
        return self
    def render(self):
        self.screen.fill("White")
        time = timer.time

        txt = pygame.font.SysFont("segoescript", 75).render("You Win", True, "Green")
        timetxt = pygame.font.SysFont("segoescript", 75).render(str(int(time * 10) / 10), True, "Black")
        self.screen.blit(txt, (self.screen.get_width()/2 - txt.get_width()/2, self.screen.get_height()/2 - txt.get_height()/2))
        self.screen.blit(timetxt, (self.screen.get_width() / 2 - txt.get_width() / 2, self.screen.get_height() / 2 + txt.get_height() / 2))
