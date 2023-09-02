from pygame import mixer

class Soundloader:
    def __init__(self):
        self.volume = 1
        self.sfx_volume = 3
        self.sfx = {
            "wrong": mixer.Sound("sounds/wrong.wav"),
            "correct": mixer.Sound("sounds/correct.mp3")
        }
        mixer.Sound.set_volume(self.sfx["wrong"], 0.07 * self.sfx_volume)
        mixer.Sound.set_volume(self.sfx["correct"], 0.2 * self.sfx_volume)
        mixer.music.load("sounds/marching.mp3")

    def play(self):
        mixer.music.set_volume(0.3 * self.volume)
        mixer.music.play(-1, 0.1, 100)
    def stop(self):
        mixer.music.fadeout(100)


    def playSound(self, sound):
        self.sfx[sound].play()