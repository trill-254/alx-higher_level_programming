#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if t == search else t for t in my_list]
