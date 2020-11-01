#init method is like a constructor 
# slef refers to the current class instance 
class Dog:
    #class attributes are common for every instance of that class
    species="Canis familiari"  
    def __init__(self,name,age):
        #instance attributes are defined in a class and are diff for every instance of class
        self.name=name
        self.age=age
    #instance methods    
    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} says {sound}"    

dog1=Dog("first",5)
print(dog1.description())
print(dog1.speak("bow wow"))
