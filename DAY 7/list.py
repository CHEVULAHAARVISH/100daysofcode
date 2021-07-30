#list
list1 = []

# asking number of elements to put in list
n = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, n + 1):
    ele = int(input("Enter elements one by one: "))
    list1.append(ele)

# print maximum element
print("Largest element is:", max(list1))
