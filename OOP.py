class Person:
    count = 0


    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        Person.count += 1


    def greet(self):
        print(f"Hello! I am {self.name}")

    

jane = Person("Jane",20,182,65)
jane.greet()

print(Person.count)