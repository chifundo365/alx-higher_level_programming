#!/user/bin/python
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if idx < 0 or idx > len(my_list) - 1:
            return my_list.copy()
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
