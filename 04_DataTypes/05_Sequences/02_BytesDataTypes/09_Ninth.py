# Converting integer into bytes

num = 1024

data = num.to_bytes(2, byteorder="big")
# If byteorder is 'big',
#   the most significant byte is at the beginning of the byte array. If
#   byteorder is 'little', the most significant byte is at the end of the
#   byte array. To request the native byte order of the host system, use
#   sys.byteorder as the byte order value. Default is to use 'big'.
# signed

print(data) # b'\x04\x00'

# Understanding to_bytes()
# to_bytes() is an instance method of the int class.
# integer.to_bytes(length, byteorder)
# it returns a bytes object
# length -->"Store this integer using exactly 2 bytes."

# Internally
# 1024 in binary--> 10000000000
# fill 16 bits-->   0000010000000000
# divide into two bytes--> 00000100  00000000
# convert into decimal--->    4          0
# so the two bytes [4,0]

# in memory for big [4], [0]
# in memory for little [0], [4]
data = num.to_bytes(2, byteorder="little")
print(data) # b'\x00\x04'