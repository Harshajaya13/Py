oldword = input("Enter the oldword")
newword = input("Enter the newword")

with open("SampleText.txt","r") as f:
    content = f.read()

updated_content = content.replace(oldword,newword)

with open("SampleText","W") as f:
    f.write(updated_content)

print("Replacement success")


