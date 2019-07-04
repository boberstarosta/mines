
import pyglet
from mines import graphics


class Button:
    def __init__(self, x, y, text, action):
        self.x = x
        self.y = y
        self.action=action
        self.sprite = pyglet.sprite.Sprite(
            graphics.img_btn_normal,
            x=x, y=y,
            batch=graphics.batch,
            group=graphics.group_back
        )
        self.label = pyglet.text.Label(
            x = x + self.sprite.width/2,
            y = y + self.sprite.height/2,
            anchor_x = "center",
            anchor_y = "center",
            text = text,
            font_size = 14,
            batch = graphics.batch,
            group = graphics.group_front
        )
    
    def __del__(self):
        self.sprite.delete()
        self.label.delete()
    
    def contains(self, x, y):
        rx = x - self.x
        ry = y - self.y
        return rx >= 0 and rx <= self.sprite.width and ry >= 0 and ry <= self.sprite.height
            
    def press(self):
        self.sprite.image = graphics.img_btn_pressed
    
    def release(self):
        self.sprite.image = graphics.img_btn_normal
    
    def click(self):
        if self.action is not None:
            self.action()


class Menu:
    def __init__(self, app):
        self.app = app
        self.label = pyglet.text.Label(
            x = app.window.width/2,
            y = 100,
            anchor_x = "center",
            text = "Choose difficulty",
            font_size = 20,
            group = graphics.group_front,
            batch = graphics.batch
        )
        self.buttons = [
            Button(10, 10, "Very easy", lambda: print("Very easy")),
            Button(148, 10, "Easy", lambda: print("Easy")),
            Button(286, 10, "Medium", lambda: print("Medium")),
            Button(424, 10, "Hard", lambda: print("Hard")),
            Button(562, 10, "Ridiculous", lambda: print("Ridiculous"))
        ]
        self.pressed_btn = None
        pyglet.gl.glClearColor(0.4, 0.5, 0.6, 1.0)
        app.window.push_handlers(self)
    
    def __del__(self):
        self.app.window.remove_handlers(self)
        self.label.delete()
    
    def get_button(self, x, y):
        for button in self.buttons:
            if button.contains(x, y):
                return button
        return None
    
    def on_mouse_press(self, x, y, buttons, modifiers):
        if buttons & pyglet.window.mouse.LEFT:
            self.pressed_btn = self.get_button(x, y)
            if self.pressed_btn is not None:
                self.pressed_btn.press()
    
    def on_mouse_release(self, x, y, buttons, modifiers):
        if buttons & pyglet.window.mouse.LEFT:
            released_btn = self.get_button(x, y)
            if released_btn is not None:
                if released_btn is self.pressed_btn:
                    released_btn.click()
            if self.pressed_btn is not None:
                self.pressed_btn.release()

