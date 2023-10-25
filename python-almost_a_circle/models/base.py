#!/usr/bin/python3
""" first class Base """


import json


class Base():
    """ class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init base """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integerValid(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def integerValid2(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """  return json string representation
            Args : list_dictionaries : a list of dictionaries
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation """
        if list_objs:
            index = cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])
        else:
            index = '[]'
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(index)

    @staticmethod
    def from_json_string(json_string):
        """ static method returns the list of the JSON string representation
            Args: json_string: json object type
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as file:
                data = cls.from_json_string(file.read())
            return [cls.create(**element) for element in data]
        except FileNotFoundError:
            return []
