#线

from tkinter import *

if __name__ == '__main__':
    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x1, y1, width=1, fill='red')
        x0 -= 5
        y0 -= 5
        x1 += 10
        y1 += 5



    mainloop()