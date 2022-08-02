import graphics   # user made module
from random import randint

class Point :
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def falls_in_rectangle(self,rectangle): # check whether point falls in rectangle

        if(rectangle.point1.x< self.x\
          and rectangle.point2.x >  self.x\
          and rectangle.point1.y <self.y\
          and  rectangle.point2.y > self.y):

            return True
        return False



class Rectangle:
    def __init__(self,point1,point2) : # point class objects 
        self.point1=point1
        self.point2=point2
    def get_coordinate(self):
        print("coordinate of rectangle are: \
        ( {0:.2f} ,{1:.2f} ) and \
        ({2:.2f}, {3:.2f})".format(self.point1.x,self.point1.y,self.point2.x,self.point2.y))

class Gui_Point(Point):
    def falls_in_rectangle(self,rectangle):

        super().falls_in_rectangle(rectangle)
        graphics.graphics_obj.draw_point(self)


class Gui_Rectangle(Rectangle): # inheriting the rectangle class
    def show_rectangle(self):
        graphics.graphics_obj.draw_rectangle(self) # passing the current object reference









try:
    rectangle1=Rectangle(Point( randint(5,15),randint(7,18) ),Point( randint(20,27),randint(20,23) ) )

    rectangle1.get_coordinate()
    print(Point(float(input("enter X: ")),float(input("enter Y : "))).falls_in_rectangle(rectangle1) )

    dynamic_rectangle=Gui_Rectangle( Point(randint(50,150) , randint(50,150) ) , Point( randint(210,300) ,randint(210,300) ) )
    dynamic_rectangle.get_coordinate()


    dynamic_point=Gui_Point( float( input("enter x: ") ) , float(input("enter y: ") ) )

    dynamic_rectangle.show_rectangle()
    dynamic_point.falls_in_rectangle(dynamic_rectangle)

except (TypeError,ValueError,KeyboardInterrupt,EOFError) as obj:
    print(obj)


 

    

