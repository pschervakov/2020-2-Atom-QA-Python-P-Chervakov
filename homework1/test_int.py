import pytest


class TestDivision:

    def test_division(self):
        assert 3 / 2 == 1.5
        assert -3 / 2 == -1.5
        assert 3 / -2 == -1.5
        assert 0 / 1 == 0

    def test_integer_division(self):
        assert 7 // 3 == 2
        assert 0 // 3 == 0

    def test_modulo_division(self):
        assert 7 % 2 == 1
        assert 0 % 2 == 0

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
        with pytest.raises(ZeroDivisionError):
            0 / 0

    def test_modulo_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            1 % 0
        with pytest.raises(ZeroDivisionError):
            0 % 0

    def test_integer_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            1 // 0
        with pytest.raises(ZeroDivisionError):
            0 // 0


@pytest.mark.parametrize('number1, number2, result', [(1, 3, 3), (0, 7, 0), (3, 4, 12), (-3, 4, -12), (-3, -4, 12)])
def test_multiple(number1, number2, result):
    assert number1 * number2 == result


@pytest.mark.parametrize('number1, number2, result',
                         [(1, 10, 1), (10, 1, 10), (10, 0, 1), (0, 0, 1), (3, 4, 81), (4, 0.5, 2)])
def test_exponentiation(number1, number2, result):
    assert number1 ** number2 == result


@pytest.mark.parametrize('number1, number2, result', [(2, 2, 4), (2, 0, 2), (-2, 4, 2), (4, -2, 2)])
def test_sum_and_substract(number1,number2, result):
    assert number1 + number2 == result
