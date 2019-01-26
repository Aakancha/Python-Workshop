def fact(b):
    if b == 0:
        return 1
    else:
        return b * fact(b-1)
b=int(input("Enter the number to calculate the factorial : "))
print(fact(b))
