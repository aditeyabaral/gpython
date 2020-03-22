import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg,FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
def exit():
    root.destroy()
    import Main
import matplotlib.pyplot as plt
from math import *
add = 0
s = str(input("Enter function : ")) #Inputs function
temp = s
s= s.replace('x','(x)')
ctr, x, y = -10, [], [] #Setting countert to starting values and x,y to empty lists
while ctr<=10:
        s1 = ''
        add = 0
        x.append(ctr)
        s1 = s.replace('x',str(ctr)) #Replaces variable with value at that point
        try:
                add = eval(s1) #Tries to evaluate function at that point, if defined
                y.append(add)
        except:
                y.append(None) #If beyond domain, append None
        ctr+=0.1
root = Tk.Tk()
root.config(bg='WHITE')
root.wm_title("Embedding in TK")
'''f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)
a.plot(t, s)
a.set_title('Tk embedding')
a.set_xlabel('X axis label')
a.set_ylabel('Y label')'''
f=plt.figure(num ='GPYTHON')
plt.plot(x,y,label = 'y = '+temp,color = 'black')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
#plt.title(temp.upper())
#plt.style.use('ggplot')
ax = plt.gca()
plt.grid(True)
plt.legend(bbox_to_anchor=(1.1, 1.05))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
button = Tk.Button(master=root, text='Quit', command=exit)
button.pack(side=Tk.BOTTOM)
root.mainloop()
