from utils import division

#
# def test_division_good():
#     assert division(10, 2) == 5
#
#
# def test_division_one():
#     assert division(10, 5) == 2
#
#
# def test_division_two():
#     assert division(20, 2) == 10
#
#
# def test_division_three():
#     assert division(-6, 3) == -2

import pytest

test_list = [(10, 2, 5),
             (20, 10, 2),
             (40, -5, -8),
             (5, 2, 2.5)]


@pytest.mark.parametrize('a, d, expected_result', test_list)
def test_division_good(a, d, expected_result):
    assert division(a, d) == expected_result


# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         division(10, 0)
# def test_type_error():
#     with pytest.raises(TypeError):
#         division(10, '2')

new_list = [(ZeroDivisionError, 10, 0),
            (TypeError, 20, '2')]


@pytest.mark.parametrize('expected_exception, divisionable, divider', new_list)
def test_division_test_error(expected_exception, divisionable, divider):
    with pytest.raises(expected_exception):
        division(divisionable, divider)
