def largestnumber(number):
    biggest_num=number[0]
    for num in number:
        if num>biggest_num:
            biggest_num=num
            return biggest_num
        print(largestnumber([1,2,3,4,5,567]))