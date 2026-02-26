word = input("enter the word to search")
with open("SampleText","r") as infile,open("SampleText.txt","w") as outfile:
    for line in infile:
        if word in line.lower():
            outfile.write(line)

print("successful")

