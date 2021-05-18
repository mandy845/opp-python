class Shapes :
    def __init__(self, name,type, size, sides):
        self.name = name
        self.type = type
        self.size = size
        self.sides = sides
    def area(self):
        print("I am a :" + self.name + '\n'+
             "I have :" + self.type+ "\n" +
              "I have :" + self.size + "\n" +
              "I have :" + self.sides )

obj_shape=Shapes("Shape", "4" , "polgon" , "14cm")
obj_shape.area()
class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        results= 3.14 * self.radius * self.radius
        return results
obj_coin = Circle(5)
print(obj_coin.area)

#Triangle
class Triangle(Shapes):
    def __init__(self , height , base):
        self.height = height
        self.base= base

    def area(self):
        results=0.5 * (self.height * self.base)
        return results

obj_pyramid= Triangle(5,10)
print(obj_pyramid.area())

#Rectangle
class Rectangle (Shapes):
    def __init__(self ,width , length):
        self.width= width
        self.length= length

    def area(self):
        results= self.length * self.width
        return results
obj_laptop=Rectangle(10,15)
print(obj_laptop.area())

#Square

class Sqaure(Shapes):
    def __init__(self ,side1 ,side2):
        self.side1= side1
        self.side2=side2

    def area(self):
        results=self.side1 * self.side2
        return results
obj_Cube= Sqaure(5, 10)
print(obj_Cube.area())



