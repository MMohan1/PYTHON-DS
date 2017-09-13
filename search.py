input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 23, 55, 78, 90]
def binary_search(input_list, search_item, found_index=0):
    total_rec = len(input_list)
    first_half, last_half = input_list[:total_rec/2], input_list[total_rec/2:]
    if first_half:
        first_half_last_item = first_half[-1]
    else:
        first_half_last_item = last_half[-1]
    if first_half_last_item == search_item:
        return "Found", found_index + total_rec/2
    elif first_half_last_item < search_item and last_half:
        found_index += total_rec/2
        return binery_search(last_half, search_item, found_index)
    elif first_half_last_item > search_item and first_half:
        return binery_search(first_half, search_item, found_index)
    else:
        return "Not Found"
    


print binary_search(input_list, 7)
