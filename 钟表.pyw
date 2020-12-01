from tkinter import *
from datetime import datetime
from time import sleep
from math import *
from threading import *

wx = 400
wy = 400
unit = 10
runstatus = True

window = Tk()
cav = Canvas(width = wx, height = wy, bg = 'black')
cav.pack()

def drawLine(theta, r, color = 'white', tag = 'line', width = 2, arrow = 'last', base = (wx / 2, wy / 2)):
    x = r * cos(theta) * unit + base[0]
    y = -r * sin(theta) * unit + base[1]
    cav.create_line(base[0], base[1], x, y, fill = color, tag = tag, width = width, arrow = arrow)
    return

def drawText(theta, r, text, color = 'white', tag = 'text', base = (wx / 2, wy / 2)):
    x = r * cos(theta) * unit + base[0]
    y = -r * sin(theta) * unit + base[1]
    cav.create_text(x, y, text = text, fill = color, tag = tag)
    return

def runClock():
    zero = pi / 2
    shour = zero
    sminute = zero
    ssecond = zero

    while runstatus:
        now_time = datetime.now()
        hour = zero - (now_time.hour % 12) * pi / 6
        minute = zero - (now_time.minute % 60) * pi / 30
        second = zero - (now_time.second % 60) * pi / 30

        if not hour == shour:
            shour = hour
            cav.delete('hour')
            drawLine(hour, 5, width = 10, color = 'blue', tag = 'hour')
        
        if not minute == sminute:
            sminute = minute
            cav.delete('minute')
            drawLine(minute, 7, width = 5, color = 'pink', tag = 'minute')
        
        if not second == ssecond:
            ssecond = second
            cav.delete('second')
            drawLine(second, 10, color = 'yellow', tag = 'second')
        
        cav.update()
        sleep(1)
    return

def drawClock():
    theta = pi / 2
    step = pi / 6
    for i in range(1, 13):
        theta -= step
        drawText(theta, 12, str(i), 'white')
    return

def close():
    window.destroy()
    exit()
    return

if __name__ == '__main__':
    drawClock()
    t = Thread(target = runClock, daemon = True)
    t.start()
    window.protocol('WM_DELETE_WINDOW', close)
    window.mainloop()