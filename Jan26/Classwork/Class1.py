class Animal:

        def __init__(self,type):
            self.type = type

class Dog(Animal):
    def __init__(self, name, type):
            super().__init__ (self)
            self.name = name
            self.type = type

d= Dog("tom", "carni")
print(d.__dict__)
print(isinstance(d,Animal))
print(isinstance(d,Dog))
print(isinstance(d,type))
