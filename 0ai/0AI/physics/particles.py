import turtle
import tkinter as tk
from tkinter import filedialog 
from tkinter import ttk 
from tkinter import * 

# check how to draw 3 circles in tkinter of 3 diff colors 

def forward():
    t.forward(100)

def back():
    t.back(100)

def left():
    t.left(90)

def right():
    t.right(90)

def somewhere():
    print("somerher")

def askopenfile(self):
    return fileDialog.askopenfile(mode='r', **self.file_opt)

def dance():
    print("dance")

def submit():
    print("I want to submit this")

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()
# file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')

# if file != None:
#     data = file.read()
#     file.close()
#     print("I got %d bytes from this file." % len(data))

t = turtle.RawTurtle(canvas)
# t.pencolor("#ff0000") # Red
# t.circle(50)
# t.penup()
# t.setposition(-120,0)
# t.pendown()
# t.color("blue")
# t.circle(70)
# t.setposition(120,0)
# t.color("green")
# t.circle(50)
# t.circle(80)
# t.circle(90)

t.penup()   # Regarding one of the comments
t.pendown() # Regarding one of the comments

tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)
tk.Button(master=root,text="Somewhere",command=somewhere ).pack(side=tk.LEFT)
tk.Button(master=root,text='Browse',command=askopenfile).pack(side=tk.LEFT)
tk.Button(master=root,text="Dance",command=dance).pack(
    side=tk.LEFT
)
tk.Entry(root).pack(
    side=tk.LEFT
)
tk.Button(master=root,text="Submit",command=submit).pack(
    side=tk.LEFT
)

root.mainloop()