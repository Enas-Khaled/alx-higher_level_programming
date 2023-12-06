#!/usr/bin/python3
''' class student '''


class Student:
    '''
    student class and its description
    '''
    def __init__(self, first_name, last_name, age):
        ''' init fun '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' to json fun '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
