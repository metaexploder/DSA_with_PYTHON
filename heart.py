import turtle
import math
import time

def draw_heart():
    turtle.pensize(3)
    turtle.speed(5)
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(180)
    turtle.end_fill()

def animate_heart():
    for i in range(5):
        turtle.hideturtle()
        time.sleep(0.5)
        turtle.showturtle()
        time.sleep(0.5)

def display_message():
    turtle.up()
    turtle.goto(-100, -200)
    turtle.color("black")
    turtle.write("I Love You!", font=("Arial", 24, "bold"))

def main():
    turtle.bgcolor("pink")
    draw_heart()
    animate_heart()
    display_message()
    turtle.done()

if __name__ == "__main__":
    main()
