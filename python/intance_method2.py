#in last exmple we used description to define a object 
#but when we print a object directly we dont a desired output
#so use the method __str__()
#replace descripion method with __str__()
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

dog1=Dog("first",5)
#print(dog1.description())
print(dog1)
print(dog1.speak("bow wow"))

#methods like __init__(),__str__() are called as dunder methods . there are several dunder methods
