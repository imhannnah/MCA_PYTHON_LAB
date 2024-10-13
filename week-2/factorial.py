n=int(input("Enter First Number: "))
fact=1
if n<0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1,1):
        fact=fact*i
    print("the factorial of",n,"is",fact)
