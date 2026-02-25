name = "Harsha"
sub = "ars"

for i in range(len(name)-len(sub)+1):
    if (name[i:i+len(sub)] == sub):
        print(i)

#advanced
print(name.find(sub))

