for i in range(0,100):
    grade=float(input("What is the grade percentage:"))
    if grade>=90:
        print("you got A+")
    elif 80<=grade<90:
        print("you got A" )
    elif 60<=grade<80:
        print("you got A-")
    else:
        print("sorry you need A- for qualified")

