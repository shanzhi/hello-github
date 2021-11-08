import pgzrun

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 600
HEIGHT = alien.height + 8

def draw():
    screen.clear()
    alien.draw()
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):#碰撞
        set_alien_hurt()
def set_alien_normal():
    alien.image = 'alien'
def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.ah.play()
    clock.schedule_unique(set_alien_normal, 1.0)#调用（安排-唯一）

pgzrun.go()
