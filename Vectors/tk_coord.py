# !/usr/bin/python3
from tkinter import *
import math
root = Tk()

xn = 750
yn = 750
step = 50
xlc = ((xn/step)%2)*step/2
ylc = ((yn/step)%2)*step/2


c = Canvas(root, width=xn+10, height=yn, bg='white') # Размер и цвет холста
c.pack()


# Вісь X
c.create_line(0, yn/2, xn, yn/2, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

# Вісь Y
c.create_line( xn/2, yn, xn/2, 3, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

# Проміжні лінії
for i in range(max(int(xn/step),int(yn/step))):
    c.create_line(0, i*step+ylc, yn, i*step+ylc)
    c.create_line(i*step+xlc, 0, i*step+xlc, yn)

# Підпис координат
for y in range(max(int(xn/step),int(yn/step))):
    for x in range(int(xn/step)):
        c.create_text(xn+22+(x-int(xn/step))*step+xlc, 0+yn-10+(y-int(yn/step))*step+ylc, text=f"({x-int(xn/step/2)};{-y+int(yn/step/2)})",
                    justify=LEFT, font="Verdana 8")

# Функція для малювання вектору
def vector(x1,y1,x2,y2):
    c.create_line(xn/2+x1*step, yn/2-y1*step, xn/2+x2*step, yn/2-y2*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    
def vector_calc(x1,y1,x2,y2):
    #Малюємо вектор
    vector(x1,y1,x2,y2)
    #Створюємо прямокутник-підкладку під текст
    c.create_rectangle(xn-350, yn-20, xn, yn,outline="#fb0",fill="#ddd")
    # Робимо обрахунки
    modulo = math.sqrt((x2-x1)**2+(y2-y1)**2)
    cos_a = (x2-x1)/modulo
    cos_b = (y2-y1)/modulo
    # Виводимо текст на прямокутник-підкладку
    c.create_text(xn-350, yn, text=f"|a| = {format(modulo, '.3f')}, cos_a = {format(cos_a, '.3f')}, cos_b = {format(cos_b, '.3f')}",
                    anchor=SW, font="Verdana 8")