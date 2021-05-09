from turtle import *
screen=Screen()
class scr():
 def __init__(self):

  screen=Screen()
  turtle=Turtle()
  image=("blank_states_img.gif")
  screen.addshape(image)
  screen.setup(800,600)
  turtle.shape(image)
 def state_turtle(x,y,guess):
  turtle=Turtle()
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(x,y)
  turtle.pencolor("black")
  turtle.write(guess,move=False,align="left", font=("Arial", 8, "normal") )
