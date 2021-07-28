#odd and even numbers
print("LETS FIND SUM OF EVEN AND ODD NUMBERS UNTILL RANGE N")
n=int(input("GIVE RANGE N:"))
even_no=[x for x in range(n) if x%2 == 0]
odd_no=[x for x in range(n) if x%2!=0]
print("ALL EVEN NUMBERS LESS THAN" ,n ,"IS" ,even_no)
ss=sum(even_no)
print('SUM OF EVEN NUMBERS IS :',ss)
print("ALL ODD NUMBERS LESS THAN ",n,"IS",odd_no)
so=sum(odd_no)
print("SUM OF ODD NUMBERS IS :",so)
