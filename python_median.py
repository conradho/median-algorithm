
def partition(unordered_list, pivot_index, left_bound, right_bound):
    # make sure we have pivot inside of left/right bound
    assert 0 <= left_bound <= pivot_index < right_bound <= len(unordered_list)

    left = []
    pivot = unordered_list[pivot_index]
    right = []

    for i, element in enumerate(unordered_list):
        if i < left_bound:
            left.append(element)
        elif i >= right_bound:
            right.append(element)
        elif i == pivot_index:
            continue
        elif element < pivot:
            left.append(element)
        else:
            right.append(element)

    pivot_index = len(left)

    return (left + [pivot] + right, pivot_index)


def get_kth_element(unordered_list, kth, search_from, search_to):
    assert 0 <= search_from <= kth < search_to <= len(unordered_list)

    if search_from == search_to - 1:
        return unordered_list[search_from]

    # we will be smarter about choosing pivot index later
    pivot_index = search_from

    new_unordered_list, new_pivot_index = partition(unordered_list, pivot_index, search_from, search_to)

    if new_pivot_index == kth:
        return new_unordered_list[kth]

    if new_pivot_index > kth:
        search_to = new_pivot_index
    else:
        search_from = new_pivot_index + 1

    return get_kth_element(new_unordered_list, kth, search_from, search_to)

