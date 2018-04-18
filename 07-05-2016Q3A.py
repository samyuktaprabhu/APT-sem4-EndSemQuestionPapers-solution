#inside the module
class Shape:
 x=0
 y=0
 def __init__(self,x,y):
      self.x=x
      self.y=y
 def __del__(self,x,y):
      self.y=y
      self.x=x
class Circle(Shape):
 radius=0
 area=0
 def __init__(self,radius):
      self.radius = radius
 def __del__(self,radius):
      self.radius = radius
 def Area(radius):
      area=3.142*radius*radius
      print(area)

class Rect(Shape):
 side1=0
 side2=0
 area=0
 def __init__(self,side1,side2):
      self.side1 = side1
      self.side2 = side2
 def __del__(self,side1,side2):
      self.side1 = side1
      self.side2 = side2
 def Area(side1,side2):
      area=side1*side2
      print(area)
     
#main prog
import pyt
#class Shape
print("hello")
print("enter radius, side1,side2")
r=int(input())
s1=int(input())
s2=int(input())
print("Area of circle of radius 1 is :")

pyt.Circle.Area(r)
print("area of rectangle is")
pyt.Rect.Area(s1,s2)
