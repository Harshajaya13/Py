name = input("Enter the name")
occur = {}

for i in name:
    if i in occur:
        occur[i] +=1 
    else:
        occur[i] = 1

print(occur)


#advanced way
name2 = input("enter the name")
count= {}
for i in name2:
    count[i] = count.get(i,0)+1

print(count)
