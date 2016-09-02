from collections import namedtuple
from hypothesis import given
from hypothesis.strategies import lists, integers, composite

from python_median import partition


@composite
def partition_params(draw):
    # use named tuples so errors are more readable
    PartitionParams = namedtuple('PartitionParams', 'xs index left right')
    xs = draw(lists(integers(), min_size=1))
    max_index = len(xs) - 1
    left_bound = draw(integers(min_value=0, max_value=max_index))
    pivot_index = draw(integers(min_value=left_bound, max_value=max_index))
    right_bound = draw(integers(min_value=pivot_index + 1, max_value=len(xs)))
    return PartitionParams(
        xs=xs, index=pivot_index, left=left_bound, right=right_bound
    )

@given(partition_params())
def test_does_not_change_elements_outside_of_bounds(hypothesis_test_case):
    unordered_list, pivot_index, left_bound, right_bound = hypothesis_test_case
    partitioned_list, _ = partition(unordered_list, pivot_index, left_bound, right_bound)

    assert partitioned_list[:left_bound] == unordered_list[:left_bound]
    assert partitioned_list[right_bound:] == unordered_list[right_bound:]

@given(partition_params())
def test_returns_correct_new_pivot_position(hypothesis_test_case):
    unordered_list, pivot_index, left_bound, right_bound = hypothesis_test_case
    partitioned_list, new_pivot_index = partition(unordered_list.copy(), pivot_index, left_bound, right_bound)
    pivot_value = unordered_list[pivot_index]

    assert partitioned_list[new_pivot_index] == pivot_value

@given(partition_params())
def test_is_not_missing_elements(hypothesis_test_case):
    unordered_list, pivot_index, left_bound, right_bound = hypothesis_test_case
    partitioned_list, _ = partition(unordered_list.copy(), pivot_index, left_bound, right_bound)

    assert len(partitioned_list) == len(unordered_list)


@given(partition_params())
def test_splits_list_by_comparing_to_pivot(hypothesis_test_case):
    unordered_list, pivot_index, left_bound, right_bound = hypothesis_test_case
    partitioned_list, new_pivot_index = partition(unordered_list.copy(), pivot_index, left_bound, right_bound)
    pivot_value = unordered_list[pivot_index]

    for element in partitioned_list[left_bound:new_pivot_index]:
        assert element < pivot_value, 'found elements bigger than pivot before pivot'
    for element in partitioned_list[new_pivot_index:right_bound]:
        assert element >= pivot_value, 'found elements smaller than pivot after pivot'
