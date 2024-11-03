#Write a program to find the factorial using recursive function
def factorial(x):
    if x==0 or x==1:
        return 1
    else: 
        return x*factorial(x-1)
x=int(input("enter a number"))
print(factorial(x))
