#prediction
from random import randrange
print("LETS PLAY PREDICTION GAME")
print("I AM ROLLING DICE WHAT IS YOUR PREDICTION?")
i=int(input("MY PREDICTION IS:"))
x=randrange(1,7)
print("DICE ENDEDUP WITH",x)
if i==x:
    print("YOU WON AND PREDICTION IS RIGHT")
else:
    print("YOU LOST")



