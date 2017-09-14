input_list = [3,4,2,7,8,101,1,67,41,69, 32, 24,12,67, 891, 111, 987, 345, 678,900, 1000,4,23]
#input_list = [3,4,2,9]


def bubble_sort(input_list):
    update = False
    total_length = len(input_list)-1
    for i in range(total_length):
        next_item = input_list[i+1]
        this_item = input_list[i]
        if this_item > next_item:
            input_list[i] = next_item
            input_list[i+1] = this_item
            update = True
    if not update:
        return input_list
    return bubble_sort(input_list)


def insertion_sort(input_list):
    total_length = len(input_list)-1
    for i in range(total_length):
        next_item = input_list[i+1]
        this_item = input_list[i]
        if this_item > next_item:
            input_list[i] = next_item
            input_list[i+1] = this_item
            return insertion_sort(input_list)
    return input_list


def selection_sort(input_list):
    total_length = len(input_list)
    for i in range(total_length):
        this_item = input_list[i]
        update = False
        for j in range(i+1, total_length):
            next_item = input_list[j]
            if next_item < this_item:
                input_list[i] = next_item
                input_list[j] = this_item
                this_item = next_item
                update = True
        if update:
            return selection_sort(input_list)
    return input_list


def merge_sort(input_list):
    def devide_data(input_list):
        total_length = len(input_list)
        left_part = total_length/2
        return input_list[0:left_part], input_list[left_part:]

    def merge_data(first_sort_list, second_sort_list):
        sorted_merged_list = []
        not_done = True
        while not_done:
            this_item = first_sort_list[0]
            to_check_item = second_sort_list[0]
            if this_item > to_check_item:
                sorted_merged_list.append(to_check_item)
                second_sort_list.pop(0)
            else:
                sorted_merged_list.append(this_item)
                first_sort_list.pop(0)
            if not first_sort_list and second_sort_list:
                sorted_merged_list.extend(second_sort_list)
                not_done = False
            elif first_sort_list and not second_sort_list:
                sorted_merged_list.extend(first_sort_list)
                not_done = False
        return sorted_merged_list

    def lest_node_sort(node):
        """
        """
        first_item = node[0]
        next_item = node[1]
        if first_item > next_item:
            return [next_item, first_item]
        return node

    def start_the_sorting(input_list):
        divided_list = []
        pending_list = [input_list]
        while pending_list:
            to_devide_list = pending_list.pop(0)
            left_part, right_part = devide_data(to_devide_list)
            if len(left_part) > 2:
                pending_list.insert(0, right_part)
                pending_list.insert(0, left_part)
            else:
                if len(left_part) == 2:
                    left_part = lest_node_sort(left_part)
                middle_part = []
                if len(right_part) == 3:
                    middle_part = lest_node_sort(right_part[:-1])
                    right_part = right_part[-1:]
                    right_part = merge_data(middle_part, right_part)
                elif len(right_part) == 2:
                    right_part = lest_node_sort(right_part)
                divided_list.append(left_part)
                divided_list.append(right_part)
        return divided_list

    tmp_sort = start_the_sorting(input_list)
    while len(tmp_sort) > 1:
        _sort_list = []
        for i in range((len(tmp_sort))/2):
            first_item = tmp_sort.pop(0)
            if tmp_sort:
                next_item = tmp_sort.pop(0)
            else:
                _sort_list.append(first_item)
                tmp_sort = _sort_list
                break
            sort_part = merge_data(first_item, next_item)
            _sort_list.append(sort_part)
        tmp_sort = _sort_list
    return tmp_sort[0]


def quick_sort(input_list):
    def get_pivot_index(input_list, pivot_index=0):
        pivot_value = input_list[0]
        left_index = 1
        right_index = len(input_list)-1
        crossed = False
        while not crossed:
            left_value = input_list[left_index]
            right_value = input_list[right_index]
            if left_value > pivot_value:
                input_list.pop(left_index)
                input_list.insert(right_index, left_value)
                right_index = right_index-1
            elif right_value < pivot_value:
                input_list.pop(right_index)
                input_list.insert(left_index, right_value)
                left_index = left_index+1
            else:
                right_index = right_index-1
                left_index = left_index+1
            if left_index > right_index:
                input_list.pop(pivot_index)
                return input_list[0:left_index-1], input_list[left_index-1:], pivot_value
                input_list.insert(left_index-1, pivot_value)
                crossed = True

        return input_list

    def start_the_process(input_list):
        """
        """
        out_list = [input_list]
        i = 0
        while i < len(out_list):
            to_sort = out_list[i]
            if isinstance(to_sort, list):
                left_partation, right_partation, pivot = get_pivot_index(to_sort)
                out_list.remove(to_sort)
                pivot_index = i+1
                if len(left_partation) > 1:
                    out_list.insert(i, left_partation)
                elif len(left_partation) == 1:
                    out_list.insert(i, left_partation[0])
                else:
                    pivot_index = i
                out_list.insert(pivot_index, pivot)
                if len(right_partation) > 1:
                    out_list.insert(pivot_index+1, right_partation)
                elif len(right_partation) == 1:
                    out_list.insert(pivot_index+1, right_partation[0])
            else:
                i += 1
        return out_list
    return start_the_process(input_list)


def heap_sort(input_list):
    def make_the_tree(input_list):
        tree_dict = {}
        i = 0
        max_key = 0
        data_len = len(input_list)
        
        if data_len > 2:
            while i < data_len-2:
                if i == data_len-2:
                    if input_list[i] > input_list[i+1]:
                        tree_dict[input_list[i]] = [input_list[i+1]]
                        if input_list[i] > max_key:
                            max_key = input_list[i]
                    else:
                        tree_dict[input_list[i+1]] = [input_list[i]]
                        if input_list[i+1] > max_key:
                            max_key = input_list[i+1]
                else:
                    if input_list[i] > input_list[i+1] and input_list[i] > input_list[i+2]:
                        tree_dict[input_list[i]] = [input_list[i+1], input_list[i+2]]
                        if input_list[i] > max_key:
                            max_key = input_list[i]
                    elif input_list[i+1] > input_list[i] and input_list[i+1] > input_list[i+2]:
                        tree_dict[input_list[i+1]] = [input_list[i], input_list[i+2]]
                        if input_list[i+1] > max_key:
                            max_key = input_list[i+1]
                    elif input_list[i+2] > input_list[i] and input_list[i+2] > input_list[i+1]:
                        tree_dict[input_list[i+2]] = [input_list[i], input_list[i+1]]
                        if input_list[i+2] > max_key:
                            max_key = input_list[i+2]
                i += 1
        else:
            first_item = input_list[0]
            next_item = input_list[1]
            if first_item > next_item:
                return first_item
            return next_item
        return max_key

    def start_the_process(input_list):
        out_list = []
        input_len = len(input_list)
        while len(out_list) != input_len:
            tree_data = make_the_tree(input_list)
            out_list.insert(0, tree_data)
            input_list.remove(tree_data)
            if len(input_list) == 1:
                out_list.insert(0, input_list[0])
        return out_list
    return start_the_process(input_list)


print heap_sort(input_list)
