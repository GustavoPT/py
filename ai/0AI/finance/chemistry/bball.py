import turtle 
import tensorflow as tf 
from keras.models import Sequential 
from keras.layers import Dense 

# model = Sequential()
# model.add(Dense(units=64,activation='relu',input_dim=100))
# model.add(Dense(units=10,activation='softmax'))

# model.compile(loss='categorical_crossentropy',
#               optimizer='sgd',
#                 metrics=['accuracy'])

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = -2
ball.dx = 2

gravity = 0.1 

while True:
    ball.dy -= gravity 
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -300:
        ball.dy *= -1

    if ball.xcor() < -300:
        ball.dy *= -1

        
wn.mainloop()