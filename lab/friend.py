numbers = {
    "Harsha":"1234567890",
    "Vardhan":"0987654321",
    "Dracula":"1111111111",
    "Phantom":"2222222222"
}

print("Enter the name of the friend:")
name = input()
if name in numbers:
    print("The phone number of", name, "is", numbers[name])
else:
    numbers[name] = input("Friend not found. Please enter the phone number for " + name + ": ")
    
print(sorted(numbers.items()))