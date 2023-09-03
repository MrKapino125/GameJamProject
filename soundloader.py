from pygame import mixer

class Soundloader:
    def __init__(self):
        self.volume = 1
        self.sfx_volume = 1
        self.sfx = {
            "wrong": mixer.Sound("sounds/wrong.wav"),
            "correct": mixer.Sound("sounds/correct.mp3")
        }
        mixer.Sound.set_volume(self.sfx["wrong"], 0.065 * self.sfx_volume)
        mixer.Sound.set_volume(self.sfx["correct"], 0.20 * self.sfx_volume)
        mixer.music.load("sounds/background.wav")
        mixer.music.set_volume(0.02 * self.volume)
        self.running = False

    def play(self):
        if self.running:
            return
        self.running = True
        mixer.music.play(-1, 0.1, 100)
    def stop(self):
        if not self.running:
            return
        self.running = False
        mixer.music.fadeout(100)
    def set_volume(self):
        mixer.Sound.set_volume(self.sfx["wrong"], 0.065 * self.sfx_volume)
        mixer.Sound.set_volume(self.sfx["correct"], 0.20 * self.sfx_volume)
    def mute_volume(self):
        mixer.Sound.set_volume(self.sfx["wrong"], 0)
        mixer.Sound.set_volume(self.sfx["correct"], 0)
    def playSound(self, sound):
        self.sfx[sound].play()
