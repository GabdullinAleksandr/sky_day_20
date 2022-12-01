from day_20.code import get_val, set_
import pytest

@pytest.fixture
def coll():
    return {"a": {"b": {"c": 3}}}


def test_get_val_first():
    assert get_val({'sky': 'pro'}, 'sky') == 'pro'


def test_get_val_second():
    assert get_val({}, 'sky', 'NOO') == 'NOO'


def test_get_val_third():
    assert get_val({'sky': 'pro'}, '', 'NOO') == 'NOO'
    assert get_val({'': ''}, '', '') == ''
    assert get_val({'sky': ''}, 'sky', 'NOO') == ''


def test_set__first(coll):
    coll = set_(coll, ["a", "b", "c"], 4)
    assert coll["a"]["b"]["c"] == 4


def test_set__second(coll):
    coll = set_(coll, ['x', 'y', 'z'], 5)
    assert coll['x']['y']['z'] == 5


def test_set__third(coll):
    coll = set_(coll, ["a", "b", "c", "d", "e"], 100)
    assert coll["a"]["b"]["c"]["d"]["e"] == 100


def test_set__fourth(coll):
    coll = set_(coll, [''], 100)
    assert coll[''] == 100


def test_set__fifth(coll):
    assert set_(coll, '', 100) == 'TypeError'
