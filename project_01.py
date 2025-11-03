#Consider the state space for the Blocks World that includes: 
#1. Five blocks (A, B, C, D, E) 
#2. The relations among the blocks (AIR, ON, CLEAR, TABLE) 
#3. Functions (PICK_UP, PUT_DOWN, STACK, MOVE, UNSTACK) performed on the blocks. 

#For the transition from one state to the next state 
#you may use the appropriate functions (actions) logically needed. 
 
#Develop an algorithm that accepts any combination of the five blocks 
#mentioned above as the initial state and any combination of the same five blocks as the goal state. 

#Given both the initial and goal states, your algorithm must generate 
#and display the sequence of scenes (or states) that lead from the initial to the goal state. 
#In other words, each state, after applying each action in your plan, must be visible.  

#The initial and the goal states will be given to you at the demo, 
#and you run your code to prove it at that time in class.

from block import Block
from scene import Scene
from state import State












class block0:
    def __init__(self, name):
        self.name = name

    def AIR(self):
        #not relating to anything
        pass

    def ON(self, block2):
        #self is on block2
        pass
    
    def CLEAR(self):
        #nothing on top of self
        pass

    def TABLE(self, table):
        #self is on table
        pass

        

def PICK_UP(block):
    pass 

def PUT_DOWN(block):
    pass

def STACK(block, block2):
    pass

def MOVE(block, block2):
    pass

def UNSTACK(block, block2):
    pass
