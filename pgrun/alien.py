import pgzrun

TITLE = "Alien walk"
alien = Actor('alien')
WIDTH = 666
HEIGHT = alien.height + 88

def draw(): 
    screen.clear()  
    alien.draw()

def update():  
    """Move the alien by one pixel."""  
    alien.x += 1
    if alien.left > WIDTH:     
        alien.right = 0

def on_mouse_down(pos):   
    if alien.collidepoint(pos):# 碰撞   
        set_alien_hurt()

def set_alien_hurt():    
    alien.image = 'alien_hurt' 
    sounds.ah.play() 
    clock.schedule_unique(set_alien_normal, 1.0)# 送终

def set_alien_normal():  
    alien.image = 'alien'

pgzrun.go()
