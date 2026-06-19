class Rectangle:
    def __init__(self, length, breadth):
        self._length = length 
        self._breadth = breadth 
        
    def area(self):
        return self._length * self._breadth 
    
    def perimeter(self):
        return 2 * (self._length + self._breadth)
    
class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self._height = height
        
    def volume(self):
        return self._length * self._breadth * self._height
    
    
l,b,h = map(int,input("Enter dimensions for cuboid :").split())
c = Cuboid(l,b,h)

print("Area of rectangle : ",c.area())
print("Perimeter of rectangle :",c.perimeter())
print("Volume of cuboid :",c.volume())