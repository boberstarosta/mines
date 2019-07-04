#!/usr/bin/env python3

import pyglet
import mines.app


window = pyglet.window.Window(caption="Mines", width=800, height=800)
app = mines.app.App(window)
pyglet.app.run()

