class Car:
    def __init__(self, name, wheels, engine):
        
        self.name= name
        self.wheels= wheels
        self.engine= engine

    def drift(self):
        print(f"{self.name} is drifting")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Car({self.name}, {self.wheels}, {self.engine})"
              

kia= Car("kia", 4, "Diesel")
tesla= Car("tesla", 6, "electric")

print(kia.engine)
print(tesla.engine)
print(kia)
print (repr(kia))

kia.drift()
tesla.drift()










