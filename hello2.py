# perform xor and AND for hello world with 127 and display ouput 

s="hello world"

for i in s:
    print(i,"^ 127",chr(ord(i)^127))

print("***"*20)

for i in s:
    print(i,"& 127",chr(ord(i)&127))

print("---"*20)
