#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum({t for t in my_list if isinstance(t, int)})
