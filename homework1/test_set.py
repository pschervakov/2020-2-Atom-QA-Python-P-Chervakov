import pytest


def test_add():
    sset = {1, 2, 3}
    sset.add(4)
    assert sset == {1, 3, 2, 4}


def test_contain():
    sset = {1, 2, 3}
    assert 1 in sset
    assert 4 not in sset


class TestSetSpecific:

    @pytest.mark.parametrize('set1, set2,intersection', [({1, 4, 6}, {2, 1, 4}, {1, 4}), ({1, 2}, {3}, set())])
    def test_intersection(self, set1, set2, intersection):
        assert set1.intersection(set2) == intersection

    def test_union(self):
        set1 = {1, 2}
        set2 = {3, 4}
        assert set1.union(set2) == {1, 2, 3, 4}


def test_clear():
    set1 = {1, 2, 3, 4}
    set1.clear()
    assert set1 == set()
    set2 = set()
    set2.clear()
    assert set2 == set()
