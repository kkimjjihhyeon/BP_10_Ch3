import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("x1: "))
x1: 0
y1 = int(input("y1: "))
y1: 0
x2 = int(input("x2: "))
x2: 100
y2 = int(input("y2: "))
y2: 100

t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.write("점의 길이=" + (str)( ((x1-x2)**2 + (y1-y2)**2)**0.5))
