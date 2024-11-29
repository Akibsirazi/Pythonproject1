def fact_of(n):
    i=1
    for x in range(1,n+1):
        i=i*x
        return i
    print(fact_of(5))