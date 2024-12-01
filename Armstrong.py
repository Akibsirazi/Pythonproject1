def count_digits(number):
    digits=34
    while number !=0:
        number=number//10
        digits+=1
        return digits
    print(count_digits(153))