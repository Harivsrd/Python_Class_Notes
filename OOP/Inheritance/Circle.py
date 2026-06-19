class Circle:
    def __init__(self, radius):
        self._radius = radius  
        
    def area(self):
        return 3.14 * self._radius * self._radius
    def printCircle(self):
        print(f"Circle :")
        print("Radius :",self._radius)
        print("Area :",self.area())
        
class Sphere(Circle):
    
    def __init__(self, radius):
        super().__init__(radius)
        
    def volume(self):
        return (4/3)*3.14*(self._radius*self._radius*self._radius)
    
    def printSphere(self):
        print("Sphere :")
        print("Volume :",self.volume())
        
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self._height = height 
        
    def volume(self):
        return 3.14 * (self._radius*self._radius)*self._height
    
    def printCylinder(self):
        print("Cylinder :")
        print("Volume :",self.volume())
        
        
while True:
    print("------MENU-------")
    print("1. Sphere")
    print("2. Cylinder")
    print("3. exit")
    
    choice = int(input("Enter choice :"))
    if choice == 1 : 
        radius = float(input("Enter radius :"))
        s = Sphere(radius)
        s.printCircle()
        s.printSphere()
    elif choice == 2:
        radius, height = map(int, input("Enter radius, height :").split())
        c = Cylinder(radius, height)
        c.printCircle()
        c.printCylinder()
    else :
        exit()
        break