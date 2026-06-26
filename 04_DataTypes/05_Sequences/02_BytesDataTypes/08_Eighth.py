# Hash functions work with bytes.
import hashlib
data = b"hello"
hash_value = hashlib.sha256(data)
print(hash_value.hexdigest())# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# The hash algorithm processes raw bytes.



# What is hashlib?
# hashlib stands for Hash Library.
# It provides functions for creating cryptographic hashes such as:
# MD5
# SHA1
# SHA224
# SHA256
# SHA384
# SHA512

# You can see what's available
print(hashlib.algorithms_available)
# {'sha512', 'sha512_224', 'sha224', 'sha1', 
#  'md5', 'sha3_512', 'sha3_224', 'shake_128', 'sha512_256', 
#  'sha3_384', 'blake2b', 'shake_256', 'sha384', 'ripemd160', 
#  'sm3', 'blake2s', 'md5-sha1', 'sha3_256', 'sha256'}



# 3. hashlib.sha256(data)
# What is SHA-256?
# SHA-256 stands for:
# Secure Hash Algorithm 256-bit
# It converts any data into a fixed-size fingerprint.
# No matter how large the input is:

# 5 bytes
# 5 MB
# 5 GB
# SHA-256 always produces:
# 256 bits = 32 bytes