# Documentation String/Docstring:-
# If we write strings inside """ """ or ''' '''
# and if these strings are written as first statement
# in a module, function, class or method, these strings are called ducumentation strings
# or docstrings


#Program to add two numbers
def Add(x,y):
    '''
    This function adds two numbers.
    It has two parameters
    '''
    print("Sum = ", (x+y))

Add(10,15)


# python -m pydoc -w 01_First
# -w  --> is used to call a pydoc-module
# -w ---> is telling that an html file to be created with 01_First.html
