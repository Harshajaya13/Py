word = input("Enter the word to search: ")
with open("sampletxt.txt","r") as file,open("copy.txt","w") as copy_file:
    for line in file:
        if word in line:
            copy_file.write(line)