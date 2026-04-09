keyword = input("Enter the keyword to search for: ")    
with open("file.txt", "r") as file:
    content =  file.read()
    
words = content.split()
for word in words:
    if keyword in word:
        print(word)