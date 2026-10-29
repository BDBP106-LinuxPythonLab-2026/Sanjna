#interchange even and odd components of an input list
#L=[23,32,33,44,'BDBH101','hello','python', 15, 1e-10, True,'hit']
L=[0,1,2,3,4,5,6,7,8]

for i in range(0,len(L)):
    if i%2!=0:
        L[i],L[i-1]=L[i-1],L[i]

print(L)

