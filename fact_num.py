
i=int(input("Enter your number"))

def factorial(j):
    if j==0:
        return 1
    else:
        return j*factorial(j-1)

print("The factorial of {0} is {1}".format(i,factorial(i)))
