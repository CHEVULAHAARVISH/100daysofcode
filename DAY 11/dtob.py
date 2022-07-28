def dtob(n):
    if n > 1:
       dtob(n//2)
    print(n % 2,end = '')

if __name__ == '__main__':
    try:
        testcase=int(input())
        arr=[]
        for i in range(testcase):
            n=int(input())
            arr.append(n)
        print(arr)
        for i in range(len(arr)):
            dtob(arr[i])
    except EOFError as e:
        pass
