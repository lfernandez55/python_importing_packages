#importing from another module
from bar import bar_1
#importing from a package (notice I'm basically specifying the path and filename of a module)
import baz.boo

#a locally defined function
def foo_1():
    print("executing foo_1 function")

#calling the locally defined function
foo_1()

#calling a function in an imported "bar" module
bar_1()

#calling a function in the module boo in the imported "baz" package
baz.boo.boo_1()

#calling a function in the imported baz package in a more succinct way then above
#I can do this because I've included "from .boo import boo_1" in the __init__.py file.  If I had left
# the __init__.py file blank I couldn't call the function this succinctly
baz.boo_1()
