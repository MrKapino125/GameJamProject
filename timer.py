import time

class Timer():
    def __init__(self):
        self.ticking = False
        self.start_time = None
        self.time = None

    def start(self):
        self.ticking = True
        self.start_time = time.time()
        self.time = 0

    def stop(self):
        self.ticking = False

    def tick(self):
        if self.ticking:
            self.time = time.time() - self.start_time