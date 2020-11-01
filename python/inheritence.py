
class Dog:
    #class attributes are common for every instance of that class
    species="Canis familiari"  
    def __init__(self,name,age):
        #instance attributes are defined in a class and are diff for every instance of class
        self.name=name
        self.age=age
    #instance methods    
    #def description(self):
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} says {sound}"    

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

#isinstance(instance/object,class)
isinstance(miles,JackRussellTerrier)#True
isinstance(miles,Bulldog)#False

#to refer to parent class attributes or methods we use super()
# exampele super().speak("bow") 
