from turtle import Turtle
# POS=[(350,-40),(350,-20),(350,0),(350,20),(350,40)]
class Paddle:

    def __init__(self,position):


        self.tim = Turtle()

        self.tim.color('white')
        self.tim.shape("square")
        self.tim.shapesize(stretch_len=1, stretch_wid=5)
        self.tim.penup()

        self.tim.goto(position)










    def up(self):
        new_y=self.tim.ycor()+ 20
        self.tim.goto(self.tim.xcor(),new_y)

    def down(self):
        new_new_y=self.tim.ycor()-20
        self.tim.goto(self.tim.xcor(),new_new_y)








