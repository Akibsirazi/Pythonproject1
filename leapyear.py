year=int(input("Enter the year:"))
if(year%100==0 and year % 400==0):
  print("Entered year{} is a leap year".format(year))
elif(year%4==0 and year% 100!=0):
  print("Entered year{} is a leap year ".format(year))
else:
  print("Entered year {} is not a leap year".format (year))


