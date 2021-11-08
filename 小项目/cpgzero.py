from cpgzero import *#一招鲜  未成功

UP = "up"#能说得是————无言
DOWN = "down"
LEFT = "left"
RIGHT = "right"

RED = "red"
GREEN = "green"
BLACK = "black"

CELLSIZE = 40#抽象大法好
#人之初 玄之又玄
startx = 0
starty = 0
snakeCoords = [{"x":startx,"y":starty},
               {"x":startx-CELLSIZE,"y":starty},
               {"x":startx-2*CELLSIZE,"y":starty}]

allPosPoints = []    
def getRandomPosPoints():#任性收割
    getAllPosPoints()
    point = random.randint(0,len(allPosPoints)-1)
    return allPosPoints[point]
def getAllPosPoints():#收豆（点）
    if len(allPosPoints)==0:
        for x in range(-640,640,CELLSIZE):
            for y in range(-480+CELLSIZE,480+CELLSIZE,CELLSIZE):#不越界
                allPosPoints.append({"x":x,"y":y})


def drawCell(coord,color):#绘格子（坐标）
    x = coord["x"]
    y = coord["y"]
    cellRect = Rect((x,y),(CELLSIZE,CELLSIZE))

def drawSnake(snakecoords):#绘🐍
    for coord in snakeCoords:
        drawCell(coord,GREEN)

def snakeMove(snakeCoords):#背包客
    if direction == RIGHT:#软脑
        newHead = {"x":snakeCoords([HEAD]["x"]+CELLSIZE),"y":snakeCoords([HEAD]["y"])}
    elif direction == LEFT:
        newHead = {"x":snakeCoords([HEAD]["x"]-CELLSIZE),"y":snakeCoords([HEAD]["y"])}
    elif direction == UP:
        newHead = {"x":snakeCoords([HEAD]["x"]),"y":snakeCoords([HEAD]["y"+CELLSIZE])}
    elif direction == DOWN:
        newHead = {"x":snakeCoords([HEAD]["x"]),"y":snakeCoords([HEAD]["y"]-CELLSIZE)}
    snakeCoods.insert(0,newhead)#正常点的
    if snakeCoods[HEAD]["x"]==bean["x"] or snakeCoods[HEAD]["y"]==bean["y"]:
        bean = getRandomPosPoint()#有豆吃豆
        drawCell(bean,RED)
    else:#换缺点什么--撞南墙，自摸
        del snakeCoords[TAIL]
        drawCell(snakeCoords[TAIL],BLACK)#洗屁屁


flag = 0
def update():
    drawSnake(snakeCoords)
    snakeMove(snakeCoords)
    global flag 
    flag += 1
    if flag%5 != 0:#减速带
        return


def on_key_down(key):
    global direction
    if key == keys.LEFT and direction != RIGHT:
        direction = LEFT#说NO 勿直接变向
    elif key == keys.RIGHT and direction != LEFT :
        direction = RIGHT
    elif key == keys.UP and direction != DOWN:
        direction = UP
    elif key == keys.DOWN and direction != UP:
        direction = DOWN
