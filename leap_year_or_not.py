
x=int(input("Enter the your desired Year:"))

if x%100:
      if x%400:
          print("{0} is a leap year".format(x))
      else:
          print("{0} is not a leap year".format(x))

else:
      if x%4:
          print("{0} is a leap year".format(x))
      else:
          print("{0} is not a leap year".format(x))
