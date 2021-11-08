import pgzrun

TITLE = "五环"
def draw():
   screen.fill("white")
   screen.draw.circle((60,60),30,"blue")
   screen.draw.circle((135,60), 30, "black")# 2*60+15
   screen.draw.circle((210,60), 30, "red")
   screen.draw.circle((105,90), 30, "yellow")#60+30+15
   screen.draw.circle((180,90), 30, "green")


pgzrun.go()