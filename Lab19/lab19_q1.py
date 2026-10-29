a=[i for i in range(1,51)]
print(a)

# Slicing with positive step:
# 2,3,4,5
# start=1 stop=5 step=1
# 4,6,8,10,12,14,16,18,20
# start=3 stop=20 step=2
# 1,3,5,7,9,......43.47,49
# start=0 stop=50 step=2
# 1,2,3,4,5,6,7,.....48,49,50
# start=0 stop=50 step=1
# 11,13,15,17,.......47,49
# start=10 stop=50 step=2
# []
# start=1 stop=1 step=1
# []
# start=0 stop=0  step=1
# 44,45,46,47,48,49,50
# start=43 stop=50 step=1
# 45,46,47,48,49,50
# start=44 stop=50 step=1
# 41,42,43,44,45,46
# start=40 stop=46 step=1

print(a[1:5], a[3:20:2], a[::2], a[::], a[10::2], a[1:1:1], a[:0:], a[-7::1], a[-6:], a[-10:-4], sep="\n")

# Slicing with negative step:
# 50,49,48,....3,2,1
# start=49 stop= before 0 step=-1
# 50,47,44,.....11,8,5,2
# start=49 stop= before 0 step=-3
# 50,48,...4
# start=49 stop=1 step =-2
# []
# start=49 stop=49 step=-1
# 50,49,48,47
# start=49 stop=45 step=-1
# 50,...,2
# start=49 stop=0 step=-1
# []
# start=49 stop=49 step=-1
# []
# start=0 stop=45 step=-1
# 50,49,....,7
# start=49 stop=5 step=-1
# []
# start=2 stop=2 step=-1
# [3]
# start=2 stop=1 step=-1
# 1,.....45
# start=0 stop=45 step=1

print(a[::-1], a[::-3], a[:1:-2], a[-1:-1:-1], a[:-5:-1], a[:0:-1], a[:-1:-1], a[0:-5:-1], a[-1:5:-1], a[2:2:-1], a[2:1:-1], a[0:-5], sep="\n")



#Modification of lists using list slicing:
even_list=a[1::2]
print(f"The list of even numbers: {even_list}")
newlist=[]
for i in a:
    if i<=10: newlist.append(i)
    if i>=35 and i%2==0: newlist.append(i)
