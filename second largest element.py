lst=eval(input("Enter a list:"))
l=len(lst)
max=smax=list[0]
for i in range(1,1):
    if lst[i]>max:
        smax=max
        max=lst[i]
    elif lst[i]>smax:
        smax=lst[i]
        print("second largest number is:",smax)
