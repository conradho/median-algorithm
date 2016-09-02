from collections import namedtuple
from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import lists, integers, composite

from python_median import get_kth_element

@composite
def get_kth_element_params(draw):
    # use named tuples so errors are more readable
    GetKthParams = namedtuple('GetKthParams', 'xs kth search_from search_to')
    xs = draw(lists(integers(), min_size=1))
    max_index = len(xs) - 1
    search_from = draw(integers(min_value=0, max_value=max_index))
    kth = draw(integers(min_value=search_from, max_value=max_index))
    search_to = draw(integers(min_value=kth + 1, max_value=len(xs)))
    return GetKthParams(
        xs=xs, kth=kth, search_from=search_from, search_to=search_to
    )

@given(lists(integers(), min_size=1))
def test_recursion_base_case(random_list):
    # we have narrowed down the search space after many iterations
    kth = 0
    assert get_kth_element(random_list, kth=kth, search_from=kth, search_to=kth + 1) == random_list[kth]


@given(get_kth_element_params())
def test_fast_return_if_lucky_and_pivot_is_kth(hypothesis_test_case):
    unordered_list, kth, search_from, search_to = hypothesis_test_case

    with patch('python_median.partition') as mock_partition:
        # we get lucky and partitioning finds pivot that is kth element
        mock_partition.return_value = unordered_list, kth
        result = get_kth_element(
            unordered_list, kth=kth, search_from=search_from, search_to=search_to
        )
    assert result == unordered_list[kth]


@given(get_kth_element_params())
def test_median_finds_median(hypothesis_test_case):
    unordered_list, kth, _, __ = hypothesis_test_case

    for kth, element in enumerate(sorted(unordered_list)):
        kth_element = get_kth_element(unordered_list.copy(), kth, 0, len(unordered_list))
        assert kth_element == element, 'The element returned at index {} is wrong'.format(kth)

