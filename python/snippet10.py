#Snippet 10

class dog(object):
    dogs = []
    def __init__(self,name):
        self.name = name
        dog.dogs.append(self.name)
    @classmethod
    def length(cls):
        return len(cls.dogs)
    @staticmethod
    def bark(n):
        for t in range(n):
            print("bark!")
mark = dog("mark")
jim = dog("jim")
print(dog.dogs)
print(dog.length())
print(dog.bark(3))
