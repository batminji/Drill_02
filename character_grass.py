from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

cnt = 0

x = 400
y = 60
pi = 0

while(True):
    if (cnt == 0):
        x = 400
        y = 60
        while(x < 790 and y == 60):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x + 2
            delay(0.01)
        while(x == 790 and y < 540 ):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y + 2
            delay(0.01)
        while(x > 10 and y == 540):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x - 2
            delay(0.01)
        while (x == 10 and y > 60):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y - 2
            delay(0.01)
        while (x < 400 and y == 60):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x + 2
            delay(0.01)
        cnt = 1

    if (cnt == 1):
        pi = 0
        while(pi<360):
            x = 400 + 200 * math.cos(math.radians(pi))
            y = 300 + 200 * math.sin(math.radians(pi))
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            pi = pi + 2
            delay(0.01)
        cnt = 0

