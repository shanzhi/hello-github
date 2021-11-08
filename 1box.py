import pgzrun

WIDTH = 300
HEIGHT = 300


def draw():#唯一不变的是一直在变
    r = 255#练就对了
    g = 0
    b = 0

    width = WIDTH
    height = HEIGHT - 200

    for i in range(20):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))

        r -= 10
        g += 10

        width -= 10
        height += 10

pgzrun.go()