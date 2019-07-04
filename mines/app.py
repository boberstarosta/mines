
from mines import graphics
from mines.menu import Menu


class App:
    def __init__(self, window):
        self.window = window
        window.push_handlers(self)
        self.current_state = Menu(self)
    
    def on_draw(self):
        self.window.clear()
        graphics.batch.draw()

