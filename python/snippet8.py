#Snippet 8

class animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print("Hello I am a animal and my name is" , self.name , "and I am" , self.age , "years old.")

class dog(animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed
    def speak(self):
        print("bark")
class cat(animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

mark = dog("mark", 12 , "pug")
jim = cat("jim", 14, "black")
mark.speak()
jim.speak()
