import vrep
import tkinter as tk
import cv2 
import keras 

class robot:
    pass 

class arm:
    pass 
class leg:
    pass 

#inhereit from the arm and the leg 
# building the robot robotics 
# making the robot move 
# making the plan 
# putting the circuits together 
# matrix 

positions = []
arms = []
vision =[]

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1',19000,True,True,5000,5)

if clientID != -1:
    print("Connected to remote api")
else:
    print("Connection not successful")