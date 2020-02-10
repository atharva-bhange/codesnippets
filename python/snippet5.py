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
