'''
# Snippet 1
class dog(object):
    def __init__(self):
        pass
    def speak(self):
        pass

mark = dog()
print("Code complete")
'''

'''
#Snippet 2
class dog(object):
    def __init__(self):
        print("Hey you have created a dog.")
    def speak(self):
        pass

mark = dog()
fread = dog()
print("Code complete")
'''

'''
# Snippet 3
class dog(object):
    def __init__(self):
        print("Hey you have created a dog.")
    def speak(self):
        print("Hey your dog is speaking.")

mark = dog()
fread = dog()
fread.speak()
'''

'''
# Snippet 4
class dog(object):
    def __init__(self,name,age):
        self.dogName = name
        print(self.dogName)
        self.dogAge = age
        print(self.dogAge)
        print("All atribute variable created.")
    def speak(self):
        print("Hey your dog is speaking.")

mark = dog("mark",23)
print(mark.dogName)
print(mark.dogAge)
'''

'''
#Snippet 5
class dog(object):
    def __init__(self,name,age):
        self.dogName = name
        self.dogAge = age
        self.bodyParts = ['mouth' , 'legs' , 'tail']
    def speak(self):
        print("Hello I am a dog and my name is" , self.dogName , "and I am" , self.dogAge , "years old.")

    def parts(self):
        print("I am dog and I have " , end ='')
        for t in self.bodyParts:
            print(t+" " , end ='')
        print("body parts.")

mark = dog('mark',22)
fread = dog('fread',10)
mark.speak()
fread.speak()
fread.parts()
'''

'''
# Snippet 6
class dog(object):
    def __init__(self,name,age):
        self.dogName = name
        self.dogAge = age
    def speak(self):
        print("Hello I am a dog and my name is" , self.dogName , "and I am" , self.dogAge , "years old.")
    def changeAge(self , newage):
        temp = self.dogAge
        self.dogAge = newage
        print("Dog age changed from" , temp , "to" , self.dogAge)
    def setBreed(self,breed):
        self.dogBreed = breed
        print('Breed successfully created and set to' , self.dogBreed)
mark = dog("mark" , 10)
fread = dog("fread" , 20)
mark.speak()
fread.speak()
mark.changeAge(999)
mark.setBreed('pug')
mark.dogAge
mark.dogBreed
fread.dogBreed
'''

'''
# Snippet 7

class animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print("Hello I am a animal and my name is" , self.name , "and I am" , self.age , "years old.")

class dog(animal):
    def __init__(self , name,age, breed):
        super().__init__(name,age)
        self.breed = breed
    def talk(self):
        print("Bark")

class cat(animal):
    def __init__(self, name,age, color):
        super().__init__(name,age)
        self.color = color
    def catColor(self):
        print(self.color)
mark = dog("mark",12,"pug")
jim = cat("jim" , 24 ,"black")
mark.speak()
jim.speak()
mark.talk()
print(mark.breed)
jim.catColor()

'''

'''
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
'''

#Snippet 9
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, p):
        return point(self.x + p.x, self.y +p.y)
    def __sub__(self, p):
        return point(self.x - p.x , self.y - p.y)
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

p1 = point(2,3)
p2 = point(4,5)
p3 = point(-2,3)
p4 = point(-3,-8)

p5 = p1 + p2
p6 = p1 - p2
print(p5)
print(p6)
