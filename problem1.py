a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def greater(a, b, c):
    if a > b and a > c:
        print ("The greatest number is; ", a)
        return a
    elif b > a and b > c:
        print ("The greatest number is; ", b)
        return b
    else:
        print ("The greatest number is; ", c)
        return c


greater(a, b, c)

