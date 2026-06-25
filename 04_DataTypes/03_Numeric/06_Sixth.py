# Binary Number Representation
# prefix -> 0b || 0B
# example -> 0b10101001, 0B110110

# Octal Number Representation
# prefix -> 0x || 0X
# example -> 0xA180 , 0X11fb91

# Hexadecimal Number Representation
# prefix -> 0o || 0O
# example -> 0o773, 0O145

# type casting (implicit) || type coercion
x = 15.56
result = int(x)
print(result) # 15

y = 19
result = float(y)
print(result) # 19.0

z = 10
result = complex(z)
print(z) # 10 because 10 + 0j == 10
p,q=10,15
result = complex(p,q)
print(result) # (10+15j)
