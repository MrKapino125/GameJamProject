class State:
    def __init__(self):
        self.s_lock = False
    def tick(self, eventHandler, states):
        pass
    def render(self, screen):
        pass

class MenuState(State):
    def __init__(self):
        super().__init__()
    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["s"] and not self.s_lock:
            print("eichel")
            self.s_lock = True
        if not eventHandler.is_pressed["s"]:
            self.s_lock = False
        if eventHandler.is_pressed["a"]:
            return states[1]
        return self
    def render(self, screen):
        pass

class GameState(State):
    def __init__(self):
        super().__init__()

    def tick(self, eventHandler, states):
        if eventHandler.is_pressed["s"] and not self.s_lock:
            print("vulva")
            self.s_lock = True
        if not eventHandler.is_pressed["s"]:
            self.s_lock = False
        if eventHandler.is_pressed["d"]:
            return states[0]
        return self
    def render(self, screen):
        pass