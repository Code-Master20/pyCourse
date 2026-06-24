# In Python, int does not have a fixed size like C/C++. Python integers can grow as large as memory allows.
# We can check the memory used by a particular integer object using sys.getsizeof():

import sys
x = 90
print(sys.getsizeof(x)) # 28 (bytes)
# 90 in binary 1011010
# so in memory-->
# 0000000000000000000001011010



x = 90**1000
print(sys.getsizeof(x)) # 892 (bytes)