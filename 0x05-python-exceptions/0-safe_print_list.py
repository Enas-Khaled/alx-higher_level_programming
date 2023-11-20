#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        for i in my_list:
            print(i, end="")
        print('\n')
except Exception as e:
    print("",end="")
