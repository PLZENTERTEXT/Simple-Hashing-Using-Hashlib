#Program to generate hashes of string data using 3 algorithms from hashlib library (MD5, SHA-256, SHA-512)
import hashlib

string = str(input("Please enter your input: "))

encoded = string.encode()
#encode() converts the string into bytes to be acceptable by hash function
result1 = hashlib.md5(encoded)
result2 = hashlib.sha256(encoded)
result3 = hashlib.sha512(encoded)

print("Your Input: ", string)
print("MD5 Hexadecimal Equivalent : ", result1.hexdigest())
print("SHA-256 Hexadecimal Equivalent : ", result2.hexdigest())
print("SHA-512 Hexadecimal Equivalent : ", result3.hexdigest())
#hexdigest() for hexadecimal format, digest() for byte format