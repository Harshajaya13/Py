text = input("Enter a string: ")
occurrences = {}

for char in text:
    if char in occurrences:
        occurrences[char] += 1
    else:
        occurrences[char] = 1
        
print(occurrences)