import hashlib

hash_choices = "sha512 or sha256 or md5"
print(f"choices: {hash_choices}")
move = input("choose method of encryption: ")
_encryptor_ = input("input message: ")

if move == "sha512":
    print(f"choice = {move}")
    result = hashlib.sha512(_encryptor_.encode())
    print("The hashed message in hexadecimal format: ", end ="")
    print(result.hexdigest())
elif move == "sha256":
    print(f"choice = {move}")
    result = hashlib.sha256(_encryptor_.encode())
    print("The hashed message in  hexadecimal format: ", end ="")
    print(result.hexdigest())
elif move == "md5":
    print(f"choice = {move}")
    result = hashlib.md5(_encryptor_.encode())
    print("The hashed message in hexadecimal format: ", end ="")
    print(result.hexdigest())
else:
    print("invalid choice")
    while True:
        result = hashlib.sha256()
        print(result.hexdigest())
#there are only 3 options at the moment but will be upgraded
