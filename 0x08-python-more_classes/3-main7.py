#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print(my_rectangle_1.height)
my_rectangle_1.print_symbol = "H"
print(my_rectangle_1)
print("end")
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)

