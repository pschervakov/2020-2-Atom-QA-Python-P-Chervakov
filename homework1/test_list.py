import pytest


@pytest.fixture()
def generate_list():
    lst = [1, 3, 7, 4, 8]
    return lst


def test_contain(generate_list):
    lst = generate_list
    assert 1 in lst
    assert 2 not in lst


def test_append(generate_list):
    lst = generate_list
    lst.append(2)
    assert lst == [1, 3, 7, 4, 8, 2]


class TestRemove:

    def test_remove(self, generate_list):
        lst = generate_list
        lst.remove(1)
        assert lst == [3, 7, 4, 8]

    def test_remove_negative(self, generate_list):
        lst = generate_list
        with pytest.raises(ValueError):
            assert lst.remove(2)


def test_sort():
    lst = [1, 6, 7, 4, 8]
    lst.sort()
    assert lst == [1, 4, 6, 7, 8]
    lst = []
    lst.sort()
    assert lst == []


@pytest.mark.parametrize('lst,test_input,test_expected', [([1, 2, 3, 4], 0, 1), ([1, 2, 3, 4], -1, 4)])
def test_get(lst, test_input, test_expected):
    assert lst[test_input] == test_expected
