#!/usr/bin/python3
S = __import__('101-square')

Square = S.Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
