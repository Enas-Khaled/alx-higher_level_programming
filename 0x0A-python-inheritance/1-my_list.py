#!/usr/bin/python3
''' Molule for MyList class '''


class MyList(list):
    """ My list driven from list"""

    def print_sorted(self):
        """ print sorted list """

        print(sorted(self))
