def flatten(my_list):
    my_clean_list = []
    for item in my_list:
        if len(item) > 1:
            my_clean_list.append(flatten(item))
        else:
            my_clean_list.append(item)
    return my_clean_list