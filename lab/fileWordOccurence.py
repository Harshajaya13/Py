word_to_count = input("Enter the word to count: ")

with open("sampletext.txt","r") as file:
    contents = file.read()
    
words = contents.split()
count = words.count(word_to_count)
print("occurence of the word is: ", count)