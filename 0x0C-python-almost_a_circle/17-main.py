#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(3, 5)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2.x)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
    print(">>>>>>>>>>>>>>>>>>>>")

    r3 = Square(1, 1, 1)
    r3_dictionary = r3.to_dictionary()

    new = Square.create(**r3_dictionary)
    print(new)
    print(type(new))
