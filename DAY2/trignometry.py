#AGE FINDER
import math
print("BASIC TRIGNOMETRY")
print("""CHOOSE ONE NUMBER FROM 1 TO 5 TO KNOW YOUR ANGLE IN:
        1 FOR KNOWING IN SIN
        2 FOR KNOWING IN COS
        3 FOR KNOWING IN TAN
        4 FOR KNOWING IN RADIANS:""")

def trigo():
    if i==1:

        x=print("sin = ",math.sin(z))

    elif i==2:
        x=print("cos = ",math.cos(z))

    elif i == 3:
        x=print("tan = ",math.tan(z))
    elif i==4:
        x=print("degree to radians = ", math.radians(z))
    elif i==5:
        x=print("EXIT")

    else:
        x=print("INVALID INPUT")
    return(x)

if __name__ == '__main__':
    i=int(input("""CHOOSE OPTION:
       """))
    z=int(input("GIVE ANGLE:"))
    trigo()
