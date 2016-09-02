from python_median import get_kth_element


def test_median_works_for_single_item():
    assert get_kth_element([1], 0) ==  1
