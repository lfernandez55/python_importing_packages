#these files duplicate the functionality described in
#https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html


import string_func.stringToLower
import string_func.stringToUpper

some_string = "Hello, Universe!"


print(string_func.stringToLowerFunc(some_string))
print(string_func.stringToUpper.stringToUpperFunc(some_string))
