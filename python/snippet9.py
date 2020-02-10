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
