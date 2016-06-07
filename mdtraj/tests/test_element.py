from mdtraj import element
from mdtraj.testing import assert_raises


def test_immutable():
    def f():
        element.hydrogen.mass = 1
    def g():
        element.radium.symbol = 'sdfsdfsdf'
    def h():
        element.iron.name = 'sdfsdf'

    assert_raises(AttributeError, f)
    assert_raises(AttributeError, g)
    assert_raises(AttributeError, h)
    assert element.hydrogen.mass == 1.007947
    assert element.radium.symbol == 'Ra'
    assert element.iron.name == 'iron'


def test_element_guessing():
    assert element.get_by_symbol('C5') == element.carbon
    assert element.get_by_symbol('H5T') == element.hydrogen
    assert element.get_by_symbol('C1*') == element.carbon
    assert element.get_by_symbol("H2'1") == element.hydrogen
    assert element.get_by_symbol("O1P") == element.oxygen
    assert element.get_by_symbol("H62") == element.hydrogen
    assert element.get_by_symbol("asdfasd") == element.virtual_site

    # This is the current expected behavior.
    assert element.get_by_symbol("Ca") == element.carbon
