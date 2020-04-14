from turtle import Turtle 
from random import randint

laura = Turtle()

laura.color('red')
laura.shape('turtle')

laura.penup()
laura.goto(-160,100)
laura.pendown()

rik = Turtle()

rik.color('green')
rik.shape('turtle')

rik.penup()
rik.goto(-160,70)
rik.pendown()

lauren = Turtle()

lauren.color('blue')
lauren.shape('turtle')

lauren.penup()
lauren.goto(-160,40)
lauren.pendown()

carren = Turtle()

carren.color('pink')
carren.shape('turtle')

carren.penup()
carren.goto(-160,10)
carren.pendown()

for movement in range(120):
    laura.forward(randint(1,5))
    rik.forward(randint(1,5))
    lauren.forward(randint(1,5))
    carren.forward(randint(1,5))
    if(laura.xcor()>=185):
      print("laura won")
      exit()
    if(rik.xcor()>=185):
      print("rik won")
      exit()
    if(lauren.xcor()>=185):
      print("lauren won")
      exit()
    if(carren.xcor()>=185):
      print("carren won")
      exit()
