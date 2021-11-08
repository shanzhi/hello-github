import pygame
def main():
    pygame.init()                               #初始化
    screen=pygame.display.set_mode((1024,640))  #开窗口
    pygame.display.set_caption("tank game")     #定标题
    background=pygame.Surface(screen.get_size())#获大小
    background=background.convert()             #屏幕转像素
    background.fill((100,100,100))              #白色填充
    clock=pygame.time.Clock()                   #开定时器
    running=True                                #运行标志
    while running:                       #主程序大循环
        clock.tick(30)                   #最大每秒30帧
        for event in pygame.event.get(): #检测退出信息
            if event.type==pygame.QUIT:  #如果有的话
                running=False            #更改标志位
        screen.blit(background,(0,0))    #位块传送把背景回到左上角
        #鼠标事件
        buttons=pygame.mouse.get_pressed()          #获鼠标按下事件
        if buttons[0]:print(pygame.mouse.get_pos()) #按左键输出坐标
        #键盘事件
        keys=pygame.key.get_pressed()               #获键盘按下事件
        if keys[pygame.K_SPACE]:print('space')      #按下空格输出space
        #绘图：画矩形（在screen上画，[r,g,b]，[左上角x,y，长，宽]，线宽），线宽取0是填充
        pygame.draw.rect(screen,[255,0,0],[600,600,10,10],0)
        #贴图
        #maps = pygame.image.load('GJL.png')         #获取图片
        #screen.blit(maps,(0,0))                     #贴到screen的左上角
        pygame.display.update()          #更新显示
    pygame.quit()                        #退出游戏
main()