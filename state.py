import pygame
import math
import card

class State:
    failcounter = 0
    def __init__(self, screen, eventHandler, timer, cardLoader, soundLoader):
        self.screen = screen
        self.eventHandler = eventHandler
        self.cardLoader = cardLoader
        self.soundLoader = soundLoader

        self.light = False
        self.alpha = 0
        self.color = "Green"
        self.surface = pygame.Surface((screen.get_width(), screen.get_height()))
        self.timer = timer
        self.start = None

    def tick(self, states):
        duration = 0.4*self.timer.fps
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
    def __init__(self, screen, eventHandler, timer, cardLoader, soundLoader):
        super().__init__(screen, eventHandler, timer, cardLoader, soundLoader)
        self.play_button = pygame.image.load("res/play_button.png")
        self.play_button_hovered = pygame.image.load("res/play_button_hovered.png")
        self.logo = pygame.image.load("res/logo_finalized.png")
        self.button = "Green"
        self.lock = True
        self.textfont = pygame.font.SysFont("segoescript", 25)
        self.text1 = self.textfont.render("All ON", True, "Red")
        self.text2 = self.textfont.render("Music OFF", True, "Red")
        self.text3 = self.textfont.render("All OFF", True, "Red")

        self.play_width = 750
        self.play_height = 150

        if soundLoader.running and soundLoader.sfx["wrong"].get_volume() > 0:
            self.button = "Green"
            self.green_size = 65
            self.yellow_size = 50
            self.red_size = 50
        elif not soundLoader.running and soundLoader.sfx["wrong"].get_volume() > 0:
            self.button = "Yellow"
            self.green_size = 50
            self.yellow_size = 65
            self.red_size = 50
        if not soundLoader.running and soundLoader.sfx["wrong"].get_volume() == 0:
            self.button = "Green"
            self.green_size = 50
            self.yellow_size = 50
            self.red_size = 65
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
                self.button = "Green"
                self.lock = False
            elif math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 5 * width / 10)**2) < self.yellow_size + 10:
                self.green_size = 50
                self.yellow_size = 65
                self.red_size = 50
                self.button = "Yellow"
                self.lock = False
            elif math.sqrt((mousePos[1] - 750)**2 + (mousePos[0] - 6.5 * width / 10)**2) < self.red_size + 10:
                self.green_size = 50
                self.yellow_size = 50
                self.red_size = 65
                self.button = "Red"
                self.lock = False
            play_pos = (width / 2 - self.play_width / 2, 11 * height / 20 - self.play_height / 2)
            if mousePos[0] > play_pos[0] and mousePos[0] < play_pos[0] + self.play_width and mousePos[1] > play_pos[1] and mousePos[1] < play_pos[1] + self.play_height:
                return states[1]
            if self.button == "Green" and not self.lock:
                self.soundLoader.play()
                self.soundLoader.set_volume()
            if self.button == "Yellow" and not self.lock:
                self.soundLoader.stop()
                self.soundLoader.set_volume()
            if self.button == "Red" and not self.lock:
                self.soundLoader.stop()
                self.soundLoader.mute_volume()
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

        self.screen.blit(self.logo, (width/2 - self.logo.get_width()/2, 30))

        self.screen.blit(self.text1, (3.5 * width / 10 - self.text1.get_width()/2, 750 + 80))
        self.screen.blit(self.text2, (width / 2 - self.text2.get_width()/2, 750 + 80))
        self.screen.blit(self.text3, (6.5 * width / 10 - self.text3.get_width()/2, 750 + 80))

class GameState(State):
    def __init__(self, screen, eventHandler, timer, cardLoader, soundLoader):
        super().__init__(screen, eventHandler, timer, cardLoader, soundLoader)
        self.interface = pygame.image.load("res/interface.png")
        self.started = False

        self.cards_left = 20
        self.current_card = self.cardLoader.loadcard(0, self.screen, self.eventHandler, self.timer)
        self.next_card = self.cardLoader.loadcard(1, self.screen, self.eventHandler, self.timer)
        self.holding_card = None
        self.cardcounter = 1

    def tick(self, states):
        if not self.started:
            self.timer.start()
            self.started = True
        super().tick(states)
        self.timer.tick()
        wincheck = self.current_card.tick()

        if wincheck:
            self.soundLoader.playSound("correct")
            self.correct()
            self.holding_card = self.current_card
            self.cards_left -= 1
            self.cardcounter += 1
            self.current_card = self.next_card
            if self.cards_left > 1:
                self.next_card = self.cardLoader.loadcard(self.cardcounter, self.screen, self.eventHandler, self.timer)
        elif wincheck == False:
            State.failcounter += 1
            self.soundLoader.playSound("wrong")
            self.wrong()

        if self.holding_card is not None:
            self.holding_card.tick()

        if self.cards_left == 0:
            self.timer.stop()
            return states[2]
        return self
    def render(self):
        super().render()
        time = self.timer.time
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
    def __init__(self, screen, eventHandler, timer, cardLoader, soundLoader):
        super().__init__(screen, eventHandler, timer, cardLoader, soundLoader)
        self.endscreen = pygame.image.load("res/endscreen_update_update.png")

    def tick(self, states):
        return self
    def render(self):
        self.screen.blit(self.endscreen, ((1600 - self.endscreen.get_width()) / 2, (900 - self.endscreen.get_height()) / 2))
        time = self.timer.time

        failstxt = pygame.font.SysFont("segoescript", 75).render(str(self.failcounter), True, "Red")
        timetxt = pygame.font.SysFont("segoescript", 75).render(str(int(time * 10) / 10), True, "Black")
        self.screen.blit(timetxt, (9 * self.screen.get_width() / 20 - timetxt.get_width() / 2 - 20, self.screen.get_height() / 2 - timetxt.get_height() / 2 + 170))
        self.screen.blit(failstxt, (3 * self.screen.get_width() / 5 - failstxt.get_width() / 2 + 3,
                                   self.screen.get_height() / 2 - failstxt.get_height() / 2 + 170))
