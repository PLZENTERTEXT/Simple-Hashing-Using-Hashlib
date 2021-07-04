#Program to add salting and iterations to hashes
import hashlib
import uuid
'''
UUID (Universal Unique Identifier) - Currently only supports generating Variant 1,
Type 4 UUIDs, which are random bit strings
'''

count = 0
iteration = True

string = str(input("Please enter your input: "))

count = int(input("How many iterations would you want to do: "))
if (count == 1):
    iteration = False

encoded = string.encode()
#encode() converts the string into bytes to be acceptable by hash function
result1 = hashlib.md5(encoded)
result2 = hashlib.sha256(encoded)
result3 = hashlib.sha512(encoded)

salt = uuid.uuid4().hex

hex1 = result1.hexdigest() + salt
hex2 = result2.hexdigest() + salt
hex3 = result3.hexdigest() + salt
#hexdigest() for hexadecimal format, digest() for byte format

if ((count >= 1) and (iteration == True)):
    for final in range(count-2):
        md5 = hashlib.md5(hex1.encode())
        sha256 = hashlib.sha256(hex2.encode())
        sha512 = hashlib.sha512(hex3.encode())

        final1 = md5.hexdigest()
        final2 = sha256.hexdigest()
        final3 = sha512.hexdigest()
    print("Your Input: ", string)
    print("Iteration made to hash: " + str(count))
    print("MD5 with salt : ", final1)
    print("SHA-256 with salt : ", final2)
    print("SHA-512 with salt : ", final3)
else:
    print("Your Input: ", string)
    print("Iteration made to hash: 1")
    print("MD5 with salt : ", hex1)
    print("SHA-256 with salt : ", hex2)
    print("SHA-512 with salt : ", hex3)
    

# OR
# """f-string"""
# print(f"Your Input: {string}")
# print(f"MD5 with salt: {result1.hexdigest()}{salt}")
# print(f"SHA-256 with salt: {result2.hexdigest()}{salt}")
# print(f"SHA-512 with salt: {result3.hexdigest()}{salt}")