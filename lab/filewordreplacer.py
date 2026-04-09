oldword = input("Enter the oldword: ")
newword = input("Enter the new word: ")

with open("sampletext.txt","r") as file:
    content = file.read()

updated_content = content.replace(oldword, newword)

with open("sampletext.txt","w") as file:
    f.write(updated_content)
    
print("Word replacement completed.")
