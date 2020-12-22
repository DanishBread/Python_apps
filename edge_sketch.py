import colorgram
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_list = [(208, 159, 108), (223, 206, 117), (136, 173, 194), (242, 250, 245), (252, 245, 249), (217, 232, 241), (38, 106, 140), (137, 184, 146), (13, 52, 76), (220, 87, 63), (146, 80, 71), (69, 165, 119), (29, 129, 106), (125, 80, 96), (9, 59, 50), (54, 153, 180), (197, 130, 144), (52, 33, 43), (129, 36, 49), (207, 83, 101), (4, 111, 88), (175, 206, 167), (156, 152, 69), (230, 167, 182), (144, 204, 233), (34, 64, 101), (46, 30, 26), (13, 87, 105), (183, 189, 204)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.speed("fastest")
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
