text = input("Enter a string: ")
pattern = input("Enter a pattern to search: ")

for i in range(len(text)-len(pattern)+1):
    if pattern == text[i:i+len(pattern)]:
        print(f"Pattern found at index {i}")