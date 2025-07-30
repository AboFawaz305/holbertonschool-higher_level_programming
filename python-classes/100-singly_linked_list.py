#!/usr/bin/python3
"""
Singly Linked List
"""


class Node:
    """
    Node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node property."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Singly Linked List Data structure
    """

    def __init__(self) -> None:
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        previous = None
        current = self.__head
        while current is not None:
            if current.data > value:
                break
            previous = current
            current = current.next_node
        n = Node(value)
        if previous is not None:
            previous.next_node = n
        else:
            self.__head = n
        n.next_node = current

    def __str__(self):
        if self.__head is None:
            return ""
        c = self.__head
        s = ""
        while c is not None:
            s += f"{c.data}\n"
            c = c.next_node
        return s[:-1]
