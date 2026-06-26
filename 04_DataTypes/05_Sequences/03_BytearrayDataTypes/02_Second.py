# Defining bytearray data type

# way-1
data = bytearray()
print(data) # bytearray(b'')
print(type(data)) # <class 'bytearray'>

# way-2
data = bytearray(b"")
print(data) # bytearray(b'')

# way-3 with a specific size
data = bytearray(5)
print(data)  # bytearray(b'\x00\x00\x00\x00\x00')
print(len(data))  # 5

for i in range(len(data)):
    print(data[i])
    # Result-->
    #             0
    #             0
    #             0
    #             0
    #             0

# assigning
data[0] = 35  # Note 35 decimal in ASCII is #
print(data) # bytearray(b'#\x00\x00\x00\x00')

# here data[0] is modified with 1
for i in range(len(data)):
    data[i] = i+1
print(data) # bytearray(b'\x01\x02\x03\x04\x05')


# Using multiplication
data = bytearray(4)
data[0] = 4
data = data*5
print(data) # bytearray(b'\x04\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00')
for i in range(len(data)):
    print(data[i])
    # Result -->
    #             4
    #             0
    #             0
    #             0
    #             4
    #             0
    #             0
    #             0
    #             4
    #             0
    #             0
    #             0
    #             4
    #             0
    #             0
    #             0
    #             4
    #             0
    #             0
    #             0

data = bytearray(b"A") *3
print(data) # bytearray(b'AAA')
print(len(data)) # 3

for i in range(len(data)):
    print(data[i])
    # result -->
    #             65
    #             65
    #             65