class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __add__(self,p1):
        x = self.x + p1.x
        y = self.y + p1.y
        p3 = Point(x,y)
        return p3 
    
#It is using fo addition of two objects so when we give add two objects we are redefining
# to add some feilds in the objects

p11 = Point(2,4)
p22 = Point(11,4)
p33 = p11+p22 
print(p33.x,p33.y)