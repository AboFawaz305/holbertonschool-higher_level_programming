#!/usr/bin/python3
"""
Serialize classes using pickle
"""
import pickle


class CustomObject:
    """
    A serializable class with pickle
    """

    def __init__(self, name, age, is_student) -> None:
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, mode="wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, mode="rb") as f:
                data = pickle.load(f)
            return cls(name=data.name, age=data.age,
                       is_student=data.is_student)
        except Exception:
            return None
