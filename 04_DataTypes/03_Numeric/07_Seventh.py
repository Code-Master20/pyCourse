# convert octal, binary, hexa into 10 base decimal
num1 = 0o17 #Octal base 8
num2 = 0b111010 # binary base 2
num3 = 0x1c2 # hexa base 16

num1_deci = int(num1)
print("Octal 0o17 = ",num1_deci) # 15
num2_deci = int(num2)
print("Binary 0b111010 = ",num2_deci) # 58
num3_deci = int(num3)
print("Hexadecimal 0x1c2 = ",num3_deci) # 450