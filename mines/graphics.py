
import pyglet


pyglet.resource.path = ["./data"]
pyglet.resource.reindex()

img_covered = pyglet.resource.image("covered.png")
img_pressed = pyglet.resource.image("pressed.png")
img_flag = pyglet.resource.image("flag.png")
img_mine = pyglet.resource.image("mine.png")
img_values = [pyglet.resource.image("{}.png".format(i)) for i in range(10)]
img_btn_normal = pyglet.resource.image("btn_normal.png")
img_btn_pressed = pyglet.resource.image("btn_pressed.png")

group_back = pyglet.graphics.OrderedGroup(0)
group_front = pyglet.graphics.OrderedGroup(1)

batch = pyglet.graphics.Batch()

