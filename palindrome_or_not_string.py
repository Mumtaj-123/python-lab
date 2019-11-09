a=input("Enter the string:")

b=reversed(a)

if list(a)==list(b):
    print("{0} is a palindrome string".format(a))
else:
    print("{0} is not a palindrome string".format(a))
