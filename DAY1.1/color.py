#color
print("WHICH COLOR U WANT")

def color():
    if i==1:

        x=print('VIOLET')
    elif i==2:
        x=print("INDIGO")
    elif i == 3:
        x=print("BLUE")
    elif i==4:
        x=print('GREEN')
    elif i==5:
        x=print("YELLOW")
    elif i==6:
        x=print("ORANGE")
    elif i==7:
        x=print("RED")
    else:
        x=print("INVALID INPUT")
    return(x)

if __name__ == '__main__':
    i=int(input("CHOOSE ONE NUMBER FROM 1 TO 7 :"))
    color()

