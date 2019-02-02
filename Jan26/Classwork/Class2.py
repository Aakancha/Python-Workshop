class TempConverter:

    
    def cel_to_far(ctemp):
        return ctemp*(9/5)+32

    def far_to_cel(ftemp):
        return (5/9)*(ftemp-32)

print(TempConverter.cel_to_far(100))
print(TempConverter.far_to_cel(34))
