import time

class Timer():
    def __init__(self):
        self.ticking = False
        self.start_time = None
        self.time = 0
        self.fps = 35
        self.frames = 0
        self.delta = 0
        self.deltaTime = 0

    def start(self):
        self.ticking = True
        self.start_time = time.time()
        self.time = 0

    def stop(self):
        self.ticking = False

    def tick(self):
        if self.ticking:
            now = time.time()
            self.delta = self.time
            self.time = now - self.start_time
            self.delta = self.time - self.delta
            self.deltaTime += self.delta
            self.frames += 1
            if self.deltaTime >= 1:
                self.fps = self.frames
                self.frames = 0
                self.deltaTime = 0