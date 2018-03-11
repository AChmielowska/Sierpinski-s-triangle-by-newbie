import tkinter
import math
from random import randint
def  draw (point):
    canvas.create_oval(point['x'], point['y'], 
    point['x'], point['y'], 
    width = 3,
    fill = 'green')

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()
a=200
points=[{'x':80, 'y':200}, 
    {'x':80+a, 'y':200}, 
    {'x':80+a/2, 'y':200-a*math.sqrt(3)/2}]
for point in points:
   draw(point)

first=points [randint(0,2)]
second=points [randint(0,2)]

x=(first['x']+second['x'])/2
y=(first['y']+second['y'])/2
current={'x':x, 'y':y}

draw (current)

root.mainloop()
