from tkinter import *

def printHello():
    print('Hi!')

root=Tk() #tkinter 활성화

w=Label(root, text='Python Test') #root에 라벨 달기
b=Button(root, text='Hello Python',command=printHello) #root에 button달기
c=Button(root, text='Quit',command=root.quit)

w.pack() #감싸주는 명령어
b.pack()
c.pack()

root.mainloop()
