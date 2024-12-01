lowerRange=int(input("Enter the lower Range:"))
upperRange=int(input("Enter the upper Range:"))
for i in range(lowerRange,upperRange+1):
    if i%2==0:
        print(i,end=",")