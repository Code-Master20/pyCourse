# bytes objects are immutable, which means you cannot add, remove, or modify individual bytes after creation.

# Can you append to a bytes object?
# Not directly. But you can create a new bytes object by concatenating:
data = b""
newData = bytes([67])
data +=newData
print(data) # b'C'

# data is b''
# bytes([67]) creates b'C'
# data + b'C' creates a new bytes object
# data is reassigned to that new object