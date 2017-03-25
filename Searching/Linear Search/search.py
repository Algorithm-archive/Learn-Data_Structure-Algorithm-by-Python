def linearSearch(item, item_list):
    for index, val in enumerate(item_list):
        if val == item:
            return True #You can return the index of the found element by 'return index'
    return False
