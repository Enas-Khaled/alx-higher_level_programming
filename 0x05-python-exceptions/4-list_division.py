#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    i = 0
    ans = 0
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
            res.append(ans)
        except ZeroDivisionError:
            print("division by 0")
            pass
        except TypeError:
            print("wrong type")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            res.append(0)
    return res
