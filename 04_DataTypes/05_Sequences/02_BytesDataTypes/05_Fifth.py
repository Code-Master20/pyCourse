# 2. Network Communication
# When sending data over the internet, data is transmitted as bytes

message = "Hello"
data = message.encode("utf-8")
print(data) # b'Hello'
print(len(data)) # 5
print(type(data)) # <class 'bytes'>
for i in range(len(data)):
    print(data[i])
# 72 --> H
# 101 -->e
# 108 -->l
# 108 -->l
# 111 -->o