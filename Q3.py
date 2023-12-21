def delDuplicateNames(data):
    names = set()
    uniqueData = []
    for d in data:
        if d["name"] not in names:
            names.add(d["name"])
            uniqueData.append(d)
    return uniqueData

data =[]
n = int(input("Enter the number of items: "))
for i in range(n):
    name = input(f"Enter name for item {i+1}: ")
    age = int(input(f"Enter age for item {i+1}: "))
    data.append({"name": name, "age": age})

print(delDuplicateNames(data))