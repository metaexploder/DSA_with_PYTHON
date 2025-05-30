import turtle
import time
import math

def heart_curve(t):
    return 16 * math.sin(t) ** 3, 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

def draw_heart():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.pensize(3)
    turtle.speed(0)
    turtle.color("red")
    turtle.begin_fill()
    for t in range(0, 628, 2):  # 0 to 2*pi in radians (scaled)
        x, y = heart_curve(t / 100)
        turtle.goto(x * 10, y * 10)
    turtle.end_fill()

def animate_heart():
    for _ in range(5):
        turtle.color("pink")
        time.sleep(0.5)
        turtle.color("red")
        time.sleep(0.5)

def display_message():
    turtle.penup()
    turtle.goto(-70, -200)
    turtle.color("black")
    turtle.write("I Love You!", font=("Arial", 24, "bold"))
    turtle.hideturtle()

def main():
    turtle.bgcolor("white")
    draw_heart()
    animate_heart()
    display_message()
    turtle.done()

if __name__ == "__main__":
    main()
