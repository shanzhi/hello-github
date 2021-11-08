import pgzrun

WIDTH = 500
HEIGHT = 100
TITLE = "fading green"
c = 0

def draw():
    screen.fill((0,c,0))

def update():
    global c, HEIGHT
    c = (c+1) % 256
    if c == 255:
        HEIGHT += 10

def on_mouse_down(button, pos):
    print(button, pos)

pgzrun.go()