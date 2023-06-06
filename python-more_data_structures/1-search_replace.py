#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    search = str(search)
    replace = str(replace)
    new_list = list(map(lambda x: str(x).replace(search, replace), new_list))
    new_list = list(map(int, new_list))
    return new_list
