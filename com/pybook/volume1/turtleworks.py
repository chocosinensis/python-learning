import turtle

turtle.color('dark blue')

for i in range(3):  # Ch 4
    turtle.forward(100)
    turtle.left(120)

turtle.reset()
turtle.color('dark blue')

turtle.speed(1)  # Ch 5
for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.reset()
turtle.color('dark blue')

turtle.speed(5)
counter1 = 0
while counter1 < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter1 += 1

turtle.reset()
turtle.color('dark blue')

height = 5
width = 5
turtle.speed(2)
turtle.penup()
for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.reset()
turtle.color('dark blue')
turtle.speed(0)

def draw_square(side_length):  # Ch 6
    for a in range(4):
        turtle.forward(side_length)
        turtle.left(90)


counter = 0
while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.reset()
turtle.color('dark blue')

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam, how are you?")
else:
    name = name.capitalize()
    str1 = "Hi " + name + "! How are you?"
    print(str1)

turtle.exitonclick()
