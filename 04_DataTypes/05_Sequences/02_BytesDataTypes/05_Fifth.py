# 2. Network Communication
# When sending data over the internet, data is transmitted as bytes

# UTF-8 is a character encoding standard that converts human-readable text (characters) into bytes so computers can store and transmit it.

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



data = b'Hello'
text = data.decode("utf-8")
print(text) # Hello
print(type(text)) # <class 'str'>