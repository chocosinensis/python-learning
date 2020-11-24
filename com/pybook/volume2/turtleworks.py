import turtle
from .exercises_oop import TurtleError  # import for Ch 6

class AjobTurtle(turtle.Turtle):  # Ch 6
    """The behavior of AjobTurtle class is fully opposite of the main Turtle class"""
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        raise TurtleError()


if __name__ == '__main__':
    ajob = AjobTurtle()
    ajob.left(30)
    ajob.forward(200)
    ajob.left(45)
    ajob.backward(100)
    try:
        ajob.right(90)
    except TurtleError:
        print('\u001b[31mAjobTurtle doesn\'t turn right\u001b[39m')
    ajob.forward(10)

    turd = turtle.Turtle()
    turd.shape('turtle')
    turd.left(30)
    turd.forward(200)
    turd.left(45)
    turd.backward(100)
    turd.right(90)
    turd.forward(10)

turtle.exitonclick()
