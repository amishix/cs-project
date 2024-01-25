from turtle import *

screen = Screen()
screen.bgcolor("lightblue")

x = 1
month = 1
const = 20
day = 1
speed(0)
monthname = ["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]
start = [2, 5, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7]

clear()

for i in range(2):
    forward(const*7)
    right(90)
    forward(20)
    right(90)
setheading(90)
backward(const)
setheading(0)
forward(20)
write(monthname[month])
backward(20)

while(day < 8):
    for i in range (2):
        forward(const)
        right(90)
    forward(const-2)
    right(90)
    write(weekdays[day])
    setheading(180)
    forward(2)
    setheading(90)
    forward(const)
    setheading(0)
    forward(const)
    day += 1

backward(const*7)
right(90)
forward(const)
left(90)

for i in range(6):
    for j in range(7):
        for k in range(2):
            forward(const)
            right(90)
            forward(const)
            right(90)
            
        forward(const)
    setheading(270)
    forward(const)
    setheading(0)
    backward(const*7)

setheading(270)
penup()
forward(const)
pendown()
setheading(0)
month+=1

# Register the emoji image as a new shape
screen.register_shape("race-car.gif")  # Replace "emoji.gif" with your image file name

def place_emoji_at_end():
    """Places an emoji at the end of the calendar drawing."""
    penup()
    goto(-100, -60)
    shape("race-car.gif")
    stamp()

def place_emoji_at_another_spot():
    """Places an emoji at a different spot."""
    penup()
    goto(-100, 100)
    shape("race-car.gif")
    stamp()

    
# Key bindings
screen.onkey(place_emoji_at_end, "r")
screen.onkey(place_emoji_at_another_spot, "2")

# Enable listening for key events
screen.listen()

# Keep the window open
mainloop()