# Different operations on strings
name = 'Sahidur Miah'

# [] this is slice operator , we can use it to retrieve a piece of string like below shown :--
# [start:end:step]
# end index is excluded
# step 1 is by defult
print(name[0]) # first character of name string || result -> s
print(name[0:])  #0 to last index+1 || result -> Sahidur Miah
print(name[:]) # first to last+1 || resullt -> Sahidur Miah
print(name[0::3]) # 0 to last+1 and skip two chars || result --> Siri
# S  a  h  i  d  u  r     M  i   a  h
# 0  1  2  3  4  5  6  7  8  9  10 11
# i  e  e  i  e  e  i  e  e  i  e  e

print(name[-1]) # The last char of the string || result -> h
reverse_name = name[::-1]  # haiM rudihaS
print(reverse_name)

# * This is repetition operator
name = "Rakibul"
print(name*3) # RakibulRakibulRakibul