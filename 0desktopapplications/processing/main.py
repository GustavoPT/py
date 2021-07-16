from processing_py import *
app = App(600,400) # create window: width, height


class circle:
    self.__init__():
        pass
     

def drawCircle(app):
    app.fill(197,10,203)
    app.ellipse(60,60,50,50)
def recursiontest():
    pass 
while(True):
   app.background(0,0,0) # set background:  red, green, blue
   app.fill(255,255,0) # set color for objects: red, green, blue
   app.ellipse(app.mouseX,app.mouseY,50,50) 
   app.fill(0,0,255)
   app.ellipse(49,49,50,50)
   app.fill(255,0,0)
   app.ellipse(60,60,50,50)
   drawCircle(app)
   # draw a circle: center_x, center_y, size_x, size_y
   app.redraw() # refresh the window