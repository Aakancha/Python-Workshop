def sum(a,b):
    yield a+b
    yield a-b
    yield a*b

gen_sum= sum(1,2)
for each in gen_sum:
    print (each)



def sum1():
    i= 0
    yield i
    i+=1
    yield i
    i= 100
    yield i

gen_sum= sum1()
for each in gen_sum:
    print (each)



l=[x for x in range(1,100000)]
g=(x for x in range(1,100000))

print("Memory consumed by list 1: ",l.__sizeof__())
print("Memory consumed by generator: ",g.__sizeof__())
