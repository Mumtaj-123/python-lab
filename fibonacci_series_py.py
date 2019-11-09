a=int(input("Enter the number upto your sereis will go:"))

b=0
c=1
print("Your fibonacci series is:")
for i in range(0,a):
    print(b,end=" ")
    d=b+c
    b=c
    c=d
