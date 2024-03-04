"""Complete Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    true_place = Place("Malagar", "Spain", 1, True)

    # Write tests to show this initialisation works
    print(new_place.__str__())
    print(true_place.__str__())

    # Add more tests, as appropriate, for each method
    print("Test mark False as unvisited:")
    print(new_place.not_visited())
    print(new_place.__str__())

    print("Test mark True as visited:")
    print(true_place.visited())  # convert True to v
    print(true_place.__str__())
    print(new_place.is_important())


run_tests()
