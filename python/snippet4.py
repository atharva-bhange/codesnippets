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
