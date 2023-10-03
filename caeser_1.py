# caeser cipher encryption and decryption 

# caser cipher ==> shift cipher / additive cipher 
# mono alphabetic cipher a->x then a -> x always 
# key = 3 
# pt abcd 
# ct defg ==> a+3= 0+3=4 ==> d

#   cti=(pti+key)%26;

# if i assume that a=0 z=25 

print("Welocme to Caeser Cipher - Additive Cipher - Shift Cipher ")
print("-"*60)

key=int(input("Enter the Key : "))

plaintxt=input("Enter the Plain text :  ")


ciphertxt=""


temp="abcdefghijklmnopqrstuvwxyz"


for i in plaintxt:
    curr_val=ord(i)-97
    new_val=(curr_val+key)%26
    ciphertxt+=temp[new_val]



print("The Cipher Text is : ",ciphertxt)