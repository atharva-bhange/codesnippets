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
