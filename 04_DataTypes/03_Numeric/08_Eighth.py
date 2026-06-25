# Program to convert into decimal number system with a base mentioned

# if you are not writing with prefix , you have to mention as string [ num1 = "1c2" ]
# num1 = 1c2  #incorrect representation

# TypeError: int() can't convert non-string with explicit base
# num1 = 0x1c2
# num1_deci = int(num1, 16)
# print(num1)

#Correct way to convert other number system into decimal number system with a base mentioned

# Hexadecimal to decimal
num1 = "1c2"
num1_deci = int(num1, 16)
print(num1_deci) #450

#Binary to decimal
num2 = "11100101"
num2_deci = int(num2, 2)
print(num2_deci) # 229

#Octal to Decimal
# rage = 0, 1, 2, 3, 4, 5, 6, 7
num3 = "76"
num3_deci = int(num3, 8)
print(num3_deci) # 62
