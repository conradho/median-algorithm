
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

def get_kth_element(unordered_list, kth, left_index, right_index):
    if left_index == right_index:
        return unordered_list[left_index]

