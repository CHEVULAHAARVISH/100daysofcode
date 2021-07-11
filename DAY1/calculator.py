def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print('''Select an operation \n
    1.Addition\n
    2.Subtraction\n
    3.Multiplication\n
    4.Division\n''')
z=int(input("Select an operation from 1,2,3,4:"))
if z==1 or z==2 or z==3 or z==4:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))

    if z==1:
        print(a, "+", b, "=",add(a,b))
    elif z==2:
        print(a, "-", b, '=',subtract(a,b))
    elif z==3:
        print(a, '*', b, '=',multiply(a,b))
    elif z==4:
        if b!=0:
            print(a, '/', b, '=',division(a,b))
        else :
            print('We cannot divide a number with zero')

else:
    print("Please give valid input")
