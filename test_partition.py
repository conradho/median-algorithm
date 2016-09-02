from hypothesis import given
from hypothesis.strategies import lists, integers, choices

from python_median import partition


@given(lists(integers(), min_size=1), choices())
def test_partition_splits_list_by_comparing_to_pivot(unordered_list, choice):
    pivot = choice(unordered_list)

    partitioned_list, pivot_index = partition(unordered_list, pivot)

    assert len(partitioned_list) == len(unordered_list)
    assert partitioned_list[pivot_index] == pivot

    for element in partitioned_list[:pivot_index]:
        assert element < pivot, 'found elements bigger than pivot before pivot'
    for element in partitioned_list[pivot_index:]:
        assert element >= pivot, 'found elements smaller than pivot after pivot'
