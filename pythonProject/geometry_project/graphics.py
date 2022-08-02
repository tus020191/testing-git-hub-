import turtle
import time
class Drawing:
    def __int__(self):
        self.myturtle1=turtle.Turtle()

    def draw_point(self,point_object): # drawing point whether it lies in rectangle or not
        self.myturtle1.penup()
        self.myturtle1.goto(point_object.x ,point_object.y) # point
        self.myturtle1.dot(25,"yellow")
        turtle.done()  # closing the turtle when rectangle and then point is drawn

    def draw_rectangle(self,rectangle_object):      # taking rectangle object defined in file rectangle.py
        self.myturtle1=turtle.Turtle()

        # orginally the origin of turtle canvas is at centre

        # to move it to specific coordinate
        # by default it draws line
        self.myturtle1.penup()  # this does not draw line
        time.sleep(2)
        self.myturtle1.goto(rectangle_object.point1.x, rectangle_object.point1.y) # starting from point1 coordinate of rectangle


        self.myturtle1.pendown() # to draw line
        time.sleep(2)
        self.myturtle1.forward(rectangle_object.point2.x - rectangle_object.point1.x) # in x direction forward
        self.myturtle1.left(90) # to turn by 90 degree to left i,e, up

        time.sleep(2)
        self.myturtle1.forward(rectangle_object.point2.y - rectangle_object.point1.y) # in y direction
        self.myturtle1.left(90) # turn  now left by 90 degree i,e, right

        time.sleep(2)
        self.myturtle1.forward(rectangle_object.point2.x - rectangle_object.point1.x) # in backward x dir
        self.myturtle1.left(90) #  turn now  down by 90 degree

        time.sleep(2)
        self.myturtle1.forward(rectangle_object.point2.y - rectangle_object.point1.y) # in y dir down
        self.myturtle1.hideturtle() # to hide the turtle after the rectangle is done


graphics_obj=Drawing() # object

