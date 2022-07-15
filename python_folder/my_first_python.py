# Python Basics
from ast import Try
import math
import time as t 
import os 
import module_example as mE
print('Hello World')

"""
This is a multiline comment
Check it out
"""
if 10 < 20:
    print("10 is less than 20")
name = input("What is your name = ")
age = 19
print(f"{name} is your name and {age} is your age")
print(name + " is your name and " + str(age) + " is your age")
print(type(age))
print(math.ceil(3.2))
print(math.floor(3.2))
mE.welcome(name)

try:
    print(x)
except:
    print("x doesn't exist.")