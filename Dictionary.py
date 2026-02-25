
friends = {
    "harsha":"123456789",
    "jaya":"987654321",
    "dracula":"999999999"
}
print(friends)
name = input("enter the name:")
if name in friends:
    print("phone number:",friends[name])
else:
    number = input('enter the number')
    friends[name] = number
    for name in sorted(friends):
        print(name,friends[name],sep=":")



