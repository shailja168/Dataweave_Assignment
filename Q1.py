def intersect(list1, list2):
    list3 = []
    for i in list1:
        if i in list2 and i not in list3:
            list3.append(i)
    return  list3


list1 = []
n1 = int(input("Enter size of list1 : "))
if(n1):
    print("Enter elements of list1")
    for i in range(0, n1):
        list1.append(int(input()))

list2 = []
n2 = int(input("Enter size of list2 : "))
if(n2):
    print("Enter elements of list2")
    for i in range(0, n2):
        list2.append(int(input()))

print("Intersection of the two lists:", intersect(list1, list2))
