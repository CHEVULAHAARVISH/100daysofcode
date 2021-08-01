# For list of integers
lst1 = []

lst2 = []

lst1 = [int(item) for item in input("Enter the list elements: ").split()]

lst2 = [int(item) for item in input("Enter the list elements: ").split()]

list=lst1+lst2
#APPENDING TWO LIST

def x(lst1, lst2):
    return lst1 + lst2



new= x(lst1, lst2)

#SUM

# add two list
sum = [lst1[i] + lst2[i] for i in range(len(lst1))]
if __name__== "__main__":


    print("Addition of all elements in given lists: ", new)

    print("sum of all elements in given lists: ", sum)
