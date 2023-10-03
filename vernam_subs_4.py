# substitutiom cipher ==> vernam cipher is a po;y alphabetic cipher 
print("Welcome to Verman's Substitution Algorithm ")
print("-"*40)
print("**NOTE: The Key Length should match the plain text ")
plain_text=input("Enter the Plain Text : ")

key=input("Enter the Key : ")

temp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

store=""

for i in range(len(key)):
    store+=temp[((ord(plain_text[i])-65)+(ord(key[i])-65))%26]

print(store)

# decryption = ct-key 

store2=""

for i in range(len(key)):
    store2+=temp[(26+(ord(store[i])-65)-(ord(key[i])-65))%26]

print(store2)