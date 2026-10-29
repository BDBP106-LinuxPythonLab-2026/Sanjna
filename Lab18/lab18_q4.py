#extract key whose value has most unique values
D= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
l=0
for key, value in D.items():
    if l<len(set(value)):
        l=len(set(value))
        uniq_key=key
print(uniq_key)
