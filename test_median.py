from hypothesis import given
from hypothesis.strategies import lists, integers

from python_median import get_kth_element

def test_median_works_for_single_item():
    assert get_kth_element([1], 0) ==  1

@given(lists(integers(), min_size=1))
def test_median_works(nonempty_list_of_integers):
    sorted_list = sorted(nonempty_list_of_integers)
    for kth, element in enumerate(sorted_list):
        kth_element = get_kth_element(nonempty_list_of_integers, kth)
        assert  kth_element == element, 'The element returned at index {} is wrong'.format(kth)
