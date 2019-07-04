#!/usr/bin/env python3

import pyglet


window = pyglet.window.Window(caption="Mines")
batch = pyglet.graphics.Batch()


@window.event
def on_draw():
    window.clear()


pyglet.app.run()

