a=int(input("enter first number"))
b=int(input("enter second number"))
while b>a:
    r=a%b
    a=b
    b=r
    GCD=a
    print("GCD is",GCD)