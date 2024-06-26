"""Complete Tests for PlaceCollection class."""

from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    new_place = Place("Smithfield", "Australia", 5, False)
    place_collection.add_place(new_place)
    new_place.not_visited()
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    # Test sorting by visit-status
    print("Test sorting - visit-status:")
    place_collection.sort("is_visited")
    print(place_collection)

    # Test sorting by country
    print("Test sorting - country:")
    place_collection.sort("country")
    print(place_collection)

    # Test sorting by name
    print("Test sorting - name:")
    place_collection.sort("name")
    print(place_collection)

    # Test sorting by country then priority
    print("Test sorting - country then priority:")
    place_collection.sort("country", "priority")
    print(place_collection)

    # Test sorting by name then priority
    print("Test sorting - name then priority:")
    place_collection.sort("name", "priority")
    print(place_collection)

    # Test saving places (check CSV file manually to see results)
    # print("Test save place collection:")
    # place_collection.save_places('places.csv')

    # Add more tests, as appropriate, for each method
    print("Test add unvisited places:")
    print(place_collection.add_unvisited_places())

    # test string representation of list of class objects
    print("Test __repr__:")
    print(place_collection.__repr__())


run_tests()
