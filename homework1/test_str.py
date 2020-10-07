import pytest


@pytest.mark.parametrize('str1, str2,result',
                         [('ab', 'cd', 'abcd'), ('', 'ab', 'ab'), ('', '', '')])
def test_concat(str1, str2, result):
    assert str1 + str2 == result


@pytest.mark.parametrize('str1, number,result',
                         [('ab', 0, ''), ('ab', 1, 'ab'), ('ab', 2, 'abab')])
def test_multiple(str1, number, result):
    assert str1 * number == result


class TestReplace():
    def test_immutability(self):
        with pytest.raises(TypeError):
            s = 'abc'
            s[0] = 'd'

    def test_replace_function(self):
        errors = []
        s = 'abcdcef'
        if s.replace('c', 'g') != 'abgdgef':
            errors.append('replace does not work')
        if s.replace('c', 'g', 1) != 'abgdcef':
            errors.append('replace with maxcount does not work')
        if s.replace('k', 'g') != 'abcdcef':
            errors.append('replace with no matches does not work')
        assert not errors


def test_find():
    s = 'abcd'
    assert s.find('a') == 0
    assert s.find('e') == -1
