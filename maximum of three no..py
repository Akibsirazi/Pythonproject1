def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
z=float(input("Enter third number:"))
print("Max of three number is :",find_max(x,y,z))