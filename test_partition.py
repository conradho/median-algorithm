from hypothesis import given
from hypothesis.strategies import lists, integers, choices

from python_median import partition


@given(lists(integers(), min_size=1), choices())
def test_partition_splits_list_by_comparing_to_pivot(unordered_list, choice):
    pivot = choice(unordered_list)

    partitioned_list = partition(unordered_list, pivot)

    assert len(partitioned_list) == len(unordered_list)

    before_pivot = True
    for element in partitioned_list:
        if element == pivot:
            before_pivot = False
        if before_pivot:
            assert element < pivot, 'found elements bigger than pivot before pivot'
        else:
            assert element >= pivot, 'found elements smaller than pivot after pivot'
