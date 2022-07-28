import random
def slicelist(n,arr):
    #reverse list
    if n>=8 and n<=50:
        arr1=arr[::-1]
       
        
        
        for i in range(1,n):
            
            if i%3==0 :
                o=arr[i]+3
                arr1.insert(n,o)
                n+=1
            if i%5==0:
                x=arr[i]-7
        
        print(" ".join(map(str,arr1)))
        print(x)
        print(sum(arr[3:8]))

        

def getlist():
    '''n=random.randint(8,50)
    arr=[random.randint(-100,100) for i in range(n)]'''
    n=int(input())
        #print("enter list")
    arr=[int(i) for i in input().split()]
    
    return n,arr
if __name__ == '__main__':
    try:
        testcase=int(input())
        arr=[]
        for i in range(1,testcase+1):
            n,arr=getlist()
            
            slicelist(n,arr)



    except EOFError as e:
        pass
    ''' #stree testing
    while True:
        testcase=random.randint(1,25)
        arr=[]
        for i in range(1,testcase+1):
            n,arr=getlist()
            
            slicelist(n,arr)'''