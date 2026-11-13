#trying out classes in python.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I don't know what to say!")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

#class Lion inherits from the class  Animal, meaning the constructor from
#Animal runs when you create a Lion object.

#Note ,,,,, if both parent and child have a method with the same name , 
# the method in the child overrides the one in the parent cause it's more specific.
#to that calling object.



class Lion(Animal):
    def __init__(self,name, age, gender):
        super().__init__(name,age) #loads contractor form the parent class
        self.gender = gender

    def speak(self):
        print("Roar!!")

    def show(self):
        print(f"I am {self.name}. I am a {self.gender} and i am {self.age} years old.")


class Leopard(Animal):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location = location

    def show(self):
        print(f"I am {self.name} . I live in {self.location} and i am {self.age} years old")

a = Animal("Elephant", 50)
a.speak()
a.show()
print("\n")

l = Lion("Simba",10,"Brunnette")
l.speak()
l.show()
print("\n")

leo = Leopard("Spots",8,"Maasai Mara")
leo.speak()
leo.show()
