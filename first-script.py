# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 1
a

import pandas as ps


def hello():
    """Print "Hello World" and return None."""
    print("Hello World")

# Main program starts here
hello()


i = 42

hello(i)

a = ("a", "b", "c")

test = 7

test - 5

#Number py calculations
import numpy

a = [1, 2, 3]

#creates a numpy array
b = numpy.array(a)

#adds 10 to the 2nd and third numbers of the array
b[1:3] += 10

#other array functions
a = numpy.array([1, 2, 3, 4]) 
#subtracs every number in teh array

#Using dictionaries with keys and come back here
a = {'banana':1, 'horse':2, 19:1, 3:'cookie'}

print(a['banana'])

#adding a value to a dict variable
a['answer'] = 42 

a
# Classes

# working with functions

def hello_world(N):
    print(N * 'Hello World!')

hello_world(10)

# Defining a function
def is_this_the_answer(number):
    result = number == 42
    return result
    
    
 is_this_the_answer(67)
 
 #Making Visual NOise
 
 #Enter Random Numbers
 import numpy
 
#Seeds will create the same random numbers
 numpy.random.seed(seed=14)
 
 #create a 5X5 arrary of random numbers
 noise = numpy.random.rand(5, 5)
 noise
 
 #Check the shape of the noise array
 
 #noise is the object, and shape is the attribute
 noise.shape
 
 #Creating rgb coordinates of visual noise
 #This creates 5 5X3 arrays
 rgb_noise = numpy.random.rand(5, 5, 3)
 print(rgb_noise)
 
 #Creating a grpahical image of random noise
 import numpy
 from matplotlib import pyplot
 
 #create random noise
 #create noise array
 noise = numpy.random.rand(500, 500, 3)
#creating a plot to show the noise
pyplot.imshow(noise) 
#show in interactive window
pyplot.show()


#################### Chapter 3 ################################SS
 import WinPython
 
 
 
 
 
 
 
 
 
 
 
