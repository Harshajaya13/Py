text = input("Enter a string: ")
pattern = input("Enter a pattern to search: ")
count=0

for i in range(len(text)-len(pattern)+1):
    if pattern == text[i:i+len(pattern)]:
        count+=1
        
print(count)