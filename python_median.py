
def partition(unordered_list, pivot_value):
    # this needs to be linear time
    # currently O(2n) if all elements in the right

    left = []
    right = []
    found_pivot = False

    for element in unordered_list:
        if element < pivot_value:
            left.append(element)
        elif not found_pivot and element == pivot_value:
            found_pivot = True
        else:
            right.append(element)

    # yay len() is O(1)
    pivot_index = len(left)

    return (left + [pivot_value] + right, pivot_index)

def get_kth_element(unordered_list, kth, left_index, right_index):
    if left_index == right_index:
        return unordered_list[left_index]

