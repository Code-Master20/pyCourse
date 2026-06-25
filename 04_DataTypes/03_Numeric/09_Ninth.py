# Decimal number systems into binary number system
num1 = 97
num1_bin = bin(num1)
print(num1_bin) # 0b1100001

# Octadecimal number system into binary number system
num1 = 0o67
num1_bin = bin(num1)
print(num1_bin) # 0b110111

#Hexadecimal number system into binary number system
num = 0X7c5
num_bin = bin(num)
num_deci = int(num)
print(num_deci) # 1989
print(num_bin) # 0b11111000101


# Binary number system into Octa decimal number system
num = 0B111001010
num_deci = int(num)
num_oct = oct(num)
print(num_deci) # 458
print(num_oct) # 0o712

#Hexadecimal number system into Octal Number system
num = 0X76c3
num_deci = int(num)
num_octal = oct(num)
print(num_deci) # 30403
print(num_octal) # 0o73303

#10 Base decimal number system into Octal number system
num = 458
num_octal = oct(num)
print(num_octal) # 0o712