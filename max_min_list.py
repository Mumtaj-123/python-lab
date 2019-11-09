
MyList=[]
print("to stop the taking input in list press -1\n")
while(1):
  r=int(input("Enter the element in the list:"))
  if(r==-1):
    break
  else:
    MyList.append(r)

print("My list is {0}\n".format(MyList))

s=max(MyList)
f=min(MyList)

print("The max element in list is {0}\n".format(s))

print("The min element in list is {0}".format(f))
  
