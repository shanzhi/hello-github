import pgzrun

TITLE = "柴——————星"
def draw():
   screen.fill("white")
   screen.draw.circle((350,300),200,"black")
   screen.draw.circle((260, 200), 50, "black")
   screen.draw.circle((410, 200), 50, "black")
   screen.draw.filled_circle((240, 200), 30, "black")
   screen.draw.filled_circle((390, 200), 30, "black")
   screen.draw.filled_circle((335, 350), 15, "red")
   screen.draw.filled_circle((335, 430), 35, "green")


pgzrun.go()