def getUniqueNames(string_list):
    lowercase = [s.lower() for s in string_list]
    uniqueNames = set(lowercase)
    sentencecase = [s.capitalize() for s in uniqueNames]
    return sentencecase

string_list = []
n = int(input("Enter number of strings : "))
print("Enter the strings:")
for i in range(0, n):
    string_list.append(input())
output = getUniqueNames(string_list)
print("Expected Output:", output)
