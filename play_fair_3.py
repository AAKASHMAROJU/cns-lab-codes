# play fair cipher 

# 5x5 matrix 

def getindex(a):
    for i in range(5):
        for j in range(5):
            if a in matrix[i][j]:
                return [i,j]

def is_same_row(x,y):
    return x[0]==y[0]

def is_same_col(x,y):
    return x[1]==y[1]

key='abhi'
matrix=[['a','b','h','ij','c'],['d','e','f','g','k'],
        ['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]
plaintext='bmfgqw' #ergkrv

cipher=""

for i in range(0,len(plaintext),2):
    a,b=plaintext[i],plaintext[i+1]
    x=getindex(a)
    y=getindex(b)
    if is_same_row(x,y):
        cipher+=matrix[x[0]][(x[1]+1)%5]+matrix[y[0]][(y[1]+1)%5]
    elif is_same_col(x,y):
        cipher+=matrix[(x[0]+1)%5][x[1]]+matrix[(y[0]+1)%5][y[1]]
    else:
        cipher+=matrix[x[0]][y[1]]+matrix[y[0]][x[1]]

print(cipher)