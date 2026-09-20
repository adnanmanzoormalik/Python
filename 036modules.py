# NOTE: calculator_036.py >>> revise from that file also
# MODULES: python files containing code that can be used in another file

import math #built-in module
print(math.sqrt(25)) # .  means go inside the calculator module and access add


#we have created calculator_036.py as a module >>> user defined module
import calculator_036

print(calculator_036.add(1, 3)) 
print(calculator_036.sub(4, 3))


#when we want only a few things from a module we can do
from calculator_036 import add
print(calculator_036.add(1,2))


from math import sqrt, pi, factorial
print(math.pi)
print(math.sqrt(36))
print(math.factorial(5))


#Alias >>> An alias is another name you give to a module.

import math as m
print(m.sqrt(4))

import calculator_036 as cal
print(cal.add(4,6))


#Different types of modules

# 1. Built-in / Standard Library Modules >>> this is provided by python e.g math, datetime, random, json etc etc
import random
print(random.randint(1,10))

# 2. Third Party Modules >>> These are created by other developers/organizations and are installed separately, usually using pip. e.g pandas, numpy, flask etc
#pip install requests
#import requests

# 3. User-defined Modules >>> these are created by us like we created calculator_036.py




#dir() >>> inspecting a module >>> It lets you see the names available inside an object/module.
print(dir(math))
print(dir(calculator_036)) 


#help() >>> to get documentation of a module
print(help(math))
print(help(math.factorial))
print(help(calculator_036))
print(help(calculator_036.add))


import calculator_036 #when we import something in python we run the whole python module
print(calculator_036.add(1,2))

# __name__ >>>  if we run a file directly it will give "__main__" in return but if we run it indirectly lets say in a module it ll give the module_name like calculator_036
# __main__ means this is the file/program Python is currently executing directly.
#NOTE: revise calculator_036.py



#Module Search Path — sys.path
import calculator_036 #when we write this python searches through a list of directories called: sys.path Python searches locations in sys.path. If the directory containing calculator.py is available in the search path, Python can find it. If Python can’t find the module, you’ll get: ModuleNotFoundError
import sys
print(sys.path) #useful when you’re trying to understand where Python looks for modules.



#Python comes with a large collection of modules called the Standard Library. (Built-in Modules)
#math, random, sys, os, json


import math
print(math.sqrt(25)) #square root
print(math.isqrt(25)) #integer square root >>> without a decimal
print(math.ceil(4.3)) #rounds upwards
print(math.floor(4.7)) #rounds downwards
print(math.floor(-2.3))
print(math.trunc(-2.3)) #removes decimal
print(math.pow(2,3)) #2^3 exponents
print(math.factorial(4)) #factorial
print(math.pi) #constant pi value
print(math.e) #constant e value
# print(abs(-1)) >>> gives absolute value of an integer
print(math.fabs(-1.0)) #abs value of a float




import random
print(random.randint(1,100)) #prints random number between 1 and 100 including 1 and 100
print(random.random()) #prints random values between 0 and 1 
print(random.uniform(1, 2)) #prints a float value between 1 and 2 inclusive

list = ["banana", "apple", "mango", "cherry", "grape"]
print(random.choice(list)) #picks a random object from the list
print(random.choices(list, k=3)) #picks 3 random objects and object can be repeated
print(random.sample(list, k=3)) #picks 3 random objects and object cant be repeated

print(list)
random.shuffle(list) #rearranges the list in a random order
print(list)

# random.seed(1)## Will always produce the exact same number on first call 
# print(random.randint(1,100))  #NOTE: understand it again




import datetime

now = datetime.datetime.now() #prints the current date and time
print(now)
print(now.date())
print(datetime.datetime.now().date()) #this is same as above
print(now.time())

date = datetime.date(2025, 9, 20) #creating a specific date
print(date)

#timedelta
from datetime import timedelta
next_week = now + timedelta(days=7)
earlier = now - timedelta(hours=12)
print(now)
print(next_week)
print(earlier)




# The os module lets Python interact with the operating system.
import os 

print(os.getcwd()) #gives current working directory
print(os.listdir()) #gives list of files and folders
print(os.path.exists("035data.txt")) #we can check whether a file exists 




#sys provides information and functionality related to the Python interpreter/system.
import sys

print(sys.version) #>>>prints python version
print(sys.path) #>>>prints python search path




# JSON is extremely important in web development, APIs, and data storage. JSON >>> JavaScript object notation
import json
data = {
    "name": "Adnan",
    "age": 22,
    "skills": ["Python", "C++"]
}

json_data = json.dumps(data) #Convert Python data into a JSON string.
print(json_data)
# print(json_data["age"]) #this will throw an error becoz it is a json string not a python directory

data_py = json.loads(json_data) #Converts JSON string into python data 
print(data_py)
print(data_py["age"])