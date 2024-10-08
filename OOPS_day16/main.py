# import turtle
# here object is name_turtle and Turtle() is a class
# name_turtle = turtle.Turtle()
# print(name_turtle)

# my_screen = turtle.Screen()
# # here canvheight is an attribute
# print(my_screen.canvheight)
# # exitonclick() is a method
# my_screen.exitonclick()
# name_turtle.shape("turtle")


from prettytable import PrettyTable
# object -> table
# PrettyTable() -> class
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
table.align = "l"
print(table)


# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])
# print(table)