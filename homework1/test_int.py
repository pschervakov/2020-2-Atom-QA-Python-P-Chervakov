import pytest


class TestDivision:

    def test_division(self):
        assert 3 / 2 == 1.5
        assert -3 / 2 == -1.5
        assert 3 / -2 == -1.5
        assert 0 / 1 == 0
        with pytest.raises(ZeroDivisionError):
            assert 1 / 0
            assert 0 / 0

    def test_integer_and_modulo_division(self):
        assert 7 // 3 == 2

        assert 7 % 2 == 1
        with pytest.raises(ZeroDivisionError):
            assert 1 // 0
            assert 1 % 0
            assert 0 // 0
            assert 0 % 0


@pytest.mark.parametrize('number1, number2, result', [(1, 3, 3), (0, 7, 0), (3, 4, 12), (-3, 4, -12), (-3, -4, 12)])
def test_multiple(number1, number2, result):
    assert number1 * number2 == result


@pytest.mark.parametrize('number1, number2, result',
                         [(1, 10, 1), (10, 1, 10), (10, 0, 1), (0, 0, 1), (3, 4, 81), (4, 0.5, 2)])
def test_exponentiation(number1, number2, result):
    assert number1 ** number2 == result


def test_sum_and_substract():
    assert 2 + 2 == 4
    assert 2 + 0 == 2
    assert -2 + 4 == 2
    assert 4 - 2 == 2
