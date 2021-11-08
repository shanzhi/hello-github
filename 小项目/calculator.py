#demo_calculator
from tkinter import *
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.flag = 0
    def initWidgets(self):
        self.show=Label(relief=SUNKEN,font=('Courier New',24),width=25,bg='white',anchor=E)
        self.show.pack(side=TOP, pady=10)
        self.p = Frame(self.master)
        self.p.pack(side=TOP)
        names=("0","1","2","3","4","5","6","7","8","9","+","-","*","/",".","=")
        for i in range(len(names)):
            b=Button(self.p,text=names[i],font=('Verdana',20),width=6)
            b.grid(row=i // 4, column=i % 4)
            b.bind('<Button-1>', self.click)
    def click(self, event):
        if(event.widget['text'] != '='):
            self.show['text'] = self.show['text'] + event.widget['text']
            self.flag = 0
        elif(event.widget['text']=='='):
            if(self.flag==1):
                self.show['text']=''
            else:
                self.flag=1#先设flag是为了下一行出错（如输入01+2）方法直接返回时也能使用双击=消值功能
                self.show['text']=str(eval(self.show['text']))#使用eval函数计算表达式的值并显示
root = Tk()
root.title("柴器")
App(root)
root.mainloop()
