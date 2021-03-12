from processing_py import *
app = App(600,400) # create window: width, height
x =100 
y = 100 
xspeed = 1
yspeed = 3



while(True):
   app.background(0,0,0) # set background:  red, green, blue
   app.fill(255,255,0) # set color for objects: red, green, blue
   app.ellipse(app.mouseX,app.mouseY,50,50) 
   app.fill(0,0,255)
   app.ellipse(49,49,50,50)
   app.fill(255,0,0)
   app.ellipse(60,60,50,50)
   # draw a circle: center_x, center_y, size_x, size_y
   x = x + xspeed 
   y = y + yspeed 
   app.redraw() # refresh the window