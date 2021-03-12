from vpython import *
import tensorflow as tf 
from keras.models import Sequential 
from keras.layers import Dense 
import pygame 

# model = Sequential()
# model.add(Dense(units=64,activation='relu',input_dim=100))
# model.add(Dense(units=10,activation='softmax'))

# model.compiler(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

class PeriodicTable:
    def __init__(self,name):
        pass
    def appendElement(self,element):
        self.elements.append(element)

class PeriodicElement:
    def __init__(self,name,protons,electrons):
        self.name = name
        self.protons = protons
        self.electrons = electrons

class Atom:
    def __init__(self):
        self.name = "atom"
        self.count = 0

    def getCount(self):
        return self.count

class Proton:
    def __init__(self):
        self.count = 12 
        
def atomsMaker():
    atom = 1 
    return atom


# atoms = []

# R = 1
# M = 1
# # Make a ring.
# z = 0
# theta = 0
# ds = 0.1 # Fixed distance between atoms.
# while (theta < 2*pi):
#   atoms.append( sphere(pos=vector(R*cos(theta),R*sin(theta),z),
#                       color=color.red, radius=0.1) )
#   theta = theta + ds/R

# # Draw rotation axis, just for visualization.
# rot_axis = cylinder(pos=vector(0,0,-1),axis=vector(0,0,1),size=vector(2,0.05,0.05))

# # Calculate MOI about z-axis.
# moi = 0
# dm = M/len(atoms)
# for atom in atoms:
#   moi = moi + dm*(atom.pos.x**2+atom.pos.y**2)
# print("moment of inertia=",moi,", or",moi/(M*R**2),"MR^2")
