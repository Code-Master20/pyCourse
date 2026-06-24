# Different values treated as False with bool-function evaluation
print(bool(None))      # False
print(bool(False))     # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(set()))     # False