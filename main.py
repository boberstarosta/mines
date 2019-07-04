#!/usr/bin/env python3

import pyglet
import mines.app


window = pyglet.window.Window(caption="Mines", width=1280, height=960)
app = mines.app.App(window)
pyglet.app.run()

