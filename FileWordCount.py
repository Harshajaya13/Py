word_to_search = input("Enter the word to search: ")

with open("SampleText.txt", "r") as f:
    content = f.read()

words = content.split()
count = words.count(word_to_search)

print("Occurrences:", count)
