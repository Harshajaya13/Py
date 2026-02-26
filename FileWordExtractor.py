keyword = input("Enter the substring")
with open("SampleText.txt","r") as f:
    content = f.read()

words = content.split()
for word in words:
    if keyword in word:
        print(word)
