# colorgram -> extract rgb colors from images
# import colorgram

# rgb_colors = []

# # extract 6 colors from image
# colors = colorgram.extract(r'C:\Users\Owner\Desktop\web322\python_dev_100projects\Turtle_graphics\hirst_painting_project\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
    
# print(rgb_colors)


from turtle import Turtle, colormode, Screen 
import random

colormode(255)
tim = Turtle()
tim.speed("fastest") 
# making pen up from start so it just drop the dots
tim.penup()
tim.hideturtle()
colors_list = [(73, 94, 121), (136, 157, 188), (35, 40, 48), (171, 148, 133), (127, 111, 98), (35, 27, 32), (201, 209, 223), (41, 29, 25), (175, 148, 161), (98, 126, 166), (171, 173, 171), (114, 91, 103), (228, 195, 175), (180, 189, 208), (50, 62, 82), (135, 128, 117), (158, 110, 124), (217, 197, 209), (29, 33, 31), (207, 182, 194), (167, 113, 96), (93, 48, 40), (222, 182, 164), (81, 51, 58), (96, 100, 97), (228, 237, 236), (222, 187, 159), (68, 66, 54), (188, 193, 192), (182, 195, 199)]

# moving turtle little between 180 and 270 and 250 steps down
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

num_dots = 100


# dot(size,color)
for dot_count in range(1,num_dots + 1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)

    # 10 * 10
    if dot_count % 10 == 0:
    # print new row up
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()