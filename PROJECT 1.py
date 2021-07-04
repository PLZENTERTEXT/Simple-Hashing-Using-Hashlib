# Program to generate MD5 of string data
import hashlib

string = str(input("Please enter your input: "))

encoded = string.encode()
# encode() converts the string into bytes to be acceptable by hash function
result = hashlib.md5(encoded)

print("Your Input: ", string)
print("Hash Value : ", result)
print("Hexadecimal Equivalent : ", result.hexdigest())
# hexdigest() for hexadecimal format, digest() for byte format
