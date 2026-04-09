start = int(input("Start: "))
end = int(input("End: "))

result = [(x, x**2) for x in range(start, end+1)]

print(result)