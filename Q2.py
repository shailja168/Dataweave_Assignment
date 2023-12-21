def countCodeFreq(data):
    codeCount = {}
    for key in data:
        for val in key.values():
            if val in codeCount:
                codeCount[val] += 1
            else:
                codeCount[val] = 1
    return codeCount

data = []
n = int(input("Enter the number of items: "))
for i in range(n):
    key, value = map(int, input(f"Enter key and code for item {i+1} separated by a space: ").split())
    data.append({key: value})

print("Frequency of each code:", countCodeFreq(data))
