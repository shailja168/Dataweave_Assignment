def generateFile(urlList, zipcodeList):
    for zipcode in zipcodeList:
        output = [{"url": f"{url}#{zipcode}", "zip": zipcode} for url in urlList]
        filename = f"{zipcode}_input.txt"
        
        with open(filename, 'w') as file:
            for data in output:
                file.write(str(data) + '\n')

urlList = []
n = int(input("Enter number of urls : "))
print("Enter the urls separated by ENTER:")
for i in range(0, n):
    urlList.append(input())

zipcodeList = []
m = int(input("Enter number of zipcode : "))
print("Enter the zipcodes separated by ENTER:")
for i in range(0, m):
    zipcodeList.append(input())

generateFile(urlList, zipcodeList)
