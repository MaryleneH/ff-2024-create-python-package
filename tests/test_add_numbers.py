""""Test if add_numbers behaves correctly (as expected)"""

from mypackage_test.add_numbers import add_numbers

def test_add_numbers():
    """Test that the ouptut of the add numbers function is correct """
    assert add_numbers(1, 2) == 3