def digit_sum(num):
    x = 0
    for each in str(num):
        x = x + int(each)
    return x
print(digit_sum(1111))
