def greet():
    pass

result = greet()

print(result) # None
print(bool(result)) # False || None result evaluates as False

# Note:- A function without a return statement automatically returns None.