import pytest


class TestPop():

    def test_pop(self):
        dic = {'1': 1, '2': 2, '3': 3}
        dic.pop('2')
        assert dic == {'1': 1, '3': 3}
        with pytest.raises(KeyError):
            assert dic.pop('4')

    def test_popitem(self):
        dict1 = {i: i for i in range(100)}
        dict2 = dict(dict1)
        dict2[100] = 2
        dict2.popitem()
        assert dict2 == dict1


@pytest.mark.parametrize('dic,test_input,test_expected', [({1: 1, 2: 4, 3: 6}, 2, 4), ({1: 1, 2: 4, 3: 6}, 3, 6)])
def test_get(dic, test_input, test_expected):
    assert dic[test_input] == test_expected


def test_copy():
    dict1 = {'1': 1, '2': 2, '3': 3}
    dict2 = dict1.copy()
    assert dict1 == dict2


def test_keys():
    dic = {'1': 1, '2': 2, '3': 3}
    assert list(dic.keys()) == ['1', '2', '3']
