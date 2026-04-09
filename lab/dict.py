dict1 = {
    "name":"Harsha",
    "age": None,
    "city":"Secret"
}
print(dict1)

dict1["name"] = "Harsha Vardhan"
print(dict1.keys())
print(dict1.values())
print(dict1.items())

del dict1["age"]
print(dict1)

for n,c in dict1.items():
    print(n,":",c)