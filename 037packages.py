# Package = folder of related Python modules, A package is a directory used to organize modules.
#A traditional package looks like this 
#  my_package/
    # ├── __init__.py #NOTE: study it later and how is diff than __main__.py
    # ├── module1.py
    # └── module2.py


#first way to import
import calculator_037.basic
print(calculator_037.basic.add(1,2))

import calculator_037.advance
print(calculator_037.advance.square(3))


#second way to import
from calculator_037 import basic
print(basic.add(1,2))


from calculator_037 import advance, basic #we can import various modules together
print(advance.cube(3))
print(basic.add(3,8))



#third way >>> we can do even deeper
from calculator_037.basic import add
print(add(1,9))

from calculator_037.advance import square, cube
print(square(10))
print(cube(10))



#using alias
import calculator_037.basic as bas
print(bas.add(1,8))

from calculator_037 import basic as b
print(b.add(2,3))

from calculator_037.basic import add as a
print(a(1,98))


# Installing Third-Party Packages with pip
#suppose we want to use requests, we will install it using >>> pip install requests (in terminal) then in python we use >>> import requests
# suppose we want to install a specific version of requests >>> pip install requests==2.32.3
#or a minimum version >>> pip install requests>=2.30
#pip is Python’s package installer. It allows you to install packages created by other developers. like pandas, numpy, requests etc etc
#we can check installed packages using >>> pip list (in the terminal)
#You can also inspect a particular package: >>> pip show requests

