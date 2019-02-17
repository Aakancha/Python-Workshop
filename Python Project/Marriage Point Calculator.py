def marriage_calc():
    a = str(input("Has the joker appeared? (y/n)"))
    if a.lower()=="y":
        x = int(input("Your Maal: "))
        y = int(input("Total Maal: "))
        z = int(input("Total number of players:"))
    if x*z > y:
         return 'Win :', (x * z) - (y + 3)
    elif x*z < y:
        return "Loss:", (y + 3) - (x * z)
    else:
        y = int(input("Total Maal: "))
        return "Your net loss is", (y + 10)
print(marriage_calc())
