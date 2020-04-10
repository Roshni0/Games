from shapes import Triangle, Oval, Rectangle
from random import randint


rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

rect2 = Rectangle()
rect2.set_width(randint(10,150))
rect2.set_height(randint(10,150))
rect2.set_color("red")
rect2.set_x(randint(0,400))
rect2.set_y(randint (0,400))

ovl1=Oval()
ovl1.randomize()

tri1 = Triangle()
tri1.randomize()
