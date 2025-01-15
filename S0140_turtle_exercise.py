"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 3:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 4:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 5:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


def square(length):
    tom = turtle.Turtle()
    for _ in range(4):
        tom.forward(length)
        tom.left(90)
    turtle.done()


def many_squares(amount, length, distance):
    tom = turtle.Turtle()
    for _ in range(amount):
        for _ in range(4):
            tom.forward(length)
            tom.left(90)
        tom.penup()
        tom.forward(distance)
        tom.pendown()
    turtle.done()


def square_spiral(n):
    tom = turtle.Turtle()
    tom.penup()
    tom.goto(0, 0)
    tom.right(90)
    tom.pendown()
    tom.pensize(20)
    length = 10
    for i in range(n):
        tom.forward(length)
        tom.left(90)
        length += 20
    turtle.done()


#square_spiral(24)


def star_simple(side_length, points=5):
    tom = turtle.Turtle()
    tom.penup()
    tom.goto(-50, 0)
    tom.pencolor("green")
    tom.pendown()
    turn_angle = 180 - (180 / points)
    for _ in range(points):
        tom.forward(side_length)
        tom.right(turn_angle)
    turtle.done()

#star_simple(100)

def star_medium(side_length, points=7):
    tom = turtle.Turtle()
    tom.penup()
    tom.goto(0, 0)
    tom.pencolor("green")
    tom.pendown()
    turn_angle = 180 - (180 / points)
    for _ in range(points):
        tom.forward(side_length)
        tom.left(turn_angle)
    turtle.done()

#star_medium(100)


def star_advanced(side_length, points=11):
    tom = turtle.Turtle()
    tom.penup()
    tom.goto(50, 0)
    tom.pencolor("green")
    tom.pendown()
    turn_angle = 180 - (180 / points)
    for _ in range(points):
        tom.forward(side_length)
        tom.left(turn_angle)
    turtle.done()

#star_advanced(100)


def draw_star(side_length, points, start_position, rotation_direction):
    tom = turtle.Turtle()
    tom.penup()
    tom.goto(start_position)
    tom.pencolor("green")
    tom.pendown()
    turn_angle = 180 - (180 / points)
    for _ in range(points):
        tom.forward(side_length)
        if rotation_direction == "right":
            tom.right(turn_angle)
        else:
            tom.left(turn_angle)

def draw_all_stars():
    draw_star(100, 5, (-150, 20), "right")
    draw_star(100, 7, (0, 0), "left")
    draw_star(100, 11, (150, 0), "left")
    turtle.done()

#draw_all_stars()

def draw_heart(size):
    tom = turtle.Turtle()
    tom.penup()
    tom.goto(0, 0)
    tom.pencolor("pink")
    tom.pensize(20)
    tom.pendown()
    tom.left(45)
    tom.forward(90)
    tom.left(45)
    tom.forward(50)
    tom.left(45)
    tom.forward(50)
    tom.left(45)
    tom.forward(40)
    tom.left(45)
    tom.goto(0, 90)
    tom.forward(50)
    tom.right(90)
    tom.forward(50)
    tom.right(-45)
    tom.forward(45)
    tom.right(-45)
    tom.forward(50)
    tom.right(-45)
    tom.forward(50)
    tom.right(-45)
    tom.forward(90)
    tom.goto(0, 0)
    turtle.done()

def draw_heart(size):
    tom = turtle.Turtle()
    tom.speed(3)
    tom.color("pink")
    tom.pensize(1)
    tom.begin_fill()
    tom.left(50)  # Tilt 50 degrees to start
    tom.forward(size)  # Draw the first line
    tom.circle(size * 0.4, 200)
    tom.right(140)
    tom.circle(size * 0.4, 200)
    tom.forward(size)
    tom.end_fill()
    tom.hideturtle()
    turtle.done()

#draw_heart(250)

def draw_heart2(size):
    tom = turtle.Turtle()
    tom.speed(100)
    tom.color("pink")
    tom.pensize(7)
    tom.left(50)  # Tilt 50 degrees to start
    tom.forward(size)  # Draw the first line
    tom.circle(size * 0.4, 200)
    tom.right(140)
    tom.circle(size * 0.4, 200)
    tom.forward(size)
    for i in range(9):
        tom.left(140)  # Tilt 50 degrees to start
        tom.forward(size)  # Draw the first line
        tom.circle(size * 0.4, 200)
        tom.right(140)
        tom.circle(size * 0.4, 200)
        tom.forward(size)
    tom.penup()
    tom.pencolor("green")
    tom.begin_fill()
    tom.fillcolor("green")
    tom.goto(-23, -34)
    tom.pendown()
    tom.circle(size * 0.1)  # Full circle
    tom.end_fill()
    tom.hideturtle()
    turtle.done()
draw_heart2(200)