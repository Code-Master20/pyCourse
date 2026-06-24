# If you want the number of bits needed to represent an integer value
# (not the actual memory used by the Python object),
# use bit_length().

# bit_length() returns the minimum number of bits required
# to represent the value in binary, excluding the sign bit.

x = 90
print(x.bit_length())  # 7

# 90 in binary is 1011010, which requires 7 bits.
# bit_length() returns the minimum number of bits needed
# to represent the value.
# It does NOT mean Python allocates only 7 bits of memory
# for the integer object.