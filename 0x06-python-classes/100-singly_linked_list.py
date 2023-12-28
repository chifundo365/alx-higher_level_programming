#!/usr/bin/python3
"""This module builds a sigly linked list."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be integer")
        self.__data = data
        if next_node != None or type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None or type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ implememts a singly  linked list structure."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
        elif new_node.data < self.__head.data:
            new_node.next = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current:
                previous = current
                current = current.next_node
                if current is None:
                    prev.next_node = new_node
                if current.data > new_node.data:
                    prev.next_node = new_node
                    new_node.next_node = current
                    break
    def __str__(self):
        output = ""
        current = self.__head
        while current:
            output += str(current.data) + "\n"
            current = current.next_node
        return output


            




