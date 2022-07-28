def star(rows):
    for i in range(rows + 1, 0, -1):    
        for j in range(1, i ):  
            if j%5==0:
                print("#", end=' ')
            else:
                print("*", end=' ')
        print()  

if __name__ == '__main__':
    try :
        testcase=int(input())
        arr=[]
        if 1<= testcase <=25:
            for i in range(testcase):
                n=int(input())
                if 1<=n<=100 :

                    arr.append(n)
                else :
                    print("ERROR")
            for i in range(len(arr)):
                star(arr[i])
    except EOFError as e:
        print(e)

