class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radius = self.radius
        a = (22/7)*radius*radius
        print(a)    
    def circumference(self):
        radius = self.radius
        C = 2*(22/7)*radius
        print(C)
class Square:
    def __init__(self,width):
        self.width = a
    def area(self):
        a = self.width
        A = a*a
        print(A)
    def perimeter(self):
        a = self.width
        P = 4*a
        print(P)
class Rectangle:
    def __init__(self,width,length):
        self.width = w
        self.length = l
    def area(self):
        w = self.width
        l = self.length
        A = w * l
        print(A)    
    def perimeter(self):
        w = self.width
        l = self.length
        P = 2(w+l)
        print(P)
class Sphere:
    def __init__(self,radius):
        self.radius = r
    def area(self):
        r = self.radius
        A = 4*(22/7)*r*r
        print(A)
    def volume(self):
        r = self.radius
        V = (4/3)*(22/7)*r*r*r
        print(V)                            
