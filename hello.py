# wap to xor hello world each char with 0 and display ouput 

s="Hello World"


print(chr(97))
print(ord('a'))

for i in s:
    print(i,"^ 0 =",chr(ord(i)^0))

