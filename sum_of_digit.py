
x=int(input("Enter the number:"))
num=x
sum2=0
while(x!=0):
   n=x%10
   sum2+=n
   x=x//10

print("The sum of digit of {0} is {1}".format(num,sum2))
