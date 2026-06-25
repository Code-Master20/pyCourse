b_yte = [65,66,67,68,69,70,71,72,73,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
b_yte = bytes(b_yte)
print(b_yte) # b'ABCDEFGHIIJKLMNOPQRSTUVWXYZ'
# A is 65 dec in ascii
# B is 66 dec in ascii
# C is 67 dec in ascii
# and so on


for i in range(len(b_yte)):
    print(b_yte[i])
# Result --> 65
#            66
#            67
#         and so on

b_yte = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
b_yte = bytes(b_yte) 
print(b_yte) # b'abcdefghijklmnopqrstuvwxyz'


# Empty Bytes Creating ways
#  ways-1 : with method bytes()
b_yte = bytes()
print(b_yte) # b''

# ways-2 : with 0 mentioned
b_yte = bytes(0)
print(b_yte) # b''

# ways-3 : with bytes literal
b__yte = b""
print(type(b__yte)) # <class 'bytes'>

# bytes with specific size
b_yte_ = bytes(2)
print(b_yte_) # b'\x00\x00' || items are two: 0,0

for i in range (len(b_yte_)):
    print(b_yte_[i])

# Result --> 
#           0
#           0