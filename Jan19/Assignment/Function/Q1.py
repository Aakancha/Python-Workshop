def max1( a, b ):
    if a > b:
        return a
    return b
def max2( a, b, c ):
    return max1( a, max1( b, c) )
print(max2(1, 2, 3))
