def sum(a,b):
    return a+b

a= sum

def accept_func(a):
    print(a(1,2))

accept_func(a)


def outer():
        def inner(a,b):
            return a+b
        return inner
    
x= outer()(2,3)
print(x)



