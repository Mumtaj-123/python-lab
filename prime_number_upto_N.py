a=int(input("Enter the number upto  print prime number"))

print("The prime number are here:")
for val in range(2,a+1): 
        
   if val > 1: 
       for a in range(2, val): 
           if (val % a) == 0: 
               break
       else: 
           print(val,end=" ")
