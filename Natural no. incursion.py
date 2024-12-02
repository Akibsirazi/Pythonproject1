def recur_sum(n):
    if(n<=0):
        return n
    else:
        return n+recur_sum(n-1)
    num=int(input("Enter the number f terms:"))
    if(num<0):
        print("enter a natural number,")
    else:
        print(recur_sum(num))