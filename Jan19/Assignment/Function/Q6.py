def string(a):
    b={"Upper_Case":0, "Lower_Case":0}
    for c in a:
        if c.isupper():
           b["Upper_Case"]+=1
        elif c.islower():
           b["Lower_Case"]+=1
        else:
           pass
    print ("Real String : ", a)
    print ("No. of Upper case characters : ", b["Upper_Case"])
    print ("No. of Lower case Characters : ", b["Lower_Case"])

string('The quick Brow Fox')

